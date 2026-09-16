"""Exact triage checks for win-00060-p04; requires SymPy."""

import itertools
import sympy as sp


a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
b1, b2, c1, c2, p1, p2 = sp.symbols("b1 b2 c1 c2 p1 p2")
x1, x2, u, up, q = sp.symbols("x1 x2 u up q")
A = sp.Matrix([[a11, a12], [a21, a22]])
b = sp.Matrix([b1, b2])
c = sp.Matrix([c1, c2])
p = sp.Matrix([[p1, p2]])
x = sp.Matrix([x1, x2])
tau, delta = A.trace(), A.det()

y = (p * x)[0] + q
yp = (p * (A * x + b * u + c))[0]
ypp = (p * (A * (A * x + b * u + c) + b * up))[0]
relation = sp.expand(
    ypp
    - tau * yp
    + delta * y
    + (p * (tau * sp.eye(2) - A) * b)[0] * u
    - (p * b)[0] * up
    + (p * (tau * sp.eye(2) - A) * c)[0]
    - delta * q
)
assert relation == 0

candidate_points = []
for point in itertools.product(range(2), repeat=6):
    l0, l1, l2, e0, e1, e2 = point
    if (
        l0 + l1 + l2 + e0 + e1 + e2 <= 1
        and e0 + e1 + e2 <= 1
        and l0 + l1 + l2 + e1 + 2 * e2 <= 3
        and l1 + e1 + 2 * e2 <= 3
        and l2 + e2 <= 1
    ):
        candidate_points.append(point)
assert candidate_points == [
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 1, 0),
    (0, 0, 0, 1, 0, 0),
    (0, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0),
]

observability_minor = sp.expand(sp.Matrix.vstack(p, p * A).det())
assert observability_minor != 0
print("identity remainder: 0")
print("candidate count: 7")
print("observability minor:", observability_minor)
