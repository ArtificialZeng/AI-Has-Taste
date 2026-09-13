#!/usr/bin/env python3
"""Exact finite check of the type-II product-certificate dual separator."""

from collections import Counter
from itertools import combinations


N = 6
EDGES = tuple(combinations(range(N), 2))


def q_vector(h):
    return {(i, j): h[i] * h[j] for i, j in EDGES}


def dual_value(q):
    return (
        3 * q[0, 1]
        + sum(q[0, k] for k in range(2, 6))
        + 2 * sum(q[1, k] for k in range(2, 6))
        + 2 * sum(q[i, j] for i, j in combinations(range(2, 6), 2))
    )


triangular = []
for support in combinations(range(N), 3):
    for negative in support:
        h = [0] * N
        h[negative] = -1
        for i in support:
            if i != negative:
                h[i] = 1
        triangular.append(q_vector(h))

pentagonal = []
for zero in range(N):
    nonzero = [i for i in range(N) if i != zero]
    for negatives in combinations(nonzero, 2):
        h = [1] * N
        h[zero] = 0
        for i in negatives:
            h[i] = -1
        pentagonal.append(q_vector(h))

target = q_vector([-2, -1, 1, 1, 1, 1])
tri_values = Counter(map(dual_value, triangular))
pent_values = Counter(map(dual_value, pentagonal))

assert len(triangular) == 60
assert len(pentagonal) == 60
assert tri_values == Counter({-2: 46, 0: 10, -4: 4})
assert pent_values == Counter({-4: 28, -2: 16, -6: 12, 0: 4})
assert max(tri_values) == max(pent_values) == 0
assert dual_value(target) == 2

print("triangular dual values:", sorted(tri_values.items()))
print("pentagonal dual values:", sorted(pent_values.items()))
print("type-II target dual value:", dual_value(target))
print("certificate verified exactly over integers")
