# Personal Notes on a Methodology for Research and Development in Applied Computational Mathematics

**Luiz Velho**, IMPA
**Claude**, Anthropic (collaborator\*)

> \* *These notes were produced in collaboration with Claude — model Opus, high
> reasoning effort. See §8.4, which takes the recursion as a subject rather than
> a disclaimer.*

---

> **Draft status.** This document was drafted on the conversational surface and
> assembled by hand. Its factual claims about the source project have now been
> through **one** claims-verification pass — the practice §4.1 describes and §7
> ships — covering §§1–8.5, resolved against pinned checkouts of the
> repositories it makes claims about.
>
> **42 claims: 22 confirmed, 5 corrected, 8 under-qualified, 6 unsupported, 1
> partial** (`mn-004`). **The thirteen corrected and under-qualified claims have
> been applied**, across twenty passages. Every verdict, its source, and the
> sentence it replaced are in `report/claims-verified.md`.
>
> **Six claims remain UNSUPPORTED and are unchanged in the prose.** They are not
> contradicted by the record; they are unestablishable from it, and four of the
> six describe events this method guarantees will leave no artifact — see
> `gap-004` and `od-006`. Read §4.2's rejection count and §4.5's cold-session
> search as recollection, not record.
>
> Sections 8.6, 8.7 and 8.8 are the first author's, written in the first person.
> They make no checkable factual claims and are out of scope for that pass.

---

# 1. What this is, and what it is not

## Not a tutorial

The major labs have documented their platforms thoroughly, and the open-source
community has covered the patterns for building software with AI assistance more
thoroughly still. A fourth account of how to prompt, how to structure a session,
how to wire a tool into an editor, would be noise. Nothing in these notes
attempts it.

The volume of that material is itself intimidating, particularly for researchers
whose background is not computer engineering, in a field moving fast enough that
specialists struggle to keep up. But the problem is not really volume, and a
document whose contribution is *translation for scientists* would be solving the
wrong thing.

## What is actually missing

Almost all of that material is about **building software**. Research is a
different activity, with a different characteristic failure, and the practices
that make AI collaboration safe for the first are insufficient for the second.

In software, the failure is a **bug**. The artifact does the wrong thing. It
crashes, or returns the wrong value, or corrupts a file — and an entire
apparatus exists to catch exactly that: tests, types, continuous integration,
code review, staged rollout. The failure announces itself, and the discipline is
built around making it announce itself sooner.

In research, the failure is a **wrong belief**. A claim that is well-formed,
plausible, internally consistent, and supported by a number that was computed
correctly and means something else. It does not crash. It passes every test,
because it is not a defect in an artifact — it is a defect in what someone
concluded from one. It propagates into the next experiment as a premise, into
the next decision as evidence, and into the paper as a result.

No test catches that. Type checking does not catch it, code review does not
catch it, and a green CI badge is entirely compatible with it.

This distinction is the whole subject of these notes. When a collaborator can
produce fluent, confident, wrong claims faster than you can check them,
**epistemic hygiene stops being a virtue and becomes the binding constraint on
the practice.** Everything that follows — pre-registered falsifiers, refusing to
ratify a number without reading it at source, marking every carried figure as a
prior rather than a fact, a ledger of what was ruled out and why — exists to
prevent a wrong belief. None of it appears in a guide about building software
with AI, because none of those guides is trying to prevent one.

## The register

These are personal notes. One researcher, one field, one project, five days of
intensive work, and a methodology that has been run exactly once. Everything
here is a case study, and the sample size is one.

That should be said before anything else, because the temptation in this genre
is to write as though a practice that worked for you is a practice. What is
offered is narrower and, I hope, more useful: an account specific enough to be
checked, with the failures left in. The project it came from is public. Every
claim in these notes about what happened there can be verified against a record
that was kept for exactly that reason.

Where the method failed, it says so — and it failed in ways that turned out to
be more useful than its successes. That claim is the argument of these notes
rather than an apology at the end of them.

## A note on scope

The title says *Applied Computational Mathematics* because that is where I work.
Nothing in the method depends on it.

What it requires is a repository, an experiment that can be pre-registered, and
a claim that can be checked at its source. That is most of empirical
computational science, and probably a good deal beyond it. The narrower title is
honesty about the sample rather than a claim about the boundary.

---

# 2. The setting

## Three surfaces

The work is divided across three AI surfaces with different access and different
jobs. The division is not about capability — the same model underlies them — but
about **what each one can see and what it can change**, which turns out to
determine what each is good for.

**Chat** holds no repository. It derives, argues, designs experiments, reviews
results, and writes the specifications the other surface executes. Its
distinguishing property is that it can be wrong for free: a claim attacked here
costs a paragraph, and the same claim attacked after implementation costs a
refactor.

**Code** lives inside the working tree. It reads and writes files, runs the
suite, inspects diffs, drives git, opens pull requests. It builds what Chat
specified and reports what it did, what it measured, and what it could not do.

**Cowork** connects a result to everything else — cross-experiment synthesis,
literature sweeps, briefings, decks. It is the surface for work that spans many
files and many sessions without living in any one of them.

One principle makes this a workflow rather than three parallel conversations:

> **Every handoff between surfaces is a versioned artifact in the repository,
> never chat context.**

Context does not survive a session. A repository does. That single rule is what
makes the arrangement reproducible, and it has a corollary that took a while to
appreciate: **clearing a session is a test of the methodology.** If clearing
feels risky — if you think *but it knows things that aren't written down* — that
reluctance is a defect report on the artifacts, not a reason to keep the
context.

## The four-station loop

One task travels a fixed circuit.

**User** sets the goal and holds the authority. Adjudicates escalations, and is
the only station that can change what the project is for.

**Chat** writes a specification.

**User relays it, verbatim.** This looks like ceremony and is not. It is the
only review a specification gets before work is spent on it, and the cheapest
point at which a specification asking for the wrong thing can be stopped. A
specification that could go straight from Chat to Code has skipped its only
gate.

**Code** does the work and reports back.

**Chat verifies in-repo** — clones the branch, runs what needs running, reads
the claimed line — and returns one of three verdicts: *advance*, *retry*, or
*escalate*.

Two properties of that circuit matter more than its shape.

**Chat never edits the repository, but it does hold the files.** The clone is a
separate checkout, outside the working tree, which Chat reads and runs and never
commits to. This is the reviewer's seat: it can check everything and change
nothing. The predecessor project's constitution had explicitly ruled it out —
*Chat holds excerpts by construction, so "Chat verifies Code's numbers" would
rot into a formality* — and that premise was simply false. The seat existed and
the workflow had talked the reviewer out of occupying it.

**Escalation is expected, not exceptional.** It is how the loop discovers that a
specification was mis-aimed, which happens often and should. A stretch of tasks
with no escalations means either the specifications are unusually good or the
reviewer is not looking hard enough, and the second is more likely.

