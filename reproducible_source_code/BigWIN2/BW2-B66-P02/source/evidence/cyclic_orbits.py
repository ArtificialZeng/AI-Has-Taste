#!/usr/bin/env python3
"""Enumerate inverse-closed generating subsets of Z_n modulo Aut(Z_n)."""

from math import gcd


def orbit_representatives(n):
    elements = range(1, n)
    candidates = []
    for mask in range(1 << (n - 1)):
        subset = frozenset(x for i, x in enumerate(elements) if mask >> i & 1)
        if subset == frozenset((-x) % n for x in subset) and gcd(n, *subset) == 1:
            candidates.append(subset)

    units = [u for u in range(1, n) if gcd(u, n) == 1]
    unseen = set(candidates)
    representatives = []
    while unseen:
        representative = min(unseen, key=lambda s: (len(s), tuple(sorted(s))))
        orbit = {
            frozenset((u * x) % n for x in representative)
            for u in units
        }
        unseen -= orbit
        representatives.append(representative)
    return candidates, representatives


if __name__ == "__main__":
    for order in range(2, 11):
        sets, reps = orbit_representatives(order)
        print(
            order,
            "sets=", len(sets),
            "Aut_orbits=", len(reps),
            "representatives=", [sorted(rep) for rep in reps],
        )

