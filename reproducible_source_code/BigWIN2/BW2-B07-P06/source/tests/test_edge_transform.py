#!/usr/bin/env python3
"""Exact regression checks for the proposed two-vertex-component transform."""

from __future__ import annotations

import json
import math
import pathlib
import sys

import networkx as nx

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from csf_subset import csf_power_sum
from graph6_utils import parse_graph6, unicyclic_decomposition


def lhs(graph6: bytes) -> list[int]:
    n, _adj, _edges = parse_graph6(graph6)
    coefficients = csf_power_sum(graph6)
    result = []
    for b in range(n + 1):
        q = n - b
        value = 0
        for partition, coefficient in coefficients.items():
            top = n - len(partition)
            choose = math.comb(top, q) if 0 <= q <= top else 0
            value += (-1) ** q * coefficient * partition.count(2) * choose
        result.append(value)
    return result


def rhs(graph6: bytes) -> list[int]:
    n, adj, edges = parse_graph6(graph6)
    cycle, cycle_set, _parent, _order = unicyclic_decomposition(adj)
    result = [0] * (n + 1)
    for u, v in edges:
        degree_index = len(adj[u]) + len(adj[v]) - 2
        if u in cycle_set or v in cycle_set:
            result[degree_index] += 1
            result[degree_index + 1] -= 1
        else:
            result[degree_index] += 1
            result[degree_index + 1] -= 1
            for j in range(len(cycle) + 1):
                result[degree_index + j] -= (
                    (-1) ** j * math.comb(len(cycle), j)
                )
    return result


def main() -> None:
    encodings = []
    for c in range(3, 9):
        cycle = nx.cycle_graph(c)
        encodings.append(nx.to_graph6_bytes(cycle, header=False).strip())
        cycle.add_edge(0, c)
        encodings.append(nx.to_graph6_bytes(cycle, header=False).strip())
        cycle.add_edge(c, c + 1)
        encodings.append(nx.to_graph6_bytes(cycle, header=False).strip())
    known = json.load(open(ROOT / "experiments/run_n14/candidates.json", encoding="utf-8"))
    encodings.extend(
        [
            known["candidates"][0]["graph6_a"].encode(),
            known["candidates"][0]["graph6_b"].encode(),
        ]
    )
    for graph6 in encodings:
        assert lhs(graph6) == rhs(graph6), graph6
    print(f"PASS edge-transform identity on {len(encodings)} exact unicyclic examples")


if __name__ == "__main__":
    main()