## The toolchain, and what each part is for

Not a tutorial, but the choices carry weight and the reasons are worth stating.

**GitHub is the autonomy mechanism, not storage.** Pull requests are a gate that
cannot be bypassed; branch protection is what makes *never commit to main*
structural rather than a request. Continuous integration means a rule about
testing is enforced by a machine rather than by memory.

**The repository is the memory.** Every durable thing — decisions, measurements,
position, the plan and its amendments — lives in files that a cold session reads
on arrival. Nothing load-bearing lives in a conversation.

**Two ledgers carry what the code cannot.** A decision ledger, recording each
foreclosed possibility with the evidence that closed it, its stated limits, and
the cost of reopening it. A measurement ledger, recording each figure with the
commit that produced it, the environment it was measured in, and its status —
measured here, inherited from earlier work, or a recorded gap. Both are written
by the surface that holds the files and read by the surface that does not.

**Everything is forward-only.** Corrections appear as amendments, never as
edits. Where a conclusion was drawn and later qualified, both appear, with the
evidence that moved between them. This is not tidiness; §4.8 argues the pair is
more informative than either half.

## What was not used

Two components were designed into the method and never exercised. Both need
describing before their absence means anything.

**Cowork** is the surface for work that spans many artifacts and no single
session. The concrete jobs: sweeping the literature and reporting where a result
sits relative to it; synthesising across experiments that were each designed to
answer their own question, looking for the pattern none of them was testing;
turning a directory of results into a briefing or a deck; reconciling what a
roadmap intended against what actually merged. Where Chat holds an argument and
Code holds a working tree, Cowork holds **the accumulated body of work** — and
it is the only one of the three that can be handed a task and left to run.

In this project every one of those jobs was done by Chat inside the
conversation, or by hand, or not at all. The cross-experiment synthesis in
particular — noticing that four separate experiments were saying the same thing
at different levels — happened in a chat window and had to be written down
afterwards from recollection, which is precisely the failure the method is built
to prevent.

**`spikes/`** is a lane inside the repository with different rules from
everywhere else. Git-tracked, so a thing tried can be pointed at. No decision
record, no findings entry, no definition of done, no tests required. One hard
constraint — nothing in the library or the experiments may import from it,
enforced by a test that runs in CI — and one permitted output: **a decision or a
deletion.** Either it taught you something, which goes into the ledger and the
spike is deleted, or it did not, and the spike is deleted. Directories that sit
there deciding nothing are the failure mode the lane has.

It exists because of a specific thing that went wrong in the predecessor
project. A step was written up twice and never started, accumulating five declared
items, four of them open questions, because the constitution had exactly one
standard — plan, decision
record, findings, tests, definition of done — and that standard is right for
library code and far too expensive for exploration. When a question is open and
the only sanctioned move is to write about it, **uncertainty turns into
documents.** The spike lane was invented so that *try it and look* would be a
legal move.

It shipped on day one, with its rules, its enforcement test and its README. It
was used zero times.

Both are the informal parts of a formal method, and that they are the two that
went unused is the subject of §6. I do not think it is a coincidence.

---

# 3. The project

Everything after this section draws its examples from one research project. This
section supplies enough of it to follow them. It is deliberately brief and
deliberately non-technical; the project has its own report, and readers who want
the science should go there.

## The question

**Active vision** is the proposition that perception is better posed as a
controlled sampling problem than as a reconstruction problem — that *choosing
where to look* improves what is perceived. The project tested that claim for
binocular depth estimation.

The biological motivation is concrete. A camera samples every pixel at the same
resolution; an eye does not. The human fovea covers one to two degrees at high
acuity, resolution falls off sharply beyond it, and several times a second a
saccade repositions that window. And the two eyes are not cameras with fixed
geometry: they rotate about centres fixed in the head, converging on whatever is
being looked at, so the stereo geometry itself changes every time gaze moves.

## The machinery, in six sentences

Two views of a scene, taken from slightly separated positions, disagree about
where things are. That disagreement — **disparity** — is larger for near
surfaces than far ones, so depth can be recovered from it. A **matcher** finds,
for each point in one image, the corresponding point in the other; it returns a
disparity, a confidence, and a **validity mask** marking points where it found
nothing trustworthy. **Vergence** is how far away the two lines of sight cross —
what the system is focused on — and converting disparity into metric depth
requires knowing it. A **belief** accumulates the depth estimates across
successive fixations, each new measurement combined with what is already
believed, weighted by confidence. And a **gaze policy** chooses where to look
next, typically by finding where the belief is least certain.

That loop — fixate, measure, update the belief, choose the next fixation — is
the object under study. Whether closing it improves anything is the question.

## Three things that recur in the examples

**Half-occlusion.** At a depth discontinuity — the edge of a nearer surface
against a farther one — a strip of the background is visible to one eye and
hidden from the other. Those points have no correspondent at all. The matcher
does not report this; it finds the best available wrong match, and a sharp
minimum at a wrong disparity is genuinely sharp. **The result is a confident,
incorrect estimate at exactly the geometry an active system might hope to
resolve by looking elsewhere.** This is the phenomenon that motivated the whole
project, and several examples turn on it.

**Foveal weighting.** Implementing the fovea by measuring everything at full
resolution and then *discounting* what is far from gaze — as opposed to a real
retina, which never samples the periphery finely in the first place. The
difference between weighting and sampling turns out to matter a great deal.

**The synthetic stimulus.** A random-dot stereogram: a field of noise, warped by
a known depth field to produce the second view. Its virtue is that depth exists
*only* in disparity — nothing can be recovered from shading or texture, so a
system that appears to see depth is genuinely seeing stereo. §4.6 is about what
was wrong with it.

## The shape of the work

Thirteen experiments over five working days, each pre-registered before its runner
existed. Two predecessor repositories, from which geometry, measurements and a
set of methods were carried forward. Roughly four thousand lines of library code
against a slightly larger volume of tests, thirteen foreclosed decisions,
eighty-seven measurements taken in the project and forty-one inherited.

Experiments are referred to below by their position in that sequence rather than
by name. What matters for these notes is not which experiment found what, but
that each was declared in advance, ran, and reported against its own falsifier.

## What it found, in brief

The negative results were consistent. The choice of gaze objective did not
matter: two objectives that never once selected the same pixel produced
indistinguishable results. Knowing *where* measurement was possible outweighed
knowing *how uncertain* it was by a large factor. Foveal weighting on a
uniformly sampled sensor was strictly lossy. Deliberately re-converging in order
to bring new depths into range made estimation worse.

One positive result survived. Closing the loop — actually re-imaging at each new
fixation rather than re-weighting a single capture — helped, at a substantial
cost, and the benefit decomposed almost entirely into **coverage** rather than
accuracy: the moving system's advantage was that it *saw more of the scene*, not
that it *estimated better*.

