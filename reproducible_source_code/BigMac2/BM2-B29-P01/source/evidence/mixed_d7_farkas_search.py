#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Search a normalized Farkas certificate for the exact d=7 mixed LP."""

from __future__ import annotations

import json
import math
from pathlib import Path

import highspy
import numpy as np
from scipy import sparse

from mixed_lp_search import N, build


OUT = Path("evidence/mixed_d7_farkas_search")


def main():
    idx, _, rows, aeq, beq, aub, bub, unames = build(7)
    nv = aeq.shape[1]
    col_scale = np.empty(nv)
    for w in range(N + 1):
        col_scale[w] = math.comb(N, w)
        col_scale[N + 1 + w] = math.comb(N, w)
    facn = math.factorial(N)
    for si, s in enumerate(idx):
        multinom = facn
        for z in s:
            multinom //= math.factorial(z)
        col_scale[2 * (N + 1) + si] = math.sqrt(multinom)

    primal = sparse.vstack([aeq, aub], format="csr") @ sparse.diags(col_scale)
    rhs = np.r_[beq, bub]
    row_scale = np.empty(primal.shape[0])
    for i in range(primal.shape[0]):
        lo, hi = primal.indptr[i], primal.indptr[i+1]
        mx = max(float(np.max(np.abs(primal.data[lo:hi]))), abs(float(rhs[i])))
        row_scale[i] = 1.0 / mx
    primal = sparse.diags(row_scale) @ primal
    srhs = row_scale * rhs

    ne = len(rows)
    nu = len(unames)
    # Certificate variables are unrestricted equality multipliers followed by
    # nonnegative packing-row multipliers.  Rows enforce A^T y >= 0; the last
    # row fixes b^T y=-1.
    certmat = sparse.vstack(
        [primal.T, sparse.csr_matrix(srhs.reshape(1, -1))], format="csc"
    )
    lp = highspy.HighsLp()
    lp.num_col_ = ne + nu
    lp.num_row_ = nv + 1
    lp.col_cost_ = np.zeros(ne + nu)
    lp.col_lower_ = np.r_[np.full(ne, -highspy.kHighsInf), np.zeros(nu)]
    lp.col_upper_ = np.full(ne + nu, highspy.kHighsInf)
    lp.row_lower_ = np.r_[np.zeros(nv), -1.0]
    lp.row_upper_ = np.r_[np.full(nv, highspy.kHighsInf), -1.0]
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = certmat.indptr.astype(np.int32)
    lp.a_matrix_.index_ = certmat.indices.astype(np.int32)
    lp.a_matrix_.value_ = certmat.data
    h = highspy.Highs()
    h.setOptionValue("output_flag", True)
    h.setOptionValue("small_matrix_value", 1e-12)
    h.setOptionValue("solver", "ipm")
    h.setOptionValue("presolve", "on")
    h.setOptionValue("primal_feasibility_tolerance", 1e-9)
    h.passModel(lp)
    h.run()
    status = h.getModelStatus()
    result = {"status": str(status), "nvar": ne+nu, "nrow": nv+1,
              "nnz": int(certmat.nnz)}
    if status == highspy.HighsModelStatus.kOptimal:
        sol = h.getSolution()
        z = np.asarray(sol.col_value)
        original = z * row_scale
        slack = aeq.T @ original[:ne] + aub.T @ original[ne:]
        dot = beq @ original[:ne] + bub @ original[ne:]
        np.savez_compressed(OUT.with_suffix(".npz"), scaled=z,
                            original=original, row_scale=row_scale,
                            col_scale=col_scale)
        basis = h.getBasis()
        np.savez_compressed(
            OUT.with_name(OUT.name + "_basis.npz"),
            col_status=np.array([int(x) for x in basis.col_status_]),
            row_status=np.array([int(x) for x in basis.row_status_]),
        )
        result.update({
            "nonzero_1e-9": int(np.sum(np.abs(original)>1e-9)),
            "packing_min": float(np.min(original[ne:])),
            "coefficient_min": float(np.min(slack)),
            "coefficient_max": float(np.max(slack)),
            "rhs_dot": float(dot),
        })
    OUT.with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
