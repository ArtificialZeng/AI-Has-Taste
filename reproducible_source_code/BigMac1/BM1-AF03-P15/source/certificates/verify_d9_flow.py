#!/usr/bin/env python3
"""Fail-closed independent verifier for the D_9 orbit-flow certificate.

This file deliberately does not import discovery code.  It reconstructs the
B_n-orbits, their sizes, the rank polynomial, the orbit cover graph and all
lifted per-vertex flow equations from the serialized certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


TOP_KEYS = {
    "claim", "environment", "failure_cut", "layers", "n", "orbit_count",
    "orbit_encoding", "quotient_action", "rank_orbit_counts", "rank_sizes",
    "schema_version", "status",
}
FLOW_KEYS = {
    "degree_from", "degree_to", "denominator", "edge_count",
    "edge_denominator", "edge_numerator", "from", "numerator", "to",
}


class Rejected(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Rejected(message)


def exact_keys(value: object, keys: set[str], where: str) -> dict:
    require(isinstance(value, dict), f"{where}: expected object")
    assert isinstance(value, dict)
    require(set(value) == keys, f"{where}: keys differ (missing/extra fields)")
    return value


def integer(value: object, where: str, minimum: int | None = None) -> int:
    require(isinstance(value, int) and not isinstance(value, bool), f"{where}: expected integer")
    assert isinstance(value, int)
    if minimum is not None:
        require(value >= minimum, f"{where}: integer below {minimum}")
    return value


def all_partitions(total: int) -> list[tuple[int, ...]]:
    """Independent bottom-up partition generator."""
    table: list[set[tuple[int, ...]]] = [set() for _ in range(total + 1)]
    table[0].add(())
    for value in range(1, total + 1):
        for subtotal in range(value, total + 1):
            for old in tuple(table[subtotal - value]):
                candidate = tuple(sorted(old + (value,), reverse=True))
                table[subtotal].add(candidate)
    return sorted(table[total], reverse=True)


def orbit_types(n: int) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    result = set()
    for positive_sum in range(n + 1):
        for positive in all_partitions(positive_sum):
            for negative in all_partitions(n - positive_sum):
                if len(negative) % 2 == 0:
                    result.add((positive, negative))
    return result


def parse_partition(text: str, where: str) -> tuple[int, ...]:
    if text == "-":
        return ()
    require(text != "", f"{where}: empty partition encoding")
    fields = text.split(",")
    require(all(field.isascii() and field.isdigit() for field in fields),
            f"{where}: non-decimal partition field")
    values = tuple(int(field) for field in fields)
    require(all(value > 0 for value in values), f"{where}: nonpositive part")
    require(values == tuple(sorted(values, reverse=True)), f"{where}: noncanonical order")
    return values


def parse_type(text: object, n: int, where: str):
    require(isinstance(text, str), f"{where}: type id is not text")
    assert isinstance(text, str)
    require(text.count("|") == 1, f"{where}: malformed type separator")
    left, right = text.split("|")
    positive = parse_partition(left, where + ".positive")
    negative = parse_partition(right, where + ".negative")
    require(sum(positive) + sum(negative) == n, f"{where}: parts do not sum to n")
    require(len(negative) % 2 == 0, f"{where}: odd number of negative cycles")
    return positive, negative


def type_text(cycle_type) -> str:
    positive, negative = cycle_type
    return (",".join(map(str, positive)) or "-") + "|" + (",".join(map(str, negative)) or "-")


def z(partition: tuple[int, ...]) -> int:
    answer = 1
    for part, multiplicity in Counter(partition).items():
        answer *= part**multiplicity * math.factorial(multiplicity)
    return answer


def class_size(cycle_type, n: int) -> int:
    positive, negative = cycle_type
    denominator = 2 ** (len(positive) + len(negative)) * z(positive) * z(negative)
    numerator = 2**n * math.factorial(n)
    require(numerator % denominator == 0, "internal class-size divisibility failure")
    return numerator // denominator


def rank(cycle_type, n: int) -> int:
    return n - len(cycle_type[0])


def replace_parts(partition: tuple[int, ...], removed_indices: set[int], additions: tuple[int, ...]):
    retained = [part for index, part in enumerate(partition) if index not in removed_indices]
    return tuple(sorted(retained + list(additions), reverse=True))


def upward_degrees(cycle_type) -> Counter:
    """Derive upward orbit neighbors from the three signed-cycle operations."""
    positive, negative = cycle_type
    result: Counter = Counter()

    # Join two positive cycles: two choices of signed reflection per point pair.
    for i, first in enumerate(positive):
        for j in range(i + 1, len(positive)):
            second = positive[j]
            target_positive = replace_parts(positive, {i, j}, (first + second,))
            result[(target_positive, negative)] += 2 * first * second

    # Join a positive and a negative cycle: the result is negative.
    for i, first in enumerate(positive):
        for j, second in enumerate(negative):
            target_positive = replace_parts(positive, {i}, ())
            target_negative = replace_parts(negative, {j}, (first + second,))
            result[(target_positive, target_negative)] += 2 * first * second

    # Split one positive cycle into two negative cycles.  For unequal arc
    # lengths there are c point-pairs; for equal lengths there are c/2.
    for i, length in enumerate(positive):
        for first in range(1, length // 2 + 1):
            second = length - first
            if first > second:
                continue
            target_positive = replace_parts(positive, {i}, ())
            target_negative = tuple(sorted(negative + (first, second), reverse=True))
            multiplicity = length // 2 if first == second else length
            result[(target_positive, target_negative)] += multiplicity

    return result


def multiply_polynomial(linear_coefficients: list[int]) -> list[int]:
    coefficients = [1]
    for value in linear_coefficients:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] += coefficient
            updated[index + 1] += coefficient * value
        coefficients = updated
    return coefficients


def verify(certificate_path: Path, expected_n: int = 9) -> dict[str, object]:
    raw = certificate_path.read_bytes()
    try:
        document = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Rejected(f"invalid UTF-8 JSON: {exc}") from exc
    document = exact_keys(document, TOP_KEYS, "root")

    require(document["schema_version"] == 1, "unsupported schema_version")
    n = integer(document["n"], "n")
    require(expected_n >= 4, "expected endpoint must have n >= 4")
    require(n == expected_n, f"certificate endpoint must be exactly D_{expected_n}")
    require(document["claim"] == f"Abs(D_{n}) admits a normalized flow with unit vertex weights",
            f"claim text does not bind the D_{n} endpoint")
    require(document["quotient_action"] == f"conjugation by B_{n} on D_{n}", "wrong quotient action")
    require(document["orbit_encoding"] ==
            "positive_partition|negative_partition; negative partition has even length",
            "wrong orbit encoding")
    require(document["status"] == "feasible", "certificate is not marked feasible")
    require(document["failure_cut"] is None, "feasible certificate contains a failure cut")
    environment = exact_keys(document["environment"], {"algorithm", "platform", "python"}, "environment")
    for key, value in environment.items():
        require(isinstance(value, str) and bool(value), f"environment.{key}: expected nonempty text")

    types = orbit_types(n)
    sizes = {cycle_type: class_size(cycle_type, n) for cycle_type in types}
    ranks = {cycle_type: rank(cycle_type, n) for cycle_type in types}
    rank_orbit_counts = [sum(ranks[t] == level for t in types) for level in range(n + 1)]
    rank_sizes_by_orbits = [sum(sizes[t] for t in types if ranks[t] == level)
                            for level in range(n + 1)]
    exponents = list(range(1, 2 * n - 2, 2)) + [n - 1]
    rank_sizes_by_solomon = multiply_polynomial(exponents)
    require(rank_sizes_by_orbits == rank_sizes_by_solomon,
            "independent rank-size computations disagree")
    require(sum(rank_sizes_by_orbits) == 2 ** (n - 1) * math.factorial(n),
            "rank sizes do not sum to |D_n|")
    require(integer(document["orbit_count"], "orbit_count") == len(types), "wrong orbit_count")
    require(document["rank_orbit_counts"] == rank_orbit_counts, "wrong rank_orbit_counts")
    require(document["rank_sizes"] == rank_sizes_by_orbits, "wrong rank_sizes")

    layers = document["layers"]
    require(isinstance(layers, list) and len(layers) == n,
            f"must contain exactly {n} adjacent-rank layers")
    checked_pairs = 0
    lifted_equations = 0
    cleared_integer_equations = 0
    for level, layer_value in enumerate(layers):
        layer = exact_keys(layer_value, {"flows", "rank"}, f"layers[{level}]")
        require(integer(layer["rank"], f"layers[{level}].rank") == level,
                f"layers[{level}]: wrong or repeated rank")
        flow_list = layer["flows"]
        require(isinstance(flow_list, list), f"layers[{level}].flows: expected list")
        outgoing = {t: Fraction(0) for t in types if ranks[t] == level}
        incoming = {t: Fraction(0) for t in types if ranks[t] == level + 1}
        lifted_outgoing = outgoing.copy()
        lifted_incoming = incoming.copy()
        seen_pairs = set()
        scale = math.lcm(rank_sizes_by_orbits[level], rank_sizes_by_orbits[level + 1])
        for index, flow_value in enumerate(flow_list):
            where = f"layers[{level}].flows[{index}]"
            flow = exact_keys(flow_value, FLOW_KEYS, where)
            source = parse_type(flow["from"], n, where + ".from")
            target = parse_type(flow["to"], n, where + ".to")
            require(source in outgoing, where + ": source is not in the lower rank")
            require(target in incoming, where + ": target is not in the upper rank")
            require((source, target) not in seen_pairs, where + ": duplicate orbit pair")
            seen_pairs.add((source, target))

            numerator = integer(flow["numerator"], where + ".numerator", 1)
            denominator = integer(flow["denominator"], where + ".denominator", 1)
            require(math.gcd(numerator, denominator) == 1, where + ": noncanonical flow fraction")
            total_flow = Fraction(numerator, denominator)
            cleared_amount = total_flow * scale
            require(cleared_amount.denominator == 1,
                    where + ": orbit flow does not clear at the canonical integer scale")

            neighbor_degrees = upward_degrees(source)
            require(target in neighbor_degrees, where + ": pair is not a cover-orbit adjacency")
            degree_from = integer(flow["degree_from"], where + ".degree_from", 1)
            degree_to = integer(flow["degree_to"], where + ".degree_to", 1)
            edge_count = integer(flow["edge_count"], where + ".edge_count", 1)
            require(degree_from == neighbor_degrees[target], where + ": wrong lower degree")
            require(edge_count == sizes[source] * degree_from, where + ": wrong edge count from lower orbit")
            require(edge_count == sizes[target] * degree_to, where + ": non-biregular upper degree")

            edge_numerator = integer(flow["edge_numerator"], where + ".edge_numerator", 1)
            edge_denominator = integer(flow["edge_denominator"], where + ".edge_denominator", 1)
            require(math.gcd(edge_numerator, edge_denominator) == 1,
                    where + ": noncanonical per-edge fraction")
            edge_flow = Fraction(edge_numerator, edge_denominator)
            require(edge_flow == total_flow / edge_count, where + ": per-edge flow is not total/edge_count")

            outgoing[source] += total_flow
            incoming[target] += total_flow
            lifted_outgoing[source] += degree_from * edge_flow
            lifted_incoming[target] += degree_to * edge_flow
            checked_pairs += 1

        for source in outgoing:
            require(outgoing[source] == Fraction(sizes[source], rank_sizes_by_orbits[level]),
                    f"rank {level} orbit {type_text(source)}: lower conservation failure")
            require(lifted_outgoing[source] == Fraction(1, rank_sizes_by_orbits[level]),
                    f"rank {level} orbit {type_text(source)}: lifted vertex outflow failure")
            require(outgoing[source] * scale ==
                    sizes[source] * (scale // rank_sizes_by_orbits[level]),
                    f"rank {level} orbit {type_text(source)}: cleared integer row failure")
            lifted_equations += sizes[source]
            cleared_integer_equations += 1
        for target in incoming:
            require(incoming[target] == Fraction(sizes[target], rank_sizes_by_orbits[level + 1]),
                    f"rank {level + 1} orbit {type_text(target)}: upper conservation failure")
            require(lifted_incoming[target] == Fraction(1, rank_sizes_by_orbits[level + 1]),
                    f"rank {level + 1} orbit {type_text(target)}: lifted vertex inflow failure")
            require(incoming[target] * scale ==
                    sizes[target] * (scale // rank_sizes_by_orbits[level + 1]),
                    f"rank {level + 1} orbit {type_text(target)}: cleared integer column failure")
            lifted_equations += sizes[target]
            cleared_integer_equations += 1

    certificate_hash = hashlib.sha256(raw).hexdigest()
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "result": "VERIFIED",
        "endpoint": f"Abs(D_{n}) normalized flow",
        "orbits": len(types),
        "orbit_pairs_with_positive_flow": checked_pairs,
        "cleared_integer_orbit_equations": cleared_integer_equations,
        "lifted_vertex_equations": lifted_equations,
        "certificate_sha256": certificate_hash,
        "verifier_sha256": code_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--expected-n", type=int, default=9)
    args = parser.parse_args()
    try:
        result = verify(args.certificate, expected_n=args.expected_n)
    except (OSError, Rejected) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
