#!/usr/bin/env python3
"""Deterministic triage probe for the n=11 CNF; not a proof logger."""

from hashlib import sha256
from itertools import combinations

from pathlib import Path

from pysat.solvers import Cadical195


def instance(n: int):
    vertices = list(combinations(range(1, n + 1), 3))
    edge_id = {}
    edges = []
    for i, a in enumerate(vertices):
        sa = set(a)
        for j in range(i + 1, len(vertices)):
            b = vertices[j]
            if sa.isdisjoint(b):
                edge_id[(i, j)] = len(edges) + 1
                edges.append((i, j))

    triangles = []
    clauses = []
    for i, j, k in combinations(range(len(vertices)), 3):
        if ((i, j) in edge_id and (i, k) in edge_id
                and (j, k) in edge_id):
            triangle = (edge_id[(i, j)], edge_id[(i, k)], edge_id[(j, k)])
            triangles.append(triangle)
            clauses.append(triangle)
            clauses.append(tuple(-x for x in triangle))
    return vertices, edges, triangles, clauses


def main():
    n = 11
    vertices, edges, triangles, clauses = instance(n)
    digest = sha256()
    for clause in clauses:
        digest.update((" ".join(map(str, clause)) + " 0\n").encode())
    print(f"n={n}")
    print(f"vertices={len(vertices)}")
    print(f"edges={len(edges)}")
    print(f"triangles={len(triangles)}")
    print(f"variables={len(edges)}")
    print(f"clauses={len(clauses)}")
    print(f"clause_stream_sha256={digest.hexdigest()}")
    with Cadical195(bootstrap_with=clauses) as solver:
        result = solver.solve()
        print(f"cadical195_result={'SAT' if result else 'UNSAT'}")
        if result:
            assignment = {abs(x): x > 0 for x in solver.get_model()}
            model_bits = bytes(assignment[i] for i in range(1, len(edges) + 1))
            print(f"model_bits_sha256={sha256(model_bits).hexdigest()}")
            lines = [
                "# Complete edge coloring of KG(11,3)",
                "# Format: endpoint_A endpoint_B color; endpoints are sorted triples",
                "# Edge order is the lexicographic order used by triage_probe.py",
            ]
            for var, (i, j) in enumerate(edges, 1):
                a = ",".join(map(str, vertices[i]))
                b = ",".join(map(str, vertices[j]))
                color = "R" if assignment[var] else "B"
                lines.append(f"{a} {b} {color}")
            target = Path(__file__).with_name("n11_coloring.txt")
            target.write_text("\n".join(lines) + "\n", encoding="ascii")
            print(f"coloring_file={target}")
            print(f"coloring_sha256={sha256(target.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
