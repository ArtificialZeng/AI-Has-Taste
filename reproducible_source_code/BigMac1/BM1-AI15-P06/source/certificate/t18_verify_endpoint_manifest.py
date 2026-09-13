#!/usr/bin/env python3
"""Independent fail-closed verifier for the exact t=18 endpoint manifest."""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


CODE = Path(__file__).resolve()
PROJECT = CODE.parents[1]
DEFAULT = CODE.with_name("t18_endpoint_manifest.json")
GENERATOR = PROJECT / "experiments" / "t18_endpoint_enumerate.py"


class VerificationError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> NoReturn:
    fail(f"non-finite JSON constant: {value}")


def require_exact(actual: object, expected: object, path: str) -> None:
    require(type(actual) is type(expected), f"type mismatch at {path}")
    if isinstance(expected, dict):
        require(set(actual) == set(expected), f"field mismatch at {path}")
        for key in expected:
            require_exact(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(len(actual) == len(expected), f"length mismatch at {path}")
        for index, (actual_item, expected_item) in enumerate(zip(actual, expected)):
            require_exact(actual_item, expected_item, f"{path}[{index}]")
    else:
        require(actual == expected, f"value mismatch at {path}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(sequence: tuple[int, ...], m: int) -> tuple[int, ...]:
    return min(sequence, tuple(m - value for value in reversed(sequence)))


def category(sequence: tuple[int, ...], m: int) -> str:
    singleton_copies = int(sequence[0] == 1) + int(sequence[-1] == m - 1)
    return "R" if singleton_copies == 2 else ("O" if singleton_copies == 1 else "N")


def verify(path: Path) -> dict[str, object]:
    raw_bytes = path.read_bytes()
    data = json.loads(
        raw_bytes,
        object_pairs_hook=unique_object,
        parse_constant=reject_constant,
    )
    require(isinstance(data, dict), "root must be an object")
    required = {"schema", "scope", "rational_bound", "chain_bounds", "partition_enumeration", "endpoint_loss_enumeration", "limitation", "environment"}
    require(set(data) == required, "root fields mismatch")
    require(data["schema"] == "kusner.t18.endpoint-loss-manifest.v1", "schema mismatch")
    expected_scope = {
        "labels": 11,
        "dimension": 5,
        "positive_gap_total": 18,
        "deficit_budget": 8,
        "naimark_max_chain_length": 9,
        "endpoint_category_meaning": {
            "R": "two singleton endpoint cut copies",
            "O": "one singleton endpoint cut copy",
            "N": "no singleton endpoint cut copies",
        },
    }
    require_exact(data["scope"], expected_scope, "scope")
    require(GENERATOR.is_file(), "generator file missing")
    environment = data["environment"]
    require(isinstance(environment, dict), "environment must be an object")
    require(set(environment) == {"python", "platform", "generator_sha256"}, "environment fields mismatch")
    require(type(environment.get("python")) is str, "environment python must be a string")
    require(type(environment.get("platform")) is str, "environment platform must be a string")
    require(environment.get("generator_sha256") == digest(GENERATOR), "generator hash mismatch")

    expected_limitation = (
        "Exact finite deficit/cardinality/endpoint-category result at t=18 only. "
        "R10_not_excluded means only that endpoint penalties permit eight singleton copies; "
        "it is not an incidence-feasible cut decomposition or equilateral witness."
    )
    require_exact(data["limitation"], expected_limitation, "limitation")

    tree = ast.parse(CODE.read_text(encoding="utf-8"), filename=str(CODE))
    assert_nodes = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(assert_nodes == 0, f"optimization-removable assert nodes: {assert_nodes}")

    bound = data["rational_bound"]
    require(isinstance(bound, dict), "rational_bound must be an object")
    require(set(bound) == {"denominator", "formula", "term_lower_numerators", "strict_pruning_rule"}, "rational_bound fields mismatch")
    denominator = bound.get("denominator")
    require(type(denominator) is int and denominator == 10**9, "denominator mismatch")
    require(bound.get("formula") == "sum_adjacent 2*r/(1+r), r^2=a*(11-b)/(b*(11-a))", "formula mismatch")
    require(bound.get("strict_pruning_rule") == "prune when lower_numerator >= 8*denominator", "pruning rule mismatch")
    term_records = bound.get("term_lower_numerators")
    require(isinstance(term_records, list) and len(term_records) == 45, "term record count mismatch")
    terms: dict[tuple[int, int], int] = {}
    for index, record in enumerate(term_records):
        require(isinstance(record, dict) and set(record) == {"a", "b", "numerator"}, f"term fields mismatch at {index}")
        a, b, numerator = record["a"], record["b"], record["numerator"]
        require(type(a) is int and type(b) is int and 1 <= a < b <= 10, f"bad term pair at {index}")
        require(type(numerator) is int and 0 <= numerator < 2 * denominator, f"bad numerator at {index}")
        require((a, b) not in terms, f"duplicate term pair {(a, b)}")
        q = Fraction(a * (11 - b), b * (11 - a))
        t = Fraction(numerator, denominator)
        threshold = t / (2 - t)
        require(q > threshold * threshold, f"invalid strict term lower bound {(a, b)}")
        next_t = Fraction(numerator + 1, denominator)
        next_threshold = next_t / (2 - next_t)
        require(q <= next_threshold * next_threshold, f"term numerator not maximal {(a, b)}")
        terms[a, b] = numerator
    require(set(terms) == set(itertools.combinations(range(1, 11), 2)), "term-pair coverage mismatch")

    general_minima: dict[int, int] = {}
    category_minima: dict[int, dict[str, int]] = {}
    expected_chain_records = []
    for length in range(10):
        if length == 0:
            sequences = [()]
        elif length == 1:
            sequences = [(size,) for size in range(1, 6)]
        else:
            sequences = sorted({canonical(sequence, 11) for sequence in itertools.combinations(range(1, 11), length)})
        scored = [(sum(terms[pair] for pair in zip(sequence, sequence[1:])), sequence) for sequence in sequences]
        general_cost, general_sequence = min(scored)
        general_minima[length] = general_cost
        grouped: dict[str, list[tuple[int, tuple[int, ...]]]] = {"R": [], "O": [], "N": []}
        if length >= 2:
            for cost, sequence in scored:
                grouped[category(sequence, 11)].append((cost, sequence))
        category_record = {}
        category_minima[length] = {}
        for name in ("R", "O", "N"):
            values = grouped[name]
            if values:
                minimum_cost, minimizing_sequence = min(values)
                category_minima[length][name] = minimum_cost
                category_record[name] = {
                    "canonical_type_count": len(values),
                    "minimum_lower_numerator": minimum_cost,
                    "minimizing_cut_sizes": list(minimizing_sequence),
                    "singleton_endpoint_copies": {"R": 2, "O": 1, "N": 0}[name],
                }
            else:
                category_record[name] = None
        expected_chain_records.append({
            "length": length,
            "canonical_type_count": len(sequences),
            "general_minimum_lower_numerator": general_cost,
            "general_minimizing_cut_sizes": list(general_sequence),
            "endpoint_categories": category_record,
        })
    require_exact(data["chain_bounds"], expected_chain_records, "chain_bounds")
    require([record["canonical_type_count"] for record in expected_chain_records] == [1, 5, 25, 60, 110, 126, 110, 60, 25, 5], "canonical chain counts mismatch")

    partitions = [
        tuple(reversed(ascending))
        for ascending in itertools.combinations_with_replacement(range(10), 5)
        if sum(ascending) == 18
    ]
    partition_records = []
    survivors = []
    for partition in partitions:
        lower_numerator = sum(general_minima[length] for length in partition)
        survives = lower_numerator < 8 * denominator
        partition_records.append({"partition": list(partition), "minimum_lower_numerator": lower_numerator, "survives": survives})
        if survives:
            survivors.append(partition)
    partition_data = data["partition_enumeration"]
    require(isinstance(partition_data, dict), "partition enumeration must be an object")
    require(set(partition_data) == {"total", "records", "survivors"}, "partition enumeration fields mismatch")
    require(type(partition_data.get("total")) is int and partition_data.get("total") == len(partitions) == 88, "partition total mismatch")
    require_exact(partition_data.get("records"), partition_records, "partition_enumeration.records")
    expected_survivors = [
        (7, 3, 3, 3, 2),
        (6, 4, 3, 3, 2),
        (5, 5, 3, 3, 2),
        (5, 4, 4, 3, 2),
        (4, 4, 4, 4, 2),
        (6, 3, 3, 3, 3),
        (5, 4, 3, 3, 3),
        (4, 4, 4, 3, 3),
    ]
    require(survivors == expected_survivors, "partition survivor endpoint mismatch")
    require_exact(partition_data.get("survivors"), [list(partition) for partition in survivors], "partition_enumeration.survivors")

    endpoint_records = []
    r10_patterns = []
    rle9_patterns = []
    expected_compatible_counts = [1, 2, 2, 3, 7, 6, 12, 21]
    expected_minimum_singletons = [10, 9, 9, 9, 8, 9, 8, 8]
    for survivor_index, partition in enumerate(survivors):
        compatible_assignments = []
        for categories in itertools.product(("R", "O", "N"), repeat=5):
            if any(name not in category_minima[length] for length, name in zip(partition, categories)):
                continue
            lower_numerator = sum(category_minima[length][name] for length, name in zip(partition, categories))
            if lower_numerator >= 8 * denominator:
                continue
            singleton_copies = sum({"R": 2, "O": 1, "N": 0}[name] for name in categories)
            compatible_assignments.append({
                "categories": list(categories),
                "lower_numerator": lower_numerator,
                "singleton_endpoint_copies": singleton_copies,
                "non_singleton_copies_R": 18 - singleton_copies,
            })
        minimum_singletons = min(record["singleton_endpoint_copies"] for record in compatible_assignments)
        maximum_r = 18 - minimum_singletons
        require(len(compatible_assignments) == expected_compatible_counts[survivor_index], f"compatible assignment count mismatch for {partition}")
        require(minimum_singletons == expected_minimum_singletons[survivor_index], f"minimum singleton count mismatch for {partition}")
        require(maximum_r <= 10, f"endpoint penalties allow R>10 for {partition}")
        endpoint_records.append({
            "partition": list(partition),
            "assignments_checked": 243,
            "compatible_assignments": compatible_assignments,
            "compatible_assignment_count": len(compatible_assignments),
            "minimum_singleton_endpoint_copies": minimum_singletons,
            "maximum_non_singleton_copies_R": maximum_r,
            "endpoint_conclusion": "R10_not_excluded" if maximum_r == 10 else "R_le_9",
        })
        if maximum_r == 10:
            r10_patterns.append(list(partition))
        else:
            rle9_patterns.append(list(partition))

    expected_r10 = [[4, 4, 4, 4, 2], [5, 4, 3, 3, 3], [4, 4, 4, 3, 3]]
    expected_rle9 = [[7, 3, 3, 3, 2], [6, 4, 3, 3, 2], [5, 5, 3, 3, 2], [5, 4, 4, 3, 2], [6, 3, 3, 3, 3]]
    require(r10_patterns == expected_r10, "R=10 pattern classification mismatch")
    require(rle9_patterns == expected_rle9, "R<=9 pattern classification mismatch")
    endpoint_data = data["endpoint_loss_enumeration"]
    require(isinstance(endpoint_data, dict), "endpoint enumeration must be an object")
    require(set(endpoint_data) == {"records", "R10_not_excluded_patterns", "R_le_9_patterns"}, "endpoint enumeration fields mismatch")
    require_exact(endpoint_data.get("records"), endpoint_records, "endpoint_loss_enumeration.records")
    require_exact(endpoint_data.get("R10_not_excluded_patterns"), r10_patterns, "endpoint_loss_enumeration.R10_not_excluded_patterns")
    require_exact(endpoint_data.get("R_le_9_patterns"), rle9_patterns, "endpoint_loss_enumeration.R_le_9_patterns")

    return {
        "status": "PASS",
        "scope": "exact finite t=18 partition/cardinality/endpoint-loss enumeration; label incidences and R=10 remain open",
        "partitions": len(partitions),
        "partition_survivors": len(survivors),
        "endpoint_assignments_checked": len(survivors) * 243,
        "compatible_assignment_counts": expected_compatible_counts,
        "R10_not_excluded_patterns": r10_patterns,
        "R_le_9_patterns": rle9_patterns,
        "input_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "code_sha256": digest(CODE),
        "generator_sha256": digest(GENERATOR),
        "ast_assert_nodes": assert_nodes,
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
