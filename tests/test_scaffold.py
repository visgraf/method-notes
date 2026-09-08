"""Scaffold guards. Infrastructure -- these pin the repository's shape, not any
result about the subject matter.

Two of the rules in CLAUDE.md are stated as enforced. This is where they are
enforced, so that "CI enforces that" is a true sentence rather than an intention:

* nothing in the library or in experiments may import from ``spikes/``;
* nothing in the repository may reach into the reference checkouts.

WHY THESE ARE TESTS AND NOT PARAGRAPHS. Both rules are stated in prose elsewhere,
and prose has nothing to fail against. The spikes rule in particular is the one
that makes the low-ceremony lane safe: a directory with no tests and no review is
harmless until something with tests and review imports from it, and the first
such import never announces itself as the moment the rule stopped holding.

The instance this template came from shipped a third guard here, pinning a
project-specific layout decision (a flat package, no per-layer subpackages, taken
on a measured argument about that project's predecessor). It is NOT carried: the
template has no such decision, and shipping the guard without the decision would
present a rule as tested practice when nothing here has exercised it. If you take
a structural decision, add its guard beside these -- that is the pattern worth
carrying, not the particular decision.
"""

import ast
import pathlib

import pytest

pytestmark = pytest.mark.infrastructure

REPO = pathlib.Path(__file__).resolve().parents[1]

# RENAME THIS to your package, and rename src/research/ with it. It is a single
# constant on purpose: the guards below are generic, and this is the only line in
# the file that knows what the project is called.
PACKAGE = "research"

# Built by concatenation rather than written literally, so that the scan below
# can cover *this* file too instead of having to exempt its own needle.
REFERENCE_DIR = "." + "reference"

# Directories whose code must stay free of both.
GOVERNED = ("src", "tests", "experiments")


def _python_files(*roots: str) -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for root in roots:
        base = REPO / root
        if base.is_dir():
            out.extend(sorted(base.rglob("*.py")))
    return out


def test_package_imports() -> None:
    """The library imports and states its public surface.

    Thin on purpose while the package is empty -- but not skipped, because a
    skipped test is a test that cannot fail. As the package grows, assert the
    names it exports here: the point is that the public surface is stated
    somewhere a change has to pass through.
    """
    package = __import__(PACKAGE)

    assert hasattr(package, "__all__"), f"{PACKAGE}.__all__ states the public surface"
    assert sorted(package.__all__) == package.__all__, "__all__ is kept sorted"


def test_governed_trees_do_not_import_spikes() -> None:
    """A spike's only permitted output is a decision or a deletion.

    Neither of those is "the library grew a dependency on it". Parsed rather than
    grepped, so a mention in a docstring or a comment does not trip it and a real
    import cannot hide behind formatting.
    """
    offenders: list[str] = []
    for path in _python_files(*GOVERNED):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            else:
                continue
            for name in names:
                if name == "spikes" or name.startswith("spikes."):
                    offenders.append(f"{path.relative_to(REPO)}:{node.lineno} imports {name}")
    assert not offenders, "spikes/ must not be importable by the library:\n" + "\n".join(offenders)


def test_nothing_reaches_into_the_reference_checkouts() -> None:
    """The references are read by people, never by code.

    They are pinned clones of other repositories, they are git-ignored, and they
    are not present in CI. Any code path that reads one passes locally and fails
    everywhere else, which is the worst available failure mode.
    """
    offenders: list[str] = []
    for path in _python_files(*GOVERNED):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if REFERENCE_DIR in line and "REFERENCE_DIR" not in line:
                offenders.append(f"{path.relative_to(REPO)}:{lineno}")
    assert not offenders, "code must not reference the pinned clones:\n" + "\n".join(offenders)


def test_every_experiment_has_a_preregistration() -> None:
    """A preregistration is written and committed BEFORE the runner exists.

    NOT CARRIED FROM THE SOURCE INSTANCE. That project wrote a preregistration
    first for all thirteen of its experiments and never enforced it in CI, so
    this guard is an addition and has not been exercised by anything. It is here
    because the practice was exercised heavily and the enforcement is cheap;
    delete it if it gets in the way, and record why.

    This guard cannot check the ORDER -- that is what the commit history is for,
    and experiments/exp000_example/README.md explains why the order is the whole
    point. What it can check is the weaker, still useful thing: that no
    experiment directory acquires a runner or results without one.

    A directory with results and no preregistration is the shape of an experiment
    whose criterion was chosen after the numbers were seen, and that is not a
    thing anyone does deliberately -- it is a thing that happens when a question
    turns into a run without passing through a written threshold.
    """
    root = REPO / "experiments"
    if not root.is_dir():
        pytest.skip("no experiments/ directory yet")

    offenders: list[str] = []
    for directory in sorted(p for p in root.iterdir() if p.is_dir()):
        if directory.name.startswith((".", "__")):
            continue
        has_work = any((directory / name).exists() for name in ("run.py", "results.json"))
        if has_work and not (directory / "preregistration.md").exists():
            offenders.append(directory.name)
    assert not offenders, "experiments with work and no preregistration:\n" + "\n".join(offenders)
