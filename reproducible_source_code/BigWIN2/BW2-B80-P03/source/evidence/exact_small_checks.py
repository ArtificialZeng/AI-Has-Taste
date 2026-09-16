#!/usr/bin/env python3
"""Exact finite checks supplementary to evidence/proof.md.

Enumerate all graph-atlas plane triangulations through seven vertices, every
degree-three choice, and every vertex subset in both G and R_v(G).  Toughness
ratios are represented by fractions.  This is not used as an infinite proof.
"""

from fractions import Fraction
from itertools import combinations

import networkx as nx


def components_after(g, removed):
    return nx.number_connected_components(g.subgraph(set(g) - set(removed)))


def exact_toughness(g):
    n = len(g)
    if len(g.edges) == n * (n - 1) // 2:
        return None, []  # infinity
    best = None
    witnesses = []
    vertices = list(g)
    for r in range(n + 1):
        for subset in combinations(vertices, r):
            count = components_after(g, subset)
            if count < 2:
                continue
            ratio = Fraction(r, count)
            if best is None or ratio < best:
                best = ratio
                witnesses = [(tuple(sorted(subset, key=str)), count)]
            elif ratio == best:
                witnesses.append((tuple(sorted(subset, key=str)), count))
    assert best is not None
    return best, witnesses


def replacement(g, v):
    nbrs = list(g.neighbors(v))
    assert len(nbrs) == 3
    assert all(g.has_edge(p, q) for p, q in combinations(nbrs, 2))
    a, b, c = nbrs
    h = g.copy()
    h.remove_node(v)
    x, y, z, w = (f"gadget-{name}" for name in "xyzw")
    h.add_edges_from(combinations((x, y, z, w), 2))
    h.add_edges_from(((x, a), (x, b), (y, b), (y, c), (z, c), (z, a)))
    return h


def is_plane_triangulation(g):
    n = len(g)
    return n >= 3 and nx.is_connected(g) and nx.check_planarity(g)[0] and len(g.edges) == 3 * n - 6


def main():
    tested_graphs = 0
    tested_pairs = 0
    k4_record = None
    for g in nx.graph_atlas_g():
        if not is_plane_triangulation(g):
            continue
        choices = [v for v in g if g.degree(v) == 3]
        if not choices:
            continue
        tested_graphs += 1
        tau_g, _ = exact_toughness(g)
        target = Fraction(3, 2) if tau_g is None else min(tau_g, Fraction(3, 2))
        for v in choices:
            tested_pairs += 1
            h = replacement(g, v)
            tau_h, witnesses_h = exact_toughness(h)
            assert tau_h == target, (g, v, tau_g, tau_h, witnesses_h)
            if len(g) == 4:
                k4_record = (tau_h, witnesses_h)

    assert k4_record is not None
    k4_tau, k4_witnesses = k4_record
    canonical = tuple(sorted(("gadget-x", "gadget-y", "gadget-z"), key=str))
    assert any(s == canonical and count == 2 for s, count in k4_witnesses)
    print(f"atlas triangulations with a degree-three vertex: {tested_graphs}")
    print(f"ordered (G,v) inputs checked: {tested_pairs}")
    print(f"K4 replacement toughness: {k4_tau}")
    print("K4 certificate {x,y,z}: 3 deleted, 2 components")
    print("all exact formula checks passed")


if __name__ == "__main__":
    main()
