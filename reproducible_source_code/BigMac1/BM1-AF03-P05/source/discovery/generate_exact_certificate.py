#!/usr/bin/env python3
"""Discovery and rational reconstruction for the sparse-complement cases.

This program is deliberately *not* the verifier.  It uses nauty ``geng`` and
floating-point least squares to locate Parseval frames, then reconstructs and
checks exact rational data before serializing it.  The independent verifier in
``verification/verify_n9_certificate.py`` uses neither this module nor its
floating-point output.
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path

import networkx as nx
import numpy as np
import scipy
import sympy as sp
from scipy.optimize import least_squares


def is_join_routed(h: nx.Graph) -> bool:
    """Test the connected-balanced-join sufficient condition."""
    components = [h.subgraph(c).copy() for c in nx.connected_components(h)]
    for mask in range(1, (1 << len(components)) - 1):
        left = nx.disjoint_union_all(
            [components[i] for i in range(len(components)) if mask & (1 << i)]
        )
        right = nx.disjoint_union_all(
            [components[i] for i in range(len(components)) if not mask & (1 << i)]
        )
        if (
            abs(len(left) - len(right)) <= 2
            and nx.is_connected(nx.complement(left))
            and nx.is_connected(nx.complement(right))
        ):
            return True
    return False


def degeneracy_order(h: nx.Graph, rank: int) -> list[int]:
    """Return an order with fewer than ``rank`` earlier H-neighbours."""
    work = h.copy()
    removed: list[int] = []
    while work:
        v = min(work, key=lambda z: (work.degree(z), z))
        if work.degree(v) >= rank:
            raise RuntimeError("chosen frame rank is below the degeneracy bound")
        removed.append(v)
        work.remove_node(v)
    return removed[::-1]


def numerical_frame(h: nx.Graph, rank: int, seed: int) -> tuple[np.ndarray, float, float]:
    """Locate an orthonormal-column matrix with H-edges as row orthogonalities."""
    n = len(h)
    edges = sorted(tuple(sorted(e)) for e in h.edges())
    rng = np.random.default_rng(seed)
    initial = rng.normal(size=(n, rank))

    def stiefel(flat: np.ndarray) -> np.ndarray:
        q, _ = np.linalg.qr(flat.reshape(n, rank))
        return q

    def residual(flat: np.ndarray) -> np.ndarray:
        u = stiefel(flat)
        p = u @ u.T
        return np.array([p[i, j] for i, j in edges])

    result = least_squares(
        residual,
        initial.ravel(),
        method="trf",
        gtol=1e-14,
        ftol=1e-14,
        xtol=1e-14,
        max_nfev=10000,
    )
    u = stiefel(result.x)
    p = u @ u.T
    maximum_residual = float(np.max(np.abs(residual(result.x))))
    required_nonzeros = [
        abs(p[i, j])
        for i in range(n)
        for j in range(i)
        if not h.has_edge(i, j)
    ]
    return u, maximum_residual, float(min(required_nonzeros))


def rational(value: float, denominator_bound: int) -> sp.Rational:
    q = Fraction(float(value)).limit_denominator(denominator_bound)
    return sp.Rational(q.numerator, q.denominator)


def rational_reconstruction(
    h: nx.Graph, u: np.ndarray, rank: int, denominator_bound: int
) -> tuple[list[int], sp.Matrix, list[sp.Rational]]:
    """Preserve all H-orthogonalities, then solve the Parseval scaling exactly."""
    order = degeneracy_order(h, rank)
    rows: dict[int, list[sp.Rational]] = {}
    seen: list[int] = []
    for v in order:
        earlier_neighbours = [z for z in seen if h.has_edge(v, z)]
        constraints = (
            sp.Matrix([[rows[z][j] for j in range(rank)] for z in earlier_neighbours])
            if earlier_neighbours
            else sp.zeros(0, rank)
        )
        basis_vectors = constraints.nullspace()
        basis = sp.Matrix.hstack(*basis_vectors)
        basis_float = np.array(basis.tolist(), dtype=float)
        coefficients = np.linalg.lstsq(basis_float, u[v], rcond=None)[0]
        exact_coefficients = sp.Matrix(
            [rational(z, denominator_bound) for z in coefficients]
        )
        rows[v] = list(basis * exact_coefficients)
        seen.append(v)

    w = sp.Matrix([rows[i] for i in range(len(h))])
    symmetric_coordinates = [
        (a, b) for a in range(rank) for b in range(a, rank)
    ]
    coefficient_matrix = sp.Matrix(
        [
            [w[i, a] * w[i, b] for i in range(len(h))]
            for a, b in symmetric_coordinates
        ]
    )
    target = sp.Matrix([1 if a == b else 0 for a, b in symmetric_coordinates])
    solution, parameters = coefficient_matrix.gauss_jordan_solve(target)
    weights = [sp.factor(z.subs({p: 1 for p in parameters})) for z in solution]

    if not all(x.is_Rational and x > 0 for x in weights):
        raise RuntimeError("rational reconstruction did not retain positive weights")
    if coefficient_matrix * sp.Matrix(weights) != target:
        raise RuntimeError("internal exact Parseval check failed")
    for i in range(len(h)):
        for j in range(i):
            dot = sum(w[i, k] * w[j, k] for k in range(rank))
            if (dot == 0) != h.has_edge(i, j):
                raise RuntimeError("internal exact support check failed")
    return order, w, weights


def fraction_text(x: sp.Rational) -> str:
    return f"{int(x.p)}/{int(x.q)}"


def graph_lines(n: int, edge_limit: int) -> list[str]:
    completed = subprocess.run(
        ["geng", "-q", "-l", str(n), f"0:{edge_limit}"],
        check=True,
        text=True,
        capture_output=True,
    )
    return [line.strip() for line in completed.stdout.splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("certificates/n9_exact_frames.json"),
    )
    parser.add_argument("--seed-count", type=int, default=32)
    parser.add_argument("--denominator-bound", type=int, default=100000)
    args = parser.parse_args()

    frame_witnesses: list[dict[str, object]] = []
    route_counts: dict[str, dict[str, int]] = {}
    for n, edge_limit in ((7, 4), (8, 5), (9, 6)):
        lines = graph_lines(n, edge_limit)
        counts = {"total": len(lines), "bipartite": 0, "join": 0, "frame": 0}
        for graph6 in lines:
            h = nx.from_graph6_bytes(graph6.encode("ascii"))
            if nx.is_bipartite(h):
                counts["bipartite"] += 1
                continue
            if is_join_routed(h):
                counts["join"] += 1
                continue

            best: tuple[int, np.ndarray, float, float] | None = None
            for seed in range(args.seed_count):
                u, residual, margin = numerical_frame(h, rank=3, seed=seed)
                if residual < 1e-9 and (best is None or margin > best[3]):
                    best = (seed, u, residual, margin)
            if best is None:
                raise RuntimeError(f"no discovery candidate for {n}:{graph6}")
            seed, u, residual, margin = best
            order, directions, weights = rational_reconstruction(
                h, u, rank=3, denominator_bound=args.denominator_bound
            )
            frame_witnesses.append(
                {
                    "n": n,
                    "edge_limit": edge_limit,
                    "graph6": graph6,
                    "rank": 3,
                    "orthogonality_order": order,
                    "directions": [
                        [fraction_text(directions[i, j]) for j in range(3)]
                        for i in range(n)
                    ],
                    "weights": [fraction_text(x) for x in weights],
                    "discovery_only": {
                        "seed": seed,
                        "maximum_zero_residual": format(residual, ".17g"),
                        "minimum_required_nonzero_margin": format(margin, ".17g"),
                    },
                }
            )
            counts["frame"] += 1
        route_counts[str(n)] = counts

    certificate = {
        "schema": "sparse-complement-q2-exact-frame-certificate-v1",
        "endpoint": {
            "orders_certified": [7, 8, 9],
            "edge_limit_formula": "n-3",
            "field": "real symmetric matrices",
            "support_convention": "off_diagonal_nonzero_iff_edge_of_G",
        },
        "external_theorems": {
            "bipartite_complement": {
                "statement": "If H=bar(G) is bipartite and |E(H)|<=n-3, then q(G)=2.",
                "source": "Barrett--Fallat--Furst--Nasserasr--Rooney--Tait, Theorem 3.7",
                "doi": "10.13001/ela.2026.9443",
            },
            "balanced_connected_join": {
                "statement": "If X and Y are connected and ||V(X)|-|V(Y)||<=2, then q(X join Y)=2.",
                "source": "Levene--Oblak--Smigoc, Theorem 3.4 (connected k=1 case)",
                "doi": "10.1080/03081087.2023.2232090",
            },
        },
        "expected_route_counts": route_counts,
        "frame_witnesses": frame_witnesses,
        "discovery_provenance": {
            "warning": "Floating-point fields locate candidates only and are not read by the verifier.",
            "generator": "discovery/generate_exact_certificate.py",
            "geng_command_template": "geng -q -l n 0:n-3",
            "seed_range": [0, args.seed_count - 1],
            "denominator_bound": args.denominator_bound,
            "python": platform.python_version(),
            "networkx": nx.__version__,
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "sympy": sp.__version__,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
