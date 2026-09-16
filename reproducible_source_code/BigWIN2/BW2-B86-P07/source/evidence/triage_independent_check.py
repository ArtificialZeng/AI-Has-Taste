#!/usr/bin/env python3
"""Independent explicit-bijection cross-check for the T* triage counts."""

from itertools import combinations, permutations
from math import comb


VERTICES = tuple(range(5))
PAIRS = tuple(combinations(VERTICES, 2))
TSTAR = frozenset({(0, 1), (0, 2), (0, 3), (3, 4)})
BIJECTIONS = tuple(permutations(VERTICES))


def edge(u, v):
    return (u, v) if u < v else (v, u)


def image(graph, bijection):
    return frozenset(edge(bijection[u], bijection[v]) for u, v in graph)


def embeds(graph_a, graph_b):
    return any(image(graph_a, bijection) <= graph_b for bijection in BIJECTIONS)


def induced_graph(vertices, global_edges):
    position = {vertex: index for index, vertex in enumerate(vertices)}
    return frozenset(
        edge(position[u], position[v])
        for u, v in global_edges
        if u in position and v in position
    )


def main():
    copies = {image(TSTAR, bijection) for bijection in BIJECTIONS}
    forbidden = []
    for bits in range(1 << len(PAIRS)):
        graph = frozenset(pair for index, pair in enumerate(PAIRS) if bits >> index & 1)
        comparable = embeds(graph, TSTAR) or embeds(TSTAR, graph)
        if comparable and graph not in copies:
            forbidden.append(graph)

    two_k4_edges = frozenset(
        pair
        for component in (range(4), range(4, 8))
        for pair in combinations(component, 2)
    )
    induced = [
        induced_graph(vertices, two_k4_edges)
        for vertices in combinations(range(8), 5)
    ]
    legal = sum(
        graph in copies or not (embeds(graph, TSTAR) or embeds(TSTAR, graph))
        for graph in induced
    )

    assert len(copies) == 60
    assert len(forbidden) == 757
    assert legal == comb(8, 5) == 56
    print("method=explicit edge sets and exhaustive bijection search")
    print(f"labeled_tstar_copies={len(copies)}")
    print(f"forbidden_comparable_nonisomorphic_patterns={len(forbidden)}")
    print(f"full_encoding_clauses={comb(9, 5) * len(forbidden)}")
    print(f"two_k4_legal_five_sets={legal}")


if __name__ == "__main__":
    main()
