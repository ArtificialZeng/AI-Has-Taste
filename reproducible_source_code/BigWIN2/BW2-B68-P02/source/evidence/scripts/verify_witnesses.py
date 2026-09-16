#!/usr/bin/env python3
"""Direct verifier for positive total-coloring witnesses; no SAT code imported."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    witness_path = ROOT / "evidence" / "coloring_witnesses.jsonl"
    verified_a = verified_e = observed_unsat = 0
    candidate_codes = []
    for line_number, line in enumerate(witness_path.read_text().splitlines(), 1):
        row = json.loads(line)
        graph = nx.from_graph6_bytes(row["graph6"].encode("ascii"))
        n = row["n"]
        assert graph.number_of_nodes() == n, line_number
        assert row["index"] >= 0, line_number
        classification = row["classification"]
        if classification == "A_unsat_observed":
            assert "colors" not in row, line_number
            observed_unsat += 1
            continue

        colors = row["colors"]
        edges = sorted((min(u, v), max(u, v)) for u, v in graph.edges())
        assert len(colors) == n + len(edges), line_number
        assert all(isinstance(color, int) and 0 <= color < 4 for color in colors), line_number
        edge_color = {edge: colors[n + index] for index, edge in enumerate(edges)}
        for u, v in edges:
            assert colors[u] != colors[v], (line_number, "adjacent vertices", u, v)
            assert edge_color[(u, v)] not in (colors[u], colors[v]), (
                line_number,
                "incident vertex-edge",
                u,
                v,
            )
        for vertex in range(n):
            incident_colors = [
                edge_color[(min(vertex, neighbor), max(vertex, neighbor))]
                for neighbor in graph.neighbors(vertex)
            ]
            assert len(incident_colors) == len(set(incident_colors)) == 3, (
                line_number,
                "adjacent edges",
                vertex,
            )
        profile = sorted(Counter(colors).values())
        assert len(profile) == 4
        if classification == "E_sat":
            assert profile[-1] - profile[0] <= 1, (line_number, profile)
            verified_e += 1
        elif classification == "A_sat_E_unsat_observed":
            assert profile == [9, 10, 10, 11], (line_number, profile)
            verified_a += 1
            candidate_codes.append(row["graph6"])
        else:
            raise AssertionError((line_number, classification))

    report = {
        "script": str(Path(__file__).relative_to(ROOT)),
        "input": str(witness_path.relative_to(ROOT)),
        "input_sha256": hashlib.sha256(witness_path.read_bytes()).hexdigest(),
        "verified_equitable_witnesses": verified_e,
        "verified_proper_nonequitable_witnesses": verified_a,
        "unverified_unsat_observations": observed_unsat,
        "candidate_graph6": candidate_codes,
        "status": "all positive witnesses pass",
    }
    output = ROOT / "evidence" / "witness_verification.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
