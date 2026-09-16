#!/usr/bin/env python3
"""Exact finite check for the two level-2, e=6 core series.

This enumerates bipartitions and applies Gerber--Norton's nested beta-set
criterion (Lemma 2.11).  It is finite integer enumeration, not an all-orders
positivity proof.
"""

from __future__ import annotations

import argparse
import math


def partitions(n: int, largest: int | None = None):
    """Yield all partitions of n as nonincreasing tuples."""
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    for first in range(largest, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def symbol_subset(lam: tuple[int, ...], s: int,
                  mu: tuple[int, ...], t: int) -> bool:
    """Test S(lam,s) subset S(mu,t) using finite beta sets.

    S(lam,s)={lam_k-k+1+s:k>=1}, with lam_k=0 beyond its length.
    S(mu,t) contains every integer <= t-len(mu), so only beads above that
    threshold need to be compared.
    """
    threshold = t - len(mu)
    mu_finite = {
        part - k + 1 + t for k, part in enumerate(mu, start=1)
    }
    last_k = max(len(lam), s - threshold)
    for k in range(1, last_k + 1):
        part = lam[k - 1] if k <= len(lam) else 0
        beta = part - k + 1 + s
        if beta > threshold and beta not in mu_finite:
            return False
    return True


def is_six_core_bipartition(lam1: tuple[int, ...],
                            lam2: tuple[int, ...], a: int) -> bool:
    """Nested criterion for charge (0,a), where a is 1 or 3."""
    return (
        symbol_subset(lam1, 0, lam2, a)
        and symbol_subset(lam2, a, lam1, 6)
    )


def charged_core_coefficients(limit: int, a: int) -> list[int]:
    by_size = [list(partitions(n)) for n in range(limit + 1)]
    result = []
    for n in range(limit + 1):
        count = 0
        for k in range(n + 1):
            for lam1 in by_size[k]:
                for lam2 in by_size[n - k]:
                    count += is_six_core_bipartition(lam1, lam2, a)
        result.append(count)
    return result


def multiply(a: list[int], b: list[int], limit: int) -> list[int]:
    out = [0] * (limit + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:limit - i + 1]):
                if bj:
                    out[i + j] += ai * bj
    return out


def core_partition_series(e: int, limit: int) -> list[int]:
    """Truncate prod_m (1-q^(e*m))^e/(1-q^m) exactly."""
    series = [1] + [0] * limit
    for m in range(1, limit + 1):
        inverse = [0] * (limit + 1)
        for degree in range(0, limit + 1, m):
            inverse[degree] = 1
        series = multiply(series, inverse, limit)
        if e * m <= limit:
            factor = [0] * (limit + 1)
            for j in range(e + 1):
                degree = e * m * j
                if degree <= limit:
                    factor[degree] = (-1) ** j * math.comb(e, j)
            series = multiply(series, factor, limit)
    return series


def phi_series(limit: int) -> list[int]:
    phi = [0] * (limit + 1)
    phi[0] = 1
    k = 1
    while k * k <= limit:
        phi[k * k] = 2
        k += 1
    return phi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be nonnegative")

    c01 = charged_core_coefficients(args.limit, 1)
    c03 = charged_core_coefficients(args.limit, 3)

    c3 = core_partition_series(3, args.limit)
    lhs = multiply(phi_series(args.limit), multiply(c3, c3, args.limit),
                   args.limit)
    rhs = [c03[n] + (2 * c01[n - 1] if n else 0)
           for n in range(args.limit + 1)]
    if lhs != rhs:
        bad = next(n for n in range(args.limit + 1) if lhs[n] != rhs[n])
        raise AssertionError(
            f"equation (5.3) fails at n={bad}: lhs={lhs[bad]}, rhs={rhs[bad]}"
        )

    print(f"exact range: 0 <= n <= {args.limit}")
    print("c_6,(0,1):", " ".join(map(str, c01)))
    print("c_6,(0,3):", " ".join(map(str, c03)))
    print("zero coefficients c_6,(0,1):", [n for n, x in enumerate(c01) if x == 0])
    print("zero coefficients c_6,(0,3):", [n for n, x in enumerate(c03) if x == 0])
    print("equation (5.3): verified coefficientwise on this range")


if __name__ == "__main__":
    main()
