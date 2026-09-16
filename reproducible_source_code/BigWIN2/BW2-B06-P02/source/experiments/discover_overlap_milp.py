#!/usr/bin/env python3
"""Diagnostic discovery of a maximum-overlap Hamilton path.

This floating/MILP computation is not part of the proof.  The retained exact
certificate and standard-library checkers independently validate the result.
"""

from __future__ import annotations

import itertools
import platform

import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix, vstack


def overlap(left: str, right: str) -> int:
    for size in range(7, 0, -1):
        if left[-size:] == right[:size]:
            return size
    return 0


def main() -> None:
    targets = [
        word
        for bits in itertools.product("01", repeat=8)
        if (word := "".join(bits))
        and all(word < word[pos:] + word[:pos] for pos in range(1, 8))
    ]
    count = len(targets)
    dummy = count
    dimension = count + 1
    arcs = [(i, j) for i in range(dimension) for j in range(dimension) if i != j]
    arc_index = {arc: index for index, arc in enumerate(arcs)}
    variable_count = len(arcs) + count
    objective = np.zeros(variable_count)
    for (i, j), index in arc_index.items():
        if i < count and j < count:
            objective[index] = -overlap(targets[i], targets[j])

    degree = lil_matrix((2 * dimension, variable_count))
    for (i, j), index in arc_index.items():
        degree[i, index] = 1
        degree[dimension + j, index] = 1

    mtz = lil_matrix((count * (count - 1), variable_count))
    row = 0
    for i in range(count):
        for j in range(count):
            if i == j:
                continue
            mtz[row, len(arcs) + i] = 1
            mtz[row, len(arcs) + j] = -1
            mtz[row, arc_index[i, j]] = count
            row += 1
    matrix = vstack([degree.tocsr(), mtz.tocsr()])
    lower_rows = np.r_[np.ones(2 * dimension), np.full(row, -np.inf)]
    upper_rows = np.r_[np.ones(2 * dimension), np.full(row, count - 1)]
    lower_vars = np.r_[np.zeros(len(arcs)), np.ones(count)]
    upper_vars = np.r_[np.ones(len(arcs)), np.full(count, count)]

    result = milp(
        objective,
        integrality=np.ones(variable_count, dtype=int),
        bounds=Bounds(lower_vars, upper_vars),
        constraints=LinearConstraint(matrix, lower_rows, upper_rows),
        options={"mip_rel_gap": 0.0, "time_limit": 120.0},
    )
    print(f"python={platform.python_version()} scipy={scipy.__version__} numpy={np.__version__}")
    print(f"status={result.status} message={result.message}")
    print(f"diagnostic_objective={result.fun} reported_gap={getattr(result, 'mip_gap', None)}")
    if result.x is None:
        return
    successor = {
        i: j for (i, j), index in arc_index.items() if result.x[index] > 0.5
    }
    order = []
    current = dummy
    for _ in range(count):
        current = successor[current]
        order.append(current)
    word = targets[order[0]]
    for left, right in zip(order, order[1:]):
        word += targets[right][overlap(targets[left], targets[right]) :]
    print(f"order={order}")
    print(f"candidate_length={len(word)} candidate={word}")


if __name__ == "__main__":
    main()
