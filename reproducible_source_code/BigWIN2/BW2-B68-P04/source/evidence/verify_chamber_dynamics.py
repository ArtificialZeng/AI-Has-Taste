#!/usr/bin/env python3
"""Exact symbolic replay for evidence/chamber_dynamics.md."""

import sympy as sp

a, b, c = sp.symbols("a b c", positive=True)

# Representative weak chamber a >= b >= c.
ka = 1 + b * (a + 2 * c - b) / ((a + b) * (a + c))
kb = 1 + a * (b + 2 * c - a) / ((a + b) * (b + c))
kc = 1 + a * (c + 2 * b - a) / ((a + c) * (b + c))
K = a * ka + b * kb + c * kc
Fa = -a * (ka - K)
Fb = -b * (kb - K)
Fc = -c * (kc - K)

# The two exact log-ratio factors, modulo a+b+c=1.
p = (a - b) * (2 * a * b + 3 * c - 1) / (
    (a + b) * (a + c) * (b + c)
)
q = 2 * a * (b - c) / ((a + b) * (a + c))
assert sp.factor((kb - ka - p).subs(c, 1 - a - b)) == 0
assert sp.factor((kc - kb - q).subs(c, 1 - a - b)) == 0

# Simplex preservation and the maximum-coordinate/geodesic-wall factor.
assert sp.factor((Fa + Fb + Fc).subs(c, 1 - a - b)) == 0
P = a**2 + 2 * a * b + 3 * b**2 - 2 * b
Fa_factored = a * (1 - 2 * a) * P / ((a + b) * (a + c))
assert sp.factor((Fa - Fa_factored).subs(c, 1 - a - b)) == 0

# Exact geodesic-wall identity a=1/2, b+c=1/2, b>=c.
x = sp.Rational(1, 2)
y = sp.symbols("y", positive=True)
z = sp.Rational(1, 2) - y
kx = 1 + 3 * y * z / ((x + y) * (x + z))
ky = 1 + z / (x + y)
kz = 1 + y / (x + z)
assert sp.factor(y * (ky - kx) + z * (kz - kx)) == 0
wall_y_dot = y * (2 * y - 1) * (4 * y - 1) / ((y - 1) * (2 * y + 1))
wall_K = x * kx + y * ky + z * kz
assert sp.factor(-y * (ky - wall_K) - wall_y_dot) == 0

# Equal-minima median b=c=s: equilibrium and scalar ODE factors.
s = sp.symbols("s", positive=True)
aa = 1 - 2 * s
median_p = sp.factor(p.subs({a: aa, b: s, c: s}))
expected_p = (1 - 3 * s) * (4 * s - 1) / (2 * s * (1 - s))
assert sp.factor(median_p - expected_p) == 0
median_s_dot = -(1 - 2 * s) * (1 - 3 * s) * (4 * s - 1) / (2 * (1 - s))
assert sp.factor(-aa * s * expected_p - median_s_dot) == 0

# Equal-maxima median a=b=x, c=1-2x: strict Lyapunov factor.
u = sp.symbols("u", positive=True)
cc = 1 - 2 * u
equal_max_q = sp.factor(q.subs({a: u, b: u, c: cc}))
assert sp.factor(equal_max_q - (3 * u - 1) / (1 - u)) == 0

print("PASS: exact chamber factors, invariant walls, and scalar strata verified")
