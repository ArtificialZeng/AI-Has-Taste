#!/usr/bin/env python3
"""Exact coefficient tests for the two e=6 charged-core series.

The computation starts from the nested beta-set criterion.  A charge-zero
6-core beta set A has, on runner i (1 <= i <= 6), first gap

    g_i = i + 6 a_i,       sum_i a_i = 0.

Thus ``(A+6) minus A`` is ``{g_1,...,g_6}``.  A beta set B of charge t satisfying
A subset B subset A+6 is obtained by adjoining exactly t of those gaps.
The standard beta-set size formula is evaluated below as an integer formula.

For an independent check of equation (5.3), the ordinary 3-core series is
expanded from (q^3;q^3)_infinity^3/(q;q)_infinity, not from charged cores.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


def core_size(a: tuple[int, ...], e: int) -> int:
    """Size of the e-core with first gaps i+e*a_i, i=1,...,e."""
    assert len(a) == e and sum(a) == 0
    return (e * sum(x * x for x in a)) // 2 + sum(
        (i + 1) * x for i, x in enumerate(a)
    )


def safe_box_radius(max_degree: int, e: int) -> int:
    """Return B such that every charge-zero e-core of size <= N has |a_i|<=B.

    On the sum-zero hyperplane, Cauchy--Schwarz gives
      |sum i*a_i| <= sqrt(sum(i-(e+1)/2)^2) * ||a||_2.
    Hence |lambda| >= (e/2)||a||^2-C||a||.  We choose B so that a
    coordinate of magnitude B+1 forces this lower bound above max_degree.
    """
    centered_sq = sum((i - (e + 1) / 2) ** 2 for i in range(1, e + 1))
    c = math.sqrt(centered_sq)
    b = 0
    while (e / 2) * (b + 1) ** 2 - c * (b + 1) <= max_degree:
        b += 1
    return b


def charged_coefficients(max_degree: int, t: int) -> tuple[list[int], int, int]:
    """Enumerate c_{6,(0,t)} through max_degree exactly."""
    if t not in (1, 3):
        raise ValueError("this job only needs t=1 or t=3")
    e = 6
    radius = safe_box_radius(max_degree, e)
    coeff = [0] * (max_degree + 1)
    core_vectors = 0
    witnesses = 0
    for first_five in itertools.product(range(-radius, radius + 1), repeat=5):
        a = first_five + (-sum(first_five),)
        if abs(a[-1]) > radius:
            continue
        size1 = core_size(a, e)
        if size1 > max_degree:
            continue
        core_vectors += 1
        gaps = tuple(i + e * a[i - 1] for i in range(1, e + 1))
        for chosen in itertools.combinations(range(e), t):
            # Adding t beta numbers x to a charge-zero beta set changes the
            # partition size by sum(x)-t(t+1)/2.
            size2 = size1 + sum(gaps[j] for j in chosen) - t * (t + 1) // 2
            assert size2 >= 0
            degree = size1 + size2
            if degree <= max_degree:
                coeff[degree] += 1
                witnesses += 1
    return coeff, radius, core_vectors


def multiply_truncated(a: list[int], b: list[int], n: int) -> list[int]:
    out = [0] * (n + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[: n + 1 - i]):
                if y:
                    out[i + j] += x * y
    return out


def three_core_coefficients(max_degree: int) -> list[int]:
    """Expand (q^3;q^3)_infinity^3/(q;q)_infinity through q^N."""
    # First expand 1/(q;q)_infinity by the usual in-place partition DP.
    series = [0] * (max_degree + 1)
    series[0] = 1
    for k in range(1, max_degree + 1):
        for n in range(k, max_degree + 1):
            series[n] += series[n - k]
    # Multiply by each relevant (1-q^(3k))^3.
    for k in range(1, max_degree // 3 + 1):
        d = 3 * k
        factor = [0] * (max_degree + 1)
        factor[0] = 1
        for j, value in enumerate((1, -3, 3, -1)):
            if j * d <= max_degree:
                factor[j * d] = value
        series = multiply_truncated(series, factor, max_degree)
    return series


def phi_coefficients(max_degree: int) -> list[int]:
    out = [0] * (max_degree + 1)
    r = math.isqrt(max_degree)
    for a in range(-r, r + 1):
        out[a * a] += 1
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=250)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    nmax = args.max_degree

    c01, radius1, cores1 = charged_coefficients(nmax, 1)
    c03, radius3, cores3 = charged_coefficients(nmax, 3)
    c3 = three_core_coefficients(nmax)
    lhs = multiply_truncated(phi_coefficients(nmax), multiply_truncated(c3, c3, nmax), nmax)
    rhs = [c03[n] + (2 * c01[n - 1] if n else 0) for n in range(nmax + 1)]
    mismatches = [n for n in range(nmax + 1) if lhs[n] != rhs[n]]
    zeros01 = [n for n, value in enumerate(c01) if value == 0]
    zeros03 = [n for n, value in enumerate(c03) if value == 0]

    result = {
        "max_degree": nmax,
        "box_radius": {"(0,1)": radius1, "(0,3)": radius3},
        "six_core_vectors_considered_after_size_cut": {
            "(0,1)": cores1,
            "(0,3)": cores3,
        },
        "equation_5_3_mismatches": mismatches,
        "zero_coefficients": {"(0,1)": zeros01, "(0,3)": zeros03},
        "first_80_coefficients": {"(0,1)": c01[:81], "(0,3)": c03[:81]},
        "congruence_minima_mod_6": {
            "(0,1)": [min(c01[r::6]) for r in range(6)],
            "(0,3)": [min(c03[r::6]) for r in range(6)],
        },
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
