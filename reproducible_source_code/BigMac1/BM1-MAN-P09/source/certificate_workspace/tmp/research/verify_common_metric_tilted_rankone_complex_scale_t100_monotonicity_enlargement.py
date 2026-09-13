#!/usr/bin/env python3
"""Fail-closed exact verifier for the seven-sign t radius 1/100 theorem.

Only the terminal sign groups danger, Delta, n, C0, C1, N0, and N1 are
formed.  The cubic discriminant and N_D are deliberately absent.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables checks")

from hashlib import sha256
from math import prod
import os
from pathlib import Path

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
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}

if os.environ.get("T100_TEST_BAD_DEPENDENCY") == "1":
    first = next(iter(DEPENDENCIES))
    DEPENDENCIES[first] = "0" * 64

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
    square = matrix * matrix
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

require(a > 0 and c > 0 and a**2 + c**2 == 1, "p normalization")
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
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q * free_Q)[2, 1]
)
require(sp.factor(sp.im(last_leak) + tau * (qfree - g)) == 0,
        "unconstrained gate center")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# First derivation: extract the scale cubic from the original conjugated gate.
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

# Second derivation: preserve both complex phases through real residual squares.
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
require(sp.factor(C2 + 3 * n**2 * TL - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature")
require(sp.factor(sp.diff(P, T, 2) - 2 * (C2 + 3 * n**2 * T)) == 0,
        "strict convexity identity")

sign_polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
if os.environ.get("T100_TEST_DROP_SIGN") == "1":
    sign_polynomials.pop("N0")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(sign_polynomials) == required_signs, "seven-sign dependency set")

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
    degree = tuple(
        sp.Poly(expression, *variables, domain=sp.QQ).degree(variable)
        for variable in variables
    )
    require(degree == expected_degrees[name], f"degree tuple {name}")

# Exact independently audited t=4 Bernstein minima on the two stitched cells.
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

# Absolute monomial bound for |partial_t p| on the full target box.
coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), sp.Rational(401, 100),
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


def absolute_power_majorant(expression):
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
    count, value = absolute_power_majorant(expression)
    require(count == expected_term_counts[name], f"derivative terms {name}")
    require(value == expected_majorants[name], f"derivative majorant {name}")
    majorants[name] = value

# Exact finite m/M ceiling among all fourteen necessary reserves.
finite_ratios = sorted(
    (sp.factor(center_minima[cell][name] / majorants[name]), cell, name)
    for cell in center_minima
    for name in required_signs
    if majorants[name] != 0
)
rho_star, limiting_cell, limiting_name = finite_ratios[0]
expected_rho_star = sp.Rational(
    139329982333373668764509741946217216,
    2461207401365957174292955503842740925,
)
require((limiting_cell, limiting_name) == ("r_low", "N0"),
        "wrong seven-sign bottleneck")
require(rho_star == expected_rho_star, "exact seven-sign safe ratio")
require(sum(1 for ratio, _, _ in finite_ratios if ratio == rho_star) == 1,
        "nonunique seven-sign bottleneck")
require(sp.Rational(1, 18) < rho_star < sp.Rational(1, 17),
        "safe-ratio reciprocal bracket")

def reserves_at(radius):
    return {
        cell: {
            name: sp.factor(center_minima[cell][name] - radius * majorants[name])
            for name in required_signs
        }
        for cell in center_minima
    }


# Requested discriminating tests, followed by the maximal current derivative box.
for denominator in (401, 400):
    trial = reserves_at(sp.Rational(1, denominator))
    require(all(value > 0 for cell in trial.values() for value in cell.values()),
            f"radius 1/{denominator}")

radius = sp.Rational(1, 100)
reserves = reserves_at(radius)
require(all(value > 0 for cell in reserves.values() for value in cell.values()),
        "radius 1/100 reserves")
require(radius < rho_star, "reserve ceiling does not exceed derivative box")
require((4 - radius, 4 + radius) == (
    sp.Rational(399, 100), sp.Rational(401, 100)
), "t endpoints")
require(radius > sp.Rational(1, 400) > sp.Rational(1, 401)
        > sp.Rational(1, 402), "strict enlargement chain")

expected_radius_100_reserves = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(5667, 2000),
        "n": sp.Rational(290259999, 1000000),
        "C0": sp.Rational(406149495807846037, 1250000000000000),
        "C1": sp.Rational(2230643124119677951, 2500000000000000),
        "N0": sp.Rational(458871633278856388086320747631159227,
                          1280000000000000000000000),
        "N1": sp.Rational(99020879552659421313731849,
                          640000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(5827, 2000),
        "n": sp.Rational(290279999, 1000000),
        "C0": sp.Rational(434134585013123909, 1250000000000000),
        "C1": sp.Rational(2362201275413817551, 2500000000000000),
        "N0": sp.Rational(495787360851046408419352824223002427,
                          1280000000000000000000000),
        "N1": sp.Rational(105071895941446064671187849,
                          640000000000000000),
    },
}
require(reserves == expected_radius_100_reserves, "radius 1/100 reserve table")

# Terminal dependency graph: no discriminant symbol exists here.
dependency_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*dependency_dag.values()) == required_signs,
        "terminal DAG closure")

# Exact complex endpoint witness at t=4+1/100.
witness_data = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(401, 100),
    tau: 1,
}
witness = Q.subs(witness_data)
require(sp.factor(witness.det()) == 0, "endpoint witness determinant")
require(Delta.subs(witness_data) == sp.Rational(30141, 10000),
        "endpoint witness Delta")
require(n.subs(witness_data) == sp.Rational(361670801, 1000000),
        "endpoint witness n")
require(g.subs(witness_data) == sp.Rational(599, 10000),
        "endpoint witness g")
require(qmin.subs(witness_data) - g.subs(witness_data)
        == sp.Rational(2126413273, 17730000) > 0,
        "endpoint witness legal branch")
require(danger.subs(witness_data) == -sp.Rational(19, 100),
        "endpoint witness danger")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    2304143350537886621, 628705800000000
) > 0, "endpoint witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
)) == -sp.Rational(30685556925187, 19700000000) < 0,
        "endpoint phase integrity")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "endpoint opposite phases")

print("PASS original complex gate, PSD rank-two boundary, and scale cubic")
print("PASS seven-sign safe ratio: r_low/N0, 1/18 < rho_star < 1/17")
print("PASS requested radii 1/401 and 1/400 on all fourteen reserves")
print("PASS stronger full derivative-box radius 1/100 on all fourteen reserves")
print("PASS exact endpoints, terminal DAG, and live-phase boundary witness")
print(f"rho_star={rho_star}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_1_100[{cell}][{name}]={reserves[cell][name]}")
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=monotonicity-certified t radius 1/100 partial theorem; general gate open")
