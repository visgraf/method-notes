# CLAUDE.md

Read at the start of every session. Normative. If a request conflicts with this
file, say so rather than quietly deviating.

**Who this governs.** The session reading this holds write access to this working
tree, and is therefore **Code** — the station in `docs/workflow.md` that does the
work in the repository. Chat does not read this file as instructions to itself.
Chat reviews from a **separate checkout that it never writes**, and its
obligations live in `docs/workflow.md`, not here.

## What this is

**This is a research project, not a software project.** In software the
characteristic failure is a bug: the artifact does the wrong thing, and tests,
types and review catch it. Here the characteristic failure is a **wrong belief**
— a claim that is well-formed, plausible, internally consistent, and supported
by a number that was computed correctly and means something else. No test
catches that. Every rule below exists to prevent one.

`method-notes` is a **document-only** repository. It holds one technical
report — *Personal Notes on a Methodology for Research and Development in
Applied Computational Mathematics* — its markdown draft, and the
claims-verification pass over that draft. There is no library, no experiment,
and no measurement apparatus here, and there is not going to be one.

The report is **about another project**: `visgraf/bio-3d-vision`, and behind it
`visgraf/active-stereo` and `visgraf/bioeye`. It reports what a methodology cost
and caught over five days of work in those repositories.

**What failure this repository exists to not repeat.** The source project's own
technical report went into its first draft with eighteen load-bearing claims and
came out of verification with seven standing as written. Nothing in it was
invented — every claim traced to something real in the record. Three were wrong
on the figure and eight were true only in the band, arm or metric they came
from. **This report is a document whose entire content is claims about that
record, written by someone who has read it and believes them.** It is therefore
exposed to exactly the failure it describes, at a higher rate than the document
it describes, because it has no experiments of its own to be corrected by. Every
number in `report/draft.md` is inherited and unverified until read at source.
That is the failure this repository exists to not repeat, and §8.4 of the draft
takes the recursion as a subject rather than a disclaimer.

Nothing here is established yet. See `docs/state.yaml` for what actually runs.

## The rules

**Carry only what can fail.** A test fails against code. A note fails against a
session that violates it. A roadmap, a plan, a changelog, an ADR that no test
pins — none of these can be wrong, so none of them carry weight here. Inherited
numbers live in `docs/inherited-measurements.yaml` as data with provenance,
because a datum can be contradicted and a paragraph cannot. Every entry there
starts `inherited`: using one without re-measuring is an assumption, and it must
be labelled as one.
> *Why:* the predecessor declared depth to be "metres, cyclopean frame" in its
> own constitution and the code returned something else; the sentence was read at
> the start of every session for months and had nothing to fail against.

**Carried methods are labelled at first use, not at first suspicion.** A
criterion, a threshold, a tolerance or a window that walked in from somewhere
else gets an entry in `docs/inherited-measurements.yaml` under `methods` the
first time it is *used*, not the first time someone doubts it.
> *Why:* in the instance, carried *numbers* were labelled from day two and
> carried *methods* only at experiment twelve, by which time a statistical bar
> nobody had examined had governed ten experiments and turned out not to test
> what everyone read it as testing — 45 of 96 null results read differently
> under the bar it was assumed to be.

**A decision is recorded after the thing it decides has been tried.** It records
what was learned by doing it, not what was planned before. If it has not been
tried, it is a question — put it in `docs/state.yaml` under `open_decisions`. If
it has been tried and settled, it is a **foreclosure**: `docs/state.yaml` under
`foreclosures`, with its evidence, its scope, and what reopening it would cost.
> *Why:* a decision recorded before the attempt is a prediction wearing the
> costume of a finding, and later sessions cannot tell the two apart.

> **On ADRs, and why this template does not ship a place for them.** The rule
> above was inherited as an ADR rule — *an ADR names the test that pins it;
> without one it is an intention.* The instance this template came from carried
> that rule, cited seventeen ADRs, and **wrote none**: all seventeen belong to
> its predecessors, it has no `docs/adr/`, and every decision it took itself went
> into the foreclosure ledger instead. The ledger won because a foreclosure has
> fields a reviewer can check — evidence, scope, cost to reopen — and a document
> has paragraphs. Recorded rather than quietly dropped, so that nobody
> reintroduces the directory believing it was tested here. If you want ADRs, add
> `docs/adr/` and say what they hold that a foreclosure entry does not.

**Every iteration regenerates the same artifact beside the previous one's** —
same inputs, written next to its predecessor rather than over it. You compare
against the last one by looking. An iteration that produces nothing to put
beside the last is not an iteration.
> *Why:* overwriting is how a regression becomes invisible; a difference nobody
> can see is a difference nobody reports.
>
> *What this means here, where the artifact is prose.* `report/draft.md` is
> tracked, and it is typeset into `report/main.tex` in the same pull request, so
> the two revisions sit side by side in the history and the sentence that changed
> on its way into LaTeX is visible as a change rather than as a fact. A
> verification pass regenerates the count table in `report/claims-verified.md`
> beside the previous count, never over it. A second pass that overwrites the
> first destroys the only evidence of whether the prose got better.

