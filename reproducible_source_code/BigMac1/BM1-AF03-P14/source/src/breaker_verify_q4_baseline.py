#!/usr/bin/env python3
"""Standard-library exact verifier for the known Q4 (2,2,1,1) saddle."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def reject(message: str) -> "None":
    raise SystemExit("REJECT: " + message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            reject(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        reject(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def mat_vec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def main() -> None:
    if len(sys.argv) != 2:
        reject("usage: breaker_verify_q4_baseline.py CERTIFICATE.json")
    path = Path(sys.argv[1])
    try:
        raw = path.read_bytes()
        data = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except (OSError, json.JSONDecodeError):
        reject("unreadable certificate")
    reject_booleans(data)
    expected = {
        "schema": "q4-rational-saddle-v1",
        "unnormalized_vector": ["1", "1", "1/2", "1/2"],
        "expected_active_sign_vectors": 6,
        "expected_wall_sign_vectors": 4,
        "expected_tangent_signature": {"positive": 1, "negative": 2, "zero": 0},
    }
    if data != expected:
        reject("schema or claimed exact data mismatch")
    a = [Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2)]
    G = Fraction(0)
    grad_G = [Fraction(0) for _ in range(4)]
    hess_G = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    active = walls = 0
    for eps in itertools.product((-1, 1), repeat=4):
        linear = sum((Fraction(eps[i], 2) * a[i] for i in range(4)), Fraction(0))
        if linear == 0:
            walls += 1
        if linear <= 0:
            continue
        active += 1
        coeff = -1 if sum(e == -1 for e in eps) % 2 else 1
        G += coeff * linear**3
        for i in range(4):
            li = Fraction(eps[i], 2)
            grad_G[i] += coeff * 3 * linear**2 * li
            for j in range(4):
                hess_G[i][j] += coeff * 6 * linear * li * Fraction(eps[j], 2)
    if (active, walls, G) != (6, 4, Fraction(5, 4)):
        reject("box-spline chamber reconstruction failed")
    r2 = dot(a, a)
    q = [a[i] / r2 + grad_G[i] / G - 1 / a[i] for i in range(4)]
    if any(q):
        reject("candidate is not stationary")
    H = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            delta = Fraction(i == j)
            H[i][j] = (
                delta / r2
                - 2 * a[i] * a[j] / r2**2
                + hess_G[i][j] / G
                - grad_G[i] * grad_G[j] / G**2
                + delta / a[i] ** 2
            )
    vectors = [
        [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(-1)],
        [Fraction(1, 2), Fraction(1, 2), Fraction(-1), Fraction(-1)],
    ]
    if any(dot(a, vector) for vector in vectors):
        reject("basis is not tangent")
    values = [dot(vector, mat_vec(H, vector)) / dot(vector, vector) for vector in vectors]
    if values != [Fraction(-1), Fraction(-2, 5), Fraction(1, 5)]:
        reject("unexpected Hessian eigenvalues")
    print(
        json.dumps(
            {
                "status": "ACCEPT",
                "claim": "Q4 direction (2,2,1,1) is an exact saddle",
                "log_hessian_eigenvalues": [str(value) for value in values],
                "certificate_sha256": hashlib.sha256(raw).hexdigest(),
                "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
