#!/usr/bin/env python3
"""Exact replay of the open-box disproof for the colored five-cycle."""

import sympy as sp


x = sp.symbols("x0:5", nonzero=True)
B = sp.zeros(5)
for i in range(5):
    B[i, (i - 1) % 5] = x[(i - 1) % 5]
    B[i, i] = x[(i + 1) % 5]

b_expected = sp.Matrix(
    [
        -(x[0] ** 2 + x[1] ** 2 - x[2] ** 2 + x[3] ** 2 - x[4] ** 2)
        / (x[0] * x[1]),
        (x[0] ** 2 - x[1] ** 2 - x[2] ** 2 + x[3] ** 2 - x[4] ** 2)
        / (x[1] * x[2]),
        -(x[0] ** 2 - x[1] ** 2 + x[2] ** 2 + x[3] ** 2 - x[4] ** 2)
        / (x[2] * x[3]),
        (x[0] ** 2 - x[1] ** 2 + x[2] ** 2 - x[3] ** 2 - x[4] ** 2)
        / (x[3] * x[4]),
        -(x[0] ** 2 - x[1] ** 2 + x[2] ** 2 - x[3] ** 2 + x[4] ** 2)
        / (x[4] * x[0]),
    ]
)

assert sp.factor(B.det()) == 2 * sp.prod(x)
assert all(sp.factor(v) == 0 for v in B * b_expected + 2 * sp.Matrix(x))

K = 2 * sp.eye(5)
for i in range(5):
    K[i, (i + 1) % 5] = b_expected[i]
    K[(i + 1) % 5, i] = b_expected[i]
assert all(sp.factor(v) == 0 for v in K * sp.Matrix(x))

# D K D is exactly the weighted cycle Laplacian, with D=diag(x) and
# w_i=-b_i*x_i*x_{i+1}.  This certifies the quadratic-form identity.
D = sp.diag(*x)
w = [-sp.factor(b_expected[i] * x[i] * x[(i + 1) % 5]) for i in range(5)]
Lw = sp.zeros(5)
for i in range(5):
    Lw[i, i] += w[i]
    Lw[(i + 1) % 5, (i + 1) % 5] += w[i]
    Lw[i, (i + 1) % 5] -= w[i]
    Lw[(i + 1) % 5, i] -= w[i]
assert D * K * D == Lw

box_margin = 3 * sp.Rational(9, 10) ** 2 - 2 * sp.Rational(11, 10) ** 2
assert box_margin == sp.Rational(1, 100)
assert 2 * sp.Rational(11, 10) ** 2 - 3 * sp.Rational(9, 10) ** 2 == -box_margin

at_one = {xi: 1 for xi in x}
K_one = K.subs(at_one)
assert b_expected.subs(at_one) == sp.Matrix([-1] * 5)
assert sp.factor(K_one.charpoly().as_expr()) == sp.Symbol("lambda") * (
    sp.Symbol("lambda") ** 2 - 5 * sp.Symbol("lambda") + 5
) ** 2

print("det B(x) =", sp.factor(B.det()))
print(
    "B(x)b(x)+2x =",
    [sp.factor(v) for v in B * b_expected + 2 * sp.Matrix(x)],
)
print("D K(x) D equals weighted cycle Laplacian:", D * K * D == Lw)
print("open-box sign margin =", box_margin)
print("b(1) =", list(b_expected.subs(at_one)))
print("charpoly K(1) =", sp.factor(K_one.charpoly().as_expr()))
