#!/usr/bin/env python3
"""Exact orbit-quotient normalized-flow construction for Abs(D_n).

This is discovery code, but it uses integers/Fractions throughout.  Nodes are
B_n-conjugacy classes in D_n, indexed by signed cycle type (lambda, mu), where
lambda lists positive-cycle lengths and mu lists negative-cycle lengths.

For every adjacent rank pair the normalized-flow problem is a transportation
problem.  Clearing the two rank-size denominators turns it into an integral
maximum-flow instance, which is solved here by a small self-contained Dinic
implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple


Partition = Tuple[int, ...]
CycleType = Tuple[Partition, Partition]


def partitions(n: int, cap: int | None = None) -> Iterable[Partition]:
    """Yield partitions of n as weakly decreasing tuples."""
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def cycle_types(n: int) -> List[CycleType]:
    """B_n-conjugacy classes contained in D_n."""
    ans: List[CycleType] = []
    for m in range(n + 1):
        for positive in partitions(n - m):
            for negative in partitions(m):
                if len(negative) % 2 == 0:
                    ans.append((positive, negative))
    return ans


def z(partition: Partition) -> int:
    """z_lambda = product_i i^(m_i) m_i!."""
    multiplicities: Dict[int, int] = defaultdict(int)
    for part in partition:
        multiplicities[part] += 1
    value = 1
    for part, multiplicity in multiplicities.items():
        value *= part**multiplicity * math.factorial(multiplicity)
    return value


def class_size(n: int, cycle_type: CycleType) -> int:
    """Size of the B_n conjugacy class indexed by (lambda, mu)."""
    positive, negative = cycle_type
    denominator = 2 ** (len(positive) + len(negative)) * z(positive) * z(negative)
    numerator = 2**n * math.factorial(n)
    assert numerator % denominator == 0
    return numerator // denominator


def rank(cycle_type: CycleType) -> int:
    """Reflection length in D_n = codim Fix = n - #positive cycles."""
    positive, negative = cycle_type
    return sum(positive) + sum(negative) - len(positive)


def _drop(partition: Partition, indices: Sequence[int]) -> List[int]:
    doomed = set(indices)
    return [value for i, value in enumerate(partition) if i not in doomed]


