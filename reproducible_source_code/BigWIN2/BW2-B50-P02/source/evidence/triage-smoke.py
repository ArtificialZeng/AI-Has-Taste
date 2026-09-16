#!/usr/bin/env python3
"""Small exact boundary/domain checks used at triage; not an atlas solver."""

from collections import Counter
import networkx as nx


def orientation_stats(graph):
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    acyclic = []
    for mask in range(1 << len(edges)):
        digraph = nx.DiGraph()
        digraph.add_nodes_from(graph)
        for i, (u, v) in enumerate(edges):
            digraph.add_edge(*((u, v) if (mask >> i) & 1 else (v, u)))
        if nx.is_directed_acyclic_graph(digraph):
            acyclic.append(mask)
    aset = set(acyclic)
    flip_edges = sum(
        (mask ^ (1 << i)) in aset
        for mask in acyclic
        for i in range(len(edges))
    ) // 2
    signature = abs(sum((-1) ** mask.bit_count() for mask in acyclic))
    return len(edges), len(acyclic), flip_edges, signature


atlas = nx.graph_atlas_g()
counts = Counter(
    graph.number_of_nodes()
    for graph in atlas
    if 2 <= graph.number_of_nodes() <= 6 and nx.is_connected(graph)
)
print("networkx", nx.__version__)
print("domain", dict(sorted(counts.items())), "total", sum(counts.values()))
for name, graph in (
    ("K2", nx.complete_graph(2)),
    ("P3", nx.path_graph(3)),
    ("K3", nx.complete_graph(3)),
    ("C4", nx.cycle_graph(4)),
    ("K6", nx.complete_graph(6)),
):
    print(name, orientation_stats(graph))
