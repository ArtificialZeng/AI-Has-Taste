#!/usr/bin/env python3
"""Independent fail-closed verifier for t16_block_size_reduction.json."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


DEFAULT = Path(__file__).resolve().with_name("t16_block_size_reduction.json")


class VerificationError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def canonical(sequence: tuple[int, ...], m: int) -> tuple[int, ...]:
    return min(sequence, tuple(m - value for value in reversed(sequence)))


def verify(path: Path) -> dict[str, object]:
    raw_bytes = path.read_bytes()
    data = json.loads(raw_bytes)
    require(isinstance(data, dict), "root must be an object")
    required = {"schema", "scope", "rational_denominator", "term_lower_numerators", "canonical_type_counts", "enumeration", "limitation"}
    require(required.issubset(data), f"missing fields: {sorted(required - set(data))}")
    require(data["schema"] == "kusner.t16.cut-cardinality-reduction.v1", "schema mismatch")
    expected_scope = {
        "labels": 11,
        "positive_gap_total": 16,
        "deficit_budget": 6,
        "gap_count_patterns": [[5, 3, 3, 3, 2], [4, 4, 3, 3, 2], [4, 3, 3, 3, 3]],
        "coordinate_reflection_quotient": True,
        "equal_length_coordinate_permutation_quotient": True,
    }
    require(data["scope"] == expected_scope, "scope mismatch")
    denominator = data["rational_denominator"]
    require(type(denominator) is int and denominator == 10**9, "denominator mismatch")

    records = data["term_lower_numerators"]
    require(isinstance(records, list) and len(records) == 45, "term record count mismatch")
    terms: dict[tuple[int, int], int] = {}
    for index, record in enumerate(records):
        require(isinstance(record, dict) and set(record) == {"a", "b", "numerator"}, f"bad term record {index}")
        a, b, numerator = record["a"], record["b"], record["numerator"]
        require(type(a) is int and type(b) is int and 1 <= a < b <= 10, f"bad term pair {index}")
        require(type(numerator) is int and 0 <= numerator < 2 * denominator, f"bad numerator {index}")
        require((a, b) not in terms, f"duplicate term {(a, b)}")
        q = Fraction(a * (11 - b), b * (11 - a))
        t = Fraction(numerator, denominator)
        threshold = t / (2 - t)
        require(q > threshold * threshold, f"invalid strict term lower bound {(a, b)}")
        next_t = Fraction(numerator + 1, denominator)
        next_threshold = next_t / (2 - next_t)
        require(q <= next_threshold * next_threshold, f"term bound not maximal {(a, b)}")
        terms[a, b] = numerator
    require(set(terms) == set(itertools.combinations(range(1, 11), 2)), "term coverage mismatch")

    types: dict[int, list[tuple[int, ...]]] = {}
    costs: dict[int, list[int]] = {}
    for length in (2, 3, 4, 5):
        sequences = {canonical(sequence, 11) for sequence in itertools.combinations(range(1, 11), length)}
        scored = sorted((sum(terms[pair] for pair in zip(sequence, sequence[1:])), sequence) for sequence in sequences)
        costs[length] = [cost for cost, _ in scored]
        types[length] = [sequence for _, sequence in scored]
    expected_counts = {str(length): len(types[length]) for length in (2, 3, 4, 5)}
    require(expected_counts == {"2": 25, "3": 60, "4": 110, "5": 126}, "internal type counts mismatch")
    require(data["canonical_type_counts"] == expected_counts, "serialized type counts mismatch")

    combinations_by_length: dict[tuple[int, int], list[tuple[int, tuple[int, ...]]]] = {}
    for length, count in ((3, 2), (3, 3), (3, 4), (4, 2)):
        combinations_by_length[length, count] = sorted(
            (sum(costs[length][index] for index in indices), indices)
            for indices in itertools.combinations_with_replacement(range(len(types[length])), count)
        )

    survivors_a = []
    for cost3, indices3 in combinations_by_length[3, 3]:
        if cost3 + costs[5][0] + costs[2][0] >= 6 * denominator:
            break
        for index5, cost5 in enumerate(costs[5]):
            if cost3 + cost5 + costs[2][0] >= 6 * denominator:
                break
            for index2, cost2 in enumerate(costs[2]):
                if cost3 + cost5 + cost2 >= 6 * denominator:
                    break
                survivors_a.append({
                    "length5": list(types[5][index5]),
                    "length3": [list(types[3][index]) for index in indices3],
                    "length2": list(types[2][index2]),
                })

    survivors_b = []
    for cost4, indices4 in combinations_by_length[4, 2]:
        if cost4 + combinations_by_length[3, 2][0][0] + costs[2][0] >= 6 * denominator:
            break
        for cost3, indices3 in combinations_by_length[3, 2]:
            if cost4 + cost3 + costs[2][0] >= 6 * denominator:
                break
            for index2, cost2 in enumerate(costs[2]):
                if cost4 + cost3 + cost2 >= 6 * denominator:
                    break
                survivors_b.append({
                    "length4": [list(types[4][index]) for index in indices4],
                    "length3": [list(types[3][index]) for index in indices3],
                    "length2": list(types[2][index2]),
                })

    survivors_c = []
    for cost3, indices3 in combinations_by_length[3, 4]:
        if cost3 + costs[4][0] >= 6 * denominator:
            break
        for index4, cost4 in enumerate(costs[4]):
            if cost3 + cost4 >= 6 * denominator:
                break
            survivors_c.append({
                "length4": list(types[4][index4]),
                "length3": [list(types[3][index]) for index in indices3],
            })

    survivors = {"5,3,3,3,2": survivors_a, "4,4,3,3,2": survivors_b, "4,3,3,3,3": survivors_c}
    totals = {
        "5,3,3,3,2": len(types[5]) * math.comb(len(types[3]) + 2, 3) * len(types[2]),
        "4,4,3,3,2": math.comb(len(types[4]) + 1, 2) * math.comb(len(types[3]) + 1, 2) * len(types[2]),
        "4,3,3,3,3": len(types[4]) * math.comb(len(types[3]) + 3, 4),
    }
    enumeration = data["enumeration"]
    require(isinstance(enumeration, dict), "enumeration must be an object")
    require(enumeration.get("totals") == totals, "total table mismatch")
    require(enumeration.get("grand_total") == sum(totals.values()) == 463_959_900, "grand total mismatch")
    require(enumeration.get("survivors") == survivors, "survivor records mismatch")
    counts = {key: len(value) for key, value in survivors.items()}
    require(counts == {"5,3,3,3,2": 78, "4,4,3,3,2": 341, "4,3,3,3,3": 929}, "survivor count endpoint mismatch")
    require(enumeration.get("survivor_counts") == counts, "survivor count table mismatch")
    require(enumeration.get("grand_survivor_count") == sum(counts.values()) == 1348, "grand survivor count mismatch")

    return {
        "status": "PASS",
        "scope": "exact necessary cut-cardinality reduction at t=16; label incidences remain",
        "grand_total": sum(totals.values()),
        "survivor_counts": counts,
        "grand_survivor_count": sum(counts.values()),
        "input_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    try:
        result = verify(args.certificate.resolve())
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
