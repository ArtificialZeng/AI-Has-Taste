#!/usr/bin/env python3
"""Direct SymPy differentiation check, independent of the state-system derivation."""

import sympy as sp


t = sp.symbols("t")
s = sp.sqrt(1 - 2*t)
f = (1+s)/s*sp.exp(-1-t+s) - (2-t)*sp.exp(-t)

l3 = {
    0: 4*t**3 + 4*t**2 + 3*t - 18,
    1: 12*t**3 + 6*t**2 + 6*t - 15,
    2: 12*t**3 + 2*t**2 - 2*t - 1,
    3: 4*t**3 - 3*t + 1,
}
l5 = {
    0: 12,
    1: 12*t + 39,
    2: 2*t**2 + 37*t + 35,
    3: 6*t**2 + 36*t + 7,
    4: 6*t**2 + 10*t - 2,
    5: t*(2*t - 1),
}

for name, operator in (("L3", l3), ("L5", l5)):
    residual = sp.simplify(sum(coefficient*sp.diff(f, t, order)
                               for order, coefficient in operator.items()))
    if residual != 0:
        raise AssertionError(f"{name} direct residual is {residual}")
print("PASS: direct differentiation gives L3(F)=L5(F)=0")
