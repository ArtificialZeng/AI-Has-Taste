#!/usr/bin/env python3
"""Exact verification of power-set--chain weighting counterexamples."""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple


EXAMPLES = (
    # power, |K|, chain length
    (0, 2, 4),
    (1, 5, 7),
    (2, 7, 53),
    (3, 9, 212),
    (4, 10, 573),
)


if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")


def formula_value(power: int, k: int, q: int) -> int:
    size = (1 << k) + q
    old_frequency = (1 << (k - 1)) + q
    return (
        k * (old_frequency ** power) * q
        + sum((i ** power) * (2 * i - size) for i in range(1, q + 1))
    )


def construct(k: int, q: int) -> Tuple[int, ...]:
    old_mask = (1 << k) - 1
    power_set = range(1 << k)
    chain = []
    chain_mask = 0
    for index in range(q):
        chain_mask |= 1 << (k + index)
        chain.append(old_mask | chain_mask)
    return tuple(power_set) + tuple(chain)


def is_union_closed(family: Sequence[int]) -> bool:
    members = set(family)
    return all(left | right in members for left in family for right in family)


def direct_value(family: Sequence[int], points: int, power: int) -> Tuple[int, List[int]]:
    frequencies = [
        sum(1 for member in family if member & (1 << point))
        for point in range(points)
    ]
    size = len(family)
    value = sum(
        (frequency ** power) * (2 * frequency - size)
        for frequency in frequencies
    )
    return value, frequencies


def verify_example(power: int, k: int, q: int) -> None:
    expected = formula_value(power, k, q)
    assert expected < 0
    family = construct(k, q)
    assert len(family) == (1 << k) + q
    assert len(set(family)) == len(family)
    assert is_union_closed(family)
    value, frequencies = direct_value(family, k + q, power)
    assert value == expected
    assert frequencies[:k] == [(1 << (k - 1)) + q] * k
    assert sorted(frequencies[k:]) == list(range(1, q + 1))

    # Incidence columns are pairwise distinct.  Use exact Python integers as
    # bit vectors indexed by family members.
    signatures = []
    for point in range(k + q):
        signature = 0
        for member_index, member in enumerate(family):
            if member & (1 << point):
                signature |= 1 << member_index
        signatures.append(signature)
    assert len(set(signatures)) == k + q
    print(
        f"p={power}, k={k}, q={q}, sets={len(family)}, "
        f"points={k + q}, W={value}: PASS"
    )


def main() -> None:
    for example in EXAMPLES:
        verify_example(*example)
    print("POWER-CHAIN NO-GO CERTIFICATE PASS")


if __name__ == "__main__":
    main()
