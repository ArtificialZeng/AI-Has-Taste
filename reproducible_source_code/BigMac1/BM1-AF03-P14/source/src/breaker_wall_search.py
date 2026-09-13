#!/usr/bin/env python3
"""Numerical search for full critical points on Q5 subset-sum walls.

Every wall is permutation-equivalent to a 1|4 or 2|3 partition.  Positive
coordinates on each side are softmax-parameterized to have sum 1/2, so the
wall equation is exact in floating point up to summation roundoff.  The full
five-component log-gradient is minimized; this is an overdetermined search
because wall membership alone does not weaken the ambient criticality test.
Output is discovery evidence only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares

from breaker_search import canonical_unit, section_jet, tangent_eigenvalues


def softmax_with_fixed_zero(parameters: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    logits = np.r_[0.0, parameters]
    logits -= logits.max()
    exponentials = np.exp(logits)
    weights = exponentials / exponentials.sum()
    jac = np.empty((len(weights), len(parameters)))
    for i in range(len(weights)):
        for column, j in enumerate(range(1, len(weights))):
            jac[i, column] = weights[i] * ((1.0 if i == j else 0.0) - weights[j])
    return weights, jac


def wall_point(parameters: np.ndarray, left_size: int) -> tuple[np.ndarray, np.ndarray]:
    left_parameters = parameters[: left_size - 1]
    right_parameters = parameters[left_size - 1 :]
    left, left_jac = softmax_with_fixed_zero(left_parameters)
    right, right_jac = softmax_with_fixed_zero(right_parameters)
    a = 0.5 * np.r_[left, right]
    jac = np.zeros((5, 3))
    if left_size > 1:
        jac[:left_size, : left_size - 1] = 0.5 * left_jac
    jac[left_size:, left_size - 1 :] = 0.5 * right_jac
    return a, jac


def residual(parameters: np.ndarray, left_size: int) -> np.ndarray:
    a, _ = wall_point(parameters, left_size)
    try:
        _, q, _, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.full(5, 1e8)
    if G <= 1e-14 or not np.all(np.isfinite(q)):
        return np.full(5, 1e8)
    return q


def jacobian(parameters: np.ndarray, left_size: int) -> np.ndarray:
    a, da = wall_point(parameters, left_size)
    try:
        _, _, H, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.full((5, 3), 1e8)
    if G <= 1e-14 or not np.all(np.isfinite(H)):
        return np.full((5, 3), 1e8)
    return H @ da


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=77140829)
    parser.add_argument("--starts", type=int, default=3000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    output: dict[str, list[dict]] = {}
    for left_size in (1, 2):
        retained: list[dict] = []
        initial_points = [np.zeros(3)]
        initial_points.extend(rng.uniform(-6, 6, size=(args.starts, 3)))
        for x0 in initial_points:
            fit = least_squares(
                residual,
                x0,
                jac=jacobian,
                args=(left_size,),
                bounds=(-10.0, 10.0),
                xtol=2e-13,
                ftol=2e-13,
                gtol=2e-13,
                max_nfev=1500,
            )
            a, _ = wall_point(fit.x, left_size)
            F, q, H, _ = section_jet(a)
            candidate = {
                "a_unit": canonical_unit(a).tolist(),
                "raw_partitioned_a": a.tolist(),
                "wall_residual": float(a[:left_size].sum() - a[left_size:].sum()),
                "gradient_l2": float(np.linalg.norm(q)),
                "gradient_linf": float(np.max(np.abs(q))),
                "least_squares_cost": float(fit.cost),
                "F": F,
                "tangent_eigenvalues": tangent_eigenvalues(a, F, H).tolist(),
            }
            if any(
                np.linalg.norm(np.asarray(candidate["a_unit"]) - np.asarray(old["a_unit"])) < 2e-5
                for old in retained
            ):
                continue
            retained.append(candidate)
            retained.sort(key=lambda row: row["gradient_l2"])
            retained = retained[:25]
        output[f"{left_size}|{5-left_size}"] = retained
    payload = {
        "warning": "FLOATING-POINT WALL SEARCH; NOT A CERTIFICATE",
        "method": "softmax parameterization of 1|4 and 2|3 walls; full ambient gradient residual",
        "seed": args.seed,
        "starts_per_wall_type": args.starts,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "retained": output,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for wall, rows in output.items():
        print(wall, "best gradient", rows[0]["gradient_l2"], "at", rows[0]["a_unit"])


if __name__ == "__main__":
    main()