And four of the thirteen experiments turned out to be about the instrument or
the criterion rather than the framework. They were the precondition for reading
the other nine.

None of that is the subject of these notes. It is the material the examples come
from.

---

# 4. How it goes wrong, and how you know when it's going right

Seven failure modes. Each is a way a research project acquires a wrong belief,
each was observed in this project rather than anticipated, and each has a
mechanism that either held or did not. The section ends with the harder
question: what it looks like when the method is working.

## 4.1 Fluent wrong claims

The characteristic failure, and the one everything else is downstream of.

A language model produces confident, well-formed, internally consistent
statements. When it is right, that fluency is the point. When it is wrong, the
fluency is the problem: nothing in the surface of the claim distinguishes the
two, and the reader's only defence is to check.

**What it looked like.** The conversational surface asserted false things at a
rate of roughly one per day. Not hallucinated citations or invented functions —
those are easy to catch. The failures were subtler and more dangerous:

A background claim that a confidence failure had been *replicated* across two
stimulus families, when the record showed the two families disagreeing in sign.
The claim was plausible, it was about the project's own prior work, and it was
the motivating premise of an entire section.

A statistic described as *frozen* across a run when it drifted by a small amount
that mattered.

A foreclosure asserted to be settled by an experiment that had measured
something else entirely — the identifier resolved, the entry existed, and it
said a different thing.

A count of experiments taken from the highest identifier rather than from the
set, because one had been specified and deliberately not run.

Every one of these is the same shape: **a claim that would survive any reading
and fails only against its source.**

**The mechanism.** Three parts, and they work together.

*Non-ratification.* The surface that does not hold the files may not settle a
numeric question. It states where to check, never what the number is. A
specification says *verify before recording*, and a number arriving in a report
is a hypothesis with a pointer until someone opens the file.

*Verification at source.* The reviewing surface clones the branch and reads the
line. Not the diff, not the excerpt, not the summary — the line. A reviewer
working from excerpts can only check that a report is internally consistent,
which is the one thing a wrong report is most likely to be.

*A claims pass on any document making factual assertions.* Before the project's
technical report was typeset, every load-bearing claim in it was checked at
source and marked confirmed, corrected, under-qualified, or unsupported. Of the
eighteen substantive claims in the first pass, seven stood as written.

**Did it hold?** Yes, and the numbers are the argument. Three claims wrong on
the figure, eight true only in the band or arm they came from, none unsupported
— all caught before typesetting. The category that mattered most was not the
outright errors but the **under-qualified** ones: claims right in the condition
they were measured under and misleading without it. Those typeset cleanly and
read as more general than they are, and there were nearly three times as many of
them as of outright mistakes.

**Where it did not hold.** Verification runs per passage; repetition crosses
passages. The same ratio was verified correctly in one section and left without
its qualifying condition in another, because a careful reading of each passage
structurally cannot notice that a figure appears twice. The fix is mechanical
rather than attentional — grep for repeated figures across the document — and it
was added afterwards, which is to say the failure was found by having it happen.

## 4.2 Stale state

A specification is written from a snapshot and executed later, against a
repository that other work has moved. The specification is not wrong when
written and not right when run, and nothing in it marks the difference.

**What it looked like.** Specifications drafted against a commit that had
advanced by the time they were sent — twice, once trivially and once not. The
serious instance had a premise about which arms of an experiment re-estimated a
parameter, and it was false; the entire question the specification posed
depended on it, and the work would have measured something other than what it
claimed.

The general form is worth stating because it is not obvious: **facts do not
expire, they just get old.** A statement learned in a conversation stays
available with undiminished confidence long after it stops being true, and a
long-running thread accumulates true-once assertions at a steady rate while
confidence in them stays flat.

**The mechanism.** Every specification names, explicitly and at the top, the
repository state it assumes — the commit, what is tracked, what does not yet
exist, the SHAs of any reference checkout. **The executing surface's first
action is to verify those assumptions and reject the task if any is false.**

An assumption stated is an assumption that can fail loudly. An assumption
unstated fails quietly and much later.

**Did it hold?** Three specifications were rejected on false assumptions, each
correctly, each before any work was spent. That is the mechanism working exactly
as designed, and it is the clearest case in the project of a rule paying for
itself: the rejections cost a round trip each, and the cheapest of them would
otherwise have cost an experiment.

It also generalises past its origin. The rule was written for repository state,
and what it actually enforces is that **the surface with the files gets to
overrule the surface with the memory** — which is the same asymmetry as §4.1's,
arriving from a different direction.

## 4.3 Work that cannot fail

The deepest failure mode, and the hardest to see, because everything about it
looks like success.

A test whose assertion is satisfied by construction. A criterion no sample size
can resolve. An acceptance check written after the code it accepts. In each case
the apparatus runs, reports green, and establishes nothing — and because it
reports green, nobody looks.

**What it looked like.** The clearest instance was a statistical criterion
inherited from earlier work: a difference counted as real if it exceeded the
seed-to-seed spread. That is a defensible question — *is this effect larger than
the variation between scenes* — but it is not a test of whether an effect
exists, and it has a property nobody noticed for ten experiments: **the spread
is a sample standard deviation, so it does not shrink with more samples.**
Adding seeds refines the estimate of the spread and moves the threshold nowhere.
No number of seeds could ever resolve anything.

That was discovered only when a specification asked, for a different reason,
*how many seeds would settle this?* — a question that cannot be answered without
inspecting the criterion. Ten experiments had reported verdicts against it, and
every one of their null results had been read as evidence of absence when the
criterion could not have produced anything else.

Smaller instances recur throughout. An acceptance test that would have passed on
a scene where the geometry made the quantity identically zero. A calibration
render whose three surfaces occluded each other, so a check written for three
measured one — and the render succeeded silently. A falsifier that could only
fire at a fixation where the effect it tested was structurally absent.

**The mechanism.** Pre-registration with a falsifier, and a specific definition
of one.

Not a success criterion. A **falsifier for the specification itself**: a
statement of what result would mean this specification asked the wrong question.
It names a result, a threshold, and the conclusion that the task — not the
worker — was mis-aimed. It is reported against whichever way it comes out,
including when it does not fire.

The rule that follows: **a specification with no falsifier cannot fail, and by
the method's own standard it does not carry.**

**Did it hold?** Partly, and the partial failure is instructive. Falsifiers
caught a great deal — including several cases where the second clause fired and
an experiment was found to have asked the wrong question. But three times the
actual outcome fell outside *every direction the falsifier had enumerated*: an
intervention that actively harmed rather than merely failing to help; an effect
that shrank rather than staying flat or growing; a result that reframed the
question rather than answering it.

The pattern in those misses is consistent. **The falsifiers were written for the
null and the confirmation, and the informative outcome was the reversal.** After
the third occurrence the practice changed: enumerate all four directions —
persists, shrinks, grows, reverses — and report which occurred. That is a small
change and it is the single most useful thing the project learned about writing
them.

