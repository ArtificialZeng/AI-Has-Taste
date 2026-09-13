#!/usr/bin/env python3
"""Fail-closed exact source verifier for the monotonicity-only t radius 1/402.

The verifier reconstructs the original fully conjugated Hermitian gate and
the rank-two scale cubic.  It deliberately does not form or assume the cubic
discriminant: the g<=0 coefficient proof and the g>0 endpoint-derivative /
strict-convexity proof do not use it.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables checks")

from hashlib import sha256
from math import prod
from pathlib import Path
import os

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


DEPENDENCIES = {
    "tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md":
        "b049ead438ebbe295d39d76608afdba9d23cd0e5e1bb61f2a5fc346259387742",
    "tmp/research/common_metric_tilted_rankone_complex_scale_r_adjacent_theorem.md":
        "3e2dcc40cb2997499ac29f735c9956278fa2c40c10bd9068c441ed8c3b5bbe15",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_rbox_theorem.py":
        "4dbcb35560800abc11ef9016438df186aa37462e1b53d1c25c29098f0b637efe",
    "audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py":
        "5836cc5e45d13bccb8a2111affdf1579fd1bd3a5da2a1bfec0f2c33dea6c3a09",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_RBOX_REFEREE_AUDIT.md":
        "81de7f859652face01fd3f760085d28956a0c61fab2c6f3c5c392ba12693859f",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_R_ADJACENT_REFEREE_AUDIT.md":
        "4fb0e88fc357ab443269935262b6e21c65838511f75b1fcb31ae09366cee721c",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
}

if os.environ.get("T402_SOURCE_TEST_BAD_DEPENDENCY") == "1":
    first_dependency = next(iter(DEPENDENCIES))
    DEPENDENCIES[first_dependency] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a, c):
    vector = sp.Matrix([a, 0, c])
    image = matrix * vector
    square = matrix**2
    return sp.expand(
        a**2 * modulus_square(image[1])
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0])**2
    )


ell, w, k, z, r, t, tau, T, qfree = sp.symbols(
    "ell w k z r t tau T qfree", real=True
)
variables = (ell, w, k, z, r, t)
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
Delta = sp.factor(r * t - z**2 - w**2)
n = sp.factor(t * (k**2 + ell**2) + r - 2 * (k * z + ell * w))
g = sp.factor(a * c * ell - z * k - w * ell - t)
qmin = tau**2 * n / Delta
Q = sp.Matrix([
    [r, tau * (k + sp.I * ell), z + sp.I * w],
    [tau * (k - sp.I * ell), qmin, tau],
    [z - sp.I * w, tau, t],
])

require(Q == sp.conjugate(Q.T), "Hermitian conjugates")
active = Q.extract([0, 2], [0, 2])
coupling = Q.extract([0, 2], [1])
require(sp.factor(active.det() - Delta) == 0, "active determinant")
require(sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0, "zero Schur complement")
require(sp.factor(Q.det()) == 0, "rank-two determinant")
danger = sp.factor(sp.re((Q * sp.Matrix([a, 0, c]))[0]))
require(sp.factor(danger - (a * r + c * z)) == 0, "danger scalar")

free_Q = Q.copy()
free_Q[1, 1] = qfree
free_image = free_Q * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q**2)[2, 1]
)
require(sp.factor(sp.im(last_leak) + tau * (qfree - g)) == 0,
        "unconstrained gate center")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# First derivation: extract P(T) directly from the fully conjugated gate.
raw_tau = sp.Poly(sp.expand(4 * Delta**2 * original_gate(Q, a, c)), tau)
require(all(power[0] % 2 == 0 for power, _ in raw_tau.terms()),
        "odd coupling power")
scale_poly = sp.Poly(sum(
    coefficient * T**(power[0] // 2)
    for power, coefficient in raw_tau.terms()
), T)
require(scale_poly.degree() == 3, "scale cubic degree")
P = scale_poly.as_expr()
C0 = sp.factor(scale_poly.coeff_monomial(1))
C1 = sp.factor(scale_poly.coeff_monomial(T))
C2 = sp.factor(scale_poly.coeff_monomial(T**2))
require(sp.factor(scale_poly.coeff_monomial(T**3) - n**2) == 0,
        "leading coefficient")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "C2 identity")

# Second derivation: exact residual squares, retaining both phase coordinates.
x = a * r + c * z
L = a * k + c
A = a * c * (r + t) + z - w * (r + t)
B = a * c - w - z * (r + t)
C = c * L + z * ell - w * k
square_formula = sp.expand(
    Delta**2 * (
        (A - T * ell)**2 + (B - T * k)**2 - 32 * a**2 * x**2
        + T * (4 * a**2 * (L**2 + a**2 * ell**2) + C**2)
    )
    + T * (T * n - Delta * g)**2
)
require(sp.factor(P - square_formula) == 0, "second cubic derivation")

TL = sp.factor(Delta * g / n)
N0, D0 = sp.cancel(P.subs(T, TL)).as_numer_denom()
N1_raw, D1 = sp.cancel(sp.diff(P, T).subs(T, TL)).as_numer_denom()
N1 = -N1_raw
require(sp.factor(D0 - 15625 * n**2) == 0, "endpoint denominator")
require(sp.factor(D1 + 625 * n) == 0, "derivative denominator")
endpoint_curvature = sp.factor(C2 + 3 * n**2 * TL)
require(sp.factor(endpoint_curvature - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature identity")
require(sp.factor(sp.diff(P, T, 2) - 2 * (C2 + 3 * n**2 * T)) == 0,
        "strict convexity identity")

# This is the complete logical dependency set.  No discriminant polynomial
# or discriminant sign is constructed below.
sign_polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
expected_degrees = {
    "danger": (0, 0, 0, 1, 1, 0),
    "Delta": (0, 2, 0, 2, 1, 1),
    "n": (2, 1, 2, 1, 1, 1),
    "C0": (0, 6, 0, 6, 4, 4),
    "C1": (2, 6, 2, 6, 3, 4),
    "N0": (5, 10, 5, 10, 6, 6),
    "N1": (4, 7, 4, 7, 4, 4),
}
for name, expression in sign_polynomials.items():
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    degree = tuple(polynomial.degree(variable) for variable in variables)
    require(degree == expected_degrees[name], f"degree tuple {name}")

center_minima = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(14219, 5000),
        "n": sp.Rational(1456753, 5000),
        "C0": sp.Rational(420515573041543529, 1250000000000000),
        "C1": sp.Rational(1195599356262447793, 1250000000000000),
        "N0": sp.Rational(544257743489740893611366179477411,
                          1250000000000000000000),
        "N1": sp.Rational(3448220588099013077412457,
                          20000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(14619, 5000),
        "n": sp.Rational(1456853, 5000),
        "C0": sp.Rational(448500662246821401, 1250000000000000),
        "C1": sp.Rational(1261378431909517593, 1250000000000000),
        "N0": sp.Rational(4642466069575661682742742534193063,
                          10000000000000000000000),
        "N1": sp.Rational(3637314850248595682332957,
                          20000000000000000),
    },
}

coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100),
    sp.Rational(401, 100),
)
expected_term_counts = {
    "danger": 1, "Delta": 1, "n": 2, "C0": 62,
    "C1": 67, "N0": 1851, "N1": 326,
}
expected_majorants = {
    "danger": sp.Integer(0),
    "Delta": sp.Rational(103, 100),
    "n": sp.Rational(1090601, 10000),
    "C0": sp.Rational(3591519308424373, 3125000000000),
    "C1": sp.Rational(32111117681043527, 5000000000000),
    "N0": sp.Rational(
        98448296054638286971718220153709637,
        12800000000000000000000,
    ),
    "N1": sp.Rational(452887170660359886538671,
                      256000000000000),
}


def exact_power_majorant(expression):
    terms = sp.Poly(sp.diff(expression, t), *variables, domain=sp.QQ).terms()
    value = sum(
        abs(coefficient) * prod(
            cap**power for cap, power in zip(coordinate_caps, powers)
        )
        for powers, coefficient in terms
    )
    return len(terms), sp.factor(value)


majorants = {}
for name, expression in sign_polynomials.items():
    count, value = exact_power_majorant(expression)
    require(count == expected_term_counts[name], f"derivative terms {name}")
    require(value == expected_majorants[name], f"derivative majorant {name}")
    majorants[name] = value

radius = sp.Rational(1, 402)
target_left, target_right = 4 - radius, 4 + radius
require((target_left, target_right) == (
    sp.Rational(1607, 402), sp.Rational(1609, 402)
), "t endpoints")
require(sp.Rational(399, 100) <= target_left < target_right
        <= sp.Rational(401, 100), "target outside derivative box")
require(radius > sp.Rational(1, 403) > sp.Rational(1, 500),
        "strict interval enlargement")

reserves = {
    cell: {
        name: sp.factor(minima[name] - radius * majorants[name])
        for name in sign_polynomials
    }
    for cell, minima in center_minima.items()
}
for cell, values in reserves.items():
    for name, value in values.items():
        require(value > 0, f"nonpositive reserve {cell}/{name}")

minimum_reserves = {
    name: min(values[name] for values in reserves.values())
    for name in sign_polynomials
}
expected_minimum_reserves = {
    "danger": sp.Rational(87, 500),
    "Delta": sp.Rational(713861, 251250),
    "n": sp.Rational(1170138811, 4020000),
    "C0": sp.Rational(83805326319665374729, 251250000000000000),
    "C1": sp.Rational(118150790449310782759, 125625000000000000),
    "N0": sp.Rational(
        53549445496650257669039960758536579907,
        128640000000000000000000000,
    ),
    "N1": sp.Rational(3602140976554567042623930779,
                      21440000000000000000),
}
require(minimum_reserves == expected_minimum_reserves,
        "minimum reserve table")

# Exact branch dependency test: neither branch references a discriminant.
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "g<=0 C2 proof")
require(sp.factor(endpoint_curvature - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "g>0 curvature proof")

# Nonredundancy of t after quotienting active-block common scale.
wide_left = sp.Rational(399, 100)
require(wide_left - 2 * sp.Rational(103, 100) > 0,
        "shape derivative not increasing in r")
shape_margin = (
    sp.Rational(99, 100) * wide_left
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(461, 625) > 0,
        "spectral-shape nonredundancy")

# Exact simultaneous-phase witness inside the enlarged interval.
witness_data = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(2001, 500),
    tau: 1,
}
witness = Q.subs(witness_data)
require(target_left < witness_data[t] < target_right,
        "phase witness outside interval")
require(sp.factor(witness.det()) == 0, "phase witness determinant")
require(qmin.subs(witness_data) > g.subs(witness_data),
        "phase witness legal branch")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    414461983319631411704949, 112939929245000000000
) > 0, "phase witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
)) == -sp.Rational(
    585660171418319979, 375732500000000
) < 0, "phase integrity")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "opposite phase product")

print("PASS original Hermitian gate, rank-two boundary, and complete legal scale half-line")
print("PASS exact branch dependency DAG: discriminant ND is unused")
print("PASS seven essential derivative reserves on both stitched r cells at radius 1/402")
print("PASS strict enlargement, nonredundancy, endpoints, and simultaneous-phase witness")
print("scope=monotonicity-certified t partial theorem; unrestricted complex gate remains open")
