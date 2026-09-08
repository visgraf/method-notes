# Claim verification — TEMPLATE

**Verified at `<commit>`** against the experiments' `findings.md`,
`preregistration.md` and `results.json`, `docs/state.yaml` and
`docs/inherited-measurements.yaml`.

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
4. **The source, by file and id.** `docs/inherited-measurements.yaml` entry id,
   the experiment's `verdicts.json`, the findings file — whichever actually
   holds it.
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

   ```bash
   grep -onE '[0-9]+(\.[0-9]+)?(×|x|:1|%|-fold)?' report/sections/*.tex report/main.tex \
     | sort -t: -k3 | uniq -c -f2 | sort -rn | head -40
   ```

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

### This check has fired once, on this template's own prose

Worth recording, because it is the only place in this repository where a rule is
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

---

## The count

Fill this in. It is a measurement about the drafting process and it is the reason
the pass is worth its cost — a tally that is 0 UNSUPPORTED and 8
UNDER-QUALIFIED says something specific and actionable about how the prose is
going wrong, which "we checked it" does not.

| verdict | n | claims |
|---|---|---|
| **CONFIRMED** |  |  |
| **CORRECTED** |  |  |
| **UNDER-QUALIFIED** |  |  |
| **UNSUPPORTED** |  |  |
| **PARTIAL** |  |  |
| total |  |  |

**The recurring defect, in one sentence:** _____

---

## <Section name>

### 1. "<the sentence, quoted from the report>"

**VERDICT.** <The correct figure, if it moved.>

- Comparison: <what against what, on which metric>
- Arms / conditions: <...>
- `n`, budget, stimulus: <...>
- Source: `docs/inherited-measurements.yaml` <id>; `experiments/<exp>/verdicts.json`

<Any caveat the source attaches, quoted.>

**Proposed:** "<the replacement sentence>"

<!-- Repeat per claim, grouped by report section. -->

---

# Resolutions

Record what was actually changed, separately from what was flagged. Two lists,
and both are needed:

## What resolved

| claim | was | resolution |
|---|---|---|
|  |  |  |

## What is still flagged and was not corrected

Claims raised and left standing, with whose call it is. **Record these even when
— especially when — the decision is to leave them.** A flag that is dropped
silently is indistinguishable from a flag that was addressed, and the difference
is the whole value of the pass.
