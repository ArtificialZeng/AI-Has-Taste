#!/usr/bin/env python3
"""Deterministic exact small-integer counterexample search for n=3 or n=4.

Two independent permanent evaluators are cross-checked:
  (1) Ryser inclusion-exclusion applied to T and its duplicated block;
  (2) the rank-two mixed-coefficient formula applied directly to U,V.
All arithmetic is Python integer arithmetic.  A positive gap means a violation.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import pathlib
import platform
import random
import sys


def permanent_ryser(matrix: list[list[int]]) -> int:
    n = len(matrix)
    total = 0
    for mask in range(1 << n):
        term = 1
        for row in matrix:
            term *= sum(row[j] for j in range(n) if (mask >> j) & 1)
        total += (-1) ** (n - mask.bit_count()) * term
    return total


def mixed_coefficients(factors: list[list[int]]) -> list[int]:
    """Coefficient k selects coordinate 0 in k rows and coordinate 1 otherwise."""
    n = len(factors)
    result = []
    for k in range(n + 1):
        value = 0
        for chosen in itertools.combinations(range(n), k):
            selected = set(chosen)
            term = 1
            for i, pair in enumerate(factors):
                term *= pair[0 if i in selected else 1]
            value += term
        result.append(value)
    return result


def permanent_rank_two(left: list[list[int]], right: list[list[int]]) -> int:
    n = len(left)
    lc = mixed_coefficients(left)
    rc = mixed_coefficients(right)
    return sum(math.factorial(k) * math.factorial(n - k) * lc[k] * rc[k] for k in range(n + 1))


def matrix_from_factors(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[j][k] for k in range(2)) for j in range(len(right))] for i in range(len(left))]


def duplicated_block(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    return [[matrix[i % n][j % n] for j in range(2 * n)] for i in range(2 * n)]


def evaluate(left: list[list[int]], right: list[list[int]]) -> dict[str, int | list[list[int]]]:
    n = len(left)
    matrix = matrix_from_factors(left, right)
    p_direct = permanent_ryser(matrix)
    q_direct = permanent_ryser(duplicated_block(matrix))
    p_factor = permanent_rank_two(left, right)
    q_factor = permanent_rank_two(left + left, right + right)
    if (p_direct, q_direct) != (p_factor, q_factor):
        raise AssertionError("independent evaluators disagree")
    violation_margin = q_direct - math.comb(2 * n, n) * p_direct**2
    return {"T": matrix, "per_T": p_direct, "per_block": q_direct, "violation_margin": violation_margin}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, choices=(3, 4), required=True)
    parser.add_argument("--trials", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=120829)
    parser.add_argument("--bound", type=int, default=3)
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    best = None
    witness = None
    for trial in range(args.trials):
        left = [[rng.randint(-args.bound, args.bound) for _ in range(2)] for _ in range(args.n)]
        right = [[rng.randint(-args.bound, args.bound) for _ in range(2)] for _ in range(args.n)]
        result = evaluate(left, right)
        record = {"trial": trial, "U": left, "V": right, **result}
        if best is None or int(record["violation_margin"]) > int(best["violation_margin"]):
            best = record
        if int(record["violation_margin"]) > 0:
            witness = record
            break
    code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    report = {
        "schema_version": 1,
        "status": "COUNTEREXAMPLE_FOUND" if witness else "NO_COUNTEREXAMPLE_IN_RECORDED_SEARCH",
        "scope_is_not_a_proof": True,
        "parameters": vars(args) | {"output": str(args.output) if args.output else None},
        "best": best,
        "witness": witness,
        "environment": {"python": sys.version, "platform": platform.platform()},
        "script_sha256": code_hash,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 1 if witness else 0


if __name__ == "__main__":
    raise SystemExit(main())
