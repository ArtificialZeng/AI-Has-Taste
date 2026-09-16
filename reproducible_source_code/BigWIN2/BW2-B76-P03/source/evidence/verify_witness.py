#!/usr/bin/env python3
"""Exact symbolic verification of the four-dimensional witness."""

from itertools import product

import sympy as sp


# Ordered coordinates: e1, e2, r, z.
e1, e2, r, z = [sp.eye(4).col(i) for i in range(4)]

# Structure constants for i < j; omitted brackets are zero.
upper = {
    (0, 1): e1 + z,
    (0, 2): -r,
    (2, 3): -r,  # [r,z]=-r, equivalently [z,r]=r
}


def bracket_basis(i, j):
    if i == j:
        return sp.zeros(4, 1)
    if i < j:
        return upper.get((i, j), sp.zeros(4, 1))
    return -bracket_basis(j, i)


def bracket(u, v):
    return sp.simplify(
        sum(
            (u[i] * v[j] * bracket_basis(i, j)
             for i, j in product(range(4), repeat=2)),
            sp.zeros(4, 1),
        )
    )


# Check Jacobi on every ordered basis triple (not only distinct triples).
jacobi_sums = {}
for i, j, k in product(range(4), repeat=3):
    J = sp.simplify(
        bracket(sp.eye(4).col(i), bracket_basis(j, k))
        + bracket(sp.eye(4).col(j), bracket_basis(k, i))
        + bracket(sp.eye(4).col(k), bracket_basis(i, j))
    )
    assert J == sp.zeros(4, 1), (i, j, k, J)
    jacobi_sums[(i, j, k)] = J

# V together with [e1,e2] spans h, and z=[e1,e2]-e1.
generation_matrix = sp.Matrix.hstack(e1, e2, r, bracket(e1, e2))
assert generation_matrix.rank() == 4
assert bracket(e1, e2) - e1 == z

# Graph complement q_p = R w, w=z-p.
x, y, t = sp.symbols("x y t")
p = x * e1 + y * e2 + t * r
w = z - p


def split_projection(u):
    """Return (V coordinates, coefficient of w) for u=Vpart+c*w."""
    c = sp.expand(u[3])
    vpart = sp.simplify(u - c * w)
    assert sp.simplify(vpart[3]) == 0
    return vpart[:3, :], c


# On the one-dimensional complement, the trace is its scalar coefficient.
vertical = []
for B in (e1, e2, r):
    _, coefficient = split_projection(bracket(B, w))
    vertical.append(sp.expand(coefficient))
assert vertical == [-y, x, 0]

# Matrix of pi_V ad_w restricted to V; its trace is the horizontal character.
horizontal_columns = []
for X in (e1, e2, r):
    vpart, _ = split_projection(bracket(w, X))
    horizontal_columns.append(vpart)
horizontal_matrix = sp.Matrix.hstack(*horizontal_columns)
horizontal_trace = sp.expand(sp.trace(horizontal_matrix))
assert horizontal_trace == 1 + x + y

# The original p=0 complement satisfies the necessary vertical half.
assert [expr.subs({x: 0, y: 0, t: 0}) for expr in vertical] == [0, 0, 0]

# Exact inconsistency certificate: the vertical ideal is <x,y>, while the
# horizontal balance polynomial has remainder 1 modulo this ideal.
balance_groebner = sp.groebner([vertical[0], vertical[1]], x, y, t, domain=sp.QQ)
horizontal_remainder = balance_groebner.reduce(horizontal_trace)[1]
assert horizontal_remainder == 1

print("Jacobi ordered triples checked:", len(jacobi_sums))
print("generation rank:", generation_matrix.rank())
print("vertical traces:", vertical)
print("horizontal trace:", horizontal_trace)
print("horizontal remainder modulo vertical ideal:", horizontal_remainder)
print("VERIFIED")
