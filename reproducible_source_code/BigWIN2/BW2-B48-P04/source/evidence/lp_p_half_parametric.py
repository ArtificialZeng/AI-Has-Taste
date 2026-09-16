#!/usr/bin/env python3
"""Discover and serialize the exact p=1/2 RHS-parametric LP certificate.

SciPy/HiGHS is used only to discover five endpoint primal vertices and four
interior dual vertices.  Every number written to the certificate is converted
to Fraction and accepted only after exact feasibility and equality checks.
The solver-free verifier is the decisive checker.
"""

from fractions import Fraction
from pathlib import Path
import json

import numpy as np
from scipy.optimize import linprog

from lp_p_half_t_quarter import (
    EDGES, build_orbits, canonical_row, connected_set, marginal_row,
    row_difference, sparse_matrix,
)


BREAKPOINTS = tuple(map(Fraction, ("3/4", "207/256", "243/256", "63/64", "1")))
DUAL_SAMPLES = tuple(map(Fraction, ("19/25", "17/20", "24/25", "99/100")))
EXPECTED_LINES = (
    (Fraction(182, 207), Fraction(0)),
    (Fraction(19, 18), -Fraction(73, 512)),
    (Fraction(4, 3), -Fraction(13, 32)),
    (Fraction(2), -Fraction(17, 16)),
)


def build_lp():
    pair_orbit, representatives, config_reps = build_orbits()
    n = len(representatives)

    eq_rows = []
    for w in config_reps:
        row = {}
        for s in range(16):
            j = pair_orbit[(w, s)]
            row[j] = row.get(j, 0) + 1
        eq_rows.append(row)

    monotone_rows = {}
    for w in range(1024):
        for e in range(10):
            if (w >> e) & 1:
                continue
            wp = w | (1 << e)
            for b in range(1, 5):
                row = row_difference(
                    marginal_row(pair_orbit, w, b),
                    marginal_row(pair_orbit, wp, b),
                )
                if row:
                    monotone_rows[canonical_row(row)] = row

    event_marginal = {}
    for w in range(1024):
        for j, value in marginal_row(pair_orbit, w, 1).items():
            event_marginal[j] = event_marginal.get(j, 0) + value
    ub_rows = list(monotone_rows.values()) + [
        {j: -v for j, v in event_marginal.items()}
    ]

    objective_counts = [0 for _ in range(n)]
    for w in range(1024):
        conn = connected_set(w)
        for s in range(16):
            if s & conn:
                objective_counts[pair_orbit[(w, s)]] += 1
    return (pair_orbit, representatives, config_reps, eq_rows,
            list(monotone_rows.values()), ub_rows, objective_counts)


def solve(r, eq_rows, ub_rows, objective_counts):
    n = len(objective_counts)
    result = linprog(
        np.asarray(objective_counts) / 1024.0,
        A_ub=sparse_matrix(ub_rows, n),
        b_ub=np.r_[np.zeros(len(ub_rows) - 1), -1024 * float(r)],
        A_eq=sparse_matrix(eq_rows, n),
        b_eq=np.ones(len(eq_rows)),
        bounds=(0, None), method="highs",
        options={"dual_feasibility_tolerance": 1e-9,
                 "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result


def rational_primal(result, r, representatives, pair_orbit, config_reps,
                    monotone_rows, ub_rows, objective_counts):
    x = [Fraction(float(v)).limit_denominator(10**9) for v in result.x]
    assert min(x) >= 0
    for w in config_reps:
        assert sum(x[pair_orbit[(w, s)]] for s in range(16)) == 1
    for row in monotone_rows:
        assert sum(a * x[j] for j, a in row.items()) <= 0
    marginal = -sum(a * x[j] for j, a in ub_rows[-1].items()) / 1024
    objective = sum(Fraction(c, 1024) * v
                    for c, v in zip(objective_counts, x))
    assert marginal == r
    return {
        "r": str(r),
        "objective": str(objective),
        "nonzero_orbit_values": [
            {"omega": w, "subset": s, "value": str(x[j])}
            for j, (w, s) in enumerate(representatives) if x[j]
        ],
    }


def rational_dual(result, expected_line, eq_rows, ub_rows, objective_counts):
    yub = [Fraction(float(v)).limit_denominator(10**9)
           for v in result.ineqlin.marginals]
    yeq = [Fraction(float(v)).limit_denominator(10**9)
           for v in result.eqlin.marginals]
    lhs = [Fraction(0) for _ in objective_counts]
    for y, row in zip(yub, ub_rows):
        for j, a in row.items():
            lhs[j] += y * a
    for y, row in zip(yeq, eq_rows):
        for j, a in row.items():
            lhs[j] += y * a
    assert all(y <= 0 for y in yub)
    assert all(Fraction(c, 1024) - v >= 0
               for c, v in zip(objective_counts, lhs))
    slope = -1024 * yub[-1]
    intercept = sum(yeq)
    assert (slope, intercept) == expected_line
    return {
        "slope": str(slope), "intercept": str(intercept),
        "nonzero_ub_duals": [
            {"constraint": i, "value": str(v)}
            for i, v in enumerate(yub) if v
        ],
        "nonzero_eq_duals": [
            {"constraint": i, "value": str(v)}
            for i, v in enumerate(yeq) if v
        ],
    }


def main():
    (pair_orbit, representatives, config_reps, eq_rows, monotone_rows,
     ub_rows, objective_counts) = build_lp()
    primals = [
        rational_primal(
            solve(r, eq_rows, ub_rows, objective_counts), r, representatives,
            pair_orbit, config_reps, monotone_rows, ub_rows, objective_counts,
        ) for r in BREAKPOINTS
    ]
    duals = [
        rational_dual(
            solve(r, eq_rows, ub_rows, objective_counts), line,
            eq_rows, ub_rows, objective_counts,
        ) for r, line in zip(DUAL_SAMPLES, EXPECTED_LINES)
    ]

    for i, (slope, intercept) in enumerate(EXPECTED_LINES):
        left, right = BREAKPOINTS[i:i + 2]
        assert Fraction(primals[i]["objective"]) == slope * left + intercept
        assert Fraction(primals[i + 1]["objective"]) == slope * right + intercept

    cert = {
        "format": "exact RHS-parametric S4-invariant joint-kernel LP certificate",
        "parameters": {"p": "1/2", "r_range": "[3/4,1]", "r": "1-t^2"},
        "edge_order": [list(e) for e in EDGES],
        "symmetry_group": "all 24 permutations of vertices 1,2,3,4 fixing 0",
        "pair_orbit_variables": len(representatives),
        "configuration_orbits": len(config_reps),
        "distinct_monotonicity_rows": len(monotone_rows),
        "breakpoints": [str(v) for v in BREAKPOINTS],
        "endpoint_primals": primals,
        "branch_duals": duals,
        "optimum_formula": [
            {"r_interval": [str(BREAKPOINTS[i]), str(BREAKPOINTS[i + 1])],
             "slope": str(line[0]), "intercept": str(line[1])}
            for i, line in enumerate(EXPECTED_LINES)
        ],
    }
    out = Path(__file__).with_name("lp_p_half_parametric_certificate.json")
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "certificate": out.name,
        "breakpoints": cert["breakpoints"],
        "optimum_formula": cert["optimum_formula"],
        "endpoint_objectives": [v["objective"] for v in primals],
        "exact_generation_checks": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
