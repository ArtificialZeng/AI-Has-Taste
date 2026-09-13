#!/usr/bin/env python3
"""Exact, dependency-free verifier for the time-eight path sums.

The first part enumerates all 70 return words and checks the five nonempty
sojourn classes against the closed formulas used in time8_classification.md.
The second part checks the univariate factor identities after r^2=x,
s^2=1-x.  All coefficients are exact integers/Fractions.
"""

from fractions import Fraction
from itertools import combinations


# Sparse Z[r,s,z] arithmetic.  A monomial key is (deg_r, deg_s, deg_z).
def padd(p, q):
    out = dict(p)
    for monomial, coefficient in q.items():
        out[monomial] = out.get(monomial, 0) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def pscale(c, p):
    return {m: c * a for m, a in p.items() if c * a}


def pmul(p, q):
    out = {}
    for (i, j, k), a in p.items():
        for (ii, jj, kk), b in q.items():
            m = (i + ii, j + jj, k + kk)
            out[m] = out.get(m, 0) + a * b
            if out[m] == 0:
                del out[m]
    return out


def ppow(p, n):
    out = {(0, 0, 0): 1}
    for _ in range(n):
        out = pmul(out, p)
    return out


ZERO = {}
ONE = {(0, 0, 0): 1}
R = {(1, 0, 0): 1}
S = {(0, 1, 0): 1}
Z = {(0, 0, 1): 1}


def mzero():
    return [[ZERO, ZERO], [ZERO, ZERO]]


def madd(a, b):
    return [[padd(a[i][j], b[i][j]) for j in range(2)] for i in range(2)]


def mmul(a, b):
    return [
        [padd(pmul(a[i][0], b[0][j]), pmul(a[i][1], b[1][j])) for j in range(2)]
        for i in range(2)
    ]


r2, s2 = ppow(R, 2), ppow(S, 2)
r3, s3 = ppow(R, 3), ppow(S, 3)
r4, s4 = ppow(R, 4), ppow(S, 4)
r6, s6 = ppow(R, 6), ppow(S, 6)
z3, z4, z5 = ppow(Z, 3), ppow(Z, 4), ppow(Z, 5)

P = [[R, pmul(S, Z)], [ZERO, ZERO]]
Q = [[ZERO, ZERO], [S, pscale(-1, pmul(R, Z))]]
identity = [[ONE, ZERO], [ZERO, ONE]]

gamma = {k: mzero() for k in range(9)}
path_count = {k: 0 for k in range(9)}
for right_positions_tuple in combinations(range(8), 4):
    right_positions = set(right_positions_tuple)
    position = 0
    sojourn = 0
    amplitude = identity
    for step_index in range(8):
        step = 1 if step_index in right_positions else -1
        if position > 0 or (position == 0 and step == 1):
            sojourn += 1
        amplitude = mmul(Q if step == 1 else P, amplitude)
        position += step
    assert position == 0
    gamma[sojourn] = madd(gamma[sojourn], amplitude)
    path_count[sojourn] += 1

f_rs = padd(
    padd(s6, pscale(-6, pmul(r2, s4))),
    padd(pscale(6, pmul(r4, s2)), pscale(-1, r6)),
)
A_rs = padd(padd(pscale(-1, s4), pscale(3, pmul(r2, s2))), pscale(-1, r4))
B_rs = padd(padd(s4, pscale(-5, pmul(r2, s2))), pscale(3, r4))
C_rs = padd(padd(pscale(-3, s4), pscale(5, pmul(r2, s2))), pscale(-1, r4))
M_rs = padd(padd(pscale(-2, s4), pscale(4, pmul(r2, s2))), pscale(-1, r4))
N_rs = padd(padd(pscale(-1, s4), pscale(4, pmul(r2, s2))), pscale(-2, r4))

r_s = pmul(R, S)
r_s3 = pmul(R, s3)
r2_s2 = pmul(r2, s2)

