#!/usr/bin/env python3
"""Exact screen of the NetworkX Graph Atlas for the M_3(4) problem.

The Atlas contains one representative of every simple graph on at most seven
vertices.  We retain connected legal graphs, construct their B-conflict
graphs, and compute chromatic numbers by exact DSATUR-style backtracking.
"""

import itertools

import networkx as nx


def is_legal(graph):
    if len(graph) == 0 or not nx.is_connected(graph):
        return False
    if max(dict(graph.degree()).values(), default=0) > 4:
        return False
    if max(nx.core_number(graph).values(), default=0) > 3:
        return False
    for triple in itertools.combinations(graph.nodes(), 3):
        common = set(graph.neighbors(triple[0]))
        common &= set(graph.neighbors(triple[1]))
        common &= set(graph.neighbors(triple[2]))
        if len(common) >= 4:
            return False
    return True


def conflict_graph(graph):
    edges = [tuple(sorted(edge)) for edge in graph.edges()]
    conflict = nx.Graph()
    conflict.add_nodes_from(range(len(edges)))
    for i, (u, v) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            x, y = edges[j]
            incident = len({u, v, x, y}) < 4
            opposite = (
                graph.has_edge(u, x) and graph.has_edge(v, y)
            ) or (
                graph.has_edge(u, y) and graph.has_edge(v, x)
            )
            if incident or opposite:
                conflict.add_edge(i, j)
    return conflict, edges


def is_k_colorable(graph, k):
    colors = {v: -1 for v in graph}
    saturation = {v: 0 for v in graph}
    degrees = dict(graph.degree())

    def search(colored):
        if colored == len(graph):
            return True
        uncolored = [v for v in graph if colors[v] < 0]
        v = max(
            uncolored,
            key=lambda x: (saturation[x].bit_count(), degrees[x]),
        )
        forbidden = saturation[v]
        for color in range(k):
            bit = 1 << color
            if forbidden & bit:
                continue
            colors[v] = color
            changed = []
            for neighbor in graph[v]:
                if colors[neighbor] < 0 and not saturation[neighbor] & bit:
                    changed.append((neighbor, saturation[neighbor]))
                    saturation[neighbor] |= bit
            if search(colored + 1):
                return True
            for neighbor, old_value in changed:
                saturation[neighbor] = old_value
            colors[v] = -1
        return False

    return search(0)


def chromatic_number(graph):
    if len(graph) == 0:
        return 0
    lower = max(map(len, nx.find_cliques(graph)))
    greedy = nx.coloring.greedy_color(
        graph, strategy="saturation_largest_first"
    )
    upper = max(greedy.values()) + 1
    for k in range(lower, upper + 1):
        if is_k_colorable(graph, k):
            return k
    raise AssertionError("greedy coloring did not give an upper bound")


def main():
    histogram = {}
    count = 0
    best = (-1, None, None, None)
    for graph in nx.graph_atlas_g():
        if len(graph) > 7 or not is_legal(graph):
            continue
        count += 1
        conflict, edges = conflict_graph(graph)
        q_b = chromatic_number(conflict)
        histogram[q_b] = histogram.get(q_b, 0) + 1
        if q_b > best[0]:
            best = (q_b, graph.copy(), conflict.copy(), edges)

    q_b, graph, conflict, edges = best
    print("networkx", nx.__version__)
    print("legal_connected_graphs", count)
    print("qB_histogram", sorted(histogram.items()))
    print(
        "first_maximizer",
        "qB", q_b,
        "n", len(graph),
        "m", graph.number_of_edges(),
        "graph6", nx.to_graph6_bytes(graph, header=False).decode().strip(),
    )
    print("edges", sorted(edges))
    print("conflict_order_size", len(conflict), conflict.number_of_edges())


if __name__ == "__main__":
    main()
