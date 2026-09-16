#!/usr/bin/env python3
"""Solver-free exact verifier for lp_p_half_t_quarter_certificate.json."""

from fractions import Fraction
from pathlib import Path
import json

from lp_p_half_t_quarter import (
    EDGES,
    build_orbits,
    canonical_row,
    connected_set,
    exact_replay,
    marginal_row,
    row_difference,
)


def main():
    path = Path(__file__).with_name("lp_p_half_t_quarter_certificate.json")
    cert = json.loads(path.read_text())
    assert cert["parameters"] == {"p": "1/2", "t": "1/4", "epsilon": "1/16"}
    assert cert["edge_order"] == [list(e) for e in EDGES]

    pair_orbit, representatives, config_reps = build_orbits()
    n = len(representatives)
    x = [Fraction(0) for _ in range(n)]
    for item in cert["orbit_representatives_and_values"]:
        pair = (item["omega"], item["subset"])
        j = pair_orbit[pair]
        assert representatives[j] == pair
        assert x[j] == 0
        x[j] = Fraction(item["value"])

    # Primal replay iterates every one of the 1024 configurations, 16 subsets,
    # 10 single-edge covers and 4 event marginals using exact fractions.
    primal = exact_replay(x, pair_orbit)
    assert primal["exact_feasible"]

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

    dc = cert["dual_certificate"]
    yub = [Fraction(0) for _ in ub_rows]
    yeq = [Fraction(0) for _ in eq_rows]
    for item in dc["nonzero_ub_duals"]:
        yub[item["constraint"]] = Fraction(item["value"])
    for item in dc["nonzero_eq_duals"]:
        yeq[item["constraint"]] = Fraction(item["value"])

    lhs = [Fraction(0) for _ in range(n)]
    for y, row in zip(yub, ub_rows):
        for j, a in row.items():
            lhs[j] += y * a
    for y, row in zip(yeq, eq_rows):
        for j, a in row.items():
            lhs[j] += y * a
    reduced_costs = [
        Fraction(c, 1024) - value for c, value in zip(objective_counts, lhs)
    ]
    dual_objective = -960 * yub[-1] + sum(yeq)
    dual_feasible = all(y <= 0 for y in yub) and all(v >= 0 for v in reduced_costs)
    assert dual_feasible
    assert primal["objective"] == str(dual_objective) == "1301/1536"

    result = {
        "certificate": path.name,
        "pair_orbit_variables": n,
        "configuration_orbits": len(config_reps),
        "unreduced_primal_replay": primal,
        "reduced_dual_feasible": dual_feasible,
        "dual_objective": str(dual_objective),
        "exact_optimum": str(dual_objective),
        "target": "15/32",
        "optimum_minus_target": str(dual_objective - Fraction(15, 32)),
        "verdict_at_test_point": "no counterexample; exact optimum exceeds target",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
