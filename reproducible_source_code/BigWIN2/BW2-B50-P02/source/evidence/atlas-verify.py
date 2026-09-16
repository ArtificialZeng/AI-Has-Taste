#!/usr/bin/env python3
"""Independent replay checks for atlas-enumerate.py's JSON artifact."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path

import networkx as nx


def canonical_graph6(graph: nx.Graph) -> str:
    nodes = list(graph.nodes())
    encodings = []
    for order in permutations(nodes):
        mapping = {order[i]: i for i in range(len(nodes))}
        relabelled = nx.Graph()
        relabelled.add_nodes_from(range(len(nodes)))
        relabelled.add_edges_from((mapping[u], mapping[v]) for u, v in graph.edges())
        encodings.append(nx.to_graph6_bytes(relabelled, header=False).decode().strip())
    return min(encodings)


def vector(mask: int, width: int) -> str:
    return "".join(str((mask >> i) & 1) for i in range(width))


def orientations_networkx(graph: nx.Graph, edges: list[tuple[int, int]]) -> set[int]:
    answer = set()
    for mask in range(1 << len(edges)):
        digraph = nx.DiGraph()
        digraph.add_nodes_from(graph.nodes())
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                u, v = v, u
            digraph.add_edge(u, v)
        if nx.is_directed_acyclic_graph(digraph):
            answer.add(mask)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("atlas", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.atlas.read_text())
    records = payload["graphs"]

    identifiers = [record["graph6"] for record in records]
    assert len(identifiers) == len(set(identifiers)) == 142
    counts = Counter(record["order"] for record in records)
    assert counts == Counter({2: 1, 3: 2, 4: 6, 5: 21, 6: 112})

    atlas_set = {
        canonical_graph6(graph)
        for graph in nx.graph_atlas_g()
        if 2 <= graph.number_of_nodes() <= 6 and nx.is_connected(graph)
    }
    assert set(identifiers) == atlas_set

    # Pairwise isomorphism rejection is deliberately separate from identifier
    # uniqueness, so a canonical-encoding bug cannot silently certify both.
    for n in range(2, 7):
        same_order = [
            nx.from_graph6_bytes(record["graph6"].encode())
            for record in records
            if record["order"] == n
        ]
        for left, right in combinations(same_order, 2):
            assert not nx.is_isomorphic(left, right)

    sigma_zero = Counter()
    sigma_nonzero = Counter()
    sigma_values = Counter()
    total_orientations = 0
    total_flips = 0
    for record in records:
        graph = nx.from_graph6_bytes(record["graph6"].encode())
        assert nx.is_connected(graph)
        assert graph.number_of_nodes() == record["order"]
        assert canonical_graph6(graph) == record["graph6"]
        edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
        assert [list(edge) for edge in edges] == record["edges"]
        aset = orientations_networkx(graph, edges)
        vectors = [vector(mask, len(edges)) for mask in sorted(aset)]
        assert vectors == record["orientation_bit_vectors"]
        flips = []
        for mask in sorted(aset):
            for i in range(len(edges)):
                other = mask ^ (1 << i)
                if mask < other and other in aset:
                    flips.append([vector(mask, len(edges)), vector(other, len(edges))])
        assert flips == record["flip_edges"]
        signed = sum((-1) ** mask.bit_count() for mask in aset)
        assert signed == record["signed_signature_for_base_orientation"]
        assert abs(signed) == record["sigma"]
        total_orientations += len(aset)
        total_flips += len(flips)
        sigma_values[abs(signed)] += 1
        if signed == 0:
            sigma_zero[record["order"]] += 1
        else:
            sigma_nonzero[record["order"]] += 1

    print("verification PASS")
    print("connected_unlabelled", dict(sorted(counts.items())), "total", len(records))
    print("sigma_zero", dict(sorted(sigma_zero.items())), "total", sum(sigma_zero.values()))
    print("sigma_nonzero", dict(sorted(sigma_nonzero.items())), "total", sum(sigma_nonzero.values()))
    print("sigma_value_distribution", dict(sorted(sigma_values.items())))
    print("total_acyclic_orientations", total_orientations)
    print("total_flip_edges", total_flips)
    for n in range(2, 7):
        zero_ids = [
            record["graph6"]
            for record in records
            if record["order"] == n and record["sigma"] == 0
        ]
        print("sigma_zero_graph6", n, len(zero_ids), " ".join(zero_ids))


if __name__ == "__main__":
    main()
