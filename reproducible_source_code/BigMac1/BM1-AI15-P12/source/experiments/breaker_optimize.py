#!/usr/bin/env python3
"""Adversarial floating-point search in the generic canonical rank-two chart.

Floating point is discovery-only.  Any positive candidate is rounded to a
nearby rational/integer canonical matrix and passed to breaker_search.py's
exact_record before it is reported as a counterexample.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import random
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import differential_evolution, minimize

from breaker_search import duplicated_permanent_dp, exact_record, permanent_ryser


def elementary(xs):
    ans = np.zeros(len(xs) + 1)
    ans[0] = 1.0
    for x in xs:
        for k in range(len(xs), 0, -1):
            ans[k] += x * ans[k - 1]
    return ans


def canonical_objective(a, b):
    """Return D/Frobenius^(2n), evaluated directly on the small entries.

    The elementary-symmetric binary-factor expansion can suffer catastrophic
    cancellation near 1+a_i*b_j=0.  Direct Ryser plus coefficient DP is the
    primary discovery evaluator here; exact certification is still separate.
    """
    n = len(a)
    t = 1.0 + np.outer(a, b)
    p = permanent_ryser(t)
    q = duplicated_permanent_dp(t)
    d = q - math.comb(2*n, n) * p*p
    denom = max(1e-300, float(np.sum(t*t)) ** n)
    return d / denom, p, q


def objective_flat(x):
    n = len(x) // 2
    d, _, _ = canonical_objective(x[:n], x[n:])
    return -d


def away_from_rank_one(x, min_variance=0.05):
    n = len(x) // 2
    return np.var(x[:n]) >= min_variance and np.var(x[n:]) >= min_variance


def exactify_if_positive(x, max_denominator=10000):
    """Round canonical parameters to fixed-denominator rationals and clear rows."""
    n = len(x) // 2
    den = max_denominator
    ai = [int(round(den * z)) for z in x[:n]]
    bi = [int(round(den * z)) for z in x[n:]]
    # den^2 * (1 + (ai/den)(bi/den)) is an integer matrix.  This is
    # a global positive scaling, so it preserves the sign of D.
    t = [[den*den + u*v for v in bi] for u in ai]
    rec = exact_record(t, "floating-adversarial-rounded", {
        "common_denominator": den, "a_numerators": ai, "b_numerators": bi
    })
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", required=True, type=int, choices=(3, 4))
    ap.add_argument("--seed", type=int, default=120040)
    ap.add_argument("--random-trials", type=int, default=200000)
    ap.add_argument("--de-maxiter", type=int, default=1200)
    ap.add_argument("--bound", type=float, default=20.0)
    ap.add_argument("--log", required=True, type=Path)
    ap.add_argument("--certificate", type=Path)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    best = (-float("inf"), None, None, None)
    accepted = 0
    for _ in range(args.random_trials):
        # Mixture attacks ordinary, near-zero, large-ratio, and sign-mixed charts.
        family = int(rng.integers(0, 4))
        if family == 0:
            x = rng.normal(0, 1, 2*args.n)
        elif family == 1:
            x = rng.uniform(-args.bound, args.bound, 2*args.n)
        elif family == 2:
            mags = np.exp(rng.uniform(-5, 5, 2*args.n))
            x = mags * rng.choice(np.array([-1.0, 1.0]), 2*args.n)
        else:
            x = rng.normal(0, 1e-3, 2*args.n)
            x[rng.integers(0, 2*args.n)] = rng.choice([-args.bound, args.bound])
        if not away_from_rank_one(x):
            continue
        accepted += 1
        d, p, q = canonical_objective(x[:args.n], x[args.n:])
        if d > best[0]:
            best = (float(d), x.copy(), float(p), float(q))

    bounds = [(-args.bound, args.bound)] * (2*args.n)
    de = differential_evolution(
        objective_flat, bounds, seed=args.seed + 1, maxiter=args.de_maxiter,
        popsize=20, tol=1e-10, polish=False, workers=1, updating="immediate",
    )
    local = minimize(objective_flat, de.x, method="Nelder-Mead",
                     options={"maxiter": 20000, "xatol": 1e-12, "fatol": 1e-14})
    candidates = [
        ("random", best[0], best[1], best[2], best[3]),
        ("differential_evolution", -float(de.fun), de.x, *canonical_objective(de.x[:args.n], de.x[args.n:])[1:]),
        ("nelder_mead", -float(local.fun), local.x, *canonical_objective(local.x[:args.n], local.x[args.n:])[1:]),
    ]
    winner = max(candidates, key=lambda z: z[1])

    certificate = None
    rounding_diagnostic = None
    if winner[1] > 0:
        rounding_diagnostic = exactify_if_positive(winner[2])
    if winner[1] > 1e-10:
        certificate = rounding_diagnostic
        if certificate["strict_difference_left_minus_right"] > 0 and args.certificate:
            args.certificate.parent.mkdir(parents=True, exist_ok=True)
            args.certificate.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")

    log = {
        "schema": "breaker-floating-search-v1",
        "discovery_only": True,
        "n": args.n,
        "seed": args.seed,
        "random_trials": args.random_trials,
        "accepted_away_from_rank_one": accepted,
        "bound": args.bound,
        "differential_evolution_maxiter": args.de_maxiter,
        "environment": {
            "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__
        },
        "objective": "(per(block)-binom(2n,n)per(T)^2)/(sum_ij T_ij^2)^n",
        "parameterization": "T_ij=1+a_i*b_j",
        "candidates": [
            {"method": name, "normalized_D": d, "parameters": x.tolist(), "per_T_unscaled": p, "per_block_unscaled": q}
            for name, d, x, p, q in candidates
        ],
        "exact_positive_certificate": certificate if certificate and certificate["strict_difference_left_minus_right"] > 0 else None,
        "exact_fixed_denominator_rounding_diagnostic": rounding_diagnostic,
    }
    args.log.parent.mkdir(parents=True, exist_ok=True)
    args.log.write_text(json.dumps(log, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"winner_method": winner[0], "normalized_D": winner[1],
                      "exact_positive": log["exact_positive_certificate"] is not None}, sort_keys=True))


if __name__ == "__main__":
    main()
