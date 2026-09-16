#!/usr/bin/env python3
"""Pure-Python exact verifier for the triage certificate.

The basis consists of exponent tuples (a,b,c,d), in lexicographic order, for
e1^a e2^b e3^c e4^d.  Matrix columns are images of basis vectors.
"""

from itertools import product


EXPECTED_DETERMINANT = 8412259151430144

X1 = [
    [2, 0, 0, -1],
    [1, 0, 0, -2],
    [1, -1, 1, 0],
    [-1, -1, 1, -3],
]
X2 = [
    [2, 1, 2, 2],
    [0, -2, 2, -1],
    [-2, -1, 2, -1],
    [2, 1, -2, -2],
]
X3 = [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [2, 1, -2, 1],
    [-2, -2, -1, 0],
]

BASIS = [a for a in product(range(4), repeat=4) if sum(a) == 3]
INDEX = {a: i for i, a in enumerate(BASIS)}
U_COLUMNS = [i for i, a in enumerate(BASIS) if a[3] == 0]


def rho(x):
    """Matrix of sum_ij x[i][j] e_i partial/e_j on Sym^3(C^4)."""
    out = [[0] * 20 for _ in range(20)]
    for column, exponent in enumerate(BASIS):
        for j in range(4):
            if exponent[j] == 0:
                continue
            for i in range(4):
                if x[i][j] == 0:
                    continue
                target = list(exponent)
                target[j] -= 1
                target[i] += 1
                row = INDEX[tuple(target)]
                out[row][column] += exponent[j] * x[i][j]
    return out


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(20)) for j in range(20)]
        for i in range(20)
    ]


def bareiss_determinant(matrix):
    """Fraction-free exact determinant, including the sign of row swaps."""
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def main():
    factors = [X1, X2, X3]
    traces = [sum(x[i][i] for i in range(4)) for x in factors]
    assert traces == [0, 0, 0]
    assert len(BASIS) == 20 and len(U_COLUMNS) == 10

    # m2 = rho(X1) rho(X2) rho(X3), so rho(X3) acts first.
    m2 = multiply(multiply(rho(X1), rho(X2)), rho(X3))
    spanning = []
    for row in range(20):
        identity_u = [1 if row == column else 0 for column in U_COLUMNS]
        m2_u = [m2[row][column] for column in U_COLUMNS]
        spanning.append(identity_u + m2_u)

    determinant = bareiss_determinant(spanning)
    print("basis =", BASIS)
    print("U column indices =", U_COLUMNS)
    print("traces =", traces)
    print("m1 = identity")
    print("m2 = rho(X1) rho(X2) rho(X3); X3 acts first")
    print("determinant =", determinant)
    assert determinant == EXPECTED_DETERMINANT
    print("certificate_verified = true")


if __name__ == "__main__":
    main()
