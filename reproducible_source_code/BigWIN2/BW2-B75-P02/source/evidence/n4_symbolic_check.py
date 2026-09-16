#!/usr/bin/env python3
"""Exact n=4 expansion of the specialized deformation-map equation.

Matrix columns are the coordinates of r(u_j).  The script evaluates (7.1)--
(7.3) on (u_1,u_2,u_3,u_4), using exactly the structure maps in Example 8.7.
"""

import sympy as sp


r = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"r{i + 1}{j + 1}"))
a = r[:3, :3]

# G_r = [r(u_1),...,r(u_4)]_g; the bracket is the coordinate volume
# times x_4.
g = sp.Matrix([0, 0, 0, r.det()])

# In H_r, rho_g(...)(u_i) vanishes for i<4.  For i=4 its sign is +1,
# and its coefficient is the x_1 wedge x_2 wedge x_3 minor of the first
# three columns.
h_scalar = a.det()
h = sp.Matrix([0, 0, 0, h_scalar])

residual = sp.Matrix([sp.expand(z) for z in (g - r * h)])
expected = sp.Matrix(
    [
        -h_scalar * r[0, 3],
        -h_scalar * r[1, 3],
        -h_scalar * r[2, 3],
        r.det() - r[3, 3] * h_scalar,
    ]
)

assert all(sp.expand(x - y) == 0 for x, y in zip(residual, expected))
print("PASS: exact polynomial identity over Z[r_ij]")
print("H_r(u1,u2,u3,u4) = det(A) u4")
print("coordinates(G_r-r(H_r)) =")
for item in expected:
    print(sp.factor(item))
