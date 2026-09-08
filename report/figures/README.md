# report/figures/

Empty. Generated figures land here and are **committed**, so the document builds
from a clean checkout with a TeX installation alone and no language runtime.

## Determinism, and its limit

**Two runs on one machine should be byte-identical.** Suppress the PDF
`CreationDate`, pin any hash salt your plotting library uses for element ids, and
select a non-interactive backend. That much is worth doing: it makes "did this
figure change?" a question `git status` can answer.

**It does not extend across machines, and you must not build a check that
assumes it does.**

> *Measured, in the instance this template came from:* regenerating one figure on
> Linux produced 103,146 bytes against the 110,709 committed from macOS — same
> trajectory, same producer string, a font-embedding difference. Neither file was
> wrong.

**So a committed PDF is not a checksum.** Do not add a CI gate that diffs a
committed figure's bytes: it would fail on the runner for a reason that has
nothing to do with the figure, and a check that fails for the wrong reason is one
people learn to override.

## The check that travels

**Regenerate and compare the DRAWN QUANTITIES.** Every `make_*.py` in this
directory should:

1. **print the numbers it drew**, so a reviewer can read them without opening the
   PDF; and
2. **assert them against the record** — the measurement ids in
   `docs/inherited-measurements.yaml`, read as constants at the top of the script
   with the id in a comment beside each.

The second is the one that matters. A figure is a claim, and a figure whose
numbers are recomputed at draw time and never checked is a claim that can drift
away from the ledger it illustrates without anything noticing. The assertions
are what make a figure fail.

> *Why this is not paranoia:* a figure is regenerated far more often than it is
> re-read, and it is re-read by people who already believe what it shows.

## Sizing

Draw to **6.5 in wide**. That is `\textwidth` for `report/main.tex` — `article`
at letterpaper with 1 in margins — so a figure included at `width=\textwidth` is
reproduced 1:1 and its type is never rescaled. Set the font size once, in a
shared style module, rather than per script.
