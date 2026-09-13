#!/usr/bin/env python3
"""Independent fail-closed verifier for the exact t=16 partition reduction."""

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


DEFAULT = Path(__file__).resolve().with_name("t16_gap_partition_reduction.json")


class VerificationError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def canonical(sequence: tuple[int, ...], m: int) -> tuple[int, ...]:
    return min(sequence, tuple(m - value for value in reversed(sequence)))


def partitions(total: int, parts: int, maximum: int) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []

    def visit(remaining: int, slots: int, cap: int, prefix: tuple[int, ...]) -> None:
        if slots == 0:
            if remaining == 0:
                result.append(prefix)
            return
        for value in range(min(cap, maximum, remaining), -1, -1):
            visit(remaining - value, slots - 1, value, prefix + (value,))

    visit(total, parts, maximum, ())
    return result


def verify(path: Path) -> dict[str, object]:
    raw_bytes = path.read_bytes()
    data = json.loads(raw_bytes)
    require(isinstance(data, dict), "root must be an object")
    required = {"schema", "scope", "rational_denominator", "term_lower_numerators", "chain_minima", "partition_enumeration", "limitation"}
    require(required.issubset(data), f"missing fields: {sorted(required - set(data))}")
    require(data["schema"] == "kusner.t16.gap-partition-reduction.v1", "schema mismatch")
    scope = data["scope"]
    require(scope == {"labels": 11, "dimension": 5, "positive_gap_total": 16, "deficit_budget": 6, "naimark_max_chain_length": 7}, "scope mismatch")
    denominator = data["rational_denominator"]
    require(type(denominator) is int and denominator == 10**9, "denominator mismatch")

    serialized_terms = data["term_lower_numerators"]
    require(isinstance(serialized_terms, list) and len(serialized_terms) == 45, "term record count mismatch")
    terms: dict[tuple[int, int], int] = {}
    for index, record in enumerate(serialized_terms):
        require(isinstance(record, dict) and set(record) == {"a", "b", "numerator"}, f"bad term record {index}")
        a, b, numerator = record["a"], record["b"], record["numerator"]
        require(type(a) is int and type(b) is int and 1 <= a < b <= 10, f"bad term pair {index}")
        require(type(numerator) is int and 0 <= numerator < 2 * denominator, f"bad term numerator {index}")
        require((a, b) not in terms, f"duplicate term {(a, b)}")
        q = Fraction(a * (11 - b), b * (11 - a))
        t = Fraction(numerator, denominator)
        threshold = t / (2 - t)
        require(q > threshold * threshold, f"invalid strict term bound {(a, b)}")
        next_t = Fraction(numerator + 1, denominator)
        next_threshold = next_t / (2 - next_t)
        require(q <= next_threshold * next_threshold, f"term bound not maximal {(a, b)}")
        terms[(a, b)] = numerator
    require(set(terms) == set(itertools.combinations(range(1, 11), 2)), "term coverage mismatch")

    minima: dict[int, tuple[int, tuple[int, ...]]] = {0: (0, ()), 1: (0, (1,))}
    counts = {0: 1, 1: 1}
    for length in range(2, 8):
        sequences = sorted({canonical(sequence, 11) for sequence in itertools.combinations(range(1, 11), length)})
        scored = [(sum(terms[pair] for pair in zip(sequence, sequence[1:])), sequence) for sequence in sequences]
        minima[length] = min(scored)
        counts[length] = len(sequences)
    expected_minima = [
        {
            "length": length,
            "canonical_type_count": counts[length],
            "minimum_lower_numerator": minima[length][0],
            "minimizing_cut_sizes": list(minima[length][1]),
        }
        for length in range(8)
    ]
    require(data["chain_minima"] == expected_minima, "chain-minimum table mismatch")

    records = []
    survivors = []
    for partition in partitions(16, 5, 7):
        lower_numerator = sum(minima[length][0] for length in partition)
        survives = lower_numerator < 6 * denominator
        records.append({"gap_partition": list(partition), "minimum_lower_numerator": lower_numerator, "survives": survives})
        if survives:
            survivors.append(list(partition))
    enumeration = data["partition_enumeration"]
    require(isinstance(enumeration, dict), "partition_enumeration must be an object")
    require(enumeration.get("total") == len(records) == 48, "partition total mismatch")
    require(enumeration.get("records") == records, "partition record mismatch")
    require(enumeration.get("survivors") == survivors, "survivor list mismatch")
    require(survivors == [[5, 3, 3, 3, 2], [4, 4, 3, 3, 2], [4, 3, 3, 3, 3]], "survivor endpoint mismatch")

    return {
        "status": "PASS",
        "scope": "exact necessary gap-count reduction at t=16",
        "partitions": len(records),
        "survivors": survivors,
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
