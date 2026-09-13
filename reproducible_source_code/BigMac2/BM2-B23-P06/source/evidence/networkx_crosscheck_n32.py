#!/usr/bin/env python3
"""Independent NetworkX chordless-cycle cross-check of the n<=32 census."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import networkx as nx


def graph_for(n: int, selected: set[int]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(
        (x, y)
        for x in range(n)
        for y in range(x + 1, n)
        if math.gcd(x - y, n) in selected
    )
    return graph


def has_odd_hole(graph: nx.Graph) -> tuple[bool, int]:
    cycles_seen = 0
    for cycle in nx.chordless_cycles(graph):
        cycles_seen += 1
        if len(cycle) >= 5 and len(cycle) % 2 == 1:
            return True, cycles_seen
    return False, cycles_seen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = args.manifest.read_bytes()
    manifest = json.loads(raw)
    mismatches = []
    total_cycles_seen = 0
    graph_holes = 0
    complement_holes = 0
    for record in manifest["records"]:
        graph = graph_for(record["n"], set(record["D"]))
        in_graph, count = has_odd_hole(graph)
        total_cycles_seen += count
        in_complement = False
        if not in_graph:
            in_complement, count = has_odd_hole(nx.complement(graph))
            total_cycles_seen += count
        if in_graph:
            graph_holes += 1
        elif in_complement:
            complement_holes += 1
        observed = "imperfect" if in_graph or in_complement else "perfect"
        if observed != record["status"]:
            mismatches.append(
                {"dmask": record["dmask"], "expected": record["status"], "n": record["n"], "observed": observed}
            )
    result = {
        "backend": "networkx.chordless_cycles",
        "complement_odd_holes_found": complement_holes,
        "graph_odd_holes_found": graph_holes,
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "mismatches": mismatches,
        "networkx_version": nx.__version__,
        "records_checked": len(manifest["records"]),
        "status": "pass" if not mismatches else "fail",
        "total_chordless_cycles_scanned_until_decision": total_cycles_seen,
    }
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
