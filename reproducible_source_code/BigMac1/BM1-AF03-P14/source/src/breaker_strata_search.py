#!/usr/bin/env python3
"""Floating-point search on every repeated-coordinate stratum for Q_m, m<=5.

For every integer partition of a support size, all assignments of group
multiplicities to the largest coordinate group are tried.  Exact permutation
symmetry turns the reduced stationary equations into the full equations.
This is broad discovery evidence, not an exhaustive exact certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares

from breaker_search import canonical_unit, section_jet, sign_data, tangent_eigenvalues


def integer_partitions(total: int, maximum: int | None = None):
    maximum = total if maximum is None else min(maximum, total)
    if total == 0:
        yield ()
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def compositions_from_partition(partition: tuple[int, ...]):
    yield from sorted(set(itertools.permutations(partition)))


def expand(log_ratios: np.ndarray, multiplicities: tuple[int, ...]) -> tuple[np.ndarray, np.ndarray]:
    values = np.r_[1.0, np.exp(log_ratios)]
    return np.repeat(values, multiplicities), values


def reduced_residual(log_ratios: np.ndarray, multiplicities: tuple[int, ...]) -> np.ndarray:
    a, _ = expand(log_ratios, multiplicities)
    try:
        _, q, _, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.full(len(multiplicities) - 1, 1e8)
    if G <= 1e-14 or not np.all(np.isfinite(q)):
        return np.full(len(multiplicities) - 1, 1e8)
    representatives = np.cumsum((0,) + multiplicities[:-1])
    return q[representatives[1:]]


def reduced_jacobian(log_ratios: np.ndarray, multiplicities: tuple[int, ...]) -> np.ndarray:
    a, values = expand(log_ratios, multiplicities)
    try:
        _, _, H, G = section_jet(a)
    except (FloatingPointError, ValueError, ZeroDivisionError):
        return np.eye(len(multiplicities) - 1) * 1e8
    if G <= 1e-14 or not np.all(np.isfinite(H)):
        return np.eye(len(multiplicities) - 1) * 1e8
    starts = np.cumsum((0,) + multiplicities[:-1])
    answer = np.empty((len(multiplicities) - 1, len(multiplicities) - 1))
    for row, representative in enumerate(starts[1:]):
        for column, (start, width) in enumerate(zip(starts[1:], multiplicities[1:])):
            answer[row, column] = values[column + 1] * H[representative, start : start + width].sum()
    return answer


def search_composition(
    multiplicities: tuple[int, ...], starts: int, rng: np.random.Generator
) -> list[dict]:
    groups = len(multiplicities)
    if groups == 1:
        initial_points = [np.empty(0)]
    else:
        initial_points = [np.zeros(groups - 1)]
        for index in range(starts):
            if index % 3 == 0:
                x0 = -np.abs(rng.normal(0, 0.6, groups - 1))
            else:
                x0 = rng.uniform(-5, 0, groups - 1)
            initial_points.append(x0)
    roots: list[dict] = []
    for x0 in initial_points:
        if groups == 1:
            a = np.ones(sum(multiplicities))
            fit_cost = 0.0
        else:
            fit = least_squares(
                reduced_residual,
                x0,
                jac=reduced_jacobian,
                args=(multiplicities,),
                bounds=(-7.0, 0.0),
                xtol=2e-13,
                ftol=2e-13,
                gtol=2e-13,
                max_nfev=1500,
            )
            a, _ = expand(fit.x, multiplicities)
            fit_cost = float(fit.cost)
        a = canonical_unit(a)
        F, q, H, G = section_jet(a)
        if fit_cost > 5e-12 or np.max(np.abs(q)) > 4e-6 or a[-1] < 1.1e-3:
            continue
        if any(np.linalg.norm(a - np.asarray(root["a_unit"])) < 3e-5 for root in roots):
            continue
        linear, _ = sign_data(len(a))
        wall_values = [float(value) for value in linear @ a if abs(value) < 2e-7]
        roots.append(
            {
                "a_unit": a.tolist(),
                "F": F,
                "max_abs_log_gradient": float(np.max(np.abs(q))),
                "least_squares_cost": fit_cost,
                "tangent_eigenvalues": tangent_eigenvalues(a, F, H).tolist(),
                "near_subset_sum_wall_values": wall_values,
                "positive_part_numerator": G,
            }
        )
    return roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=99140829)
    parser.add_argument("--starts", type=int, default=500)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    strata: list[dict] = []
    canonical: dict[str, list[dict]] = {str(m): [] for m in range(2, 6)}
    for m in range(2, 6):
        for partition in integer_partitions(m):
            for multiplicities in compositions_from_partition(partition):
                roots = search_composition(multiplicities, args.starts, rng)
                strata.append({"support": m, "multiplicities": multiplicities, "roots": roots})
                for root in roots:
                    if not any(
                        np.linalg.norm(np.asarray(root["a_unit"]) - np.asarray(old["a_unit"])) < 3e-5
                        for old in canonical[str(m)]
                    ):
                        combined = dict(root)
                        combined["first_found_multiplicities"] = multiplicities
                        canonical[str(m)].append(combined)
    for roots in canonical.values():
        roots.sort(key=lambda root: tuple(-x for x in root["a_unit"]))
    payload = {
        "warning": "FLOATING-POINT STRATIFIED DISCOVERY OUTPUT; NOT A CERTIFICATE",
        "method": "all integer multiplicity partitions, reduced symmetry equations",
        "seed": args.seed,
        "starts_per_ordered_multiplicity_composition": args.starts,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "canonical_roots": canonical,
        "strata": strata,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for m, roots in canonical.items():
        print(f"support {m}: {len(roots)} canonical roots")
        for root in roots:
            print(root["a_unit"], root["tangent_eigenvalues"], root["first_found_multiplicities"])


if __name__ == "__main__":
    main()
