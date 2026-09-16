"""Independent bit-packed RESOCA-115 checker using the rule's ANF.

This does not import the truth table or state constructors from the dense
reference implementation.
"""

from __future__ import annotations

from typing import Iterable, Tuple


PackedState = Tuple[int, int, int]


def background_bit(time: int) -> int:
    return 1 if time % 3 == 1 else 0


def make_initial(k: int) -> PackedState:
    """Return phase and packed layers on W_k=[-k-1,k]."""

    if k < 1:
        raise ValueError("the odd-parameter target has k >= 1")
    width = 2 * k + 2
    memory = 1 << (k + 1)  # site 0 has offset k+1 from -k-1
    current = 0
    # Word 1(01)^k occupies offsets 1,3,...,2k+1.
    for offset in range(1, width, 2):
        current |= 1 << offset
    return 0, memory, current


def anf_scalar(left: int, center: int, right: int) -> int:
    """Scalar ANF: 1+x+l*x+l*x*r over GF(2)."""

    return 1 ^ center ^ (left & center) ^ (left & center & right)


def packed_step(state: PackedState, width: int) -> PackedState:
    phase, memory, current = state
    mask = (1 << width) - 1
    ghost = background_bit(phase)
    lefts = (current << 1) & mask
    rights = current >> 1
    if ghost:
        lefts |= 1
        rights |= 1 << (width - 1)
    # Vectorized ANF, with ``mask`` representing the constant-one term.
    local = mask ^ current ^ (lefts & current) ^ (lefts & current & rights)
    updated = (memory ^ local) & mask
    return (phase + 1) % 3, current, updated


def unpack(state: PackedState, width: int) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    phase, memory, current = state
    return (
        phase,
        tuple((memory >> pos) & 1 for pos in range(width)),
        tuple((current >> pos) & 1 for pos in range(width)),
    )


def packed_trajectory(k: int, steps: int) -> Iterable[PackedState]:
    width = 2 * k + 2
    state = make_initial(k)
    yield state
    for _ in range(steps):
        state = packed_step(state, width)
        yield state


def exact_period_packed(k: int, max_steps: int | None = None) -> int:
    start = make_initial(k)
    state = start
    width = 2 * k + 2
    elapsed = 0
    while max_steps is None or elapsed < max_steps:
        state = packed_step(state, width)
        elapsed += 1
        if state == start:
            return elapsed
    raise RuntimeError(f"no return for k={k} within {max_steps} steps")

