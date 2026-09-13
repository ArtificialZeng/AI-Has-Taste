#!/usr/bin/env python3
"""Deterministic floating-point discovery for projection realizations.

This is NOT a proof or certificate.  It searches ranks 3 and 4 in two
parameterizations:

1. a 9-by-r Stiefel factor U, with P=UU^T;
2. the free entries of a symmetric involution A with H-entries fixed to 0.

The second solve starts from the first candidate but uses an independent
polynomial residual.  Retained decimal matrices are diagnostics only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
import time
from collections import deque
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares

from breaker_enumerate import decode_graph6, edge_count


N = 9
DEFAULT_SEED = 2026082905


def edges_from_adj(adj: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(i, j) for j in range(1, len(adj)) for i in range(j) if (adj[i] >> j) & 1]


def nonedges_from_adj(adj: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(i, j) for j in range(1, len(adj)) for i in range(j) if not ((adj[i] >> j) & 1)]


def graph_invariants(adj: tuple[int, ...]) -> dict[str, object]:
    n = len(adj)
    degrees = [row.bit_count() for row in adj]
    unseen = set(range(n))
    components: list[int] = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        queue = deque([root])
        size = 0
        while queue:
            u = queue.popleft()
            size += 1
            for v in range(n):
                if ((adj[u] >> v) & 1) and v in unseen:
                    unseen.remove(v)
                    queue.append(v)
        components.append(size)
    triangles = 0
    k4 = 0
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if all((adj[u] >> v) & 1 for u, v in ((a, b), (a, c), (b, c))):
                    triangles += 1
                    for d in range(c + 1, n):
                        verts = (a, b, c, d)
                        if all((adj[verts[i]] >> verts[j]) & 1 for j in range(1, 4) for i in range(j)):
                            k4 += 1
    return {
        "degree_sequence": sorted(degrees, reverse=True),
        "component_sizes": sorted(components, reverse=True),
        "triangles": triangles,
        "k4_subgraphs": k4,
    }


def stiefel_residual(flat: np.ndarray, rank: int, h_edges: list[tuple[int, int]]) -> np.ndarray:
    u = flat.reshape(N, rank)
    gram = u.T @ u - np.eye(rank)
    values = [gram[i, j] for j in range(rank) for i in range(j + 1)]
    values.extend(float(u[i] @ u[j]) for i, j in h_edges)
    return np.asarray(values)


def matrix_metrics(a: np.ndarray, h_edges: list[tuple[int, int]], g_edges: list[tuple[int, int]]) -> dict[str, float]:
    square_error = float(np.max(np.abs(a @ a - np.eye(N))))
    forced_zero_error = max((abs(float(a[i, j])) for i, j in h_edges), default=0.0)
    required_nonzero_margin = min((abs(float(a[i, j])) for i, j in g_edges), default=float("inf"))
    symmetry_error = float(np.max(np.abs(a - a.T)))
    return {
        "max_involution_error": square_error,
        "max_forced_zero_error": forced_zero_error,
        "min_required_nonzero_abs": required_nonzero_margin,
        "max_symmetry_error": symmetry_error,
    }


def solve_stiefel(
    rank: int,
    h_edges: list[tuple[int, int]],
    g_edges: list[tuple[int, int]],
    rng: np.random.Generator,
    starts: int,
    max_nfev: int,
) -> dict[str, object]:
    attempts: list[dict[str, object]] = []
    best: dict[str, object] | None = None
    for start in range(starts):
        x0 = rng.normal(size=(N, rank))
        q, _ = np.linalg.qr(x0)
        x0 = q[:, :rank].reshape(-1)
        fit = least_squares(
            stiefel_residual,
            x0,
            args=(rank, h_edges),
            method="trf",
            ftol=1e-13,
            xtol=1e-13,
            gtol=1e-13,
            max_nfev=max_nfev,
        )
        u_raw = fit.x.reshape(N, rank)
        q, _ = np.linalg.qr(u_raw)
        u = q[:, :rank]
        p = u @ u.T
        a = np.eye(N) - 2.0 * p
        metrics = matrix_metrics(a, h_edges, g_edges)
        residual_inf = float(np.max(np.abs(stiefel_residual(fit.x, rank, h_edges))))
        attempt = {
            "start": start,
            "success_flag": bool(fit.success),
            "status": int(fit.status),
            "nfev": int(fit.nfev),
            "cost": float(fit.cost),
            "raw_residual_inf": residual_inf,
            **metrics,
        }
        attempts.append(attempt)
        feasibility_error = max(
            metrics["max_involution_error"], metrics["max_forced_zero_error"]
        )
        # Once a candidate is well inside the discovery tolerance, prefer a
        # larger nonzero-pattern margin instead of meaningless 1e-14 versus
        # 1e-13 residual differences.  Candidates outside tolerance remain
        # ordered by feasibility error.
        score = (
            0 if feasibility_error < 1e-9 else 1,
            -metrics["min_required_nonzero_abs"] if feasibility_error < 1e-9 else feasibility_error,
            feasibility_error,
        )
        if best is None or score < tuple(best["score"]):
            best = {
                "score": list(score),
                "attempt": attempt,
                "U": u.tolist(),
                "A": a.tolist(),
            }
    assert best is not None
    numerical_hits = [
        item
        for item in attempts
        if item["max_involution_error"] < 1e-9
        and item["max_forced_zero_error"] < 1e-9
        and item["min_required_nonzero_abs"] > 1e-7
    ]
    return {
        "rank": rank,
        "starts": starts,
        "numerical_hit_count": len(numerical_hits),
        "attempts": attempts,
        "best": best,
    }


def direct_parameterization(h_edges: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], set[tuple[int, int]]]:
    h_set = set(h_edges)
    free = [(i, j) for j in range(N) for i in range(j + 1) if i == j or (i, j) not in h_set]
    return free, h_set


def pack_symmetric(a: np.ndarray, free: list[tuple[int, int]]) -> np.ndarray:
    return np.asarray([a[i, j] for i, j in free])


def unpack_symmetric(x: np.ndarray, free: list[tuple[int, int]]) -> np.ndarray:
    a = np.zeros((N, N))
    for value, (i, j) in zip(x, free, strict=True):
        a[i, j] = value
        a[j, i] = value
    return a


def direct_residual(x: np.ndarray, free: list[tuple[int, int]]) -> np.ndarray:
    a = unpack_symmetric(x, free)
    residual = a @ a - np.eye(N)
    return np.asarray([residual[i, j] for j in range(N) for i in range(j + 1)])


def refine_direct(
    initial_a: np.ndarray,
    h_edges: list[tuple[int, int]],
    g_edges: list[tuple[int, int]],
    max_nfev: int,
) -> dict[str, object]:
    free, _ = direct_parameterization(h_edges)
    fit = least_squares(
        direct_residual,
        pack_symmetric(initial_a, free),
        args=(free,),
        method="trf",
        ftol=1e-14,
        xtol=1e-14,
        gtol=1e-14,
        max_nfev=max_nfev,
    )
    a = unpack_symmetric(fit.x, free)
    eig = np.linalg.eigvalsh(a)
    metrics = matrix_metrics(a, h_edges, g_edges)
    singular_values = np.linalg.svd(fit.jac, compute_uv=False)
    rank_tolerance = (
        max(fit.jac.shape) * np.finfo(float).eps * singular_values[0]
        if singular_values.size
        else 0.0
    )
    jacobian_rank = int(np.sum(singular_values > rank_tolerance))
    diagnostic_rank_tolerance = 1e-7
    diagnostic_rank = int(np.sum(singular_values > diagnostic_rank_tolerance))
    return {
        "success_flag": bool(fit.success),
        "status": int(fit.status),
        "nfev": int(fit.nfev),
        "cost": float(fit.cost),
        "free_variables": len(free),
        "polynomial_equations": N * (N + 1) // 2,
        "jacobian_rank_default_svd_tolerance": jacobian_rank,
        "jacobian_nullity_default_svd_tolerance": len(free) - jacobian_rank,
        "jacobian_rank_tolerance": float(rank_tolerance),
        "jacobian_rank_at_1e-7": diagnostic_rank,
        "jacobian_nullity_at_1e-7": len(free) - diagnostic_rank,
        "jacobian_largest_singular_value": float(singular_values[0]),
        "jacobian_smallest_singular_value": float(singular_values[-1]),
        "eigenvalues": eig.tolist(),
        **metrics,
        "A": a.tolist(),
    }


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run(args: argparse.Namespace) -> None:
    script_dir = Path(__file__).resolve().parent
    graph6_path = args.graph6.resolve()
    lines = graph6_path.read_text(encoding="ascii").splitlines()
    rng = np.random.default_rng(args.seed)
    started = time.time()
    cases: list[dict[str, object]] = []

    for case_id, graph6 in enumerate(lines):
        n, adj = decode_graph6(graph6)
        if n != N:
            raise ValueError("only n=9 is accepted")
        h_edges = edges_from_adj(adj)
        g_edges = nonedges_from_adj(adj)
        case: dict[str, object] = {
            "case_id": case_id,
            "graph6": graph6,
            "h_edges": h_edges,
            "edge_count": edge_count(adj),
            "invariants": graph_invariants(adj),
            "ranks": {},
        }
        for rank in (3, 4):
            result = solve_stiefel(rank, h_edges, g_edges, rng, args.starts, args.max_nfev)
            initial_a = np.asarray(result["best"]["A"], dtype=float)
            result["direct_refinement"] = refine_direct(initial_a, h_edges, g_edges, args.max_nfev)
            case["ranks"][str(rank)] = result
        cases.append(case)
        print(
            f"{case_id:02d} e={len(h_edges)} g6={graph6} "
            + " ".join(
                f"r{r}:hits={case['ranks'][str(r)]['numerical_hit_count']}/{args.starts},"
                f"z={case['ranks'][str(r)]['best']['attempt']['max_forced_zero_error']:.1e},"
                f"nz={case['ranks'][str(r)]['best']['attempt']['min_required_nonzero_abs']:.1e}"
                for r in (3, 4)
            ),
            flush=True,
        )

    hardness: list[dict[str, object]] = []
    for case in cases:
        for rank_text, result in case["ranks"].items():
            attempt = result["best"]["attempt"]
            hardness.append(
                {
                    "case_id": case["case_id"],
                    "graph6": case["graph6"],
                    "rank": int(rank_text),
                    "numerical_hit_count": result["numerical_hit_count"],
                    "starts": result["starts"],
                    "best_forced_zero_error": attempt["max_forced_zero_error"],
                    "best_required_nonzero_margin": attempt["min_required_nonzero_abs"],
                    "median_nfev": float(np.median([item["nfev"] for item in result["attempts"]])),
                    "invariants": case["invariants"],
                }
            )
    hardness.sort(
        key=lambda item: (
            -int(item["starts"]) + int(item["numerical_hit_count"]),
            -float(item["best_forced_zero_error"]),
            float(item["best_required_nonzero_margin"]),
            -float(item["median_nfev"]),
        )
    )

    output = {
        "schema": "breaker-projection-discovery-v1",
        "warning": "FLOATING-POINT DISCOVERY ONLY; NOT A MATHEMATICAL CERTIFICATE",
        "scope": {"vertices": N, "ranks": [3, 4], "cases": len(cases)},
        "parameters": {
            "seed": args.seed,
            "starts_per_case_rank": args.starts,
            "max_nfev": args.max_nfev,
            "hit_thresholds": {
                "max_involution_error": 1e-9,
                "max_forced_zero_error": 1e-9,
                "min_required_nonzero_abs": 1e-7,
            },
        },
        "environment": {
            "command": " ".join(sys.argv),
            "python_executable": sys.executable,
            "python": sys.version,
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
            "blas_info": str(np.show_config),
            "thread_environment": {
                key: os.environ.get(key)
                for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")
            },
        },
        "input": {"path": str(graph6_path), "sha256": file_sha256(graph6_path)},
        "elapsed_seconds": time.time() - started,
        "hardness_order": hardness,
        "cases": cases,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph6", type=Path, default=script_dir / "breaker_n9_nonbip_e_le6.g6")
    parser.add_argument("--output", type=Path, default=script_dir / "breaker_projection_results.json")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--starts", type=int, default=12)
    parser.add_argument("--max-nfev", type=int, default=1600)
    run(parser.parse_args())


if __name__ == "__main__":
    main()
