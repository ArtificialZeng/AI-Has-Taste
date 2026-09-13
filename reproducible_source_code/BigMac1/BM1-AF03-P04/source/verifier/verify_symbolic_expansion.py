#!/usr/bin/env python3
"""Second evaluator: expand the three commutators from the R terms themselves."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def expanded_terms(array: str, n: int):
    # Each R term is (first direct-sum component, second component, color).
    terms = [(j, i, array[i * n + j]) for i, j in itertools.product(range(n), repeat=2)]
    output: dict[tuple[tuple[int, int, int], str], tuple[str, str]] = {}
    for left, right in itertools.product(terms, repeat=2):
        p, q, c = left
        p2, q2, d = right
        if p == p2:
            key = ((p, q, q2), "12-13")
            require(key not in output, "duplicate [R12,R13] contribution")
            output[key] = (c, d)
        if q == p2:
            key = ((p, q, q2), "12-23")
            require(key not in output, "duplicate [R12,R23] contribution")
            output[key] = (c, d)
        if q == q2:
            key = ((p, p2, q), "13-23")
            require(key not in output, "duplicate [R13,R23] contribution")
            output[key] = (c, d)
    return output


def verify_array(array: str, n: int) -> None:
    actual = expanded_terms(array, n)
    require(len(actual) == 3 * n**3, "wrong number of expanded commutator terms")
    for j, i, k in itertools.product(range(n), repeat=3):
        c = array[i * n + j]
        middle = array[k * n + j]
        c_double_prime = array[k * n + i]
        require(actual[((j, i, k), "12-13")] == (c, middle), "first bracket mismatch")
        require(actual[((j, i, k), "12-23")] == (c, c_double_prime), "second bracket mismatch")
        require(actual[((j, i, k), "13-23")] == (middle, c_double_prime), "third bracket mismatch")
        require(middle in (c, c_double_prime), "not an admissible transitive-CYBE triple")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_symbolic_expansion.py CERTIFICATE.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        raw = path.read_bytes()
        data = json.loads(raw)
        values = data["n_values"]
        checked = 0
        for key in ("2", "3", "4", "5"):
            n = int(key)
            for array in values[key]["arrays"]:
                verify_array(array, n)
                checked += 1
        print(
            "SYMBOLIC_EXPANSION_VERIFIED "
            f"arrays={checked} input_sha256={hashlib.sha256(raw).hexdigest()} "
            f"verifier_sha256={hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}"
        )
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
