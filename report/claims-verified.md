# Claim verification — FIRST PASS, RUN 2026-09-08

**Verified at `9b58d1a`** against checkouts cloned into `.reference/`:
`instance` = `visgraf/bio-3d-vision` @ `5f8e39f`, `template` =
`visgraf/math-ai-method` @ `81a638e`, plus `active-stereo` and `bioeye` at their
default branches (unpinned — recorded as a limit, see *What this pass did not
do*).

**Scope: §§1–8.5.** Sections 8.6–8.8 are the first author's, first-person, and
make no checkable factual claims; they are out of scope and were not read for
claims. `gap-001` and `od-001` are closed by this pass.

**Superseded header, kept for the record —** *"Verified at `<commit>`"* against **cloned checkouts in `.reference/`, at the
SHAs pinned in `docs/inherited-measurements.yaml`** — principally
`visgraf/bio-3d-vision` at `5f8e39f`, and `visgraf/math-ai-method` for claims
about the template — plus `docs/state.yaml` and
`docs/inherited-measurements.yaml`.

> **THE SOURCES ARE IN ANOTHER REPOSITORY, AND THAT CHANGES THIS PASS'S
> CHARACTER.** The template assumed the record being checked against lived in the
> same tree: `experiments/exp0NN/verdicts.json`, a path that cannot rot because
> CI would notice. Here every source is a file in a repository this one does not
> contain, at a SHA that must be pinned by hand and can only be wrong silently.
> There is no equivalent of "the test suite would have caught it". **Cite by
> source key, path and SHA, never by path alone** — `instance:
> report/claims-verified.md @5f8e39f`, not `report/claims-verified.md`, which in
> this repository names a different file: *this* one.

**No prose is written and no `.tex` file is touched during a verification pass.**
This document is a verification pass, not a draft. Keeping the two apart is what
stops a claim from being fixed by softening the sentence that carries it.

---

## The practice

A verification pass takes every factual claim in the report, finds the thing in
the record that supports it, and marks it. **The claim is checked against the
source, not against the sentence that introduced it** — a report is internally
consistent by construction, and internal consistency is the one property a wrong
report is most likely to have.

Numbers arriving in prose are **hypotheses with pointers** until read at their
source. Open the file. Open the line.

### The verdicts

| verdict | meaning |
|---|---|
| **CONFIRMED** | true as written, at the scope the sentence states |
| **CORRECTED** | the number is wrong; the right one is given |
| **UNDER-QUALIFIED** | true in the band, arm, metric or stimulus it came from, and unsupported as written |
| **UNSUPPORTED** | nothing in the record establishes it |
| **PARTIAL** | verified except for a named part |

> **UNDER-QUALIFIED is the category that earns this document.** In the instance
> this template came from, 22 claims were checked: 10 confirmed, 3 corrected,
> **8 under-qualified**, 0 unsupported. Nothing was invented. Every claim traced
> to something real in the record, and the recurring defect throughout was scope
> and metric — *a figure measured on one metric, one band or one arm carried into
> a sentence that does not name it.* That is what a wrong belief looks like from
> the inside: not a fabrication, a correct number with its conditions filed off.

### What each entry records

Per claim, in this order:

1. The sentence, quoted from the report.
2. The verdict, in bold, with the correct figure if it moved.
3. The comparison, the arms, the `n`, and the stimulus.
4. **The source, by key, file and id.** The `docs/inherited-measurements.yaml`
   entry id, and — inside the pinned checkout — the experiment's
   `verdicts.json`, the findings file, the ledger entry, whichever actually
   holds it. **Name the source key** (`instance`, `template`, `active-stereo`,
   `bioeye`) so that a claim about the template is never filed as a claim about
   the instance. That confusion is a domain invariant in `CLAUDE.md` because the
   template's own front page has already made it.
5. Any caveat the source attaches to the value, quoted. *A caveat that lives only
   in the ledger does not travel; this is where it gets carried into the prose or
   consciously dropped.*
6. **Proposed:** the replacement sentence, when the verdict is not CONFIRMED.

---

## The repeated-claim check — do this with `grep`, not by reading

**Verification runs per passage. Repetition crosses passages.** A careful
per-passage reading structurally cannot catch a figure that is qualified
correctly in section 4 and stated bare in the abstract, because at the moment you
read the abstract you have not yet read section 4, and at the moment you read
section 4 the abstract is already marked CONFIRMED.

> *Observed, in the instance:* a ratio verified correctly and with its full
> stimulus scope in the policy section appeared in the abstract with the scope
> dropped, and was caught only on a second pass. A separate figure was wrong in
> **three** places at once — abstract, section 4.3 and section 5.1 — and correcting
> one would have left two.

**So the check is mechanical.** After the per-passage pass and before signing
off:

1. Extract every numeral, ratio, percentage and multiplier that appears in the
   typeset sources.

   **Run it over `report/draft.md`, which is where this report's prose lives**,
   and over the `.tex` sources once step 4 has typeset them. Both, once both
   exist — a figure that is correct in the draft and mangled in the typeset copy
   is the specific defect the draft/typeset split exists to expose.

   ```bash
   grep -onE '[0-9]+(\.[0-9]+)?(×|x|:1|%|-fold)?' report/draft.md \
     report/sections/*.tex report/main.tex 2>/dev/null \
     | sort -t: -k3 | uniq -c -f2 | sort -rn | head -40
   ```

   > **THE COMMAND AS SHIPPED DOES NOT WORK ON THIS DOCUMENT, and that is
   > recorded rather than patched over.** Run against `draft.md` it fails twice:
   > `uniq -c -f2` counts whitespace-separated fields, not the `:`-separated ones
   > `sort -t:` just ordered, so the whole output collapses to a single line; and
   > markdown section numbering means `4.1` and `8.6` are returned as repeated
   > figures while the prose's actual figures — *thirteen*, *eighteen*, *seven* —
   > are words and are not matched at all. **A numeral-only check misses most of
   > the claims in a document that spells its numbers out.** This is `od-003`;
   > the fix is not yet written, and the check must be validated against a known
   > answer (it has to surface the `mn-001`/`mn-002` pair) before it is trusted.
   > Until then, do this step by reading.