## 4.4 Inherited assumptions

Numbers and methods carried in from earlier work acquire, silently, the
authority of things decided here. Nobody decides to promote them. They simply
arrive without a marker, get cited, and after a few citations there is no way to
tell them apart from what was measured.

**What it looked like.** This project inherited a great deal from two
predecessors: forty-one measurements, a body of geometry, a matcher, a stimulus,
and a set of parameter values. The measurements were handled from the second day
— every one marked `inherited`, meaning *a prior awaiting re-test, not an
established fact*, with the repository and commit it came from. That discipline
worked. Inherited figures were cited as inherited, and when one was contradicted
the contradiction was legible.

The methods were not handled at all, and nothing in the apparatus noticed. A
statistical criterion, a set of band thresholds, a search window, an inhibition
radius, a foveal width, the parameters of a validity test — all carried across,
all used, none marked. Thirteen carried constants and criteria, ten of them
carried in from elsewhere, **eight never examined by anyone in this project** —
and one of the eight was the criterion in §4.3 that governed ten experiments
before its properties were checked.

The asymmetry is the finding. The same repository that would not let a *number*
cross without provenance let a *criterion* cross unmarked — and the criterion
determined how every number was read.

**The mechanism.** Extend the inherited marker to methods, with the same three
fields: what was carried, from where, and whether it has been re-derived here.
Then one rule that the project learned the expensive way:

> **A carried method gets its entry at first use, not at first suspicion.**

**Did it hold?** It was not in place when it was needed. Applied to numbers on
day one and to methods at experiment twelve, by which point the damage was done
and required a re-analysis of every recorded verdict. That re-analysis is the
reason the failure is well documented rather than well hidden.

The template that came out of this project ships the methods section
pre-populated with the rule and this failure as its worked example. That is the
only honest form: a rule presented without the thing that motivated it gets
simplified away by the next person to read it.

## 4.5 Knowledge that lives only in a conversation

The methodology's foundational rule is that every handoff is a versioned
artifact and never chat context. The failure mode is what happens when something
important slips past it — and the thing about this failure is that **you cannot
detect it from inside the conversation**, because there the knowledge is present
and load-bearing and feels like part of the project.

**What it looked like.** An eighteen-step plan, with stages, altitudes, and two
recorded amendments, existed in a chat window and nowhere else. It had shaped
every specification for a day — seven merged pull requests — before anyone wrote
it down. Nobody noticed, because both parties to the conversation could see it.

It was found the moment a session was cleared. The fresh session was asked to
record the plan, searched the repository, the git history including commit
bodies, and both reference checkouts, found six of eighteen steps inferable from
side-references in old prompts and none of the stage groupings, and **refused to
invent the rest.** Its stated reason was that the state file is the one document
a cold session trusts without checking, and fabricated content carrying that
authority would be the same defect in the place it does most damage.

That refusal was the detector. Nothing else in the project would have caught it.

A second instance in the same shape, smaller and sharper: a decision was taken
in conversation and then recorded in the repository as *complete*, citing an
experiment identifier that resolved to an entry about something else. The claim
entered the durable record wearing a citation that did not support it, and it
sat next to a verdict in the same file explicitly saying the opposite.

**The mechanism.** The repository is the memory, and **clearing a session is the
test of that claim.** If clearing feels risky, the reluctance is a defect report
on the artifacts.

There is a subtler corollary the second instance forced. A record that
distinguishes *what is established* from *what is intended* has a boundary, and
a claim can cross it. The project's state file was eventually split into a
**position** half — derivable from the ledger, verifiable, cannot be wrong
without the ledger being wrong — and a **plan** half, marked as intent supplied
from outside the repository and not established by it. The failure was a claim
that entered through the plan half and was recorded in the position half,
**losing its warning without losing its origin.** Splitting the file created the
boundary that made the error invisible.

**Did it hold?** The rule held; the enforcement arrived late. Both instances
were caught, one by a cold session and one by a reviewer reading the file, and
both are in the record with their corrections. What the project did not have —
and what the template now ships — is any check that runs *before* something
load-bearing goes unwritten. Clearing the session is a good detector and an
expensive one, because by then the work has already been done under the
unwritten assumption.

## 4.6 The instrument you authored

This one is not about AI collaboration. It belongs here anyway, for a reason
worth stating: **it was the failure that consumed the most effort, it is
invisible to every mechanism described so far, and it is going to be common** —
because AI collaboration makes synthetic experiments dramatically cheaper to
build, and cheap instruments get less scrutiny than expensive ones.

**What it looked like.** The project's synthetic stimulus followed a standard
construction: generate a texture, warp it by the ground-truth field to produce
the second view. The warp has a defect at depth discontinuities, where adjacent
output samples draw from widely separated input regions, and the second image
acquires a stretched patch of real texture with no consistent correspondence.

The obvious criticism of such a stimulus is that it lacks the hard cases that
real data has. The measured problem was worse and had the opposite sign. The
artefact was **harder than the real thing it stood in for, and it passed the
validity test built to catch exactly that class of failure** — self-consistent
enough to be accepted, wrong enough to poison the estimate, and concentrated in
precisely the region where the scientific question lived. Rendering the same
geometry physically, the synthetic fixture was roughly twenty times worse in the
tail. Two fifths of the valid measured pixels, four fifths of the total *squared*
error.

Three of thirteen experiments went to establishing this. Conclusions already
drawn had to be re-read. And the obvious correction — restrict the analysis to
the clean region — was itself wrong, because the contaminated band was also the
only band where the question was live: excluding it did not isolate clean
measurement, it isolated easy measurement.

**The mechanism.** There isn't a clean one, which is why this subsection is
shorter on remedy than the others. What the project arrived at:

> **A stimulus is an instrument, and must be characterised before it is used to
> measure.**

Characterised in the specific sense of an unfamiliar sensor: what are its
failure modes, where do they fall, and do they coincide with the regime you care
about. The last clause is the load-bearing one, and the expectation should be
that **they do** — because the regime you care about is usually the hardest
thing to synthesise, and therefore where the synthesis cuts its corners.

**Did it hold?** It was learned rather than applied, at a cost of roughly a
quarter of the project's experiments. That said, the cost bought a durable result:
the fixture's operating range is now measured, and every experiment afterwards
was sized against it.

The generalisation is uncomfortable and I think correct. **In simulation-based
science the instrument is authored by the same hand as the hypothesis.** Real
data can be difficult, biased, or insufficient; it is not written by someone who
wants a particular answer. That is not an argument against synthetic stimuli,
which offer dense ground truth no capture provides. It is an argument that they
deserve the scrutiny given to an unfamiliar instrument, and that the scrutiny
should be budgeted in advance rather than discovered.

## 4.7 Momentum

The last failure mode is the only one with no artifact to point at, because it
consists of not looking.

