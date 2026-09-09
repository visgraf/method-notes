"""Scaffold guards. Infrastructure -- these pin the repository's shape, not any
claim about the subject matter.

RESTORED WITH tools/md2tex.py, in the order fc-003's scope required: "stops
holding the moment any .py file lands: restore the [pinned-clone] guard first,
before the others." That guard is first in this file for that reason and for no
other. The bracket is a substitution -- fc-003 names the directory literally and
this file may not, because the guard below scans this file for that string.

WHAT IS NOT CARRIED BACK, and why, so nobody restores it out of habit:

* the spikes/ import ban -- there is no spikes/ (fc-004);
* the package-imports guard -- there is no package (fc-003 stands for src/);
* the every-experiment-has-a-preregistration guard -- there are no experiments.

Restoring a guard whose subject does not exist would make it pass by scanning an
empty set, which is the shape of a check that cannot fail. Two guards have a
subject here, and both are below.
"""

import pathlib
import subprocess
import sys
import tempfile

import pytest

pytestmark = pytest.mark.infrastructure

REPO = pathlib.Path(__file__).resolve().parents[1]

# Built by concatenation rather than written literally, so the scan below can
# cover *this* file too instead of having to exempt its own needle.
REFERENCE_DIR = "." + "reference"

# Directories whose code must stay free of it. There is no src/ and no
# experiments/ in this repository; tools/ and tests/ are where code lives.
GOVERNED = ("tools", "tests")


def _python_files(*roots: str) -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for root in roots:
        base = REPO / root
        if base.is_dir():
            out.extend(sorted(base.rglob("*.py")))
    return out


def test_nothing_reaches_into_the_reference_checkouts() -> None:
    """The references are read by people, never by code.

    They are pinned clones of other repositories, they are git-ignored, and they
    are absent in CI. Any code path that reads one passes locally and fails
    everywhere else, which is the worst available failure mode -- and this
    repository has now had that failure once for real, in the ledger check that
    passed on Psych 3 and failed on Psych 4 (od-004). The guard is cheap and the
    failure it prevents is not.

    THIS IS THE GUARD fc-003 NAMED AS THE ONE TO RESTORE FIRST. Every claim in
    report/claims-verified.md is resolved against those clones by a person
    reading them; the moment code reads one instead, the verification becomes
    unreproducible for anyone who does not have them on disk.
    """
    offenders: list[str] = []
    for path in _python_files(*GOVERNED):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if REFERENCE_DIR in line and "REFERENCE_DIR" not in line:
                offenders.append(f"{path.relative_to(REPO)}:{lineno}")
    assert not offenders, "code must not reference the pinned clones:\n" + "\n".join(offenders)


def test_typeset_sections_match_the_draft() -> None:
    """report/sections/*.tex are generated from report/draft.md, and this proves it.

    THE CLAIM THIS TESTS WAS PREVIOUSLY A COMMENT. report/main.tex says the .tex
    is generated from the draft and that the diff between them is where a mangled
    figure shows. Nothing checked it, so an edit made directly to a .tex would
    have silently broken the correspondence the whole draft/typeset practice
    depends on -- and the next regeneration would have thrown that edit away
    without telling anyone.

    It regenerates into a temporary directory and compares bytes. It does not
    write to report/sections/, so a failing test never "fixes" itself.
    """
    with tempfile.TemporaryDirectory() as tmp:
        result = subprocess.run(
            [sys.executable, str(REPO / "tools" / "md2tex.py"), "--out", tmp],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"conversion failed:\n{result.stdout}\n{result.stderr}"

        generated = sorted(pathlib.Path(tmp).glob("*.tex"))
        committed = sorted((REPO / "report" / "sections").glob("*.tex"))
        assert [p.name for p in generated] == [p.name for p in committed], (
            "the set of section files differs from what the converter produces"
        )

        stale = [
            g.name
            for g, c in zip(generated, committed, strict=True)
            if g.read_bytes() != c.read_bytes()
        ]
        assert not stale, (
            "report/sections/ is out of date with report/draft.md: "
            + ", ".join(stale)
            + "\nRun `make -C report sections` and commit the result."
        )
