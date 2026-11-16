"""LP relaxation of 'cycle cover in which every ray from the pivot is crossed exactly c times' (no subtour cuts).
Rays: one per angular gap between consecutive cell angles (exact, via rational cross products), so the set of ray
constraints is complete. Reports LP feasibility; if infeasible, extracts a Farkas certificate y and verifies it in
exact arithmetic:  max_{0<=x<=1} y.Ax = sum_j max(0,(A^T y)_j) < y.b  proves no 0/1 (or fractional) solution.
  python lp_certificates.py n c [inner]      ("inner" adds the cut: some arc leaves the 8 cells around the centre)
"""
import sys
from fractions import Fraction as F
from functools import cmp_to_key

import numpy as np
from scipy.optimize import linprog
from scipy import sparse

n, c = int(sys.argv[1]), int(sys.argv[2])
CUT_INNER = len(sys.argv) > 3 and sys.argv[3] == "inner"   # add: some arc must leave the 8 cells around the centre
p = q = F(n - 1, 2)
cells = [(i, j) for i in range(n) for j in range(n) if not (n % 2 and F(i) == p and F(j) == q)]
idx = {v: k for k, v in enumerate(cells)}
arcs = [((i, j), (i + di, j + dj)) for (i, j) in cells
        for di, dj in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
        if (i + di, j + dj) in idx and (i - p) * (j + dj - q) > (i + di - p) * (j - q)]
# exact angular order of cells around the pivot, in the arcs' direction of motion
vec = {v: (F(v[0]) - p, F(v[1]) - q) for v in cells}
def half(u):  # split the plane into two half-planes for a total order of directions
    x, y = u
    return 0 if (y > 0 or (y == 0 and x > 0)) else 1
def cmp(u, v):
    hu, hv = half(u), half(v)
    if hu != hv: return hu - hv
    cr = u[0] * v[1] - u[1] * v[0]
    return -1 if cr > 0 else (1 if cr < 0 else 0)
dirs = sorted({vec[v] for v in cells}, key=cmp_to_key(cmp))
# distinct directions (up to positive scaling)
uniq = []
for d in dirs:
    if not uniq or cmp(uniq[-1], d) != 0: uniq.append(d)
# arcs move with positive cross product (i-p)(j'-q) - (i'-p)(j-q) > 0, i.e. vec(u) x vec(v) > 0 in (x=i,y=j) coords,
# which is increasing angle in the order above. A ray strictly between directions uniq[k] and uniq[k+1] is crossed by
# arc u->v iff the counterclockwise sweep from dir(u) to dir(v) (less than pi) contains it.
def pos(u):
    for k, d in enumerate(uniq):
        if cmp(d, u) == 0: return k
K = len(uniq)
rows, rhs = [], []
A = []   # list of (row, col, val)
r = 0
for v in cells:   # out-degree 1, in-degree 1
    for a_i, a in enumerate(arcs):
        if a[0] == v: A.append((r, a_i, 1))
    rhs.append(1); r += 1
    for a_i, a in enumerate(arcs):
        if a[1] == v: A.append((r, a_i, 1))
    rhs.append(1); r += 1
for k in range(K):   # ray in the gap after direction uniq[k]
    for a_i, a in enumerate(arcs):
        s, t = pos(vec[a[0]]), pos(vec[a[1]])
        # sweep from s to t in increasing order, cyclically; crosses gap k if k in [s, t) cyclically
        if (k - s) % K < (t - s) % K: A.append((r, a_i, 1))
    rhs.append(c); r += 1
ineq = []   # rows of the form sum x >= 1 (subtour cuts)
if CUT_INNER:
    ctr = (n - 1) // 2
    S = {(ctr + di, ctr + dj) for di in (-1, 0, 1) for dj in (-1, 0, 1)} - {(ctr, ctr)}
    ineq.append([a_i for a_i, a in enumerate(arcs) if a[0] in S and a[1] not in S])
m_rows, n_cols = r, len(arcs)
for cut in ineq:   # sum_{cut} x - t = 1 with t >= 0, encoded via an extra column per cut
    for a_i in cut: A.append((m_rows, a_i, 1))
    rhs.append(1); m_rows += 1
n_surplus = len(ineq)
for k in range(n_surplus):
    A.append((m_rows - n_surplus + k, n_cols + k, -1))
n_cols_tot = n_cols + n_surplus
M = sparse.csr_matrix(([x[2] for x in A], ([x[0] for x in A], [x[1] for x in A])), shape=(m_rows, n_cols_tot))
b = np.array(rhs, dtype=float)
# phase-1 LP: min sum(s+ + s-) s.t. M x + s+ - s- = b, 0<=x<=1, s>=0
I = sparse.identity(m_rows)
res = linprog(np.concatenate([np.zeros(n_cols_tot), np.ones(2 * m_rows)]),
              A_eq=sparse.hstack([M, I, -I]).tocsr(), b_eq=b,
              bounds=[(0, 1)] * n_cols + [(0, None)] * n_surplus + [(0, None)] * (2 * m_rows), method="highs")
print(f"[cut inner ring: {CUT_INNER}] n={n} c={c}: {len(cells)} cells, {n_cols} arcs, {K} rays; phase-1 optimum {res.fun:.6g}")
if res.fun < 1e-7:
    print("LP relaxation FEASIBLE (fractional cycle covers exist); an exact argument needs integrality."); sys.exit(0)
y = res.eqlin.marginals   # duals of the equality rows
# rationalise and verify exactly
best = None
for D in (1, 2, 3, 4, 6, 8, 12, 24, 48, 120, 720, 5040):
    yr = [F(round(v * D), D) for v in y]
    Aty = [F(0)] * n_cols_tot
    for (i, j, val) in A:
        Aty[j] += yr[i] * val
    if any(t > 0 for t in Aty[n_cols:]):   # surplus vars are unbounded above: need nonpositive coefficients
        lhs = F(10 ** 9)
    else:
        lhs = sum(max(F(0), t) for t in Aty[:n_cols])
    yb = sum(yr[i] * rhs[i] for i in range(m_rows))
    if lhs < yb or (-lhs > -yb and False):
        best = (D, yr, lhs, yb); break
    # also try the sign-flipped certificate
    Aty2 = [-t for t in Aty]
    lhs2 = F(10 ** 9) if any(t > 0 for t in Aty2[n_cols:]) else sum(max(F(0), t) for t in Aty2[:n_cols])
    if lhs2 < -yb:
        best = (D, [-v for v in yr], lhs2, -yb); break
if best:
    D, yr, lhs, yb = best
    nz = sum(1 for v in yr if v != 0)
    import json
    rowinfo = []
    rr = 0
    for v in cells:
        rowinfo.append(("out", v)); rowinfo.append(("in", v))
    for k in range(K):
        rowinfo.append(("ray", k, str(uniq[k][0]) + "," + str(uniq[k][1])))
    for cut in ineq: rowinfo.append(("cut",))
    dump = [(rowinfo[i], str(v)) for i, v in enumerate(yr) if v != 0]
    json.dump(dump, open(f"cert_n{n}_c{c}{'_inner' if CUT_INNER else ''}.json", "w"))
    print(f"EXACT Farkas certificate (denominator {D}, {nz} nonzero multipliers): "
          f"max over the box of y.Ax = {lhs} < y.b = {yb}  => no cycle cover with {c} crossings on every ray")
else:
    print("LP infeasible numerically, but no small-denominator certificate found")