**What it looks like.** A method that is working stops being questioned, and it
stops being questioned *precisely because it is working.* Each clean iteration
lowers the felt need for the next one to be examined. Verdicts land, falsifiers
report, the ledger grows, and somewhere in the middle of that the frame within
which all of it is being measured stops being a question anybody asks.

This project had two clear instances. The statistical criterion of §4.3 went ten
experiments without examination during the stretch where results were arriving
cleanly — the criterion was not questioned *because nothing was going wrong*.
And a positive result, one experiment old and underpowered in its most important
band, created immediate pressure to build on it rather than to consolidate; the
consolidation, when it eventually happened, found the criterion defect that
changed how every null in the project read.

**The mechanism.** A devil's advocate pass: argue the case against the whole
approach, not against its details. Not the specification's falsifier, which asks
whether a task was well-posed, but one level up — *what result would mean this
stage should not continue.*

Two triggers, either party may call it. A stage boundary, where the next
commitment is largest and least paid for. And **a run of clean iterations**,
which is the counterintuitive one and the one that matters: a run of failures
gets scrutiny for free.

Two properties keep it from decaying. It must be **occasional** — a
per-iteration requirement would generate a devil's advocate pass on a routine
commit, the pass would be pro forma, and a check that always fires is a check
nobody reads, which is §4.3's failure in a new costume. And it must **not be
announced in advance**: a pass labelled as an exercise argues knowing it is an
exercise, which is a weaker thing. The best instance in this project came from a
provocation I could not distinguish from a position — and being unable to tell
is what made it work.

**Did it hold?** It was agreed in conversation and never written into the
workflow, which by the method's own standard means it did not exist. It ran
twice anyway, informally, and both times produced something. That is the least
satisfying verdict in this section: a mechanism that worked when used and was
never made structural, left depending on someone having a good instinct on a
given afternoon.

## 4.8 The signatures of good work

Everything so far has been failure, and there is a reason for that: **failure is
easy to write about because it hurts.** A wrong claim announces itself once you
check it. A stale premise gets rejected. A criterion that cannot resolve
anything can be shown, arithmetically, to be unable to.

Recognising the method *working* is a genuinely harder problem, and it is the
more important one. A good result and a lucky one look identical from outside. A
project can produce clean verdicts for a month on a broken criterion — this one
did — and every artifact along the way looks like evidence of health.

So the two sides of the coin are not symmetric. **Failure is detected; success
has to be recognised.** The first has mechanisms; the second has only signatures
— and if you cannot read them, you cannot tell a working method from a
comfortable one.

Here is the transition, and it is the thing I would most want a reader to take
from these notes.

> **Every signature of the method working is an event that felt, at the time,
> like something going wrong.**

A result nobody wanted. A falsifier that fired in a direction nobody enumerated.
A collaborator refusing to proceed. A correction to a claim already published
internally. Each of those arrives as friction — as a delay, an inconvenience, a
thing that has to be gone back over. And each of them is the system doing the
only job it exists to do.

That inversion is not a nice framing; it is the practical content of the whole
method. If your instinct treats those moments as costs, you will optimise them
away, and what remains will be a fast, fluent, unfalsifiable practice that feels
excellent. **The discipline is learning to feel the friction as the product.**

Five signatures, each observed here.

**A result nobody wanted.** The strongest indicator and the least comfortable.
Foveal weighting — the biologically motivated mechanism at the centre of the
framework — lost on every seed. The one positive result decomposed to show the
system's value was that it *saw more*, not that it *estimated better*. The
statistical criterion turned out not to test what everyone had read it as
testing. None of these was hoped for. **A method that only ever confirms is not
a method**, and the surest sign of one is a project whose results all point the
way its author was already facing.

**An outcome outside every direction the falsifier enumerated.** Three times: an
intervention that harmed rather than merely failing; an effect that shrank
rather than growing; a result that reframed the question. Each omission recorded
beside the result. A falsifier that always fires in one of its stated directions
is probably not testing anything — it is checking that reality is one of the two
shapes you imagined, and reality is under no obligation.

**A control invented that nobody asked for.** A specification asked whether a
geometric operation was accurate. The test that came back also asserted that
*not* performing it must be ten times worse — because a number is only a result
when the alternative is measured beside it. That pattern then recurred three more
times, unprompted. **A collaborator adding the control you forgot is the
clearest evidence that a standard has been internalised rather than complied
with**, and it is the difference between a rule that is followed and a rule that
is understood.

**Someone stopping rather than inferring.** A cold session refused to write down
a plan it could not find, and said why: fabricated content in the one file a
cold session trusts would be the same defect in the place it does most damage.
Another declined to commit because permission had not been given, at the cost of
a round trip. Both were mildly inconvenient. Both were the constitution working
on exactly the case where inferring would have been easier — which is the only
case where a constitution is worth anything.

**A correction that makes the claim narrower and more interesting.** A
background section asserted that a confidence failure had been replicated across
stimulus families; the record showed the families disagreeing in sign. The
corrected claim was narrower, and it was a *better* motivation than replication
would have been, because a failure that appears on real imagery and not on
synthetic dots poses a sharper question than one that appears everywhere. **When
a correction improves the argument, the record is doing what it exists for.**

**How to cherish it: keep the wrong version beside the right one.** Not as
ritual honesty — because the pair carries information neither half does. That a
verification pass recommended a figure read off a rounded table, and a second
pass corrected it from the underlying rows, is a finding *about verification*:
the escalation from summary to source is what made the difference, and it is
reusable. Erase the first version and you keep a correct number and lose the
lesson.

This is why the record is forward-only. Corrections are amendments, never edits.
The history of a claim being wrong and then right is more valuable than the
claim.

---

# 5. What it cost, and what it caught

The previous section argued that the signatures of a working method arrive
disguised as friction. This one puts numbers to the friction, and then makes a
claim that follows from §4.8 and is easy to miss: **the costs and the catches
are not two lists. They are the same list, read twice.**

## What the friction cost

**Verification costs an iteration.** Checking a document's claims at source
before typesetting it took a full cycle and produced no prose. Re-scoring every
recorded verdict under a corrected criterion took another. Two of thirteen
experiments' worth of effort produced no new science.

**Pre-registration costs a commit and an argument.** Declaring what would
falsify a hypothesis, and separately what would mean the experiment asked the
wrong question, before the runner exists — that is genuine work done at the
moment when the answer is least visible and the temptation to defer is
strongest.

**Rejections cost round trips.** Three specifications were rejected on false
premises. Each cost a cycle.

**The record costs reading.** Nine thousand lines of ledger in five working days, and
one human reading every pull request.

## What the friction caught

The same events.

The verification iteration found three wrong figures and eight claims true only
in the condition they were measured under. The re-scoring iteration found that a
criterion had governed ten experiments without testing what it was read as
testing. The three rejections each stopped work that would have measured the
wrong thing — one of them a premise so central that the experiment would have
answered a different question entirely and reported the answer as if it were the
one asked.

