#!/usr/bin/env python3
"""Cross-check the two exact evaluators and the DP evaluation on small graphs."""

from __future__ import annotations

import pathlib
import sys

import networkx as nx

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from csf_delete_contract import csf_power_sum as dc_csf
from csf_hash_search import coloring_evaluation, evaluate_record
from csf_subset import csf_power_sum as subset_csf


def graph6(graph: nx.Graph) -> bytes:
    return nx.to_graph6_bytes(graph, header=False).strip()


def evaluate_from_power_sum(coefficients, values, modulus):
    total = 0
    power_sums = {part: sum(pow(x, part, modulus) for x in values) % modulus for part in range(1, 20)}
    for partition, coefficient in coefficients.items():
        term = coefficient % modulus
        for part in partition:
            term = term * power_sums[part] % modulus
        total = (total + term) % modulus
    return total


def check(graph: nx.Graph) -> None:
    encoded = graph6(graph)
    a = subset_csf(encoded)
    b = dc_csf(encoded)
    assert a == b
    evaluated = evaluate_record(encoded)
    n, adj, cycle, cycle_set, parent, order, _data, _primary = evaluated
    values = tuple(range(1, n + 1))
    modulus = 1_000_000_007
    dp = coloring_evaluation(adj, cycle, cycle_set, parent, order, values, modulus)
    direct = evaluate_from_power_sum(a, values, modulus)
    assert dp == direct


def main() -> None:
    for n in range(3, 9):
        check(nx.cycle_graph(n))
        graph = nx.cycle_graph(n)
        graph.add_node(n)
        graph.add_edge(0, n)
        check(graph)
    print("PASS exact subset = weighted deletion-contraction = coloring DP on 12 small unicyclic graphs")


if __name__ == "__main__":
    main()
