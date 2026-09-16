#!/usr/bin/env python3
"""Exact certificate and optimal-face checks for win-00060-p03.

All equalities are checked in Q(alpha), where alpha is the real root in
(-1/24,-1/25) of 32*a^3+48*a^2+26*a+1.  Sign checks use rational interval
arithmetic on that isolating interval, not floating point.
"""

import itertools
import sympy as sp


a = sp.symbols("a")
P = sp.Poly(32 * a**3 + 48 * a**2 + 26 * a + 1, a, domain=sp.QQ)
ALO, AHI = -sp.Rational(1, 24), -sp.Rational(1, 25)


def red(expr):
    """Reduce an element of Q(a) modulo P."""
    expr = sp.cancel(expr)
    num, den = sp.fraction(expr)
    num = sp.rem(sp.Poly(num, a, domain=sp.QQ), P).as_expr()
    den = sp.rem(sp.Poly(den, a, domain=sp.QQ), P).as_expr()
    inv = sp.invert(sp.Poly(den, a, domain=sp.QQ), P).as_expr()
    return sp.factor(sp.rem(sp.Poly(num * inv, a, domain=sp.QQ), P).as_expr())


def interval_add(x, y):
    return x[0] + y[0], x[1] + y[1]


def interval_mul(x, y):
    vals = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return min(vals), max(vals)


def interval_poly(expr):
    """A rational enclosure of expr(a) on [ALO,AHI]."""
    expr = red(expr)
    poly = sp.Poly(expr, a, domain=sp.QQ)
    out = (sp.Rational(0), sp.Rational(0))
    for coefficient in poly.all_coeffs():
        out = interval_add(interval_mul(out, (ALO, AHI)), (coefficient, coefficient))
    return out


def positive(expr):
    lo, _ = interval_poly(expr)
    assert lo > 0, (expr, interval_poly(expr))


# P is strictly increasing on the isolating interval and changes sign there.
assert P.eval(ALO) == -sp.Rational(1, 432)
assert P.eval(AHI) == sp.Rational(543, 15625)
positive(sp.diff(P.as_expr(), a))

# Dual certificate.  Its lower 4-by-4 diagonal is diag(Q).
v = (8 * a**2 + 8 * a + 1) / 2
w = -2 * a - 1
t = (32 * a**2 + 16 * a + 1) / 36
S = sp.Matrix(
    [
        [t, sp.Rational(1, 4) - a - v, -sp.Rational(1, 2) - v - w, a, 0],
        [sp.Rational(1, 4) - a - v, sp.Rational(1, 4), -sp.Rational(1, 2) - a, v, 2 * a],
        [-sp.Rational(1, 2) - v - w, -sp.Rational(1, 2) - a, 1, w, v],
        [a, v, w, 1, -sp.Rational(1, 2) - a],
        [0, 2 * a, v, -sp.Rational(1, 2) - a, sp.Rational(1, 4)],
    ]
)
assert [S[i, i] for i in range(1, 5)] == [sp.Rational(1, 4), 1, 1, sp.Rational(1, 4)]

# Exact PSD proof for S: reverse-coordinate even/odd blocks of B=S[1:,1:]
# are rank-one PSD; the top row lies in their ranges; the Schur complement is 0.
e1, e12, e2 = sp.Rational(1, 4) + 2 * a, -sp.Rational(1, 2) - a + v, 1 + w
o1, o12, o2 = sp.Rational(1, 4) - 2 * a, -sp.Rational(1, 2) - a - v, 1 - w
assert red(e1 * e2 - e12**2) == 0
assert red(o1 * o2 - o12**2) == 0
for entry in (e1, e2, o1, o2):
    positive(entry)
k1 = sp.Rational(1, 4) - a - v
k2 = -sp.Rational(1, 2) - v - w
assert red(e1 * (k2 + a) - e12 * k1) == 0
assert red(o1 * (k2 - a) - o12 * k1) == 0
assert red(t - k1**2 / (2 * e1) - k1**2 / (2 * o1)) == 0
positive(t)

# The 16 dual atom slacks h_z-<S,F_z>-tau, with tau=0.
Q = sp.Matrix(
    [
        [sp.Rational(1, 4), -sp.Rational(1, 2), 0, 0],
        [-sp.Rational(1, 2), 1, -1, 0],
        [0, -1, 1, -sp.Rational(1, 2)],
        [0, 0, -sp.Rational(1, 2), sp.Rational(1, 4)],
    ]
)
cvec = [sp.Rational(1, 2), 1, 0, 0]
vertices = list(itertools.product((0, 1), repeat=4))
slacks = {}
for z in vertices:
    h = sum(cvec[i] * z[i] for i in range(4))
    h += sum(2 * Q[i, j] * z[i] * z[j] for i in range(4) for j in range(i + 1, 4))
    inner = 2 * sum(S[0, i + 1] * z[i] for i in range(4))
    inner += 2 * sum(S[i + 1, j + 1] * z[i] * z[j] for i in range(4) for j in range(i + 1, 4))
    slacks["".join(map(str, z))] = red(h - inner)

