#!/usr/bin/env python3
"""Exact exhaustive verifier for the false independent-2-domination lemma."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import networkx as nx


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", type=Path)
    args = parser.parse_args()
    data = json.loads(args.witness.read_text())
    g = nx.from_graph6_bytes(data["graph6"].encode())
    vertices = list(g.nodes())
    assert vertices == list(range(len(vertices)))
    assert g.number_of_nodes() == data["order"]
    assert g.number_of_edges() == data["size"]
    assert sorted(d for _, d in g.degree()) == data["degree_multiset"]
    assert nx.number_of_selfloops(g) == 0
    assert not any(nx.triangles(g).values())

    coloring = data["proper_3_coloring_in_vertex_order"]
    assert len(coloring) == len(vertices)
    assert set(coloring) == {0, 1, 2}
    assert all(coloring[u] != coloring[v] for u, v in g.edges())
    assert not nx.is_bipartite(g)

    neighborhoods = {v: set(g.neighbors(v)) for v in vertices}
    independent_count = 0
    best_score = -1
    best_set = None
    for mask in range(1 << len(vertices)):
        chosen = {v for v in vertices if (mask >> v) & 1}
        if any(u in chosen and v in chosen for u, v in g.edges()):
            continue
        independent_count += 1
        outside = set(vertices) - chosen
        score = min((len(neighborhoods[v] & chosen) for v in outside), default=99)
        if score > best_score:
            best_score = score
            best_set = sorted(chosen)

    assert independent_count == data["independent_set_count"]
    assert best_score == data["maximum_over_independent_sets_of_minimum_I_neighbor_count_outside_I"]
    assert best_score == 1  # In particular, no independent 2-dominating set exists.
    print(json.dumps({
        "verified": True,
        "order": len(vertices),
        "size": g.number_of_edges(),
        "triangle_free": True,
        "minimum_degree": min(dict(g.degree()).values()),
        "maximum_degree": max(dict(g.degree()).values()),
        "chromatic_number": 3,
        "independent_sets_exhausted": independent_count,
        "best_score": best_score,
        "first_best_set": best_set,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
