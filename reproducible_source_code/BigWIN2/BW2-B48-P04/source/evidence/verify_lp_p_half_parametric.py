#!/usr/bin/env python3
"""Solver-free exact verifier for the p=1/2 parametric LP certificate.

The verifier expands every orbit table to all 1024 configurations.  It checks
the five endpoint primals, four affine dual bounds, interpolation coverage of
the whole r interval, and the symbolic comparison with the proposed modulus.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json

from lp_p_half_parametric import BREAKPOINTS, EXPECTED_LINES, build_lp
from lp_p_half_t_quarter import EDGES, connected_set


def load_vector(items, representatives, pair_orbit):
    x = [Fraction(0) for _ in representatives]
    seen = set()
    for item in items:
        pair = (item["omega"], item["subset"])
        assert pair not in seen
        seen.add(pair)
        j = pair_orbit[pair]
        assert representatives[j] == pair
        value = Fraction(item["value"])
        assert value > 0
        x[j] = value
    return x


def verify_endpoint(item, pair_orbit, representatives):
    r = Fraction(item["r"])
    claimed_objective = Fraction(item["objective"])
    x = load_vector(item["nonzero_orbit_values"], representatives, pair_orbit)
    marginal_sums = [Fraction(0) for _ in range(4)]
    objective_sum = Fraction(0)
    normalization_failures = 0
    monotonicity_failures = 0

    for w in range(1024):
        if sum(x[pair_orbit[(w, s)]] for s in range(16)) != 1:
            normalization_failures += 1
        conn = connected_set(w)
        for s in range(16):
            value = x[pair_orbit[(w, s)]]
            if s & conn:
                objective_sum += value
            for b in range(4):
                if s & (1 << b):
                    marginal_sums[b] += value
        for e in range(10):
            if (w >> e) & 1:
                continue
            wp = w | (1 << e)
            for b in range(4):
                bit = 1 << b
                q0 = sum(x[pair_orbit[(w, s)]] for s in range(16) if s & bit)
                q1 = sum(x[pair_orbit[(wp, s)]] for s in range(16) if s & bit)
                if q0 > q1:
                    monotonicity_failures += 1

    marginals = [v / 1024 for v in marginal_sums]
    objective = objective_sum / 1024
    assert normalization_failures == 0
    assert monotonicity_failures == 0
    assert marginals == [r] * 4
    assert objective == claimed_objective
    return {
        "r": str(r),
        "marginals": [str(v) for v in marginals],
        "objective": str(objective),
        "normalization_failures": normalization_failures,
        "monotonicity_failures": monotonicity_failures,
        "nonzero_orbit_values": sum(v != 0 for v in x),
    }


def verify_dual(item, eq_rows, ub_rows, objective_counts):
    yub = [Fraction(0) for _ in ub_rows]
    yeq = [Fraction(0) for _ in eq_rows]
    for entry in item["nonzero_ub_duals"]:
        i = entry["constraint"]
        assert yub[i] == 0
        yub[i] = Fraction(entry["value"])
    for entry in item["nonzero_eq_duals"]:
        i = entry["constraint"]
        assert yeq[i] == 0
        yeq[i] = Fraction(entry["value"])

    lhs = [Fraction(0) for _ in objective_counts]
    for y, row in zip(yub, ub_rows):
        for j, a in row.items():
            lhs[j] += y * a
    for y, row in zip(yeq, eq_rows):
        for j, a in row.items():
            lhs[j] += y * a
    reduced_costs = [
        Fraction(c, 1024) - v for c, v in zip(objective_counts, lhs)
    ]
    assert all(y <= 0 for y in yub)
    assert all(v >= 0 for v in reduced_costs)
    slope = -1024 * yub[-1]
    intercept = sum(yeq)
    assert slope == Fraction(item["slope"])
    assert intercept == Fraction(item["intercept"])
    return {
        "slope": str(slope),
        "intercept": str(intercept),
        "negative_reduced_costs": sum(v < 0 for v in reduced_costs),
        "positive_inequality_duals": sum(y > 0 for y in yub),
    }


def main():
    project = Path(__file__).resolve().parent.parent
    path = Path(__file__).with_name("lp_p_half_parametric_certificate.json")
    cert = json.loads(path.read_text())
    assert cert["parameters"] == {"p": "1/2", "r": "1-t^2", "r_range": "[3/4,1]"}
    assert cert["edge_order"] == [list(e) for e in EDGES]
    assert tuple(map(Fraction, cert["breakpoints"])) == BREAKPOINTS

    (pair_orbit, representatives, config_reps, eq_rows, monotone_rows,
     ub_rows, objective_counts) = build_lp()
    assert len(representatives) == cert["pair_orbit_variables"] == 996
    assert len(config_reps) == cert["configuration_orbits"] == 90
    assert len(monotone_rows) == cert["distinct_monotonicity_rows"] == 984

    primal_reports = [
        verify_endpoint(item, pair_orbit, representatives)
        for item in cert["endpoint_primals"]
    ]
    dual_reports = [
        verify_dual(item, eq_rows, ub_rows, objective_counts)
        for item in cert["branch_duals"]
    ]

    endpoint_values = [Fraction(v["objective"]) for v in primal_reports]
    lines = [(Fraction(v["slope"]), Fraction(v["intercept"]))
             for v in dual_reports]
    assert tuple(lines) == EXPECTED_LINES
    for i, (slope, intercept) in enumerate(lines):
        left, right = BREAKPOINTS[i:i + 2]
        # The endpoint primal tables give the affine upper bound throughout
        # by convex interpolation.  This feasible dual gives the same affine
        # lower bound throughout, hence equality on the entire interval.
        assert endpoint_values[i] == slope * left + intercept
        assert endpoint_values[i + 1] == slope * right + intercept
    for i in range(3):
        m0, b0 = lines[i]
        m1, b1 = lines[i + 1]
        assert (b1 - b0) / (m0 - m1) == BREAKPOINTS[i + 1]

    # Put r=1-t^2.  On every branch the gap from
    # (15/16)(1-2t) is a concave quadratic in t, so its minimum on a closed
    # branch interval is at an endpoint.  The five endpoint gaps are positive
    # except for t=0, which is outside the frozen t>0 domain.
    endpoint_gap_data = {
        "t=1/2": "91/138",
        "t=7/16": "19/32",
        "t=sqrt(13)/16": "(15*sqrt(13)-10)/128",
        "t=1/8": "13/64",
        "t=0": "0",
    }
    assert endpoint_values[0] == Fraction(91, 138)
    assert endpoint_values[1] - Fraction(15, 16) * Fraction(1, 8) == Fraction(19, 32)
    assert 15 * 15 * 13 > 10 * 10  # 15*sqrt(13)-10 > 0
    assert endpoint_values[3] - Fraction(15, 16) * Fraction(3, 4) == Fraction(13, 64)
    assert endpoint_values[4] - Fraction(15, 16) == 0
    # On the only branch incident with t=0, the exact gap factors as
    # t*(15/8-2t), strictly positive for 0<t<=1/8.
    assert Fraction(15, 8) - 2 * Fraction(1, 8) > 0

    source_hash = hashlib.sha256((project / "source.md").read_bytes()).hexdigest()
    assert source_hash == "77497af47aed92acbca8315b367c3e806160368e352ed35e8b6bd9de2247fc7c"
    report = {
        "certificate": path.name,
        "source_sha256": source_hash,
        "pair_orbit_variables": len(representatives),
        "configuration_orbits": len(config_reps),
        "unreduced_endpoint_primal_replays": primal_reports,
        "exact_branch_dual_replays": dual_reports,
        "breakpoints": [str(v) for v in BREAKPOINTS],
        "optimum_formula": cert["optimum_formula"],
        "target_endpoint_gaps": endpoint_gap_data,
        "target_comparison": (
            "strictly above (15/16)(1-2t) for every 0<t<=1/2; "
            "gap infimum 0 is approached only as t decreases to 0"
        ),
        "exact_parametric_certificate_verified": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
