#!/usr/bin/env python3
"""Independent AND-recurrence and normalised-elimination kernel-rank check."""

import hashlib
import json
import sys

import numpy as np


def sequence_via_and(limit, int64_max):
    a = np.empty(limit + 1, dtype=np.int64)
    a[0], a[1] = 0, 1
    maximum = 2
    for n in range(2, limit + 1):
        x, y = int(a[n - 2]), int(a[n - 1])
        guard = abs(x) + abs(y) + n
        assert guard <= int64_max
        maximum = max(maximum, guard)
        a[n] = y + n - 2 * (y & n) - x
    return a, maximum


def make_matrix(a, name, level_count):
    size = (1 << level_count) - 1
    matrix = np.empty((size, size), dtype=np.int64)
    columns = np.arange(size, dtype=np.int64)
    row = 0
    for e in range(level_count):
        for r in range(1 << e):
            q = (1 << e) * columns + r
            if name == "U":
                values = a[6 * q + 1] - 1
            elif name == "V":
                values = a[12 * q + 8] - 1
            else:
                assert name == "W"
                values = a[6 * q + 3] + 1
            assert np.all(values % 4 == 0)
            matrix[row] = values // 4
            row += 1
    return matrix


def normalised_determinant_mod(matrix, prime):
    """A separately written elimination that normalises each pivot row."""
    a = matrix.copy() % prime
    size = len(a)
    determinant = 1
    for c in range(size):
        nz = np.flatnonzero(a[c:, c])
        if not len(nz):
            return 0
        pivot = c + int(nz[0])
        if pivot != c:
            a[[c, pivot]] = a[[pivot, c]]
            determinant = (-determinant) % prime
        pivot_value = int(a[c, c])
        determinant = determinant * pivot_value % prime
        a[c, c:] = a[c, c:] * pow(pivot_value, prime - 2, prime) % prime
        coefficients = a[c + 1:, c].copy()
        a[c + 1:, c:] = (
            a[c + 1:, c:] - coefficients[:, None] * a[c, c:]
        ) % prime
    return int(determinant)


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/kernel-rank-evidence.json"
with open(path, encoding="utf-8") as handle:
    claim = json.load(handle)
assert claim["schema_version"] == 1
parameters = claim["parameters"]
recurrence = claim["recurrence"]
a, maximum = sequence_via_and(parameters["recurrence_limit"], recurrence["int64_max"])
assert maximum == recurrence["maximum_conservative_step_bound"]
assert [int(a[-2]), int(a[-1])] == recurrence["final_pair"]

for name in ("U", "V", "W"):
    matrix = make_matrix(a, name, parameters["max_level_count"])
    assert hashlib.sha256(matrix.tobytes()).hexdigest() == claim["results"][name]["largest_matrix_sha256"]
    for item in claim["results"][name].get("boundary_tests", []):
        size = item["dimension"]
        assert size == (1 << item["level_count"]) - 1
        minor = matrix[:size, :size]
        values = []
        for prime_text, expected in item["determinants_mod_primes"].items():
            actual = normalised_determinant_mod(minor, int(prime_text))
            assert actual == expected
            values.append(actual)
        assert item["all_nonzero"] == all(values)
    for item in claim["results"][name]["tests"]:
        size = item["dimension"]
        assert size == (1 << item["level_count"]) - 1
        minor = matrix[:size, :size]
        for prime_text, expected in item["determinants_mod_primes"].items():
            assert normalised_determinant_mod(minor, int(prime_text)) == expected != 0
        assert item["all_nonzero"] is True

assert parameters["largest_dimension"] == (1 << parameters["max_level_count"]) - 1
print(json.dumps({
    "status": "PASS",
    "recurrence_limit": parameters["recurrence_limit"],
    "largest_dimension": parameters["largest_dimension"],
    "sequences": ["U", "V", "W"],
    "primes": parameters["primes"],
}, separators=(",", ":")))
