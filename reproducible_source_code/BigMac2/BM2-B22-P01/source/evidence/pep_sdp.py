#!/usr/bin/env python3
"""Full dimension-free N=2 smooth-convex interpolation PEP (floating point).

This script is used only to discover a sparse exact dual.  It includes every
ordered interpolation inequality on {*,0,1,2}; exact certification is separate.
"""

import cvxpy as cp
import numpy as np
from math import sqrt


beta = (sqrt(5.0) - 1.0) / (1.0 + sqrt(7.0 + 2.0 * sqrt(5.0)))
alpha = 1.0 + beta
c = 1.0 / (2.0 + alpha)
n = 4

points = {
    -1: np.zeros(n),
    0: np.array([1.0, 0.0, 0.0, 0.0]),
    1: np.array([1.0, -1.0, 0.0, 0.0]),
    2: np.array([1.0, -1.0, -alpha, 0.0]),
}
grads = {
    -1: np.zeros(n),
    0: np.array([0.0, 1.0, 0.0, 0.0]),
    1: np.array([0.0, 0.0, 1.0, 0.0]),
    2: np.array([0.0, 0.0, 0.0, 1.0]),
}


def sym_outer(u, v):
    return (np.outer(u, v) + np.outer(v, u)) / 2.0


def hmat(i, j):
    dx = points[i] - points[j]
    dg = grads[i] - grads[j]
    return -sym_outer(grads[j], dx) - 0.5 * sym_outer(dg, dg)


def fcoef(i, j):
    a = np.zeros(3)
    if i >= 0:
        a[i] += 1.0
    if j >= 0:
        a[j] -= 1.0
    return a


G = cp.Variable((n, n), symmetric=True)
f = cp.Variable(3)
tau = cp.Variable()
constraints = []
radius = 1.0 - G[0, 0] >= 0
constraints.append(radius)
perf = []
for k in range(3):
    q = G[k + 1, k + 1] - tau >= 0
    constraints.append(q)
    perf.append(q)
interp = {}
for i in (-1, 0, 1, 2):
    for j in (-1, 0, 1, 2):
        if i == j:
            continue
        q = fcoef(i, j) @ f + cp.sum(cp.multiply(hmat(i, j), G)) >= 0
        constraints.append(q)
        interp[i, j] = q
psd = G >> 0
constraints.append(psd)

problem = cp.Problem(cp.Maximize(tau), constraints)
for solver, opts in [
    ("CLARABEL", dict(tol_gap_abs=1e-10, tol_feas=1e-10, tol_gap_rel=1e-10,
                      max_iter=1000)),
    ("SCS", dict(eps=1e-9, max_iters=1000000, acceleration_lookback=20)),
]:
    value = problem.solve(solver=solver, verbose=False, **opts)
    print("solver", solver, "status", problem.status, "value", repr(value),
          "target", repr(c*c), "difference", value-c*c)
    print("G eigenvalues", np.linalg.eigvalsh(G.value))
    print("G", np.array2string(G.value, precision=11, suppress_small=True))
    print("f", f.value, "tau", tau.value)
    print("radius dual", radius.dual_value)
    print("performance duals", [q.dual_value for q in perf], "sum",
          sum(q.dual_value for q in perf))
    print("positive interpolation duals")
    for edge, q in interp.items():
        if q.dual_value > 1e-8:
            print(edge, "dual", q.dual_value, "slack", q.value())
    print("PSD dual eigenvalues", np.linalg.eigvalsh(psd.dual_value))
    print("PSD dual", np.array2string(psd.dual_value, precision=11,
                                      suppress_small=True))
    print()
