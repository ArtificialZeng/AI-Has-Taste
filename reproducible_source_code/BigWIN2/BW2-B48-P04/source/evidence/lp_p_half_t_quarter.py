#!/usr/bin/env python3
"""S4-orbit LP and exact unreduced replay for p=1/2, t=1/4.

The only numerical step is discovery of an orbit optimizer with SciPy/HiGHS.
Every reported feasibility and objective assertion is then recomputed over all
1024 configurations with fractions.Fraction.
"""

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


EDGES = (
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4),
)
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
PERMS = tuple((0,) + p for p in permutations((1, 2, 3, 4)))


def act_config(w, perm):
    out = 0
    for i, (u, v) in enumerate(EDGES):
        if (w >> i) & 1:
            e = tuple(sorted((perm[u], perm[v])))
            out |= 1 << EDGE_INDEX[e]
    return out


def act_subset(s, perm):
    out = 0
    for b in range(1, 5):
        if (s >> (b - 1)) & 1:
            out |= 1 << (perm[b] - 1)
    return out


def connected_set(w):
    seen = {0}
    changed = True
    while changed:
        changed = False
        for i, (u, v) in enumerate(EDGES):
            if not ((w >> i) & 1):
                continue
            if u in seen and v not in seen:
                seen.add(v)
                changed = True
            elif v in seen and u not in seen:
                seen.add(u)
                changed = True
    return sum(1 << (b - 1) for b in seen if b)


def sparse_matrix(rows, ncols):
    rr, cc, vv = [], [], []
    for i, row in enumerate(rows):
        for j, value in row.items():
            rr.append(i)
            cc.append(j)
            vv.append(value)
    return coo_matrix((vv, (rr, cc)), shape=(len(rows), ncols)).tocsr()


def build_orbits():
    pair_orbit = {}
    representatives = []
    for w in range(1024):
        for s in range(16):
            if (w, s) in pair_orbit:
                continue
            oid = len(representatives)
            representatives.append((w, s))
            for perm in PERMS:
                pair_orbit[(act_config(w, perm), act_subset(s, perm))] = oid

    config_orbit = {}
    config_reps = []
    for w in range(1024):
        if w in config_orbit:
            continue
        oid = len(config_reps)
        config_reps.append(w)
        for perm in PERMS:
            config_orbit[act_config(w, perm)] = oid
    return pair_orbit, representatives, config_reps


def marginal_row(pair_orbit, w, b):
    row = {}
    bit = 1 << (b - 1)
    for s in range(16):
        if s & bit:
            j = pair_orbit[(w, s)]
            row[j] = row.get(j, 0) + 1
    return row


def row_difference(left, right):
    row = dict(left)
    for j, value in right.items():
        row[j] = row.get(j, 0) - value
        if row[j] == 0:
            del row[j]
    return row


def canonical_row(row):
    return tuple(sorted(row.items()))


def exact_replay(x, pair_orbit):
    normalization_failures = []
    negativity_failures = []
    monotonicity_failures = []
    marg_sums = [Fraction(0) for _ in range(4)]
    objective_sum = Fraction(0)
    connected_nonempty = 0

    for value in x:
        if value < 0:
            negativity_failures.append(str(value))

    for w in range(1024):
        qsum = sum(x[pair_orbit[(w, s)]] for s in range(16))
        if qsum != 1:
            normalization_failures.append((w, str(qsum)))
        conn = connected_set(w)
        if conn:
            connected_nonempty += 1
        for s in range(16):
            value = x[pair_orbit[(w, s)]]
            if s & conn:
                objective_sum += value
            for b in range(4):
                if s & (1 << b):
                    marg_sums[b] += value

        for e in range(10):
            if (w >> e) & 1:
                continue
            wp = w | (1 << e)
            for b in range(1, 5):
                bit = 1 << (b - 1)
                q0 = sum(x[pair_orbit[(w, s)]] for s in range(16) if s & bit)
                q1 = sum(x[pair_orbit[(wp, s)]] for s in range(16) if s & bit)
                if q0 > q1:
                    monotonicity_failures.append((w, e, b, str(q0), str(q1)))

    objective = objective_sum / 1024
    marginals = [m / 1024 for m in marg_sums]
    return {
        "normalization_failures": normalization_failures,
        "negativity_failures": negativity_failures,
        "monotonicity_failures": monotonicity_failures,
        "marginals": [str(v) for v in marginals],
        "objective": str(objective),
        "objective_numerator_sum": str(objective_sum),
        "conditioning_probability": str(Fraction(15, 16)),
        "target": str(Fraction(15, 32)),
        "objective_minus_target": str(objective - Fraction(15, 32)),
        "connected_configuration_count": connected_nonempty,
        "exact_feasible": (
            not normalization_failures
            and not negativity_failures
            and not monotonicity_failures
            and all(v >= Fraction(15, 16) for v in marginals)
        ),
    }


