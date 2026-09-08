# spikes/

Where you try things. This is the low-ceremony part of the repository, and the
low ceremony is the point: an idea should be cheap to test and cheap to throw
away.

## The trigger

**A question written about twice without being tested goes to a spike.**

That is the rule. It is not "use spikes when they seem useful", because that is
what the instance this template came from had, and it produced a directory that
shipped on day one — with its rules, its enforcement test and its README — and
was **never used once in five days**.

> *The failure it is aimed at:* in the predecessor repository, a step was written
> up twice and never started, accumulating five open questions, because writing a
> document was the only sanctioned response to not knowing. `spikes/` was
> invented to fix that. Adding the directory did not fix it. A trigger is the
> fix.

The trigger is written to be countable rather than to be wise. If a question has
appeared in two documents — two specifications, a specification and a findings
file, an open decision that has been restated, a paragraph of a report and the
state file — and no code has been run against it, the next thing that happens is
a spike. Not a third document.

Note what the trigger measures: **not how hard the question is, and not how
important.** Twice-written is a proxy for "we keep reasoning about this instead
of looking", which is the actual failure, and it has the advantage of being
visible from outside the head of the person doing it.

## The rules

**Git-tracked.** Spikes are committed. A spike that lives only on your disk
cannot be pointed at, and the whole reason this directory exists is so that "I
tried that, here is what happened" is a thing you can show.

**No decision record. No findings entry. No definition of done.** None of them
apply here. Do not write a foreclosure *about* a spike — a decision is recorded
after the thing it decides has been tried, so the spike is what you do *before*
the record, and the record comes after if the answer was worth keeping.

**No tests required.** Write them if they help you; nothing checks.

**Not importable.** Nothing in `src/` or `experiments/` may import from here.
Enforced by `tests/test_scaffold.py`, which CI runs. If the library needs
something a spike has, that is the signal to write it properly in `src/` — with
tests — not to import it from here.
> *Why the ban is enforced rather than stated:* a lane whose whole value is that
> it has no rules stops having that value the moment something with rules
> depends on it. The first import is the one that turns a scratch directory into
> untested production code, and it never announces itself as that.

**The only permitted output is a decision or a deletion.**

- *A decision:* write what you learned into `docs/state.yaml` — an open decision
  resolved, a new one opened, or a foreclosure with its reason — and then delete
  the spike.
- *A deletion:* it did not work, or it stopped being interesting. Delete it. The
  git history keeps it if anyone ever wants it.

A spike that is neither — still sitting there, not deciding anything, not
deleted — is the failure mode this directory has. It should go. Ask, and then
delete it.

## Naming

`spikes/<short-question>/`. Name it after the question you are answering, not
the technique you are using: `does-the-fixture-need-occlusion/`, not
`numpy-warp-test/`. When the question is answered the directory's name tells you
the spike is finished.
