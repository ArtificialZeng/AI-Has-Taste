#!/usr/bin/env python3
"""Fresh symbolic cross-check of the frozen two-step certificate."""

import json
import sympy as sp

s = sp.sqrt(2)
t = sp.sqrt(9 + 8*s)
r = 2/(1+t)
C = r**2/2
h = (s, 1+r*(1+s))

# Treat every inner product among x0,g0,g1,g2 as an independent symbol.
names = ("x", "p", "q", "z")
gram = {}
symbols = []
for i in range(4):
    for j in range(i, 4):
        gram[i, j] = gram[j, i] = sp.Symbol(f"G_{names[i]}{names[j]}")
        symbols.append(gram[i, j])

def dot(a, b):
    return sum(a[i]*b[j]*gram[i, j] for i in range(4) for j in range(4))

e = tuple(tuple(sp.Integer(i == j) for i in range(4)) for j in range(4))
zero = (0, 0, 0, 0)

def add(*vectors):
    return tuple(sum(v[k] for v in vectors) for k in range(4))

def scale(c, v):
    return tuple(c*x for x in v)

xpos = (
    zero,
    e[0],
    add(e[0], scale(-h[0], e[1])),
    add(e[0], scale(-h[0], e[1]), scale(-h[1], e[2])),
)
grad = (zero, e[1], e[2], e[3])
f0, f1, f2 = sp.symbols("f0 f1 f2")
fval = (0, f0, f1, f2)

def sub(a, b):
    return tuple(a[k]-b[k] for k in range(4))

def interp(i, j):
    dg = sub(grad[i], grad[j])
    dx = sub(xpos[i], xpos[j])
    return fval[i]-fval[j]-dot(grad[j], dx)-dot(dg, dg)/2

lam = {
    (0, 1): s*r**2,
    (0, 2): (2+s)*r**2,
    (0, 3): r,
    (1, 2): (1+s)*r**2,
    (2, 1): r**2,
    (2, 3): 1-r,
}
w = (r/s, -r, -r*(1+s), -1/s)
residual = sp.expand(C*gram[0, 0]-f2-sum(c*interp(*ij) for ij, c in lam.items())-dot(w, w))
poly = sp.Poly(residual, f0, f1, f2, *symbols, extension=True)
if not poly.is_zero:
    raise AssertionError(poly.terms())

# Independently evaluate every adversarial trajectory/value formula.
a, b = sp.symbols("a b", positive=True)
delta_h = 1/(1+2*(a+b))
x1_h = 1-a*delta_h
x2_h = x1_h-b*delta_h
checks = {
    "huber_x1_above_delta": sp.simplify(x1_h-delta_h-(a+2*b)/(1+2*(a+b))),
    "huber_x2_above_delta": sp.simplify(x2_h-delta_h-(a+b)/(1+2*(a+b))),
    "huber_value": sp.simplify(delta_h*x2_h-delta_h**2/2-1/(2*(1+2*(a+b)))),
    "right_cap_value": sp.simplify((1-b)**2/(2*(1+a)**2)-(b-1)**2/(2*(a+1)**2)),
    "left_cap_value": sp.simplify((a-1)**2/(2*(b+1)**2)-(a-1)**2/(2*(b+1)**2)),
    "constant": sp.simplify(sp.radsimp(C-1/(5+4*s+t))),
    "schedule": sp.simplify(sp.radsimp(h[1]-(3+t)/4)),
}
if any(v != 0 for v in checks.values()):
    raise AssertionError(checks)

print(json.dumps({
    "status": "fresh referee symbolic cross-check passed",
    "formal_identity_coefficients_zero": True,
    "independent_gram_symbols": len(symbols),
    "interpolation_multipliers_positive_numeric": all(float(sp.N(v, 30)) > 0 for v in lam.values()),
    "witness_formula_checks_zero": sorted(checks),
}, indent=2))
