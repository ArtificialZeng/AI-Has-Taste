#!/usr/bin/env python3
"""Exact symbolic replay for evidence/edge12_lp.md."""

import sympy as sp

a, b, c, eps = sp.symbols("a b c eps", positive=True)
D = (a + b) * (a + c)

d1 = 1 - eps - eps * b / (a + b)
d2 = -1 + eps + eps * c / (a + c)
d3 = eps * a * (b - c) / D
assert sp.cancel(d1 + d2 + d3) == 0

# Cell b >= c, with B the metric distance d(v2,v3).
B = sp.symbols("B", positive=True)
W_b = a * d1 + B * d3
k_b = sp.cancel((1 - W_b / a) / eps)
assert sp.simplify(k_b - (1 + b / (a + b) - B * (b - c) / D)) == 0

# Cell c >= b, with C the metric distance d(v3,v1).
C = sp.symbols("C", positive=True)
W_c = a * (-d2) + C * (-d3)
k_c = sp.cancel((1 - W_c / a) / eps)
assert sp.simplify(k_c - (1 + c / (a + c) - C * (c - b) / D)) == 0

# All-edge-geodesic specializations.
k_bg = sp.factor(k_b.subs(B, b))
k_cg = sp.factor(k_c.subs(C, c))
formula_bg = 1 + b * (a + 2 * c - b) / D
formula_cg = 1 + c * (a + 2 * b - c) / D
assert sp.simplify(k_bg - formula_bg) == 0
assert sp.simplify(k_cg - formula_cg) == 0
assert sp.factor(formula_bg - formula_cg) == (b - c) * (a - b - c) / D

# A different edge is non-geodesic.
assert sp.simplify(k_b.subs(B, a + c) - (1 + c / (a + b))) == 0
assert sp.simplify(k_c.subs(C, a + b) - (1 + b / (a + c))) == 0

# The tied edge a=1/2, equivalently a=b+c before normalization.
tied = 1 + 3 * b * c / ((a + b) * (a + c))
assert sp.simplify(formula_bg.subs(a, b + c) - tied.subs(a, b + c)) == 0
assert sp.simplify(formula_cg.subs(a, b + c) - tied.subs(a, b + c)) == 0

# Primal costs equal the stated dual objectives.
dual_b = a * d1 + B * d3
dual_c = a * d1 + (a - C) * d3
assert sp.simplify(W_b - dual_b) == 0
assert sp.simplify(W_c - dual_c) == 0

print("PASS: exact e_12 primal/dual and all cell formulas verified")
