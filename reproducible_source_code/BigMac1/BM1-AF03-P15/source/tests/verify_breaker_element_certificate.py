#!/usr/bin/env python3
"""Independent fail-closed verifier for breaker_d*_element_audit.json.

Unlike the generator, this verifier represents a signed permutation by its
signed images (for example ``(-2, -1, 3, 4)``), constructs products through
signed substitution, and derives all covers from generic group composition.
It imports no discovery module and trusts no cached orbit sizes, degrees, or
flow totals from the JSON input.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path
from typing import DefaultDict, Dict, List, Mapping, Sequence, Tuple


SignedPermutation = Tuple[int, ...]
CycleType = Tuple[Tuple[int, ...], Tuple[int, ...]]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def exact_int(value: object, name: str, minimum: int | None = None) -> int:
    require(type(value) is int, f"{name} must be an integer")
    answer = value
    if minimum is not None:
        require(answer >= minimum, f"{name} is below {minimum}")
    return answer


def signed_elements(n: int) -> List[SignedPermutation]:
    answer: List[SignedPermutation] = []
    for permutation in itertools.permutations(range(1, n + 1)):
        for mask in range(1 << n):
            if mask.bit_count() % 2:
                continue
            answer.append(tuple(-value if (mask >> i) & 1 else value for i, value in enumerate(permutation)))
    return answer


def product(left: SignedPermutation, right: SignedPermutation) -> SignedPermutation:
    answer = []
    for image in right:
        outer = left[abs(image) - 1]
        answer.append(outer if image > 0 else -outer)
    return tuple(answer)


def reflection(n: int, i: int, j: int, dotted: int) -> SignedPermutation:
    answer = list(range(1, n + 1))
    if dotted:
        answer[i], answer[j] = -(j + 1), -(i + 1)
    else:
        answer[i], answer[j] = j + 1, i + 1
    return tuple(answer)


def signature(value: SignedPermutation) -> CycleType:
    n = len(value)
    underlying = [abs(image) - 1 for image in value]
    seen = [False] * n
    positive: List[int] = []
    negative: List[int] = []
    for start in range(n):
        if seen[start]:
            continue
        here = start
        length = 0
        parity = 0
        while not seen[here]:
            seen[here] = True
            length += 1
            parity ^= value[here] < 0
            here = underlying[here]
        (negative if parity else positive).append(length)
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def type_key(value: CycleType) -> str:
    positive, negative = value
    return "P[" + (",".join(map(str, positive)) or "-") + "]N[" + (",".join(map(str, negative)) or "-") + "]"


def z(partition: Sequence[int]) -> int:
    result = 1
    for part, multiplicity in Counter(partition).items():
        result *= part**multiplicity * math.factorial(multiplicity)
    return result


def closed_class_size(n: int, value: CycleType) -> int:
    positive, negative = value
    numerator = (1 << n) * math.factorial(n)
    denominator = (1 << (len(positive) + len(negative))) * z(positive) * z(negative)
    require(numerator % denominator == 0, "nonintegral class-size formula")
    return numerator // denominator


def d_orbits(n: int, universe: Sequence[SignedPermutation], index: Mapping[SignedPermutation, int]) -> List[List[int]]:
    simple = [reflection(n, i, i + 1, 0) for i in range(n - 1)]
    simple.append(reflection(n, n - 2, n - 1, 1))
    unseen = set(range(len(universe)))
    answer: List[List[int]] = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        orbit = [seed]
        queue = deque([seed])
        while queue:
            current = queue.popleft()
            for generator in simple:
                conjugate = product(product(generator, universe[current]), generator)
                target = index[conjugate]
                if target in unseen:
                    unseen.remove(target)
                    orbit.append(target)
                    queue.append(target)
        answer.append(sorted(orbit))
    return answer


def parse_type_record(n: int, record: object) -> Tuple[CycleType, Mapping[str, object]]:
    require(type(record) is dict, "type record must be an object")
    positive_raw = record.get("positive")
    negative_raw = record.get("negative")
    require(type(positive_raw) is list and type(negative_raw) is list, "partitions must be lists")
    positive = tuple(exact_int(v, "positive part", 1) for v in positive_raw)
    negative = tuple(exact_int(v, "negative part", 1) for v in negative_raw)
    require(tuple(sorted(positive, reverse=True)) == positive, "positive partition is not canonical")
    require(tuple(sorted(negative, reverse=True)) == negative, "negative partition is not canonical")
    require(sum(positive) + sum(negative) == n, "partition has wrong total")
    require(len(negative) % 2 == 0, "negative-cycle parity is odd")
    value = positive, negative
    require(record.get("key") == type_key(value), "type key mismatch")
    return value, record


def discovery_rep_to_signed(record: object, n: int) -> SignedPermutation:
    require(type(record) is dict, "representative must be an object")
    permutation = record.get("permutation")
    require(type(permutation) is list and len(permutation) == n, "bad representative permutation")
    p = tuple(exact_int(v, "representative image", 0) for v in permutation)
    require(sorted(p) == list(range(n)), "representative is not a permutation")
    mask = exact_int(record.get("sign_mask"), "representative sign mask", 0)
    require(mask < (1 << n) and mask.bit_count() % 2 == 0, "bad representative sign mask")
    return tuple(-(p[i] + 1) if (mask >> i) & 1 else p[i] + 1 for i in range(n))


def verify(data: object) -> Mapping[str, object]:
    require(type(data) is dict, "top level must be an object")
    require(data.get("schema") == "abs-dn-element-breaker-audit-v1", "wrong schema")
    require(data.get("scope") == "finite element-level baseline; not a D9 certificate", "wrong scope")
    n = exact_int(data.get("n"), "n", 4)
    require(n <= 7, "n exceeds verifier scope")

    universe = signed_elements(n)
    index = {value: i for i, value in enumerate(universe)}
    require(len(index) == len(universe), "enumerator produced duplicates")
    order = (1 << (n - 1)) * math.factorial(n)
    require(len(universe) == order, "wrong enumerated group order")
    require(exact_int(data.get("group_order"), "group_order", 1) == order, "certificate group order mismatch")
    require(exact_int(data.get("reflection_count"), "reflection_count", 1) == n * (n - 1), "reflection count mismatch")

    signatures = [signature(value) for value in universe]
    ranks = [n - len(value[0]) for value in signatures]
    members: DefaultDict[CycleType, List[int]] = defaultdict(list)
    rank_members: DefaultDict[int, List[int]] = defaultdict(list)
    for i, value in enumerate(signatures):
        members[value].append(i)
        rank_members[ranks[i]].append(i)
    rank_sizes = [len(rank_members[r]) for r in range(n + 1)]
    require(data.get("rank_sizes") == rank_sizes, "rank-size list mismatch")
    require(data.get("rank_sizes_palindromic") is False, "false rank-symmetry flag required")
    require(rank_sizes != list(reversed(rank_sizes)), "verifier unexpectedly found palindromic ranks")

    raw_types = data.get("types")
    require(type(raw_types) is list, "types must be a list")
    parsed_types: Dict[CycleType, Mapping[str, object]] = {}
    for raw in raw_types:
        value, record = parse_type_record(n, raw)
        require(value not in parsed_types, "duplicate type record")
        parsed_types[value] = record
    require(set(parsed_types) == set(members), "type list is incomplete or extraneous")
    require(exact_int(data.get("b_type_count"), "b_type_count", 1) == len(members), "B-type count mismatch")
    for value, indices in members.items():
        record = parsed_types[value]
        require(exact_int(record.get("rank"), "type rank", 0) == n - len(value[0]), "type rank mismatch")
        require(exact_int(record.get("class_size"), "class_size", 1) == len(indices), "enumerated class size mismatch")
        require(len(indices) == closed_class_size(n, value), "closed class-size formula mismatch")

    # Independently reconstruct W(D_n) conjugacy orbits.
    conjugacy = d_orbits(n, universe, index)
    by_type: DefaultDict[CycleType, List[List[int]]] = defaultdict(list)
    orbit_id: Dict[int, int] = {}
    for oid, orbit in enumerate(conjugacy):
        values = {signatures[i] for i in orbit}
        require(len(values) == 1, "conjugacy orbit crosses signed cycle types")
        by_type[next(iter(values))].append(orbit)
        for i in orbit:
            orbit_id[i] = oid
    require(exact_int(data.get("d_conjugacy_orbit_count"), "D orbit count", 1) == len(conjugacy), "D orbit count mismatch")
    actual_split = sorted(type_key(value) for value, orbits in by_type.items() if len(orbits) > 1)
    require(data.get("split_b_types") == actual_split, "split-class list mismatch")
    for value, record in parsed_types.items():
        orbits = by_type[value]
        require(exact_int(record.get("d_conjugacy_orbit_count"), "cell D-orbit count", 1) == len(orbits), "cell D-orbit count mismatch")
        require(record.get("d_conjugacy_orbit_sizes") == sorted(len(orbit) for orbit in orbits), "cell D-orbit sizes mismatch")
        raw_reps = record.get("d_conjugacy_representatives")
        require(type(raw_reps) is list and len(raw_reps) == len(orbits), "representative count mismatch")
        rep_orbits = set()
        for raw_rep in raw_reps:
            rep = discovery_rep_to_signed(raw_rep, n)
            require(rep in index and signature(rep) == value, "representative is outside its type")
            rep_orbits.add(orbit_id[index[rep]])
        require(len(rep_orbits) == len(orbits), "representatives do not meet distinct D orbits")

    # Build all cover edges with generic signed-permutation multiplication.
    reflections = [reflection(n, i, j, dotted) for i in range(n) for j in range(i + 1, n) for dotted in (0, 1)]
    edge_counts: Counter[Tuple[CycleType, CycleType]] = Counter()
    out_profiles: List[Counter[CycleType]] = [Counter() for _ in universe]
    in_profiles: List[Counter[CycleType]] = [Counter() for _ in universe]
    for lower_index, lower in enumerate(universe):
        for generator in reflections:
            upper = product(lower, generator)
            upper_index = index[upper]
            if ranks[upper_index] != ranks[lower_index] + 1:
                continue
            pair = signatures[lower_index], signatures[upper_index]
            edge_counts[pair] += 1
            out_profiles[lower_index][pair[1]] += 1
            in_profiles[upper_index][pair[0]] += 1

    require(data.get("cycle_surgery_support_exact") is True, "support-audit flag missing")
    require(data.get("biregularity_exact") is True, "biregularity flag missing")
    raw_rank_pairs = data.get("rank_pairs")
    require(type(raw_rank_pairs) is list and len(raw_rank_pairs) == n, "rank-pair list mismatch")
    parsed_keys = {type_key(value): value for value in members}
    total_nonzero_flows = 0
    for rank, record in enumerate(raw_rank_pairs):
        require(type(record) is dict, "rank-pair record must be an object")
        require(exact_int(record.get("lower_rank"), "lower_rank", 0) == rank, "rank-pair order mismatch")
        require(exact_int(record.get("upper_rank"), "upper_rank", 1) == rank + 1, "upper rank mismatch")
        lower_size, upper_size = rank_sizes[rank], rank_sizes[rank + 1]
        scale = lower_size * upper_size
        require(exact_int(record.get("lower_size"), "lower_size", 1) == lower_size, "lower size mismatch")
        require(exact_int(record.get("upper_size"), "upper_size", 1) == upper_size, "upper size mismatch")
        require(exact_int(record.get("integer_scale"), "integer_scale", 1) == scale, "scale mismatch")
        require(exact_int(record.get("max_flow"), "max_flow", 0) == scale, "claimed max flow is not full")
        require(record.get("feasible") is True and record.get("lifted_vertex_equations_verified") is True, "success flag missing")

        expected_pairs = {pair for pair in edge_counts if ranks[members[pair[0]][0]] == rank}
        raw_support = record.get("support")
        require(type(raw_support) is list, "support must be a list")
        seen_support: set[Tuple[CycleType, CycleType]] = set()
        for item in raw_support:
            require(type(item) is dict, "support item must be an object")
            lower_key, upper_key = item.get("lower"), item.get("upper")
            require(type(lower_key) is str and lower_key in parsed_keys, "unknown lower support key")
            require(type(upper_key) is str and upper_key in parsed_keys, "unknown upper support key")
            pair = parsed_keys[lower_key], parsed_keys[upper_key]
            require(pair in expected_pairs and pair not in seen_support, "bad or duplicate support pair")
            seen_support.add(pair)
            actual_out = {out_profiles[i][pair[1]] for i in members[pair[0]]}
            actual_in = {in_profiles[i][pair[0]] for i in members[pair[1]]}
            require(len(actual_out) == len(actual_in) == 1, "enumerated cell is not biregular")
            out_degree, in_degree = next(iter(actual_out)), next(iter(actual_in))
            require(exact_int(item.get("edge_count"), "edge_count", 1) == edge_counts[pair], "edge count mismatch")
            require(exact_int(item.get("out_degree"), "out_degree", 1) == out_degree, "out-degree mismatch")
            require(exact_int(item.get("in_degree"), "in_degree", 1) == in_degree, "in-degree mismatch")
            require(edge_counts[pair] == len(members[pair[0]]) * out_degree, "left biregular identity failed")
            require(edge_counts[pair] == len(members[pair[1]]) * in_degree, "right biregular identity failed")
        require(seen_support == expected_pairs, "support is incomplete")

        raw_flows = record.get("flows")
        require(type(raw_flows) is list, "flows must be a list")
        flows: Dict[Tuple[CycleType, CycleType], int] = {}
        for item in raw_flows:
            require(type(item) is dict, "flow item must be an object")
            lower_key, upper_key = item.get("lower"), item.get("upper")
            require(type(lower_key) is str and lower_key in parsed_keys, "unknown lower flow key")
            require(type(upper_key) is str and upper_key in parsed_keys, "unknown upper flow key")
            pair = parsed_keys[lower_key], parsed_keys[upper_key]
            require(pair in expected_pairs and pair not in flows, "unsupported or duplicate flow")
            amount = exact_int(item.get("cleared_amount"), "cleared_amount", 1)
            fraction = Fraction(amount, scale)
            require(exact_int(item.get("numerator"), "numerator", 1) == fraction.numerator, "reduced numerator mismatch")
            require(exact_int(item.get("denominator"), "denominator", 1) == fraction.denominator, "reduced denominator mismatch")
            flows[pair] = amount
        total_nonzero_flows += len(flows)

        for lower_type in {value for value in members if n - len(value[0]) == rank}:
            outgoing = sum(amount for (source, _), amount in flows.items() if source == lower_type)
            require(outgoing == len(members[lower_type]) * upper_size, "quotient left conservation failed")
        for upper_type in {value for value in members if n - len(value[0]) == rank + 1}:
            incoming = sum(amount for (_, target), amount in flows.items() if target == upper_type)
            require(incoming == len(members[upper_type]) * lower_size, "quotient right conservation failed")

        # Reconstruct every lifted vertex equation using actual cell degrees.
        outbound = [Fraction(0) for _ in universe]
        inbound = [Fraction(0) for _ in universe]
        for pair, amount in flows.items():
            per_edge = Fraction(amount, scale * edge_counts[pair])
            for i in members[pair[0]]:
                outbound[i] += out_profiles[i][pair[1]] * per_edge
            for i in members[pair[1]]:
                inbound[i] += in_profiles[i][pair[0]] * per_edge
        require(all(outbound[i] == Fraction(1, lower_size) for i in rank_members[rank]), "lifted lower equation failed")
        require(all(inbound[i] == Fraction(1, upper_size) for i in rank_members[rank + 1]), "lifted upper equation failed")

    require(data.get("all_rank_pairs_feasible") is True, "global feasibility flag missing")
    require(data.get("all_lifted_vertex_equations_verified") is True, "global lifting flag missing")
    return {
        "n": n,
        "group_order": order,
        "rank_sizes": rank_sizes,
        "b_type_count": len(members),
        "d_conjugacy_orbit_count": len(conjugacy),
        "cover_count": sum(edge_counts.values()),
        "nonzero_quotient_flows": total_nonzero_flows,
        "status": "ACCEPT",
    }


def mutated_copies(data: object) -> List[Tuple[str, object]]:
    require(type(data) is dict, "top level must be an object")
    mutations: List[Tuple[str, object]] = []

    changed = copy.deepcopy(data)
    changed["rank_sizes"][0] += 1
    mutations.append(("rank-size", changed))

    changed = copy.deepcopy(data)
    changed["types"] = changed["types"][:-1]
    mutations.append(("missing-type", changed))

    changed = copy.deepcopy(data)
    changed["rank_pairs"][0]["support"][0]["edge_count"] += 1
    mutations.append(("edge-multiplicity", changed))

    changed = copy.deepcopy(data)
    target = next(pair for pair in changed["rank_pairs"] if pair["flows"])
    target["flows"][0]["cleared_amount"] += 1
    mutations.append(("flow-conservation", changed))

    changed = copy.deepcopy(data)
    if changed["split_b_types"]:
        changed["split_b_types"] = []
    else:
        changed["split_b_types"] = ["P[-]N[-]"]
    mutations.append(("split-class", changed))
    return mutations


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    try:
        data = json.loads(raw)
        result = dict(verify(data))
        mutation_results = []
        if args.self_test_mutations:
            for name, changed in mutated_copies(data):
                try:
                    verify(changed)
                except Reject as error:
                    mutation_results.append({"mutation": name, "status": "REJECT", "reason": str(error)})
                else:
                    raise Reject(f"mutation {name} was incorrectly accepted")
            result["mutation_tests"] = mutation_results
        result["input_sha256"] = hashlib.sha256(raw).hexdigest()
        result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        print(json.dumps(result, sort_keys=True))
    except (OSError, json.JSONDecodeError, KeyError, IndexError, TypeError, Reject) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
