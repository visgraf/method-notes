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

**FILL THIS IN, then delete this instruction.** One paragraph: what is being
investigated, what the predecessors are if there are any, and — the part that
does the work — **what failure this repository exists to not repeat.** Naming
that failure is what makes clause 1 of the definition of done specific rather
than pious.

> *Example, from the instance this template came from:*
>
> `bio-3d-vision` is a research project on active 3D vision — successor to
> `visgraf/active-stereo` and `visgraf/bioeye`. The predecessors built good
> components. Neither ever ran the loop those components were for. That is the
> failure this repository exists to not repeat.

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
same inputs, same seed, written next to its predecessor rather than over it. You
compare against the last one by looking. An iteration that produces nothing to
put beside the last is not an iteration.
> *Why:* overwriting is how a regression becomes invisible; a difference nobody
> can see is a difference nobody reports.

**`spikes/` is where you try things.** Git-tracked, and that is the whole
ceremony: no decision record, no findings entry, no definition of done, and
no tests required.
Nothing in `src/` or `experiments/` may import from it, and CI enforces that. A
spike's only permitted output is **a decision or a deletion** — write what you
learned into `docs/state.yaml` and delete it, or delete it. See
`spikes/README.md`, and note the trigger there: **a question written about twice
without being tested goes to a spike.**
> *Why:* in the predecessor a step was written up twice and never started,
> accumulating five open questions, because writing a document was the only
> sanctioned response to not knowing; in the instance `spikes/` shipped on day
> one with its rules and its enforcement test and was never used once.

## Domain invariants

**EMPTY ON PURPOSE. FILL IT IN, or delete it and record why.**

This is the section that does not generalise, and it is the section that does the
most work. It holds the facts of *your* domain that a plausible sentence can
violate without any test noticing: units, coordinate frames, sign conventions,
what a positive number means, what the null hypothesis is, which quantities are
commensurable, what "the same scene" means.

**The rule for what goes here:** an invariant belongs in this file only if it
cannot be declared at the place the value is produced. Prefer the code — see
*Where authority lives* below, which is not optional and which constrains this
section.

<!-- YOUR DOMAIN INVARIANTS GO HERE. -->

---

<details>
<summary><b>A filled example, from the instance this template came from.</b>
Delete this block once yours is written.</summary>

> **Two stimulus sources, and they are not peers.**
> - *One rendered source:* Blender. When a result needs an image, it comes from
>   there. Adding a second renderer needs an ADR.
> - *One analytic fixture:* closed-form, milliseconds, no monocular depth cues.
>   It is a **test fixture, not a scene family** — it exists so tests are fast and
>   exact. The moment a finding rests on it, it has been misused. Do not grow it
>   into a corpus; 42% of the predecessor's library was stimulus infrastructure.
>
> **Depth is not one quantity.** The loop's estimator returns planar `z` in the
> rectified frame *at the measuring fixation*, which is fixation-dependent, so
> fusing it across fixations fuses different quantities. Convert to range from
> the cyclopean origin before fusing.

**Note the shape of both.** Each names a thing that is easy to state wrongly and
says which side is right. The second goes further and names **the operation that
silently produces a wrong number if you get it backwards** — that clause is worth
more than the rest of the entry, because it is the one that turns an invariant
into something a reviewer can check a diff against.

**Note also what is *not* in the example:** the units of any particular return
value. Those are declared at the function that returns them, never here.

</details>

## Definition of done

A task is done when all of these hold:

1. **It moved something.** It moved a measurement, closed an open decision, or
   is explicitly labelled infrastructure.
   > *Why this clause is first:* the predecessor's five conditions were all about
   > artifact quality, so a perfectly-tested component could be added to a loop
   > that had never run — and was.
2. New behaviour has a test, and the suite passes.
3. Units, frames and conventions are stated where the code states them (below).
4. `docs/state.yaml` is updated if any of it changed.
5. The diff contains nothing that was not asked for.

"Infrastructure" is a real and honest label — scaffolding, CI, a refactor. Use
it. What it is not is a default: if most tasks in a row are infrastructure, the
project is not moving and that is worth saying out loud.

## Where authority lives

**Units, frames and conventions are declared at the function that returns the
value, in its docstring — not here.** This file does not restate them,
deliberately.

> *Why:* the predecessor's CLAUDE.md §3 declared depth to be "metres, cyclopean
> frame". It was false — the value was `z` in the rectified left-camera frame,
> and the two agree only at zero elevation. The clause sat there being read at
> the start of every session, and nothing could catch it, because a sentence in
> a governance file has nothing to fail against. A docstring beside the return
> statement is checkable against the code under it.

So: this file governs process. Code governs facts about code. When they
disagree, the code is the finding and this file is the bug.

## Working agreement

- **Branch.** `feat/…`, `fix/…`, `exp/…`, `docs/…`, `spike/…`. Never commit to
  `main`.
- **Never commit or push unless asked.** Never force-push or rewrite history.
  > *Why the asking is explicit:* a specification that names a branch but never
  > asks for a commit leaves the work sitting uncommitted and costs a round
  > trip. See `docs/spec-defects.md`.
- **Never weaken, skip, or delete a failing test to get green**, and never move a
  tolerance to make a number pass. A failing test is a result.
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
pytest -q                  # suite
ruff check src tests       # lint
ruff format src tests      # format
mypy src                   # types
make -C report             # build the report PDF (needs a TeX installation)
```
