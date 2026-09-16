#!/usr/bin/env python3
"""Exact certificate search for the r=3, 13-layer junction repair.

Floating-point LP is used only to discover certificates.  Every certificate
used in the conclusion is reconstructed as a Fraction and checked exactly.
"""

from fractions import Fraction
from itertools import combinations

import numpy as np
from scipy.optimize import linprog


COUNTS = [1, 4, 2, 1, 3, 3, 1, 2, 4, 1, 3, 4, 3]
TARGET = Fraction(39, 8)
CLAIMED_MINIMUM = Fraction(122, 25)


def fraction_vector(vector):
    return [Fraction(float(value)).limit_denominator(1_000_000) for value in vector]


starts = np.cumsum([0] + COUNTS)
layers = [list(range(starts[i], starts[i + 1])) for i in range(13)]
n_vertices = int(starts[-1])

# The maximal periodic layered graph: cliques in every layer and complete
# joins between consecutive layers (including layer 12 to layer 0 of the next
# period).  All other pairs are nonedges.
maximal_edges = set()
for layer in layers:
    maximal_edges.update(tuple(sorted(edge)) for edge in combinations(layer, 2))
for i in range(13):
    maximal_edges.update(
        tuple(sorted((u, v))) for u in layers[i] for v in layers[(i + 1) % 13]
    )

# Only these consecutive unions have seven vertices.  A K_7-free subgraph
# must omit an edge from each one.
junction_1 = layers[10] + layers[11]
junction_2 = layers[11] + layers[12]
deletions_1 = list(combinations(junction_1, 2))
deletions_2 = list(combinations(junction_2, 2))

best_primal_value = None
best_primal = None
best_deletions = None
dual_values = {}
checked = 0

for deletion_1 in deletions_1:
    for deletion_2 in deletions_2:
        edges = maximal_edges - {
            tuple(sorted(deletion_1)),
            tuple(sorted(deletion_2)),
        }
        adjacency = np.zeros((n_vertices, n_vertices), dtype=int)
        for u, v in edges:
            adjacency[u, v] = adjacency[v, u] = 1

        # Primal: min sum_v w_v, subject to A w >= 1 and w >= 0.
        result = linprog(
            np.ones(n_vertices),
            A_ub=-adjacency,
            b_ub=-np.ones(n_vertices),
            bounds=(0, None),
            method="highs",
        )
        assert result.success

        # Dual: max sum_v y_v, subject to A^T y <= 1 and y >= 0.
        # Reconstruct and verify this certificate using exact rational
        # arithmetic.  No floating-point objective enters an assertion.
        dual = fraction_vector(-result.ineqlin.marginals)
        assert all(value >= 0 for value in dual)
        assert all(
            sum(Fraction(adjacency[u, v]) * dual[u] for u in range(n_vertices))
            <= 1
            for v in range(n_vertices)
        )
        dual_value = sum(dual)
        assert dual_value >= CLAIMED_MINIMUM
        dual_values[dual_value] = dual_values.get(dual_value, 0) + 1

        primal = fraction_vector(result.x)
        if (
            all(value >= 0 for value in primal)
            and all(
                sum(Fraction(adjacency[u, v]) * primal[v] for v in range(n_vertices))
                >= 1
                for u in range(n_vertices)
            )
        ):
            primal_value = sum(primal)
            if best_primal_value is None or primal_value < best_primal_value:
                best_primal_value = primal_value
                best_primal = primal
                best_deletions = (deletion_1, deletion_2)
        checked += 1

assert checked == 21 * 21 == 441
assert best_primal_value == CLAIMED_MINIMUM
assert CLAIMED_MINIMUM - TARGET == Fraction(1, 200)

print(f"vertices: {n_vertices}")
print(f"maximal edges: {len(maximal_edges)}")
print(f"deletion pairs checked: {checked}")
print("all reconstructed dual certificates feasible: yes")
print(f"certified minimum: {CLAIMED_MINIMUM}")
print(f"target: {TARGET}")
print(f"minimum minus target: {CLAIMED_MINIMUM - TARGET}")
print(f"best deletion pair: {best_deletions}")
print("exact best primal weights:")
print(" ".join(map(str, best_primal)))
print("verified dual objective distribution:")
for value, multiplicity in sorted(dual_values.items()):
    print(f"  {value}: {multiplicity}")
