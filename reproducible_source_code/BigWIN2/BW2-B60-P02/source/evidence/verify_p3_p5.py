#!/usr/bin/env python3
"""Exact certificate checker for the p=3,4,5 Schur complements.

All calculations use SymPy rationals and polynomial arithmetic. Coefficient
lists below are ordered from the constant coefficient upward.
"""

from sympy import Matrix, Poly, Rational, eye, factor, together, zeros


EXPECTED = {
    3: [
        (288030, [307, 288030]),
        (5184540, [25, 61422, 23211, 7368, 1728180]),
        (34563600, [0, 5880, 2840, 2120, 181635, 143000,
                    310954, 46422, 5526, 576060]),
    ],
    4: [
        (48007300, [51771, 48007300]),
        (3600547500, [24375, 27996320, 7713468, 5177100,
                      1200182500]),
        (72010950000, [875, 1739100, 975540, 1337000, 114382590,
                       258434400, 436320220, 46280808, 11648475,
                       1200182500]),
        (630095812500, [0, 61000, 62400, 94500, 6815025, 23373000,
                        48129900, 42105980, 24482475, 103345560,
                        146389600, 175877940, 193087755, 135333240,
                        7713468, 1035420, 60009125]),
    ],
    5: [
        (6916071394725, [6278291156, 6916071394725]),
        (20748214184175, [84567189, 106874255547, 28461576147,
                          25113164624, 6916071394725]),
        (414964283683500, [2668344, 4810393332, 2672153712,
                           4198766224, 474811709205, 1020581506614,
                           1660048955862, 170769456882, 56504620404,
                           6916071394725]),
        (72618749644612500, [333396, 832077540, 684736080,
                             1293181680, 122210625915, 462292088538,
                             1214092038530, 1612891692510,
                             1347981905385, 3856221165605,
                             10764841802388, 17921277398340,
                             15187050676180, 10287912491580,
                             569231522940, 100452658496,
                             6916071394725]),
        (5123978974923858000, [0, 32450544, 55714176, 139878144,
                               12001478076, 85474806984, 315059491656,
                               646065363384, 811064107476,
                               1531206650484, 4815423196416,
                               10864703913504, 16644420401196,
                               19355277131064, 17235330280896,
                               12474909886544, 10263697225341,
                               9027379754694, 9240770097776,
                               11347738287144, 8917299321651,
                               4238179481074, 1640073302706,
                               56923152294, 6278291156,
                               276642855789]),
    ],
}


def blocks(p, k):
    D = 5 * p * (p + 1)
    g = Rational(1, p * (4 * p + 5))
    U = Matrix([
        [Rational(i * j) * (-1) ** (i + j - 2) / (i + j - 1)
         for j in range(1, p + 1)]
        for i in range(1, p + 1)
    ])
    K = Matrix([
        [Rational(i * j, i + j - 1) * k ** (i + j - 1)
         for j in range(1, p + 1)]
        for i in range(1, p + 1)
    ])
    v = Matrix([i * k ** (i - 1) for i in range(1, p + 1)])
    P = U + g * eye(p)
    C = K - v * v.T / D
    S = C + g * eye(p) - g ** 2 * P.inv()
    return D, g, U, K, v, P, S


def verify():
    from sympy import symbols
    k = symbols("k")
    for p in range(1, 6):
        D, g, U, K, v, P, S = blocks(p, k)

        # Endpoint evaluation norm: (U^{-1})_11 = p^2.
        assert U.inv()[0, 0] == p * p

        # Check the stated two-square congruence against the direct matrix in
        # coordinates (y, alpha, beta).
        M = zeros(1 + 2 * p)
        M[0, 0] = D
        M[0, 1 + p:1 + 2 * p] = -v.T
        M[1 + p:1 + 2 * p, 0] = -v
        M[1:1 + p, 1:1 + p] = P
        M[1:1 + p, 1 + p:1 + 2 * p] = -g * eye(p)
        M[1 + p:1 + 2 * p, 1:1 + p] = -g * eye(p)
        M[1 + p:1 + 2 * p, 1 + p:1 + 2 * p] = K + g * eye(p)

        B = zeros(1 + 2 * p)
        B[0, 0] = D
        B[0, 1 + p:1 + 2 * p] = -v.T
        B[1 + p:1 + 2 * p, 0] = -v
        B[1 + p:1 + 2 * p, 1 + p:1 + 2 * p] = v * v.T / D

        Q = zeros(1 + 2 * p)
        Q[1:1 + p, 1:1 + p] = P
        Q[1:1 + p, 1 + p:1 + 2 * p] = -g * eye(p)
        Q[1 + p:1 + 2 * p, 1:1 + p] = -g * eye(p)
        Q[1 + p:1 + 2 * p, 1 + p:1 + 2 * p] = g ** 2 * P.inv()

        R = zeros(1 + 2 * p)
        R[1 + p:1 + 2 * p, 1 + p:1 + 2 * p] = S
        assert M == B + Q + R

        if p < 3:
            continue
        for j, (expected_den, expected_coeffs) in enumerate(EXPECTED[p], 1):
            num, den = together(factor(S[:j, :j].det())).as_numer_denom()
            polynomial = Poly(num.expand(), k)
            coeffs = [int(polynomial.nth(i))
                      for i in range(polynomial.degree() + 1)]
            assert int(den) == expected_den
            assert coeffs == expected_coeffs
            if j < p:
                assert all(c > 0 for c in coeffs)
            else:
                assert coeffs[0] == 0 and all(c > 0 for c in coeffs[1:])
    print("exact p=3,4,5 certificates verified")


if __name__ == "__main__":
    verify()
