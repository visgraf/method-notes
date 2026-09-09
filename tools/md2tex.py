"""Convert report/draft.md into report/sections/*.tex.

WHY THIS FILE IS IN THE REPOSITORY, AND WHAT IT COST TO PUT IT HERE.
report/main.tex says the .tex files are generated from the draft and that the
diff between the two is where a mangled figure shows. That was true and
unverifiable at the same time: the converter lived outside the tree, so the
regeneration a reader is told to perform could not be performed by them.
Recorded as od-007 and closed by committing this.

IT REOPENED TWO FORECLOSURES TO GET HERE. fc-003 anticipated exactly this --
"stops holding the moment any .py file lands: restore the [pinned-clone] guard
first, before the others" -- and that order was followed. (The bracket is a
substitution: fc-003 names the directory literally, and this file may not, because
the guard it is quoting scans this file for exactly that string. The guard is
crude on purpose and prose bends around it, not the other way round.) fc-002 did not: its
scope named a GENERATED FIGURE as the trigger that would bring pyproject.toml
back, and the actual trigger was a converter. Both entries are annotated in
docs/state.yaml rather than reversed.

RUN IT:  make -C report sections

IT IS NOT PART OF THE PDF BUILD, deliberately. report/sections/*.tex are
COMMITTED, so `make -C report` compiles from a clean checkout with a TeX
installation alone and no language runtime -- the property
.github/workflows/report.yml depends on. This script regenerates them; it never
runs during a build. Same arrangement report/figures/README.md prescribes for
figures, and for the same reason.

DETERMINISTIC AND ENFORCED. tests/test_scaffold.py regenerates into a temporary
directory and asserts the result is byte-identical to what is committed, so "the
.tex is generated from the draft" is a tested claim rather than a comment. Edit
the draft, re-run this, commit both.

STANDARD LIBRARY ONLY. No markdown or LaTeX dependency, so pyproject.toml can
stay dependency-free.
"""

from __future__ import annotations

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]

SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

SECTION_FILES = (
    "01-what-this-is",
    "02-the-setting",
    "03-the-project",
    "04-how-it-goes-wrong",
    "05-what-it-cost",
    "06-where-it-failed",
    "07-the-template",
    "08-reflection",
    "09-appendix-availability",
)

# Characters that must never reach the output. Each one renders wrongly or not at
# all, and each has been seen doing so: the straight double quote shipped into a
# built PDF as two right-facing marks, inside a verbatim quotation.
FORBIDDEN = (
    ('"', "straight double quote (LaTeX renders it as two RIGHT marks)"),
    ("\u201c", "unconverted left curly quote"),
    ("\u201d", "unconverted right curly quote"),
    ("\u2014", "unconverted em dash"),
    ("\u2013", "unconverted en dash"),
    ("\u00a7", "unconverted section mark"),
)

HEADING_NUMBER = re.compile(r"^(?:Appendix\s+[A-Z]|\d+(?:\.\d+)?)\.?\s+")
HEADING = re.compile(r"^(#{1,3})\s+(.*)$")
BULLET = re.compile(r"^\s*[-*]\s+")
LEVELS = {1: "section", 2: "subsection", 3: "subsubsection"}


def escape(text: str) -> str:
    return "".join(SPECIALS.get(char, char) for char in text)


def typography(text: str) -> str:
    """Unicode and straight quotes to their LaTeX forms.

    Straight double quotes are paired here. LaTeX renders `"` as two RIGHT-facing
    marks, so an opening straight quote points the wrong way -- and it does so
    inside verbatim quotations, which is where it is most visible and least
    excusable. Curly quotes were handled from the first version and straight ones
    were not, because Markdown renders both identically and the exceptions were
    invisible at the source. Pairing here leaves only a genuinely unbalanced
    quote for the guard in `main` to catch.
    """
    text = (
        text.replace("\u2014", "---")
        .replace("\u2013", "--")
        .replace("\u00a7", r"\S")
        .replace("\u201c", "``")
        .replace("\u201d", "''")
    )
    return re.sub(r'"([^"]*)"', r"``\1''", text)


