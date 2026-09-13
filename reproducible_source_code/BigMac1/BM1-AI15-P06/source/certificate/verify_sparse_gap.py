#!/usr/bin/env python3
"""Fail-closed exact-arithmetic checker for the sparse-gap certificate.

This program checks the serialized scope and the finite arithmetic core used
by the human proof.  It deliberately does not claim to machine-check the
rank-one Parseval/Naimark argument in ``proof/structural_reduction.md``.
Every decisive condition is an ordinary branch that remains active under
``python -O``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "certificate" / "sparse_gap_claim.json"
CODE = Path(__file__).resolve()


class VerificationError(Exception):
    """A malformed input or failed mathematical check."""


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(input_path: Path) -> dict[str, object]:
    raw = input_path.read_bytes()
    data = json.loads(raw)
    required_fields = {
        "schema_version",
        "claim",
        "m",
        "d",
        "rank_lower_bound",
        "excluded_positive_gap_counts",
        "arithmetic_identity",
        "proof_file",
    }
    require(isinstance(data, dict), "certificate root must be an object")
    missing = sorted(required_fields - set(data))
    require(not missing, f"missing required fields: {missing}")
    require(data["schema_version"] == 1, "schema_version must equal 1")
    require(
        data["claim"]
        == "For m=11 and d=5, an equilateral l1 configuration has at least 12 positive consecutive coordinate gaps.",
        "unexpected claim endpoint",
    )
    require(
        data["arithmetic_identity"]
        == "<H1_C,H1_D> = |C intersect D| - |C||D|/m",
        "unexpected arithmetic identity",
    )
    require(data["proof_file"] == "proof/structural_reduction.md", "unexpected proof binding")

    m = data["m"]
    d = data["d"]
    require(type(m) is int and type(d) is int, "m and d must be integers")
    require(m == 11, f"m must equal 11, got {m!r}")
    require(d == 5, f"d must equal 5, got {d!r}")
    require(data["rank_lower_bound"] == m - 1 == 10, "rank lower bound mismatch")
    require(
        data["excluded_positive_gap_counts"] == [m - 1, m],
        "excluded gap-count list mismatch",
    )

    checked_types = 0
    for a in range(1, m):
        for b in range(1, m):
            lo = max(0, a + b - m)
            hi = min(a, b)
            for c in range(lo, hi + 1):
                inner = Fraction(c, 1) - Fraction(a * b, m)
                require(inner != 0, f"orthogonal cut type found: a={a}, b={b}, c={c}")
                checked_types += 1

    checked_nested = 0
    for a in range(1, m):
        for b in range(a, m):
            inner = Fraction(a * (m - b), m)
            require(inner > 0, f"nested cut inner product is not positive: a={a}, b={b}")
            checked_nested += 1

    q = m
    require(2 * d < q, "five-chain pigeonhole contradiction is absent")
    certified_minimum = q + 1
    require(certified_minimum == 12, "certified gap endpoint mismatch")

    return {
        "status": "PASS",
        "scope": "finite arithmetic core; human Parseval/Naimark implication not machine-checked",
        "m": m,
        "d": d,
        "cut_intersection_types_checked": checked_types,
        "nested_types_checked": checked_nested,
        "certified_minimum_positive_gaps": certified_minimum,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "code_sha256": sha256(CODE),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    try:
        result = verify(args.certificate.resolve())
    except Exception as exc:
        print(
            json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
