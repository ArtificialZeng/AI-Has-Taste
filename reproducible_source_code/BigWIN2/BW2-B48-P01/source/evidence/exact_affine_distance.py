#!/usr/bin/env python3
"""Replay exact rational KKT certificates for the five face orbits of B_3.

For a face G with vertex matrices A_i and complementary vertices B_j, the
program minimizes

    dist(aff(G), sum_j beta_j B_j)^2,  beta_j >= 0, sum_j beta_j = 1.

The listed alpha coefficients give the affine projection x of y onto aff(G).
Orthogonality to the direction space of aff(G), simplex feasibility, and the
simplex KKT inequalities are all checked over fractions.  Convexity then makes
each certificate global.
"""

from fractions import Fraction as F
from itertools import permutations


PERMS = tuple(permutations(range(3)))
LABEL = tuple("".join(str(j + 1) for j in p) for p in PERMS)
VERTICES = tuple(
    tuple(F(int(p[i] == j)) for i in range(3) for j in range(3))
    for p in PERMS
)


def add(*vectors):
    return tuple(sum(entries, F(0)) for entries in zip(*vectors))


def scale(c, vector):
    return tuple(c * entry for entry in vector)


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), F(0))


def affine_combination(indices, coefficients):
    return add(*(scale(c, VERTICES[i]) for i, c in zip(indices, coefficients)))


def fmt(value):
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


# (description, face vertex indices, affine alpha, complementary beta,
#  expected squared affine-hull distance)
CERTIFICATES = (
    ("vertex", (0,), (F(1),), (F(1, 3), F(1, 3), F(0), F(0), F(1, 3)), F(2)),
    (
        "3-cycle edge",
        (0, 3),
        (F(1, 2), F(1, 2)),
        (F(1, 3), F(1, 3), F(0), F(1, 3)),
        F(1, 2),
    ),
    (
        "transposition edge",
        (0, 1),
        (F(1, 2), F(1, 2)),
        (F(1, 4), F(1, 4), F(1, 4), F(1, 4)),
        F(9, 4),
    ),
    (
        "two-face",
        (0, 1, 2),
        (F(-1, 5), F(3, 5), F(3, 5)),
        (F(1, 2), F(1, 2), F(0)),
        F(9, 10),
    ),
    (
        "facet",
        (0, 1, 2, 3),
        (F(1, 4), F(1, 4), F(1, 4), F(1, 4)),
        (F(1, 2), F(1, 2)),
        F(9, 4),
    ),
)


def verify(description, face, alpha, beta, expected):
    complement = tuple(i for i in range(6) if i not in face)
    assert len(beta) == len(complement)
    assert sum(alpha, F(0)) == 1
    assert sum(beta, F(0)) == 1 and all(c >= 0 for c in beta)

    x = affine_combination(face, alpha)
    y = affine_combination(complement, beta)
    residual = sub(x, y)

    # x is the orthogonal projection of y onto aff(G).
    directions = tuple(sub(VERTICES[i], VERTICES[face[0]]) for i in face[1:])
    orthogonality = tuple(dot(residual, direction) for direction in directions)
    assert all(value == 0 for value in orthogonality)

    # Gradient of dist(aff(G), sum beta_j B_j)^2 at beta.
    gradient = tuple(-2 * dot(VERTICES[i], residual) for i in complement)
    active_values = tuple(g for g, c in zip(gradient, beta) if c > 0)
    multiplier = active_values[0]
    assert all(g == multiplier for g in active_values)
    assert all(g >= multiplier for g, c in zip(gradient, beta) if c == 0)

    squared_distance = dot(residual, residual)
    assert squared_distance == expected

    print(f"case={description}")
    print("  G=" + repr(tuple(LABEL[i] for i in face)))
    print("  complement=" + repr(tuple(LABEL[i] for i in complement)))
    print("  alpha=" + repr(tuple(fmt(c) for c in alpha)))
    print("  beta=" + repr(tuple(fmt(c) for c in beta)))
    print("  projection_orthogonality=" + repr(tuple(fmt(v) for v in orthogonality)))
    print("  beta_gradient=" + repr(tuple(fmt(v) for v in gradient)))
    print("  kkt_multiplier=" + fmt(multiplier))
    print("  squared_affine_distance=" + fmt(squared_distance))
    print("  affine_projection_in_G=" + repr(all(c >= 0 for c in alpha)))
    return squared_distance


def main():
    values = tuple(verify(*certificate) for certificate in CERTIFICATES)
    minimum = min(values)
    minimizers = tuple(i for i, value in enumerate(values) if value == minimum)
    assert minimum == F(1, 2)
    assert minimizers == (1,)
    # The sole affine minimizer has nonnegative alpha, hence supplies a direct
    # feasible face-to-complement witness with the same squared distance.
    assert all(c >= 0 for c in CERTIFICATES[minimizers[0]][2])
    print("all_squared_affine_distances=" + repr(tuple(fmt(v) for v in values)))
    print("unique_minimizing_representative=3-cycle edge")
    print("minimum_squared_affine_distance=1/2")
    print("minimum_face_containment=True")
    print("Phi(B_3)=1/sqrt(2)")


if __name__ == "__main__":
    main()