expected = {k: mzero() for k in range(9)}
expected[0] = [
    [ZERO, ZERO],
    [pmul(pmul(r_s, f_rs), z3), pmul(pmul(s2, f_rs), z4)],
]
expected[2] = [
    [pmul(pmul(r2_s2, A_rs), z4), pmul(pmul(r_s3, A_rs), z5)],
    [pmul(pmul(r_s3, B_rs), z3), pmul(pmul(r2_s2, C_rs), z4)],
]
expected[4] = [
    [pmul(pmul(r2_s2, M_rs), z4), pmul(pmul(r_s3, N_rs), z5)],
    [pscale(-1, pmul(pmul(r_s3, N_rs), z3)), pmul(pmul(r2_s2, M_rs), z4)],
]
expected[6] = [
    [pmul(pmul(r2_s2, C_rs), z4), pscale(-1, pmul(pmul(r_s3, B_rs), z5))],
    [pscale(-1, pmul(pmul(r_s3, A_rs), z3)), pmul(pmul(r2_s2, A_rs), z4)],
]
expected[8] = [
    [pmul(pmul(s2, f_rs), z4), pscale(-1, pmul(pmul(r_s, f_rs), z5))],
    [ZERO, ZERO],
]

assert sum(path_count.values()) == 70
assert path_count == {0: 14, 1: 0, 2: 14, 3: 0, 4: 14, 5: 0, 6: 14, 7: 0, 8: 14}
assert gamma == expected


# Sparse Q[x] arithmetic for the factorizations used in the proof.
def uadd(p, q):
    out = dict(p)
    for degree, coefficient in q.items():
        out[degree] = out.get(degree, Fraction(0)) + coefficient
        if out[degree] == 0:
            del out[degree]
    return out


def uscale(c, p):
    c = Fraction(c)
    return {d: c * a for d, a in p.items() if c * a}


def umul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] = out.get(i + j, Fraction(0)) + a * b
            if out[i + j] == 0:
                del out[i + j]
    return out


def upow(p, n):
    out = {0: Fraction(1)}
    for _ in range(n):
        out = umul(out, p)
    return out


def usub(p, q):
    return uadd(p, uscale(-1, q))


def ueval(p, value):
    value = Fraction(value)
    return sum(a * value**d for d, a in p.items())


one = {0: Fraction(1)}
x = {1: Fraction(1)}
y = usub(one, x)
xy = umul(x, y)
two_x_minus_one = usub(uscale(2, x), one)

f = uadd(
    uadd(upow(y, 3), uscale(-6, umul(x, upow(y, 2)))),
    uadd(uscale(6, umul(upow(x, 2), y)), uscale(-1, upow(x, 3))),
)
A = uadd(uadd(uscale(-1, upow(y, 2)), uscale(3, xy)), uscale(-1, upow(x, 2)))
B = uadd(uadd(upow(y, 2), uscale(-5, xy)), uscale(3, upow(x, 2)))
C = uadd(uadd(uscale(-3, upow(y, 2)), uscale(5, xy)), uscale(-1, upow(x, 2)))
M = uadd(uadd(uscale(-2, upow(y, 2)), uscale(4, xy)), uscale(-1, upow(x, 2)))
N = uadd(uadd(uscale(-1, upow(y, 2)), uscale(4, xy)), uscale(-2, upow(x, 2)))

f_factor = umul(usub(one, uscale(2, x)), uadd(usub(one, uscale(7, x)), uscale(7, upow(x, 2))))
assert f == f_factor
assert uadd(upow(A, 2), umul(B, C)) == uscale(2, umul(two_x_minus_one, f))

base = uscale(
    Fraction(1, 2),
    uadd(
        uadd(umul(upow(xy, 2), upow(A, 2)), umul(umul(xy, upow(y, 2)), upow(A, 2))),
        uadd(umul(umul(xy, upow(y, 2)), upow(B, 2)), umul(upow(xy, 2), upow(C, 2))),
    ),
)
w4 = uadd(umul(upow(xy, 2), upow(M, 2)), umul(umul(xy, upow(y, 2)), upow(N, 2)))
square_gap = umul(umul(upow(x, 2), upow(y, 3)), upow(two_x_minus_one, 2))
assert usub(base, w4) == square_gap
assert ueval(w4, Fraction(1, 2)) == Fraction(1, 128)

print("PASS: 70 exact return paths; class counts 14 at k=0,2,4,6,8")
print("PASS: all five Gamma_8 matrices match the closed formulas")
print("PASS: f=(1-2x)(1-7x+7x^2)")
print("PASS: A^2+BC=2(2x-1)f")
print("PASS: base(w2,w6)-w4=x^2(1-x)^3(2x-1)^2")
print("PASS: at x=1/2, w2=w4=w6=1/128")
