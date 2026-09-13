#!/usr/bin/env python3
"""Fail-closed independent verifier for an Abs(D_n) orbit-flow certificate.

The verifier does not import the construction program.  It rebuilds the full
set of B_n signed-cycle types and their class/rank data, realizes every claimed
flow edge by multiplying a canonical signed permutation by all D_n reflections,
and checks all normalized-flow equations with ``fractions.Fraction``.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Tuple


CycleType = Tuple[Tuple[int, ...], Tuple[int, ...]]


class VerificationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def exact_int(value: Any, label: str) -> int:
    require(type(value) is int, f"{label} must be a JSON integer")
    return value


def partitions(n: int, maximum: int | None = None) -> Iterable[Tuple[int, ...]]:
    if n == 0:
        yield ()
        return

    top = n if maximum is None else min(n, maximum)
    for first in range(top, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def all_types(n: int) -> set[CycleType]:
    result: set[CycleType] = set()
    for negative_weight in range(n + 1):
        for positive in partitions(n - negative_weight):
            for negative in partitions(negative_weight):
                if not len(negative) % 2:
                    result.add((positive, negative))
    return result


def key(value: CycleType) -> str:
    positive, negative = value
    p = ",".join(str(x) for x in positive) or "-"
    q = ",".join(str(x) for x in negative) or "-"
    return f"P[{p}]N[{q}]"


def z(partition: Tuple[int, ...]) -> int:
    result = 1
    for part, multiplicity in Counter(partition).items():
        result *= part**multiplicity * math.factorial(multiplicity)
    return result


def class_size(n: int, value: CycleType) -> int:
    positive, negative = value
    numerator = 2**n * math.factorial(n)
    denominator = 2 ** (len(positive) + len(negative)) * z(positive) * z(negative)
    require(numerator % denominator == 0, "centralizer order does not divide |B_n|")
    return numerator // denominator


def absolute_rank(n: int, value: CycleType) -> int:
    return n - len(value[0])


def canonical_signed_permutation(value: CycleType) -> Tuple[int, ...]:
    """Build a signed permutation having exactly the requested cycle type."""
    positive, negative = value
    output: list[int | None] = [None] * (sum(positive) + sum(negative))
    first = 1
    for is_negative, lengths in ((False, positive), (True, negative)):
        for length in lengths:
            labels = list(range(first, first + length))
            for source, target in zip(labels, labels[1:] + labels[:1]):
                output[source - 1] = target
            if is_negative:
                output[labels[-1] - 1] = -labels[0]
            first += length
    require(all(x is not None for x in output), "canonical representative incomplete")
    return tuple(int(x) for x in output)


def signed_cycle_type(element: Tuple[int, ...]) -> CycleType:
    n = len(element)
    visited = [False] * n
    positive: list[int] = []
    negative: list[int] = []
    for start in range(n):
        if visited[start]:
            continue
        current = start
        cycle_sign = 1
        length = 0
        while not visited[current]:
            visited[current] = True
            image = element[current]
            cycle_sign *= 1 if image > 0 else -1
            current = abs(image) - 1
            length += 1
        (positive if cycle_sign == 1 else negative).append(length)
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def reflections(n: int) -> Iterable[Tuple[int, ...]]:
    for left in range(n):
        for right in range(left + 1, n):
            for sign in (1, -1):
                reflection = list(range(1, n + 1))
                reflection[left] = sign * (right + 1)
                reflection[right] = sign * (left + 1)
                yield tuple(reflection)


def apply(element: Tuple[int, ...], signed_label: int) -> int:
    image = element[abs(signed_label) - 1]
    return image if signed_label > 0 else -image


def right_multiply(
    element: Tuple[int, ...], reflection: Tuple[int, ...]
) -> Tuple[int, ...]:
    return tuple(apply(element, image) for image in reflection)


def actual_upper_type_counts(n: int, source: CycleType) -> dict[CycleType, int]:
    representative = canonical_signed_permutation(source)
    source_rank = absolute_rank(n, source)
    result: Counter[CycleType] = Counter()
    for reflection in reflections(n):
        target = signed_cycle_type(right_multiply(representative, reflection))
        if absolute_rank(n, target) == source_rank + 1:
            result[target] += 1
    return dict(result)


def parse_type_record(n: int, record: Any, index: int) -> CycleType:
    require(type(record) is dict, f"types[{index}] must be an object")
    require(
        set(record) == {"key", "positive", "negative", "rank", "class_size"},
        f"types[{index}] has missing or unknown fields",
    )
    for label in ("positive", "negative"):
        require(type(record[label]) is list, f"types[{index}].{label} must be a list")
        require(
            all(type(x) is int and x > 0 for x in record[label]),
            f"types[{index}].{label} must contain positive integers",
        )
        require(
            record[label] == sorted(record[label], reverse=True),
            f"types[{index}].{label} is not a partition in canonical order",
        )
    value = tuple(record["positive"]), tuple(record["negative"])
    require(sum(value[0]) + sum(value[1]) == n, f"types[{index}] has wrong total size")
    require(len(value[1]) % 2 == 0, f"types[{index}] is not contained in D_n")
    require(record["key"] == key(value), f"types[{index}] has a noncanonical key")
    require(exact_int(record["rank"], f"types[{index}].rank") == absolute_rank(n, value), "bad rank")
    require(
        exact_int(record["class_size"], f"types[{index}].class_size") == class_size(n, value),
        f"types[{index}] has bad class size",
    )
    return value


def verify(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        data = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"invalid JSON: {exc}") from exc
    require(type(data) is dict, "top level must be an object")
    require(
        set(data)
        == {
            "schema",
            "n",
            "group_order",
            "orbit_count",
            "rank_sizes",
            "all_rank_pairs_feasible",
            "types",
            "rank_pairs",
        },
        "top level has missing or unknown fields",
    )
    require(data["schema"] == "abs-dn-bn-orbit-flow-v1", "unknown schema")
    n = exact_int(data["n"], "n")
    require(n >= 4, "certificate endpoint requires n >= 4")
    require(
        exact_int(data["group_order"], "group_order") == 2 ** (n - 1) * math.factorial(n),
        "wrong D_n order",
    )
    require(type(data["types"]) is list, "types must be a list")
    parsed_types = [parse_type_record(n, record, i) for i, record in enumerate(data["types"])]
    require(len(set(parsed_types)) == len(parsed_types), "duplicate type record")
    expected_types = all_types(n)
    require(set(parsed_types) == expected_types, "type list is not exhaustive")
    require(exact_int(data["orbit_count"], "orbit_count") == len(expected_types), "bad orbit count")

    size_by_key = {key(value): class_size(n, value) for value in expected_types}
    type_by_key = {key(value): value for value in expected_types}
    rank_sizes = [0] * (n + 1)
    for value in expected_types:
        rank_sizes[absolute_rank(n, value)] += class_size(n, value)
    require(type(data["rank_sizes"]) is list, "rank_sizes must be a list")
    require(
        all(type(x) is int for x in data["rank_sizes"]) and data["rank_sizes"] == rank_sizes,
        "rank sizes do not match the reconstructed orbit data",
    )
    require(sum(rank_sizes) == 2 ** (n - 1) * math.factorial(n), "rank sizes do not sum to |D_n|")

    require(data["all_rank_pairs_feasible"] is True, "certificate does not claim all pairs feasible")
    require(type(data["rank_pairs"]) is list, "rank_pairs must be a list")
    require(len(data["rank_pairs"]) == n, "must have exactly n adjacent rank pairs")
    seen_pairs: set[Tuple[int, int]] = set()
    verified_edges = 0
    cached_upper: dict[CycleType, dict[CycleType, int]] = {}
    allowed_pair_fields = {
        "lower_rank",
        "upper_rank",
        "scale",
        "max_flow",
        "feasible",
        "edge_count",
        "nonzero_flow_count",
        "flows",
    }
    for pair_index, pair in enumerate(data["rank_pairs"]):
        require(type(pair) is dict and set(pair) == allowed_pair_fields, f"bad rank_pairs[{pair_index}]")
        lower_rank = exact_int(pair["lower_rank"], f"rank_pairs[{pair_index}].lower_rank")
        upper_rank = exact_int(pair["upper_rank"], f"rank_pairs[{pair_index}].upper_rank")
        require(0 <= lower_rank < n and upper_rank == lower_rank + 1, "bad adjacent ranks")
        require((lower_rank, upper_rank) not in seen_pairs, "duplicate adjacent rank pair")
        seen_pairs.add((lower_rank, upper_rank))
        require(pair["feasible"] is True, "rank-pair feasibility flag is false")
        scale = exact_int(pair["scale"], f"rank_pairs[{pair_index}].scale")
        max_flow = exact_int(pair["max_flow"], f"rank_pairs[{pair_index}].max_flow")
        require(
            scale == math.lcm(rank_sizes[lower_rank], rank_sizes[upper_rank])
            and max_flow == scale,
            "discovery max-flow metadata is inconsistent",
        )
        require(type(pair["flows"]) is list, "flows must be a list")
        require(
            exact_int(pair["nonzero_flow_count"], "nonzero_flow_count") == len(pair["flows"]),
            "nonzero flow count is inconsistent",
        )

        row_sums: defaultdict[str, Fraction] = defaultdict(Fraction)
        column_sums: defaultdict[str, Fraction] = defaultdict(Fraction)
        lifted_row_sums: defaultdict[str, Fraction] = defaultdict(Fraction)
        lifted_column_sums: defaultdict[str, Fraction] = defaultdict(Fraction)
        seen_edges: set[Tuple[str, str]] = set()
        for flow_index, flow in enumerate(pair["flows"]):
            require(
                type(flow) is dict
                and set(flow) == {"lower", "upper", "numerator", "denominator"},
                f"malformed flow {pair_index}:{flow_index}",
            )
            lower_key = flow["lower"]
            upper_key = flow["upper"]
            require(type(lower_key) is str and lower_key in type_by_key, "unknown lower type")
            require(type(upper_key) is str and upper_key in type_by_key, "unknown upper type")
            lower_type = type_by_key[lower_key]
            upper_type = type_by_key[upper_key]
            require(absolute_rank(n, lower_type) == lower_rank, "lower type is in the wrong rank")
            require(absolute_rank(n, upper_type) == upper_rank, "upper type is in the wrong rank")
            require((lower_key, upper_key) not in seen_edges, "duplicate flow edge")
            seen_edges.add((lower_key, upper_key))
            if lower_type not in cached_upper:
                cached_upper[lower_type] = actual_upper_type_counts(n, lower_type)
            require(upper_type in cached_upper[lower_type], "claimed edge is not an actual D_n cover")
            numerator = exact_int(flow["numerator"], "flow numerator")
            denominator = exact_int(flow["denominator"], "flow denominator")
            require(numerator > 0 and denominator > 0, "serialized flows must be strictly positive")
            require(math.gcd(numerator, denominator) == 1, "flow fraction is not reduced")
            amount = Fraction(numerator, denominator)
            row_sums[lower_key] += amount
            column_sums[upper_key] += amount

            # Reconstruct the orbit-pair lift.  If d_out is the number of
            # relevant covers at a fixed lower vertex, then E=|A|d_out is the
            # total edge count.  B_n transitivity gives d_in=E/|B| at a fixed
            # upper vertex.  Each individual edge receives amount/E.
            d_out = cached_upper[lower_type][upper_type]
            edge_total = size_by_key[lower_key] * d_out
            require(edge_total % size_by_key[upper_key] == 0, "orbit pair is not biregular")
            d_in = edge_total // size_by_key[upper_key]
            individual_edge_amount = amount / edge_total
            lifted_row_sums[lower_key] += d_out * individual_edge_amount
            lifted_column_sums[upper_key] += d_in * individual_edge_amount
            verified_edges += 1

        lower_keys = [k for k, value in type_by_key.items() if absolute_rank(n, value) == lower_rank]
        upper_keys = [k for k, value in type_by_key.items() if absolute_rank(n, value) == upper_rank]
        actual_edge_count = 0
        for lower_key in lower_keys:
            lower_type = type_by_key[lower_key]
            if lower_type not in cached_upper:
                cached_upper[lower_type] = actual_upper_type_counts(n, lower_type)
            actual_edge_count += len(cached_upper[lower_type])
        require(
            exact_int(pair["edge_count"], "edge_count") == actual_edge_count,
            "orbit adjacency edge count is inconsistent",
        )
        for lower_key in lower_keys:
            expected = Fraction(size_by_key[lower_key], rank_sizes[lower_rank])
            require(row_sums[lower_key] == expected, f"row equation fails at {lower_key}")
            require(
                lifted_row_sums[lower_key] == Fraction(1, rank_sizes[lower_rank]),
                f"lifted per-vertex row equation fails at {lower_key}",
            )
        for upper_key in upper_keys:
            expected = Fraction(size_by_key[upper_key], rank_sizes[upper_rank])
            require(column_sums[upper_key] == expected, f"column equation fails at {upper_key}")
            require(
                lifted_column_sums[upper_key] == Fraction(1, rank_sizes[upper_rank]),
                f"lifted per-vertex column equation fails at {upper_key}",
            )
        require(sum(row_sums.values(), Fraction()) == 1, "total flow is not one")

    require(seen_pairs == {(r, r + 1) for r in range(n)}, "adjacent rank pairs are incomplete")
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "VERIFIED",
        "n": n,
        "orbits": len(expected_types),
        "rank_pairs": n,
        "positive_orbit_flows": verified_edges,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": code_hash,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (OSError, VerificationError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
