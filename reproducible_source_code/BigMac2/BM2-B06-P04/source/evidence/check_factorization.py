#!/usr/bin/env python3
"""Held-out exact test of the product suggested for c_{6,(0,1)}."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from enumerate_series import charged_coefficients, multiply_truncated, three_core_coefficients


def psi(max_degree: int, scale: int = 1) -> list[int]:
    """Coefficients of psi(q^scale)=sum_{k>=0}q^(scale*k*(k+1)/2)."""
    out = [0] * (max_degree + 1)
    k = 0
    while scale * k * (k + 1) // 2 <= max_degree:
        out[scale * k * (k + 1) // 2] = 1
        k += 1
    return out


def dilate(series: list[int], scale: int, max_degree: int) -> list[int]:
    out = [0] * (max_degree + 1)
    for n, value in enumerate(series):
        if scale * n <= max_degree:
            out[scale * n] = value
    return out


def universal_subfamily_misses(max_degree: int) -> list[int]:
    """Test n=x^2+y(y+1)+2z^2, the proposed positivity subfamily."""
    hit = bytearray(max_degree + 1)
    for x in range(math.isqrt(max_degree) + 1):
        x2 = x * x
        y = 0
        while x2 + y * (y + 1) <= max_degree:
            base = x2 + y * (y + 1)
            for z in range(math.isqrt((max_degree - base) // 2) + 1):
                hit[base + 2 * z * z] = 1
            y += 1
    return [n for n, value in enumerate(hit) if not value]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=500)
    parser.add_argument("--subfamily-bound", type=int, default=10000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    nmax = args.max_degree

    charged, radius, core_count = charged_coefficients(nmax, 1)
    c3 = dilate(three_core_coefficients(nmax // 2), 2, nmax)
    proposed = multiply_truncated(
        multiply_truncated(psi(nmax), psi(nmax), nmax),
        multiply_truncated(c3, psi(nmax, 6), nmax),
        nmax,
    )
    result = {
        "max_degree": nmax,
        "box_radius": radius,
        "six_core_vectors_after_size_cut": core_count,
        "proposed_identity": "c_6,(0,1)(q) = psi(q)^2 c_3(q^2) psi(q^6)",
        "mismatches": [n for n in range(nmax + 1) if charged[n] != proposed[n]],
        "held_out_range_after_discovery": [81, nmax],
        "held_out_mismatches": [
            n for n in range(81, nmax + 1) if charged[n] != proposed[n]
        ],
        "zero_coefficients_charged": [n for n, value in enumerate(charged) if not value],
        "universal_subfamily": "n=x^2+y(y+1)+2z^2",
        "universal_subfamily_test_bound": args.subfamily_bound,
        "universal_subfamily_misses": universal_subfamily_misses(args.subfamily_bound),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
