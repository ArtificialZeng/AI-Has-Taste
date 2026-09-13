#!/usr/bin/env python3
"""Fail-closed comparison of a rebuilt cap-347 result with the frozen record."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


DETERMINISTIC_KEYS = (
    "cap",
    "largest_prime_in_universe",
    "odd_prime_count",
    "compatible_pairs",
    "incompatible_pairs",
    "selection_attempts",
    "upper_bound_prunes",
    "surviving_nodes",
    "visited_by_cardinality",
    "ratio_eligible_sets",
    "ratio_eligible_by_cardinality",
    "two_adic_pass",
    "two_adic_pass_by_cardinality",
    "two_adic_survivors",
    "korselt_lcm_pass",
    "korselt_lcm_pass_by_cardinality",
    "exact_divisibility_pass",
    "solutions",
    "candidate_stream_sha256",
    "search_code_sha256",
)

FROZEN_ENDPOINT = {
    "cap": 347,
    "largest_prime_in_universe": 347,
    "odd_prime_count": 68,
    "compatible_pairs": 2183,
    "incompatible_pairs": 95,
    "selection_attempts": 27_179_711,
    "upper_bound_prunes": 5_457_679,
    "surviving_nodes": 21_722_032,
    "ratio_eligible_sets": 17_803_010,
    "two_adic_pass": 38,
    "korselt_lcm_pass": 0,
    "exact_divisibility_pass": 0,
    "solutions": [],
    "candidate_stream_sha256": (
        "aefd032694eeb999a94642dbdc37965d122a07e30b33819168759d18d5fc0023"
    ),
    "search_code_sha256": (
        "cc236e3aa47e2b1aeb7c6afb6cc9ae787cfe5fec3da7f8c2cadb5eb1d4eacb8d"
    ),
}


def load_object(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"FAIL: cannot parse {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"FAIL: {path} does not contain a JSON object")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("frozen", type=Path)
    parser.add_argument("rebuilt", type=Path)
    args = parser.parse_args()

    frozen = load_object(args.frozen)
    rebuilt = load_object(args.rebuilt)

    errors: list[str] = []
    for label, record in (("frozen", frozen), ("rebuilt", rebuilt)):
        if record.get("schema") != "lehmer-prime-set-search-v1":
            errors.append(f"{label}: unexpected schema")
        if record.get("arithmetic") != (
            "exact Python integers; no floating-point search decisions"
        ):
            errors.append(f"{label}: unexpected arithmetic declaration")
        for key, expected in FROZEN_ENDPOINT.items():
            if record.get(key) != expected:
                errors.append(
                    f"{label}: {key}={record.get(key)!r}, expected {expected!r}"
                )

    for key in DETERMINISTIC_KEYS:
        if key not in frozen or key not in rebuilt:
            errors.append(f"missing deterministic key: {key}")
        elif frozen[key] != rebuilt[key]:
            errors.append(f"deterministic mismatch: {key}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)

    print("FROZEN COMPARISON: PASS")
    print(f"selection_attempts: {rebuilt['selection_attempts']}")
    print(f"ratio_eligible_sets: {rebuilt['ratio_eligible_sets']}")
    print(f"two_adic_pass: {rebuilt['two_adic_pass']}")
    print(f"korselt_lcm_pass: {rebuilt['korselt_lcm_pass']}")
    print(f"exact_divisibility_pass: {rebuilt['exact_divisibility_pass']}")


if __name__ == "__main__":
    main()
