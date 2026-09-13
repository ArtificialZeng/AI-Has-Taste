#!/usr/bin/env python3
"""Search the full complementary-slackness face of the N=2 PEP dual.

This is floating-point discovery code.  It fixes the exact lower-bound Gram
ray and permits precisely the interpolation inequalities active on that ray.
Any proposed certificate found here still needs a separate exact verifier.
"""

from itertools import permutations
from math import sqrt

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import LinearConstraint, minimize


BETA = (sqrt(5.0) - 1.0) / (1.0 + sqrt(7.0 + 2.0 * sqrt(5.0)))
ALPHA = 1.0 + BETA
C = 1.0 / (2.0 + ALPHA)
RHO = C * C
N = 4
IDS = (-1, 0, 1, 2)

POINTS = {
    -1: np.zeros(N),
    0: np.array([1.0, 0.0, 0.0, 0.0]),
    1: np.array([1.0, -1.0, 0.0, 0.0]),
    2: np.array([1.0, -1.0, -ALPHA, 0.0]),
}
GRADS = {
    -1: np.zeros(N),
    0: np.array([0.0, 1.0, 0.0, 0.0]),
    1: np.array([0.0, 0.0, 1.0, 0.0]),
    2: np.array([0.0, 0.0, 0.0, 1.0]),
}


def sym_outer(u, v):
    return (np.outer(u, v) + np.outer(v, u)) / 2.0


def hmat(i, j):
    dx = POINTS[i] - POINTS[j]
    dg = GRADS[i] - GRADS[j]
    return -sym_outer(GRADS[j], dx) - 0.5 * sym_outer(dg, dg)


# h(i,j) is active at the collinear projection-envelope witness exactly on
# every ordered nonstar pair, every (-1,j), and (2,-1).
EDGES = tuple(permutations((0, 1, 2), 2)) + (
    (-1, 0), (-1, 1), (-1, 2), (2, -1)
)
NV = len(EDGES) + 3


def slack(z):
    lam = z[:len(EDGES)]
    mu = z[len(EDGES):]
    s = np.zeros((N, N))
    s[0, 0] = RHO
    for k in range(3):
        s[k + 1, k + 1] -= mu[k]
    for q, edge in zip(lam, EDGES):
        s -= q * hmat(*edge)
    return s


def equalities():
    """Flow conservation, sum(mu)=1, and S(1,c,c,c)=0."""
    a = []
    b = []
    for node in (0, 1, 2):
        row = np.zeros(NV)
        for k, (i, j) in enumerate(EDGES):
            row[k] = (1.0 if i == node else 0.0) - (1.0 if j == node else 0.0)
        a.append(row)
        b.append(0.0)
    row = np.zeros(NV)
    row[len(EDGES):] = 1.0
    a.append(row)
    b.append(1.0)
    w = np.array([1.0, C, C, C])
    s0 = slack(np.zeros(NV))
    for i in range(N):
        row = np.zeros(NV)
        for k in range(NV):
            e = np.zeros(NV)
            e[k] = 1.0
            row[k] = ((slack(e) - s0) @ w)[i]
        a.append(row)
        b.append(-(s0 @ w)[i])
    return np.asarray(a), np.asarray(b)


def orthogonal_basis():
    w = np.array([[1.0, C, C, C]])
    return null_space(w)


def main():
    a, b = equalities()
    q = orthogonal_basis()

    # First obtain a nonnegative point on the affine face by least squares,
    # then use random starts around it.  SLSQP maximizes the minimum eigenvalue
    # on w-perp; a strictly positive value certifies numerical dual feasibility.
    x0 = np.linalg.lstsq(a, b, rcond=None)[0]
    linear = LinearConstraint(a, b, b)
    bounds = [(0.0, None)] * NV

    def objective(z):
        return -np.linalg.eigvalsh(q.T @ slack(z) @ q)[0]

    rng = np.random.default_rng(20260909)
    best = None
    starts = [np.maximum(x0, 1e-3)]
    starts.extend(rng.uniform(0.01, 1.0, NV) for _ in range(80))
    for start in starts:
        # Project a random start onto A z=b.  Bounds are restored softly; SLSQP
        # handles the remaining discrepancy.
        start = start + a.T @ np.linalg.lstsq(a @ a.T, b - a @ start, rcond=None)[0]
        start = np.maximum(start, 1e-8)
        ans = minimize(objective, start, method="SLSQP", bounds=bounds,
                       constraints=[linear],
                       options={"ftol": 1e-13, "maxiter": 3000, "disp": False})
        eig = np.linalg.eigvalsh(q.T @ slack(ans.x) @ q)
        score = eig[0]
        if best is None or score > best[0]:
            best = (score, ans, eig)

    score, ans, eig = best
    print("status", ans.success, ans.message)
    print("beta alpha c rho", BETA, ALPHA, C, RHO)
    print("edges")
    for edge, value in zip(EDGES, ans.x[:len(EDGES)]):
        print(edge, "%.16g" % value)
    print("mu", ["%.16g" % x for x in ans.x[len(EDGES):]],
          "sum", sum(ans.x[len(EDGES):]))
    print("equality residual", np.max(np.abs(a @ ans.x - b)))
    print("w-perp eigenvalues", eig)
    print("full eigenvalues", np.linalg.eigvalsh(slack(ans.x)))
    print("slack")
    print(np.array2string(slack(ans.x), precision=14, suppress_small=True))


if __name__ == "__main__":
    main()
