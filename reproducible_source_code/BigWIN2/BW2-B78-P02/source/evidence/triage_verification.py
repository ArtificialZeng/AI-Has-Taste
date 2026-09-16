#!/usr/bin/env python3
"""Reproduce the finite-count and boundary checks used in triage."""

from itertools import combinations
from math import comb


TAU = (0, 2, 1, 5, 4, 3)
EDGES = tuple((i, j) for i in range(6) for j in range(6) if i != j)


def moved(edge):
    return TAU[edge[0]], TAU[edge[1]]


fixed = 0
representatives = set()
for size in (3, 4):
    for network in combinations(EDGES, size):
        image = tuple(sorted(moved(edge) for edge in network))
        fixed += network == image
        representatives.add(min(network, image))

labelled = sum(comb(30, size) for size in (3, 4))
print(f"labelled={labelled}")
print(f"fixed={fixed}")
print(f"orbits={len(representatives)}")

# Columns correspond to 0->X, X->Y, Y->0.
S = ((1, -1, 0), (0, 1, -1))
flux = (1, 1, 1)
residual = tuple(sum(row[j] * flux[j] for j in range(3)) for row in S)
minor = S[0][0] * S[1][1] - S[0][1] * S[1][0]
print(f"boundary_Sv={residual}")
print(f"boundary_rank_minor={minor}")

assert (labelled, fixed, len(representatives)) == (31465, 133, 15799)
assert residual == (0, 0) and minor != 0
