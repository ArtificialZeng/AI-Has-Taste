"""Exact algebra checks supporting evidence/rederivation.md."""

from fractions import Fraction
from math import factorial

import sympy as sp


x, q = sp.symbols("x q", positive=True)
S, C = sp.sinh(x), sp.cosh(x)
A = x * C - S
B = A + q * S
phi = 3 * q * A / (x**2 * B)
phi_p = sp.diff(phi, x) / (2 * x)
phi_q = sp.diff(phi, q)

assert sp.simplify(phi_q - 3 * A**2 / (x**2 * B**2)) == 0
assert sp.simplify(
    phi_p - 3 * q * (x * q * (S * C - x) - 2 * A * B) / (2 * x**4 * B**2)
) == 0

mean_t = (1 - phi) / x**2
mean_l = phi / q
second_t = 2 * (1 - phi) / x**4 + 2 * phi_p / x**2
second_l = 2 * phi / q**2 - 2 * phi_q / q
mixed = phi_q / x**2 - phi_p / q

assert sp.simplify(mean_t - (x**2 * B - 3 * q * A) / (x**4 * B)) == 0
assert sp.simplify(mean_l - 3 * A / (x**2 * B)) == 0
assert sp.simplify(
    second_t
    - (2 * x**2 * B**2 - 12 * q * A * B + 3 * q**2 * x * (S * C - x))
    / (x**6 * B**2)
) == 0
assert sp.simplify(second_l - 6 * A * S / (x**2 * B**2)) == 0
assert sp.simplify(
    mixed - 3 * (2 * A * (A + B) + q * x * (x - S * C)) / (2 * x**4 * B**2)
) == 0

xi1 = 4 * x**2 * A**2
xi2 = (
    2 * x**2 * (x**2 + 3)
    - x * (x**2 + 12) * sp.sinh(2 * x)
    + 6 * (x**2 + 1) * sp.cosh(2 * x)
    - 6
)
assert sp.trigsimp(xi2 - (2 * x**3 * (x - S * C) + 12 * A**2)) == 0

covariance = mixed - mean_t * mean_l
assert sp.trigsimp(
    sp.factor(covariance - 3 * (xi1 + q * xi2) / (4 * x**6 * B**2))
) == 0

m = sp.symbols("m")
coefficient_polynomial = -m * (m - 1) * (m - 2) - 48 * m + 12 * m * (m - 1) + 48
assert sp.expand(coefficient_polynomial + (m - 1) * (m - 6) * (m - 8)) == 0
assert sp.series(xi2, x, 0, 10).removeO() == 0

partial = sum(Fraction(2**n, factorial(n)) for n in range(12))
rational_lower_bound = Fraction(7389, 1000)
assert partial == Fraction(164591, 22275)
assert partial - rational_lower_bound == Fraction(41, 891000)
f_at_bound = rational_lower_bound**2 - 4 * rational_lower_bound - 25
assert f_at_bound == Fraction(41321, 1_000_000)
assert f_at_bound > Fraction(1, 25)

print("all exact symbolic and rational checks passed")
