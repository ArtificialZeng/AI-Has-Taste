#!/usr/bin/env python3
"""Second-path symbolic derivation of the defect recurrence using SymPy."""
import sympy as s

x = s.symbols("x")
L_num = 4 - x**2 + x**3
L_den = 1 - 4*x + x**3 - x**4
E_num = 4 + 15*x - 3*x**2 + x**4
E_den = 1 - 3*x**2 - 15*x**3 + 3*x**4 - x**6
multiplier = 231 + 233*x**2 + 30*x**3 + 6*x**4
expected_den = (231 - 460*x**2 - 3435*x**3 - 3585*x**5
                - 215*x**8 - 30*x**9 - 6*x**10)
expected_num = 924 + 3465*x + 239*x**2 + 3615*x**3 + 6*x**4 + 215*x**6 + 30*x**7 + 6*x**8

assert s.expand(E_den * multiplier - expected_den) == 0
assert s.expand(E_num * multiplier - expected_num) == 0

# Universal algebraic derivation: start from four independent indeterminates,
# apply the linear recurrence, form the defects, and check the order-six
# relation.  Translation invariance in the index makes this one polynomial
# identity valid at every n >= 6.
u = list(s.symbols("u0:4"))
for _ in range(4, 9):
    u.append(s.expand(4*u[-1] - u[-3] + u[-4]))
edef_generic = [(-1)**n * (u[n+1]**2 - u[n]*u[n+2]) for n in range(7)]
assert s.expand(edef_generic[6] - 3*edef_generic[4] - 15*edef_generic[3]
                + 3*edef_generic[2] - edef_generic[0]) == 0

# Directly regenerate L and its signed quadratic defect, then verify the
# claimed rational generating function through more coefficients than needed.
series_L = s.series(L_num / L_den, x, 0, 40).removeO()
vals = [int(series_L.coeff(x, n)) for n in range(40)]
edef = [(-1)**n * (vals[n+1]**2 - vals[n]*vals[n+2]) for n in range(38)]
series_E = s.series(E_num / E_den, x, 0, 38).removeO()
assert edef == [int(series_E.coeff(x, n)) for n in range(38)]
print("PASS universal defect identity, polynomial identities, and 38 coefficient cross-checks")
