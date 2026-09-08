# Workflow — the four-station loop

One task travels a fixed circuit. Each station does one job and hands on.

```
   ┌─────────────────────────────────────────────────────────────┐
   │                                                             │
   ▼                                                             │
 User ──────────▶ Chat ──────────▶ User ──────────▶ Code ────────┘
  sets the       writes the        relays the       does the work,
  goal           specification     spec verbatim    reports back
                                                          │
                                                          ▼
                                                        Chat
                                                   verifies in-repo,
                                                   returns a verdict
                                                          │
                                          advance ┌───────┴───────┐ escalate
                                                  ▼               ▼
                                                User            User
                                              (next task)     (decides)
                                                  ▲
                                          retry ──┘
```

**User** holds the goal and the authority. Decides what matters, adjudicates
escalations, and is the only station that can change what the project is for.

**Chat** writes specifications and reviews results. It **never edits this
repository** — it works from a separate checkout of its own, which it reads and
runs but does not change. See *Chat clones and verifies in-repo* below; the two
statements are not in tension, and the seat they describe is the reviewer's.

**User relays.** The specification reaches Code through the User, verbatim. This
is not a formality: it is the User's read of the spec before any work is spent
on it, and the point at which a spec that asks for the wrong thing is cheapest to
stop. A spec that could go straight from Chat to Code has skipped its only
review.

**Code** does the work in the repository and reports what it did, what it
measured, and what it could not do.

## The surfaces, and the one with no station

| surface | role | exercised in the source instance? |
|---|---|---|
| **Chat** | writes specifications, reviews results, never edits the repository | yes, every iteration |
| **Code** | does the work in the repository, writes `docs/state.yaml` | yes, every iteration |
| **Cowork** | the third surface: cross-experiment synthesis, literature sweeps, briefings — work that spans several experiments and produces no commit | **no. Not once in five days.** |

**Cowork gets a role stated here and an obituary in the same box.** What it is
for is real: the loop above moves one task at a time through one repository, and
nothing in it does the work that spans a whole project's experiments at once —
a sweep of
what the field already knows about the question, a briefing that reconciles five
findings files, a synthesis that is not itself a result and so has no station to
be verified at. That is Cowork's role. In the instance this template came from
it was available and was never used.

**`spikes/` went unexercised in the same instance, and that is probably not a
coincidence.** Both are the low-ceremony lane. A project with strong ceremony
does not reach for its low-ceremony lane, because every artifact that meets the
standard raises the cost of producing one that does not: once a repository is
full of pre-registered experiments with falsifiers and provenance, a scratch
directory with no rules and a briefing with no verdict both start to feel like
things you would have to apologise for. The ceremony is worth keeping. The cost
of it is that the two cheapest instruments in the toolkit go untouched, so if
you want them used, **trigger them** — see the spike trigger in
`spikes/README.md`, and note that it exists precisely because "we added the
directory" turned out not to be enough.

## What a specification is

The loop's central artifact, and **the only one that leaves no trace in the
repository.** Chat writes it, the User relays it verbatim, Code executes it — and
then it is gone. In the instance this template came from, no specification was
ever committed; `docs/state.yaml`'s `falsifier_verdicts` block exists precisely
to compensate, so that at least the *falsifier* survives in the tree after the
specification that carried it has evaporated.

So it has no file and no template here. It has a required shape, and this is it:

| | |
|---|---|
| **1. The assumed repository state** | Branch, commit, what is tracked, what does not exist yet, the SHAs of any reference checkout. **Code's first action is to verify these and reject the task if any is false.** |
| **2. The goal** | What this task is for, in a sentence, in terms of what it would move. |
| **3. The work** | What to do. Clause by clause. |
| **4. The falsifier** | What result would mean *this specification asked the wrong question*. Not a success criterion. |
| **5. A finish condition per clause** | For every clause: what result makes it finished. A clause that cannot be given one is bounded or split out. |
| **6. The end state of the working tree** | Uncommitted; committed; committed and pushed; or a pull request opened. Naming a branch does not say. |

