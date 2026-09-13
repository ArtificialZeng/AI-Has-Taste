#!/usr/bin/env python3
"""Discovery-only chamber enumeration and critical-point search for Q5.

This program is not a certificate.  It uses floating-point linear programming
and nonlinear least squares to locate structure.  Exact polynomials printed by
``--emit-singular`` are reconstructed from the graph mask, not from numerical
roots, and are intended as inputs to a later exact pipeline.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares, linprog
import sympy as sp


N = 5
PAIRS = tuple(itertools.combinations(range(N), 2))
PERMS = tuple(itertools.permutations(range(N)))


def permute_mask(mask: int, perm: tuple[int, ...]) -> int:
    edge = {tuple(sorted(PAIRS[k])) for k in range(len(PAIRS)) if mask >> k & 1}
    out = 0
    for k, (i, j) in enumerate(PAIRS):
        pre = tuple(sorted((perm[i], perm[j])))
        if pre in edge:
            out |= 1 << k
    return out


def canonical_mask(mask: int) -> int:
    return min(permute_mask(mask, p) for p in PERMS)


@dataclass(frozen=True)
class FeasibleMask:
    mask: int
    margin: float
    sample: tuple[float, ...]


def strict_feasible(mask: int) -> FeasibleMask | None:
    # Variables are a_0,...,a_4,t.  We maximize a common strict margin t.
    c = np.array([0.0] * N + [-1.0])
    aub: list[list[float]] = []
    bub: list[float] = []

    # a_i >= t and a_i <= 1-t (the latter is the strict polygon inequality).
    for i in range(N):
        row = [0.0] * (N + 1)
        row[i], row[-1] = -1.0, 1.0
        aub.append(row)
        bub.append(0.0)
        row = [0.0] * (N + 1)
        row[i], row[-1] = 1.0, 1.0
        aub.append(row)
        bub.append(1.0)

    for k, (i, j) in enumerate(PAIRS):
        row = [0.0] * (N + 1)
        if mask >> k & 1:  # active: a_i+a_j < 1
            row[i] = row[j] = 1.0
            row[-1] = 1.0
            rhs = 1.0
        else:
            row[i] = row[j] = -1.0
            row[-1] = 1.0
            rhs = -1.0
        aub.append(row)
        bub.append(rhs)

    aeq = np.array([[1.0] * N + [0.0]])
    beq = np.array([2.0])
    res = linprog(
        c,
        A_ub=np.asarray(aub),
        b_ub=np.asarray(bub),
        A_eq=aeq,
        b_eq=beq,
        bounds=[(0.0, None)] * N + [(0.0, None)],
        method="highs",
    )
    if not res.success or res.x[-1] <= 1e-9:
        return None
    return FeasibleMask(mask, float(res.x[-1]), tuple(map(float, res.x[:N])))


def active_mask(a: np.ndarray, tol: float = 0.0) -> int:
    ans = 0
    for k, (i, j) in enumerate(PAIRS):
        if a[i] + a[j] < 1.0 - tol:
            ans |= 1 << k
    return ans


def polynomial_for_mask(mask: int) -> tuple[sp.Expr, tuple[sp.Symbol, ...]]:
    x = sp.symbols("a0:4")
    a = (*x, 2 - sum(x))
    p = sp.Integer(1) - sum((1 - z) ** 4 for z in a)
    for k, (i, j) in enumerate(PAIRS):
        # Pair S and its complementary triple both occur in the full
        # inclusion--exclusion sum.  Exactly one has positive truncated
        # argument.  Hence their combined contribution is +L^4 when
        # L=1-a_i-a_j>0 and -L^4 when L<0.  Omitting the negative branch
        # creates false critical points, so keep both signs explicitly.
        sign = 1 if mask >> k & 1 else -1
        p += sign * (1 - a[i] - a[j]) ** 4
    return sp.factor(p), x


def critical_equations(mask: int) -> tuple[list[sp.Expr], sp.Expr, tuple[sp.Symbol, ...]]:
    p, x = polynomial_for_mask(mask)
    a = (*x, 2 - sum(x))
    q = sp.expand(sum(z * z for z in a))
    eqs = []
    for i, xi in enumerate(x):
        pi = sp.diff(p, xi)
        eq = (a[i] - a[4]) * p * (a[i] * a[4] + q) + q * a[i] * a[4] * pi
        eqs.append(sp.factor(eq))
    return eqs, p, x


def log_gradient_factory(mask: int):
    _, p, x = critical_equations(mask)
    a = (*x, 2 - sum(x))
    q = sum(z * z for z in a)
    d = sp.prod(a)
    logf = sp.log(q) / 2 + sp.log(p) - sp.log(d)
    gx = sp.Matrix([sp.diff(logf, z) for z in x])
    gxf = sp.lambdify(x, gx, "numpy")
    return gxf, p, x


def closure_admissible(mask: int, a: np.ndarray, tol: float = 2e-7) -> bool:
    if min(a) < -tol or max(a) > 1 + tol or abs(float(sum(a)) - 2) > tol:
        return False
    for k, (i, j) in enumerate(PAIRS):
        s = a[i] + a[j]
        if mask >> k & 1:
            if s > 1 + tol:
                return False
        elif s < 1 - tol:
            return False
    return True


def orbit_key(a: np.ndarray, digits: int = 7) -> tuple[float, ...]:
    return tuple(np.round(np.sort(a)[::-1], digits))


def tangent_hessian(mask: int, a: np.ndarray) -> np.ndarray:
    # Hessian of log F in affine sum=2 coordinates.  At a critical point it is
    # congruent, up to the positive factor F, to the Hessian of F.
    p, x = polynomial_for_mask(mask)
    avec = (*x, 2 - sum(x))
    q = sum(z * z for z in avec)
    d = sp.prod(avec)
    log_h = sp.hessian(sp.log(q) / 2 + sp.log(p) - sp.log(d), x)
    hf = sp.lambdify(x, log_h, "numpy")
    return np.asarray(hf(*a[:4]), dtype=float)


def search_mask(fm: FeasibleMask, seed: int, trials: int) -> list[dict]:
    rng = np.random.default_rng(seed + fm.mask)
    gxf, _, _ = log_gradient_factory(fm.mask)
    starts = [np.asarray(fm.sample[:4])]
    # Random Dirichlet points filtered into this labeled chamber.
    attempts = 0
    while len(starts) < trials and attempts < 500000:
        attempts += 1
        a = 2.0 * rng.dirichlet(np.ones(N))
        if max(a) >= 1.0 or active_mask(a) != fm.mask:
            continue
        starts.append(a[:4])
    # Local convex perturbations around the Chebyshev center add starts for
    # narrow chambers that random Dirichlet sampling rarely sees.
    center = np.asarray(fm.sample)
    while len(starts) < trials:
        b = 2.0 * rng.dirichlet(np.ones(N))
        lam = rng.uniform(0.0, 0.35)
        a = (1 - lam) * center + lam * b
        if max(a) < 1.0 and active_mask(a) == fm.mask:
            starts.append(a[:4])

    found: dict[tuple[float, ...], dict] = {}
    for x0 in starts:
        y0 = np.log(x0 / (2.0 - sum(x0)))

        def from_logits(y: np.ndarray) -> np.ndarray:
            z = np.r_[y, 0.0]
            z -= max(z)
            ez = np.exp(z)
            return 2.0 * ez / sum(ez)

        def gy(y: np.ndarray) -> np.ndarray:
            aa = from_logits(y)
            gx = np.asarray(gxf(*aa[:4]), dtype=float).reshape(4)
            jac = np.diag(aa[:4]) - np.outer(aa[:4], aa[:4]) / 2.0
            return jac.T @ gx

        try:
            res = least_squares(
                gy,
                y0,
                jac="3-point",
                xtol=1e-13,
                ftol=1e-13,
                gtol=1e-13,
                max_nfev=4000,
            )
        except (FloatingPointError, ValueError, OverflowError):
            continue
        a = from_logits(res.x)
        residual = float(np.linalg.norm(np.asarray(gxf(*a[:4]), dtype=float)))
        if min(a) < 1e-5 or residual > 1e-8 or not closure_admissible(fm.mask, a):
            continue
        key = orbit_key(a)
        try:
            eig = np.linalg.eigvalsh(tangent_hessian(fm.mask, a))
        except Exception:
            eig = np.full(4, np.nan)
        old = found.get(key)
        row = {
            "sorted_sum2": list(map(float, np.sort(a)[::-1])),
            "labeled_sum2": list(map(float, a)),
            "residual": residual,
            "hessian_logF_eigenvalues_affine": list(map(float, eig)),
            "on_pair_wall": bool(any(abs(a[i] + a[j] - 1) < 2e-6 for i, j in PAIRS)),
        }
        if old is None or residual < old["residual"]:
            found[key] = row
    return list(found.values())


def enumerate_masks() -> list[FeasibleMask]:
    all_feasible = [fm for mask in range(1 << len(PAIRS)) if (fm := strict_feasible(mask))]
    reps: dict[int, FeasibleMask] = {}
    for fm in all_feasible:
        cm = canonical_mask(fm.mask)
        candidate = strict_feasible(cm)
        if candidate is None:
            raise RuntimeError("canonical relabeling unexpectedly infeasible")
        if cm not in reps or candidate.margin > reps[cm].margin:
            reps[cm] = candidate
    return [reps[k] for k in sorted(reps)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20260829)
    ap.add_argument("--trials", type=int, default=80)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--no-search", action="store_true")
    args = ap.parse_args()

    reps = enumerate_masks()
    payload = {
        "warning": "DISCOVERY ONLY; floating point is not a proof certificate",
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "sympy": sp.__version__,
        },
        "seed": args.seed,
        "trials_per_canonical_labeled_chamber": args.trials,
        "pair_order": [list(e) for e in PAIRS],
        "canonical_chamber_count": len(reps),
        "chambers": [],
    }
    for fm in reps:
        p, _ = polynomial_for_mask(fm.mask)
        row = {
            "mask": fm.mask,
            "edges": [list(PAIRS[k]) for k in range(len(PAIRS)) if fm.mask >> k & 1],
            "lp_margin": fm.margin,
            "lp_sample_sum2": list(fm.sample),
            "P": str(p),
        }
        if not args.no_search:
            row["roots"] = search_mask(fm, args.seed, args.trials)
        payload["chambers"].append(row)
        print(f"mask={fm.mask:04x} margin={fm.margin:.6g} roots={len(row.get('roots', []))}")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
