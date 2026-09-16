#!/usr/bin/env python3
"""Exact degree-multiset filter for the order-17 C4-free target.

Uses only integer arithmetic and the Erdos--Gallai characterization. The
mathematical inputs and each filtering stage are printed for auditability.
"""

from math import comb

N = 17
TARGET = 123
MAX_EDGES = 36
# If m is the edge count, Cauchy and TARGET = (sum(d^2)-2m)/2 give
# TARGET >= 2m^2/N-m; at m=37 the right side is already greater than 123.


def is_graphical(degrees):
    """Return Erdos--Gallai graphicality for a nonincreasing tuple."""
    if sum(degrees) % 2:
        return False
    for k in range(1, len(degrees) + 1):
        left = sum(degrees[:k])
        right = k * (k - 1) + sum(min(d, k) for d in degrees[k:])
        if left > right:
            return False
    return True


arithmetic = []


def enumerate_degrees(remaining_vertices, largest, remaining_target, prefix):
    if remaining_vertices == 0:
        if remaining_target != 0:
            return
        degrees = tuple(prefix)
        if not (5 <= degrees[0] <= 9):
            return
        if sum(degrees) % 2 or sum(degrees) // 2 > MAX_EDGES:
            return
        arithmetic.append(degrees)
        return

    for degree in range(min(largest, 9), 0, -1):
        contribution = comb(degree, 2)
        if contribution > remaining_target:
            continue
        rest = remaining_target - contribution
        if rest > (remaining_vertices - 1) * comb(degree, 2):
            continue
        enumerate_degrees(
            remaining_vertices - 1, degree, rest, prefix + [degree]
        )


enumerate_degrees(N, 9, TARGET, [])
graphical = [degrees for degrees in arithmetic if is_graphical(degrees)]


def satisfies_lemma_5_3(degrees):
    total = sum(comb(d - 1, 2) for d in degrees)
    return all(
        comb(N - d, 2) >= total - comb(d - 1, 2) for d in degrees
    )


survivors = [degrees for degrees in graphical if satisfies_lemma_5_3(degrees)]

print("n=17 target_sum_binom=123 degree_range=1..9 max_edges=36")
print(f"arithmetic={len(arithmetic)}")
print(f"graphical={len(graphical)}")
print(f"lemma_5_3_survivors={len(survivors)}")
for degrees in survivors:
    print(f"edges={sum(degrees)//2} degrees={degrees}")
