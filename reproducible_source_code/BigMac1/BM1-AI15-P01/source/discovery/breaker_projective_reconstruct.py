#!/usr/bin/env python3
"""Reconstruct the rational decomposition from a Segre/tensor boundary chart.

This is discovery provenance, not the trusted verifier.  It uses only exact
fractions and starts from W = diag(1,1/4,1,1/3) P, where every row of P is a
decomposable 2-by-2 tensor.  It solves W Z = M and checks that every column of
Z is decomposable as well.
"""

from fractions import Fraction as Q


def inverse(matrix):
    n = len(matrix)
    augmented = [list(row) + [Q(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if augmented[row][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        scale = augmented[col][col]
        augmented[col] = [entry / scale for entry in augmented[col]]
        for row in range(n):
            if row != col and augmented[row][col]:
                scale = augmented[row][col]
                augmented[row] = [
                    augmented[row][j] - scale * augmented[col][j] for j in range(2 * n)
                ]
    return [row[n:] for row in augmented]


def matmul(left, right):
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0)) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


M = [
    [Q(1), Q(1), Q(1), Q(1)],
    [Q(1), Q(1), Q(1), Q(0)],
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(1), Q(0), Q(0), Q(0)],
]
P = [
    [Q(1), Q(0), Q(0), Q(0)],
    [Q(1), Q(1), Q(1), Q(1)],
    [Q(0), Q(0), Q(0), Q(1)],
    [Q(0), Q(0), Q(1), Q(-1)],
]
row_scales = [Q(1), Q(1, 4), Q(1), Q(1, 3)]
W = [[row_scales[i] * P[i][j] for j in range(4)] for i in range(4)]
Z = matmul(inverse(W), M)

expected_z = [
    [Q(1), Q(1), Q(1), Q(1)],
    [Q(0), Q(1), Q(3), Q(-1)],
    [Q(3), Q(1), Q(0), Q(0)],
    [Q(0), Q(1), Q(0), Q(0)],
]
assert Z == expected_z
assert matmul(W, Z) == M
assert all(Z[0][j] * Z[3][j] == Z[1][j] * Z[2][j] for j in range(4))

print("W =")
for row in W:
    print(" ", [str(value) for value in row])
print("Z = W^{-1} M =")
for row in Z:
    print(" ", [str(value) for value in row])
print("PASS: WZ=M and all rows of W / columns of Z are decomposable tensors")
