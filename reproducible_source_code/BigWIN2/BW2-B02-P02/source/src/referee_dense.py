"""Independent dense reference simulator for the locked RESOCA-115 orbit.

This implementation deliberately uses the eight-entry Wolfram truth table,
not the algebraic normal form used by ``referee_bitpacked.py``.
"""

from __future__ import annotations

from typing import Iterable, Tuple


# Indices are the binary integers lxr, from 000 through 111.
RULE_115 = (1, 1, 0, 0, 1, 1, 1, 0)

DenseState = Tuple[int, Tuple[int, ...], Tuple[int, ...]]


def background(time: int) -> int:
    """The current layer of the all-zero initial pair at integer time."""

    return int(time % 3 == 1)


def initial_state(k: int) -> DenseState:
    """Return phase, memory, current on W_k=[-k-1,k]."""

    if k < 1:
        raise ValueError("the odd-parameter target has k >= 1")
    sites = tuple(range(-k - 1, k + 1))
    memory = tuple(int(site == 0) for site in sites)
    current = tuple(
        int(-k <= site <= k and (site + k) % 2 == 0) for site in sites
    )
    return 0, memory, current


def local_table(left: int, center: int, right: int) -> int:
    """Evaluate rule 115 directly from its Wolfram truth table."""

    return RULE_115[(left << 2) | (center << 1) | right]


def step(state: DenseState) -> DenseState:
    """Advance the fixed-window state by one exact RESOCA time step."""

    phase, memory, current = state
    ghost = background(phase)
    width = len(current)
    updated = []
    for pos in range(width):
        left = ghost if pos == 0 else current[pos - 1]
        right = ghost if pos + 1 == width else current[pos + 1]
        updated.append(memory[pos] ^ local_table(left, current[pos], right))
    return (phase + 1) % 3, current, tuple(updated)


def trajectory(k: int, steps: int) -> Iterable[DenseState]:
    """Yield times 0,...,steps for diagnostic cross-checks."""

    state = initial_state(k)
    yield state
    for _ in range(steps):
        state = step(state)
        yield state


def exact_period(k: int, max_steps: int | None = None) -> int:
    """Enumerate positive times and return the first full-state return.

    Sequential enumeration makes minimality exact.  ``max_steps`` is only a
    resource guard; reaching it is an error, not evidence about the period.
    """

    start = initial_state(k)
    state = start
    elapsed = 0
    while max_steps is None or elapsed < max_steps:
        state = step(state)
        elapsed += 1
        if state == start:
            return elapsed
    raise RuntimeError(f"no return for k={k} within {max_steps} steps")

