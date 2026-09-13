#!/usr/bin/env python3
"""Independent exact verifier for builder_counterexample.json.

Only Python's standard library is used.  The verifier parses all numeric
entries as rational numbers, reconstructs every asserted matrix identity,
checks all 3-by-3 minors of A and B, and supplies nonzero 2-by-2 witnesses.
It deliberately does not trust the human-readable row relations in the JSON.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> "None":
    raise SystemExit("FAIL: " + message)


def parse_matrix(raw: object, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or len(raw) != 4:
        fail(f"{name} must have exactly four rows")
    parsed: list[list[Fraction]] = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != 4:
            fail(f"{name}[{i}] must have exactly four entries")
        parsed_row: list[Fraction] = []
        for j, entry in enumerate(row):
            if not isinstance(entry, str):
                fail(f"{name}[{i}][{j}] must be a rational string")
            try:
                value = Fraction(entry)
            except (ValueError, ZeroDivisionError) as exc:
                fail(f"invalid rational at {name}[{i}][{j}]: {exc}")
            parsed_row.append(value)
        parsed.append(parsed_row)
    return parsed


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        fail("determinant received a nonsquare matrix")
    total = Fraction(0)
    for permutation in itertools.permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(n)
            for j in range(i + 1, n)
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += term
    return total


def minor(
    matrix: list[list[Fraction]], rows: tuple[int, ...], cols: tuple[int, ...]
) -> Fraction:
    return determinant([[matrix[i][j] for j in cols] for i in rows])


def verify_rank_two(matrix: list[list[Fraction]], name: str) -> tuple[int, int]:
    three_by_three = [
        minor(matrix, rows, cols)
        for rows in itertools.combinations(range(4), 3)
        for cols in itertools.combinations(range(4), 3)
    ]
    if any(value != 0 for value in three_by_three):
        fail(f"{name} has a nonzero 3-by-3 minor")
    two_by_two = [
        minor(matrix, rows, cols)
        for rows in itertools.combinations(range(4), 2)
        for cols in itertools.combinations(range(4), 2)
    ]
    nonzero = [value for value in two_by_two if value != 0]
    if not nonzero:
        fail(f"{name} has no nonzero 2-by-2 minor")
    return len(three_by_three), len(nonzero)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: builder_verify_counterexample.py CERTIFICATE.json")
    input_path = Path(sys.argv[1])
    raw_bytes = input_path.read_bytes()
    try:
        payload = json.loads(raw_bytes)
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")
    if not isinstance(payload, dict):
        fail("certificate root must be an object")
    for required in ("schema", "field", "M", "A", "B"):
        if required not in payload:
            fail(f"missing required key {required}")
    if payload["schema"] != "hadamard-rank-factorization-certificate-v1":
        fail("unsupported certificate schema")
    if payload["field"] != "Q":
        fail("this verifier accepts only certificates over Q")

    matrix_m = parse_matrix(payload["M"], "M")
    matrix_a = parse_matrix(payload["A"], "A")
    matrix_b = parse_matrix(payload["B"], "B")

    expected_m = [
        [Fraction(1), Fraction(1), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
    ]
    if matrix_m != expected_m:
        fail("serialized M is not the matrix in the problem statement")

    product = [
        [matrix_a[i][j] * matrix_b[i][j] for j in range(4)]
        for i in range(4)
    ]
    if product != matrix_m:
        fail("A Hadamard B does not equal M")

    a_minors, a_nonzero_two = verify_rank_two(matrix_a, "A")
    b_minors, b_nonzero_two = verify_rank_two(matrix_b, "B")
    det_m = determinant(matrix_m)
    if det_m == 0:
        fail("M is not full rank")

    input_sha = hashlib.sha256(raw_bytes).hexdigest()
    code_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("PASS exact rational Hadamard rank-(2,2) factorization")
    print(f"det(M)={det_m}")
    print(f"A: checked {a_minors} 3x3 minors; nonzero 2x2 minors={a_nonzero_two}")
    print(f"B: checked {b_minors} 3x3 minors; nonzero 2x2 minors={b_nonzero_two}")
    print(f"input_sha256={input_sha}")
    print(f"code_sha256={code_sha}")


if __name__ == "__main__":
    main()
