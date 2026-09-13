#!/usr/bin/env python3
"""Independent verifier for serialized breaker records.

This file deliberately imports no discovery code.  It reconstructs the
literal block matrix, computes both permanents with a row/mask dynamic
program, checks exact rational rank by Gaussian elimination, and compares all
serialized integers.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


def permanent_mask_dp(a):
    n = len(a)
    dp = {0: 1}
    for i in range(n):
        nxt = {}
        for mask, value in dp.items():
            for j in range(n):
                if not (mask >> j) & 1:
                    new = mask | (1 << j)
                    nxt[new] = nxt.get(new, 0) + value * a[i][j]
        dp = nxt
    return dp[(1 << n) - 1]


def rational_rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    r = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][col] != 0), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pivot_value = m[r][col]
        for j in range(col, len(m[0])):
            m[r][j] /= pivot_value
        for i in range(r + 1, len(m)):
            multiplier = m[i][col]
            if multiplier:
                for j in range(col, len(m[0])):
                    m[i][j] -= multiplier * m[r][j]
        r += 1
    return r


def verify_record(rec):
    t = rec["matrix"]
    n = len(t)
    assert n == rec["n"] and all(len(row) == n for row in t)
    block = []
    for copy_i in range(2):
        for i in range(n):
            block.append(t[i] + t[i])
    rank = rational_rank(t)
    p = permanent_mask_dp(t)
    q = permanent_mask_dp(block)
    rhs = math.comb(2*n, n) * p*p
    computed = {
        "rank_over_Q": rank,
        "per_T": p,
        "binomial": math.comb(2*n, n),
        "per_duplicated_block": q,
        "rhs": rhs,
        "strict_difference_left_minus_right": q-rhs,
    }
    for key, value in computed.items():
        assert rec[key] == value, f"{key}: serialized {rec[key]} != recomputed {value}"
    assert rank <= 2, f"rank condition failed: {rank}"
    return computed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path)
    args = ap.parse_args()
    results = []
    for path in args.paths:
        data = json.loads(path.read_text())
        rec = data.get("best_exact_recheck", data)
        if rec is None:
            results.append({"path": str(path), "status": "no-record"})
            continue
        computed = verify_record(rec)
        results.append({"path": str(path), "status": "verified", **computed})
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
