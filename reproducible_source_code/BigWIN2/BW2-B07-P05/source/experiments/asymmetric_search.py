#!/usr/bin/env python3
"""Deterministic falsification search outside the three-parameter ansatz.

This is discovery code only.  It optimizes within the orientation chamber of
each start and evaluates every retained candidate by two determinant formulas.
The output explicitly carries no global-optimality claim.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import minimize


TRIPLES = np.array(list(itertools.combinations(range(10), 3)), dtype=int)
SEED = 20260830


def determinants_cross(flat: np.ndarray) -> np.ndarray:
    points = flat.reshape(10, 2)
    a = points[TRIPLES[:, 0]]
    b = points[TRIPLES[:, 1]]
    c = points[TRIPLES[:, 2]]
    return ((b[:, 0] - a[:, 0]) * (c[:, 1] - a[:, 1])
            - (b[:, 1] - a[:, 1]) * (c[:, 0] - a[:, 0]))


def determinants_shoelace(flat: np.ndarray) -> np.ndarray:
    points = flat.reshape(10, 2)
    a = points[TRIPLES[:, 0]]
    b = points[TRIPLES[:, 1]]
    c = points[TRIPLES[:, 2]]
    return (a[:, 0] * (b[:, 1] - c[:, 1])
            + b[:, 0] * (c[:, 1] - a[:, 1])
            + c[:, 0] * (a[:, 1] - b[:, 1]))


def minimum_area(flat: np.ndarray) -> float:
    first = determinants_cross(flat)
    second = determinants_shoelace(flat)
    if not np.allclose(first, second, rtol=0.0, atol=2e-15):
        raise AssertionError("independent determinant evaluators disagree")
    return float(np.min(np.abs(first)) / 2)


def incumbent() -> tuple[np.ndarray, float]:
    roots = np.roots([12.0, -27.0, 20.0, -4.0])
    z = float(roots[np.argmin(np.abs(roots.imag))].real)
    x = z / 2
    y = (1 - z) * (1 - 2 * z)
    points = np.array([
        (x, 0), (1 - y, 0), (0, x), (1, y), (1 - z, z),
        (z, 1 - z), (0, 1 - y), (1, 1 - x), (y, 1), (1 - x, 1)
    ], dtype=float).ravel()
    return points, minimum_area(points)


def eight_boundary_start(rng: np.random.Generator) -> np.ndarray:
    points = []
    for edge in range(4):
        for value in rng.random(2):
            if edge == 0:
                points.append((value, 0.0))
            elif edge == 1:
                points.append((1.0, value))
            elif edge == 2:
                points.append((value, 1.0))
            else:
                points.append((0.0, value))
    points.extend(map(tuple, rng.random((2, 2))))
    rng.shuffle(points)
    return np.array(points, dtype=float).ravel()


def five_boundary_start(rng: np.random.Generator) -> np.ndarray:
    a, b, c, d, e = rng.random(5)
    if a > e:
        a, e = e, a
    boundary = [(0.0, a), (b, 0.0), (1.0, c), (d, 1.0), (0.0, e)]
    points = boundary + list(map(tuple, rng.random((5, 2))))
    rng.shuffle(points)
    return np.array(points, dtype=float).ravel()


def optimize(start: np.ndarray) -> dict:
    signs = np.where(determinants_cross(start) >= 0, 1.0, -1.0)
    initial = np.concatenate([start, [minimum_area(start)]])

    def constraints(vector: np.ndarray) -> np.ndarray:
        return signs * determinants_cross(vector[:-1]) / 2 - vector[-1]

    result = minimize(
        lambda vector: -vector[-1],
        initial,
        method="SLSQP",
        bounds=[(0.0, 1.0)] * 20 + [(0.0, 0.06)],
        constraints={"type": "ineq", "fun": constraints},
        options={"maxiter": 1000, "ftol": 1e-12, "disp": False},
    )
    actual = minimum_area(result.x[:-1])
    return {
        "success": bool(result.success),
        "iterations": int(result.nit),
        "reported_t": float(result.x[-1]),
        "actual_minimum_area": actual,
        "points": result.x[:-1].reshape(10, 2).tolist(),
    }


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("asymmetric_search_result.json")
    rng = np.random.default_rng(SEED)
    incumbent_points, incumbent_area = incumbent()
    starts: list[tuple[str, np.ndarray]] = []
    for scale in (1e-5, 1e-4, 1e-3, 1e-2):
        for _ in range(10):
            starts.append((f"incumbent_perturb_{scale:g}",
                           np.clip(incumbent_points + rng.normal(0, scale, 20), 0, 1)))
    starts.extend(("uniform", rng.random(20)) for _ in range(100))
    starts.extend(("eight_boundary", eight_boundary_start(rng)) for _ in range(100))
    starts.extend(("five_boundary", five_boundary_start(rng)) for _ in range(100))

    summaries = {}
    for category, start in starts:
        result = optimize(start)
        record = summaries.setdefault(category, {
            "starts": 0, "solver_successes": 0, "best_actual_minimum_area": -1.0,
            "best_points": None, "best_iterations": None
        })
        record["starts"] += 1
        record["solver_successes"] += int(result["success"])
        if result["actual_minimum_area"] > record["best_actual_minimum_area"]:
            record["best_actual_minimum_area"] = result["actual_minimum_area"]
            record["best_points"] = result["points"]
            record["best_iterations"] = result["iterations"]

    global_best = max(record["best_actual_minimum_area"] for record in summaries.values())
    result = {
        "schema": "heilbronn-square-ten-asymmetric-search-v1",
        "status": "diagnostic_only",
        "global_optimality_claim": False,
        "seed": SEED,
        "start_count": len(starts),
        "objective": "minimum of all 120 unsigned Euclidean triangle areas",
        "method": "SLSQP in the orientation chamber of each start",
        "incumbent_area_float64": incumbent_area,
        "best_area_float64": global_best,
        "beat_incumbent_by_1e-9": bool(global_best > incumbent_area + 1e-9),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
        },
        "categories": summaries,
        "limitations": [
            "local optimization only",
            "orientation signs fixed from each start",
            "floating-point output is not a proof or certificate"
        ]
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"], "start_count": len(starts),
        "incumbent_area_float64": incumbent_area, "best_area_float64": global_best,
        "beat_incumbent_by_1e-9": result["beat_incumbent_by_1e-9"],
        "output": str(output)
    }, sort_keys=True))


if __name__ == "__main__":
    main()