**A wrong belief costs everything downstream of it.** That is not rhetoric; it
is the arithmetic of this project. The criterion defect propagated through ten
experiments and required re-reading every null result they had produced. Caught
at experiment two, it would have cost an afternoon.

So the honest accounting is not *the method cost two iterations and caught four
errors.* It is: **the method spent two iterations to avoid re-running ten.**

## The cost of success

The costs above are the ones a reader expects. These are the ones that
surprised, and every one of them arrives when things are going *well*.

**A positive result creates pressure to build on it.** The project's one
positive finding was a single experiment old, underpowered in its most important
band, and untested against its own dose-response. The obvious next move was to
build the next stage on it. The consolidation done instead found the criterion
defect — which is to say, **the discipline that paid best was the one applied at
the moment of greatest momentum.** Had the result been negative, nobody would
have wanted to build on it and the consolidation would have happened for free.

**A run of clean iterations is when framing stops being examined.** §4.7's
trigger. Worth restating as a cost rather than a mechanism: the better a project
is going, the more expensive its next unexamined assumption becomes, because
more has been built on top before anyone checks.

**Rigour is self-reinforcing, and that is not entirely good.** Every artifact
that meets a high standard raises the felt cost of producing one that does not.
The low-ceremony lane — where an idea can be tried and thrown away — shipped on
day one and was never used once. §6 argues this is the method's deepest problem
and not an oversight.

**The record outgrows the reader.** A methodology that produces more record than
anyone can read has moved the bottleneck rather than removed it. In the
predecessor project, two failures got in exactly there, under merge pressure,
with green tests. The apparatus catches wrong *numbers* well and wrong *merges*
poorly, and the variable that moved was the rate.

**The deliverable is unfashionable.** The better this works, the more of the
output takes the form of *a well-ordered set of eliminated possibilities* —
harder to publish than a benchmark number, and harder to describe at a
conference. That is a fact about publishing rather than about the knowledge, but
it is a real cost borne by whoever adopts the method.

## The asymmetry that justifies the whole thing

One number carries the argument. The **first** of the two verification passes
over the project's technical report checked twenty-two claims, eighteen of them
substantive and four bibliographic. Of those eighteen, **seven stood as
written.**

The other eleven were not fabrications. They were claims made by someone who had
read the record, believed them, and would have published them. Three were wrong
on the figure; eight were true in the condition they came from and misleading
without it.

That is the ratio the method exists for. In software, shipping eleven of
eighteen statements slightly wrong is a bad release. In research, it is a body
of work that other people build on.

The costs are all paid in time. The failure is paid in credibility, and it is
paid by everyone who cited you.

---

# 6. Where the method failed

Four of the seven mechanisms in §4 arrived late, after the failure they were
built for had already happened. That is not damning — a method extracted from
one project will be, by construction, a record of what that project learned the
hard way. Those are covered where they occurred.

This section is about the failures that are still live. The last one is the
serious one, and I want to arrive at it properly.

## Three that arrived late

**The inherited marker was applied to numbers and not to methods.** Day one for
figures, experiment twelve for criteria — by which point a carried statistical
bar had governed ten experiments. The asymmetry is the finding: a repository
that would not let a number cross without provenance let a criterion cross
unmarked, and the criterion determined how every number was read.

**Verification ran per passage while repetition crossed passages.** Found only
because the same ratio appeared twice and someone happened to look at both.

**Specification defects had no ledger.** Decisions got foreclosures,
measurements got provenance, and badly-written specifications got nothing — so
the same two errors recurred: bundling a bounded task with an unbounded one, and
naming a branch without asking for a commit. Both were cheap and both were
avoidable by a five-line list that did not exist.

All three now ship in the template, each with the failure that motivated it.
That is the ordinary way a method matures, and it is unremarkable.

## The devil's advocate was agreed and never written down

Less ordinary, and worth its own paragraph because of what it demonstrates.

The pass was proposed, discussed, refined into two triggers, and endorsed. It
ran twice, informally, and both times produced something the loop would not have
produced. **It was never written into the workflow file.**

By the method's own foundational rule — every handoff is a versioned artifact,
never chat context — that means it did not exist. A mechanism designed to catch
the failure of a method going unquestioned was itself never subjected to the
method. If the sessions had been cleared, it would have vanished without trace,
and nobody would have known to miss it.

## And now the one that matters

Two components of the method were never used. Not underused. **Zero times.**

The low-ceremony lane — where an idea can be tried and thrown away, no decision
record, no findings entry, no definition of done, one permitted output — shipped
on the first day with its rules, its README, and a test that enforces its one
constraint in continuous integration. It was used zero times in thirteen
experiments.

The third surface, for cross-experiment synthesis and work spanning many
artifacts, was designed into the workflow, given a role in the table, and used
zero times. The synthesis it existed for happened in a chat window and had to be
reconstructed afterwards from recollection.

The obvious reading is oversight. It is not, and the evidence against it is
specific and damning.

**The lane was built as a fix for exactly this failure, in the previous project,
where it had already cost something.** In that project a step was written up
twice and never started, accumulating five declared items, four of them open
questions, because the constitution had one standard — plan, decision record, findings, tests,
definition of done — and that standard is right for library code and far too
expensive for exploration. When a question is open and the only sanctioned move
is to write about it, uncertainty turns into documents. The diagnosis was made
explicitly. The remedy was designed explicitly. It was carried into the new
repository on day one, complete with enforcement.

And then the new project **did the same thing again.** Not by forgetting the
lane, but by never reaching for it, while writing preambles and specifications
and analyses about questions that could have been settled in twenty minutes by
trying them.

So the finding is not *the method lacked a lane for informal work.* It is:

> **A project with strong ceremony does not reach for its low-ceremony lane,
> even when the lane exists, is enforced, is documented, and was built
> specifically because its absence had already caused harm.**

The mechanism is not mysterious once stated. Every artifact that meets a high
standard raises the felt cost of producing one that does not. After ten
pre-registered experiments with falsifiers, verdicts and provenance, writing a
directory containing a rough script and no record does not feel like the
sanctioned move it formally is. **It feels like a lapse.** The rigour is
self-reinforcing, and self-reinforcement does not distinguish between the parts
of itself that are load-bearing and the parts that are ritual.

This has a second face which is worse. The formal parts of the method are the
ones that produce artifacts, and artifacts are the only thing the method can
see. A spike that would have settled a question in an afternoon leaves nothing
behind if it succeeds — the whole point is that it is deleted. **So the method is
structurally blind to the value of the work it is discouraging**, and the record
it produces will always show that the ceremony was worth it, because the record
is made of ceremony.

