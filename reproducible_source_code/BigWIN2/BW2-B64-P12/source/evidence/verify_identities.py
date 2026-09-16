"""Exact symbolic checks for evidence/diagonal_orbit_proof.md.

Run with: python3 evidence/verify_identities.py
"""

import sympy as sp

a, b, q, t = sp.symbols("a b q t", positive=True)
m = (a**4 + b**4 + 1) / (a**2 + b**2 + 1)
d = 1 - m + q * m
A = sp.cancel(a**2 * (m - a**2 - q * m * a**2) / d)
B = sp.cancel(b**2 * (m - b**2 - q * m * b**2) / d)
P1 = sp.cancel(A.subs(q, 0))
P2 = sp.cancel(B.subs(q, 0))

checks = {
    "retraction_sum": sp.factor(P1 + P2 - 1),
    "fixed_line_a": sp.factor((P1 - a).subs(b, 1 - a)),
    "fixed_line_b": sp.factor((P2 - b).subs(b, 1 - a)),
    "defect": sp.factor(
        (1 - A - B)
        - q
        * (a**4 + b**4 + 1) ** 2
        / (a**2 - a**4 + b**2 - b**4 + q * (a**4 + b**4 + 1))
    ),
    "dA_dq": sp.factor(
        sp.diff(A, q) + a**2 * m**2 * (1 - a**2) / d**2
    ),
    "dB_dq": sp.factor(
        sp.diff(B, q) + b**2 * m**2 * (1 - b**2) / d**2
    ),
}

nu = 7 * t**2
r = [t, 2 * t, 3 * t]
r_next = [sp.expand(-nu * x**2 + (1 + nu) * x**4) for x in r]
target = [
    -6 * t**4 + 7 * t**6,
    -12 * t**4 + 112 * t**6,
    18 * t**4 + 567 * t**6,
]
checks["one_step"] = [sp.factor(x - y) for x, y in zip(r_next, target)]

failed = {name: value for name, value in checks.items() if value != 0 and value != [0, 0, 0]}
if failed:
    raise SystemExit(f"FAILED: {failed}")
print("all exact symbolic identities verified")