def exact_dual_replay(objective_counts, ub_rows, ub_rhs, eq_rows, result):
    yub = [Fraction(float(v)).limit_denominator(10**9)
           for v in result.ineqlin.marginals]
    yeq = [Fraction(float(v)).limit_denominator(10**9)
           for v in result.eqlin.marginals]
    dual_columns = [Fraction(0) for _ in range(len(objective_counts))]
    for y, row in zip(yub, ub_rows):
        for j, a in row.items():
            dual_columns[j] += y * a
    for y, row in zip(yeq, eq_rows):
        for j, a in row.items():
            dual_columns[j] += y * a
    exact_c = [Fraction(int(v), 1024) for v in objective_counts]
    reduced_costs = [c - lhs for c, lhs in zip(exact_c, dual_columns)]
    dual_objective = sum(
        y * Fraction(int(b)) for y, b in zip(yub, ub_rhs)
    ) + sum(yeq)
    return {
        "ub_sign_failures": [i for i, y in enumerate(yub) if y > 0],
        "dual_column_failures": [
            {"variable": j, "reduced_cost": str(v)}
            for j, v in enumerate(reduced_costs) if v < 0
        ],
        "dual_objective": str(dual_objective),
        "nonzero_ub_duals": [
            {"constraint": i, "value": str(y)} for i, y in enumerate(yub) if y
        ],
        "nonzero_eq_duals": [
            {"constraint": i, "value": str(y)} for i, y in enumerate(yeq) if y
        ],
        "exact_dual_feasible": (
            all(y <= 0 for y in yub) and all(v >= 0 for v in reduced_costs)
        ),
    }


def main():
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

    # Under invariant kernels the four event marginals agree, so b=1 suffices.
    event_marginal = {}
    for w in range(1024):
        for j, value in marginal_row(pair_orbit, w, 1).items():
            event_marginal[j] = event_marginal.get(j, 0) + value
    probability_row = {j: -v for j, v in event_marginal.items()}
    ub_rows = list(monotone_rows.values()) + [probability_row]
    ub_rhs = np.r_[np.zeros(len(monotone_rows)), -960.0]

    objective_counts = np.zeros(n)
    for w in range(1024):
        conn = connected_set(w)
        for s in range(16):
            if s & conn:
                objective_counts[pair_orbit[(w, s)]] += 1

    result = linprog(
        objective_counts / 1024.0,
        A_ub=sparse_matrix(ub_rows, n),
        b_ub=ub_rhs,
        A_eq=sparse_matrix(eq_rows, n),
        b_eq=np.ones(len(eq_rows)),
        bounds=(0, None),
        method="highs",
        options={"dual_feasibility_tolerance": 1e-9,
                 "primal_feasibility_tolerance": 1e-9},
    )
    if not result.success:
        raise RuntimeError(result.message)

    # HiGHS returns a basic rational vertex numerically. Reconstruct its entries
    # with a generous denominator cap, then accept it only if exact replay passes.
    x_fraction = [Fraction(float(v)).limit_denominator(10**9) for v in result.x]
    replay = exact_replay(x_fraction, pair_orbit)
    dual_replay = exact_dual_replay(
        objective_counts, ub_rows, ub_rhs, eq_rows, result
    )
    exact_optimum_certified = (
        replay["exact_feasible"]
        and dual_replay["exact_dual_feasible"]
        and replay["objective"] == dual_replay["dual_objective"]
    )

    used_values = sorted({str(v) for v in x_fraction if v})
    report = {
        "parameters": {"p": "1/2", "t": "1/4", "epsilon": "1/16"},
        "edge_order": [list(e) for e in EDGES],
        "symmetry_group": "all 24 permutations of vertices 1,2,3,4 fixing 0",
        "pair_orbit_variables": n,
        "configuration_orbits": len(config_reps),
        "distinct_monotonicity_rows": len(monotone_rows),
        "solver_status": result.message,
        "floating_objective": result.fun,
        "nonzero_orbit_variables": sum(v != 0 for v in x_fraction),
        "distinct_nonzero_values": used_values,
        "exact_replay": replay,
        "exact_dual_replay": {
            "ub_sign_failures": dual_replay["ub_sign_failures"],
            "dual_column_failures": dual_replay["dual_column_failures"],
            "dual_objective": dual_replay["dual_objective"],
            "nonzero_ub_dual_count": len(dual_replay["nonzero_ub_duals"]),
            "nonzero_eq_dual_count": len(dual_replay["nonzero_eq_duals"]),
            "exact_dual_feasible": dual_replay["exact_dual_feasible"],
        },
        "exact_orbit_optimum_certified": exact_optimum_certified,
    }
    print(json.dumps(report, indent=2, sort_keys=True))

    # This compact orbit table losslessly expands to all 16384 Q_w(S) values.
    certificate = {
        "format": "S4-invariant joint-kernel orbit table",
        "parameters": report["parameters"],
        "edge_order": report["edge_order"],
        "orbit_representatives_and_values": [
            {"omega": w, "subset": s, "value": str(x_fraction[j])}
            for j, (w, s) in enumerate(representatives) if x_fraction[j]
        ],
        "exact_replay": replay,
        "dual_certificate": {
            "convention": (
                "min c*x, A_ub*x<=b_ub, A_eq*x=1, x>=0; "
                "dual y_ub<=0 and A_ub^T*y_ub+A_eq^T*y_eq<=c"
            ),
            "nonzero_ub_duals": dual_replay["nonzero_ub_duals"],
            "nonzero_eq_duals": dual_replay["nonzero_eq_duals"],
            "replay_summary": {
                "ub_sign_failures": dual_replay["ub_sign_failures"],
                "dual_column_failures": dual_replay["dual_column_failures"],
                "dual_objective": dual_replay["dual_objective"],
                "exact_dual_feasible": dual_replay["exact_dual_feasible"],
            },
        },
        "exact_orbit_optimum_certified": exact_optimum_certified,
    }
    out = Path(__file__).with_name("lp_p_half_t_quarter_certificate.json")
    out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
