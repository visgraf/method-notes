# math-ai-method

**A template for doing research with AI collaborators — not for building
software with them.**

The distinction is the point, and it should be legible in every file here.

> In software, the characteristic failure is a **bug**: the artifact does the
> wrong thing, and tests, types and review catch it.
>
> In research, the characteristic failure is a **wrong belief**: a claim that is
> well-formed, plausible, internally consistent, and supported by a number that
> was computed correctly and means something else.
>
> **No test catches that.** Every rule in this template exists to prevent one.

That is why this looks different from an AI-for-developers guide. A guide for
developers optimises for producing correct artifacts quickly. This optimises for
never believing something that is not so — which means most of what is here is
machinery for making claims **falsifiable, scoped, and attributable to a source
you can open.**

**Every rule that ships carries the observed failure that motivated it**, in a
sentence, right next to the rule. That is deliberate: a rule without its reason
gets simplified away by the next person who reads it, and looks like ceremony
right up until the day it would have saved them.

## Where this came from, and what that limits

This is extracted from **one instance**: one researcher, one field, one project,
**five days** — [`visgraf/bio-3d-vision`](https://github.com/visgraf/bio-3d-vision)
at commit `5f8e39f`. Thirteen experiments, a decision ledger, a measurement
ledger, a technical report and a verification pass over its claims.

**One instance is not a validated methodology, and this document does not claim
to be one.** What it claims is narrower and, I think, more useful: these rules
were *exercised*, several of them failed in a specific way that is recorded here,
and the fixes are the parts marked as new. Where a component was designed and
never used, the file says so rather than presenting it as tested practice — see
`spikes/README.md` and the roles table in `docs/workflow.md`, both of which
document their own non-use.

Adopt it, argue with it, and record what breaks.

## What is in it

| | |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | **The constitution.** Read at the start of every session; normative. Contains an empty, marked `## Domain invariants` section with a filled example beside it — that section is yours and it is the one that does not generalise. |
| [`docs/workflow.md`](docs/workflow.md) | **The four-station loop** — User → Chat → User → Code → Chat — and its rules: every specification carries a falsifier, states the repository state it assumes, and is reviewed in-repo rather than from excerpts. Also the devil's advocate pass, and the surfaces table with its obituary. |
| [`docs/spec-defects.md`](docs/spec-defects.md) | **Re-read before writing a specification.** Ways a specification has actually gone wrong here, with what each cost. |
| [`docs/state.yaml`](docs/state.yaml) | **The decision ledger.** Schema and headers, no entries. Written by Code, read by Chat, never the reverse. Splits *position* (derivable from the ledger) from *plan* (intent, from Chat, not established here). Carries a **required stopping rule**. |
| [`docs/inherited-measurements.yaml`](docs/inherited-measurements.yaml) | **The measurement ledger.** Every number with its provenance and its status — measured here, inherited, or a recorded gap. Its `methods` section carries the most expensive lesson in the template, as a worked example. |
| [`experiments/exp000_example/`](experiments/exp000_example/) | **The shape of an experiment**: five files, empty, in the order they are written. The README explains why the order is load-bearing. |
| [`spikes/`](spikes/) | **The low-ceremony lane**, with a trigger for when to use it — because in the instance it shipped with rules and enforcement and was used zero times. |
| [`report/`](report/) | Scaffold that compiles from a clean checkout, plus [`claims-verified.md`](report/claims-verified.md): the practice of checking every claim in a report back against its source. |
| [`tests/test_scaffold.py`](tests/test_scaffold.py) | **The enforcement.** What makes "CI enforces that" a true sentence rather than an intention. |
| [`.github/workflows/`](.github/workflows/) | The gate, and the report build. |

## Starting from it

1. **Use it as a GitHub template** (or clone it), then take these five steps
   before any research work.
2. **Rename the package.** `src/research/`, `name` in `pyproject.toml`, and
   `PACKAGE` in `tests/test_scaffold.py` move together.
3. **Fill in `CLAUDE.md`'s two blanks:** *What this is* — including the failure
   this project exists to not repeat — and **`## Domain invariants`**, which
   holds the facts of your field that a plausible sentence can violate without
   any test noticing. Read the filled example beside it first. If your domain
   genuinely has none, delete the section and say why.
4. **Answer `docs/state.yaml`'s stopping rule.** "none yet" is a legal answer and
   it is the answer the instance had for five days without anyone having to type
   it. Typing it is the point.
5. **Clone your reference repositories into `.reference/`**, pinned to a SHA.
   It is git-ignored, and `tests/test_scaffold.py` enforces that code never reads
   from it — references are read by people.
6. **Write the first specification.** `docs/workflow.md` says what one must
   contain; `docs/spec-defects.md` says how they have gone wrong.

Then, at the point where you first want to run something:
`experiments/exp000_example/README.md`, and commit the preregistration alone.

## The parts that are new

Five rules here were **not** in the source instance. Each fixes something that
went wrong in it, and each is marked in the file that carries it:

1. **Methods are entered at first use, not first suspicion**
   (`docs/inherited-measurements.yaml`). Carried *numbers* were labelled from day
   two; carried *methods* only at experiment twelve, by which time an unexamined
   statistical bar had governed ten experiments and turned out not to test what
   it was read as testing.
2. **`docs/spec-defects.md` exists at all.** Decisions get foreclosures,
   measurements get provenance, badly-written specifications got nothing.
3. **The devil's advocate pass** (`docs/workflow.md`). The loop had no move for
   *argue the opposite and see what holds*. Its second trigger is the
   counterintuitive one: a run of **clean** iterations, since a run of failures
   gets scrutiny for free.
4. **The spike trigger** (`spikes/README.md`): a question written about twice
   without being tested goes to a spike. Adding the directory was not enough — it
   was used zero times.
5. **The repeated-claim check** (`report/claims-verified.md`): grep for repeated
   figures across sections, because verification runs per passage and repetition
   crosses passages.
   **This one has fired**, on the provenance paragraph of this README — the only
   place in the template where a rule is caught working rather than argued for.
   Read it under *"This check has fired once, on this template's own prose"* in
   [`report/claims-verified.md`](report/claims-verified.md).

And one required field: **a stopping rule** in `docs/state.yaml`, because the
instance ran five days without one after being told in week one.

## What this template does not do

- It does not check your reasoning. Nothing here can tell you that a correct
  measurement is answering a different question than the one you asked. It can
  only make sure that when someone finally notices, the conditions are still
  attached to the number.
- It does not scale itself down. The ceremony here was written for a project
  where a wrong belief was the expensive outcome. If that is not your situation,
  take less of it — but take the reasons with you, since they are what tell you
  which parts you are giving up.
- It is Python-shaped in its scaffolding (`pyproject.toml`, the test guards, the
  CI matrix) because the instance was. The rules are not; the plumbing is.

## Licence and lineage

Extracted from [`visgraf/bio-3d-vision`](https://github.com/visgraf/bio-3d-vision)
at `5f8e39f84a235bf53ace5789e739f0d51377344a`. Its predecessors —
`visgraf/active-stereo` and `visgraf/bioeye` — supply several of the observed
failures cited above; where a rule's reason begins "the predecessor", that is
which repository it means.

No `LICENSE` file yet. Adding one is the maintainer's call, not the scaffold's.
