#!/usr/bin/env python3
"""Exact finite proof for complete K7-free 13-layer periods.

LP solves discover dual certificates; all claimed inequalities are then
checked with Fraction arithmetic.  The exhaustive enumeration itself uses
only integer comparisons.
"""

from fractions import Fraction

import numpy as np
from scipy.optimize import linprog


PERIOD = 13
TARGET = Fraction(39, 8)
sequence = []
admissible_count = 0
maximal_count = 0
maximal_representatives = set()


def canonical(values):
    """Canonical representative under cyclic shifts and reflection."""
    images = []
    for orientation in (values, values[::-1]):
        for shift in range(PERIOD):
            images.append(tuple(orientation[shift:] + orientation[:shift]))
    return min(images)


def is_maximal(values):
    """Maximal coordinatewise subject to adjacent sums at most six."""
    return all(
        values[i] == 5
        or values[i] + values[(i - 1) % PERIOD] == 6
        or values[i] + values[(i + 1) % PERIOD] == 6
        for i in range(PERIOD)
    )


def enumerate_sequences():
    global admissible_count, maximal_count
    if len(sequence) == PERIOD:
        if sequence[-1] + sequence[0] > 6:
            return
        admissible_count += 1
        if is_maximal(sequence):
            maximal_count += 1
            maximal_representatives.add(canonical(sequence[:]))
        return
    for value in range(1, 6):
        if sequence and sequence[-1] + value > 6:
            continue
        sequence.append(value)
        enumerate_sequences()
        sequence.pop()


enumerate_sequences()
assert admissible_count == 12_426_742
assert maximal_count == 3_836
assert len(maximal_representatives) == 178

minimum_certified_bound = None
equality_patterns = []
checked = 0

for counts in sorted(maximal_representatives):
    # If A_i is the total weight in layer i, equal splitting within each
    # clique shows that the exact layer-total constraints are B A >= 1, where
    # B[i,i]=1-1/counts[i] and B[i,i+-1]=1.
    matrix = [[Fraction(0) for _ in range(PERIOD)] for _ in range(PERIOD)]
    for i, count in enumerate(counts):
        matrix[i][(i - 1) % PERIOD] = 1
        matrix[i][i] = Fraction(count - 1, count)
        matrix[i][(i + 1) % PERIOD] = 1
    matrix_float = np.array([[float(value) for value in row] for row in matrix])
    result = linprog(
        np.ones(PERIOD),
        A_ub=-matrix_float,
        b_ub=-np.ones(PERIOD),
        bounds=(0, None),
        method="highs",
    )
    assert result.success

    dual = [
        Fraction(float(-value)).limit_denominator(1_000_000)
        for value in result.ineqlin.marginals
    ]
    assert all(value >= 0 for value in dual)
    assert all(
        sum(matrix[i][j] * dual[i] for i in range(PERIOD)) <= 1
        for j in range(PERIOD)
    )
    dual_value = sum(dual)
    assert dual_value >= TARGET
    if minimum_certified_bound is None or dual_value < minimum_certified_bound:
        minimum_certified_bound = dual_value
    if dual_value == TARGET:
        equality_patterns.append(counts)
    checked += 1

assert checked == 178
assert minimum_certified_bound == TARGET
assert equality_patterns == [(3,) * PERIOD]

# Exact feasible equality witness: three vertices of weight 1/8 in every
# layer.  Every vertex sees eight such neighboring base vertices.
equality_layer_total = Fraction(3, 8)
assert PERIOD * equality_layer_total == TARGET
assert 2 * equality_layer_total + Fraction(2, 3) * equality_layer_total == 1

print(f"admissible labeled cardinality patterns: {admissible_count}")
print(f"coordinatewise maximal labeled patterns: {maximal_count}")
print(f"maximal dihedral representatives checked: {checked}")
print("all reconstructed dual certificates feasible: yes")
print(f"certified global minimum: {minimum_certified_bound}")
print(f"equality representatives: {equality_patterns}")
print("exact equality weights: 3 vertices of weight 1/8 in each layer")
