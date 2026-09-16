#!/usr/bin/env python3
"""Exact finite census of edge cards and maximal-planar parents of J_m.

For a card C=J_m-e on n vertices, every possible maximal-planar parent has
exactly one more edge, hence is C+xy for a nonedge xy of C.  We test every
such pair for planarity and quotient both cards and parents by exact NetworkX
VF2 graph isomorphism.  No floating-point or random operation is used.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations

import networkx as nx


def rim(i: int) -> str:
    return f"r{i}"


def jm(m: int) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(["p", "q", "w"] + [rim(i) for i in range(m)])
    g.add_edges_from((rim(i), rim((i + 1) % m)) for i in range(m))
    g.add_edges_from(("p", rim(i)) for i in range(m))
    g.add_edges_from(("q", rim(i)) for i in range(m))
    g.add_edges_from([("w", "p"), ("w", "r0"), ("w", "r1")])
    assert len(g) == m + 3 and g.number_of_edges() == 3 * len(g) - 6
    assert nx.check_planarity(g)[0]
    return g


def edge_key(e: tuple[str, str]) -> tuple[str, str]:
    return tuple(sorted(e))


def edge_name(e: tuple[str, str]) -> str:
    return "-".join(edge_key(e))


def degree_sequence(g: nx.Graph) -> list[int]:
    return sorted((d for _, d in g.degree()), reverse=True)


def iso_class_indices(graphs: list[nx.Graph]) -> tuple[list[int], list[nx.Graph]]:
    reps: list[nx.Graph] = []
    indices: list[int] = []
    for g in graphs:
        for i, h in enumerate(reps):
            if nx.is_isomorphic(g, h):
                indices.append(i)
                break
        else:
            indices.append(len(reps))
            reps.append(g)
    return indices, reps


def edge_orbits(g: nx.Graph) -> list[list[tuple[str, str]]]:
    """Compute edge orbits from all abstract automorphisms of g."""
    edges = sorted(map(edge_key, g.edges()))
    unseen = set(edges)
    result = []
    automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter())
    while unseen:
        e = min(unseen)
        orb = {
            edge_key((a[e[0]], a[e[1]]))
            for a in automorphisms
        }
        result.append(sorted(orb))
        unseen -= orb
    return result


def all_parents(card: nx.Graph) -> list[tuple[tuple[str, str], nx.Graph]]:
    """Enumerate every one-edge completion that is maximal planar."""
    n = len(card)
    assert card.number_of_edges() == 3 * n - 7
    ans = []
    for x, y in combinations(sorted(card.nodes()), 2):
        if card.has_edge(x, y):
            continue
        h = card.copy()
        h.add_edge(x, y)
        planar = nx.check_planarity(h, counterexample=False)[0]
        if planar:
            assert h.number_of_edges() == 3 * n - 6
            ans.append(((x, y), h))
    return ans


def graph_edges(g: nx.Graph) -> list[str]:
    return sorted(edge_name(e) for e in g.edges())


def census(m: int) -> dict:
    g = jm(m)
    edges = sorted(map(edge_key, g.edges()))
    cards = []
    for e in edges:
        c = g.copy()
        c.remove_edge(*e)
        cards.append(c)
    card_indices, card_reps = iso_class_indices(cards)
    aut_orbits = edge_orbits(g)
    edge_to_orbit = {
        e: i for i, orb in enumerate(aut_orbits) for e in orb
    }

    type_records = []
    for ci, card in enumerate(card_reps):
        members = [edges[i] for i, x in enumerate(card_indices) if x == ci]
        completions = all_parents(card)
        parent_indices, parent_reps = iso_class_indices([h for _, h in completions])
        parent_records = []
        for pi, h in enumerate(parent_reps):
            added = [
                edge_name(completions[i][0])
                for i, x in enumerate(parent_indices) if x == pi
            ]
            parent_records.append({
                "is_Jm": nx.is_isomorphic(h, g),
                "added_nonedges": sorted(added),
                "degree_sequence": degree_sequence(h),
                "edges": graph_edges(h),
            })
        identifying = all(p["is_Jm"] for p in parent_records)
        type_records.append({
            "card_type": ci,
            "multiplicity": len(members),
            "member_edges": [edge_name(e) for e in members],
            "automorphism_orbits": sorted({edge_to_orbit[e] for e in members}),
            "labeled_completions": len(completions),
            "unlabeled_parent_types": len(parent_reps),
            "identifying": identifying,
            "parents": parent_records,
        })

    return {
        "m": m,
        "vertices": len(g),
        "edges": g.number_of_edges(),
        "degree_sequence_Jm": degree_sequence(g),
        "automorphism_group_order": len(list(
            nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter()
        )),
        "automorphism_orbits": [
            {"orbit": i, "size": len(orb), "edges": [edge_name(e) for e in orb]}
            for i, orb in enumerate(aut_orbits)
        ],
        "card_types": type_records,
        "identifying_edges": sorted(
            e
            for t in type_records if t["identifying"]
            for e in t["member_edges"]
        ),
        "checks": {
            "all_edges_accounted": sum(t["multiplicity"] for t in type_records) == g.number_of_edges(),
            "each_card_has_original_completion": all(
                any(p["is_Jm"] for p in t["parents"]) for t in type_records
            ),
            "identifying_constant_on_card_type": True,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int, nargs="+", help="rim sizes")
    args = ap.parse_args()
    data = {
        "method": (
            "For every edge card, test every nonedge as the unique possible added "
            "edge; retain planar 3n-6-edge completions; group by exact VF2 isomorphism."
        ),
        "networkx_version": nx.__version__,
        "cases": [census(m) for m in args.m],
    }
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