active = ("0000", "0001", "0011", "0111", "1010", "1111")
assert tuple(key for key, value in slacks.items() if value == 0) == active
for key, value in slacks.items():
    if key not in active:
        positive(value)

# The unique primal certificate.  The six entries are ordered as in `active`.
pstar = [
    4 * (5144 * a**2 + 3256 * a + 1711) / 35073,
    -2 * (7552 * a**2 + 3362 * a - 2779) / 35073,
    -8 * (1046 * a**2 + 1153 * a - 1193) / 35073,
    -2 * (7552 * a**2 + 3362 * a - 2779) / 35073,
    -(2576 * a**2 + 3376 * a - 725) / 35073,
    4 * (5144 * a**2 + 3256 * a + 1711) / 35073,
]
dstar = [
    (8368 * a**2 + 9224 * a + 2147) / 11691,
    -4 * (1204 * a**2 + 53 * a - 2245) / 35073,
    -(15760 * a**2 + 12812 * a - 19249) / 35073,
    -8 * (454 * a**2 - 349 * a - 1099) / 11691,
]
assert red(sum(pstar) - 1) == 0
for probability in pstar:
    positive(probability)

az = [tuple(map(int, key)) for key in active]
xstar = [sum(pstar[k] * az[k][i] for k in range(6)) for i in range(4)]
Xstar = sp.zeros(4)
for i in range(4):
    Xstar[i, i] = dstar[i]
for i in range(4):
    for j in range(i + 1, 4):
        Xstar[i, j] = Xstar[j, i] = sum(pstar[k] * az[k][i] * az[k][j] for k in range(6))
Ystar = sp.Matrix([[1, *xstar], *[[xstar[i], *list(Xstar.row(i))] for i in range(4)]])
assert all(red(entry) == 0 for entry in S * Ystar)

# Exact PSD proof for Ystar: it has rank 3 and a positive-definite principal
# 3-by-3 block on indices {0,1,2}.
assert all(red(Ystar.extract(I, I).det()) == 0 for I in itertools.combinations(range(5), 4))
minor2 = red(Ystar.extract((0, 1), (0, 1)).det())
minor3 = red(Ystar.extract((0, 1, 2), (0, 1, 2)).det())
positive(minor2)
positive(minor3)

objective = sum(Q[i, j] * Xstar[i, j] for i in range(4) for j in range(4))
objective += sum(cvec[i] * xstar[i] for i in range(4))
assert red(objective + t) == 0

# Full-face classification.  Strict atom slacks force every optimal p to be
# supported on `active`; PSD complementarity forces S*Y=0.  Exact row reduction
# of those equations and sum(p)=1 has rank 10 in the 10 remaining variables.
ps = sp.symbols("p0:6")
ds = sp.symbols("d1:5")
xs = [sum(ps[k] * az[k][i] for k in range(6)) for i in range(4)]
Xs = sp.zeros(4)
for i in range(4):
    Xs[i, i] = ds[i]
for i in range(4):
    for j in range(i + 1, 4):
        Xs[i, j] = Xs[j, i] = sum(ps[k] * az[k][i] * az[k][j] for k in range(6))
Ys = sp.Matrix([[1, *xs], *[[xs[i], *list(Xs.row(i))] for i in range(4)]])
equations = [sum(ps) - 1] + list(S * Ys)
A, rhs = sp.linear_eq_to_matrix(equations, list(ps) + list(ds))
aug = [[red(A[i, j]) for j in range(A.cols)] + [red(rhs[i, 0])] for i in range(A.rows)]
row = 0
pivots = []
for col in range(A.cols):
    pivot = next((i for i in range(row, len(aug)) if aug[i][col] != 0), None)
    if pivot is None:
        continue
    aug[row], aug[pivot] = aug[pivot], aug[row]
    scale = red(1 / aug[row][col])
    aug[row] = [red(entry * scale) for entry in aug[row]]
    for i in range(len(aug)):
        if i != row and aug[i][col] != 0:
            scale = aug[i][col]
            aug[i] = [red(aug[i][j] - scale * aug[row][j]) for j in range(A.cols + 1)]
    pivots.append(col)
    row += 1
assert pivots == list(range(10))
solution = [red(aug[i][-1]) for i in range(10)]
assert all(red(solution[i] - (pstar + dstar)[i]) == 0 for i in range(10))

# Minimal polynomial of t (and hence a compact exact encoding of the value).
T = sp.symbols("T")
assert sp.expand(
    sp.resultant(P.as_expr(), 36 * T - (32 * a**2 + 16 * a + 1), a)
    - 82944 * (576 * T**3 + 16 * T**2 + 92 * T - 1)
) == 0

print("exact checks passed")
print("alpha interval:", ALO, AHI)
print("v_* is", -t, "approximately", -float(t.subs(a, -0.04156226056964984)))
print("active atoms:", active)
print("p approximately:", [float(x.subs(a, -0.04156226056964984)) for x in pstar])
print("diag(X) approximately:", [float(x.subs(a, -0.04156226056964984)) for x in dstar])
