#!/usr/bin/env python3
"""Exact connected-graph and acyclic-orientation atlas through six vertices.

This generator uses two exhaustive constructions for its decisive checks:

* all labelled simple graphs, quotiented by every vertex permutation, and
* all edge-orientation masks, checked by Kahn elimination, compared with the
  set of orientations induced by all vertex orders.

The output is deterministic JSON.  A bit-vector character in position i is 0
when edge i is directed from its smaller to its larger endpoint and 1 when it
is reversed.  Edges are in Python lexicographic order.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import permutations
import json
from pathlib import Path

import networkx as nx


ORDERS = range(2, 7)


def g6_pairs(n: int) -> list[tuple[int, int]]:
    """Pairs in graph6 bit order."""
    return [(i, j) for j in range(1, n) for i in range(j)]


def lex_pairs(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def connected(n: int, mask: int, pairs: list[tuple[int, int]]) -> bool:
    adjacency = [0] * n
    for k, (u, v) in enumerate(pairs):
        if (mask >> k) & 1:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    reached = 1
    frontier = 1
    while frontier:
        neighbors = 0
        for u in range(n):
            if (frontier >> u) & 1:
                neighbors |= adjacency[u]
        frontier = neighbors & ~reached
        reached |= frontier
    return reached == (1 << n) - 1


def permutation_maps(n: int) -> list[tuple[int, ...]]:
    """For each new-label -> old-label permutation, map new g6 bits to old."""
    pairs = g6_pairs(n)
    index = {edge: k for k, edge in enumerate(pairs)}
    maps = []
    for perm in permutations(range(n)):
        mapping = []
        for u, v in pairs:
            a, b = sorted((perm[u], perm[v]))
            mapping.append(index[(a, b)])
        maps.append(tuple(mapping))
    return maps


def relabel(mask: int, mapping: tuple[int, ...]) -> int:
    out = 0
    for new_k, old_k in enumerate(mapping):
        out |= ((mask >> old_k) & 1) << new_k
    return out


def canonical_key(mask: int, bit_count: int) -> tuple[int, ...]:
    """Lexicographic graph6 adjacency-bit key (first bit is most important)."""
    return tuple((mask >> k) & 1 for k in range(bit_count))


def graph6_string(n: int, mask: int) -> str:
    bits = [(mask >> k) & 1 for k in range(n * (n - 1) // 2)]
    while len(bits) % 6:
        bits.append(0)
    chars = [chr(n + 63)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        chars.append(chr(value + 63))
    return "".join(chars)


def canonical_classes(n: int) -> tuple[list[int], int]:
    """Generate all connected labelled graphs and quotient exact S_n orbits."""
    pairs = g6_pairs(n)
    maps = permutation_maps(n)
    seen: set[int] = set()
    canonical: list[int] = []
    connected_labelled = 0
    for mask in range(1 << len(pairs)):
        if not connected(n, mask, pairs):
            continue
        connected_labelled += 1
        if mask in seen:
            continue
        orbit = {relabel(mask, mapping) for mapping in maps}
        seen.update(orbit)
        canonical.append(min(orbit, key=lambda x: canonical_key(x, len(pairs))))
    canonical.sort(key=lambda x: graph6_string(n, x))
    assert len(seen) == connected_labelled
    return canonical, connected_labelled


def mask_to_graph(n: int, mask: int) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(
        edge for k, edge in enumerate(g6_pairs(n)) if (mask >> k) & 1
    )
    return graph


def canonical_graph6_nx(graph: nx.Graph) -> str:
    values = []
    nodes = list(graph.nodes())
    for perm in permutations(nodes):
        mapping = {perm[i]: i for i in range(len(perm))}
        # Construct afresh because graph6 conversion follows node insertion
        # order; relabel_nodes alone retains the old insertion order.
        relabelled = nx.Graph()
        relabelled.add_nodes_from(range(len(perm)))
        relabelled.add_edges_from((mapping[u], mapping[v]) for u, v in graph.edges())
        values.append(nx.to_graph6_bytes(relabelled, header=False).decode().strip())
    return min(values)


def is_acyclic_kahn(n: int, edges: list[tuple[int, int]], mask: int) -> bool:
    out = [[] for _ in range(n)]
    indegree = [0] * n
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            u, v = v, u
        out[u].append(v)
        indegree[v] += 1
    stack = [u for u in range(n) if indegree[u] == 0]
    removed = 0
    while stack:
        u = stack.pop()
        removed += 1
        for v in out[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)
    return removed == n


def order_induced_orientations(n: int, edges: list[tuple[int, int]]) -> set[int]:
    orientations: set[int] = set()
    for order in permutations(range(n)):
        position = {v: i for i, v in enumerate(order)}
        mask = 0
        for i, (u, v) in enumerate(edges):
            if position[v] < position[u]:
                mask |= 1 << i
        orientations.add(mask)
    return orientations


def bit_vector(mask: int, width: int) -> str:
    return "".join(str((mask >> i) & 1) for i in range(width))


def graph_record(graph6: str, graph: nx.Graph) -> dict:
    n = graph.number_of_nodes()
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    m = len(edges)
    by_masks = {
        mask for mask in range(1 << m) if is_acyclic_kahn(n, edges, mask)
    }
    by_orders = order_induced_orientations(n, edges)
    assert by_masks == by_orders
    orientations = sorted(by_masks)
    vectors = [bit_vector(mask, m) for mask in orientations]
    aset = set(orientations)
    flip_edges = []
    for mask in orientations:
        for i in range(m):
            other = mask ^ (1 << i)
            if mask < other and other in aset:
                flip_edges.append([bit_vector(mask, m), bit_vector(other, m)])
    signed_signature = sum((-1) ** mask.bit_count() for mask in orientations)
    return {
        "graph6": graph6,
        "order": n,
        "edges": [list(edge) for edge in edges],
        "edge_count": m,
        "orientation_bit_vectors": vectors,
        "acyclic_orientation_count": len(vectors),
        "flip_edges": flip_edges,
        "flip_edge_count": len(flip_edges),
        "signed_signature_for_base_orientation": signed_signature,
        "sigma": abs(signed_signature),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    all_graph6: list[str] = []
    class_counts = {}
    labelled_counts = {}
    for n in ORDERS:
        masks, labelled_count = canonical_classes(n)
        identifiers = [graph6_string(n, mask) for mask in masks]
        assert len(identifiers) == len(set(identifiers))
        all_graph6.extend(identifiers)
        class_counts[str(n)] = len(identifiers)
        labelled_counts[str(n)] = labelled_count

    atlas_graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if 2 <= graph.number_of_nodes() <= 6 and nx.is_connected(graph)
    ]
    atlas_graph6 = {canonical_graph6_nx(graph) for graph in atlas_graphs}
    assert set(all_graph6) == atlas_graph6
    assert len(all_graph6) == len(set(all_graph6)) == len(atlas_graphs)

    records = []
    for identifier in sorted(all_graph6, key=lambda s: (ord(s[0]) - 63, s)):
        graph = nx.from_graph6_bytes(identifier.encode())
        records.append(graph_record(identifier, graph))

    sigma_zero_counts = Counter(
        record["order"] for record in records if record["sigma"] == 0
    )
    sigma_nonzero_counts = Counter(
        record["order"] for record in records if record["sigma"] != 0
    )
    payload = {
        "metadata": {
            "software": {"python": "3", "networkx": nx.__version__},
            "orders": list(ORDERS),
            "canonical_identifier": "lexicographically least graph6 string over all vertex permutations",
            "edge_order": "lexicographic pairs (u,v) with u<v",
            "orientation_bits": "character i is 0 for u->v on edge i=(u,v), and 1 for v->u",
            "domain_method": "all 2^(n choose 2) labelled graphs; connectedness; exact S_n orbits",
            "domain_cross_check": "canonicalized connected NetworkX graph_atlas_g entries",
            "orientation_method": "all 2^m masks with Kahn acyclicity test",
            "orientation_cross_check": "distinct orientations induced by all n! vertex orders",
        },
        "summary": {
            "connected_unlabelled_counts": class_counts,
            "connected_labelled_counts": labelled_counts,
            "total_graphs": len(records),
            "sigma_zero_counts": {
                str(n): sigma_zero_counts[n] for n in ORDERS
            },
            "sigma_nonzero_counts": {
                str(n): sigma_nonzero_counts[n] for n in ORDERS
            },
            "total_acyclic_orientations": sum(
                record["acyclic_orientation_count"] for record in records
            ),
            "total_flip_edges": sum(record["flip_edge_count"] for record in records),
        },
        "graphs": records,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
