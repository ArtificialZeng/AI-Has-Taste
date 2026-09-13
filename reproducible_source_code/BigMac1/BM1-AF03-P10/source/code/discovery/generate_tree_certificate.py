#!/usr/bin/env python3
"""Discovery-side enumeration for the Lotka--Volterra tree certificate.

This program may use NetworkX.  The independent verifier deliberately does
not import this file or NetworkX and instead enumerates all labelled trees
from Prüfer words.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from collections import Counter, deque
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / "certificates" / "trees_n2_n9.json"
MANIFEST = ROOT / "experiments" / "discovery_manifest.json"


def canonical_tree_code(edges: list[tuple[int, int]], n: int) -> str:
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)

    degree = [len(x) for x in adjacency]
    leaves = deque(i for i, d in enumerate(degree) if d <= 1)
    remaining = n
    while remaining > 2:
        layer = len(leaves)
        remaining -= layer
        for _ in range(layer):
            leaf = leaves.popleft()
            degree[leaf] = 0
            for neighbour in adjacency[leaf]:
                if degree[neighbour] > 0:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        leaves.append(neighbour)
    centres = sorted(set(leaves))
    if n == 1:
        centres = [0]

    def rooted(vertex: int, parent: int) -> str:
        children = sorted(
            rooted(neighbour, vertex)
            for neighbour in adjacency[vertex]
            if neighbour != parent
        )
        return "(" + "".join(children) + ")"

    if len(centres) == 1:
        return "C" + rooted(centres[0], -1)
    if len(centres) == 2:
        left = rooted(centres[0], centres[1])
        right = rooted(centres[1], centres[0])
        return "B" + "".join(sorted((left, right)))
    raise ValueError("input is not a nonempty tree")


def triangle_reconstruction_code(edges: list[tuple[int, int]], n: int) -> str:
    """Reconstruct T from the 3-circuits of the cone-incidence configuration."""

    if n == 2:
        return canonical_tree_code([(0, 1)], 2)

    triples = [(u, v, n + index) for index, (u, v) in enumerate(edges)]
    incidence_degree = Counter(item for triple in triples for item in triple)
    internal = {item for item, degree in incidence_degree.items() if degree >= 2}
    internal_order = {item: index for index, item in enumerate(sorted(internal))}
    reconstructed_edges: list[tuple[int, int]] = []
    next_leaf = len(internal_order)
    for triple in triples:
        core = sorted(item for item in triple if item in internal)
        if len(core) == 2:
            reconstructed_edges.append(
                (internal_order[core[0]], internal_order[core[1]])
            )
        elif len(core) == 1:
            reconstructed_edges.append((internal_order[core[0]], next_leaf))
            next_leaf += 1
        else:
            raise ValueError("a tree of order at least three has no leaf--leaf edge")
    if next_leaf != n:
        raise ValueError("triangle reconstruction has the wrong number of vertices")
    return canonical_tree_code(reconstructed_edges, n)


def cycle_incidence_signature(edges: list[tuple[int, int]], n: int) -> list[list[list[int]]]:
    """Matroid invariant: per-element counts of circuits of every size."""

    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for edge_index, (u, v) in enumerate(edges):
        adjacency[u].append((v, edge_index))
        adjacency[v].append((u, edge_index))
    profiles = [Counter() for _ in range(2 * n - 1)]
    for source in range(n):
        parent: list[tuple[int, int] | None] = [None] * n
        parent[source] = (-1, -1)
        stack = [source]
        while stack:
            vertex = stack.pop()
            for neighbour, edge_index in adjacency[vertex]:
                if parent[neighbour] is None:
                    parent[neighbour] = (vertex, edge_index)
                    stack.append(neighbour)
        for target in range(source + 1, n):
            path_edges = []
            vertex = target
            while vertex != source:
                step = parent[vertex]
                if step is None:
                    raise ValueError("disconnected tree")
                vertex, edge_index = step
                path_edges.append(edge_index)
            circuit = [source, target] + [n + index for index in path_edges]
            size = len(circuit)
            for element in circuit:
                profiles[element][size] += 1
    return sorted(
        [[[size, count] for size, count in sorted(profile.items())] for profile in profiles]
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    orders = []
    expected_counts = {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23, 9: 47}
    for n in range(2, 10):
        rows = []
        for tree in nx.nonisomorphic_trees(n):
            edges = sorted(tuple(sorted(edge)) for edge in tree.edges())
            code = canonical_tree_code(edges, n)
            rows.append(
                {
                    "canonical_code": code,
                    "cycle_incidence_signature": cycle_incidence_signature(edges, n),
                    "degree_sequence": sorted(dict(tree.degree()).values()),
                    "edges": [list(edge) for edge in edges],
                    "reconstruction_code": triangle_reconstruction_code(edges, n),
                }
            )
        rows.sort(key=lambda row: row["canonical_code"])
        if len(rows) != expected_counts[n]:
            raise RuntimeError(f"unexpected order-{n} count")
        if len({row["canonical_code"] for row in rows}) != len(rows):
            raise RuntimeError(f"duplicate canonical tree at order {n}")
        for index, row in enumerate(rows, start=1):
            row["id"] = f"n{n}_t{index:03d}"
            if row["canonical_code"] != row["reconstruction_code"]:
                raise RuntimeError(f"triangle reconstruction failed for {row['id']}")
        orders.append(
            {
                "expected_unlabeled_count": expected_counts[n],
                "n": n,
                "trees": rows,
            }
        )

    payload = {
        "endpoint": "all unlabeled simple trees of orders 2 through 9",
        "exact_arithmetic": True,
        "orders": orders,
        "schema_version": 1,
    }
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    manifest = {
        "certificate": str(CERTIFICATE.relative_to(ROOT)),
        "certificate_sha256": sha256(CERTIFICATE),
        "command": "python code/discovery/generate_tree_certificate.py",
        "evaluator": "NetworkX nonisomorphic_trees plus AHU canonical codes",
        "networkx": nx.__version__,
        "objective_convention": "projective 3-circuit hypergraph reconstruction",
        "parameters": {"max_order": 9, "min_order": 2},
        "platform": platform.platform(),
        "python": sys.version,
        "seed": None,
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"certificate_sha256": manifest["certificate_sha256"], "counts": expected_counts}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
