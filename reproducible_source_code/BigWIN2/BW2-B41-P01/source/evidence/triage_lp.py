"""Numerical triage only: maximize a common strictness margin in the RP polytope.

Hard-coded small cases keep the exponential subset system bounded. A positive
floating-point optimum is evidence, not an exact RP certificate.
"""

import itertools

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def graph(m, ell):
    a = 0
    b = list(range(1, m + 1))
    x = list(range(m + 1, 2 * m + 1))
    u = list(range(2 * m + 1, 2 * m + ell + 1))
    n = 2 * m + ell + 1
    edges = set(itertools.combinations(b, 2))
    for i in range(m):
        edges.add(tuple(sorted((a, x[i]))))
        edges.add(tuple(sorted((x[i], b[i]))))
    edges.update(itertools.combinations(u, 2))
    for ui in u:
        for v in range(2 * m + 1):
            edges.add(tuple(sorted((ui, v))))
    return n, sorted(edges)


def common_margin(m, ell):
    n, edges = graph(m, ell)
    q = len(edges)
    rows, rhs = [], []
    # Variables are edge marginals x_e and common margin epsilon.
    for edge_index in range(q):
        rows.append({edge_index: -1, q: 1})       # x_e >= epsilon
        rhs.append(0)
    for v in range(n):
        row = {q: 1}                              # x(delta(v)) <= 2-epsilon
        for edge_index, edge in enumerate(edges):
            if v in edge:
                row[edge_index] = 1
        rows.append(row)
        rhs.append(2)
    for mask in range(1, 1 << n):
        size = mask.bit_count()
        if size < 2 or size == n:
            continue
        row = {q: 1}                              # x(E[S]) <= |S|-1-epsilon
        for edge_index, (v, w) in enumerate(edges):
            if (mask >> v) & 1 and (mask >> w) & 1:
                row[edge_index] = 1
        rows.append(row)
        rhs.append(size - 1)
    matrix = lil_matrix((len(rows), q + 1))
    for i, row in enumerate(rows):
        for j, value in row.items():
            matrix[i, j] = value
    objective = np.zeros(q + 1)
    objective[q] = -1
    equality = np.zeros((1, q + 1))
    equality[0, :q] = 1
    solution = linprog(
        objective,
        A_ub=matrix.tocsr(),
        b_ub=np.asarray(rhs),
        A_eq=equality,
        b_eq=[n - 1],
        bounds=[(None, None)] * q + [(0, None)],
        method="highs",
    )
    return n, q, solution.success, solution.x[q] if solution.success else None


for parameters in ((5, 1), (6, 1)):
    print(parameters, common_margin(*parameters))

