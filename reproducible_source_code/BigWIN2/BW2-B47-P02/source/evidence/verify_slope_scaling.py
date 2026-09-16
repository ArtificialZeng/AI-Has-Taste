#!/usr/bin/env python3
"""Exact construction and certificate verifier for the six q=7 graphs.

No third-party packages are used.  The primary construction finds the common
symbol by scanning the seven columns of the two Latin-square rows.  A second
construction uses the closed formula from problem.md; their edge sets must
agree before any artifact is emitted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


Q = 7
X_SIZE = 8
SLOPES = tuple(range(1, Q))
ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "evidence" / "adjacency"
CERT_PATH = ROOT / "evidence" / "slope_scaling_certificates.json"
SUMMARY_PATH = ROOT / "evidence" / "verification-summary.json"


def inv(a: int) -> int:
    """Multiplicative inverse in F_7, with a required to be nonzero."""
    if a % Q == 0:
        raise ValueError("zero has no inverse")
    return pow(a % Q, Q - 2, Q)


def character(a: int) -> int:
    """Quadratic character of F_7, with character(0)=0."""
    a %= Q
    if a == 0:
        return 0
    return 1 if a in {1, 2, 4} else -1


def paley_rows() -> tuple[tuple[int, ...], ...]:
    """The seven nonfirst rows of the normalized order-8 Paley matrix.

    Coordinates are infinity,0,...,6.  The row indexed by t starts with +1;
    its field coordinate c is -1 for c=t and chi(c-t) otherwise.
    """
    rows = []
    for t in range(Q):
        rows.append((1,) + tuple(-1 if c == t else character(c - t)
                                 for c in range(Q)))
    return tuple(rows)


H_NONFIRST = paley_rows()


def latin(alpha: int, row: int, col: int) -> int:
    return alpha * (row - col) % Q


def common_symbol_scan(alpha: int, beta: int, row: int, other_row: int) -> int:
    """Find K without using its rational closed formula."""
    hits = [latin(alpha, row, col) for col in range(Q)
            if latin(alpha, row, col) == latin(beta, other_row, col)]
    if len(hits) != 1:
        raise AssertionError((alpha, beta, row, other_row, hits))
    return hits[0]


def common_symbol_formula(alpha: int, beta: int, row: int, other_row: int) -> int:
    return alpha * beta * (row - other_row) * inv(beta - alpha) % Q


def retained(deletion: int) -> tuple[int, ...]:
    return tuple(alpha for alpha in SLOPES if alpha != deletion)


def vertices(deletion: int) -> tuple[tuple[int, int, int], ...]:
    return tuple((alpha, row, x)
                 for alpha in retained(deletion)
                 for row in range(Q)
                 for x in range(X_SIZE))


def is_adjacent(v: tuple[int, int, int], w: tuple[int, int, int], *, scan: bool) -> bool:
    alpha, row, x = v
    beta, other_row, y = w
    if alpha == beta:
        return row != other_row
    symbol = (common_symbol_scan(alpha, beta, row, other_row) if scan
              else common_symbol_formula(alpha, beta, row, other_row))
    return H_NONFIRST[symbol][x] * H_NONFIRST[symbol][y] == 1


def build_graph(deletion: int, *, scan: bool) -> tuple[frozenset[int], ...]:
    verts = vertices(deletion)
    adjacency = [set() for _ in verts]
    for i in range(len(verts)):
        for j in range(i + 1, len(verts)):
            if is_adjacent(verts[i], verts[j], scan=scan):
                adjacency[i].add(j)
                adjacency[j].add(i)
    return tuple(frozenset(nbrs) for nbrs in adjacency)


def adjacency_bytes(deletion: int, graph: tuple[frozenset[int], ...]) -> bytes:
    slope_text = ",".join(map(str, retained(deletion)))
    lines = [
        f"# G_{deletion}; deleted slope {deletion}; retained slopes {slope_text}",
        "# vertex id ((slope-position)*7+row)*8+x; row=0..6; x=0..7",
        "# each following line is id:space-separated-neighbor-ids",
    ]
    for vertex_id, nbrs in enumerate(graph):
        lines.append(f"{vertex_id}:" + "".join(f" {j}" for j in sorted(nbrs)))
    return ("\n".join(lines) + "\n").encode("ascii")


def edge_count(graph: tuple[frozenset[int], ...]) -> int:
    return sum(map(len, graph)) // 2


def scaling_permutation(a: int, b: int) -> tuple[int, ...]:
    """Serialize phi_(b/a): Omega_a -> Omega_b in the fixed vertex order."""
    source = vertices(a)
    target_index = {v: i for i, v in enumerate(vertices(b))}
    u = b * inv(a) % Q
    u_inverse = inv(u)
    return tuple(target_index[(u * alpha % Q, u_inverse * row % Q, x)]
                 for alpha, row, x in source)


def verify_permutation(
    source: tuple[frozenset[int], ...],
    target: tuple[frozenset[int], ...],
    permutation: tuple[int, ...],
) -> None:
    n = len(source)
    if sorted(permutation) != list(range(n)):
        raise AssertionError("certificate is not a permutation")
    for i in range(n):
        image_neighbors = {permutation[j] for j in source[i]}
        if image_neighbors != set(target[permutation[i]]):
            raise AssertionError(f"adjacency mismatch at source vertex {i}")


def verify_paley() -> dict[str, object]:
    full = ((1,) * X_SIZE,) + H_NONFIRST
    gram = [[sum(a * b for a, b in zip(row_i, row_j))
             for row_j in full] for row_i in full]
    expected = [[X_SIZE if i == j else 0 for j in range(X_SIZE)]
                for i in range(X_SIZE)]
    if gram != expected:
        raise AssertionError("Paley matrix is not Hadamard")
    if any(sum(row) != 0 for row in H_NONFIRST):
        raise AssertionError("nonfirst Paley row is not balanced")
    return {
        "full_rows": [list(row) for row in full],
        "gram_matrix": gram,
        "is_normalized_hadamard": True,
    }


def generate_payloads() -> tuple[dict[Path, bytes], dict[str, object]]:
    paley_check = verify_paley()
    graphs: dict[int, tuple[frozenset[int], ...]] = {}
    graph_records = []
    payloads: dict[Path, bytes] = {}

    for deletion in SLOPES:
        graph_scan = build_graph(deletion, scan=True)
        graph_formula = build_graph(deletion, scan=False)
        if graph_scan != graph_formula:
            raise AssertionError(f"two builders disagree for deletion {deletion}")
        if any(i in nbrs for i, nbrs in enumerate(graph_scan)):
            raise AssertionError(f"loop in G_{deletion}")
        if any((i in graph_scan[j]) != (j in graph_scan[i])
               for i in range(len(graph_scan)) for j in range(len(graph_scan))):
            raise AssertionError(f"asymmetry in G_{deletion}")
        degrees = tuple(map(len, graph_scan))
        if set(degrees) != {160}:
            raise AssertionError(f"wrong degrees in G_{deletion}: {set(degrees)}")
        if edge_count(graph_scan) != 22400:
            raise AssertionError(f"wrong edge count in G_{deletion}")

        data = adjacency_bytes(deletion, graph_scan)
        path = OUT_DIR / f"G_{deletion}.adj"
        payloads[path] = data
        graphs[deletion] = graph_scan
        graph_records.append({
            "deletion": deletion,
            "retained_slopes": list(retained(deletion)),
            "vertices": len(graph_scan),
            "degree_min": min(degrees),
            "degree_max": max(degrees),
            "edges": edge_count(graph_scan),
            "simple": True,
            "symmetric_adjacency": True,
            "scan_builder_equals_formula_builder": True,
            "adjacency_file": str(path.relative_to(ROOT)),
            "adjacency_sha256": hashlib.sha256(data).hexdigest(),
        })

    certificates = []
    for a in SLOPES:
        for b in SLOPES:
            permutation = scaling_permutation(a, b)
            verify_permutation(graphs[a], graphs[b], permutation)
            certificates.append({
                "source_deletion": a,
                "target_deletion": b,
                "u_equals_b_over_a_mod_7": b * inv(a) % Q,
                "permutation": list(permutation),
                "verified_bijection_and_adjacency": True,
            })

    cert_object = {
        "schema": "win-00047-p02-explicit-permutations-v1",
        "field": "F_7 represented by integers 0,...,6",
        "vertex_order": "lexicographic (retained slope, row, x), with retained slopes numerically sorted",
        "map": "(alpha,row,x) -> (u*alpha,u^(-1)*row,x), u=b/a in F_7",
        "certificates": certificates,
    }
    cert_data = (json.dumps(cert_object, indent=2, sort_keys=True) + "\n").encode("utf-8")
    payloads[CERT_PATH] = cert_data

    summary = {
        "schema": "win-00047-p02-verification-v1",
        "arithmetic": "exact integer arithmetic reduced modulo 7; no floating point",
        "paley_matrix": paley_check,
        "graphs": graph_records,
        "ordered_scaling_certificates_checked": len(certificates),
        "all_certificates_are_bijections_and_edge_preserving": True,
        "certificate_file": str(CERT_PATH.relative_to(ROOT)),
        "certificate_sha256": hashlib.sha256(cert_data).hexdigest(),
    }
    summary_data = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode("utf-8")
    payloads[SUMMARY_PATH] = summary_data
    return payloads, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verify-existing",
        action="store_true",
        help="recompute in memory and require every existing artifact byte-for-byte",
    )
    args = parser.parse_args()
    payloads, summary = generate_payloads()
    if args.verify_existing:
        for path, expected in payloads.items():
            if not path.is_file():
                raise SystemExit(f"missing artifact: {path.relative_to(ROOT)}")
            actual = path.read_bytes()
            if actual != expected:
                raise SystemExit(f"artifact differs: {path.relative_to(ROOT)}")
    else:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        for path, data in payloads.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps({
        "mode": "verify-existing" if args.verify_existing else "write",
        "graphs": len(summary["graphs"]),
        "vertices_each": sorted({g["vertices"] for g in summary["graphs"]}),
        "degrees": sorted({(g["degree_min"], g["degree_max"])
                           for g in summary["graphs"]}),
        "edges_each": sorted({g["edges"] for g in summary["graphs"]}),
        "ordered_certificates": summary["ordered_scaling_certificates_checked"],
        "success": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
