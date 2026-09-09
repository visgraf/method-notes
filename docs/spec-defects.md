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

## 4. A specification that contradicts the environment it sets up

**The defect.** One instruction did two things. A setup step enabled branch
protection on `main` — *"require a pull request before merging"* — and a later
step in the same instruction said **"first commit direct to main; PRs after
that."** The second is not merely wrong, it is *made* wrong by the first. The
push was rejected by the ruleset the same specification had just installed.

**What it cost.** A round trip, and a commit that had to be moved onto a branch
after it was made — so its message, already written and already pushed, records
being committed direct to `main` at the maintainer's instruction, which is now
false. Correcting it would have meant a force-push, which the working agreement
forbids. **The cheapest possible defect still left a permanent wrong sentence in
the history**, because the history is the one thing the method will not rewrite.

**Why it is hard to see when writing.** The two halves are separately correct and
are usually written at different moments — the setup half is infrastructure and
feels like it belongs to a different task. Neither half is reviewed against the
other, because the reviewer is checking whether each step is *right*, not whether
the environment one step creates is one the next step can run in. A specification
is normally checked against the repository as it is; this class of defect is a
specification checked against a repository that its own earlier clause has
changed.

**The check.** **Read the setup steps against the task steps before sending.**
Ask of each task step: does an earlier step in this same instruction make this
impossible? It is a two-pass read of one document and it takes a minute.

## 5. A placeholder that was never filled

**The defect.** A specification's Part B read: *"Insert the text the maintainer
supplies"*, followed by the literal line **`[PASTE THE SECTION TEXT HERE]`**. The
text was never pasted. Everything around it was complete and specific — the
insertion point named to the adjacent subsection headings, the title given, a
falsifiable claim about the content stated and marked checkable, and an
instruction not to edit it — which is exactly what made the hole hard to see: a
placeholder surrounded by precision reads as precision.

**What it cost.** One part of four could not be done, and it was the part the
next part depended on: the section was to be inserted into the prose that the
following step typesets. The dependent work was done anyway against the prose as
it stands, so it must be revisited when the text arrives.

**Why it is hard to see when writing.** The author of a specification is
assembling it from parts they already hold, and a paste marker is a note to
themselves that reads as satisfied the moment they think of the text. It is
invisible to a re-read for *correctness*, because there is nothing incorrect
there — the sentence around it is true.

**The check.** **Grep the specification for its own placeholders before sending**
— square brackets, `TODO`, `TBD`, `<...>`, "here". Mechanical, like the
repeated-figure check and for the same reason: it is a failure of attention that
attention does not catch, because the reader supplies the missing content from
their own head.

**Both entries above were observed in specifications for *this* repository**, in
consecutive tasks, and neither is a defect of judgement. They are defects of
assembly, and the two checks are both mechanical two-minute reads.

---

## 6. A verification search written from the expected finding, not from the claim

**The defect.** A claim was to be checked: *no specification text survives
anywhere in the instance.* The search run against it grepped for
`REPOSITORY STATE ASSUMED` and `reject and report if` — **phrases a committed
specification would contain.** Finding none, it reported the claim confirmed.

But those phrases could only ever have found a *whole specification sitting in a
file*. The claim was about **text**, and the way specification text actually
reaches a record is as a **quotation inside some other artifact** — a
pre-registration repeating a clause in order to depart from it, a findings file
naming the instruction it deviated from. A search for a committed specification
is structurally incapable of finding a quoted one. It was not a weak search; it
was a search for the wrong object, and it returned exactly the answer it had
been built to return.

**What it cost.** The claim shipped in a draft section, was caught on a
re-check, and the section had to be rewritten around the weaker and true claim —
*no specification was ever committed.* One round trip, and the corrected version
is better than the original, because where the fragments survive turned out to
be the interesting part.

**It then happened a second time, in the correction.** The re-check searched for
`specification (said|says|reads|stated)` and returned **four** hits. The report
said **three** — one hit was in the output and was never opened, and it was the
best example of the very thing the section argues. The replacement text was
written from that summary and inherited the wrong count and a false universal
("every one is text an artifact was arguing with"; one of them agrees). **The
second search was better-aimed than the first and was still read from the
expectation rather than from the output.**

**Why it is hard to see when writing.** You search for what you expect to find,
because that is the only image you have of what the thing looks like. A search
built from the expected answer returns the expected answer whether or not the
answer is true, and — this is the part that makes it dangerous — **it returns it
with the authority of a mechanical check.** "I grepped the tree" sounds like
evidence. It is evidence only about the pattern you chose.

**The check.** Two clauses, both cheap:

- **Search for what would falsify the claim, not for what would confirm it.** If
  the claim is *no X survives*, the search must be for anything that could
  possibly be X — including X quoted, paraphrased, referenced, or embedded in
  something else — not for X in the form you imagine it taking.
- **Open every hit before you report a count.** A grep that returns four and a
  report that says three is not a mechanical check; it is a mechanical check
  followed by an unmechanical reading. This is `## 3` — count the set, not the
  ceiling — occurring one level up: **the ceiling of your attention rather than
  the ceiling of an identifier.**

**Where this one came from is part of the entry**, as with `## 3`: the first
instance was written by Chat, the second by Code, in a repository whose subject
is claims that are well-formed, plausible and wrong. Both stations made the same
error inside three iterations of each other.

---

## The general shape

Entries 1 and 2 are the same defect wearing different clothes: **the
specification stated what to do and not what "done" looks like.** The falsifier
rule in `docs/workflow.md` covers the scientific half of that — what result
would mean the question was wrong. This file covers the mechanical half — what
state the world is in when the task is over.

A specification needs both. They fail differently: a missing falsifier produces
a result nobody can interpret, and a missing finish condition produces work
nobody can find.

**Entries 3, 4, 5 and 6 are a second family, and the file is more useful for
separating them.** They are not about what "done" looks like; each states a
finish condition perfectly well. They are defects of **assembly** — a figure
copied from the wrong place, a clause contradicted by another clause, a
placeholder left unfilled. What they share is that **re-reading does not catch
them**, because each one reads correctly in isolation and the error is a relation
between two things. Every check in this family is therefore mechanical: count the
set, diff the setup against the task, grep for your own placeholders. If a
proposed check for a defect in this family can only be described as "be careful",
it is not a check.

**Entry 6 is the family's sharpest case**, because the defective check *was*
mechanical. A grep is not made trustworthy by being a grep: it inherits every
assumption in the pattern, and then hands its output to a reader who already
believes the answer. The two clauses that survive contact with that — search for
the falsifier, open every hit — are the same two moves the repeated-figure check
in `report/claims-verified.md` makes, which is not a coincidence.