**`spikes/` is not part of this repository, and its absence was decided rather
than defaulted.** The template ships a low-ceremony lane; this repository has no
lane to be low-ceremony *about*, because it runs nothing. The exploratory work a
spike would hold is a discarded draft section, and that already has a home in
`report/`.
> *Why the absence is recorded instead of silent:* the source instance shipped
> `spikes/` on day one with its rules and its enforcement test and used it zero
> times in thirteen experiments, and §6 of the draft argues that a project with
> strong ceremony structurally will not reach for its informal lane.
> Instantiating the directory here would have reproduced the exact failure the
> report identifies, and its emptiness would then have been read as evidence for
> the argument rather than as a consequence of it. See `fc-004` in
> `docs/state.yaml`.

## Domain invariants

This section holds the facts of this project's subject matter that a plausible
sentence can violate without anything noticing. **The template's rule for what
goes here — prefer to declare it at the place the value is produced — has no
force in this repository, because no value is produced here.** There is no
function with a docstring to carry a unit. Every number arrives from somewhere
else already formed, which means this section is the *only* place these can live,
and the *Where authority lives* section below is inert. That inversion is the
main structural consequence of being document-only, and it makes this section
load-bearing rather than supplementary.

**Four repositories, and claims about them are not interchangeable.**

| | what it is | what claims about it look like |
|---|---|---|
| `visgraf/bioeye` | predecessor; closed the accumulation loop, not the perception–action loop | qualitative, mostly |
| `visgraf/active-stereo` | predecessor; verified geometry, a decision record, the loop never ran | the low-ceremony-lane failure, the constitution clause that was false |
| `visgraf/bio-3d-vision` | **the instance.** Thirteen experiments, two ledgers, a report and its verification pass | *every count in the draft* |
| `visgraf/math-ai-method` | **the template**, which this repository was instantiated from | what it ships, what it fixed |

**The instance is not the template, and the sentence that conflates them is the
one to watch.** A count about thirteen experiments is a fact about
`bio-3d-vision`. A claim about what a rule fixes is a fact about
`math-ai-method`. They are routinely stated in adjacent sentences, and the
template's own front page has already been caught attributing an instance count
wrongly — see `docs/spec-defects.md` §3. When a figure appears, the question is
always *which repository is this true of*, and the answer belongs in the
sentence.

**Counts are taken from the set, never from the highest identifier.** The
instance ran experiments `exp001`–`exp005` and `exp007`–`exp014`. That is
**thirteen**, not fourteen: `exp006` was specified and deliberately not run.
Any count of experiments, foreclosures, or ledger entries is computed by
enumerating the things and counting them, and the enumeration goes in the entry
in `docs/inherited-measurements.yaml` beside the number.

**A denominator is part of a figure, not context for it.** Two counts of the
instance's verification pass are in circulation — *22 claims checked* and
*eighteen load-bearing claims* — and they agree on 3 corrected and 8
under-qualified while disagreeing on the total and on the confirmed count. They
are reconcilable if "load-bearing" names a subset, and **neither passage says
so.** Do not quote either figure without its denominator and the word that
selects it. See `mn-001` and `mn-002` in `docs/inherited-measurements.yaml`;
they are recorded as two entries precisely because prose cannot hold a
disagreement and two data can.

**`report/draft.md` is the prose of record; `report/main.tex` is a derivative.**
When the two disagree about a number, the draft is not automatically right — but
the disagreement is always a defect, and it is *the* defect this arrangement
exists to expose. **The operation that silently produces a wrong number here is
typesetting**: a qualifier dropped, a digit transposed, or a scope clause that
did not survive being turned into a sentence is invisible in either document
alone and obvious between them. Never edit one without diffing the other in the
same pull request.

**Every figure in this report is `inherited` and none will ever be `measured`,
with one exception.** The exception is the verification pass over this report's
own claims: its tally is produced here, and it is the only number this
repository will ever own. Do not let the exception widen — a figure recomputed
by reading a source is still inherited, because the conditions it was produced
under are still not this repository's.

## Definition of done

A task is done when all of these hold:

1. **It moved something.** It moved a measurement, closed an open decision, or
   is explicitly labelled infrastructure.
   > *Why this clause is first:* the predecessor's five conditions were all about
   > artifact quality, so a perfectly-tested component could be added to a loop
   > that had never run — and was.
2. **Every claim it adds to the prose is traceable, and new behaviour has a
   test.** Both halves are live now. The prose half is the one that matters
   almost always: a new factual sentence names which repository it is true of,
   and any figure in it has an entry in `docs/inherited-measurements.yaml`,
   written at the same time and not later. The code half applies to
   `tools/` and `tests/`, which exist again as of `od-007`.
   > *Why this clause was rewritten twice:* it originally read "new behaviour has
   > a test, and the suite passes", which was inapplicable when there was no
   > suite; it was replaced by the prose standard alone; and the code half came
   > back when `tools/md2tex.py` did. **The prose half was never the substitute
   > for the code half — it is the more important of the two here**, because new
   > prose is what mostly arrives and the unchecked version of it is this
   > project's entire failure mode.
