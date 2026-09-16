#!/usr/bin/env python3
"""Exact symbolic/rational checks for evidence/exact_solution.md.

Only the final decimal diagnostics use numerical arithmetic.  All assertions
that certify the primal and dual solutions use SymPy exact expressions or
fractions.Fraction interval arithmetic.
"""

from fractions import Fraction as F

import sympy as sp


u, x = sp.symbols("u x")
P = (
    256 * u**7
    + 256 * u**6
    - 96 * u**5
    - 80 * u**4
    + 40 * u**3
    + 30 * u**2
    - 15 * u
    - 5
)
lo, hi = F(533, 1000), F(267, 500)


def at_fraction(poly, value):
    return F(int(sp.numer(poly.subs(u, sp.Rational(value.numerator, value.denominator)))),
             int(sp.denom(poly.subs(u, sp.Rational(value.numerator, value.denominator)))))


# The defining algebraic number is unambiguous.
p_lo, p_hi = at_fraction(P, lo), at_fraction(P, hi)
assert p_lo < 0 < p_hi
# A termwise exact lower bound for P' throughout [lo,hi].
derivative_lower = (
    1792 * lo**6
    + 1536 * lo**5
    - 480 * hi**4
    - 320 * hi**3
    + 120 * lo**2
    + 60 * lo
    - 15
)
assert derivative_lower > 0


# Exact primal square and its Chebyshev expansion.
b = 2 * u**2 - sp.Rational(5, 4)
q = x**3 + u * x**2 + b * x - 2 * u**3
cheb_symbols = sp.symbols("C0:7")
cheb_identity = sum(cheb_symbols[k] * sp.chebyshevt(k, x) for k in range(7))
cheb = sp.solve(
    sp.Poly(sp.expand(cheb_identity - q**2), x).all_coeffs(),
    cheb_symbols,
    dict=True,
)[0]
A0 = (128 * u**6 - 20 * u**2 + 5) / 32
assert sp.factor(cheb[cheb_symbols[0]] - A0) == 0
assert sp.factor(cheb[cheb_symbols[2]]) == 0
assert sp.factor(cheb[cheb_symbols[3]]) == 0


# The three roots of q lie in disjoint subintervals of (-1,1).  The returned
# bounds enclose q(u0,x0) for every u0 in [lo,hi], with x0 fixed.
def q_interval(x0):
    constant = x0**3 - F(5, 4) * x0
    ux2 = (lo * x0**2, hi * x0**2)
    if x0 >= 0:
        two_u2_x = (2 * lo**2 * x0, 2 * hi**2 * x0)
    else:
        two_u2_x = (2 * hi**2 * x0, 2 * lo**2 * x0)
    minus_two_u3 = (-2 * hi**3, -2 * lo**3)
    return (
        constant + ux2[0] + two_u2_x[0] + minus_two_u3[0],
        constant + ux2[1] + two_u2_x[1] + minus_two_u3[1],
    )


root_test_points = [F(-23, 25), F(-91, 100), F(-21, 50), F(-41, 100), F(79, 100), F(4, 5)]
root_intervals = [q_interval(t) for t in root_test_points]
assert root_intervals[0][1] < 0 < root_intervals[1][0]
assert root_intervals[2][0] > 0 > root_intervals[3][1]
assert root_intervals[4][1] < 0 < root_intervals[5][0]


# Exact dual moment functional.  Recurrence is reduction modulo q.
D = 5 * (2 * u - 1) * (32 * u**4 + 8 * u**2 + 1)
m0 = -(512 * u**4 - 256 * u**3 - 32 * u**2 + 6 * u - 3) / D
m1 = sp.Integer(-1)
m2 = -(
    256 * u**6
    - 128 * u**5
    + 48 * u**4
    - 44 * u**3
    + 42 * u**2
    - 23 * u
    - 1
) / D
moments = [m0, m1, m2]
for n in range(4):
    moments.append(sp.factor(-u * moments[n + 2] - b * moments[n + 1] + 2 * u**3 * moments[n]))


def L(poly):
    power_poly = sp.Poly(sp.expand(poly), x)
    return sp.factor(sum(coefficient * moments[degree]
                         for (degree,), coefficient in power_poly.terms()))


assert L(sp.chebyshevt(1, x)) == -1
assert sp.factor(L(sp.chebyshevt(4, x)) + 1) == 0
assert sp.factor(L(sp.chebyshevt(6, x)) + 1) == 0
t5_residual = sp.factor(L(sp.chebyshevt(5, x)) + 1)
t5_numerator = sp.together(t5_residual).as_numer_denom()[0]
assert sp.rem(t5_numerator, P, domain=sp.QQ) == 0


