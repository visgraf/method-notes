# Specification defects

**Re-read this before writing a specification.** It is a list, not an essay.
What a specification must *contain* is in `docs/workflow.md`; this is how the
ones written here have gone wrong.

Decisions get foreclosures. Measurements get provenance. A badly-written
specification gets nothing — it costs an iteration, the iteration gets fixed, and
the defect evaporates. Nobody writes it down, so the next specification makes it
again. This file is where they are written down.

Two rules about what belongs here:

- **Only observed defects.** A defect enters this list when a real specification
  in this repository exhibited it and it cost something. Not defects you can
  imagine. A list of imaginable defects is unbounded and gets skimmed.
- **Each entry names what it cost.** The cost is what makes the entry survive
  the next person who thinks the list is too long.

The list below opens with the two observed in the instance this template came
from. **Add to it.** A specification that goes wrong in a new way and is not
recorded here has been paid for twice: once now and once later.

---

## 1. Do not bundle a bounded task with an unbounded one

**The defect.** A single specification asked for two things: a fixed set of file
checks, which has a definite finish condition, and open-ended verification
against external sources, which does not. The bounded half completed. The
unbounded half ran until it was interrupted.

**What it cost.** An interrupted iteration, and no way to tell from the outside
whether the work was incomplete or merely still running.

**Why it is hard to see when writing.** Both halves sound like the same kind of
request, because both are verification. The distinguishing question is not "is
this verification" but **"what result makes this task finished?"** The file
checks have an answer: all of them have been checked. The external sweep has
none: there is always one more source.

**The check.** For every clause in the specification, state the finish
condition. If any clause cannot be given one, either

- give it a bound that is part of the specification — a count, a list of named
  sources, a time box, a stopping rule — or
- split it into its own task, so that the bounded work lands regardless of how
  the unbounded work goes.

Never leave an unbounded clause sharing a task with a bounded one. The bounded
one is what you will actually get, and you will not know that is what happened.

---

## 2. Naming a branch is not asking for a commit

**The defect.** A specification named the branch the work should be done on and
said nothing about committing. The work was done, correctly, on the right branch
— and left uncommitted, because `CLAUDE.md` says *never commit or push unless
asked* and naming a branch is not asking.

**What it cost.** A round trip: the review could not see the work, and a second
message was spent asking for the commit that the first had implied.

**Why it is hard to see when writing.** "Do it on `exp/foo`" reads as a complete
instruction about version control. It is not — it is an instruction about
*where*, with the instruction about *whether* silently omitted. The rule that
makes it a defect is a good rule and should not be relaxed; the specification is
the wrong half of the pair to fix.

**The check.** Every specification says explicitly, in one line, what the
end state of the working tree should be. Pick one and write it:

- work left uncommitted for inspection;
- committed on the named branch, not pushed;
- committed and pushed;
- committed, pushed, and a pull request opened.

If the specification does not say, the answer is the first one, and you have
bought a round trip.

---

## 3. A count taken from the highest identifier rather than from the set

**The defect.** A specification described the source instance as having
*"fourteen experiments"*. It has **thirteen**: `exp001`–`exp005` and
`exp007`–`exp014`. There is no `exp006` — it was specified and deliberately not
run, recorded as an amendment. The count was read off the highest id.

**What it cost.** The wrong number shipped in `README.md`, in the paragraph about
this template's own provenance, **and propagated**: it was picked up and repeated
in a test docstring, so correcting the source alone would have left it standing.
One wrong figure became two claims.

**Why it is hard to see when writing.** `exp014` is right there and it is
correct — it is the highest id, and ids are allocated sequentially and never
reused, so the sequence *looks* dense. The gap is invisible from the id alone;
it is visible only in the directory listing, and the reason for it is in an
amendment elsewhere in the ledger. Nothing about `exp014` announces that it is the
fourteenth *label* and the thirteenth *thing*.

**The check.** **Count the set, not the ceiling.** `ls`, `wc -l`, a length — some
operation over the members. An identifier is a name, not a tally, and a sequence
with a deliberate gap in it is exactly the sequence you will be tempted to count
by reading its last element.

Two corollaries worth the same line:

- **A deliberate absence is not a hole to be smoothed over.** The gap here is a
  *record* — a step specified and consciously not taken. A count that erases it
  erases the decision too.
- **When you correct a repeated figure, correct every occurrence.** That is the
  repeated-claim check in `report/claims-verified.md`, and this defect is an
  instance of it outside the report: verification runs per passage, repetition
  crosses passages, and prose about the record is not exempt from the rules the
  record lives under. **The tree-wide grep is what found the second occurrence**,
  not a re-reading — recorded as that check's worked example under *"This check
  has fired once, on this template's own prose"*.

**Where this one came from is part of the entry.** It was written by Chat, in a
specification, in a template whose stated purpose is preventing exactly this
class of error — a claim that is well-formed, plausible, and off by one because
nobody counted. The station that writes the rules is not outside them.

---

## The general shape

Both entries above are the same defect wearing different clothes: **the
specification stated what to do and not what "done" looks like.** The falsifier
rule in `docs/workflow.md` covers the scientific half of that — what result
would mean the question was wrong. This file covers the mechanical half — what
state the world is in when the task is over.

A specification needs both. They fail differently: a missing falsifier produces
a result nobody can interpret, and a missing finish condition produces work
nobody can find.