2. **For every figure that appears more than once, open all of its occurrences
   together.** Not in reading order — side by side. Ask of each: does this
   sentence carry the same scope as the others?
3. A figure that appears in *n* places has *n* claims attached to it, and this
   document gets *n* entries or one entry naming all *n* locations. It does not
   get one entry and a hope.
4. When a figure is corrected, **fix every occurrence in the same change.** Record
   the count in the resolution, so the next reader can tell a complete correction
   from a partial one.

**Round a bound in the direction that stays true.** A minimum quoted as "at least
33×" against an exact 33.5× is true; "at least 34×" is not. Rounding *down* is
the safe direction for a lower bound, and *up* for an upper one.

### This check has fired once, on the template's own prose

> **The `README.md` and `tests/test_scaffold.py` named below are the TEMPLATE's,
> at `81a638e` — not this repository's.** This repository's README is a different
> file and it has no test suite (`fc-001`, `fc-003`). The account is kept
> verbatim as an inherited record of an event in `template`, because the whole
> point of it is that it is a real event with commits attached; do not go looking
> for these files here, and do not restate the event as something that happened
> in this repository.

Worth recording, because it is the only place in the template where a rule is
shown catching the failure it was written for — and it caught it in the document
that ships the rule.

`README.md` described the source instance as having **fourteen** experiments. It
has thirteen: the count had been taken from the highest identifier (`exp014`)
rather than from the set, and `exp006` was specified and deliberately not run.

**The figure was in two places.** It had been repeated in a test docstring in
`tests/test_scaffold.py`. A per-passage reading would have corrected the
`README` line and left the other standing — which is exactly the structural
blind spot this section describes, occurring in the paragraph about *this
template's own provenance*, in a template whose stated purpose is preventing
claims that are well-formed, plausible and wrong.

**The tree-wide grep is what found the second one.** Not a re-reading. Run over
every figure asserted about the instance, it also confirmed the rest were
consistent across their occurrences — 45 of 96 nulls, ten experiments, five
days, eleven fields — and turned up two loose counts in illustrative prose,
one of which was sitting inside the new entry about counts taken loosely.

The full defect and its check are `docs/spec-defects.md` §3.

### A second candidate, found here, and NOT by this check

Recorded so the two are not confused. Adapting the template surfaced `mn-001` /
`mn-002`: the instance's verification tally stated as *22 claims / 10 confirmed*
in this file and as *eighteen load-bearing / seven stood* in `report/draft.md`,
agreeing exactly on 3 corrected and 8 under-qualified.

**It was found by reading the two documents against each other, not by the grep**
— and it could not have been found by the grep as written, since the figures are
spelled out as words in the draft (`od-003`). It is not yet a verdict: both
statements are recorded as inherited and unresolved, and reconciling them is
`od-002`, which is blocked on `gap-001` like everything else here. The likely
reconciliation is a subset selector — `met-002`, the undefined word
"load-bearing" — which would make this an UNDER-QUALIFIED defect in the
documents that define the category.

---

## The count

| verdict | n | claims |
|---|---|---|
| **CONFIRMED** | **22** | 2, 3, 4, 6, 7, 8, 9, 10, 15, 18, 19, 23, 28, 32, 33, 36, 39, 40, 42, 43, 44, 47 |
| **CORRECTED** | **5** | 22, 24, 26, 29, 41 |
| **UNDER-QUALIFIED** | **8** | 1, 5, 11, 14, 21, 27, 31, 46 |
| **UNSUPPORTED** | **6** | 12, 17, 20, 25, 38, 45 |
| **PARTIAL** | **1** | 13 |
| total | **42** | |

**The recurring defect, in one sentence:** *a figure lifted correctly from the
record and re-attached to the wrong noun* — iterations read as days, gaps closed
read as gaps open, a criterion experiment counted as a stimulus experiment.

**This is not the defect the source pass found, and the difference is
structural.** The instance's own first pass reported scope-and-metric as its
recurring failure: a correct number quoted without the band it came from. That
is a *first-order* defect — the defect of a report standing next to its own
measurements. This document is second-order: it restates figures that were
already condensed once, and its characteristic error is therefore
**transcription**, not scope. Three of the five corrections are the same shape —
the source says "twice in seven iterations" and the draft says "for a week"
(claim 24); the record shows numbers marked from day one and the draft says day
two (claim 22); a commit says "close four cold-start gaps" and the draft says
"four remain open" (claim 41). In each case the number survived and the noun
attached to it did not.

### On falsifier 2 — it fires, and neither offered explanation is the right one

The specification said: *if UNDER-QUALIFIED does not substantially outnumber
CORRECTED, either this draft is unusually well-scoped or the category is being
applied too loosely.* The ratio here is **8 : 5 = 1.6 : 1**, against the
instance's **8 : 3 = 2.7 : 1**. It does not substantially outnumber, so the
falsifier fires.

**I do not think either branch is the explanation, and I think the category was
applied correctly.** UNDER-QUALIFIED is not depressed — 8 is the same absolute
count the source pass found. **CORRECTED is elevated**, from 3 to 5, and the
reason is the second-order structure above: a document that quotes a report
inherits a class of error a report cannot make, because a report is written
beside its measurements and this one is written from a reading of them. If that
is right, the prediction is testable and worth recording: **a third-order
document would show more corrections still**, and the UNDER-QUALIFIED-dominates
pattern is a property of first-order reports rather than of prose in general.

### On falsifier 3 — it fires hardest, and the pattern is not random

**Six claims are UNSUPPORTED — not contradicted, unestablishable.** The
specification predicted what this would mean: §4.5's failure occurring in the
document that describes it. It is that, and it is sharper than that, because
**the unsupported claims are not scattered. Five of the six are about an event
the workflow guarantees will leave no artifact.**

