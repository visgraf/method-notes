"""The library. RENAME THIS PACKAGE -- see pyproject.toml.

Flat as shipped, with no opinion about structure, because structure is a decision
and this template has not taken it for you. If you add subpackages, take that
decision explicitly and record it in ``docs/state.yaml`` as a foreclosure with
its rationale.

    A measured argument for staying flat, from the instance this template came
    from: its predecessor grew a directory per architectural layer, and a
    directory per layer invites filling it. The result was a library 42.1% of
    which was stimulus infrastructure, against 9.1% for the three layers the
    framework was actually named for. Every individual step had been reasonable.

That is an argument, not a rule, and it is offered rather than enforced. What is
NOT optional is CLAUDE.md's rule about where authority lives: units, frames,
conventions and the meaning of a returned value are declared in the docstring of
the function that returns them, never in a governance file.
"""

#: The public surface. Stated here so that a change to it has to pass through a
#: diff; pinned sorted by tests/test_scaffold.py.
__all__: list[str] = []