def upper_neighbors(cycle_type: CycleType) -> List[CycleType]:
    """All signed cycle types obtainable along one upward absolute cover.

    The three operations are
      PP -> P,  PN -> N,  and  P -> NN.
    Only existence, rather than edge multiplicity, is needed in the quotient.
    """
    positive, negative = cycle_type
    ans: set[CycleType] = set()

    # Merge two positive cycles into one positive cycle.
    for i in range(len(positive)):
        for j in range(i + 1, len(positive)):
            new_positive = _drop(positive, (i, j)) + [positive[i] + positive[j]]
            ans.add((tuple(sorted(new_positive, reverse=True)), negative))

    # Merge one positive and one negative cycle into a negative cycle.
    for i in range(len(positive)):
        for j in range(len(negative)):
            new_positive = tuple(sorted(_drop(positive, (i,)), reverse=True))
            new_negative = _drop(negative, (j,)) + [positive[i] + negative[j]]
            ans.add((new_positive, tuple(sorted(new_negative, reverse=True))))

    # Split one positive cycle into two negative cycles.
    for i, total in enumerate(positive):
        for left in range(1, total // 2 + 1):
            right = total - left
            new_positive = tuple(sorted(_drop(positive, (i,)), reverse=True))
            new_negative = tuple(sorted(list(negative) + [left, right], reverse=True))
            ans.add((new_positive, new_negative))

    expected_rank = rank(cycle_type) + 1
    assert all(rank(target) == expected_rank for target in ans)
    return sorted(ans)


@dataclass
class Arc:
    target: int
    reverse: int
    capacity: int
    initial_capacity: int


class Dinic:
    def __init__(self, vertex_count: int) -> None:
        self.graph: List[List[Arc]] = [[] for _ in range(vertex_count)]

    def add_arc(self, source: int, target: int, capacity: int) -> int:
        assert capacity >= 0
        forward_index = len(self.graph[source])
        reverse_index = len(self.graph[target])
        self.graph[source].append(Arc(target, reverse_index, capacity, capacity))
        self.graph[target].append(Arc(source, forward_index, 0, 0))
        return forward_index

    def max_flow(self, source: int, sink: int) -> int:
        total = 0
        vertex_count = len(self.graph)
        while True:
            level = [-1] * vertex_count
            level[source] = 0
            queue = deque([source])
            while queue:
                vertex = queue.popleft()
                for arc in self.graph[vertex]:
                    if arc.capacity and level[arc.target] < 0:
                        level[arc.target] = level[vertex] + 1
                        queue.append(arc.target)
            if level[sink] < 0:
                return total
            cursor = [0] * vertex_count

            def augment(vertex: int, amount: int) -> int:
                if vertex == sink:
                    return amount
                while cursor[vertex] < len(self.graph[vertex]):
                    arc = self.graph[vertex][cursor[vertex]]
                    if arc.capacity and level[arc.target] == level[vertex] + 1:
                        pushed = augment(arc.target, min(amount, arc.capacity))
                        if pushed:
                            arc.capacity -= pushed
                            self.graph[arc.target][arc.reverse].capacity += pushed
                            return pushed
                    cursor[vertex] += 1
                return 0

            while True:
                pushed = augment(source, 10**100)
                if not pushed:
                    break
                total += pushed


def type_key(cycle_type: CycleType) -> str:
    positive, negative = cycle_type
    p = ",".join(map(str, positive)) or "-"
    q = ",".join(map(str, negative)) or "-"
    return f"P[{p}]N[{q}]"


def construct(n: int) -> Mapping[str, object]:
    types = cycle_types(n)
    sizes = {cycle_type: class_size(n, cycle_type) for cycle_type in types}
    by_rank: Dict[int, List[CycleType]] = defaultdict(list)
    for cycle_type in types:
        by_rank[rank(cycle_type)].append(cycle_type)
    for values in by_rank.values():
        values.sort()
    rank_sizes = {r: sum(sizes[t] for t in values) for r, values in by_rank.items()}

    # Global structural checks independent of flow construction.
    assert sum(sizes.values()) == 2 ** (n - 1) * math.factorial(n)
    expected_coefficients = [1]
    for exponent in list(range(1, 2 * n - 2, 2)) + [n - 1]:
        new = [0] * (len(expected_coefficients) + 1)
        for i, coefficient in enumerate(expected_coefficients):
            new[i] += coefficient
            new[i + 1] += exponent * coefficient
        expected_coefficients = new
    assert [rank_sizes[r] for r in range(n + 1)] == expected_coefficients

    pair_records = []
    for r in range(n):
        lower = by_rank[r]
        upper = by_rank[r + 1]
        lower_index = {value: i for i, value in enumerate(lower)}
        upper_index = {value: i for i, value in enumerate(upper)}

        scale = math.lcm(rank_sizes[r], rank_sizes[r + 1])
        supplies = [scale * sizes[value] // rank_sizes[r] for value in lower]
        demands = [scale * sizes[value] // rank_sizes[r + 1] for value in upper]
        assert sum(supplies) == scale == sum(demands)

        source = 0
        lower_offset = 1
        upper_offset = lower_offset + len(lower)
        sink = upper_offset + len(upper)
        network = Dinic(sink + 1)
        for i, supply in enumerate(supplies):
            network.add_arc(source, lower_offset + i, supply)
        for j, demand in enumerate(demands):
            network.add_arc(upper_offset + j, sink, demand)

        arc_locations: Dict[Tuple[int, int], Tuple[int, int]] = {}
        for i, value in enumerate(lower):
            for target in upper_neighbors(value):
                assert target in upper_index, (value, target)
                j = upper_index[target]
                vertex = lower_offset + i
                arc_index = network.add_arc(vertex, upper_offset + j, scale)
                arc_locations[(i, j)] = (vertex, arc_index)

        achieved = network.max_flow(source, sink)
        flows = []
        if achieved == scale:
            for (i, j), (vertex, arc_index) in sorted(arc_locations.items()):
                arc = network.graph[vertex][arc_index]
                amount = arc.initial_capacity - arc.capacity
                if amount:
                    value = Fraction(amount, scale)
                    flows.append(
                        {
                            "lower": type_key(lower[i]),
                            "upper": type_key(upper[j]),
                            "numerator": value.numerator,
                            "denominator": value.denominator,
                        }
                    )

        pair_records.append(
            {
                "lower_rank": r,
                "upper_rank": r + 1,
                "scale": scale,
                "max_flow": achieved,
                "feasible": achieved == scale,
                "edge_count": len(arc_locations),
                "nonzero_flow_count": len(flows),
                "flows": flows,
            }
        )

    type_records = [
        {
            "key": type_key(cycle_type),
            "positive": list(cycle_type[0]),
            "negative": list(cycle_type[1]),
            "rank": rank(cycle_type),
            "class_size": sizes[cycle_type],
        }
        for cycle_type in sorted(types, key=lambda value: (rank(value), value))
    ]
    return {
        "schema": "abs-dn-bn-orbit-flow-v1",
        "n": n,
        "group_order": 2 ** (n - 1) * math.factorial(n),
        "orbit_count": len(types),
        "rank_sizes": [rank_sizes[r] for r in range(n + 1)],
        "all_rank_pairs_feasible": all(record["feasible"] for record in pair_records),
        "types": type_records,
        "rank_pairs": pair_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.n < 2:
        parser.error("n must be at least 2")
    result = construct(args.n)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.output:
        args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "n": args.n,
                "orbit_count": result["orbit_count"],
                "rank_sizes": result["rank_sizes"],
                "feasible": result["all_rank_pairs_feasible"],
                "sha256": hashlib.sha256(encoded).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
