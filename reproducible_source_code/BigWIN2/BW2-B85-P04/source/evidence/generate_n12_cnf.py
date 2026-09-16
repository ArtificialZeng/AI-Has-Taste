#!/usr/bin/env python3
"""Generate the canonical ordinary two-color KG(12,3) NAE CNF."""

from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path


N = 12
HERE = Path(__file__).resolve().parent
CNF = HERE / "n12.cnf"
META = HERE / "n12_cnf_metadata.json"


def instance():
    vertices = list(combinations(range(1, N + 1), 3))
    edge_id = {}
    edges = []
    for i, a in enumerate(vertices):
        sa = set(a)
        for j in range(i + 1, len(vertices)):
            if sa.isdisjoint(vertices[j]):
                edge_id[(i, j)] = len(edges) + 1
                edges.append((i, j))

    triangles = []
    for i, j, k in combinations(range(len(vertices)), 3):
        if (i, j) in edge_id and (i, k) in edge_id and (j, k) in edge_id:
            triangles.append((edge_id[(i, j)], edge_id[(i, k)], edge_id[(j, k)]))
    return vertices, edges, triangles


def main():
    vertices, edges, triangles = instance()
    assert (len(vertices), len(edges), len(triangles)) == (220, 9240, 61600)

    clause_lines = []
    for triangle in triangles:
        clause_lines.append(" ".join(map(str, triangle)) + " 0\n")
        clause_lines.append(" ".join(str(-x) for x in triangle) + " 0\n")
    clause_stream = "".join(clause_lines).encode("ascii")
    header = f"p cnf {len(edges)} {len(clause_lines)}\n".encode("ascii")
    cnf_bytes = header + clause_stream
    CNF.write_bytes(cnf_bytes)

    metadata = {
        "n": N,
        "vertex_order": "lexicographic 3-subsets of [12]",
        "variable_order": "lexicographic pairs of disjoint ordered vertices i<j",
        "triangle_order": "lexicographic triples of vertex indices i<j<k",
        "vertices": len(vertices),
        "variables": len(edges),
        "triangles": len(triangles),
        "clauses": len(clause_lines),
        "clause_stream_sha256": sha256(clause_stream).hexdigest(),
        "dimacs_sha256": sha256(cnf_bytes).hexdigest(),
        "dimacs_file": "evidence/n12.cnf",
    }
    META.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
