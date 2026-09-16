#!/usr/bin/env python3
"""Independent exact boundary-family attack on conjecture C001.

This audit helper constructs canonical triangle-free graphs of maximum degree
at most six and asks the project certificate solver for the C001 partition.
Every returned certificate is then checked without Z3 by the project's direct
graph checker.  The finite run is a falsification attempt, not a proof.
"""

from __future__ import annotations

import itertools
import json

import networkx as nx

from partition_probe import partition_certificate, verify_certificate


def odd_cycle_blowup(length: int, width: int) -> nx.Graph:
    """Replace each vertex of an odd cycle by an independent set of `width`."""
    graph = nx.Graph()
    graph.add_nodes_from((part, index) for part in range(length) for index in range(width))
    for part in range(length):
        next_part = (part + 1) % length
        graph.add_edges_from(
            ((part, i), (next_part, j))
            for i in range(width)
            for j in range(width)
        )
    return nx.convert_node_labels_to_integers(graph)


def andrasfai_graph(k: int) -> nx.Graph:
    """Return the k-regular Andrasfai graph on 3k-1 vertices."""
    order = 3 * k - 1
    residues = {value % order for value in range(1, order, 3)}
    graph = nx.Graph()
    graph.add_nodes_from(range(order))
    for u, v in itertools.combinations(range(order), 2):
        if (u - v) % order in residues or (v - u) % order in residues:
            graph.add_edge(u, v)
    return graph


def odd_graph(k: int) -> nx.Graph:
    """Return the Kneser odd graph KG(2k+1,k), of degree k+1."""
    ground = range(2 * k + 1)
    vertices = list(itertools.combinations(ground, k))
    graph = nx.Graph()
    graph.add_nodes_from(range(len(vertices)))
    supports = list(map(set, vertices))
    for u, v in itertools.combinations(range(len(vertices)), 2):
        if supports[u].isdisjoint(supports[v]):
            graph.add_edge(u, v)
    return graph


def cases() -> list[tuple[str, nx.Graph]]:
    result: list[tuple[str, nx.Graph]] = []
    for length in range(4, 16):
        result.append((f"cycle-{length}", nx.cycle_graph(length)))
    for left in range(1, 7):
        for right in range(1, 7):
            result.append((f"K-{left}-{right}", nx.complete_bipartite_graph(left, right)))
    for length in (5, 7, 9):
        for width in (1, 2, 3):
            result.append((f"C-{length}-blowup-{width}", odd_cycle_blowup(length, width)))
    for k in range(2, 7):
        result.append((f"Andrasfai-{k}", andrasfai_graph(k)))
    for k in range(2, 6):
        result.append((f"odd-graph-O-{k + 1}", odd_graph(k)))
    result.extend(
        [
            ("Petersen", nx.petersen_graph()),
            ("dodecahedral", nx.dodecahedral_graph()),
            ("Desargues", nx.desargues_graph()),
            ("Heawood", nx.heawood_graph()),
            ("Moebius-Kantor", nx.moebius_kantor_graph()),
            ("Pappus", nx.pappus_graph()),
            ("Chvatal", nx.chvatal_graph()),
        ]
    )
    return result


def main() -> None:
    records = []
    for name, graph in cases():
        graph = nx.convert_node_labels_to_integers(graph)
        maximum_degree = max((degree for _, degree in graph.degree()), default=0)
        assert nx.number_of_selfloops(graph) == 0
        assert maximum_degree <= 6
        assert not any(nx.triangles(graph).values())
        certificate = partition_certificate(graph)
        verified = certificate is not None and verify_certificate(graph, certificate)
        records.append(
            {
                "name": name,
                "order": graph.number_of_nodes(),
                "size": graph.number_of_edges(),
                "maximum_degree": maximum_degree,
                "regular": len(set(dict(graph.degree()).values())) <= 1,
                "partition_found": certificate is not None,
                "certificate_verified": verified,
            }
        )
    failures = [record for record in records if not record["certificate_verified"]]
    summary = {
        "tested": len(records),
        "failures": failures,
        "maximum_order": max(record["order"] for record in records),
        "degree_six_cases": sum(record["maximum_degree"] == 6 for record in records),
        "regular_degree_six_cases": sum(
            record["maximum_degree"] == 6 and record["regular"] for record in records
        ),
        "records": records,
        "limitation": "Finite canonical-family attack only; no universal conclusion follows.",
    }
    print(json.dumps(summary, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
