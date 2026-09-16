#!/usr/bin/env python3
"""Reconstruct and audit the graph fixed in problem.md; does not solve the game."""

import networkx as nx


def graph():
    g = nx.Graph()
    g.add_nodes_from((m, i) for m in range(4) for i in range(3))
    g.add_node("omega")
    g.add_edges_from(((0, i), (0, j)) for i in range(3) for j in range(i + 1, 3))
    g.add_edges_from(
        ((m, i), (m + 1, j))
        for m in range(3)
        for i in range(3)
        for j in range(3)
        if i != j
    )
    g.add_edges_from(((3, i), "omega") for i in range(3))
    return g


def main():
    g = graph()
    automorphisms = sum(
        1 for _ in nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter()
    )
    print(f"vertices {g.number_of_nodes()}")
    print(f"edges {g.number_of_edges()}")
    print(f"degree_multiset {sorted(dict(g.degree()).values())}")
    print(f"connected {nx.is_connected(g)}")
    print(f"clique_number {max(map(len, nx.find_cliques(g)))}")
    print(f"automorphisms {automorphisms}")


if __name__ == "__main__":
    main()
