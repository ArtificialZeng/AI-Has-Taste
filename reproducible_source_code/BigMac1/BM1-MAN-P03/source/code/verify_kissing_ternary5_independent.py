#!/usr/bin/env python3
"""Independent list-based exact check of the ternary 5D clique number."""

from itertools import product
import networkx as nx


def weight(v):
    return sum(x * x for x in v)


def compatible(u, v):
    dot = sum(x * y for x, y in zip(u, v))
    return dot <= 0 or 4 * dot * dot <= weight(u) * weight(v)


def main():
    vertices = [v for v in product((-1, 0, 1), repeat=5) if any(v)]
    graph = nx.Graph()
    graph.add_nodes_from(range(len(vertices)))
    graph.add_edges_from(
        (i, j)
        for i, u in enumerate(vertices)
        for j, v in enumerate(vertices[:i])
        if compatible(u, v)
    )
    clique, size = nx.max_weight_clique(graph, weight=None)
    if size != 40:
        raise RuntimeError(f"independent maximum-clique check returned {size}")
    if not all(weight(vertices[i]) == 2 for i in clique):
        raise RuntimeError("independent verifier found a non-D5 incumbent")
    print("INDEPENDENT VERIFIED: clique number = 40; incumbent = D5")


if __name__ == "__main__":
    main()
