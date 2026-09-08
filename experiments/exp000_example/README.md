# exp000_example — the shape of an experiment

Five files, and **the order they are written in is the whole point**. They are
shipped empty because the shape is what carries; the contents are yours.

```
preregistration.md   written and committed ALONE, before the runner exists
run.py               the runner
results.json         what it produced, raw
verdicts.json        results scored against the pre-registered rule
findings.md          what it means, and which falsifiers fired
```

## Why the order is load-bearing

**The order is the entire mechanism.** Every one of these files could be written
in any sequence and the directory would look identical afterwards. What the order
buys is that **the threshold is fixed before the numbers exist** — and the git
history is the only thing that can prove it was.

> *The failure it prevents:* not fraud. The ordinary case is that you run the
> thing, look at the numbers, and *then* decide what counts as a difference —
> and every choice you make at that point feels like judgement rather than
> selection. A threshold chosen after seeing the data lets any outcome be the
> desired one, and it does not feel like that from the inside.

So:

**1. `preregistration.md` is committed alone, in its own commit, before any
runner exists.** Alone, so that `git log` shows a commit containing the
threshold and nothing that could have produced a number. That commit is the
evidence. It is cheap to make and impossible to reconstruct afterwards.

**2. `run.py` produces `results.json` and does not score it.** The runner writes
what it measured. Keeping scoring out of it means the scoring code can be read
against the pre-registration by someone who has not looked at the results.

**3. `verdicts.json` applies the pre-registered rule, mechanically.** It records,
per comparison and per metric: the difference, the bar, **which clause of the bar
was binding**, and the verdict. Recording which clause bound is what later makes
it possible to ask what the criterion was actually testing — exactly the question
that went unasked for ten experiments in the instance this template came from
(`met-000-EXAMPLE` in `docs/inherited-measurements.yaml`).

**4. `findings.md` is written last and states which falsifiers fired**, including
the ones that did not. It reports the outcome the pre-registration did not
predict as prominently as the one it did.

**And when the protocol says to stop, stop.** A pre-registration that declares a
check — a grid resolution, a sanity condition, a control that must hold — and
then fails it has produced a result. In the instance, a declared stride check
failed on the first run; the protocol said reduce the stride and discard the run,
and following it cost one re-run and turned up a fact about the objective that
anticipated the main finding. The alternative was to report the discarded run.

## What goes in the preregistration

Written before the fact, and none of it revisable afterwards without an
amendment recorded in `findings.md`:

- **The question**, and why it is worth an experiment rather than an argument.
- **The arms**, and what differs between them. Name what differs *besides* the
  thing under test — the confound you already know about is the one you can
  declare, and declaring it lets you say in advance what you will do if it bites.
- **The metrics**, split into primary (the verdict rests on these) and secondary
  (reported, decisive of nothing). Say which is which before you know which one
  moves.
- **The threshold**, stated as a formula. If it is carried from somewhere else,
  it gets an entry in `docs/inherited-measurements.yaml` under `methods` **now**,
  not when someone doubts it.
- **The falsifier for the specification itself** — what result would mean this
  experiment asked the wrong question. See `docs/workflow.md`.
- **Declared limitations, before the fact.** What this experiment forecloses and
  what it cannot: the stimulus it does not have, the regime it does not cover.
  This is where a finding's scope is fixed, and scope is what gets dropped
  between here and the report.
- **What each outcome means**, enumerated in advance. Every branch, including the
  surprising one. If you cannot say in advance what a result would mean, you will
  say afterwards that it means whatever it turned out to be.

## Naming

`experiments/expNNN_short_question/`. Numbered so ordering is unambiguous in the
record, named after the question rather than the method.

## On this directory

`exp000_example` is not an experiment and produced nothing. Delete it once you
have a real one, or keep it as a checklist — but do not let it accumulate
contents, because an example experiment with plausible-looking numbers in it is a
thing somebody will eventually cite.