I felt this directly and did not name it at the time. There were several
afternoons of writing about a question — carefully, with pointers and open
questions and a plan for resolving it — where the honest move was to spend
twenty minutes finding out. The writing was good. It met the standard. It also
postponed the answer, and it was easier than admitting I did not know, because a
document that says *here are the four open questions* looks like progress and a
directory called `does-the-fixture-need-occlusion` looks like not knowing.

That is the thing a methodology cannot fix by adding a rule, which is why it is
the last section rather than a bullet in §4. **Adding the directory was not
enough. It was already there.**

## What might actually work

Not confident about this, and stating it as a proposal rather than a finding.

A **trigger** rather than a lane, in the same shape as the devil's advocate
pass: *when a question has been written about twice without being tested, it
goes to a spike.* Twice is countable. It fires on the observable — documents
produced — rather than on a judgement about whether something needs trying,
which is exactly the judgement the ceremony corrupts.

And a **default toward the cheap move at the moment of maximum uncertainty**.
The method's autonomy ladder governs how much the collaborator decides; nothing
governs how much rigour the artifact must carry, and the answer should vary. At
the point where a question is genuinely open, the standard should drop, not
rise.

Both are in the template. Neither has been tested, and the reader should treat
them accordingly — as the most recent guesses of someone who has now made this
mistake twice.

---

# 7. The template

The method described here is extracted into a repository template, public and
instantiable. This section says what is in it, what deliberately is not, and
what it does not yet know.

## What it contains

**A constitution.** The rules the file-holding surface operates under: what it
may do without asking, what requires permission, what it may never do. About a
third of the original was domain-specific — coordinate frames, units,
conventions particular to one problem — and that third is now an empty section
marked *domain invariants*, with the filled original visible beside it. The
blank is the template; the example is what makes the blank legible.

**A workflow.** The four-station loop, the three verdicts, the rule that every
specification carries a falsifier and names the repository state it assumes.
Plus the two additions §4 argued for: the devil's advocate pass with its
triggers, and the note that the reviewing surface's clone is a separate checkout
it reads and runs and never commits to.

**Two ledgers, as schema and prose headers with no entries.** Most of their
value is in the headers — the rule that one is written by the surface holding
the files and read by the surface that does not; the distinction between what is
derivable and what is intent; the procedure for reopening a closed decision,
which is to annotate and never reverse.

**An experiment exemplar.** Five empty files in the order they are written,
pre-registration first, with a short note on why the order is load-bearing.

**The low-ceremony lane**, with its rules, its enforcement test, and — per §6 —
its own record of non-use.

**A report scaffold**, including the claims-verification practice: prose drafted
in one format, typeset in another, both committed so the translation is
diffable, and a pass that checks every load-bearing claim at source before
anything is set.

**A list of specification defects**, which is the artifact §6 says did not
exist, seeded with the two that recurred.

## What it does not contain

No library code, no experiments, no ledger entries, no domain content. The rules
travel; the content does not.

Also absent, deliberately: several practices from the original project judged
specific to it rather than general. A migration audit of two particular
predecessors — the practice survives inside *carry only what can fail*, the
artifact does not. A provenance file for fixture data, which without any data
beside it is ceremony. A structural test resting on a decision the template's
user has not taken.

Each omission is recorded with its reason, which is the same discipline the
template applies to everything else.

## The rule the template is built on

One rule governed the extraction and it is worth stating on its own:

> **Every rule that ships carries the observed failure that motivated it, in one
> sentence.**

A rule without its reason gets simplified away by the next person to read it.
Someone encountering *mark carried methods at first use* with no explanation
will reasonably conclude it is bureaucratic and drop it. Someone encountering it
beside *a carried criterion governed ten experiments before anyone asked what it
tested* will not.

This has a consequence that took a moment to accept. **The template is mostly a
record of failures**, and it reads that way. That is correct. A methodology
presented as a set of good practices is a set of assertions; presented as a set
of failures with their remedies attached, it is evidence.

## What it does not know

The template was audited against one question: can a session starting cold, with
no other context, read it and write a first specification without asking what
any of it means? That audit found several gaps, and four were closed in a single
change. Its residue is argued below rather than recorded in the template, because
recording it would mean inventing rules the original project never exercised.

The largest: one of the method's own concepts — the distinction between
decisions that change what the project *is* and decisions about how to build it
— is defined in the template by an example from a layered software architecture.
For a project without that structure, the distinction has no test. It is a real
gap and the honest fix is for a second project to supply the general case by
having its own.

## And the thing to hold on to

The template's value is **unproven**, and its front page says so. One
researcher, one field, one project, five days. It does not claim to be a
validated methodology. What it claims is narrower and checkable: these rules
were exercised, several of them failed in specific recorded ways, and the fixes
are marked as new and untested.

There is one exception, and it is the only place in the template where a rule is
caught working rather than argued for. The check for figures repeated across a
document fired on the template's own front page, where a count had been taken
from the highest identifier rather than from the set — and the figure had been
repeated in a second file, so correcting the first would have left the second
standing. The tree-wide search found it; a re-reading would not have.

That is a small error about an unimportant number. It is also, exactly, the
failure this whole method exists to prevent, occurring in the provenance
paragraph of the document that ships the remedy. It is recorded there, beside
the rule, for that reason.

---

# 8. Reflection

## 8.1 The bottleneck moved

Thirteen experiments in five working days. At no point was implementation the limiting
resource.

What limited the work was **trust** — and specifically, one human reading. Every
pull request, every ledger entry, every claimed number. The apparatus in §4
exists because implementation stopped being scarce and verification did not, and
a practice built for the old scarcity will optimise the wrong thing.

That inversion has consequences beyond a single project. Research training is
organised around production: how to design an experiment, implement it, analyse
it, write it up. The implicit model is that thinking is fast and building is
slow, so rigour can be afforded because you are waiting for the build anyway.
Reverse it — building becomes fast, checking stays slow — and rigour stops being
something you have time for and becomes the thing you spend your time on.

This is not a lament. It is arguably a better allocation. But it is not the one
anyone was trained for, and a researcher who keeps optimising production will
produce more than they can vouch for, faster, without ever noticing the moment
it happened.

## 8.2 Confident and wrong has no analogue in the tools we inherited

Version control, testing, code review, continuous integration: every one of them
was built for artifacts that **break loudly**. A test fails. A type does not
check. A merge conflicts. The entire apparatus of software engineering is a set
of amplifiers for a signal that already exists.

A wrong belief emits no signal. It is internally consistent by construction —
that is what makes it believable — and it passes every check because it is not a
defect in an artifact but a defect in what someone concluded from one. The green
badge and the wrong claim are perfectly compatible, and in this project they
coexisted for ten experiments.

We have almost no tools for this. Pre-registration is one, borrowed from
clinical trials and psychology, and it is telling that the borrowing was
necessary — computational research had not needed it while the cost of running
an experiment was itself a check on how many you could run and how loosely you
could interpret them.

