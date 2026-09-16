"""Exact symbolic certificate for the generic affine-linear eliminant."""

import itertools

import sympy as sp


a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
b1, b2, c1, c2, p1, p2, q = sp.symbols("b1 b2 c1 c2 p1 p2 q")
x1, x2, u0, u1 = sp.symbols("x1 x2 u0 u1")
Y0, Y1, Y2 = sp.symbols("Y0 Y1 Y2")

A = sp.Matrix([[a11, a12], [a21, a22]])
b = sp.Matrix([b1, b2])
c = sp.Matrix([c1, c2])
p = sp.Matrix([[p1, p2]])
x = sp.Matrix([x1, x2])
tau = A.trace()
delta = A.det()
O = sp.Matrix.vstack(p, p * A)
Omega = sp.expand(O.det())
assert sp.expand(
    Omega - (p1**2 * a12 + p1 * p2 * (a22 - a11) - p2**2 * a21)
) == 0
assert Omega != 0

y = (p * x)[0] + q
yp = (p * (A * x + b * u0 + c))[0]
ypp = (p * (A * (A * x + b * u0 + c) + b * u1))[0]
alpha = sp.expand((p * (tau * sp.eye(2) - A) * b)[0])
beta = sp.expand((p * b)[0])
gamma = sp.expand((p * (tau * sp.eye(2) - A) * c)[0])
E_evaluated = sp.expand(
    ypp - tau * yp + delta * y + alpha * u0 - beta * u1 + gamma - delta * q
)
assert E_evaluated == 0

# Clearing the only denominator verifies the inverse coordinate map in (3).
z = sp.Matrix([Y0 - q, Y1 - beta * u0 - (p * c)[0]])
x_inverse_numerator = O.adjugate() * z
for entry in O * x_inverse_numerator - Omega * z:
    assert sp.expand(entry) == 0

# The graph equation obtained after using Y0,Y1 as coordinates.
graph_E = sp.expand(
    Y2 - tau * Y1 + delta * Y0 + alpha * u0 - beta * u1 + gamma - delta * q
)
graph_value = sp.expand(graph_E.subs({Y0: y, Y1: yp, Y2: ypp}))
assert graph_value == 0
assert sp.Poly(graph_E, Y2).degree() == 1
assert sp.Poly(graph_E, Y2).LC() == 1

# One exact point witnesses simultaneous generic nonvanishing.
witness = {
    a11: 1,
    a12: 1,
    a21: 1,
    a22: 2,
    p1: 1,
    p2: 0,
    b1: 1,
    b2: 1,
    c1: 1,
    c2: 0,
    q: 0,
}
open_factors = [Omega, tau, delta, beta, alpha, gamma - delta * q]
assert [sp.expand(f).subs(witness) for f in open_factors] == [1, 3, 1, 1, 1, 2]

# Enumerate all nonnegative integral points of the specialized support bound.
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
    (0, 0, 0, 0, 0, 0),  # 1
    (0, 0, 0, 0, 0, 1),  # y''
    (0, 0, 0, 0, 1, 0),  # y'
    (0, 0, 0, 1, 0, 0),  # y
    (0, 0, 1, 0, 0, 0),  # u''
    (0, 1, 0, 0, 0, 0),  # u'
    (1, 0, 0, 0, 0, 0),  # u
]

print("universal eliminant identity: 0")
print("observability determinant:", Omega)
print("open-set witness factors: 1, 3, 1, 1, 1, 2")
print("Theorem 3.7 candidate count: 7")
print("actual generic support: 1,u,u',y,y',y''")
