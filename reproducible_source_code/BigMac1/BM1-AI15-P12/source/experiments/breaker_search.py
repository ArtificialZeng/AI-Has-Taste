#!/usr/bin/env python3
"""Counterexample search for the n=3,4 rank-two Marcus inequality.

Discovery evaluators:
  (A) coefficient DP specialized to the duplicated block matrix;
  (B) ordinary permanent by Ryser on the explicit 2n by 2n matrix.

Exact candidates are always rechecked with a third evaluator (permutations).
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import random
from pathlib import Path


def permanent_permutations(a):
    """Permanent over any exact scalar ring, by the definition."""
    n = len(a)
    return sum(
        math.prod(a[i][p[i]] for i in range(n))
        for p in itertools.permutations(range(n))
    )


def permanent_ryser(a):
    """Ryser evaluator (independent of coefficient DP)."""
    n = len(a)
    total = 0
    for mask in range(1, 1 << n):
        term = 1
        for row in a:
            term *= sum(row[j] for j in range(n) if mask >> j & 1)
        total += (-1 if (n - mask.bit_count()) & 1 else 1) * term
    return total


def duplicated_block(t):
    """[[T,T],[T,T]] in the literal block ordering."""
    n = len(t)
    return [
        [t[i % n][j % n] for j in range(2 * n)]
        for i in range(2 * n)
    ]


def duplicated_permanent_dp(t):
    """Coefficient evaluator for repeated rows and columns.

    per([[T,T],[T,T]]) = 2^n [z_1^2...z_n^2]
                             prod_i (sum_j T_ij z_j)^2.
    """
    n = len(t)
    zero = (0,) * n
    dp = {zero: 1}
    for i in range(n):
        nxt = {}
        for exps, old in dp.items():
            for j in range(n):
                for k in range(j, n):
                    new = list(exps)
                    new[j] += 1
                    new[k] += 1
                    if new[j] > 2 or new[k] > 2:
                        continue
                    coefficient = t[i][j] * t[i][k] * (1 if j == k else 2)
                    key = tuple(new)
                    nxt[key] = nxt.get(key, 0) + old * coefficient
        dp = nxt
    return (2**n) * dp.get((2,) * n, 0)


def rank_over_q(t):
    """Fraction-free exact rank for integer matrices."""
    from fractions import Fraction

    a = [[Fraction(x) for x in row] for row in t]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def exact_record(t, source, parameters):
    """Triple-check a serialized integer matrix and return an exact record."""
    n = len(t)
    p_perm = permanent_permutations(t)
    p_ryser = permanent_ryser(t)
    assert p_perm == p_ryser
    b = duplicated_block(t)
    q_perm = permanent_permutations(b)
    q_ryser = permanent_ryser(b)
    q_dp = duplicated_permanent_dp(t)
    assert q_perm == q_ryser == q_dp
    rhs = math.comb(2 * n, n) * p_perm * p_perm
    return {
        "schema": "breaker-candidate-v1",
        "n": n,
        "field": "Z",
        "source": source,
        "parameters": parameters,
        "matrix": t,
        "rank_over_Q": rank_over_q(t),
        "per_T": p_perm,
        "binomial": math.comb(2 * n, n),
        "per_duplicated_block": q_perm,
        "rhs": rhs,
        "strict_difference_left_minus_right": q_perm - rhs,
        "evaluators": [
            "definition/permutation enumeration",
            "Ryser inclusion-exclusion",
            "repeated-row/column coefficient DP",
        ],
    }


def matrix_uv(u, x, v, y):
    return [[u[i] * v[j] + x[i] * y[j] for j in range(len(v))] for i in range(len(u))]


def matrix_canonical(a, b):
    return [[1 + ai * bj for bj in b] for ai in a]


def score_fast(t):
    n = len(t)
    p = permanent_ryser(t)
    q = duplicated_permanent_dp(t)
    return q - math.comb(2 * n, n) * p * p


def random_vector(rng, n, bound, nonzero=False):
    while True:
        ans = [rng.randint(-bound, bound) for _ in range(n)]
        if not nonzero or any(ans):
            return ans


def random_search(n, trials, bound, seed, mode):
    rng = random.Random(seed)
    best_score = None
    best_data = None
    zero_per_best = None
    for iteration in range(1, trials + 1):
        if mode == "uv":
            u = random_vector(rng, n, bound, True)
            x = random_vector(rng, n, bound, True)
            v = random_vector(rng, n, bound, True)
            y = random_vector(rng, n, bound, True)
            t = matrix_uv(u, x, v, y)
            pars = {"u": u, "x": x, "v": v, "y": y}
        elif mode == "canonical":
            a = random_vector(rng, n, bound)
            b = random_vector(rng, n, bound)
            t = matrix_canonical(a, b)
            pars = {"a": a, "b": b}
        else:
            raise ValueError(mode)
        d = score_fast(t)
        scale = max(1, max(abs(z) for row in t for z in row)) ** (2 * n)
        normalized = d / scale
        if best_score is None or normalized > best_score:
            best_score = normalized
            best_data = (normalized, d, t, pars, iteration)
        if permanent_ryser(t) == 0 and (zero_per_best is None or d > zero_per_best[0]):
            zero_per_best = (d, t, pars, iteration)
        if d > 0:
            return exact_record(t, f"random-{mode}", {**pars, "seed": seed, "iteration": iteration}), best_data
    return None, best_data


def zero_permanent_search(n, trials, bound, seed):
    """Force per(T)=0 by solving exactly for the final canonical row ratio.

    Starting with T_ij=1+a_i*b_j, the permanent is affine in a_n.
    If per(T)|_{a_n=0}=c0 and the linear coefficient is c1, choose
    a_n=-c0/c1 and multiply the final row by c1.  The resulting integer
    matrix has final row c1-c0*b_j and permanent exactly zero.
    """
    rng = random.Random(seed)
    best = None
    for iteration in range(1, trials + 1):
        ahead = random_vector(rng, n - 1, bound)
        b = random_vector(rng, n, bound)
        t0 = matrix_canonical(ahead + [0], b)
        t1 = matrix_canonical(ahead + [1], b)
        c0 = permanent_ryser(t0)
        c1 = permanent_ryser(t1) - c0
        if c1 == 0:
            continue
        t = t0[:-1] + [[c1 - c0 * bj for bj in b]]
        assert permanent_ryser(t) == 0
        q = duplicated_permanent_dp(t)
        scale = max(1, max(abs(z) for row in t for z in row)) ** (2 * n)
        score = q / scale
        if best is None or score > best[0]:
            best = (score, q, t, {"a_head": ahead, "b": b, "c0": c0, "c1": c1}, iteration)
        if q > 0:
            pars = {
                "a_head": ahead,
                "b": b,
                "c0": c0,
                "c1": c1,
                "a_final": f"{-c0}/{c1}",
                "final_row_scaled_by": c1,
                "seed": seed,
                "iteration": iteration,
            }
            return exact_record(t, "forced-zero-permanent-canonical", pars), best
    return None, best


def sparse_exhaustion(n, alphabet):
    """Exhaust U,V in a small alphabet after fixing a GL(2) gauge on U.

    U has first two rows e1,e2; remaining rows range over alphabet^2.
    This covers a useful sparse boundary chart, not all rank-two matrices.
    """
    best = None
    tail_count = 2 * (n - 2)
    for flat_u in itertools.product(alphabet, repeat=tail_count):
        urows = [[1, 0], [0, 1]] + [list(flat_u[2*i:2*i+2]) for i in range(n - 2)]
        for flat_v in itertools.product(alphabet, repeat=2*n):
            vrows = [flat_v[2*j:2*j+2] for j in range(n)]
            t = [[sum(urows[i][k] * vrows[j][k] for k in range(2)) for j in range(n)] for i in range(n)]
            d = score_fast(t)
            scale = max(1, max(abs(z) for row in t for z in row)) ** (2 * n)
            normalized = d / scale
            if best is None or normalized > best[0]:
                best = (normalized, d, t, urows, vrows)
            if d > 0:
                rec = exact_record(t, "sparse-gauge-exhaustion", {
                    "U_rows": urows, "V_rows": vrows, "alphabet": list(alphabet)
                })
                return rec, best
    return None, best


def save_record(record, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, choices=(3, 4), required=True)
    ap.add_argument("--mode", choices=("uv", "canonical", "zero", "sparse"), required=True)
    ap.add_argument("--trials", type=int, default=100000)
    ap.add_argument("--bound", type=int, default=3)
    ap.add_argument("--seed", type=int, default=120034)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--log", type=Path)
    args = ap.parse_args()
    if args.mode == "sparse":
        record, best = sparse_exhaustion(args.n, tuple(range(-args.bound, args.bound + 1)))
    elif args.mode == "zero":
        record, best = zero_permanent_search(args.n, args.trials, args.bound, args.seed)
    else:
        record, best = random_search(args.n, args.trials, args.bound, args.seed, args.mode)
    best_record = exact_record(best[2], f"best-nonpositive-{args.mode}", {
        "seed": args.seed, "mode": args.mode, "iteration": best[4]
    }) if best else None
    summary = {
        "schema": "breaker-exact-search-v1",
        "discovery_arithmetic": "exact integers",
        "n": args.n,
        "mode": args.mode,
        "seed": args.seed,
        "trials_requested": args.trials if args.mode != "sparse" else None,
        "bound": args.bound,
        "alphabet": list(range(-args.bound, args.bound + 1)) if args.mode == "sparse" else None,
        "sparse_cases": ((2*args.bound+1) ** (2*(args.n-2)+2*args.n)) if args.mode == "sparse" else None,
        "counterexample": record,
        "best_normalized": best[0] if best else None,
        "best_raw_difference": best[1] if best else None,
        "best_matrix": best[2] if best else None,
        "best_exact_recheck": best_record,
        "evaluators_for_best": [
            "definition/permutation enumeration", "Ryser inclusion-exclusion",
            "repeated-row/column coefficient DP"
        ],
        "environment": {"python": platform.python_version()},
    }
    # Keep stdout concise; exact positives are serialized in full.
    print(json.dumps({
        "found": record is not None,
        "best_normalized": summary["best_normalized"],
        "best_raw_difference": summary["best_raw_difference"],
    }, sort_keys=True))
    if record is not None and args.output:
        save_record(record, args.output)
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        args.log.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