def inline(text: str) -> str:
    """Inline markup. Code spans are stashed first, so nothing rewrites inside them."""
    code: list[str] = []

    def stash(match: re.Match[str]) -> str:
        code.append(match.group(1))
        return f"\0{len(code) - 1}\0"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text, flags=re.S)
    text = re.sub(r"(?<![*\w])\*([^*\n]+?)\*(?!\*)", r"\\textit{\1}", text)
    text = typography(text)
    for index, span in enumerate(code):
        text = text.replace(f"\0{index}\0", rf"\texttt{{{typography(escape(span))}}}")
    return text


def _quote(lines: list[str], start: int) -> tuple[list[str], int]:
    index = start
    block: list[str] = []
    while index < len(lines) and (
        lines[index].startswith(">")
        or (
            lines[index].strip() == ""
            and index + 1 < len(lines)
            and lines[index + 1].startswith(">")
        )
    ):
        block.append(re.sub(r"^>\s?", "", lines[index]))
        index += 1

    out = [r"\begin{quote}"]
    para: list[str] = []
    for line in block:
        if line.strip() == "":
            if para:
                out.append(inline(" ".join(para)))
                out.append("")
                para = []
        else:
            para.append(line.strip())
    if para:
        out.append(inline(" ".join(para)))
    out.append(r"\end{quote}")
    out.append("")
    return out, index


def _itemize(lines: list[str], start: int) -> tuple[list[str], int]:
    index = start
    items: list[str] = []
    while index < len(lines):
        if BULLET.match(lines[index]):
            items.append(BULLET.sub("", lines[index]).strip())
            index += 1
        elif lines[index].startswith("  ") and lines[index].strip() and items:
            items[-1] += " " + lines[index].strip()
            index += 1
        else:
            break

    out = [r"\begin{itemize}"]
    out.extend(rf"\item {inline(item)}" for item in items)
    out.append(r"\end{itemize}")
    out.append("")
    return out, index


def convert(markdown: str) -> str:
    out: list[str] = []
    lines = markdown.split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]

        if line.strip() == "---":
            index += 1
            continue

        heading = HEADING.match(line)
        if heading:
            title = HEADING_NUMBER.sub("", heading.group(2).strip())
            out.append(rf"\{LEVELS[len(heading.group(1))]}{{{inline(title)}}}")
            out.append("")
            index += 1
            continue

        if line.startswith(">"):
            block, index = _quote(lines, index)
            out.extend(block)
            continue

        if BULLET.match(line):
            block, index = _itemize(lines, index)
            out.extend(block)
            continue

        if line.strip() == "":
            out.append("")
            index += 1
            continue

        para: list[str] = []
        while (
            index < len(lines)
            and lines[index].strip() != ""
            and not lines[index].startswith(">")
            and not HEADING.match(lines[index])
            and lines[index].strip() != "---"
            and not BULLET.match(lines[index])
        ):
            para.append(lines[index].strip())
            index += 1
        out.append(inline(" ".join(para)))
        out.append("")

    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def main(argv: list[str]) -> int:
    source = (REPO / "report" / "draft.md").read_text(encoding="utf-8")
    body = source[source.index("\n# 1.") :]
    parts = [part for part in re.split(r"\n(?=# )", body) if part.strip()]

    if "--out" in argv:
        outdir = pathlib.Path(argv[argv.index("--out") + 1])
        outdir.mkdir(parents=True, exist_ok=True)
    else:
        outdir = REPO / "report" / "sections"

    if len(parts) != len(SECTION_FILES):
        headings = [part.split("\n")[0] for part in parts]
        print(
            f"expected {len(SECTION_FILES)} top-level sections, got {len(parts)}: {headings}",
            file=sys.stderr,
        )
        return 1

    problems: list[str] = []
    for name, part in zip(SECTION_FILES, parts, strict=True):
        rendered = convert(part)
        # THE GUARD. This class of defect shipped once and was found by eye in a
        # built PDF, which is the most expensive place to find it. An
        # untranslated character is now a hard failure of the conversion.
        for char, why in FORBIDDEN:
            if char in rendered:
                problems.append(f"{name}.tex: {rendered.count(char)} x {why}")
        (outdir / f"{name}.tex").write_text(rendered, encoding="utf-8")
        print(f"{name + '.tex':<32} {len(rendered):5d} bytes  <- {part.split(chr(10))[0][:52]}")

    if problems:
        print("CONVERSION FAILED, untranslated characters left in the output:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print("guard: no straight quotes, curly quotes, dashes or section marks survived")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
