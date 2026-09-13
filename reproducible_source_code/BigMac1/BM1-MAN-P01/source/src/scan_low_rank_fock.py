#!/usr/bin/env python3
"""Numerical discovery scan for the real Bapat--Sunder F_A problem.

This is deliberately a discovery engine.  It evaluates permanental minors of
a real Gram matrix through the exact symmetric-tensor identity

    per(A(i,j)) = sum_{|alpha|=n-1} alpha! c[i,alpha] c[j,alpha],

where prod_{k != i} <x_k,z> = sum_alpha c[i,alpha] z^alpha.
No floating-point output from this file is a theorem or final certificate.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def polynomial_without(vectors: np.ndarray, omitted: int) -> dict[tuple[int, ...], float]:
    rank = vectors.shape[1]
    poly: dict[tuple[int, ...], float] = {(0,) * rank: 1.0}
    for index, vector in enumerate(vectors):
        if index == omitted:
            continue
        nxt: dict[tuple[int, ...], float] = {}
        for exponent, coefficient in poly.items():
            for coordinate, value in enumerate(vector):
                if value == 0.0:
                    continue
                new_exponent = list(exponent)
                new_exponent[coordinate] += 1
                key = tuple(new_exponent)
                nxt[key] = nxt.get(key, 0.0) + coefficient * float(value)
        poly = nxt
    return poly


def fock_f_matrix(vectors: np.ndarray) -> tuple[float, np.ndarray, float]:
    norms = np.linalg.norm(vectors, axis=1)
    if np.any(norms == 0):
        raise ValueError("zero Gram vector")
    vectors = vectors / norms[:, None]
    polynomials = [polynomial_without(vectors, i) for i in range(len(vectors))]
    monomials = sorted(set().union(*(poly.keys() for poly in polynomials)))
    weights = np.array(
        [math.prod(math.factorial(value) for value in exponent) for exponent in monomials],
        dtype=float,
    )
    coefficients = np.array(
        [[poly.get(exponent, 0.0) for exponent in monomials] for poly in polynomials],
        dtype=float,
    )
    minor_gram = (coefficients * weights) @ coefficients.T
    gram = vectors @ vectors.T
    f_matrix = gram * minor_gram
    row_sums = f_matrix.sum(axis=1)
    permanent = float(np.mean(row_sums))
    row_sum_relative_error = float(np.max(np.abs(row_sums - permanent)) / max(1.0, abs(permanent)))
    return permanent, f_matrix, row_sum_relative_error


def ratio(vectors: np.ndarray) -> tuple[float, float, float]:
    permanent, f_matrix, row_error = fock_f_matrix(vectors)
    eigenvalues = np.linalg.eigvalsh((f_matrix + f_matrix.T) / 2.0)
    return float(eigenvalues[-1] / permanent), float(eigenvalues[-2] / permanent), row_error


def mutate(vectors: np.ndarray, scale: float, rng: np.random.Generator) -> np.ndarray:
    proposal = vectors + scale * rng.normal(size=vectors.shape)
    return proposal / np.linalg.norm(proposal, axis=1)[:, None]


def search(n: int, rank: int, restarts: int, steps: int, seed: int) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    best_ratio = -math.inf
    best_second = -math.inf
    best_vectors: np.ndarray | None = None
    evaluations = 0
    for _ in range(restarts):
        current = rng.normal(size=(n, rank))
        current /= np.linalg.norm(current, axis=1)[:, None]
        current_ratio, current_second, _ = ratio(current)
        evaluations += 1
        scale = 0.25
        for step in range(steps):
            candidate = mutate(current, scale, rng)
            candidate_ratio, candidate_second, _ = ratio(candidate)
            evaluations += 1
            # The top eigenvalue is always at least the permanent.  Until a
            # violation appears, maximize the second eigenvalue instead of
            # numerical noise in the trivial top eigenvalue.
            current_score = current_ratio if current_ratio > 1.0 + 1e-9 else current_second
            candidate_score = candidate_ratio if candidate_ratio > 1.0 + 1e-9 else candidate_second
            if candidate_score > current_score:
                current = candidate
                current_ratio = candidate_ratio
                current_second = candidate_second
            scale = max(0.002, 0.25 * (0.999 ** step))
        if current_ratio > best_ratio + 1e-12 or (
            abs(current_ratio - best_ratio) <= 1e-12 and current_second > best_second
        ):
            best_ratio = current_ratio
            best_second = current_second
            best_vectors = current.copy()
    assert best_vectors is not None
    permanent, f_matrix, row_error = fock_f_matrix(best_vectors)
    eigenvalues = np.linalg.eigvalsh((f_matrix + f_matrix.T) / 2.0)
    return {
        "n": n,
        "rank": rank,
        "seed": seed,
        "restarts": restarts,
        "steps_per_restart": steps,
        "evaluations": evaluations,
        "best_top_ratio": float(eigenvalues[-1] / permanent),
        "best_second_ratio": float(eigenvalues[-2] / permanent),
        "row_sum_relative_error": row_error,
        "strict_candidate": bool(eigenvalues[-1] > permanent * (1.0 + 1e-8)),
        "vectors": best_vectors.tolist(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--rank", type=int, required=True)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20260827)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (2 <= args.rank <= args.n):
        raise SystemExit("require 2 <= rank <= n")
    result = search(args.n, args.rank, args.restarts, args.steps, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "vectors"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
