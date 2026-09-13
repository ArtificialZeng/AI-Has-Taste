#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Generate Definition 5.1 exactly and search the (20,8,d) mixed LP.

The integer coefficient matrix is retained in memory.  HiGHS receives a
floating copy only as a discovery oracle; any eventual witness is checked by a
separate exact verifier.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import highspy
import numpy as np
from scipy import sparse


N = 20
K = 8
QK = 1 << K
QDUAL = 1 << (N - K)
SCALE = 1 << N
H4 = np.array(
    [[1, 1, 1, 1], [1, 1, -1, -1],
     [1, -1, 1, -1], [1, -1, -1, 1]], dtype=np.int64
)


def comps(degree: int) -> list[tuple[int, int, int, int]]:
    return [
        (a, b, c, degree - a - b - c)
        for a in range(degree + 1)
        for b in range(degree - a + 1)
        for c in range(degree - a - b + 1)
    ]


def hadamard_coefficient_matrix(n: int = N) -> tuple[list[tuple[int, ...]], np.ndarray]:
    """Return T[t,s]=[x^t] prod_i (H4 x)_i**s_i, using integer recursion."""
    prev_idx = [(0, 0, 0, 0)]
    prev = np.ones((1, 1), dtype=np.int64)
    for degree in range(1, n + 1):
        cur_idx = comps(degree)
        cur_pos = {x: i for i, x in enumerate(cur_idx)}
        prev_pos = {x: i for i, x in enumerate(prev_idx)}
        targets = [
            np.fromiter(
                (cur_pos[tuple(u[q] + (q == j) for q in range(4))] for u in prev_idx),
                dtype=np.int32,
                count=len(prev_idx),
            )
            for j in range(4)
        ]
        cur = np.zeros((len(cur_idx), len(cur_idx)), dtype=np.int64)
        for col, s in enumerate(cur_idx):
            i = next(q for q, z in enumerate(s) if z)
            p = list(s)
            p[i] -= 1
            v = prev[:, prev_pos[tuple(p)]]
            for j in range(4):
                cur[targets[j], col] += H4[i, j] * v
        prev_idx, prev = cur_idx, cur
    return prev_idx, prev


def kraw(j: int, w: int) -> int:
    return sum(
        (-1) ** ell * math.comb(w, ell) * math.comb(N - w, j - ell)
        for ell in range(max(0, j - (N - w)), min(j, w) + 1)
    )


def build(d: int):
    idx, transform = hadamard_coefficient_matrix()
    mi = {x: i for i, x in enumerate(idx)}
    m0 = 2 * (N + 1)
    nv = m0 + len(idx)
    rows: list[tuple[str, dict[int, int], int]] = []

    def A(w): return w
    def B(w): return N + 1 + w
    def M(x): return m0 + mi[x]
    def eq(name, co, rhs):
        co = {int(j): int(v) for j, v in co.items() if v}
        rows.append((name, co, int(rhs)))

    eq("A0", {A(0): 1}, 1)
    eq("B0", {B(0): 1}, 1)
    for w in range(1, d):
        eq(f"A_zero[{w}]", {A(w): 1}, 0)
    for j in range(N + 1):
        co = {B(j): QK}
        for w in range(N + 1):
            co[A(w)] = co.get(A(w), 0) - kraw(j, w)
        eq(f"hamming_MacWilliams[{j}]", co, 0)

    for x in idx:
        a, b, c, e = x
        if e & 1:
            eq(f"M_even[{a},{b},{c},{e}]", {M(x): 1}, 0)
        if 1 <= c + e < d:
            eq(f"M_distance[{a},{b},{c},{e}]", {M(x): 1}, 0)
        if b == 0 and c == 0 and e > 0:
            eq(f"M_diagonal_axis[{a},0,0,{e}]", {M(x): 1}, 0)

    for w in range(N + 1):
        eq(f"B_axis[{w}]", {M((N-w, w, 0, 0)): 1, B(w): -1}, 0)
        eq(f"A_axis[{w}]", {M((N-w, 0, w, 0)): 1, A(w): -1}, 0)
        co = {A(w): -QDUAL}
        for x in idx:
            if x[2] + x[3] == w:
                co[M(x)] = 1
        eq(f"A_marginal[{w}]", co, 0)
        co = {B(w): -QK}
        for x in idx:
            if x[1] + x[3] == w:
                co[M(x)] = 1
        eq(f"B_marginal[{w}]", co, 0)
        co = {}
        for x in idx:
            if x[1] + x[2] == w:
                co[M(x)] = 1
        eq(f"binomial_marginal[{w}]", co, math.comb(N, w))

    # 2^20 M_t - [x^t]J(H4 x)=0 for every t.
    for ti, t in enumerate(idx):
        nz = np.flatnonzero(transform[ti])
        co = {M(idx[int(si)]): -int(transform[ti, si]) for si in nz}
        co[M(t)] = co.get(M(t), 0) + SCALE
        eq(f"joint_MacWilliams[{','.join(map(str,t))}]", co, 0)

    rr, cc, vv, rhs = [], [], [], np.empty(len(rows), dtype=float)
    for i, (_, co, b) in enumerate(rows):
        rhs[i] = b
        for j, v in co.items():
            rr.append(i); cc.append(j); vv.append(float(v))
    amat = sparse.coo_matrix((vv, (rr, cc)), shape=(len(rows), nv)).tocsc()

    # A_w+B_w <= binomial(n,w), w>=1.  All variables have lower bound zero.
    ur, uc, uv, ub, unames = [], [], [], [], []
    for w in range(1, N + 1):
        i = len(ub)
        ur += [i, i]; uc += [A(w), B(w)]; uv += [1.0, 1.0]
        ub.append(float(math.comb(N, w)))
        unames.append(f"packing[{w}]")
    aub = sparse.coo_matrix((uv, (ur, uc)), shape=(len(ub), nv)).tocsc()
    return idx, transform, rows, amat, rhs, aub, np.array(ub), unames


