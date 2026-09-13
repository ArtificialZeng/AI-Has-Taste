#!/usr/bin/env python3
"""Independent exact verifier for breaker_decomposition.json.

Only Python's standard library is used.  The verifier parses the serialized
rational data, reconstructs both advertised rank factorizations, verifies the
Hadamard product, and independently recomputes ranks/minors/determinants.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


EXPECTED_KEYS = {
    "schema",
    "statement",
    "M",
    "A",
    "B",
    "rank_factorizations",
}
EXPECTED_STATEMENT = (
    "A and B are rational 4 by 4 matrices with A o B = M and rank(A)=rank(B)=2."
)
EXPECTED_TARGET = [
    [Fraction(1), Fraction(1), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(1), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def parse_matrix(value: object, rows: int, cols: int, name: str) -> list[list[Fraction]]:
    if not isinstance(value, list) or len(value) != rows:
        fail(f"{name} must have exactly {rows} rows")
    result: list[list[Fraction]] = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != cols:
            fail(f"{name}[{i}] must have exactly {cols} entries")
        parsed_row: list[Fraction] = []
        for j, entry in enumerate(row):
            if not isinstance(entry, str):
                fail(f"{name}[{i}][{j}] must be a rational string")
            try:
                parsed_row.append(Fraction(entry))
            except (ValueError, ZeroDivisionError) as exc:
                fail(f"invalid rational at {name}[{i}][{j}]: {exc}")
        result.append(parsed_row)
    return result


def matmul_transpose(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    if not left or not right or len(left[0]) != len(right[0]):
        fail("incompatible rank-factor dimensions")
    width = len(left[0])
    if any(len(row) != width for row in left) or any(len(row) != width for row in right):
        fail("ragged rank factor")
    return [
        [sum((left[i][k] * right[j][k] for k in range(width)), Fraction(0)) for j in range(len(right))]
        for i in range(len(left))
    ]


def determinant_permutations(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    """Leibniz determinant, deliberately independent of row reduction."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        fail("determinant requested for a non-square matrix")
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


def exact_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    """Exact Gaussian rank over Q."""
    work = [list(row) for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                multiple = work[r][col]
                work[r] = [
                    work[r][c] - multiple * work[pivot_row][c] for c in range(cols)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def minors(matrix: Sequence[Sequence[Fraction]], order: int) -> Iterable[Fraction]:
    for row_indices in itertools.combinations(range(len(matrix)), order):
        for col_indices in itertools.combinations(range(len(matrix[0])), order):
            submatrix = [[matrix[i][j] for j in col_indices] for i in row_indices]
            yield determinant_permutations(submatrix)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("breaker_decomposition.json"),
    )
    args = parser.parse_args()
    certificate_path = args.certificate.resolve()
    try:
        payload = json.loads(
            certificate_path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        fail(f"cannot parse certificate: {exc}")
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        fail("certificate has missing or unexpected top-level keys")
    if payload["schema"] != "hadamard-rank22-rational-certificate-v1":
        fail("unrecognized schema")
    if payload["statement"] != EXPECTED_STATEMENT:
        fail("certificate statement does not match the expected endpoint")

    matrix_m = parse_matrix(payload["M"], 4, 4, "M")
    matrix_a = parse_matrix(payload["A"], 4, 4, "A")
    matrix_b = parse_matrix(payload["B"], 4, 4, "B")
    if matrix_m != EXPECTED_TARGET:
        fail("serialized M is not the designated target matrix")

    rank_data = payload["rank_factorizations"]
    if not isinstance(rank_data, dict) or set(rank_data) != {"A_equals_U_Vt", "B_equals_S_Tt"}:
        fail("rank_factorizations has the wrong keys")
    factor_a = rank_data["A_equals_U_Vt"]
    factor_b = rank_data["B_equals_S_Tt"]
    if not isinstance(factor_a, dict) or set(factor_a) != {"U", "V"}:
        fail("A rank factorization is malformed")
    if not isinstance(factor_b, dict) or set(factor_b) != {"S", "T"}:
        fail("B rank factorization is malformed")
    matrix_u = parse_matrix(factor_a["U"], 4, 2, "U")
    matrix_v = parse_matrix(factor_a["V"], 4, 2, "V")
    matrix_s = parse_matrix(factor_b["S"], 4, 2, "S")
    matrix_t = parse_matrix(factor_b["T"], 4, 2, "T")

    if matmul_transpose(matrix_u, matrix_v) != matrix_a:
        fail("U V^T does not reconstruct A")
    if matmul_transpose(matrix_s, matrix_t) != matrix_b:
        fail("S T^T does not reconstruct B")
    hadamard = [
        [matrix_a[i][j] * matrix_b[i][j] for j in range(4)] for i in range(4)
    ]
    if hadamard != matrix_m:
        fail("A o B does not equal M")

    rank_a = exact_rank(matrix_a)
    rank_b = exact_rank(matrix_b)
    rank_m = exact_rank(matrix_m)
    if (rank_a, rank_b, rank_m) != (2, 2, 4):
        fail(f"unexpected ranks {(rank_a, rank_b, rank_m)}")
    if any(minors(matrix_a, 3)) or any(minors(matrix_b, 3)):
        fail("a 3 by 3 minor of A or B is nonzero")
    if not any(minors(matrix_a, 2)) or not any(minors(matrix_b, 2)):
        fail("exact rank two was not witnessed by a 2 by 2 minor")
    det_m = determinant_permutations(matrix_m)
    if det_m != 1:
        fail(f"target determinant should be 1, got {det_m}")

    code_path = Path(__file__).resolve()
    print("PASS exact rational Hadamard rank-(2,2) decomposition")
    print(f"ranks A,B,M = {rank_a},{rank_b},{rank_m}; det(M) = {det_m}")
    print(f"certificate_sha256={digest(certificate_path)}")
    print(f"verifier_sha256={digest(code_path)}")


if __name__ == "__main__":
    main()
