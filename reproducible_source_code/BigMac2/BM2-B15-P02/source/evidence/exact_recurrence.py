#!/usr/bin/env python3
"""Exact first-failure computation for q_N=N/(2N+1).

For k_m = kappa_{2m}=A_m/D^m, D=2N+1, the moment--cumulant
recursion gives

  A_1=N,
  A_m=N(D^(m-1)-sum_{j<m} binom(2m-1,2j-1) A_j D^(m-1-j)).

Thus every reported sign is an integer sign; floating point is used only for
the displayed value of arcosh(1+1/N)*m_*.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def cumulant_numerators(N: int, stop: int) -> list[int]:
    if N < 1 or stop < 1:
        raise ValueError("N and stop must be positive")
    D = 2 * N + 1
    powers = [1]
    for _ in range(stop):
        powers.append(powers[-1] * D)
    A = [0, N]
    for m in range(2, stop + 1):
        inner = powers[m - 1]
        for j in range(1, m):
            inner -= math.comb(2 * m - 1, 2 * j - 1) * A[j] * powers[m - 1 - j]
        A.append(N * inner)
    return A


def first_failure(N: int, stop: int | None = None) -> tuple[int, int]:
    # The conjectured scale is O(sqrt(N)); this default is deliberately much
    # wider and raises rather than silently treating non-discovery as a result.
    if stop is None:
        stop = max(32, 8 * math.isqrt(N) + 32)
    D = 2 * N + 1
    powers = [1]
    for _ in range(stop):
        powers.append(powers[-1] * D)
    A = [0, N]
    for m in range(2, stop + 1):
        inner = powers[m - 1]
        for j in range(1, m):
            inner -= math.comb(2 * m - 1, 2 * j - 1) * A[j] * powers[m - 1 - j]
        A.append(N * inner)
        if ((-1) ** (m + 1)) * A[m] < 0:
            return m, A[m]
    raise RuntimeError(f"no strict failure through m={stop} for N={N}")


def fraction_crosscheck(N: int, stop: int) -> None:
    """Independent Fraction implementation of the unscaled recurrence."""
    q = Fraction(N, 2 * N + 1)
    k = [Fraction(0), q]
    A = cumulant_numerators(N, stop)
    D = 2 * N + 1
    for m in range(2, stop + 1):
        value = q * (1 - sum(
            math.comb(2 * m - 1, 2 * j - 1) * k[j]
            for j in range(1, m)
        ))
        k.append(value)
    for m in range(1, stop + 1):
        assert k[m] == Fraction(A[m], D**m), (N, m)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("N", nargs="*", type=int)
    parser.add_argument("--crosscheck-through", type=int, default=20)
    args = parser.parse_args()
    Ns = args.N or [1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000]
    print("N\tq\tm_star\tsign_certificate\ta*m_star\tgap_from_pi2_over_4")
    target = math.pi**2 / 4
    for N in Ns:
        m, certificate = first_failure(N)
        fraction_crosscheck(N, min(args.crosscheck_through, m))
        scaled = math.acosh(1 + 1 / N) * m
        print(
            f"{N}\t{N}/{2*N+1}\t{m}\t"
            f"{'negative' if ((-1)**(m+1))*certificate < 0 else 'ERROR'}\t"
            f"{scaled:.15g}\t{scaled-target:+.15g}"
        )


if __name__ == "__main__":
    main()
