#!/usr/bin/env python3
"""Fail-closed, standard-library verifier for the exact rational certificate."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


REQUIRED_KEYS = {
    "schema_version",
    "claim",
    "field",
    "fraction_encoding",
    "M",
    "U",
    "V",
    "X",
    "Y",
    "A",
    "B",
}


def die(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def parse_matrix(name: str, raw: object, rows: int, cols: int) -> list[list[Fraction]]:
    if not isinstance(raw, list) or len(raw) != rows:
        die(f"{name} must have {rows} rows")
    result: list[list[Fraction]] = []
    for i, row in enumerate(raw):
        if not isinstance(row, list) or len(row) != cols:
            die(f"{name}[{i}] must have {cols} entries")
        parsed_row: list[Fraction] = []
        for j, value in enumerate(row):
            if not isinstance(value, str):
                die(f"{name}[{i}][{j}] is not a string")
            try:
                parsed = Fraction(value)
            except (ValueError, ZeroDivisionError) as exc:
                die(f"invalid rational at {name}[{i}][{j}]: {exc}")
            if str(parsed) != value and not (parsed.denominator == 1 and value == str(parsed.numerator)):
                die(f"non-canonical rational at {name}[{i}][{j}]")
            parsed_row.append(parsed)
        result.append(parsed_row)
    return result


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if not left or not right or len(left[0]) != len(right):
        die("incompatible matrix product")
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def hadamard(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[x * y for x, y in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        die("determinant called on non-square matrix")
    total = Fraction(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = Fraction(-1 if inversions % 2 else 1)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def submatrix(matrix: list[list[Fraction]], rows: tuple[int, ...], cols: tuple[int, ...]) -> list[list[Fraction]]:
    return [[matrix[i][j] for j in cols] for i in rows]


def exact_rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    row = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        pivot_value = work[row][col]
        work[row] = [entry / pivot_value for entry in work[row]]
        for i in range(len(work)):
            if i != row and work[i][col]:
                multiplier = work[i][col]
                work[i] = [x - multiplier * y for x, y in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def verify_rank_two_twice(name: str, matrix: list[list[Fraction]]) -> None:
    rank = exact_rank(matrix)
    if rank != 2:
        die(f"{name} has exact Gaussian-elimination rank {rank}, not 2")
    three_minors = [
        determinant(submatrix(matrix, rows, cols))
        for rows in itertools.combinations(range(4), 3)
        for cols in itertools.combinations(range(4), 3)
    ]
    if any(three_minors):
        die(f"{name} has a nonzero 3x3 minor")
    two_minors = [
        determinant(submatrix(matrix, rows, cols))
        for rows in itertools.combinations(range(4), 2)
        for cols in itertools.combinations(range(4), 2)
    ]
    if not any(two_minors):
        die(f"{name} has no nonzero 2x2 minor")


def main() -> None:
    default_certificate = Path(__file__).resolve().parents[1] / "certificates" / "rational_decomposition.json"
    certificate_path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else default_certificate
    if len(sys.argv) > 2:
        die("usage: verify_rational_decomposition.py [certificate.json]")
    raw_bytes = certificate_path.read_bytes()
    try:
        data = json.loads(raw_bytes)
    except json.JSONDecodeError as exc:
        die(f"invalid JSON: {exc}")
    if not isinstance(data, dict) or set(data) != REQUIRED_KEYS:
        die("certificate keys are incomplete or contain unrecognized data")
    if data["schema_version"] != 1 or data["field"] != "Q":
        die("unsupported schema version or field")

    matrices = {
        "M": parse_matrix("M", data["M"], 4, 4),
        "U": parse_matrix("U", data["U"], 4, 2),
        "V": parse_matrix("V", data["V"], 2, 4),
        "X": parse_matrix("X", data["X"], 4, 2),
        "Y": parse_matrix("Y", data["Y"], 2, 4),
        "A": parse_matrix("A", data["A"], 4, 4),
        "B": parse_matrix("B", data["B"], 4, 4),
    }

    if matmul(matrices["U"], matrices["V"]) != matrices["A"]:
        die("A != U V")
    if matmul(matrices["X"], matrices["Y"]) != matrices["B"]:
        die("B != X Y")
    if hadamard(matrices["A"], matrices["B"]) != matrices["M"]:
        die("A o B != M")
    if determinant(matrices["M"]) != 1:
        die("det(M) != 1")
    verify_rank_two_twice("A", matrices["A"])
    verify_rank_two_twice("B", matrices["B"])

    record = {
        "status": "PASS",
        "field": "Q",
        "det_M": "1",
        "rank_A": 2,
        "rank_B": 2,
        "certificate_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0],
    }
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