Items 5 and 6 are `docs/spec-defects.md`'s two entries, in the form of a
checklist. Items 1 and 4 are the two rules below. **Re-read that file before
writing one** — it is where the ways these have actually gone wrong are kept.

**Write it so that Code can reject it.** That is the test for whether a
specification is finished: not "is it clear enough to follow" but "does it state
enough that a reader who disagrees can point at the sentence that is wrong."

## The rules

### Every specification carries a falsifier

Not a success criterion — a **falsifier for the specification itself**: a
statement of what result would mean *this specification asked the wrong
question*. It is not about whether the work succeeds. It is about whether the
task was worth specifying.

> If more than roughly a third of items land in `decide`, the criterion is not
> discriminating enough to govern the migration and needs sharpening before it
> is used.

That is the shape. It names a result, a threshold, and the conclusion that the
spec — not the worker — was wrong. Code reports against it whichever way it
comes out, including when it does not fire.

A specification with no falsifier cannot fail, and by this repository's own rule
it does not carry. Chat should refuse to write one without it.

> *Why:* the characteristic research failure is a plausible claim that nobody
> can tell is mis-aimed; a falsifier is the only part of a specification that
> can tell you the question itself was wrong, as opposed to the answer.

### Every specification states the repository state it assumes

Named explicitly at the top: the branch, the commit, what is tracked, what does
not exist yet, the SHAs of any reference checkout. Code's **first action** is to
verify those assumptions and **reject the task and report** if any is false.

> *Why:* a specification is written from a snapshot and executed later, against
> a repository other work has moved. The predecessors lost an amendment exactly
> this way — drafted against a state that had changed by the time it could land,
> and lost silently to a merge. An assumption stated is an assumption that can
> fail loudly; an assumption unstated fails quietly and much later.

### Before writing a specification, re-read `docs/spec-defects.md`

Decisions get foreclosures and measurements get provenance, but a badly-written
specification leaves no record at all — it costs an iteration and then
disappears. That file is the record. It is short and it is a checklist.

### Chat clones and verifies in-repo

Chat does not review from excerpts, transcripts, diffs, or grep output. It
clones the branch and checks the claim against the files.

**The clone is a separate checkout, outside this working tree.** It is thrown
away after the review. That is the whole of the apparent contradiction between
"Chat never edits the repository" and "Chat clones and verifies in-repo":
**Chat holds the files without holding write access**, which is exactly the
reviewer's seat — it can check everything and change nothing. A Chat session
that edits files has left that seat, and the review it then gives is of its own
work.

**Reading is not the limit; changing the record is.** Chat may check out any
commit, install the project, run the suite, run an analysis script, and compare
across revisions — the review in the note below did exactly that. What Chat does
not do is modify tracked files, commit, push, or write `docs/state.yaml`. Build
output and caches in a throwaway clone are not the repository.

A reviewer working from excerpts can only check that the report is internally
consistent, which is the one thing a wrong report is most likely to be. Numbers
arriving in a report are **hypotheses with pointers** until read at their source.
Line references are checked by opening the line.

> *Why this needs saying rather than assuming:* the predecessor's constitution
> asserted the opposite as a structural fact — *"Chat holds excerpts by
> construction, so 'Chat verifies Code's numbers' would rot into a formality"* —
> and on that premise gave Chat non-ratification instead of verification
> (`visgraf/active-stereo`, `CLAUDE.md` §5). **The premise was false.** Chat can
> clone; in the instance it did, ran the suite across two commits in four
> configurations, and found a discrepancy the affected document had been
> rewritten to prevent. The seat existed the whole time and the workflow had
> talked its reviewer out of occupying it.

**And check the claim, not the reference.** An id that resolves is not an id
that agrees.

