#!/usr/bin/env python3
"""Four-sample normalized PEP for two gradient steps.

This script deliberately uses only NumPy/SciPy.  It builds all 12 directed
smooth-convex interpolation inequalities for samples (*,0,1,2), solves the
fixed-schedule primal through a Gram-factor parametrization, and solves the
Lagrange dual through a small nonlinear representation of its PSD slack.

Floating-point output is discovery evidence, not an exact certificate.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


LABELS = ("*", "0", "1", "2")
EDGES = tuple((i, j) for i in range(4) for j in range(4) if i != j)


def sym_outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (np.outer(a, b) + np.outer(b, a)) / 2.0


def pep_data(h1: float, h2: float):
    """Return (f coefficients, Gram coefficients) for q_ij >= 0."""
    e = np.eye(4)
    positions = (np.zeros(4), e[0], e[0] - h1 * e[1],
                 e[0] - h1 * e[1] - h2 * e[2])
    gradients = (np.zeros(4), e[1], e[2], e[3])
    # f variables are (f0,f1,f2); f_* is fixed to zero.
    fcoords = (np.zeros(3), np.eye(3)[0], np.eye(3)[1], np.eye(3)[2])
    avecs, amats = [], []
    for i, j in EDGES:
        avecs.append(fcoords[i] - fcoords[j])
        dg = gradients[i] - gradients[j]
        amats.append(
            -sym_outer(gradients[j], positions[i] - positions[j])
            - 0.5 * np.outer(dg, dg)
        )
    return np.asarray(avecs), np.asarray(amats)


def gram_factor(z: np.ndarray) -> np.ndarray:
    """Cholesky-type Gram parametrization with ||x0||=1."""
    a, b, c, d, e, p, q, r, s = z[:9]
    V = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [a, b, 0.0, 0.0],
        [c, d, e, 0.0],
        [p, q, r, s],
    ])
    return V @ V.T


def slacks(z: np.ndarray, avecs: np.ndarray, amats: np.ndarray) -> np.ndarray:
    G, f = gram_factor(z), z[9:12]
    return avecs @ f + np.einsum("kij,ij->k", amats, G)


def instance_start(h1: float, h2: float, kind: str) -> np.ndarray:
    z = np.zeros(12)
    if kind == "quadratic":
        gs = (1.0, 1.0 - h1, (1.0 - h1) * (1.0 - h2))
        z[[0, 2, 5]] = gs
        x1, x2 = 1.0 - h1, (1.0 - h1) * (1.0 - h2)
        z[9:12] = (0.5, 0.5 * x1 * x1, 0.5 * x2 * x2)
    elif kind == "huber":
        # This delta is tailored to the radical schedule; it remains a useful
        # feasible initialization nearby whenever all iterates stay linear.
        rt2 = math.sqrt(2.0)
        t = math.sqrt(9.0 + 8.0 * rt2)
        C = 1.0 / (5.0 + 4.0 * rt2 + t)
        delta = 2.0 * C
        x1 = 1.0 - h1 * delta
        x2 = x1 - h2 * delta
        z[[0, 2, 5]] = delta
        z[9:12] = tuple(delta * x - 0.5 * delta * delta for x in (1.0, x1, x2))
    return z


def solve_primal(h1: float, h2: float, starts: int = 24):
    avecs, amats = pep_data(h1, h2)
    cons = {"type": "ineq", "fun": lambda z: slacks(z, avecs, amats)}
    bounds = [(None, None)] * 12
    for k in (1, 4, 8):
        bounds[k] = (0.0, None)
    seeds = [instance_start(h1, h2, "quadratic"), instance_start(h1, h2, "huber")]
    rng = np.random.default_rng(2402)
    for _ in range(max(0, starts - len(seeds))):
        z = instance_start(h1, h2, "huber")
        z += rng.normal(scale=1e-3, size=12)
        z[[1, 4, 8]] = np.abs(z[[1, 4, 8]])
        # Start the nonlinear solver close to feasibility; SLSQP can restore it.
        seeds.append(z)
    sols = []
    for z0 in seeds:
        res = minimize(lambda z: -z[11], z0, method="SLSQP", bounds=bounds,
                       constraints=cons,
                       options={"ftol": 1e-13, "maxiter": 4000, "disp": False})
        if res.success and np.min(slacks(res.x, avecs, amats)) >= -2e-8:
            sols.append(res)
    if not sols:
        raise RuntimeError("no numerically feasible primal solution")
    res = min(sols, key=lambda r: r.fun)
    return res, gram_factor(res.x), slacks(res.x, avecs, amats)


def f_balance_matrix(avecs: np.ndarray) -> np.ndarray:
    return avecs.T


def dual_slack(y: np.ndarray, amats: np.ndarray) -> np.ndarray:
    lam, nu = y[:12], y[12]
    E00 = np.zeros((4, 4)); E00[0, 0] = 1.0
    return nu * E00 - np.einsum("k,kij->ij", lam, amats)


def solve_dual(h1: float, h2: float, starts: int = 36):
    avecs, amats = pep_data(h1, h2)
    B = f_balance_matrix(avecs)
    target = np.array([0.0, 0.0, -1.0])
    # Equal positive weights on reverse edges cancel; adding (*,2) creates -f2.
    base = np.ones(12)
    base[EDGES.index((0, 3))] += 1.0
    assert np.linalg.norm(B @ base - target) < 1e-12

    def eigs(y):
        return np.linalg.eigvalsh(dual_slack(y, amats))

    eq = {"type": "eq", "fun": lambda y: B @ y[:12] - target}
    psd = {"type": "ineq", "fun": eigs}
    bounds = [(0.0, None)] * 12 + [(0.0, None)]
    rng = np.random.default_rng(4242)
    seeds = []
    for k in range(starts):
        lam = base.copy()
        if k:
            # Symmetric reverse-edge perturbations preserve balance.
            for i, j in itertools.combinations(range(4), 2):
                w = math.exp(rng.normal(scale=1.0))
                lam[EDGES.index((i, j))] += w
                lam[EDGES.index((j, i))] += w
        seeds.append(np.r_[lam, 10.0 + k])

    # First restore PSD as well as possible, then minimize the bound.
    sols = []
    for y0 in seeds:
        phase1 = minimize(
            lambda y: y[12] + 1e3 * np.sum(np.minimum(eigs(y), 0.0) ** 2),
            y0, method="SLSQP", bounds=bounds, constraints=eq,
            options={"ftol": 1e-12, "maxiter": 3000, "disp": False})
        res = minimize(lambda y: y[12], phase1.x, method="SLSQP", bounds=bounds,
                       constraints=(eq, psd),
                       options={"ftol": 1e-13, "maxiter": 5000, "disp": False})
        if (np.linalg.norm(B @ res.x[:12] - target) <= 2e-7
                and np.min(eigs(res.x)) >= -2e-7):
            sols.append(res)
    if not sols:
        raise RuntimeError("no numerically feasible dual solution")
    res = min(sols, key=lambda r: r.x[12])
    return res, dual_slack(res.x, amats)


def summarize(h1: float, h2: float, starts: int):
    pres, G, qs = solve_primal(h1, h2, starts)
    dres, S = solve_dual(h1, h2, max(starts, 24))
    lam = dres.x[:12]
    return {
        "h": [h1, h2],
        "primal_value": float(pres.x[11]),
        "dual_value": float(dres.x[12]),
        "duality_gap": float(dres.x[12] - pres.x[11]),
        "gram": G.tolist(),
        "gram_eigenvalues": np.linalg.eigvalsh(G).tolist(),
        "function_values": pres.x[9:12].tolist(),
        "interpolation": [
            {"edge": LABELS[i] + "<-" + LABELS[j], "slack": float(q)}
            for (i, j), q in zip(EDGES, qs)
        ],
        "dual_multipliers": [
            {"edge": LABELS[i] + "<-" + LABELS[j], "lambda": float(x)}
            for (i, j), x in zip(EDGES, lam)
        ],
        "dual_slack": S.tolist(),
        "dual_slack_eigenvalues": np.linalg.eigvalsh(S).tolist(),
        "solver_note": "SciPy SLSQP factor/eigenvalue solve; floating-point discovery only",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--h1", type=float, default=math.sqrt(2.0))
    p.add_argument("--h2", type=float,
                   default=(3.0 + math.sqrt(9.0 + 8.0 * math.sqrt(2.0))) / 4.0)
    p.add_argument("--starts", type=int, default=32)
    args = p.parse_args()
    print(json.dumps(summarize(args.h1, args.h2, args.starts), indent=2))


if __name__ == "__main__":
    main()
