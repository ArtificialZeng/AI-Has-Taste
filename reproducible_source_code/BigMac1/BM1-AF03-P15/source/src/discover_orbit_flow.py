#!/usr/bin/env python3
"""Discover exact orbit-level normalized flows for Abs(D_n).

This is discovery code, not the independent verifier.  The quotient uses the
conjugation action of B_n on its normal subgroup D_n.  B_n-orbits in D_n are
the signed cycle types (lambda, mu) with len(mu) even.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def partitions(total: int, maximum: int | None = None) -> Iterable[tuple[int, ...]]:
    """Yield integer partitions in weakly decreasing order; include () for 0."""
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def signed_cycle_types(n: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    result = []
    for positive_size in range(n + 1):
        for lam in partitions(positive_size):
            for mu in partitions(n - positive_size):
                if len(mu) % 2 == 0:
                    result.append((lam, mu))
    return sorted(result, key=lambda t: (n - len(t[0]), t[0], t[1]))


def z_value(partition: tuple[int, ...]) -> int:
    counts = Counter(partition)
    answer = 1
    for part, multiplicity in counts.items():
        answer *= (part ** multiplicity) * math.factorial(multiplicity)
    return answer


def orbit_size(n: int, cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> int:
    lam, mu = cycle_type
    centralizer = (2 ** (len(lam) + len(mu))) * z_value(lam) * z_value(mu)
    numerator = (2**n) * math.factorial(n)
    assert numerator % centralizer == 0
    return numerator // centralizer


def representative(cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> tuple[int, ...]:
    """Return a signed-permutation window with the requested signed cycles."""
    lam, mu = cycle_type
    n = sum(lam) + sum(mu)
    window = list(range(1, n + 1))
    cursor = 1
    for length, negative in [(x, False) for x in lam] + [(x, True) for x in mu]:
        cycle = list(range(cursor, cursor + length))
        for a, b in zip(cycle, cycle[1:]):
            window[a - 1] = b
        window[cycle[-1] - 1] = -cycle[0] if negative else cycle[0]
        cursor += length
    return tuple(window)


def classify(window: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    n = len(window)
    seen: set[int] = set()
    positive: list[int] = []
    negative: list[int] = []
    for start in range(1, n + 1):
        if start in seen:
            continue
        here = start
        sign = 1
        length = 0
        while here not in seen:
            seen.add(here)
            image = window[here - 1]
            sign *= 1 if image > 0 else -1
            here = abs(image)
            length += 1
        (positive if sign == 1 else negative).append(length)
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Window of left o right."""
    return tuple((1 if x > 0 else -1) * left[abs(x) - 1] for x in right)


def reflections(n: int) -> Iterable[tuple[int, ...]]:
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for sign in (1, -1):
                window = list(range(1, n + 1))
                window[i - 1] = sign * j
                window[j - 1] = sign * i
                yield tuple(window)


def rank_of(cycle_type: tuple[tuple[int, ...], tuple[int, ...]], n: int) -> int:
    return n - len(cycle_type[0])


def quotient_data(n: int):
    types = signed_cycle_types(n)
    type_set = set(types)
    sizes = {t: orbit_size(n, t) for t in types}
    ranks = {t: rank_of(t, n) for t in types}
    adjacency: dict[tuple[tuple[int, ...], tuple[int, ...]], Counter] = {
        t: Counter() for t in types
    }
    ref_list = list(reflections(n))
    for t in types:
        w = representative(t)
        assert classify(w) == t
        assert sum(x < 0 for x in w) % 2 == 0
        for reflection in ref_list:
            target = classify(compose(w, reflection))
            assert target in type_set
            if ranks[target] == ranks[t] + 1:
                adjacency[t][target] += 1
    rank_sizes = [sum(sizes[t] for t in types if ranks[t] == r) for r in range(n + 1)]
    expected_order = (2 ** (n - 1)) * math.factorial(n)
    assert sum(rank_sizes) == expected_order
    return types, sizes, ranks, adjacency, rank_sizes


@dataclass
class Arc:
    to: int
    rev: int
    cap: int
    original: int