> *Why:* in the instance, a completed step recorded "Decide the plant" with a
> foreclosure id as its evidence. The id resolved. The sentence describing it was
> true. The foreclosure decided something else entirely — the disparity search
> window — and none of its eleven fields mentioned the plant. The check passed
> on a false claim for four iterations, because "does the entry say what is
> claimed here" was read against the citation's own words instead of against the
> step's title.

### Chat's review returns exactly one of three verdicts

- **advance** — the work is right and the loop moves to the next task.
- **retry** — something specific is wrong and Code can fix it with what it
  already has. Name the defect and the file:line. A retry is not a rewrite of the
  goal.
- **escalate** — the specification was wrong, ambiguous, or asked a question
  whose answer changes what the project should do next. Goes to the User, who
  decides. Chat does not resolve it by rewriting the spec.

**Escalation is expected, not exceptional.** It is the loop's normal way of
discovering that a specification was mis-aimed, which is a thing that happens
often and should. A stretch of tasks with no escalations means either the
specifications are unusually good or the reviewer is not looking hard enough,
and the second is more likely. A reviewer who never escalates is not reviewing;
a reviewer who escalates everything is not reviewing either.

The verdict is stated as one of the three words. "Looks good with some notes" is
not a verdict.

> *Why the rejection path is load-bearing:* in the instance, a framework-level
> decision was specified one way, rejected by Code, and re-specified with an
> extra clause. Without that clause two of the system's three degrees of freedom
> would have been inert, and the closed loop would have re-rendered an identical
> image after every move — a null result that would have looked like a finding.

### The devil's advocate pass

The loop above has no move for *argue the opposite and see what holds*. Chat
reviews Code and Code rejects Chat's specifications, but both of those are aimed
at work that is already suspect. Nothing in the circuit pressure-tests a position
that is **not yet wrong**.

**Either station may call one. Two triggers:**

1. **A stage boundary.** Before the work commits to the next stage, one pass
   arguing that the stage just finished established less than it appears to.
   *Note that stages live in `docs/state.yaml`'s `plan` half, which is empty in a
   new project — so this trigger does not fire until a plan exists, and trigger 2
   is the only live one until then. That is the right way round: trigger 2 is the
   more important of the two anyway.*
2. **A run of clean iterations.** Three or four in a row with no escalation, no
   retry, and no falsifier firing. *This is the counterintuitive trigger and it
   is the one that matters.* A run of failures gets scrutiny for free — every
   failed iteration is already an invitation to re-examine the premise. A run of
   clean ones buys none, and looks like progress the whole time.

**What the pass is.** Take the project's current position — the thing everyone
believes, the direction the plan assumes, the interpretation the last four
findings share — and build the strongest available case that it is wrong. Not a
list of caveats. An argument, with the evidence in the repository that supports
it: which numbers were measured on one stimulus and read as general, which
foreclosure rests on a knife-edge, which carried method has never been examined,
which alternative explanation the experiments do not distinguish from the
favoured one.

**Do not announce it in advance.** A labelled devil's advocate argues knowing it
is an exercise, and that argument is weaker — it reaches for the objections that
are safe to raise and stops at the ones that would actually cost something. The
pass is identified as what it was *after* it is delivered, in the record, not
before it, in the framing.

**Its output goes in the record like anything else.** An open decision, an
annotation on a foreclosure, a falsifier for the next specification, or an
explicit note that the position survived and what it survived.

## What crosses the boundary

`docs/state.yaml` is **written by Code and read by Chat, never the reverse.**
Chat does not edit it — that is what keeps it a report of what is true rather
than a record of what was intended. It is the only durable channel from Code back
to Chat, and it is why Chat can start a session without being briefed.

> *Why the direction is enforced:* the half of that file supplied from the Chat
> surface drifted until the project's centrepiece was still marked `planned`
> while the thing it described was running. A cold session deriving its position
> from the intent half would have taken the work as unstarted.

`docs/inherited-measurements.yaml` is what either station cites when it uses a
number or a method it did not establish here. Cite the `id`. An `inherited`
entry is always the declaration of an assumption.
