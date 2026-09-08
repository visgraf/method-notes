# method-notes

**One technical report, its draft, and the pass that checks its claims.**

*Personal Notes on a Methodology for Research and Development in Applied
Computational Mathematics* — Luiz Velho (IMPA), with Claude (Anthropic) as
collaborator. The notes describe a methodology for research with AI
collaborators, drawn from one project run over five days, and they argue that
research has a different characteristic failure from software:

> In software the failure is a **bug** — the artifact does the wrong thing, and
> tests, types and review catch it.
>
> In research the failure is a **wrong belief** — a claim that is well-formed,
> plausible, internally consistent, and supported by a number that was computed
> correctly and means something else. **No test catches that.**

## What is here

| | |
|---|---|
| [`report/draft.md`](report/draft.md) | **The prose of record.** Eight sections and an appendix, drafted on the conversational surface and assembled by hand. This is the document. |
| [`report/claims-verified.md`](report/claims-verified.md) | **The verification pass — not yet run.** Every factual claim in the draft, read back against its source and marked CONFIRMED / CORRECTED / UNDER-QUALIFIED / UNSUPPORTED / PARTIAL. |
| [`report/main.tex`](report/main.tex) | The typeset form. Still the scaffold; typesetting is gated on the pass above. |
| [`docs/inherited-measurements.yaml`](docs/inherited-measurements.yaml) | **The measurement ledger**, and the spine of the repository — see below. |
| [`docs/state.yaml`](docs/state.yaml) | **The decision ledger.** Where the project is, what is closed and why, what is open. |
| [`CLAUDE.md`](CLAUDE.md) | The constitution. Read at the start of every session; normative. |
| [`docs/workflow.md`](docs/workflow.md) | The four-station loop and its rules. |
| [`docs/spec-defects.md`](docs/spec-defects.md) | Re-read before writing a specification. |

Build the PDF with `make -C report` (needs a TeX installation). That is the only
command this repository has.

## The thing to understand before reading anything else

**This report is about another project, so every figure in it is inherited.**
Nothing was measured here. The counts in the draft — thirteen experiments, ten
governed by an unexamined criterion, 45 of 96 nulls reading differently, eighteen
load-bearing claims of which seven stood — are all claims about
[`visgraf/bio-3d-vision`](https://github.com/visgraf/bio-3d-vision) at
`5f8e39f`, or about its two predecessors, or about the template.

That makes this repository an unusually exposed instance of the failure its own
subject matter is about: **a document whose entire content is claims about a
record, written by people who have read that record and believe them.** It has no
experiments of its own to be corrected by. The only instrument it has is the
verification pass, and the only thing it will ever measure is that pass's own
tally.

**That pass has not been run.** The sources are not yet cloned (`gap-001`), no
claim has been resolved to a file and a line (`od-001`), and until then
Appendix A's closing promise — *every claim these notes make about what happened
can be checked* — is a statement about what is possible, not about what has been
done. Read the draft accordingly.

> **A worked example of why the ledger exists, found in this repository's own
> files.** The instance's verification tally appears twice here: as *22 claims,
> 10 confirmed* in `report/claims-verified.md`, and as *eighteen load-bearing
> claims, seven stood* in `report/draft.md`. They agree exactly on 3 corrected
> and 8 under-qualified. They are reconcilable if "load-bearing" names a subset —
> and **neither passage says so.** As two paragraphs in two files they had
> coexisted without contradiction, because a paragraph cannot contradict a
> paragraph. As `mn-001` and `mn-002` in the measurement ledger they are a
> disagreement you trip over. Resolving them is `od-002`.

## Provenance

Instantiated from the template
[`visgraf/math-ai-method`](https://github.com/visgraf/math-ai-method) at commit
`81a638e`, then adapted to a document-only shape: no library, no experiments, no
test suite, no Python. What was deleted and what was kept is recorded with its
reasoning in the `foreclosures` block of
[`docs/state.yaml`](docs/state.yaml) — `fc-001` through `fc-006` — rather than
left to be inferred from an absence.

Two of those decisions are worth flagging on the front page, because the obvious
call went the other way:

- **The decision ledger was kept.** Its argument never depended on there being
  experiments — it exists so a later session can tell *we decided against this*
  from *nobody thought of it*, and editorial decisions have that property too.
  Adapting the template generated six foreclosures, five open decisions and a
  stopping rule before any report work began.
- **The measurement ledger was kept, and is load-bearing.** A report in which
  every figure is inherited is this file's ideal case, not a category error: a
  count in a repository at a pinned SHA is exactly recheckable in a way a
  physical measurement is not.

The four repositories this report makes claims about, and the rule that claims
about them are never interchangeable, are in `CLAUDE.md` under **Domain
invariants**. That distinction is not pedantry — the template's own front page
was caught attributing an instance count wrongly, which is `docs/spec-defects.md`
§3.

No `LICENSE` file yet. Adding one is the maintainer's call.