# Complementarity: the primal value is exactly 1+m0 when P(u)=0.
M = 2 * (2 * u + 1) ** 2 * (4 * u**2 - 6 * u + 1) ** 2 / (128 * u**6 - 20 * u**2 + 5)
complementarity_numerator = sp.together(M - 1 - m0).as_numer_denom()[0]
assert sp.rem(complementarity_numerator, P, domain=sp.QQ) == 0


# Sylvester positivity for the degree-two moment matrix.  These identities do
# not use P(u)=0; signs are certified on the entire isolating interval.
H = sp.Matrix(
    [
        [moments[0], moments[1], moments[2]],
        [moments[1], moments[2], moments[3]],
        [moments[2], moments[3], moments[4]],
    ]
)
principal_minors = [sp.factor(H[:k, :k].det()) for k in range(1, 4)]


def interval_add(a, c):
    return a[0] + c[0], a[1] + c[1]


def interval_mul(a, c):
    products = (a[0] * c[0], a[0] * c[1], a[1] * c[0], a[1] * c[1])
    return min(products), max(products)


def polynomial_interval(coefficients):
    value = (F(coefficients[0]), F(coefficients[0]))
    for coefficient in coefficients[1:]:
        value = interval_add(interval_mul(value, (lo, hi)), (F(coefficient), F(coefficient)))
    return value


sign_factors = {
    "delta1_numerator": [-512, 256, 32, -6, 3],
    "delta2_factor_1": [4, -6, 1],
    "delta2_factor_2": [64, -32, -24, 32, -11],
    "delta2_factor_3": [112, 112, 46, 3, 2],
    "delta3_last_factor": [512, 1024, 864, 328, 32, -11],
}
factor_intervals = {name: polynomial_interval(coeffs) for name, coeffs in sign_factors.items()}
assert factor_intervals["delta1_numerator"][0] > 0
assert factor_intervals["delta2_factor_1"][1] < 0
assert factor_intervals["delta2_factor_2"][1] < 0
assert factor_intervals["delta2_factor_3"][0] > 0
assert factor_intervals["delta3_last_factor"][0] > 0

delta1_expected = (-512 * u**4 + 256 * u**3 + 32 * u**2 - 6 * u + 3) / D
delta2_expected = (
    (4 * u**2 - 6 * u + 1)
    * (64 * u**4 - 32 * u**3 - 24 * u**2 + 32 * u - 11)
    * (112 * u**4 + 112 * u**3 + 46 * u**2 + 3 * u + 2)
    / (25 * (2 * u - 1) ** 2 * (32 * u**4 + 8 * u**2 + 1) ** 2)
)
delta3_expected = (
    (2 * u + 1)
    * (4 * u**2 - 6 * u + 1) ** 2
    * (64 * u**4 - 32 * u**3 - 24 * u**2 + 32 * u - 11) ** 2
    * (512 * u**5 + 1024 * u**4 + 864 * u**3 + 328 * u**2 + 32 * u - 11)
    / (2000 * (2 * u - 1) ** 3 * (32 * u**4 + 8 * u**2 + 1) ** 3)
)
for actual, expected in zip(principal_minors, [delta1_expected, delta2_expected, delta3_expected]):
    assert sp.factor(actual - expected) == 0


# An optional polynomial characterization of T=M/2.
y = sp.symbols("y")
t_polynomial = (
    28900000 * y**7
    - 131750000 * y**6
    + 120730000 * y**5
    + 214615000 * y**4
    - 355902050 * y**3
    - 31494803 * y**2
    + 238257375 * y
    - 82156250
)
resultant = sp.resultant(P, sp.together(y - M / 2).as_numer_denom()[0], u)
assert sp.rem(resultant, t_polynomial, y, domain=sp.QQ) == 0


u_numeric = next(root for root in sp.nroots(P, n=40, maxsteps=200)
                 if abs(sp.im(root)) < sp.Float("1e-35") and lo < root < hi)
q_roots_numeric = sp.nroots(q.subs(u, u_numeric), n=25, maxsteps=200)
print("P(lo), P(hi):", p_lo, p_hi)
print("exact lower bound for P' on [lo,hi]:", derivative_lower)
print("root-sign interval enclosures:")
for point, enclosure in zip(root_test_points, root_intervals):
    print(" ", point, enclosure)
print("minor-factor interval enclosures:")
for name, enclosure in factor_intervals.items():
    print(" ", name, enclosure)
print("u =", u_numeric)
print("roots(q) =", q_roots_numeric)
print("T =", sp.N((M / 2).subs(u, u_numeric), 30))
print("all exact assertions passed")