> **Two counts, both right, recorded rather than reconciled away.** *Four* are
> unrecordable **by construction** — the workflow guarantees no artifact
> (claims 17 and 20 live in specifications, which are never committed; 12 is a
> rate over conversational turns; 25 is a cleared session's search). *Five*
> "describe an event the workflow guarantees will leave no trace", the selector
> §6's *The method destroys its own best evidence* uses, which also admits claim
> 45: the afternoons a foreclosure cost were events, and nothing logs duration.
> **Claim 38 is the odd one out under either selector** — not an event at all,
> but a proportion of a document that still exists, so it is unsupported and
> *measurable*, and the only one of the six a successor could close by looking.
> This is `mn-001`/`mn-002` again: two numbers, two selectors, neither wrong.
> See `gap-004`.

| claim | what it asserts | why no record exists |
|---|---|---|
| 12 | false claims "at a rate of roughly one per day" | a rate over conversations; nothing counts them |
| 17 | "three specifications were rejected on false assumptions" | **specifications are never committed** — `docs/workflow.md` says so explicitly: the loop's central artifact is "the only one that leaves no trace in the repository" |
| 20 | "three times" an outcome fell outside every enumerated falsifier direction | the misses are in specifications, not verdicts |
| 25 | a cold session "found six of eighteen steps inferable… and refused to invent the rest" | the search happened in a cleared session |
| 38 | "about a third of the original was domain-specific" | no measurement of the original's composition |
| 45 | "most of these thirteen cost an afternoon each" | no per-decision time record |

**A rejected specification is the strongest evidence the method has and the only
kind it systematically destroys.** Claim 17 is the sharpest case: §4.2 calls the
rejections "the clearest case in the project of a rule paying for itself", and a
rejection that stops work before it starts produces no branch, no commit and no
verdict. The one rejection that *is* in the record survived only because it
changed the shape of a foreclosure that was taken anyway (`fc-012`), and it was
not a stale-state rejection at all.

**This is a finding about the method, not only about the draft.** The workflow
records what work *produced*; it has no channel for work that was correctly
prevented. `docs/state.yaml`'s `falsifier_verdicts` block exists to keep the
falsifier after the specification evaporates — the same argument extends, and
does not yet reach, the rejections. Recorded as `od-006`.

---

## §1 Register

### 1. "One researcher, one field, one project, five days of intensive work"
**UNDER-QUALIFIED — five *working* days spanning eight calendar days.**
- The instance's commits fall on five distinct dates: 2026-08-29, 08-30, 08-31, 09-01 and **09-05**. First commit 08-29 09:56, last 09-05.
- Source: `git log` over `instance` @5f8e39f.
- "Five days of intensive work" (§1) is right. **"Thirteen experiments over five days" (§3:304) and "Thirteen experiments in five days" (§8.1:1138) read as elapsed time and the elapsed time is eight days**, with a four-day gap before the last.
- The figure recurs at :72, :304, :810, :1115, :1138, :1257 and is consistent in every one — it is the *noun* that varies, not the number.

**Proposed:** "five working days" wherever the sentence is about elapsed time.

---

## §2 The setting

### 2. The predecessor's constitution ruled out in-repo verification — *"Chat holds excerpts by construction, so 'Chat verifies Code's numbers' would rot into a formality"*
**CONFIRMED, verbatim, including the attribution.**
- Source: `active-stereo: CLAUDE.md:141` (§5, "The handoff contract"). Quoted word for word.
- The draft attributes it to "the predecessor project's constitution". Correct. **This is the attribution the template itself had to fix once** — `template` commit `2b6d482` records correcting it from bio-3d-vision to active-stereo — and the draft has it right.

### 3. Cowork was used zero times
**CONFIRMED.** `template: docs/workflow.md` surfaces table — "**no. Not once in five days.**" No artifact in `instance` is attributable to it.

### 4. `spikes/` shipped on the first day with rules, README and a CI-enforced constraint, and was used zero times in thirteen experiments
**CONFIRMED, on all four parts.**
- Shipped `2026-08-29 11:45` (`9fb4ef8`), the project's first day.
- `instance: tests/test_scaffold.py:54` — `test_governed_trees_do_not_import_spikes`.
- **`git log --diff-filter=A -- spikes/` returns exactly one path ever added: `spikes/README.md`.** No spike was ever created.

### 5. In the predecessor "a step was written up twice and never started, accumulating five open questions"
**UNDER-QUALIFIED — written up twice and never started is exact; four of the five are open questions.**
- Step 6 has a lab-notebook preamble (`active-stereo: docs/lab-notebook/2026-08-25-step-6-preamble.md`) and a block in `docs/plans/fixation-migration.md:214` — **two write-ups**.
- Never started: the only step-6 commits are `2e0a148` (the preamble) and its merge `3f7a263`, **which is the repository's HEAD**. The predecessor's last act was writing up a step it never began.
- The block is headed "*Declared open questions*" and carries five lettered items **a–e**. Item **b** states: "**The static-path guard is not an open question.** … it has a specified fix and must not be reopened as a choice."

**Proposed:** "accumulating five declared items, four of them open questions".

---

## §3 The project

### 6. "Thirteen experiments"
**CONFIRMED by enumeration**, not by highest identifier: `exp001`–`exp005` and `exp007`–`exp014` in `instance: experiments/`. No `exp006`; `am-004` records it as specified and deliberately not run.

### 7. "each pre-registered before its runner existed"
**CONFIRMED** on the three spot-checked (exp001, exp010, exp013): `preregistration.md` is added in an earlier commit than `run.py` in every case (exp001 13:58 vs 14:50; exp010 15:08 vs 15:22; exp013 19:43 vs 20:01).

### 8. "Roughly four thousand lines of library code against a slightly larger volume of tests"
**CONFIRMED, and unusually precisely.** `src/` = **4,363** lines; `tests/` = **4,416**. Tests exceed library by 1.2% — "slightly larger" is exact.

### 9. "Thirteen foreclosed decisions"
**CONFIRMED.** `instance: docs/state.yaml` `foreclosures` — 13 entries.

### 10. "Eighty-seven measurements taken in the project and forty-one inherited"
**CONFIRMED.** `instance: docs/inherited-measurements.yaml` `measurements` — 139 entries: **87 `measured`, 41 `inherited`, 11 `gap`.**
- *Caveat the source attaches and the sentence drops:* the ledger's third status. Eleven recorded gaps are measurements deliberately **not** made, and the ledger argues their absence is as citable as a number. A reader totalling 87 + 41 = 128 will not find the other 11.

### 11. "Four of the thirteen experiments turned out to be about the instrument rather than the framework"
**UNDER-QUALIFIED — the source's phrase is "the instrument *or the criterion*", and the second half is the half that matters.**
- The four are exp004, exp005, exp008 and **exp012**. exp012 is the re-analysis of `met-001`, the inherited statistical bar — **a criterion, not an instrument**.
- Source: `instance: report/claims-verified.md` claim 29, which marks exactly this compression **CORRECTED** in the instance's own second pass: "*Three about the stimulus, one about the criterion.*" `instance: report/draft.md:315` states it correctly.
- The draft's "instrument" is closer than the Abstract's "stimulus" that the source corrected, and still drops the criterion.

**Proposed:** "about the instrument or the criterion rather than the framework".

---

## §4.1 Fluent wrong claims

### 12. "The conversational surface asserted false things at a rate of roughly one per day"
**UNSUPPORTED.** Four instances are named and three trace to the record (claim 13). **Nothing counts assertions, and no denominator exists**: the rate is over conversational turns, which are not retained. Four named instances over five working days is *consistent with* the claim and does not establish it.

### 13. The four named false claims
**PARTIAL — three of four trace to the record; the fourth does not.**
- *"a confidence failure replicated across two stimulus families, when the record showed the two families disagreeing in sign"* — **CONFIRMED**. `instance: report/claims-verified.md` claim 16, CORRECTED, and its own summary says claim 16 "**inverts the finding**".
- *"a foreclosure asserted to be settled by an experiment that had measured something else entirely"* — **CONFIRMED**. `template: docs/workflow.md` records it: a completed step read "Decide the plant", the id resolved, and the foreclosure decided the disparity search window; "none of its eleven fields mentioned a plant".
- *"a count of experiments taken from the highest identifier rather than from the set"* — **CONFIRMED**. `template: docs/spec-defects.md` §3, and `template` commit `931f6d3`.
- *"a statistic described as frozen across a run when it drifted by a small amount that mattered"* — **not located.** No entry in either ledger, and no commit body, matches. Not marked unsupported on its own because the other three establish the pattern; recorded so it is not read as verified.

### 14. "Of eighteen claims in the first draft, seven stood as written." (§4.1:391)
**UNDER-QUALIFIED — and this is the third location of a figure corrected in two others.**
- The figures are right (see `mn-001`, `mn-002`, and `od-002`'s resolution): 22 claims checked, 18 substantive, 7 of the 18 stood.
- **This sentence names neither the pass nor the subset**, and the instance ran **two** passes. It says "eighteen claims", not "eighteen substantive claims", and "the first draft" rather than the first pass.
- **The same figure was amended at :870 and :1219 in commit `9b58d1a` and NOT here**, because the specification limited prose edits to od-002's sentence. That leaves the document internally inconsistent, which the repeated-claim rule in this file exists to prevent. **It is the single most important item for the maintainer.**

**Proposed:** "Of the eighteen substantive claims in the first pass, seven stood as written."

### 15. "Nearly three times as many under-qualified as outright mistakes"
**CONFIRMED.** 8 UNDER-QUALIFIED against 3 CORRECTED in the instance's first pass = 2.67 : 1. "Nearly three times" rounds in the direction that stays true.

---

## §4.2 Stale state

### 16. *(merged into claim 17)*

### 17. "Three specifications were rejected on false assumptions/premises" — §4.2:433 and §5:806; and "specifications drafted against a commit that had advanced — twice" §4.2:412
**UNSUPPORTED, and structurally so. This is the pass's most important finding.**
- **One** rejection is in the record: `instance: docs/state.yaml` records at two points that the `fc-012` rectification specification "WAS REJECTED BECAUSE IT MAKES AZIMUTH AND VERGENCE INERT". Both mentions are the same event.
- **That rejection was not on a false assumption about repository state.** It was rejected on a geometry defect — composed alone, rectification makes azimuth and vergence inert and a closed loop would re-render an identical image after every saccade. It is §4.3's failure mode, not §4.2's.
- **No record of the other two can exist.** `docs/workflow.md`: a specification is "the only [artifact] that leaves no trace in the repository… In the instance this template came from, no specification was ever committed." A specification rejected *before any work was spent* produces no branch and no commit by construction.
- The `fc-012` rejection survived only because it changed the shape of a foreclosure that was taken anyway.

**This is a gap in the method, not only in the draft.** See `od-006`.

---

## §4.3 Work that cannot fail

### 18. "A property nobody noticed for ten experiments" / "governed ten experiments"
**CONFIRMED, and the ten are enumerable.** `instance` `met-001.re_derived_here`: "Used unexamined in exp001, exp002, exp003, exp004, exp005, exp007, exp008, exp009, exp010 and exp011 — every comparison this repository has ever scored." Exactly ten. Recurs at :460, :524, :662, :819, :826, :904, :1089, :1169 and is consistent throughout.

### 19. "The spread is a sample standard deviation, so it does not shrink with more samples… No number of seeds could ever resolve anything"
**CONFIRMED.** `met-001`: "exp011 was the first iteration to notice it is a SAMPLE STANDARD DEVIATION and not a standard error, and exp012 is the first to measure what that costs: **45 of 96 nulls (46.9%)** read differently under the other bar (bio-074)."

### 20. "Three times the actual outcome fell outside every direction the falsifier had enumerated"
**UNSUPPORTED.** The remedy is confirmed — the four-direction enumeration with "**(d) REVERSES DIRECTION**" appears in `exp007/preregistration.md:116` and `exp011/preregistration.md:119`, so the practice demonstrably changed. **The count of three is not recorded anywhere**: the misses are properties of specifications, which are not committed. Same structural cause as claim 17.

---

## §4.4 Inherited assumptions

### 21. "Thirteen carried methods, eight of which had never been examined"
**UNDER-QUALIFIED — both numbers are right and the word joining them is not.**
- The `methods` section holds **13 entries**, of which **10** are `kind: carried`; 2 are `choice` and 1 is `measurement`.
- **Exactly 8** carry `status: never_examined` — and `template` commit `f135d43`'s subject says so independently: "*exp012: one foreclosure moved, and **eight constants were never examined***".
- **One of the eight (`met-002`) is `kind: choice`** — a value this project chose deliberately and said why — so it is not a carried method. The set of thirteen is "methods", not "carried methods".

**Proposed:** "Thirteen carried constants and criteria, ten of them carried in from elsewhere, eight never examined by anyone in this project."

### 22. "Applied to numbers on day two and to methods at experiment twelve" (§4.4:534, repeated §6:899)
**CORRECTED. Numbers were marked on day ONE, not day two.**
- `instance: docs/inherited-measurements.yaml` was created at **2026-08-29 11:45** (`9fb4ef8`), one hour forty-nine minutes after the repository's initial stub (09:56) — **and it already contained 42 entries carrying `status: inherited`.**
- The methods half is confirmed: `methods:` first appears at `f135d43`, **2026-08-31 17:45**, in the exp012 commit. `met-001.status` = `examined_at_exp012`.
- **The error runs against the draft's own interest.** The asymmetry it is describing is *worse* than stated — one day versus experiment twelve, not two days — so the correction strengthens the finding. The same "day two" appears in `template: CLAUDE.md`, so it is inherited rather than invented here.

**Proposed:** "Applied to numbers on day one and to methods at experiment twelve."

---

## §4.5 Knowledge that lives only in a conversation

### 23. "An eighteen-step plan, with stages, altitudes, and two recorded amendments, existed in a chat window and nowhere else"
**CONFIRMED on every element, at the moment of the event.** At `19d2723`, the commit that first wrote the plan into the repository: **18 steps** across **5 stages**, altitude tags present (`fw`, `geom`, `infra`), and **exactly two amendments** — `am-001`, `am-002`. The commit message says so: "Eighteen steps in five stages, with altitude tags, statuses, and the two amendments taken so far."
- *Note for any future quotation:* the ledger now carries **nine** amendments at `5f8e39f`. The claim is correct **because it is scoped to the moment**, and would be wrong as a statement about the file today.

### 24. "It had shaped every specification for a week"
**CORRECTED. For one day — nine and a half hours, and seven merged pull requests.**
- The repository's first commit is `e3a17cf`, **2026-08-29 09:56**. The plan was recorded at `19d2723`, **2026-08-29 19:34 — the same day.**
- Pull requests #1–#7 were merged in between, so the plan governed **seven iterations**, not seven days.
- **The likely origin of the error is in the record itself**: `sequence.plan.amended` reads "**twice in seven iterations**", and `19d2723`'s own message repeats "eighteen steps amended twice in seven iterations". *Iterations became days.* That is claim 31's error in a different unit and this pass's recurring defect in its purest form.

**Proposed:** "It had shaped every specification for a day — seven merged pull requests — before anyone wrote it down."

### 25. The cold session "searched the repository, the git history including commit bodies, and both reference checkouts, found six of eighteen steps inferable from side-references in old prompts and none of the stage groupings, and refused to invent the rest"
**UNSUPPORTED.**
- No occurrence of "six", "inferable", "side-reference" or any equivalent appears in `instance`'s tree or in any commit body.
- The nearest recorded figure points the other way: at `19d2723` the **position** half lists **eight** completed steps with evidence (1–4, 7–10) plus two deferred — but that is derived from the foreclosure ledger, which is a different operation from reconstructing the plan.
- **The refusal is the load-bearing part of the anecdote and there is no artifact for it.** §4.5's own thesis is that knowledge living only in a conversation cannot be detected from inside it; its central example is knowledge that lived only in a conversation.

---

## §4.6 The instrument you authored

### 26. "The synthetic fixture was an order of magnitude worse in the tail"
**CORRECTED → 22.7× at p90.**
| AT band | fixture | render | ratio |
|---|---|---|---|
| median | 0.02050 | 0.01248 | 1.64× |
| **p90** | **1.49626** | **0.06580** | **22.7×** |
- Source: `instance: experiments/exp004_scene_model_check/findings.md`, falsifier 2; 8 seeds, policy A′, 18 fixations, AT = within 10 px of a depth discontinuity.
- **The draft is already better than the sentence the source corrected.** The instance's claim 12 was CORRECTED for saying "roughly an order of magnitude" *unscoped*; the draft adds "**in the tail**", which is the p90 scope the source demanded. What remains is the figure: 22.7× is more than twice "an order of magnitude".
- *Caveat the source attaches:* "the 48× that appears in `docs/state.yaml` is `diff / bar`, a distinguishability multiple, and **must not be read as an error ratio**."

**Proposed:** "roughly twenty times worse in the tail".

### 27. "Two fifths of the measured pixels, four fifths of the total error"
**UNDER-QUALIFIED — the denominator was carried across correctly and the word "squared" was not.**
- Measured: AT pixels are **38.23%** of the **53,098 valid measured pixels** and carry **82.27% of total squared error**. Source: `instance: experiments/exp005_stratified_reanalysis/preregistration.md:35` — measured **before** the run.
- The instance's claim 13 was UNDER-QUALIFIED on **two** grounds: the denominator was "the image" (wrong — over the image AT is 26.4%), and the error is **squared**. **The draft fixes the first and drops the second.** Half a correction travelled.
- *Do not conflate with `bio-007`*, a different statement about the same fixture: the worst 5% of valid pixels carry 80.9% of squared error. Two different pixel sets, both landing near four fifths.

**Proposed:** "two fifths of the valid measured pixels, four fifths of the total *squared* error".

### 28. "It passed the validity test built to catch exactly that class of failure"
**CONFIRMED — and more precisely worded than the sentence the source corrected.**
- The instance's claim 14 was UNDER-QUALIFIED for saying "passes left–right consistency", because LR is one of two conjuncts in `valid = (distinct > 0.10) & agree` (`src/bio3dvision/matching.py:102-104`) and was never isolated.
- The draft says "the validity test", which is the conjunction — the source's own proposed repair. Measured: **78.5%** of AT pixels marked valid, **21.7%** of those wrong by more than 2 px.

### 29. "Four of thirteen experiments went to establishing this" (:620) and "roughly a third of the project's experiments" (:638)
**CORRECTED → three.**
- "This" is the fixture artefact. Per `instance: report/claims-verified.md` claim 29, the four are exp004, exp005, exp008 and exp012, and **exp012 is the criterion re-analysis, not a stimulus experiment**: "Three about the stimulus, one about the criterion."
- **This is the sharper form of claim 11.** In §3 the sentence says "about the instrument", which merely drops a disjunct; here the four are attributed *to the fixture finding specifically*, which is the error the source corrected.
- Consequently "roughly a third" (4/13 = 31%) becomes **3/13 = 23%**, closer to a quarter.

**Proposed:** "Three of thirteen experiments went to establishing this… at a cost of roughly a quarter of the project's experiments."

---

## §5 What it cost, and what it caught

### 31. "Two of thirteen iterations produced no new science"
**UNDER-QUALIFIED — the units do not match.**
- The two are the claims-verification pass and the re-scoring. **The re-scoring is exp012, one of the thirteen experiments; the claims pass is not an experiment at all**, so the numerator mixes an experiment with a non-experiment while the denominator counts experiments.
- The project's own unit of iteration is the merged pull request: **30** of them at `5f8e39f`. On that denominator the ratio is 2 of 30.
- "Thirteen" carries three different referents across the draft — experiments (:329, :620, :941), foreclosures (:307, :1187) and iterations (:798). The first two happen to coincide at 13; the third does not.

**Proposed:** "Two of thirteen experiments' worth of effort produced no new science" — or state the iteration denominator.

### 32. "Nine thousand lines of ledger in five days" (:810, repeated §8.5:1256)
**CONFIRMED.** `docs/state.yaml` 4,054 + `docs/inherited-measurements.yaml` 5,190 = **9,244 lines**. "Nine thousand" rounds down, which is the direction that stays true. ("Five days" carries claim 1's qualifier.)

### 33. "The verification iteration found three wrong figures and eight claims true only in the condition they were measured under"
**CONFIRMED.** First pass: CORRECTED 3 (claims 6, 12, 16); UNDER-QUALIFIED 8 (1, 3, 7, 10, 11, 13, 14, 15).

---

## §6 Where the method failed

### 36. "The same two errors recurred: bundling a bounded task with an unbounded one, and naming a branch without asking for a commit"
**CONFIRMED.** `template: docs/spec-defects.md` §1 and §2, and its own header: "The list below opens with the two observed in the instance this template came from."

### 37. "Used zero times in thirteen experiments" — both components
**CONFIRMED.** See claims 3 and 4.

---

## §7 The template

### 38. "About a third of the original was domain-specific"
**UNSUPPORTED.** `template: CLAUDE.md` does carry an empty `## Domain invariants` section with a filled example beside it, exactly as described. **The proportion is not measured anywhere**, and the instance's CLAUDE.md is not partitioned in a way that makes "a third" checkable without a judgement about which paragraphs count as domain-specific.

### 39. "An experiment exemplar. Five empty files in the order they are written, pre-registration first, with a short note on why the order is load-bearing"
**CONFIRMED.** `template: experiments/exp000_example/` holds six files: the five exemplar files plus `README.md`, whose line 3 reads "Five files, and **the order they are written in is the whole point**" and which carries a section headed "Why the order is load-bearing".

### 40. "A list of specification defects… seeded with the two that recurred"
**CONFIRMED.** The file carries three entries at `81a638e`, and says so itself: it "opens with the two observed in the instance", the third being the count defect found in the template's own prose. "Seeded with" is accurate about origin.

### 41. "That audit found several gaps, most of which were closed. **Four remain open** and are recorded in the repository rather than fixed"
**CORRECTED. The four in the record are four gaps CLOSED, not four left open.**
- `template` commit `2b6d482`: "**docs: close four cold-start gaps** and carry the draft/typeset practice — Five fixes from the cold-start audit."
- `template` commit `a2ce623`: "docs: **close the two gaps these fixes opened**."
- **No record of four open gaps exists.** `README.md`'s "What this template does not do" carries **three** bullets, and they are stated limitations rather than audit findings.
- The gap the draft calls "the largest" is real (claim 42) — but it is argued in the draft, not recorded in the template.

**Proposed:** either "four gaps were closed and the audit's residue is argued in §7 rather than recorded", or record the four in the template and cite them.

### 42. The framework/implementation distinction "is defined in the template by an example from a layered software architecture"
**CONFIRMED.** `template: docs/state.yaml:279` defines altitude `fw` as "Changes the shape of the thing: **interfaces between layers**, what a type means, what the project is committed to." A project without layers has no test for the distinction.

### 43. The repeated-figure check fired on the template's own front page
**CONFIRMED in every particular**, from `template` commit `931f6d3`:
- "The source instance has THIRTEEN experiments, not fourteen… **The count had been taken from the highest identifier rather than from the set.**"
- "**CORRECTED IN BOTH PLACES IT APPEARED.** README.md carried it, and a test docstring had picked it up and repeated it — so fixing the source alone would have left one standing."
- "Then ran the template's own repeated-claim grep **over the whole tree**" — confirming the draft's "the tree-wide search found it; a re-reading would not have".
- The same commit independently confirms that "45 of 96 nulls, ten experiments, five days" are consistent across their occurrences in the template.

---

## §8 Reflection (8.1–8.5)

### 44. "A ledger of thirteen foreclosed possibilities, each with the evidence that closed it, the conditions under which it holds, and the cost of reopening it"
**CONFIRMED.** 13 foreclosures; the schema carries `rationale`, `scope` and `cost_to_reopen`, and `scope` is a required field.

### 45. "Most of these thirteen cost an afternoon each"
**UNSUPPORTED.** No per-decision time is recorded anywhere. The commit timeline shows several experiments completed within a few hours (exp001 pre-registered 13:58, findings 14:54), which is *consistent with* the claim for some, and no record establishes it for "most".

### 46. "The low-ceremony lane went unused in two consecutive projects under different conditions"
**UNDER-QUALIFIED — the lane existed in one of the two.**
- `active-stereo` has **no `spikes/` directory** and never did. Its failure was the *absence* of a lane: a step written up twice and never started (claim 5).
- §6 states this correctly — the lane "was built as a fix for exactly this failure, in the previous project" and "was carried into the new repository on day one". §8.5 compresses that into the lane going unused twice, which asserts it existed twice.
- **The underlying argument survives**: the *behaviour* — not reaching for informal work — did recur across both projects. That is the claim §8.5 needs and not the one it makes.

**Proposed:** "informal exploration went undone in two consecutive projects — in the first because there was no lane, in the second although there was."

### 47. "Nine thousand lines of ledger, written by one collaborator, read by one human, in five days"
**CONFIRMED** on the count (claim 32); "five days" carries claim 1's qualifier.

---

# Addendum — §6, *The method destroys its own best evidence*

**Checked at the same pinned SHAs, on the revised text.** Seven checkable
claims: **five CONFIRMED, one CORRECTED, one UNDER-QUALIFIED.** Numbered A1–A7
and kept out of `mn-004`'s tally, which covers §§1–8.5 as they stood at the
first pass.

### A1. "§4.2 describes three specifications rejected… *the clearest case in the project of a rule paying for itself*"
**CONFIRMED.** Quoted accurately from §4.2.

### A2. "That claim came back from the verification pass **unsupported**"
**CONFIRMED.** Claim 17, UNSUPPORTED.

### A3. "**No specification was ever committed.** No file in the instance is one, and none is named as one."
**CONFIRMED, and this is the sentence the previous round got wrong.** Re-checked
at `instance` @`5f8e39f`: no tracked file is a specification, and no filename
matches *spec*, *task*, *brief*, *instruction*, *relay* or *prompt* — zero hits.
The earlier form, *"no specification text survives anywhere"*, was false. This
form is true.

### A4. "One rejection survives… it reshaped a decision that was taken anyway… not even a stale-state rejection"
**CONFIRMED on all three parts.** `fc-012`'s entry: "THAT VERSION WAS REJECTED
BECAUSE IT MAKES AZIMUTH AND VERGENCE INERT, and the rejection is the reason
this entry exists in the form it does." The decision was taken; the rejection
was on a geometry defect, not a repository-state assumption.

### A5. "Five of the six unsupported claims… describe events the workflow guarantees will leave no trace"
**CONFIRMED under the selector the sentence states** — admits 12, 17, 20, 25, 45;
excludes 38, which is a proportion of a document rather than an event. A stricter
selector ("unrecordable by construction") gives four. Both recorded; see
`gap-004`.

### A6. "**Three** passages in the instance quote specification text"
**CORRECTED → four passages report specification content, and one of the three named is not one of them.**

| passage | reports spec content? | what it does |
|---|---|---|
| `exp007/preregistration.md:38` | **yes** | quotes it — the specification says "six arms, one stimulus" |
| `exp009/preregistration.md:19` | **yes** | reports the clause, then argues it is wrong |
| `exp007/findings.md:123` | **yes** | "The specification said 18 steps for A, A′, D and E", under a heading reading *"A deviation from the specification, and why"* |
| `exp007/findings.md:32` | **yes** | "The specification asked for this to be visible rather than inferred, and it is" |
| `exp007/findings.md:46` | **no** | "the correct reading, which neither exp005 nor this specification stated" — **records an ABSENCE in the specification.** The blockquote after it is the findings file's own reading, not the specification's words. |

- **The third named fragment is the one that does not qualify**, and
  `exp007/findings.md:123` — omitted — is the clearest instance of the section's
  own thesis: an artifact departing from a specification clause and quoting it to
  say so.
- **This is my error propagating, and it is worth naming as such.** The
  search behind the previous round returned *four* hits and the report said
  *three*: `findings.md:123` was in the output and never opened. The section was
  then written from that summary. See `docs/spec-defects.md` §6.

**Proposed:** "Four passages in the instance report specification text — a
pre-registration quoting a clause before departing from it, another quoting an
instruction and then arguing it is wrong, a findings file recording a deviation
and the clause it deviates from, and one recording that the specification asked
for something that was duly delivered."

### A7. "**Every one is text that an artifact was arguing with.**"
**UNDER-QUALIFIED — true of three of the four, and the fourth is a counterexample.**
- Arguing: `exp007/preregistration.md:38` (declares a design change),
  `exp009/preregistration.md:19` ("The second half is wrong"),
  `exp007/findings.md:123` ("A deviation from the specification, and why").
- **Not arguing:** `exp007/findings.md:32` — "The specification asked for this to
  be visible rather than inferred, **and it is**." An artifact *agreeing* with a
  specification and carrying its content into the record.

**THE SECTION'S CONCLUSION SURVIVES INTACT, AND THIS IS THE IMPORTANT PART.** The
load-bearing sentence is the next one — *the survival mechanism is parasitic on
the work happening* — and `findings.md:32` satisfies it completely: agreement or
disagreement, the fragment is there because the specification was **executed**
and produced an artifact. A rejected specification produces no artifact either
way. **"Arguing with" is too narrow a mechanism for a conclusion that only needs
"executed".** Narrowing it costs the argument nothing and removes a false
universal.

**Proposed:** "Every one is text that an artifact had to reckon with — mostly to
depart from it, once to confirm it."

---

# Resolutions

## What resolved

| claim | was | resolution |
|---|---|---|
| 14 (partial) | "eighteen load-bearing claims… seven stood" at :870 and :1219, naming neither pass nor subset | Amended in `9b58d1a` to name the first pass and the substantive subset. **:391 was left standing** — see below. |
| — | `od-005`: section 8.6 unwritten | 8.6, 8.7 and 8.8 are written; the draft's status block corrected in `9b58d1a`. |
| — | `od-002`: mn-001 and mn-002 disagree | Both correct; different denominators. Resolved at source, `mn-003` added for the dropped PARTIAL. |
| — | `gap-001`: no source cloned | Closed. Four checkouts in `.reference/`. |

## What is still flagged and was not corrected

**APPLIED 2026-09-08.** All 13 proposed replacements — every CORRECTED and every
UNDER-QUALIFIED claim — were applied to `report/draft.md` by the maintainer's
wholesale approval. They touched **20 passages**, because five claims recur:

| claim | verdict | locations changed |
|---|---|---|
| 1 | UNDER-QUALIFIED | 4 of 6 "five days" — the two register descriptors (§1, §7) were left, per the entry, since they are not about elapsed time |
| 5 | UNDER-QUALIFIED | 3 — §2, §6, **and §6's later "here are the five open questions"**, which the check caught and the entry had not named |
| 11 | UNDER-QUALIFIED | 1 |
| 14 | UNDER-QUALIFIED | 1 — §4.1:398, the third occurrence the previous commit left inconsistent |
| 21 | UNDER-QUALIFIED | 1 |
| 22 | CORRECTED | 2 — §4.4 and §6 |
| 24 | CORRECTED | 1 |
| 26 | CORRECTED | 1 |
| 27 | UNDER-QUALIFIED | 1 |
| 29 | CORRECTED | 2 — the count and the proportion that follows from it |
| 31 | UNDER-QUALIFIED | 1 |
| 41 | CORRECTED | 1 — first option taken; the second would require editing `template` |
| 46 | UNDER-QUALIFIED | 1 |

**Two entries offered alternatives and the first was taken in both** (31 and 41).
For 41 the second option — record the four gaps in the template and cite them —
is not available from this repository.

### Still standing: the six UNSUPPORTED claims

**12, 17, 20, 25, 38, 45 are unchanged in the prose.** They carry no proposed
replacement because none can be written from the record: four of the six describe
events the workflow guarantees leave no artifact. `gap-004` and `od-006` hold the
argument. **This is the maintainer's decision and it has not been taken** — the
options are to soften each to what the record supports, or to keep them and say
in the text that they rest on recollection.

---


# The repeated-figure check, as run — and the fix for `od-003`

**The shipped command does not work on this document, exactly as `od-003`
predicted.** Run over `report/draft.md` it returns a single line — `52 1023:7` —
because `uniq -c -f2` skips *whitespace*-separated fields while `sort -t:` has
just ordered colon-separated ones, so every record collapses into one group. It
also matches only numerals, and this document spells its figures out.

**What was run instead**, and what `od-003` should adopt:

```sh
# Repeated-figure check for prose that spells its numbers out.
#   1. words as well as numerals;
#   2. group on the VALUE with awk, not `uniq -f2`;
#   3. -H so the field offsets hold for one file as well as many;
#   4. drop bare decimals -- in markdown they are section numbers, not claims.
for f in "$@"; do
  grep -onHEi '\b([0-9]+(\.[0-9]+)?(×|x|:1|%|-fold)?|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|eighteen|twenty-two|forty-one|eighty-seven|thousand)\b' "$f" \
  | grep -vE ':[0-9]+\.[0-9]+$'
done | awk -F: '{v=tolower($3); n[v]=n[v]" "$2} END {for (v in n) {c=split(n[v],a," "); if (c>1) printf "%3d  %-12s lines:%s\n", c, v, n[v]}}' | sort -rn
```

> **`-i`, AND THE GROUPING LOWERCASED TOO — ADDED AFTER THE CHECK WAS ALREADY
> SHIPPED AS `od-003`'s FIX.** The first version was case-sensitive, so it saw
> "three passages" and missed "Three passages". Measured over these files:
> **252 hits case-sensitive against 301 case-insensitive — it was missing 49, or
> 16%, and the missed class was every sentence-initial figure.** Prose puts
> figures at the start of sentences constantly.
>
> It was found by hand: a figure known to be in §6 did not appear in the output.
> **A check that silently drops a sixth of its input is worse than no check,
> because it is reported as a clean run** — which is `docs/spec-defects.md` §6
> in the tool built to prevent §6's defect. Both halves matter: `-i` on the grep
> finds the hits, and `tolower` in the awk stops "Three" and "three" from being
> counted as two different figures.

**It was validated against a known answer before being trusted**, which the
shipped one never was: it had to surface the `mn-001`/`mn-002` pair, and it does
— "eighteen" at seven locations and "twenty-two" at two.

**What it found that a per-passage reading did not:**

1. **"eighteen" carries two unrelated figures** — eighteen claims (:391, :872, :882, :1222) and an eighteen-**step plan** (:554, :561). A reader meeting the second after the first has to notice the noun changed.
2. **"thirteen" carries three** — experiments, foreclosures, and iterations (:798). The first two coincide at 13 by accident; the third does not, which is claim 31.
3. **Claim 14's third location.** :391 is in §4.1 and the other occurrences are in §5 and §8.4 — three sections apart. This is precisely the structural blind spot: at :391 the reader has not yet read §5, and by §5 the §4.1 sentence is already behind them.

**Its limit, stated so it is not over-trusted:** the word list is enumerated, so a
figure written as a word not on the list is missed. The list covers every
spelled-out figure this draft uses; it will need extending for the next document,
and that is a maintenance cost, not a one-time fix.

---

# What this pass did not do

- **No prose was written and no `.tex` file was touched.** The two amendments in `9b58d1a` were made before this pass, under the specification's explicit exception, and are recorded as claim 14's partial resolution.
- **`active-stereo` and `bioeye` are unpinned.** They were cloned at their default branches, not at a recorded SHA, because none is pinned in `docs/inherited-measurements.yaml`. Claims 2, 5 and 46 rest on them. `active-stereo`'s HEAD is `3f7a263` and `bioeye`'s is `e908170`; **pin them before quoting those claims**, or a later reader is citing whatever `main` says the day they read it.
- **Nothing was re-run.** Every figure above is read from a committed artifact or computed from `git log` over a pinned checkout.
- **§§8.6–8.8 were not read for claims**, per the specification's scope.
- **Claim 13's fourth instance was not located**, and is recorded as PARTIAL rather than silently dropped.
