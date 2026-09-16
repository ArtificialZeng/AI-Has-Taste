#!/usr/bin/env python3
"""Reproducible checks for the quantitative (3.38) endpoint audit.

The Markdown proof establishes the infinite statements.  This script checks
the exact coefficients symbolically and stress-tests the stated (very
conservative) remainder on a finite high-precision grid.
"""

import mpmath as mp
import sympy as sp


h, A, b = sp.symbols("h A b", positive=True)
zeta3 = sp.zeta(3)
d = -h / (A + h)
u = 2 * h

t2 = -sp.zeta(2) * d * u
t3 = sp.zeta(3) * (d**2 * u + d * u**2)
c2 = sp.pi**2 / (3 * A)
c3 = -sp.pi**2 / (3 * A**2) + zeta3 * (2 / A**2 - 4 / A)

assert sp.simplify(sp.limit((t2 + t3 - c2 * h**2) / h**3, h, 0) - c3) == 0

q0 = sp.simplify(A * b * c2)
q1 = sp.simplify(A * b * c3 + (b + 1) * c2)
q1_expected = sp.pi**2 / (3 * A) - 2 * b * zeta3 * (2 - 1 / A)
assert sp.simplify(q0 - sp.pi**2 * b / 3) == 0
assert sp.simplify(q1 - q1_expected) == 0


mp.mp.dps = 90


def quantities(a, beta):
    z3 = mp.zeta(3)
    c_2 = mp.pi**2 / (3 * a)
    c_3 = -mp.pi**2 / (3 * a**2) + z3 * (2 / a**2 - 4 / a)
    k_phi = mp.pi**2 / (3 * a**3) + z3 / 2 + mp.mpf(897) / 28
    p_bound = c_2 + abs(c_3) / 4 + k_phi / 16
    e_bound = mp.exp(p_bound / 16) * p_bound**2 / 2
    k_n = k_phi + e_bound
    deriv = mp.pi**2 / (3 * a) - 2 * beta * z3 * (2 - 1 / a)
    k_l = a * beta * k_n + (beta + 1) * abs(c_3) + (beta + 1) * k_n / 4
    return c_2, c_3, deriv, k_l


def exact_l_loggamma(a, beta, step):
    x = a / (a + step)
    phi = mp.loggamma(x) + mp.loggamma(1 + 2 * step) - mp.loggamma(x + 2 * step)
    return (a * beta + (beta + 1) * step) / step**2 * (-mp.expm1(-phi))


def exact_l_beta(a, beta, step):
    x = a / (a + step)
    prefactor = (a * beta + (beta + 1) * step) / step**2
    return prefactor * (1 - 1 / (2 * step * mp.beta(x, 2 * step)))


checks = 0
worst_ratio = mp.mpf("0")
for a in map(mp.mpf, [2, "2.1", 3, 5, 10, 50]):
    c_a = mp.beta(a - 1, 1 + a / 2)
    b_star = 3 * c_a / mp.pi**2
    betas = [mp.mpf("0"), b_star / 2, b_star, min(mp.mpf("0.9"), 2 * b_star)]
    for beta in betas:
        if beta >= 1:
            continue
        _, _, deriv, k_l = quantities(a, beta)
        cap = mp.mpf("0.25") if beta == 0 else min(mp.mpf("0.25"), a * (1 - beta) / (2 * beta))
        for fraction in map(mp.mpf, ["1e-7", "1e-5", "1e-3", "0.05", "0.5", "0.99"]):
            step = cap * fraction
            l_gamma = exact_l_loggamma(a, beta, step)
            l_beta = exact_l_beta(a, beta, step)
            # The two exact representations should agree well beyond 60 digits.
            assert mp.almosteq(l_gamma, l_beta, rel_eps=mp.mpf("1e-60"), abs_eps=mp.mpf("1e-60"))
            linear = mp.pi**2 * beta / 3 + deriv * step
            error = abs(l_gamma - linear)
            bound = k_l * step**2
            assert error <= bound
            worst_ratio = max(worst_ratio, error / bound)
            checks += 1

print("symbolic c2 =", c2)
print("symbolic c3 =", sp.factor(c3))
print("symbolic L constant =", q0)
print("symbolic L linear coefficient =", sp.factor(q1))
print("finite high-precision checks =", checks)
print("largest observed error/bound ratio =", mp.nstr(worst_ratio, 15))
