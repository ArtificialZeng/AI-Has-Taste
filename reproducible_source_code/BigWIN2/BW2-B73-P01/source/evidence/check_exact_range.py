#!/usr/bin/env python3
"""Exact finite audit of the all-N constant using half-integer kernels.

This does not prove the infinite claim.  It independently expands the finite
exponential polynomial for each requested N and integrates every monomial over
(0, infinity) with rational arithmetic.
"""

from fractions import Fraction
from math import factorial


def add(a, b):
    out = dict(a)
    for degree, coefficient in b.items():
        out[degree] = out.get(degree, Fraction()) + coefficient
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def scale_shift(a, scale=Fraction(1), shift=0):
    return {degree + shift: scale * coefficient for degree, coefficient in a.items()}


def derivative(a):
    return {
        degree - 1: degree * coefficient
        for degree, coefficient in a.items()
        if degree != 0
    }


def kernel_polynomial(N):
    """Return P_N with F_N(z)=exp(-z) P_N(z)/pi."""
    if N == 1:
        return {-1: Fraction(1, 4)}
    n = N - 2
    prefactor = Fraction(1, 2 ** (N + 1) * factorial(N - 1))
    return {
        n - k: prefactor
        * Fraction(factorial(n + k), factorial(k) * factorial(n - k) * 2**k)
        for k in range(n + 1)
    }


def normalized_constant(N):
    """Compute I_N/(kappa*m), with the common pi factor cancelled."""
    P = kernel_polynomial(N)
    # G_N=exp(-z) H_N/pi, H_N=(3P+zP'-zP)/2.
    H = scale_shift(P, Fraction(3, 2))
    H = add(H, scale_shift(derivative(P), Fraction(1, 2), 1))
    H = add(H, scale_shift(P, Fraction(-1, 2), 1))

    # pi^2 Q_N = integral z^5 exp(-2z) H_N(z)^2 dz.
    pi_squared_Q = Fraction()
    for i, ai in H.items():
        for j, aj in H.items():
            power = 5 + i + j
            assert power >= 0
            pi_squared_Q += ai * aj * Fraction(factorial(power), 2 ** (power + 1))
    return Fraction(32, 9) * pi_squared_Q


def claimed_constant(N):
    # Gamma(N+3/2)=((2N+2)! sqrt(pi))/(4^(N+1)(N+1)!).
    half_gamma_without_sqrt_pi = Fraction(
        factorial(2 * N + 2), 4 ** (N + 1) * factorial(N + 1)
    )
    return Fraction(2, 3 * (N + 1) * (N + 2) * (2 * N + 1)) * (
        half_gamma_without_sqrt_pi / factorial(N - 1)
    ) ** 2


if __name__ == "__main__":
    for N in range(1, 31):
        computed = normalized_constant(N)
        claimed = claimed_constant(N)
        assert computed == claimed, (N, computed, claimed)
        print(f"N={N:2d}: {computed}  OK")
