# report/figures/

**Empty, and expected to stay that way.** This document has no graphics: every
occurrence of the word "figure" in `report/draft.md` means *a numeral*, not a
plot. That was checked, not assumed, and it is what decided `fc-002` — deleting
`pyproject.toml`, whose one remaining justification would have been a figure
generated from data.

The directory is kept because `report/main.tex` sets `\graphicspath{{figures/}}`,
and this file is kept because the rules below are the ones that come back with
the first figure. They are not in force today. **Do not read them as describing a
practice this repository performs.**

## If a figure is ever added, these come back with it

**`pyproject.toml` and the guards are already back** — restored when
`tools/md2tex.py` landed (`od-007`), not for a figure. So the two steps this
section used to prescribe are done, and what remains for a figure is narrower:
**ask before adding the plotting dependency**, per `CLAUDE.md`'s working
agreement and `fc-002`'s scope. `pyproject.toml` is currently dependency-free and
that is a property worth not losing by accident.

**Commit the generated PDF.** That is what lets `.github/workflows/report.yml`
build with a TeX installation alone and no language runtime, which is the
property the whole report build currently rests on.

**Do not add a CI gate that diffs a committed figure's bytes.** Two runs on one
machine can be made byte-identical — suppress the PDF `CreationDate`, pin the
plotting library's hash salt, select a non-interactive backend — and that much is
worth doing, because it makes "did this figure change?" a question `git status`
can answer.

> *Inherited, from the template (`sha` unexpanded, see the `template` entry in
> `docs/inherited-measurements.yaml`):* regenerating one figure on Linux produced
> 103,146 bytes against the 110,709 committed from macOS — same trajectory, same
> producer string, a font-embedding difference. Neither file was wrong.
>
> **This figure has not been re-measured here and never will be, since there is
> no figure to regenerate.** It is a prior. If you add a figure and want the
> determinism claim, measure it yourself and give it an `mn-` id.

Determinism does not survive crossing machines, so a byte-diff gate would fail on
the runner for a reason that has nothing to do with the figure — and a check that
fails for the wrong reason is one people learn to override. The same argument
kept the repeated-claim check manual; see `fc-001`'s scope.

## The check that travels

**Regenerate and compare the drawn quantities.** Every `make_*.py` should print
the numbers it drew, and **assert them against `docs/inherited-measurements.yaml`
by id**, read as constants at the top of the script with the id in a comment
beside each. The second is the one that matters: a figure is a claim, and a
figure whose numbers are recomputed at draw time and never checked can drift away
from the ledger it illustrates without anything noticing.

> *Why this is not paranoia:* a figure is regenerated far more often than it is
> re-read, and it is re-read by people who already believe what it shows.

**Note that this rule is the reason `docs/inherited-measurements.yaml` and a
figure script are a package.** A figure asserting against ids is the only
mechanism in the whole template that makes a drawing fail, and it needs the
ledger that `fc-006` kept.

## Sizing

Draw to **6.5 in wide** — `\textwidth` for `report/main.tex` (`article`,
letterpaper, 1 in margins) — so a figure included at `width=\textwidth` is
reproduced 1:1 and its type is never rescaled. Set the font size once, in a
shared style module, rather than per script.
