#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Turn the numerical d=7 dual separator into an exact dyadic certificate.

Every binary64 multiplier is interpreted as its exact dyadic rational.  A tiny
exact multiple of the sum of the 21 binomial-marginal equations supplies slack;
zero-right-hand-side axis equations supply slack for A and B.  The final JSON
contains no floating-point data.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mixed_lp_search import N, build  # discovery generator, not the verifier


SEARCH = Path("evidence/mixed_d7_farkas_search.npz")
OUT = Path("evidence/mixed_d7_farkas.json")


def main():
    z = np.load(SEARCH)["original"]
    idx, transform, rows, _, _, _, _, _ = build(7)
    ne = len(rows)
    fr = [Fraction.from_float(float(v)) for v in z[:ne]]
    power = max(q.denominator.bit_length() - 1 for q in fr if q)
    den = 1 << power
    y = [q.numerator * (den // q.denominator) for q in fr]

    # Add lambda=sum_j lambda*(binomial_marginal[j]), lambda=2^-30.
    lam = den >> 30
    for i, (name, _, _) in enumerate(rows):
        if name.startswith("binomial_marginal["):
            y[i] += lam

    # Accumulate the exact equality-row combination in original coordinates.
    coeff = [0] * (2 * (N + 1) + len(idx))
    rhs = 0
    for yi, (_, co, b) in zip(y, rows):
        if yi:
            rhs += yi * b
            for j, a in co.items():
                coeff[j] += yi * a

    # Make all A/B coefficients strictly positive using only zero-RHS axes.
    delta = lam >> 4
    name_to_i = {name: i for i, (name, _, _) in enumerate(rows)}
    mpos = {s: 2 * (N + 1) + q for q, s in enumerate(idx)}
    for w in range(N + 1):
        for kind, off, axis in (("A", 0, "A_axis"), ("B", N + 1, "B_axis")):
            j = off + w
            alpha = max(0, delta - coeff[j])
            if alpha:
                ri = name_to_i[f"{axis}[{w}]"]
                y[ri] -= alpha
                coeff[j] += alpha
                mj = mpos[(N-w, 0, w, 0)] if kind == "A" else mpos[(N-w, w, 0, 0)]
                coeff[mj] -= alpha

    if min(coeff) < 0 or rhs >= 0:
        raise RuntimeError(f"adjustment failed: min coeff={min(coeff)}, rhs={rhs}")

    def rat(num: int) -> list[int]:
        g = math.gcd(abs(num), den)
        return [num // g, den // g]

    payload = {
        "format": "mixed-d7-farkas-v1",
        "parameters": {"n": 20, "k": 8, "d": 7},
        "convention": (
            "Equalities are E_i x=b_i; nonnegativity rows are -x_j<=0. "
            "The listed equality multipliers y and lower multipliers s=E^T y "
            "give sum_i y_i(E_i x-b_i)+sum_j s_j(-x_j)<=0 with zero "
            "left-hand coefficient and right-hand constant -sum_i y_i b_i>0; "
            "equivalently 0<=sum_i y_i b_i<0."
        ),
        "common_dyadic_denominator": den,
        "equality_multipliers": [
            {"row": i, "name": rows[i][0], "value": rat(v)}
            for i, v in enumerate(y) if v
        ],
        "lower_bound_multipliers": [
            {"variable": j, "value": rat(v)} for j, v in enumerate(coeff) if v
        ],
        "packing_multipliers": [],
        "rhs_dot": rat(rhs),
        "minimum_lower_numerator_over_common_denominator": min(coeff),
        "counts": {
            "equalities_total": len(rows),
            "variables_total": len(coeff),
            "nonzero_equalities": sum(v != 0 for v in y),
            "positive_lower_multipliers": sum(v > 0 for v in coeff),
        },
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({k: payload[k] for k in ("format", "parameters", "rhs_dot", "counts")}, indent=2))


if __name__ == "__main__":
    main()