The practices in §4 are, I think, the beginning of an answer rather than an
answer. Non-ratification, provenance on every carried figure, a falsifier for
the specification and not just for the hypothesis: these are attempts to make a
wrong belief *break loudly*, by manufacturing the signal that does not naturally
exist. Whether they are the right attempts is exactly what a second project
would find out.

## 8.3 The unfashionable deliverable

The most reusable thing this project produced is not the code, and not its one
positive result. It is a ledger of thirteen foreclosed possibilities, each with
the evidence that closed it, the conditions under which it holds, and the cost
of reopening it.

Someone building a system of this kind now knows several things not to try, and
why. That is a different sort of result from a benchmark number, and I would
argue a more durable one: a benchmark is superseded by the next method, while a
well-founded elimination stays eliminated until someone changes the assumptions
it rested on — which the ledger states, so they can check.

It is also almost unpublishable. There is no venue for *here are thirteen things
that do not work and the reasons*, no citation economy that rewards it, and no
obvious way to present it at a conference. That is a fact about publishing
rather than about the knowledge, and I want to state it plainly rather than
pretend the incentives are aligned: **the better this method works, the more of
its output takes a form the field does not reward.**

Which raises a question I cannot answer from one project. If AI collaboration
makes elimination cheap — and it does; most of these thirteen cost an afternoon
each — then a great deal of the total knowledge produced will be of a kind we
currently have no way to share. Either the practice changes to accommodate it,
or the knowledge stays in repositories that nobody reads.

## 8.4 That this report exists at all

These notes were produced under the method they describe, by the collaboration
they analyse, including their own claims-verification pass. The recursion is not
decoration. It is either the strongest available evidence for the method or a
closed loop, and I owe the reader a position on which.

The honest answer is: **both, in different parts, and the boundary is
checkable.**

The parts that are evidence are the ones where the method's mechanisms fired
against this document. The first claims pass ran on the technical report and
moved eleven of its eighteen substantive claims. The repeated-figure check fired on the template's own
front page. A specification about this work was rejected on a false premise
about which surface held which file. Those are not testimonials; they are
recorded events with commits attached, and a reader can go and look.

The part that is a closed loop is the argument. §6's finding — that a rigorous
project will not use its own informal lane — is my reading of my own behaviour,
produced in conversation with the collaborator whose behaviour is also under
examination. No mechanism checked it. It survived because it explained something
that had happened twice and because I recognised it, which is exactly the
standard §4.1 says is insufficient.

So: trust the events, weigh the arguments. That is the same instruction the
method gives about any of its own claims, and applying it here is not modesty
but consistency.

## 8.5 What I would want checked

Three things a second project would settle that this one could not.

**Whether the failures are the method's or mine.** One researcher. Every failure
in §6 is consistent with *this is what happens to a rigorous project* and
equally consistent with *this is what happens when this particular person is
given a rigorous framework*. I lean toward the first because informal exploration went
undone in two consecutive projects — in the first because there was no lane, in
the second although there was — but two is not many.

**Whether the mechanisms transfer or were shaped by the domain.**
Pre-registration with a falsifier works cleanly when an experiment produces a
number that can be compared against a threshold. Whether it works for research
whose outputs are qualitative, or exploratory, or where the interesting result
is a construction rather than a measurement, I do not know. I would guess the
falsifier survives and the threshold does not.

**Whether the record is readable by anyone but its author.** Nine thousand lines
of ledger, written by one collaborator, read by one human, in five working days. A
colleague opening it cold is the test that has not been run, and until it is,
*the repository is the memory* is a claim about a memory of one.

## 8.6 How did it feel

As stated at the beginning, this is a document written in collaboration between a researcher and an AI entity. The curious reader may be challenged to imagine how this collaboration actually took place—and perhaps even to identify who wrote which parts.

This subsection, starting with its very title, is the only one for which our readership can be certain that it was written by a human—because a machine does not have feelings, right?

So, let us rephrase the question that cries out for an answer: **“How did it feel to partner with an AI?”** (Which, by the way, I prefer to call an *entity*, not an *agent*.)

Unfortunately, it is indescribable. Like jazz, you have to experience it to know. It is certainly different, and it feels new. It is here to stay, but each one of us, as humans, must find the answer in our own inner way.

On the other hand, for endeavors such as the one described in this document, we can say that the collaboration is a kind of *contract* whose terms the two parties must learn to negotiate in order for things to work out. It is also a moving target, because everything is changing at a rapid pace and requires us to learn as we go.

But since, as a researcher, I am naturally drawn to discovery as well as to the unknown, I can assure you that **“It Feels Good!”**

## 8.7 What I would tell a student starting now

For a scientist who is also a mentor and educator, this is perhaps the question of a lifetime. It has two inseparable sides: one seen from the perspective of the teacher, and the other from that of the student. Together, they reveal an intrinsic interdependence of purpose, learning, and aspiration.

The present moment is changing not only how we learn, but also what is worth learning. The emphasis is gradually moving away from mechanical procedures and the memorization of rules—the kinds of tasks that machines can now perform remarkably well and with increasing ease. What becomes more important, then, are basic principles, fundamentals, genuine understanding, intuition, judgment, and creativity. And, of course, talent helps.

In that spirit, the advice I would give is simple: “Discover the things you love and the things you are good at. Find where they meet, and pursue that path.”

Perhaps education, in this new context, is less about preparing someone to follow a predefined path and more about helping them acquire the confidence and understanding needed to discover one of their own.

## 8.8 Is this a good way to spend a career?

To answer this question, we may first need to reconsider what we mean by a *career*. In this new context, perhaps the traditional idea of a career—a more or less predefined trajectory through a profession—will no longer be the most useful one.

A career may increasingly become something that is continuously invented: a sequence of questions, discoveries, collaborations, changes of direction, and new beginnings.

So, to close briefly, I would return to the advice of the previous subsection: discover what you care about, discover what you can contribute, and invent your own career around the intersection of the two.

If you can do that, perhaps the question of whether it is a good way to spend a career becomes less important.

It may simply become a good way to spend a lifetime.

---

# Appendix A. Availability

Four public repositories. The first two are the predecessors these notes refer
to; the third is the project the examples come from; the fourth is the template
§7 describes.

- **`visgraf/bioeye`** — a thin vertical slice through the framework, written
  first. It closed the accumulation loop and not the perception–action loop.
- **`visgraf/active-stereo`** — a full implementation with verified geometry and
  a decision record. The loop never ran. Both the failure that motivated the
  low-ceremony lane and the constitution clause that talked the reviewer out of
  verifying are in this repository's history.
- **`visgraf/bio-3d-vision`** — the project. Thirteen experiments, each with its
  pre-registration, runner, raw results, verdicts and findings; two ledgers; a
  technical report with its claims-verification pass; and a forward-only history
  in which every correction appears as an amendment.
- **`visgraf/math-ai-method`** — the template, instantiable.

Every claim these notes make about what happened can be checked in the third.
That is the point of having kept it.
