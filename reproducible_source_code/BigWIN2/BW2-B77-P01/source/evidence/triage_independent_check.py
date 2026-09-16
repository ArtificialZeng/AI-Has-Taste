#!/usr/bin/env python3
"""Independent finite sanity check for triage job 04d7940f967d.

NetworkX's VF2 monomorphism routine supplies a second implementation of the
non-induced-copy test.  These finite checks are not the unbounded proof.
"""

import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher


def target_graph():
    graph = nx.Graph()
    graph.add_nodes_from(range(7))
    graph.add_edges_from(((0, 1), (0, 2), (0, 3), (3, 4), (5, 6)))
    return graph


def colour_graphs(m):
    vertices = ("a", "b", *range(m))
    red = nx.Graph()
    blue = nx.Graph()
    red.add_nodes_from(vertices)
    blue.add_nodes_from(vertices)
    red.add_edges_from((apex, i) for apex in ("a", "b") for i in range(m))
    blue.add_edges_from((i, (i + 1) % m) for i in range(m))
    host = nx.compose(red, blue)
    return host, red, blue


def main():
    target = target_graph()
    for m in range(3, 13):
        host, red, blue = colour_graphs(m)
        assert len(host) == m + 2
        assert host.number_of_edges() == 3 * len(host) - 6
        assert nx.check_planarity(host)[0]
        assert not GraphMatcher(red, target).subgraph_is_monomorphic()
        assert not GraphMatcher(blue, target).subgraph_is_monomorphic()
    print(f"NetworkX {nx.__version__}")
    print("PASS: VF2 non-induced monomorphism and planarity checks, m=3..12")


if __name__ == "__main__":
    main()
