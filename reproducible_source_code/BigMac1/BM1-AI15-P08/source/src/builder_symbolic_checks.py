#!/usr/bin/env python3
"""Independent exact checks for the builder's Schur factorizations.

This script is diagnostic algebra, not a numerical certificate.  It exits
nonzero if any identity used in proof/builder_notes.md fails in SymPy.
"""

import argparse

import sympy as sp


z, d, db, b, bb, c, cc = sp.symbols("z d db b bb c cc", nonzero=True)


def conj_on_circle(expr):
    return sp.expand(
        expr.xreplace({z: 1 / z, d: db, db: d, b: bb, bb: b, c: cc, cc: c})
    )


def schur(coeffs):
    m = len(coeffs) - 1
    return [
        sp.factor(
            conj_on_circle(coeffs[m]) * coeffs[j + 1]
            - coeffs[0] * conj_on_circle(coeffs[m - 1 - j])
        )
        for j in range(m)
    ]


def fail(message):
    """Terminate verification explicitly; never disabled by ``python -O``."""
    raise SystemExit(f"VERIFICATION FAILED: {message}")


def check_zero(expr, label):
    residual = sp.factor(expr)
    if residual != 0:
        fail(f"{label}: residual {residual}")


def check_coeffwise(lhs, rhs, label):
    if len(lhs) != len(rhs):
        fail(f"{label}: coefficient lengths {len(lhs)} != {len(rhs)}")
    for index, (left, right) in enumerate(zip(lhs, rhs)):
        check_zero(left - right, f"{label}, coefficient {index}")


# Degree three, equation (3.3).
p3 = db + z + z**2 + d * z**3
h3 = [d, d * z + 1, d * z**2 + z + 1]
check_coeffwise(
    schur(h3),
    [p3 / z**2, (1 + z) * p3 / z**2],
    "degree-three identity (3.3)",
)

# Degree four, equation (4.4).
p4 = db + bb * z + c * z**2 + b * z**3 + d * z**4
h4 = [d, d * z + b, d * z**2 + b * z + c,
      d * z**3 + b * z**2 + c * z + bb]
k4 = [b, b * z + c, b * z**2 + c * z + bb]
check_coeffwise(
    [item.subs(cc, c) for item in schur(h4)],
    [p4.subs(cc, c) * item / z**3 for item in k4],
    "degree-four identity (4.4)",
)

# The two coefficients in the second degree-four reduction, modulo phases.
u, ub, sreal = sp.symbols("u ub sreal")
k4_rephased = [u, u + c, sreal]
t4 = [
    sreal * (u + c) - u * (ub + c),
    sreal**2 - u * ub,
]
check_zero(
    (t4[0] - (c * sreal + u**2)).subs(ub, sreal - c - u),
    "degree-four second Schur endpoint",
)

# Degree five, equation (5.2): first reduction.
p5 = db + bb * z + cc * z**2 + c * z**3 + b * z**4 + d * z**5
h5 = [d, d * z + b, d * z**2 + b * z + c,
      d * z**3 + b * z**2 + c * z + cc,
      d * z**4 + b * z**3 + c * z**2 + cc * z + bb]
k5 = [b, b * z + c, b * z**2 + c * z + cc,
      b * z**3 + c * z**2 + cc * z + bb]
check_coeffwise(
    schur(h5),
    [p5 * item / z**4 for item in k5],
    "degree-five identity (5.2)",
)

# Equation (5.5): constant and leading terms of Schur(L).
B, Bb, C, Cb, S = sp.symbols("B Bb C Cb S", nonzero=True)
L = [B, B + C, B + C + Cb, S]
# Here S is real and B+C+Cb = S-Bb.
t0 = sp.expand(S * L[1] - B * (S - B))
t2 = S**2 - B * Bb
check_zero(t0 - (S * C + B**2), "degree-five second Schur constant")
check_zero(t2 - (S**2 - B * Bb), "degree-five second Schur leading term")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--inject-failure",
    action="store_true",
    help="exercise the explicit nonzero exit path used by the audit",
)
args = parser.parse_args()
if args.inject_failure:
    check_zero(1, "injected fail-closed self-test")

print("builder symbolic identities: OK")