3. Conventions are stated in `## Domain invariants` above, because there is no
   code to state them at. See the note there.
4. `docs/state.yaml` is updated if any of it changed.
5. The diff contains nothing that was not asked for.

"Infrastructure" is a real and honest label — scaffolding, CI, a refactor. Use
it. What it is not is a default: if most tasks in a row are infrastructure, the
project is not moving and that is worth saying out loud.

## Where authority lives

**INERT IN THIS REPOSITORY, AND KEPT SO THAT ITS INERTNESS IS DELIBERATE.** The
rule below is the template's best rule and it needs a function to attach to.
There is none here. Authority over the facts in this project lives in the
**pinned reference checkouts** named in `docs/inherited-measurements.yaml`: the
source, not the sentence. The practical translation is that a number's authority
is a file and a line in another repository at a stated SHA, and the ledger entry
is the docstring's stand-in — with the important difference that a docstring sits
beside the code it describes and can be checked against it in one glance, while a
ledger entry can drift from its source silently. **That is a real weakening, not
a clean substitution.** The claims-verification pass is what compensates for it,
and it is the reason that pass is not optional here.

The original rule, kept because it is what the substitution is measured against:

**Units, frames and conventions are declared at the function that returns the
value, in its docstring — not here.** This file does not restate them,
deliberately.

> *Why:* the predecessor's CLAUDE.md §3 declared depth to be "metres, cyclopean
> frame". It was false — the value was `z` in the rectified left-camera frame,
> and the two agree only at zero elevation. The clause sat there being read at
> the start of every session, and nothing could catch it, because a sentence in
> a governance file has nothing to fail against. A docstring beside the return
> statement is checkable against the code under it.

So: this file governs process. In the template, code governs facts about code.
Here, **the pinned sources govern facts about the world, and this file governs
how a claim about them may be written.** When the prose and a source disagree,
the source is the finding and the prose is the bug.

## Working agreement

- **Branch.** `docs/…`, `report/…`, `feat/…`, `fix/…`. Never commit to `main`.
  (`exp/…` and `spike/…` stay dropped: this repository has neither.)
- **Never commit or push unless asked.** Never force-push or rewrite history.
  > *Why the asking is explicit:* a specification that names a branch but never
  > asks for a commit leaves the work sitting uncommitted and costs a round
  > trip. See `docs/spec-defects.md`.
- **Never soften a sentence to make a claim survive verification.** This is the
  document-only form of *never weaken a failing test to get green*, and it is the
  one that will actually be tempting here: the cheapest way to clear an
  UNDER-QUALIFIED verdict is to blur the sentence until nothing can contradict
  it. A claim that cannot fail is worth less than one that failed. Correct the
  figure, add the condition, or drop the sentence.
- **Never add a dependency without asking.**
- **Say when a number is measured and when it is assumed.** An assumed input
  that goes unnamed is the defect; the assumption itself is not.
- **Ask when the spec is ambiguous.** A wrong assumption corrected now is much
  cheaper than a plausible result trusted for a month.
- Uncertain about a numerical result? Say so, and propose the check that settles
  it.

## Process

`docs/workflow.md` — the four-station loop, its rules, and the devil's advocate
pass.
`docs/spec-defects.md` — re-read before writing a specification.
`docs/state.yaml` — written by Code, read by Chat, never the reverse.
`docs/inherited-measurements.yaml` — every carried number and every carried
method, with its provenance.

## Commands

```bash
make -C report             # build the report PDF (needs a TeX installation)
make -C report sections    # regenerate report/sections/*.tex from draft.md (needs Python)
pytest -q                  # the two scaffold guards
ruff check tools tests     # lint
ruff format tools tests    # format
mypy                       # types
```

**This list was one line until `tools/md2tex.py` landed, and the change is worth
naming rather than absorbing.** The converter generates `report/sections/*.tex`
from `report/draft.md`. It lived outside the repository, which made
`report/main.tex`'s claim that the `.tex` is regenerable true and unverifiable at
the same time — `od-007`. Committing it reopened `fc-002` and `fc-003`, and
`fc-002`'s scope is explicit that `pyproject.toml` returns with the gates
attached. Taking the code without the gates would have been taking the convenient
half of a decision.

**What is still true:** there is no library and no experiment. `pyproject.toml`
carries tool configuration and no build backend. The PDF build needs no Python —
the `.tex` files are committed, so `make -C report` compiles from a clean
checkout with TeX alone, and `make -C report sections` is a separate step that
never runs during a build.

**And the prose instrument is unchanged and still the important one.** The gates
catch nothing that a claims pass catches. `report/claims-verified.md`, run by a
person against a pinned checkout, is where this repository's characteristic
failure is caught.
