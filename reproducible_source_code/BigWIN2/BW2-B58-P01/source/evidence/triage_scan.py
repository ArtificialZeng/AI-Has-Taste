#!/usr/bin/env python3
"""Exact smoke test for triage; finite coverage is not a proof.

Checks all rational v=k/d with 2<=d<=100 and 0<=k<d for n=2,3.
All interval endpoints, masses, and costs use fractions.Fraction.
"""

from fractions import Fraction as F
from math import floor


def fractional_part(x: F) -> F:
    return x - F(x.numerator // x.denominator)


def z(y: F) -> F:
    return fractional_part(F(1, 2) - y)


def decomposition(v: F):
    alpha = fractional_part(20 * v)
    beta = fractional_part(41 * v)
    endpoints = sorted(
        {
            F(0),
            F(1),
            F(1, 2),
            beta,
            fractional_part(F(1, 2) - alpha),
            fractional_part(F(1, 2) - v),
        }
    )
    pieces = []
    for left, right in zip(endpoints, endpoints[1:]):
        sample = (left + right) / 2
        height = (
            2 * floor(20 * v)
            - floor(41 * v)
            + 2 * int(z(sample) < alpha)
            - int(z(sample) < v)
            + int(sample > beta)
        )
        pieces.append((left, right, height))
    return pieces


def lowest_cost(v: F, target_mass: F) -> F:
    # For fixed v the oscillation of h_v is at most four. Since the tested
    # target mass is below four, r=0,...,7 contains every possibly selected
    # rung, with ample slack.
    levels = []
    for left, right, height in decomposition(v):
        for rung in range(8):
            levels.append((height + 2 * rung, right - left))
    levels.sort()
    mass = F(0)
    cost = F(0)
    for value, available in levels:
        take = min(available, target_mass - mass)
        if take > 0:
            mass += take
            cost += value * take
        if mass == target_mass:
            return cost
    raise AssertionError("rung cutoff insufficient")


checked = 0
for denominator in range(2, 101):
    for numerator in range(denominator):
        v = F(numerator, denominator)
        for n in (2, 3):
            left = lowest_cost(v, n + v)
            right = n * n + lowest_cost(v, 1 + v) - 1
            checked += 1
            if left != right:
                raise SystemExit(
                    f"mismatch: v={v}, n={n}, lhs={left}, rhs={right}, "
                    f"decomposition={decomposition(v)}"
                )

print(f"PASS: {checked} exact (v,n) checks; no mismatch found")
print("Coverage: v=k/d, 2<=d<=100, 0<=k<d; n in {2,3}")
print("Interpretation: finite smoke test only, not proof of the universal claim")

