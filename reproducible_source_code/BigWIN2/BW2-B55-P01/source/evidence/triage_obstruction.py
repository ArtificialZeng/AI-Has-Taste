#!/usr/bin/env python3
"""Exact replay of the m=5 transverse PSD-kernel certificate."""

import sympy as sp


x = sp.symbols("x0:5")
B = sp.Matrix(
    [
        [x[1], 0, 0, 0, x[4]],
        [x[0], x[2], 0, 0, 0],
        [0, x[1], x[3], 0, 0],
        [0, 0, x[2], x[4], 0],
        [0, 0, 0, x[3], x[0]],
    ]
)
at_one = {xi: 1 for xi in x}

K = sp.zeros(5)
for i in range(5):
    K[i, i] = 2
    K[i, (i + 1) % 5] = -1
    K[(i + 1) % 5, i] = -1

print("det B(x) =", sp.factor(B.det()))
print("det B(1) =", B.subs(at_one).det())
print("b(1) for a=2 =", list(B.subs(at_one).LUsolve(sp.Matrix([-2] * 5))))
print("K*1 =", list(K * sp.ones(5, 1)))
print("leading principal minors =", [K[:k, :k].det() for k in range(1, 6)])
print("characteristic polynomial =", sp.factor(K.charpoly().as_expr()))
