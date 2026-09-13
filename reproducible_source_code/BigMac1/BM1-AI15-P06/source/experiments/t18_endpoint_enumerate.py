#!/usr/bin/env python3
"""Generate an exact finite t=18 partition and endpoint-loss manifest.

Floating point only seeds each rational term numerator.  Exact Fraction
comparisons move it to the unique maximal valid strict lower bound.  Every
partition and endpoint-category decision thereafter uses integer arithmetic.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path


M = 11
DIMENSION = 5
TOTAL_GAPS = 18
DEFICIT_BUDGET = 8
MAX_CHAIN = 9
DENOMINATOR = 10**9
OUTPUT = Path("certificate/t18_endpoint_manifest.json")


def qvalue(a: int, b: int) -> Fraction:
    return Fraction(a * (M - b), b * (M - a))


def valid_term_lower(a: int, b: int, numerator: int) -> bool:
    t = Fraction(numerator, DENOMINATOR)
    if not (0 <= t < 2):
        return False
    threshold = t / (2 - t)
    return qvalue(a, b) > threshold * threshold


def maximal_term_numerator(a: int, b: int) -> int:
    r = math.sqrt(float(qvalue(a, b)))
    numerator = int(2 * r / (1 + r) * DENOMINATOR)
    while not valid_term_lower(a, b, numerator):
        numerator -= 1
    while valid_term_lower(a, b, numerator + 1):
        numerator += 1
    return numerator


def reflect(sequence: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(M - value for value in reversed(sequence))


def canonical(sequence: tuple[int, ...]) -> tuple[int, ...]:
    return min(sequence, reflect(sequence))


def category(sequence: tuple[int, ...]) -> str:
    singleton_copies = int(sequence[0] == 1) + int(sequence[-1] == M - 1)
    return "R" if singleton_copies == 2 else ("O" if singleton_copies == 1 else "N")


def sorted_partitions() -> list[tuple[int, ...]]:
    return [
        tuple(reversed(ascending))
        for ascending in itertools.combinations_with_replacement(range(MAX_CHAIN + 1), DIMENSION)
        if sum(ascending) == TOTAL_GAPS
    ]


def main() -> int:
    terms = {
        (a, b): maximal_term_numerator(a, b)
        for a in range(1, M)
        for b in range(a + 1, M)
    }

    chain_records = []
    general_minima: dict[int, int] = {0: 0, 1: 0}
    category_minima: dict[int, dict[str, int]] = {}
    for length in range(MAX_CHAIN + 1):
        if length == 0:
            sequences = [()]
        elif length == 1:
            sequences = [(size,) for size in range(1, (M - 1) // 2 + 1)]
        else:
            sequences = sorted(
                {canonical(sequence) for sequence in itertools.combinations(range(1, M), length)}
            )
        scored = [
            (sum(terms[pair] for pair in zip(sequence, sequence[1:])), sequence)
            for sequence in sequences
        ]
        general_cost, general_sequence = min(scored)
        general_minima[length] = general_cost
        categories: dict[str, list[tuple[int, tuple[int, ...]]]] = {"R": [], "O": [], "N": []}
        if length >= 2:
            for cost, sequence in scored:
                categories[category(sequence)].append((cost, sequence))
        category_record = {}
        category_minima[length] = {}
        for name in ("R", "O", "N"):
            values = categories[name]
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
        chain_records.append(
            {
                "length": length,
                "canonical_type_count": len(sequences),
                "general_minimum_lower_numerator": general_cost,
                "general_minimizing_cut_sizes": list(general_sequence),
                "endpoint_categories": category_record,
            }
        )

    partition_records = []
    surviving_partitions = []
    for partition in sorted_partitions():
        lower_numerator = sum(general_minima[length] for length in partition)
        survives = lower_numerator < DEFICIT_BUDGET * DENOMINATOR
        partition_records.append(
            {
                "partition": list(partition),
                "minimum_lower_numerator": lower_numerator,
                "survives": survives,
            }
        )
        if survives:
            surviving_partitions.append(partition)

    endpoint_records = []
    r10_patterns = []
    rle9_patterns = []
    for partition in surviving_partitions:
        compatible_assignments = []
        for categories in itertools.product(("R", "O", "N"), repeat=DIMENSION):
            if any(name not in category_minima[length] for length, name in zip(partition, categories)):
                continue
            lower_numerator = sum(
                category_minima[length][name]
                for length, name in zip(partition, categories)
            )
            if lower_numerator >= DEFICIT_BUDGET * DENOMINATOR:
                continue
            singleton_copies = sum({"R": 2, "O": 1, "N": 0}[name] for name in categories)
            compatible_assignments.append(
                {
                    "categories": list(categories),
                    "lower_numerator": lower_numerator,
                    "singleton_endpoint_copies": singleton_copies,
                    "non_singleton_copies_R": TOTAL_GAPS - singleton_copies,
                }
            )
        minimum_singletons = min(record["singleton_endpoint_copies"] for record in compatible_assignments)
        maximum_r = TOTAL_GAPS - minimum_singletons
        record = {
            "partition": list(partition),
            "assignments_checked": 3**DIMENSION,
            "compatible_assignments": compatible_assignments,
            "compatible_assignment_count": len(compatible_assignments),
            "minimum_singleton_endpoint_copies": minimum_singletons,
            "maximum_non_singleton_copies_R": maximum_r,
            "endpoint_conclusion": "R10_not_excluded" if maximum_r == 10 else "R_le_9",
        }
        endpoint_records.append(record)
        if maximum_r == 10:
            r10_patterns.append(list(partition))
        else:
            rle9_patterns.append(list(partition))

    certificate = {
        "schema": "kusner.t18.endpoint-loss-manifest.v1",
        "scope": {
            "labels": M,
            "dimension": DIMENSION,
            "positive_gap_total": TOTAL_GAPS,
            "deficit_budget": DEFICIT_BUDGET,
            "naimark_max_chain_length": MAX_CHAIN,
            "endpoint_category_meaning": {
                "R": "two singleton endpoint cut copies",
                "O": "one singleton endpoint cut copy",
                "N": "no singleton endpoint cut copies",
            },
        },
        "rational_bound": {
            "denominator": DENOMINATOR,
            "formula": "sum_adjacent 2*r/(1+r), r^2=a*(11-b)/(b*(11-a))",
            "term_lower_numerators": [
                {"a": a, "b": b, "numerator": terms[a, b]}
                for a in range(1, M)
                for b in range(a + 1, M)
            ],
            "strict_pruning_rule": "prune when lower_numerator >= 8*denominator",
        },
        "chain_bounds": chain_records,
        "partition_enumeration": {
            "total": len(partition_records),
            "records": partition_records,
            "survivors": [list(partition) for partition in surviving_partitions],
        },
        "endpoint_loss_enumeration": {
            "records": endpoint_records,
            "R10_not_excluded_patterns": r10_patterns,
            "R_le_9_patterns": rle9_patterns,
        },
        "limitation": (
            "Exact finite deficit/cardinality/endpoint-category result at t=18 only. "
            "R10_not_excluded means only that endpoint penalties permit eight singleton copies; "
            "it is not an incidence-feasible cut decomposition or equilateral witness."
        ),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "GENERATED",
        "output": str(OUTPUT),
        "partitions": len(partition_records),
        "partition_survivors": len(surviving_partitions),
        "R10_not_excluded_patterns": r10_patterns,
        "R_le_9_patterns": rle9_patterns,
        "output_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
