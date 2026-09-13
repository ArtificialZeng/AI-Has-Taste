#!/usr/bin/env python3
"""Independent numerical counterexample search for central cube sections.

This is discovery code only.  It uses the exact box-spline polynomial on each
open chamber, but floating point root finding.  Nothing printed by this file
is a proof certificate.
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
from scipy.optimize import least_squares


def sign_data(m: int) -> tuple[np.ndarray, np.ndarray]:
    bits = np.array(list(itertools.product((0, 1), repeat=m)), dtype=int)
    linear = 0.5 - bits
    coeff = (-1.0) ** bits.sum(axis=1)
    return linear, coeff


def section_jet(a: np.ndarray) -> tuple[float, np.ndarray, np.ndarray, float]:
    """Return F, grad(log F), Hess(log F), and positive-part numerator.

    F(a)=||a|| f_{sum a_i U_i}(0) is homogeneous of degree zero.  The
    formula is evaluated in ordinary float64 and is therefore discovery-only.
    """
    a = np.asarray(a, dtype=float)
    m = len(a)
    if m < 2 or np.min(a) <= 0:
        raise ValueError("section_jet requires at least two positive coordinates")
    linear, coeff = sign_data(m)
    p = m - 1
    values = linear @ a
    active = values > 0.0
    lin = linear[active]
    c = coeff[active]
    val = values[active]
    G = float(c @ (val**p))
    grad_G = (c * p * val ** (p - 1)) @ lin
    if p >= 2:
        hess_G = np.einsum(
            "k,ki,kj->ij", c * p * (p - 1) * val ** (p - 2), lin, lin
        )
    else:
        hess_G = np.zeros((m, m))
    r2 = float(a @ a)
    F = math.sqrt(r2) * G / (math.factorial(p) * float(np.prod(a)))
    grad_log = a / r2 + grad_G / G - 1.0 / a
    hess_log = (
        np.eye(m) / r2
        - 2.0 * np.outer(a, a) / r2**2
        + hess_G / G
        - np.outer(grad_G, grad_G) / G**2
        + np.diag(1.0 / a**2)
    )
    return F, grad_log, hess_log, G


def tangent_eigenvalues(a: np.ndarray, F: float, hess_log: np.ndarray) -> np.ndarray:
    unit = a / np.linalg.norm(a)
    _, _, vh = np.linalg.svd(unit.reshape(1, -1))
    tangent_basis = vh[1:].T
    return np.linalg.eigvalsh(tangent_basis.T @ (F * hess_log) @ tangent_basis)


def canonical_unit(a: np.ndarray) -> np.ndarray:
    a = np.sort(np.abs(a))[::-1]
    return a / np.linalg.norm(a)


def residual(log_ratios: np.ndarray, m: int) -> np.ndarray:
    a = np.r_[1.0, np.exp(log_ratios)]
    try:
        _, grad_log, _, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.full(m - 1, 1e8)
    if G <= 1e-14 or not np.all(np.isfinite(grad_log)):
        return np.full(m - 1, 1e8)
    # Scale invariance gives a.grad_log=0 identically; these m-1 equations
    # are equivalent to the full stationary system when a_1=1.
    return grad_log[1:]


def residual_jacobian(log_ratios: np.ndarray, m: int) -> np.ndarray:
    a = np.r_[1.0, np.exp(log_ratios)]
    try:
        _, _, hess_log, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.eye(m - 1) * 1e8
    if G <= 1e-14 or not np.all(np.isfinite(hess_log)):
        return np.eye(m - 1) * 1e8
    # Chain rule: d q_i / d log(a_j) = Hess(log F)_{ij} a_j.
    return hess_log[1:, 1:] * a[None, 1:]


def search_support(m: int, starts: int, rng: np.random.Generator) -> list[dict]:
    if m == 1:
        return [{"a_unit": [1.0], "F": 1.0, "tangent_eigenvalues": []}]
    roots: list[dict] = []
    initial_points = [np.zeros(m - 1)]
    for index in range(starts):
        # Mix broad log-uniform coverage with a neighbourhood of the fully
        # supported diagonal, where bounded solvers otherwise converge slowly.
        if index % 4 == 0:
            x0 = np.sort(-np.abs(rng.normal(0.0, 0.45, m - 1)))[::-1]
        else:
            x0 = np.sort(rng.uniform(-5.0, 0.0, m - 1))[::-1]
        initial_points.append(x0)
    for x0 in initial_points:
        fit = least_squares(
            residual,
            x0,
            args=(m,),
            jac=residual_jacobian,
            bounds=(-7.0, 0.0),
            xtol=2e-13,
            ftol=2e-13,
            gtol=2e-13,
            max_nfev=1200,
        )
        a = canonical_unit(np.r_[1.0, np.exp(fit.x)])
        F, grad_log, hess_log, G = section_jet(a)
        if fit.cost > 2e-12 or np.max(np.abs(grad_log)) > 3e-6 or a[-1] < 1.1e-3:
            continue
        if any(np.linalg.norm(a - np.asarray(r["a_unit"])) < 2e-5 for r in roots):
            continue
        walls = []
        lin, _ = sign_data(m)
        for row in lin:
            w = float(row @ a)
            if abs(w) < 2e-7:
                walls.append(w)
        roots.append(
            {
                "a_unit": a.tolist(),
                "F": F,
                "max_abs_log_gradient": float(np.max(np.abs(grad_log))),
                "least_squares_cost": float(fit.cost),
                "tangent_eigenvalues": tangent_eigenvalues(a, F, hess_log).tolist(),
                "near_subset_sum_wall_values": walls,
                "positive_part_numerator": G,
            }
        )
    roots.sort(key=lambda r: tuple(-x for x in r["a_unit"]))
    return roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=140829)
    parser.add_argument("--starts", type=int, default=1200)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    results = {str(m): search_support(m, args.starts, rng) for m in range(1, 6)}
    payload = {
        "warning": "FLOATING-POINT DISCOVERY OUTPUT; NOT A CERTIFICATE",
        "method": "bounded log-ratio least_squares on exact chamber jets",
        "seed": args.seed,
        "starts_per_support": args.starts,
        "log_ratio_bounds": [-7.0, 0.0],
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "roots": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for m, roots in results.items():
        print(f"support {m}: {len(roots)} roots")
        for root in roots:
            print(np.array(root["a_unit"]), root["tangent_eigenvalues"])


if __name__ == "__main__":
    main()
