#!/usr/bin/env python3
"""Exact defect-set simulation for the Section 6 family 1(01)^k."""


def rule115(left: int, center: int, right: int) -> int:
    return (115 >> (4 * left + 2 * center + right)) & 1


def step(bg_b: int, bg_c: int, b_def: set[int], c_def: set[int]):
    """Advance uniform background plus finite symmetric-difference sets."""
    next_bg_b = bg_c
    next_bg_c = bg_b ^ rule115(bg_c, bg_c, bg_c)
    next_b_def = set(c_def)
    candidates = set(b_def)
    for site in c_def:
        candidates.update((site - 1, site, site + 1))
    next_c_def = set()
    for site in candidates:
        b = bg_b ^ (site in b_def)
        left = bg_c ^ (site - 1 in c_def)
        center = bg_c ^ (site in c_def)
        right = bg_c ^ (site + 1 in c_def)
        value = b ^ rule115(left, center, right)
        if value != next_bg_c:
            next_c_def.add(site)
    return next_bg_b, next_bg_c, next_b_def, next_c_def


def least_period(family_k: int, cutoff: int) -> int | None:
    # Memory is u.  The centered current word is 1(01)^k.
    initial = (0, 0, {0}, set(range(-family_k, family_k + 1, 2)))
    state = initial
    for time in range(1, cutoff + 1):
        state = step(*state)
        if state == initial:
            return time
    return None


def formula(i: int) -> int:
    return (2 * 4 ** (2 * i + 2) - 7 * 4 ** (i + 1) + 5) // 3


if __name__ == "__main__":
    for i in range(4):
        predicted = formula(i)
        observed = least_period(2 * i, predicted)
        print(
            f"i={i} family_k={2*i} predicted={predicted} "
            f"first_return={observed} match={observed == predicted}"
        )
