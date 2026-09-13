#!/usr/bin/env python3
"""Discovery derivation of the scalar annihilators (not trusted by verifier)."""

import sympy as sp


t = sp.symbols("t")
q = 1 - 2*t
A = sp.Matrix([
    [-1, -1, 0],
    [-1/q, 1/q - 1, 0],
    [0, 0, (t - 3)/(2 - t)],
])
rows = [sp.Matrix([[1, 1, -1]])]
for _ in range(3):
    rows.append(sp.simplify(rows[-1].diff(t) + rows[-1]*A))

p0, p1, p2 = sp.symbols("p0 p1 p2")
solution = sp.solve(list(rows[3] + p2*rows[2] + p1*rows[1] + p0*rows[0]),
                    [p0, p1, p2], dict=True, simplify=True)[0]
denominator = sp.lcm([sp.cancel(solution[p]).as_numer_denom()[1]
                      for p in (p0, p1, p2)])
l3 = {
    0: sp.factor(denominator*solution[p0]),
    1: sp.factor(denominator*solution[p1]),
    2: sp.factor(denominator*solution[p2]),
    3: sp.factor(denominator),
}

m = {
    0: -1/((t + 1)**2*(2*t - 1)**2),
    1: (t - 2)/((t + 1)**2*(2*t - 1)**2),
    2: t/((t + 1)*(2*t - 1)),
}


def compose(left, right):
    out = {}
    for i, ai in left.items():
        for j, bj in right.items():
            for r in range(i + 1):
                order = i-r+j
                out[order] = out.get(order, 0) + ai*sp.binomial(i, r)*sp.diff(bj, t, r)
    return {k: sp.factor(v) for k, v in out.items()}


print("L3 coefficients by D-order:")
for order in sorted(l3):
    print(order, sp.expand(l3[order]))
print("M o L3 coefficients by D-order:")
for order, coefficient in sorted(compose(m, l3).items()):
    print(order, sp.factor(coefficient))
