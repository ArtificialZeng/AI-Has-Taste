#!/usr/bin/env python3
"""Exact finite 2-kernel rank tests for three unit-hit subsequences."""

import argparse
import hashlib
import json
import platform

import numpy as np


INT64_MAX = (1 << 63) - 1


def direct_sequence(limit):
    a = np.empty(limit + 1, dtype=np.int64)
    a[0], a[1] = 0, 1
    max_guard = 2
    for n in range(2, limit + 1):
        x, y = int(a[n - 2]), int(a[n - 1])
        guard = abs(x) + abs(y) + n
        if guard > INT64_MAX:
            raise OverflowError(f"int64 guard failed at n={n}")
        max_guard = max(max_guard, guard)
        a[n] = (y ^ n) - x
    return a, max_guard


def kernel_matrix(a, name, level_count):
    dimension = (1 << level_count) - 1
    columns = np.arange(dimension, dtype=np.int64)
    matrix = np.empty((dimension, dimension), dtype=np.int64)
    row = 0
    for e in range(level_count):
        for r in range(1 << e):
            q = (1 << e) * columns + r
            if name == "U":
                numerator = a[6 * q + 1] - 1
            elif name == "V":
                numerator = a[12 * q + 8] - 1
            else:
                assert name == "W"
                numerator = a[6 * q + 3] + 1
            assert np.all(numerator % 4 == 0)
            matrix[row] = numerator // 4
            row += 1
    assert row == dimension
    return matrix


def determinant_mod(matrix, prime):
    """Unnormalised modular Gaussian elimination."""
    a = matrix.copy() % prime
    size = a.shape[0]
    det = 1
    for c in range(size):
        candidates = np.flatnonzero(a[c:, c])
        if not len(candidates):
            return 0
        pivot = c + int(candidates[0])
        if pivot != c:
            a[[c, pivot]] = a[[pivot, c]]
            det = (-det) % prime
        value = int(a[c, c])
        det = (det * value) % prime
        inverse = pow(value, prime - 2, prime)
        factors = (a[c + 1:, c] * inverse) % prime
        a[c + 1:, c + 1:] = (
            a[c + 1:, c + 1:] - factors[:, None] * a[c, c + 1:]
        ) % prime
        a[c + 1:, c] = 0
    return int(det)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level-count", type=int, default=10)
    parser.add_argument("--min-level-count", type=int, default=3)
    parser.add_argument("--primes", type=int, nargs="+", default=[1_000_003, 1_000_033])
    parser.add_argument("--output")
    args = parser.parse_args()
    assert 3 <= args.min_level_count <= args.max_level_count <= 11
    largest_dimension = (1 << args.max_level_count) - 1
    max_q = (1 << (args.max_level_count - 1)) * (largest_dimension - 1) + (1 << (args.max_level_count - 1)) - 1
    recurrence_limit = 12 * max_q + 8
    a, max_guard = direct_sequence(recurrence_limit)

    results = {}
    for name in ("U", "V", "W"):
        matrix = kernel_matrix(a, name, args.max_level_count)
        boundary_tests = []
        for level_count in (1, 2):
            dimension = (1 << level_count) - 1
            minor = matrix[:dimension, :dimension]
            determinants = {str(p): determinant_mod(minor, p) for p in args.primes}
            boundary_tests.append({
                "level_count": level_count,
                "dimension": dimension,
                "determinants_mod_primes": determinants,
                "all_nonzero": all(determinants.values()),
            })
        tests = []
        for level_count in range(args.min_level_count, args.max_level_count + 1):
            dimension = (1 << level_count) - 1
            minor = matrix[:dimension, :dimension]
            determinants = {str(p): determinant_mod(minor, p) for p in args.primes}
            tests.append({
                "level_count": level_count,
                "dimension": dimension,
                "determinants_mod_primes": determinants,
                "all_nonzero": all(determinants.values()),
            })
        assert all(item["all_nonzero"] for item in tests)
        results[name] = {
            "largest_matrix_sha256": hashlib.sha256(matrix.tobytes()).hexdigest(),
            "boundary_tests": boundary_tests,
            "tests": tests,
        }

    assert results["U"]["boundary_tests"][0]["all_nonzero"] is False
    assert results["V"]["boundary_tests"][0]["all_nonzero"] is False
    assert results["V"]["boundary_tests"][1]["all_nonzero"] is False
    assert results["W"]["boundary_tests"][0]["all_nonzero"] is False
    assert results["W"]["boundary_tests"][1]["all_nonzero"] is False

    record = {
        "schema_version": 1,
        "purpose": "finite exact obstruction to low-rank rational 2-kernel representations",
        "sequence_definitions": {
            "U": "U(q)=(a_(6q+1)-1)/4",
            "V": "V(q)=(a_(12q+8)-1)/4",
            "W": "W(q)=(a_(6q+3)+1)/4",
        },
        "row_definition": "rows (e,r), ordered by e then r, are s(2^e*q+r), 0<=e<level_count, 0<=r<2^e; columns are q=0,...,2^level_count-2",
        "parameters": {
            "min_level_count": args.min_level_count,
            "max_level_count": args.max_level_count,
            "primes": args.primes,
            "recurrence_limit": recurrence_limit,
            "largest_dimension": largest_dimension,
            "maximum_q_index": max_q,
        },
        "recurrence": {
            "implementation": "direct signed XOR in guarded int64",
            "maximum_conservative_step_bound": max_guard,
            "int64_max": INT64_MAX,
            "final_pair": [int(a[-2]), int(a[-1])],
        },
        "results": results,
        "proved_finite_consequence": f"Each of U,V,W has rational 2-kernel rank at least {largest_dimension}.",
        "limitations": [
            "Finite rank 1023 does not prove infinite 2-kernel rank or non-2-regularity.",
            "The result does not exclude nonlinear finite-state or unbounded-carry descriptions.",
            "It does not resolve any of the three universal unit-value classifications.",
        ],
        "python": platform.python_version(),
        "numpy": np.__version__,
    }
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
