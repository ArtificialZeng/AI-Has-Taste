#!/usr/bin/env python3
"""Independent exact verifier for B_n-orbit normalized-flow candidates.

This verifier imports no discovery code.  It regenerates all signed cycle
types, class sizes, ranks, and quotient support.  Support is reconstructed by
a generic signed-cycle merge/split operation (not by hard-coding PP->P,
PN->N, P->NN).  It also derives exact per-element cover degrees, hence the
number of original Hasse edges in every orbit-cell pair, and checks the lifted
per-vertex equations with rational arithmetic.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Mapping, Sequence, Tuple


Partition = Tuple[int, ...]
CycleType = Tuple[Partition, Partition]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def integer(value: object, name: str, minimum: int | None = None) -> int:
    require(type(value) is int, f"{name} must be an integer")
    result = value
    if minimum is not None:
        require(result >= minimum, f"{name} is below {minimum}")
    return result


def partitions_ascending(total: int, minimum: int = 1) -> Iterable[Partition]:
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for rest in partitions_ascending(total - first, first):
            yield (first,) + rest


def all_types(n: int) -> set[CycleType]:
    answer = set()
    for negative_total in range(n + 1):
        for positive_ascending in partitions_ascending(n - negative_total):
            for negative_ascending in partitions_ascending(negative_total):
                if len(negative_ascending) % 2 == 0:
                    answer.add((tuple(reversed(positive_ascending)), tuple(reversed(negative_ascending))))
    return answer


def key(value: CycleType) -> str:
    positive, negative = value
    return "P[" + (",".join(map(str, positive)) or "-") + "]N[" + (",".join(map(str, negative)) or "-") + "]"


def z(partition: Sequence[int]) -> int:
    result = 1
    for part, multiplicity in Counter(partition).items():
        result *= part**multiplicity * math.factorial(multiplicity)
    return result


def class_size(n: int, value: CycleType) -> int:
    positive, negative = value
    numerator = (1 << n) * math.factorial(n)
    denominator = (1 << (len(positive) + len(negative))) * z(positive) * z(negative)
    require(numerator % denominator == 0, "class size is nonintegral")
    return numerator // denominator


def rank(value: CycleType) -> int:
    positive, negative = value
    return sum(positive) + sum(negative) - len(positive)


def canonical(cycles: Sequence[Tuple[int, int]]) -> CycleType:
    positive = sorted((length for length, sign in cycles if sign == 0), reverse=True)
    negative = sorted((length for length, sign in cycles if sign == 1), reverse=True)
    return tuple(positive), tuple(negative)


def generic_upper_degrees(value: CycleType) -> Counter[CycleType]:
    """Count upper covers of each target type from a fixed source element.

    A cycle is represented by (length, sign).  Merging two cycles has two
    reflection sign choices for each pair of letters.  Splitting a cycle has
    both compatible output-sign assignments; the cyclic chord count is L,
    except L/2 for an equal split.  Only surgeries whose codimension rises by
    one are retained.
    """
    positive, negative = value
    cycles = [(length, 0) for length in positive] + [(length, 1) for length in negative]
    source_rank = rank(value)
    answer: Counter[CycleType] = Counter()

    # Join two cycles.  Both reflection sign choices have the same cycle type.
    for i in range(len(cycles)):
        for j in range(i + 1, len(cycles)):
            a, sign_a = cycles[i]
            b, sign_b = cycles[j]
            remaining = [cycle for k, cycle in enumerate(cycles) if k not in (i, j)]
            target = canonical(remaining + [(a + b, sign_a ^ sign_b)])
            if rank(target) == source_rank + 1:
                answer[target] += 2 * a * b

    # Split one cycle.  Output signs xor to the input sign.
    for i, (length, old_sign) in enumerate(cycles):
        remaining = [cycle for k, cycle in enumerate(cycles) if k != i]
        for first in range(1, length // 2 + 1):
            second = length - first
            chord_count = length // 2 if first == second else length
            sign_assignments = [(0, old_sign), (1, old_sign ^ 1)]
            seen_assignments = set()
            for sign_first, sign_second in sign_assignments:
                assignment = canonical([(first, sign_first), (second, sign_second)])
                # For an equal split, swapping the signs is the same output and
                # the two listed assignments must not be double-counted.
                if assignment in seen_assignments:
                    continue
                seen_assignments.add(assignment)
                target = canonical(remaining + [(first, sign_first), (second, sign_second)])
                if rank(target) == source_rank + 1:
                    answer[target] += chord_count
    return answer


def rank_polynomial(n: int) -> List[int]:
    coefficients = [1]
    for exponent in list(range(1, 2 * n - 2, 2)) + [n - 1]:
        updated = [0] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            updated[i] += coefficient
            updated[i + 1] += exponent * coefficient
        coefficients = updated
    return coefficients


def parse_types(data: Mapping[str, object], n: int, expected: set[CycleType]) -> Dict[str, CycleType]:
    raw = data.get("types")
    require(type(raw) is list, "types must be a list")
    parsed: Dict[str, CycleType] = {}
    for record in raw:
        require(type(record) is dict, "type record must be an object")
        p_raw, q_raw = record.get("positive"), record.get("negative")
        require(type(p_raw) is list and type(q_raw) is list, "partitions must be lists")
        p = tuple(integer(part, "positive part", 1) for part in p_raw)
        q = tuple(integer(part, "negative part", 1) for part in q_raw)
        require(p == tuple(sorted(p, reverse=True)) and q == tuple(sorted(q, reverse=True)), "noncanonical partition")
        value = p, q
        require(value in expected, "extraneous signed cycle type")
        label = key(value)
        require(record.get("key") == label and label not in parsed, "bad or duplicate type key")
        require(integer(record.get("rank"), "type rank", 0) == rank(value), "type rank mismatch")
        require(integer(record.get("class_size"), "class_size", 1) == class_size(n, value), "class size mismatch")
        parsed[label] = value
    require(set(parsed.values()) == expected, "type list is incomplete")
    return parsed


def verify(data: object) -> Mapping[str, object]:
    require(type(data) is dict, "top level must be an object")
    require(data.get("schema") == "abs-dn-bn-orbit-flow-v1", "wrong schema")
    n = integer(data.get("n"), "n", 4)
    expected_types = all_types(n)
    parsed = parse_types(data, n, expected_types)
    sizes = {value: class_size(n, value) for value in expected_types}
    order = (1 << (n - 1)) * math.factorial(n)
    require(sum(sizes.values()) == order, "B-orbit cells do not partition D_n")
    require(integer(data.get("group_order"), "group_order", 1) == order, "group order mismatch")
    require(integer(data.get("orbit_count"), "orbit_count", 1) == len(expected_types), "orbit count mismatch")

    by_rank: DefaultDict[int, List[CycleType]] = defaultdict(list)
    for value in expected_types:
        by_rank[rank(value)].append(value)
    rank_sizes = [sum(sizes[value] for value in by_rank[r]) for r in range(n + 1)]
    require(rank_sizes == rank_polynomial(n), "rank polynomial mismatch")
    require(data.get("rank_sizes") == rank_sizes, "rank sizes mismatch")
    require(rank_sizes != list(reversed(rank_sizes)), "unjustified rank symmetry")

    degrees = {value: generic_upper_degrees(value) for value in expected_types}
    edge_counts: Dict[Tuple[CycleType, CycleType], int] = {}
    incoming_degrees: Dict[Tuple[CycleType, CycleType], int] = {}
    for lower, targets in degrees.items():
        for upper, out_degree in targets.items():
            require(upper in expected_types and rank(upper) == rank(lower) + 1, "invalid generic surgery target")
            edge_count = sizes[lower] * out_degree
            require(edge_count % sizes[upper] == 0, "cell edge count is incompatible with right biregularity")
            in_degree = edge_count // sizes[upper]
            require(in_degree > 0, "zero incoming degree")
            edge_counts[(lower, upper)] = edge_count
            incoming_degrees[(lower, upper)] = in_degree
    total_covers = sum(edge_counts.values())
    require(total_covers == order * n * (n - 1) // 2, "global cover count mismatch")

    raw_pairs = data.get("rank_pairs")
    require(type(raw_pairs) is list and len(raw_pairs) == n, "rank-pair list mismatch")
    total_nonzero = 0
    for r, record in enumerate(raw_pairs):
        require(type(record) is dict, "rank-pair record must be an object")
        require(integer(record.get("lower_rank"), "lower_rank", 0) == r, "lower rank mismatch")
        require(integer(record.get("upper_rank"), "upper_rank", 1) == r + 1, "upper rank mismatch")
        support = {(lower, upper) for (lower, upper) in edge_counts if rank(lower) == r}
        require(integer(record.get("edge_count"), "edge_count", 0) == len(support), "quotient support count mismatch")
        scale = integer(record.get("scale"), "scale", 1)
        require(scale == math.lcm(rank_sizes[r], rank_sizes[r + 1]), "unexpected clearing scale")
        require(record.get("feasible") is True, "rank pair is not marked feasible")
        require(integer(record.get("max_flow"), "max_flow", 0) == scale, "max-flow value is not full")

        raw_flows = record.get("flows")
        require(type(raw_flows) is list, "flows must be a list")
        require(integer(record.get("nonzero_flow_count"), "nonzero_flow_count", 0) == len(raw_flows), "nonzero-flow count mismatch")
        flows: Dict[Tuple[CycleType, CycleType], Fraction] = {}
        for item in raw_flows:
            require(type(item) is dict, "flow entry must be an object")
            lower_key, upper_key = item.get("lower"), item.get("upper")
            require(type(lower_key) is str and lower_key in parsed, "unknown lower type")
            require(type(upper_key) is str and upper_key in parsed, "unknown upper type")
            pair = parsed[lower_key], parsed[upper_key]
            require(pair in support and pair not in flows, "unsupported or duplicate quotient flow")
            numerator = integer(item.get("numerator"), "flow numerator", 1)
            denominator = integer(item.get("denominator"), "flow denominator", 1)
            require(math.gcd(numerator, denominator) == 1, "flow fraction is not reduced")
            value = Fraction(numerator, denominator)
            require(value * scale == int(value * scale), "flow does not lie on claimed integer scale")
            flows[pair] = value
        total_nonzero += len(flows)

        # Exact quotient conservation.
        for lower in by_rank[r]:
            outgoing = sum((amount for (source, _), amount in flows.items() if source == lower), Fraction(0))
            require(outgoing == Fraction(sizes[lower], rank_sizes[r]), "lower quotient conservation failed")
        for upper in by_rank[r + 1]:
            incoming = sum((amount for (_, target), amount in flows.items() if target == upper), Fraction(0))
            require(incoming == Fraction(sizes[upper], rank_sizes[r + 1]), "upper quotient conservation failed")

        # Independent lifted equations using derived cell multiplicities.
        for lower in by_rank[r]:
            lifted = Fraction(0)
            for (source, upper), amount in flows.items():
                if source != lower:
                    continue
                per_edge = amount / edge_counts[(source, upper)]
                lifted += degrees[source][upper] * per_edge
            require(lifted == Fraction(1, rank_sizes[r]), "lifted lower vertex equation failed")
        for upper in by_rank[r + 1]:
            lifted = Fraction(0)
            for (lower, target), amount in flows.items():
                if target != upper:
                    continue
                per_edge = amount / edge_counts[(lower, target)]
                lifted += incoming_degrees[(lower, target)] * per_edge
            require(lifted == Fraction(1, rank_sizes[r + 1]), "lifted upper vertex equation failed")

    require(data.get("all_rank_pairs_feasible") is True, "global feasibility flag missing")
    return {
        "status": "ACCEPT",
        "n": n,
        "group_order": order,
        "orbit_count": len(expected_types),
        "rank_sizes": rank_sizes,
        "quotient_support_count": len(edge_counts),
        "full_hasse_cover_count": total_covers,
        "nonzero_quotient_flows": total_nonzero,
        "lifted_equations": "exact rational",
    }


def mutations(data: object) -> List[Tuple[str, object]]:
    require(type(data) is dict, "top level must be an object")
    answer = []

    changed = copy.deepcopy(data)
    changed["types"][0]["class_size"] += 1
    answer.append(("class-size", changed))

    changed = copy.deepcopy(data)
    changed["rank_pairs"][0]["edge_count"] += 1
    answer.append(("support-count", changed))

    changed = copy.deepcopy(data)
    pair = next(record for record in changed["rank_pairs"] if record["flows"])
    pair["flows"][0]["numerator"] += 1
    answer.append(("flow", changed))

    changed = copy.deepcopy(data)
    changed["rank_sizes"][-1] += 1
    answer.append(("rank-size", changed))
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    try:
        data = json.loads(raw)
        result = dict(verify(data))
        if args.self_test_mutations:
            outcomes = []
            for name, changed in mutations(data):
                try:
                    verify(changed)
                except Reject as error:
                    outcomes.append({"mutation": name, "status": "REJECT", "reason": str(error)})
                else:
                    raise Reject(f"mutation {name} was incorrectly accepted")
            result["mutation_tests"] = outcomes
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        print(json.dumps(result, sort_keys=True))
    except (OSError, json.JSONDecodeError, KeyError, IndexError, TypeError, Reject) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