def solve(d: int, out: Path, solver: str, presolve: str):
    then = time.time()
    idx, transform, rows, aeq, beq, aub, bub, unames = build(d)
    # Numerically balanced discovery model.  If x is the original vector, use
    # x_j=col_scale[j]*y_j.  The sqrt(multinomial) scaling makes the normalized
    # degree-20 Hadamard action orthogonal; every joint-MacWilliams entry is at
    # most one after row scaling.  This does not enter exact verification.
    col_scale = np.empty(aeq.shape[1])
    for w in range(N + 1):
        col_scale[w] = math.comb(N, w)
        col_scale[N + 1 + w] = math.comb(N, w)
    for si, s in enumerate(idx):
        multinom = math.factorial(N)
        for z in s:
            multinom //= math.factorial(z)
        col_scale[2 * (N + 1) + si] = math.sqrt(multinom)
    allmat = sparse.vstack([aeq, aub], format="csr")
    allmat = allmat @ sparse.diags(col_scale)
    raw_lower = np.r_[beq, np.full(len(bub), -highspy.kHighsInf)]
    raw_upper = np.r_[beq, bub]
    row_scale = np.ones(allmat.shape[0])
    for i in range(allmat.shape[0]):
        lo, hi = allmat.indptr[i], allmat.indptr[i + 1]
        mx = float(np.max(np.abs(allmat.data[lo:hi]))) if hi > lo else 1.0
        if i < len(beq):
            mx = max(mx, abs(float(beq[i])))
        else:
            mx = max(mx, abs(float(bub[i-len(beq)])))
        row_scale[i] = 1.0 / mx
    mat = sparse.diags(row_scale) @ allmat
    mat = mat.tocsc()
    nr, nv = mat.shape
    inf = highspy.kHighsInf
    lower = raw_lower * row_scale
    upper = raw_upper * row_scale
    lp = highspy.HighsLp()
    lp.num_col_ = nv
    lp.num_row_ = nr
    lp.col_cost_ = np.zeros(nv)
    lp.col_lower_ = np.zeros(nv)
    lp.col_upper_ = np.full(nv, inf)
    lp.row_lower_ = lower
    lp.row_upper_ = upper
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = mat.indptr.astype(np.int32)
    lp.a_matrix_.index_ = mat.indices.astype(np.int32)
    lp.a_matrix_.value_ = mat.data
    h = highspy.Highs()
    h.setOptionValue("output_flag", True)
    h.setOptionValue("small_matrix_value", 1e-12)
    h.setOptionValue("presolve", presolve)
    h.setOptionValue("solver", solver)
    h.setOptionValue("simplex_strategy", 1)
    h.setOptionValue("primal_feasibility_tolerance", 1e-9)
    h.setOptionValue("dual_feasibility_tolerance", 1e-9)
    h.passModel(lp)
    h.run()
    status = str(h.getModelStatus())
    info = h.getInfo()
    result = {
        "d": d, "status": status, "seconds": time.time()-then,
        "nvar": nv, "neq": len(rows), "nub": len(bub), "nnz": int(mat.nnz),
        "simplex_iterations": int(info.simplex_iteration_count),
    }
    if h.getModelStatus() == highspy.HighsModelStatus.kOptimal:
        sol = h.getSolution()
        y = np.asarray(sol.col_value)
        x = col_scale * y
        np.savez_compressed(out.with_suffix(".solution.npz"), x=x)
        result.update({
            "min_x": float(x.min()), "max_x": float(x.max()),
            "max_eq_residual": float(np.max(np.abs(aeq @ x - beq))),
            "max_ub_excess": float(np.max(aub @ x - bub)),
            "positive_count_1e-8": int(np.sum(x > 1e-8)),
        })
    elif h.getModelStatus() == highspy.HighsModelStatus.kInfeasible:
        ray_status, has_ray, scaled_ray = h.getDualRay()
        # A scaled row multiplier z corresponds to z_i*row_scale_i on the
        # original rows.  Save both for rational reconstruction.
        scaled_ray = np.asarray(scaled_ray)
        ray = scaled_ray * row_scale
        ray = np.asarray(ray)
        np.savez_compressed(out.with_suffix(".dualray.npz"), ray=ray,
                            scaled_ray=scaled_ray, row_scale=row_scale,
                            col_scale=col_scale)
        result.update({
            "dual_ray_status": str(ray_status), "has_dual_ray": bool(has_ray),
            "ray_nonzero_1e-8": int(np.sum(np.abs(ray) > 1e-8)),
            "ray_max_abs": float(np.max(np.abs(ray))),
            "ray_dot_reported_rhs": float(ray @ np.r_[beq, bub]),
        })
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--d", type=int, required=True, choices=(6, 7))
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--solver", choices=("simplex", "ipm"), default="simplex")
    p.add_argument("--presolve", choices=("on", "off"), default="on")
    a = p.parse_args()
    solve(a.d, a.out, a.solver, a.presolve)
