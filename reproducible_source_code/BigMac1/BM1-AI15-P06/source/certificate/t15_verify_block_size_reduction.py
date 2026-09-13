#!/usr/bin/env python3
"""Fail-closed independent verifier for the t=15 cut-size reduction."""

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


DEFAULT = Path(__file__).resolve().with_name("t15_block_size_reduction.json")


class VerificationError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def reflect(sequence: tuple[int, ...], m: int) -> tuple[int, ...]:
    return tuple(m - value for value in reversed(sequence))


def canonical(sequence: tuple[int, ...], m: int) -> tuple[int, ...]:
    return min(sequence, reflect(sequence, m))


def verify(path: Path) -> dict[str, object]:
    raw_bytes = path.read_bytes()
    data = json.loads(raw_bytes)
    require(isinstance(data, dict), "certificate root must be an object")
    required = {"schema", "scope", "bound", "canonical_chain_types", "enumeration", "limitation"}
    require(required.issubset(data), f"missing root fields: {sorted(required - set(data))}")
    require(data["schema"] == "kusner.t15.cut-cardinality-reduction.v1", "schema mismatch")
    scope = data["scope"]
    require(isinstance(scope, dict), "scope must be an object")
    require(scope.get("labels") == 11, "label endpoint mismatch")
    require(scope.get("positive_gap_total") == 15, "gap-total endpoint mismatch")
    require(scope.get("gap_count_patterns") == [[3, 3, 3, 3, 3], [4, 3, 3, 3, 2]], "pattern mismatch")
    require(scope.get("coordinate_reflection_quotient") is True, "reflection quotient missing")
    require(scope.get("equal_length_coordinate_permutation_quotient") is True, "coordinate quotient missing")
    m = 11

    bound = data["bound"]
    require(isinstance(bound, dict), "bound must be an object")
    denominator = bound.get("rational_denominator")
    require(type(denominator) is int and denominator == 10**9, "denominator mismatch")
    records = bound.get("term_lower_numerators")
    require(isinstance(records, list) and len(records) == 45, "term-bound record count mismatch")
    term_numerators: dict[tuple[int, int], int] = {}
    for index, record in enumerate(records):
        require(isinstance(record, dict), f"term record {index} must be an object")
        require(set(record) == {"a", "b", "numerator"}, f"term record {index} fields mismatch")
        a, b, numerator = record["a"], record["b"], record["numerator"]
        require(type(a) is int and type(b) is int and 1 <= a < b <= 10, f"bad cut-size pair at term {index}")
        require(type(numerator) is int and 0 <= numerator < 2 * denominator, f"bad numerator at term {index}")
        require((a, b) not in term_numerators, f"duplicate term pair {(a, b)}")
        q = Fraction(a * (m - b), b * (m - a))
        t = Fraction(numerator, denominator)
        threshold = t / (2 - t)
        require(q > threshold * threshold, f"numerator is not a strict lower bound for {(a, b)}")
        next_t = Fraction(numerator + 1, denominator)
        next_threshold = next_t / (2 - next_t)
        require(q <= next_threshold * next_threshold, f"numerator is not maximal for {(a, b)}")
        term_numerators[(a, b)] = numerator
    require(set(term_numerators) == set(itertools.combinations(range(1, 11), 2)), "term-pair coverage mismatch")

    types: dict[int, list[tuple[int, ...]]] = {}
    costs: dict[int, dict[tuple[int, ...], int]] = {}
    serialized_types = data["canonical_chain_types"]
    require(isinstance(serialized_types, dict), "canonical_chain_types must be an object")
    require(set(serialized_types) == {"2", "3", "4"}, "chain-length keys mismatch")
    for length in (2, 3, 4):
        generated = sorted(
            {canonical(sequence, m) for sequence in itertools.combinations(range(1, m), length)}
        )
        generated_costs = {
            sequence: sum(term_numerators[pair] for pair in zip(sequence, sequence[1:]))
            for sequence in generated
        }
        generated.sort(key=lambda sequence: (generated_costs[sequence], sequence))
        expected_records = [
            {"cut_sizes": list(sequence), "lower_numerator": generated_costs[sequence]}
            for sequence in generated
        ]
        require(serialized_types[str(length)] == expected_records, f"canonical type table mismatch for length {length}")
        types[length] = generated
        costs[length] = generated_costs
    require(tuple(len(types[length]) for length in (2, 3, 4)) == (25, 60, 110), "canonical type counts mismatch")

    balanced: list[list[list[int]]] = []
    for indices in itertools.combinations_with_replacement(range(len(types[3])), 5):
        lower_sum = sum(costs[3][types[3][index]] for index in indices)
        if lower_sum < 5 * denominator:
            balanced.append([list(types[3][index]) for index in indices])

    triples: list[tuple[int, tuple[int, int, int]]] = []
    for indices in itertools.combinations_with_replacement(range(len(types[3])), 3):
        lower_sum = sum(costs[3][types[3][index]] for index in indices)
        if lower_sum + costs[4][types[4][0]] + costs[2][types[2][0]] < 5 * denominator:
            triples.append((lower_sum, indices))
    mixed: list[dict[str, object]] = []
    for triple_cost, indices in triples:
        for sequence4 in types[4]:
            partial = triple_cost + costs[4][sequence4]
            if partial + costs[2][types[2][0]] >= 5 * denominator:
                break
            for sequence2 in types[2]:
                if partial + costs[2][sequence2] >= 5 * denominator:
                    break
                mixed.append(
                    {
                        "length4": list(sequence4),
                        "length3": [list(types[3][index]) for index in indices],
                        "length2": list(sequence2),
                    }
                )

    enumeration = data["enumeration"]
    require(isinstance(enumeration, dict), "enumeration must be an object")
    balanced_total = math.comb(len(types[3]) + 4, 5)
    mixed_total = len(types[4]) * math.comb(len(types[3]) + 2, 3) * len(types[2])
    require(enumeration.get("balanced_total_multisets") == balanced_total == 7_624_512, "balanced total mismatch")
    require(enumeration.get("mixed_total_multisets") == mixed_total == 104_005_000, "mixed total mismatch")
    require(enumeration.get("balanced_survivors") == balanced, "balanced survivor list mismatch")
    require(enumeration.get("mixed_survivors") == mixed, "mixed survivor list mismatch")
    require(len(balanced) == 40, "balanced survivor count mismatch")
    require(len(mixed) == 12, "mixed survivor count mismatch")

    return {
        "status": "PASS",
        "scope": "exact necessary cut-cardinality reduction at t=15; not label-incidence feasibility",
        "balanced_total": balanced_total,
        "balanced_survivors": len(balanced),
        "mixed_total": mixed_total,
        "mixed_survivors": len(mixed),
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