class Dinic:
    def __init__(self, count: int):
        self.graph: list[list[Arc]] = [[] for _ in range(count)]

    def add(self, source: int, target: int, capacity: int) -> tuple[int, int]:
        forward = Arc(target, len(self.graph[target]), capacity, capacity)
        backward = Arc(source, len(self.graph[source]), 0, 0)
        self.graph[source].append(forward)
        self.graph[target].append(backward)
        return source, len(self.graph[source]) - 1

    def max_flow(self, source: int, sink: int) -> int:
        answer = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = deque([source])
            while queue:
                v = queue.popleft()
                for edge in self.graph[v]:
                    if edge.cap and level[edge.to] < 0:
                        level[edge.to] = level[v] + 1
                        queue.append(edge.to)
            if level[sink] < 0:
                return answer
            next_edge = [0] * len(self.graph)

            def send(v: int, pushed: int) -> int:
                if v == sink:
                    return pushed
                while next_edge[v] < len(self.graph[v]):
                    edge = self.graph[v][next_edge[v]]
                    if edge.cap and level[edge.to] == level[v] + 1:
                        amount = send(edge.to, min(pushed, edge.cap))
                        if amount:
                            edge.cap -= amount
                            self.graph[edge.to][edge.rev].cap += amount
                            return amount
                    next_edge[v] += 1
                return 0

            while True:
                pushed = send(source, 10**200)
                if not pushed:
                    break
                answer += pushed


def type_id(cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> str:
    lam, mu = cycle_type
    left = ",".join(map(str, lam)) or "-"
    right = ",".join(map(str, mu)) or "-"
    return f"{left}|{right}"


def layer_flow(n: int, rank: int, types, sizes, ranks, adjacency, rank_sizes):
    left = [t for t in types if ranks[t] == rank]
    right = [t for t in types if ranks[t] == rank + 1]
    left_total, right_total = rank_sizes[rank], rank_sizes[rank + 1]
    scale = math.lcm(left_total, right_total)
    source = 0
    left_vertex = {t: i + 1 for i, t in enumerate(left)}
    right_vertex = {t: i + 1 + len(left) for i, t in enumerate(right)}
    sink = 1 + len(left) + len(right)
    network = Dinic(sink + 1)
    for t in left:
        network.add(source, left_vertex[t], sizes[t] * (scale // left_total))
    for t in right:
        network.add(right_vertex[t], sink, sizes[t] * (scale // right_total))
    handles = {}
    for a in left:
        for b in sorted(adjacency[a]):
            handles[(a, b)] = network.add(left_vertex[a], right_vertex[b], scale)
    value = network.max_flow(source, sink)
    if value != scale:
        reachable = {source}
        queue = deque([source])
        while queue:
            v = queue.popleft()
            for edge in network.graph[v]:
                if edge.cap and edge.to not in reachable:
                    reachable.add(edge.to)
                    queue.append(edge.to)
        return None, {
            "rank": rank,
            "max_flow": value,
            "required": scale,
            "reachable_left": [type_id(t) for t in left if left_vertex[t] in reachable],
            "reachable_right": [type_id(t) for t in right if right_vertex[t] in reachable],
        }
    flows = []
    for (a, b), (v, edge_index) in handles.items():
        edge = network.graph[v][edge_index]
        used = edge.original - edge.cap
        if used:
            value_q = Fraction(used, scale)
            degree_from = adjacency[a][b]
            edge_count = sizes[a] * degree_from
            assert edge_count % sizes[b] == 0
            edge_value = value_q / edge_count
            flows.append({
                "from": type_id(a),
                "to": type_id(b),
                "numerator": value_q.numerator,
                "denominator": value_q.denominator,
                "degree_from": degree_from,
                "degree_to": edge_count // sizes[b],
                "edge_count": edge_count,
                "edge_numerator": edge_value.numerator,
                "edge_denominator": edge_value.denominator,
            })
    return flows, None


def discover(n: int):
    types, sizes, ranks, adjacency, rank_sizes = quotient_data(n)
    layers = []
    failure = None
    for rank in range(n):
        flow, cut = layer_flow(n, rank, types, sizes, ranks, adjacency, rank_sizes)
        if flow is None:
            failure = cut
            break
        layers.append({"rank": rank, "flows": flow})
    return {
        "schema_version": 1,
        "claim": f"Abs(D_{n}) admits a normalized flow with unit vertex weights",
        "n": n,
        "quotient_action": f"conjugation by B_{n} on D_{n}",
        "orbit_encoding": "positive_partition|negative_partition; negative partition has even length",
        "orbit_count": len(types),
        "rank_sizes": rank_sizes,
        "rank_orbit_counts": [sum(ranks[t] == r for t in types) for r in range(n + 1)],
        "status": "feasible" if failure is None else "infeasible",
        "layers": layers,
        "failure_cut": failure,
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "algorithm": "integer Dinic max-flow; deterministic; no random seed",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.n < 4:
        raise SystemExit("D_n is requested only for n >= 4")
    result = discover(args.n)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("n", "orbit_count", "rank_sizes", "rank_orbit_counts", "status")}))
    return 0 if result["status"] == "feasible" else 1


if __name__ == "__main__":
    raise SystemExit(main())
