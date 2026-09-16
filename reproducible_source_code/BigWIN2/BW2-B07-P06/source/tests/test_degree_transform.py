#!/usr/bin/env python3
"""Exact regression checks for equation (1) in proof/degree_transform.md."""

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
            value += (-1) ** q * coefficient * partition.count(1) * choose
        result.append(value)
    return result


def rhs(graph6: bytes) -> list[int]:
    n, adj, _edges = parse_graph6(graph6)
    cycle, cycle_set, _parent, _order = unicyclic_decomposition(adj)
    result = [0] * (n + 1)
    for vertex in range(n):
        degree = len(adj[vertex])
        if vertex in cycle_set:
            result[degree] += 1
        else:
            for j in range(1, len(cycle)):
                result[degree + j] += (
                    (-1) ** (j + 1) * math.comb(len(cycle) - 1, j)
                )
    return result


def main() -> None:
    encodings = []
    for c in range(3, 9):
        cycle = nx.cycle_graph(c)
        encodings.append(nx.to_graph6_bytes(cycle, header=False).strip())
        cycle.add_edge(0, c)
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
    print(f"PASS degree-transform identity on {len(encodings)} exact unicyclic examples")


if __name__ == "__main__":
    main()
