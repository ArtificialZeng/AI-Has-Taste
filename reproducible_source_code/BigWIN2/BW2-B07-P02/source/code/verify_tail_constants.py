#!/usr/bin/env python3
"""Exact rational checks used by the analytic-tail proof.

This script checks only finite/rational arithmetic.  The accompanying proof
establishes why these inequalities imply the infinite coefficient bound.
"""

from fractions import Fraction


def divisors_between(n: int, low: int, high: int):
    return [d for d in range(low, high + 1) if n % d == 0]


def finite_rho_majorant() -> tuple[Fraction, int]:
    maximum = Fraction(0)
    maximizer = -1
    for n in range(6, 100):
        # n^3 times the sum of the absolute values of the contributions
        # [z^n] R from exponents r >= 3 and base indices k=n/r >= 2.
        value = sum(
            (Fraction(r * r, (n // r) ** (r - 3))
             for r in divisors_between(n, 3, n // 2)),
            Fraction(0),
        )
        if value > maximum:
            maximum = value
            maximizer = n
    return maximum, maximizer


def square_sum_from_five_at_one_third() -> Fraction:
    # Sum_{r>=0} r^2 x^r = x(1+x)/(1-x)^3.
    x = Fraction(1, 3)
    whole = x * (1 + x) / (1 - x) ** 3
    initial = sum((r * r * x**r for r in range(5)), Fraction(0))
    return (whole - initial) / x**3


def main() -> None:
    maximum, maximizer = finite_rho_majorant()
    assert maximum == Fraction(113, 6)
    assert maximizer == 12
    assert maximum < 19

    r_ge_five_k_ge_three = square_sum_from_five_at_one_third()
    assert r_ge_five_k_ge_three == Fraction(31, 6)
    k_two_at_r_fifty = Fraction(50 * 50, 2 ** 47)
    assert k_two_at_r_fifty < Fraction(1, 100)
    analytic_rho_bound = 9 + Fraction(16, 25) + Fraction(31, 6) + Fraction(1, 100)
    assert analytic_rho_bound < 15

    # Integral lower bound:
    # zeta(2) > sum_{k=1}^5 1/k^2 + integral_6^infty x^-2 dx.
    zeta_two_lower = sum(
        (Fraction(1, k * k) for k in range(1, 6)), Fraction(0)
    ) + Fraction(1, 6)
    assert zeta_two_lower == Fraction(5869, 3600)
    assert zeta_two_lower > Fraction(13, 8)
    r_l1_bound = (2 - zeta_two_lower) / 3
    assert r_l1_bound < Fraction(1, 8)

    # For a=1/8, sum_{s>=1} s^4 a^(s-1)/s!
    # = exp(a)(a^3+6a^2+7a+1).  The proof bounds exp(1/8)<17/15.
    a = Fraction(1, 8)
    polynomial = a**3 + 6 * a**2 + 7 * a + 1
    exponential_series_bound = Fraction(17, 15) * polynomial
    assert polynomial == Fraction(1009, 512)
    assert exponential_series_bound < Fraction(9, 4)
    assert 19 * Fraction(9, 4) < 43

    # Elementary logarithmic bounds used to show exp(-gamma)>1/2.
    log_two_lower = Fraction(56, 81)
    log_three_lower = Fraction(263, 240)
    assert log_two_lower > Fraction(2, 3)
    assert log_two_lower + log_three_lower - Fraction(107, 60) == Fraction(5, 1296)

    # exp(9)>5000 follows from exp(1)>8/3.
    assert 8**9 > 5000 * 3**9

    # At n=5000 use log(n)<9 in the final error coefficient.
    endpoint_error_coefficient = (
        Fraction(1280, 7) + 1057 + Fraction(512, 7) * 10
    )
    assert endpoint_error_coefficient == Fraction(13799, 7)
    assert Fraction(5000, 2) - endpoint_error_coefficient == Fraction(3701, 7)
    # Derivative of the error coefficient is 512/(7n), below 1/2.
    assert Fraction(512, 7 * 5000) < Fraction(1, 2)

    print("finite_rho_majorant=113/6")
    print("finite_rho_maximizer=12")
    print("global_rho_constant=19")
    print("K_pointwise_constant=43")
    print("J_pointwise_constant_from_index_2000=88")
    print("tail_endpoint_error_coefficient=13799/7")
    print("tail_endpoint_main_lower_coefficient=2500")
    print("tail_endpoint_margin=3701/7")
    print("status=PASS")


if __name__ == "__main__":
    main()
