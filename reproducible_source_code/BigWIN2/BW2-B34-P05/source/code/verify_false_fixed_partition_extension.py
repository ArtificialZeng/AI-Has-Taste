#!/usr/bin/env python3
"""Verify the exact obstruction to naive one-vertex C001 extension."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import networkx as nx

from partition_probe import verify_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", type=Path)
    args = parser.parse_args()
    data = json.loads(args.witness.read_text())
    graph = nx.from_graph6_bytes(data["graph6"].encode())
    vertex = data["deleted_vertex"]

    assert graph.number_of_nodes() == data["order"]
    assert graph.number_of_edges() == data["size"]
    assert graph.degree(vertex) == data["degree_of_deleted_vertex"]
    assert nx.is_tree(graph)
    assert not any(nx.triangles(graph).values())
    assert max(dict(graph.degree()).values()) <= 6

    deleted = graph.copy()
    deleted.remove_node(vertex)
    certificate = data["partition_of_deleted_graph"]
    assert verify_certificate(deleted, certificate)

    for destination in ("A0", "A1", "B"):
        attempted = {key: list(value) for key, value in certificate.items()}
        attempted[destination].append(vertex)
        assert not verify_certificate(graph, attempted)

    assert verify_certificate(graph, data["valid_partition_of_full_graph"])
    print(
        json.dumps(
            {
                "verified": True,
                "order": graph.number_of_nodes(),
                "tree": True,
                "deleted_vertex_degree": graph.degree(vertex),
                "all_three_fixed_partition_insertions_fail": True,
                "full_graph_still_has_C001_partition": True
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
