#!/usr/bin/env python3
"""Geometric cross-check of the Q_m section formula via edge intersections.

Unlike breaker_search.py, this evaluator never uses the box-spline formula.
It enumerates cube-edge intersections with the central hyperplane, projects
them to an orthonormal basis, and asks Qhull for the convex-hull volume.
The comparison remains a floating-point diagnostic, not a certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def edge_vertices(a: np.ndarray) -> np.ndarray:
    m = len(a)
    points: list[np.ndarray] = []
    for varying in range(m):
        fixed = [j for j in range(m) if j != varying]
        for signs in itertools.product((-0.5, 0.5), repeat=m - 1):
            x = np.zeros(m)
            x[fixed] = signs
            x[varying] = -float(a[fixed] @ x[fixed]) / float(a[varying])
            if -0.5 - 2e-13 <= x[varying] <= 0.5 + 2e-13:
                x[varying] = min(0.5, max(-0.5, x[varying]))
                points.append(x)
    # Coincident intersections occur on subset-sum walls.
    unique: list[np.ndarray] = []
    for point in points:
        if not any(np.linalg.norm(point - old, ord=np.inf) < 1e-11 for old in unique):
            unique.append(point)
    return np.asarray(unique)


def geometric_volume(a: np.ndarray) -> tuple[float, int]:
    a = np.asarray(a, dtype=float)
    unit = a / np.linalg.norm(a)
    basis = null_space(unit.reshape(1, -1))
    vertices = edge_vertices(a)
    projected = vertices @ basis
    if len(a) == 2:
        volume = float(projected.max() - projected.min())
    else:
        volume = float(ConvexHull(projected, qhull_options="Qt").volume)
    return volume, len(vertices)


def box_spline_volume(a: np.ndarray) -> float:
    m = len(a)
    total = 0.0
    A = float(a.sum())
    for bits in itertools.product((0, 1), repeat=m):
        linear = A / 2.0 - sum(a[i] for i, bit in enumerate(bits) if bit)
        if linear > 0:
            total += (-1.0) ** sum(bits) * linear ** (m - 1)
    return np.linalg.norm(a) * total / (math.factorial(m - 1) * np.prod(a))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=512140829)
    parser.add_argument("--random", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    cases: list[dict] = []
    t = (24.0 - math.sqrt(69.0)) / 39.0
    special = [np.ones(5), np.array([1.0, 1.0, t, t, t])]
    for m in range(2, 6):
        vectors = [np.ones(m)]
        if m == 5:
            vectors.extend(special)
        vectors.extend(rng.uniform(0.25, 1.0, size=(args.random, m)))
        for a in vectors:
            geom, count = geometric_volume(a)
            spline = box_spline_volume(a)
            cases.append(
                {
                    "support": m,
                    "a": a.tolist(),
                    "geometric": geom,
                    "box_spline": spline,
                    "absolute_error": abs(geom - spline),
                    "relative_error": abs(geom - spline) / spline,
                    "vertex_count": count,
                }
            )
    payload = {
        "warning": "FLOATING-POINT CROSS-CHECK; NOT A CERTIFICATE",
        "method": "cube-edge intersections + orthogonal projection + Qhull",
        "seed": args.seed,
        "random_cases_per_support": args.random,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "maximum_absolute_error": max(c["absolute_error"] for c in cases),
        "maximum_relative_error": max(c["relative_error"] for c in cases),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in payload.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
