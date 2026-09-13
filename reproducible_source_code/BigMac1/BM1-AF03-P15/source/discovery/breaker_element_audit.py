#!/usr/bin/env python3
"""Element-level exact audit of the type-D normalized-flow quotient.

This program intentionally does not import ``discovery/orbit_lp.py``.  It
enumerates every even signed permutation, constructs every absolute cover by
right multiplication by a reflection, computes D_n-conjugacy orbits from
simple reflections, and only then groups elements by signed cycle type (the
B_n-conjugacy quotient used by the D9 discovery route).

For each adjacent pair of ranks it solves the quotient transportation problem
with an integer Edmonds--Karp implementation.  The resulting quotient flow is
then lifted by dividing by the *actual enumerated number of edges* between the
two orbit cells.  All vertex equations are checked with ``fractions.Fraction``.

The intended scope is n <= 6.  It is an independent finite baseline/audit, not
the D9 certificate itself.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Mapping, Sequence, Tuple


Element = Tuple[Tuple[int, ...], int]
CycleType = Tuple[Tuple[int, ...], Tuple[int, ...]]


def compose(left: Element, right: Element) -> Element:
    """Return left*right for monomial actions on column basis vectors."""
    lp, lm = left
    rp, rm = right
    n = len(lp)
    permutation = tuple(lp[rp[i]] for i in range(n))
    signs = 0
    for i in range(n):
        bit = ((rm >> i) & 1) ^ ((lm >> rp[i]) & 1)
        signs |= bit << i
    return permutation, signs


def inverse(value: Element) -> Element:
    permutation, signs = value
    n = len(permutation)
    inverse_permutation = [0] * n
    inverse_signs = 0
    for i, image in enumerate(permutation):
        inverse_permutation[image] = i
        inverse_signs |= ((signs >> i) & 1) << image
    return tuple(inverse_permutation), inverse_signs


def reflection(n: int, i: int, j: int, dotted: int) -> Element:
    permutation = list(range(n))
    permutation[i], permutation[j] = permutation[j], permutation[i]
    signs = ((1 << i) | (1 << j)) if dotted else 0
    return tuple(permutation), signs


def right_multiply_reflection(value: Element, i: int, j: int, dotted: int) -> Element:
    """Specialized exact right multiplication, independently checked in tests."""
    permutation, signs = value
    new_permutation = list(permutation)
    new_permutation[i], new_permutation[j] = permutation[j], permutation[i]
    bit_i = ((signs >> j) & 1) ^ dotted
    bit_j = ((signs >> i) & 1) ^ dotted
    cleared = signs & ~(1 << i) & ~(1 << j)
    new_signs = cleared | (bit_i << i) | (bit_j << j)
    return tuple(new_permutation), new_signs


def elements(n: int) -> List[Element]:
    even_masks = [mask for mask in range(1 << n) if mask.bit_count() % 2 == 0]
    return [(permutation, mask) for permutation in itertools.permutations(range(n)) for mask in even_masks]


def cycle_type(value: Element) -> CycleType:
    permutation, signs = value
    n = len(permutation)
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
            parity ^= (signs >> here) & 1
            here = permutation[here]
        (negative if parity else positive).append(length)
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def absolute_rank(value: Element) -> int:
    positive, negative = cycle_type(value)
    return sum(positive) + sum(negative) - len(positive)


def type_key(value: CycleType) -> str:
    positive, negative = value
    p = ",".join(map(str, positive)) or "-"
    q = ",".join(map(str, negative)) or "-"
    return f"P[{p}]N[{q}]"


def z(partition: Sequence[int]) -> int:
    counts = Counter(partition)
    answer = 1
    for part, multiplicity in counts.items():
        answer *= part**multiplicity * math.factorial(multiplicity)
    return answer


def expected_class_size(n: int, value: CycleType) -> int:
    positive, negative = value
    numerator = (1 << n) * math.factorial(n)
    denominator = (1 << (len(positive) + len(negative))) * z(positive) * z(negative)
    assert numerator % denominator == 0
    return numerator // denominator


def expected_upper_types(value: CycleType) -> set[CycleType]:
    """The PP->P, PN->N, P->NN support predicted from cycle surgery."""
    positive, negative = value
    result: set[CycleType] = set()

    for i in range(len(positive)):
        for j in range(i + 1, len(positive)):
            p = [part for k, part in enumerate(positive) if k not in (i, j)]
            p.append(positive[i] + positive[j])
            result.add((tuple(sorted(p, reverse=True)), negative))

    for i in range(len(positive)):
        for j in range(len(negative)):
            p = [part for k, part in enumerate(positive) if k != i]
            q = [part for k, part in enumerate(negative) if k != j]
            q.append(positive[i] + negative[j])
            result.add((tuple(sorted(p, reverse=True)), tuple(sorted(q, reverse=True))))

    for i, total in enumerate(positive):
        for first in range(1, total // 2 + 1):
            second = total - first
            p = [part for k, part in enumerate(positive) if k != i]
            q = list(negative) + [first, second]
            result.add((tuple(sorted(p, reverse=True)), tuple(sorted(q, reverse=True))))
    return result


def d_conjugacy_orbits(n: int, universe: Sequence[Element], index: Mapping[Element, int]) -> List[List[int]]:
    generators = [reflection(n, i, i + 1, 0) for i in range(n - 1)]
    generators.append(reflection(n, n - 2, n - 1, 1))
    unseen = set(range(len(universe)))
    orbits: List[List[int]] = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        orbit = [seed]
        queue = deque([seed])
        while queue:
            current = queue.popleft()
            value = universe[current]
            for generator in generators:
                conjugate = compose(compose(generator, value), generator)
                target = index[conjugate]
                if target in unseen:
                    unseen.remove(target)
                    orbit.append(target)
                    queue.append(target)
        orbits.append(sorted(orbit))
    return orbits


class IntegerNetwork:
    """Small Edmonds--Karp network; all capacities and flows are integers."""

    def __init__(self) -> None:
        self.capacity: DefaultDict[Tuple[str, str], int] = defaultdict(int)
        self.adjacency: DefaultDict[str, set[str]] = defaultdict(set)

    def add(self, source: str, target: str, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("negative capacity")
        self.capacity[(source, target)] += capacity
        self.adjacency[source].add(target)
        self.adjacency[target].add(source)

    def solve(self, source: str, sink: str) -> Tuple[int, Dict[Tuple[str, str], int]]:
        residual = dict(self.capacity)
        for u, neighbors in self.adjacency.items():
            for v in neighbors:
                residual.setdefault((u, v), 0)
                residual.setdefault((v, u), 0)
        value = 0
        while True:
            parent: Dict[str, str | None] = {source: None}
            queue = deque([source])
            while queue and sink not in parent:
                u = queue.popleft()
                for v in sorted(self.adjacency[u]):
                    if v not in parent and residual[(u, v)] > 0:
                        parent[v] = u
                        queue.append(v)
            if sink not in parent:
                break
            bottleneck: int | None = None
            v = sink
            while parent[v] is not None:
                u = parent[v]
                capacity = residual[(u, v)]
                bottleneck = capacity if bottleneck is None else min(bottleneck, capacity)
                v = u
            assert bottleneck is not None and bottleneck > 0
            v = sink
            while parent[v] is not None:
                u = parent[v]
                residual[(u, v)] -= bottleneck
                residual[(v, u)] += bottleneck
                v = u
            value += bottleneck
        flow = {edge: capacity - residual[edge] for edge, capacity in self.capacity.items()}
        return value, flow


def polynomial_rank_sizes(n: int) -> List[int]:
    coefficients = [1]
    exponents = list(range(1, 2 * n - 2, 2)) + [n - 1]
    for exponent in exponents:
        updated = [0] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            updated[i] += coefficient
            updated[i + 1] += exponent * coefficient
        coefficients = updated
    return coefficients


def encode_element(value: Element) -> Mapping[str, object]:
    return {"permutation": list(value[0]), "sign_mask": value[1]}


def audit(n: int) -> Mapping[str, object]:
    if n < 4 or n > 7:
        raise ValueError("element audit is intentionally restricted to 4 <= n <= 7")
    universe = elements(n)
    index = {value: i for i, value in enumerate(universe)}
    if len(index) != len(universe):
        raise AssertionError("duplicate group elements")
    expected_order = (1 << (n - 1)) * math.factorial(n)
    assert len(universe) == expected_order

    # Cross-check specialized reflection multiplication against generic composition.
    reflections = [reflection(n, i, j, dotted) for i in range(n) for j in range(i + 1, n) for dotted in (0, 1)]
    for value in universe[: min(128, len(universe))]:
        for i in range(n):
            for j in range(i + 1, n):
                for dotted in (0, 1):
                    assert right_multiply_reflection(value, i, j, dotted) == compose(value, reflection(n, i, j, dotted))

    signatures = [cycle_type(value) for value in universe]
    ranks = [n - len(signature[0]) for signature in signatures]
    type_members: DefaultDict[CycleType, List[int]] = defaultdict(list)
    rank_members: DefaultDict[int, List[int]] = defaultdict(list)
    for i, signature in enumerate(signatures):
        type_members[signature].append(i)
        rank_members[ranks[i]].append(i)

    rank_sizes = [len(rank_members[r]) for r in range(n + 1)]
    assert rank_sizes == polynomial_rank_sizes(n)
    assert rank_sizes != list(reversed(rank_sizes)), "unexpected rank symmetry"
    for signature, members in type_members.items():
        assert len(signature[1]) % 2 == 0
        assert len(members) == expected_class_size(n, signature)

    # Direct W(D_n)-conjugacy computation detects the well-known split classes.
    d_orbits = d_conjugacy_orbits(n, universe, index)
    d_orbits_by_type: DefaultDict[CycleType, List[List[int]]] = defaultdict(list)
    for orbit in d_orbits:
        orbit_types = {signatures[i] for i in orbit}
        assert len(orbit_types) == 1
        d_orbits_by_type[next(iter(orbit_types))].append(orbit)
    for signature, members in type_members.items():
        union = {i for orbit in d_orbits_by_type[signature] for i in orbit}
        assert union == set(members)

    # Enumerate all covers and retain edge multiplicities/degrees by B_n cell.
    edge_counts: Counter[Tuple[CycleType, CycleType]] = Counter()
    out_profiles: List[Counter[CycleType]] = [Counter() for _ in universe]
    in_profiles: List[Counter[CycleType]] = [Counter() for _ in universe]
    observed_upper: DefaultDict[CycleType, set[CycleType]] = defaultdict(set)
    for lower_index, lower in enumerate(universe):
        lower_rank = ranks[lower_index]
        for i in range(n):
            for j in range(i + 1, n):
                for dotted in (0, 1):
                    upper = right_multiply_reflection(lower, i, j, dotted)
                    upper_index = index[upper]
                    if ranks[upper_index] != lower_rank + 1:
                        continue
                    pair = (signatures[lower_index], signatures[upper_index])
                    edge_counts[pair] += 1
                    out_profiles[lower_index][pair[1]] += 1
                    in_profiles[upper_index][pair[0]] += 1
                    observed_upper[pair[0]].add(pair[1])

    for signature in type_members:
        observed = observed_upper.get(signature, set())
        expected = expected_upper_types(signature)
        if n - len(signature[0]) == n:
            expected = set()
        assert observed == expected, (signature, observed - expected, expected - observed)

    support_records: Dict[Tuple[CycleType, CycleType], Mapping[str, object]] = {}
    for pair, edge_count in sorted(edge_counts.items()):
        lower_type, upper_type = pair
        out_degrees = {out_profiles[i][upper_type] for i in type_members[lower_type]}
        in_degrees = {in_profiles[i][lower_type] for i in type_members[upper_type]}
        assert len(out_degrees) == 1 and len(in_degrees) == 1
        out_degree = next(iter(out_degrees))
        in_degree = next(iter(in_degrees))
        assert out_degree > 0 and in_degree > 0
        assert edge_count == len(type_members[lower_type]) * out_degree
        assert edge_count == len(type_members[upper_type]) * in_degree
        support_records[pair] = {
            "lower": type_key(lower_type),
            "upper": type_key(upper_type),
            "edge_count": edge_count,
            "out_degree": out_degree,
            "in_degree": in_degree,
        }

    rank_pairs: List[Mapping[str, object]] = []
    types_by_rank: Dict[int, List[CycleType]] = {
        rank: sorted({signatures[i] for i in members}) for rank, members in rank_members.items()
    }
    for rank in range(n):
        lower_types = types_by_rank[rank]
        upper_types = types_by_rank[rank + 1]
        lower_size = rank_sizes[rank]
        upper_size = rank_sizes[rank + 1]
        scale = lower_size * upper_size
        network = IntegerNetwork()
        source, sink = "SOURCE", "SINK"
        for value in lower_types:
            network.add(source, "L:" + type_key(value), len(type_members[value]) * upper_size)
        for value in upper_types:
            network.add("U:" + type_key(value), sink, len(type_members[value]) * lower_size)
        for lower_type, upper_type in edge_counts:
            if n - len(lower_type[0]) == rank:
                network.add("L:" + type_key(lower_type), "U:" + type_key(upper_type), scale)
        achieved, network_flow = network.solve(source, sink)
        assert achieved == scale

        flows: Dict[Tuple[CycleType, CycleType], int] = {}
        flow_records: List[Mapping[str, object]] = []
        for lower_type in lower_types:
            for upper_type in observed_upper[lower_type]:
                edge = ("L:" + type_key(lower_type), "U:" + type_key(upper_type))
                amount = network_flow.get(edge, 0)
                if amount:
                    flows[(lower_type, upper_type)] = amount
                    reduced = Fraction(amount, scale)
                    flow_records.append(
                        {
                            "lower": type_key(lower_type),
                            "upper": type_key(upper_type),
                            "cleared_amount": amount,
                            "numerator": reduced.numerator,
                            "denominator": reduced.denominator,
                        }
                    )

        # Explicit exact lifting: each edge in a cell pair gets F/E.
        outbound = [Fraction(0) for _ in universe]
        inbound = [Fraction(0) for _ in universe]
        for pair, amount in flows.items():
            lower_type, upper_type = pair
            edge_count = edge_counts[pair]
            per_edge = Fraction(amount, scale * edge_count)
            for member in type_members[lower_type]:
                outbound[member] += out_profiles[member][upper_type] * per_edge
            for member in type_members[upper_type]:
                inbound[member] += in_profiles[member][lower_type] * per_edge
        target_out = Fraction(1, lower_size)
        target_in = Fraction(1, upper_size)
        assert all(outbound[i] == target_out for i in rank_members[rank])
        assert all(inbound[i] == target_in for i in rank_members[rank + 1])
        assert all(outbound[i] == 0 for i in range(len(universe)) if ranks[i] != rank)
        assert all(inbound[i] == 0 for i in range(len(universe)) if ranks[i] != rank + 1)

        rank_pairs.append(
            {
                "lower_rank": rank,
                "upper_rank": rank + 1,
                "lower_size": lower_size,
                "upper_size": upper_size,
                "integer_scale": scale,
                "max_flow": achieved,
                "feasible": True,
                "support": [
                    support_records[pair]
                    for pair in sorted(edge_counts)
                    if n - len(pair[0][0]) == rank
                ],
                "flows": sorted(flow_records, key=lambda item: (item["lower"], item["upper"])),
                "lifted_vertex_equations_verified": True,
            }
        )

    type_records = []
    for signature in sorted(type_members, key=lambda value: (n - len(value[0]), value)):
        split_orbits = d_orbits_by_type[signature]
        type_records.append(
            {
                "key": type_key(signature),
                "positive": list(signature[0]),
                "negative": list(signature[1]),
                "rank": n - len(signature[0]),
                "class_size": len(type_members[signature]),
                "d_conjugacy_orbit_count": len(split_orbits),
                "d_conjugacy_orbit_sizes": sorted(len(orbit) for orbit in split_orbits),
                "d_conjugacy_representatives": [encode_element(universe[min(orbit)]) for orbit in split_orbits],
            }
        )

    return {
        "schema": "abs-dn-element-breaker-audit-v1",
        "scope": "finite element-level baseline; not a D9 certificate",
        "n": n,
        "group_order": len(universe),
        "reflection_count": len(reflections),
        "rank_sizes": rank_sizes,
        "rank_sizes_palindromic": rank_sizes == list(reversed(rank_sizes)),
        "b_type_count": len(type_members),
        "d_conjugacy_orbit_count": len(d_orbits),
        "split_b_types": [type_key(value) for value in sorted(type_members) if len(d_orbits_by_type[value]) > 1],
        "cycle_surgery_support_exact": True,
        "biregularity_exact": True,
        "all_rank_pairs_feasible": True,
        "all_lifted_vertex_equations_verified": True,
        "types": type_records,
        "rank_pairs": rank_pairs,
        "environment": {
            "python": sys.version.split()[0],
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "random_seed": None,
            "arithmetic": "integers and fractions.Fraction only",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.n)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "n": args.n,
                "group_order": result["group_order"],
                "b_type_count": result["b_type_count"],
                "d_conjugacy_orbit_count": result["d_conjugacy_orbit_count"],
                "rank_sizes": result["rank_sizes"],
                "feasible": result["all_rank_pairs_feasible"],
                "lift_verified": result["all_lifted_vertex_equations_verified"],
                "sha256": hashlib.sha256(encoded).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
