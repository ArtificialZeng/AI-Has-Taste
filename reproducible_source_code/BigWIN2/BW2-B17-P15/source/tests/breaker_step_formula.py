#!/usr/bin/env python3
"""Independent, exact small-case checks of the step autoconvolution formula."""
from fractions import Fraction as F
import random


def coefficient_values(a):
    n = len(a)
    out = []
    for k in range(2 * n - 1):
        out.append(sum((a[i] * a[k - i]
                        for i in range(n) if 0 <= k - i < n), F(0)))
    return out


def direct_integral(a, t):
    """Integrate by interval intersections, independently of convolution sums."""
    n = len(a)
    h = F(1, 2 * n)
    left = F(-1, 4)
    total = F(0)
    for i, ai in enumerate(a):
        Li, Ri = left + i * h, left + (i + 1) * h
        for j, aj in enumerate(a):
            Lj, Rj = left + j * h, left + (j + 1) * h
            overlap = max(F(0), min(Rj, t - Li) - max(Lj, t - Ri))
            total += ai * aj * overlap
    return total


def run():
    rng = random.Random(20260901)
    cases = [[F(2)], [F(1), F(3)], [F(0), F(2), F(1)]]
    for n in range(1, 9):
        for _ in range(20):
            cases.append([F(rng.randrange(5)) for _ in range(n)])
    checked = 0
    for a in cases:
        n = len(a)
        h = F(1, 2 * n)
        coeff = coefficient_values(a)
        # Pair-sum k peaks at t=-1/2+(k+1)h, not at -1/2+kh.
        for k, ck in enumerate(coeff):
            t = F(-1, 2) + (k + 1) * h
            assert direct_integral(a, t) == h * ck
            checked += 1
        # On each grid segment the integral is affine.
        for m in range(0, 2 * n):
            lo = F(-1, 2) + m * h
            hi = lo + h
            assert 2 * direct_integral(a, (lo + hi) / 2) == (
                direct_integral(a, lo) + direct_integral(a, hi))
            checked += 1
    print(f"PASS exact direct-integration identities: {checked} checks, {len(cases)} cases")


if __name__ == "__main__":
    run()
