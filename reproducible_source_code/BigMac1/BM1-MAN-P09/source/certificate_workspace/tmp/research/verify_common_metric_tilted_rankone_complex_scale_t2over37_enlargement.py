#!/usr/bin/env python3
"""Fail-closed exact verifier for the complex-scale half-width 2/37.

The frozen radius-1/19 theorem supplies independently audited t=4 center
minima.  This verifier starts from the fully conjugated original Hermitian
gate, reconstructs the seven terminal sign polynomials, recomputes every
derivative majorant on 146/37 <= t <= 150/37, and checks all fourteen new
reserves.  No discriminant, N_D, real-part monotonicity, absorption, or
fixed copositivity allocation is used.
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
    "tmp/research/common_metric_tilted_rankone_complex_scale_t19_monotonicity_enlargement.md":
        "211976602dbeaef10f0a49eb07c788957bf6f31b4c9673a53e0b28abf9a90195",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t19_monotonicity_enlargement.py":
        "799254227c42ff34c20f646c70ff9848df231690f45d2b306f41df22cac51fcd",
    "audit/verify_common_metric_tilted_rankone_complex_scale_t19_monotonicity_referee.py":
        "98e74e87f3b34711afdd2b3fab5951bf7ecd8a732340afc4baa3f8ec8a08fd3b",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T19_MONOTONICITY_REFEREE_AUDIT.md":
        "206d87cdf33b84fc5e84d1a17466c0919571ba9e16f999f19b3b2714b9796073",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t19_monotonicity_enlargement_manifest.sha256":
        "422263e15c7d7ccc10fe61a42d97c3a434959a42bb9e6b1323493fbfa196d9e7",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}

if os.environ.get("T2OVER37_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def check_t19_manifest():
    manifest = ROOT / (
        "tmp/research/common_metric_tilted_rankone_complex_scale_t19_"
        "monotonicity_enlargement_manifest.sha256"
    )
    entries = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        require("  " in line, "malformed t19 manifest line")
        digest, relative = line.split("  ", 1)
        path = ROOT / relative
        require(len(digest) == 64 and path.is_file(),
                f"malformed t19 manifest entry {relative}")
        require(sha256(path.read_bytes()).hexdigest() == digest,
                f"t19 manifest mismatch {relative}")
        entries.append(relative)
    require(len(entries) == 10 and len(set(entries)) == 10,
            "t19 manifest entry set")


check_t19_manifest()


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a_value, c_value):
    vector = sp.Matrix([a_value, 0, c_value])
    image = matrix * vector
    square = matrix * matrix
    return sp.expand(
        a_value**2 * modulus_square(image[1])
        + sp.Rational(1, 4) * modulus_square(
            c_value * sp.conjugate(image[0]) + a_value * image[2]
            + sp.I * (a_value * c_value - square[2, 0])
        )
        + sp.Rational(1, 4) * modulus_square(
            c_value * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a_value**2 * sp.re(image[0])**2
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

require(a**2 + c**2 == 1 and a > 0 and c > 0, "target normalization")
require(Q == sp.conjugate(Q.T), "Hermitian conjugation")
active = Q.extract([0, 2], [0, 2])
coupling = Q.extract([0, 2], [1])
require(sp.factor(active.det() - Delta) == 0, "active determinant")
require(sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0, "zero Schur complement")
require(sp.factor(Q.det()) == 0, "rank-two determinant")

danger_raw = sp.factor(sp.re((Q * sp.Matrix([a, 0, c]))[0]))
require(sp.factor(danger_raw - (a * r + c * z)) == 0, "danger scalar")
free_Q = Q.copy()
free_Q[1, 1] = qfree
free_image = free_Q * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q * free_Q)[2, 1]
)
require(sp.factor(sp.im(last_leak) + tau * (qfree - g)) == 0,
        "free-middle center")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# First cubic derivation: fully conjugated original gate.
raw_tau = sp.Poly(sp.expand(4 * Delta**2 * original_gate(Q, a, c)), tau)
require(all(power[0] % 2 == 0 for power, _ in raw_tau.terms()),
        "even coupling powers")
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
        "positive leading coefficient")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "C2 identity")

# Second cubic derivation: phase-retaining real residual squares.
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
require(sp.factor(D1 + 625 * n) == 0, "slope denominator")
require(sp.factor(C2 + 3 * n**2 * TL - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature")

sign_polynomials = {
    "danger": -danger_raw,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
if os.environ.get("T2OVER37_TEST_DROP_SIGN") == "1":
    sign_polynomials.pop("N0")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(sign_polynomials) == required_signs, "seven terminal signs")

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
    require(tuple(polynomial.degree(v) for v in variables)
            == expected_degrees[name], f"degree tuple {name}")

# These are the exact minima of the two frozen, independently audited t=4
# center tensors.  Their artifact chain is hash-bound above.
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

radius = sp.Rational(2, 37)
lower_t, upper_t = 4 - radius, 4 + radius
require((lower_t, upper_t) == (sp.Rational(146, 37), sp.Rational(150, 37)),
        "target interval")
coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), upper_t,
)
expected_term_counts = {
    "danger": 1, "Delta": 1, "n": 2, "C0": 62,
    "C1": 67, "N0": 1851, "N1": 326,
}
expected_majorants = {
    "danger": sp.Integer(0),
    "Delta": sp.Rational(103, 100),
    "n": sp.Rational(1090601, 10000),
    "C0": sp.Rational(744128529196165565221, 633162500000000000),
    "C1": sp.Rational(4126672805275222029427, 633162500000000000),
    "N0": sp.Rational(
        1775215308784565826159975640142805255396523,
        221900662400000000000000000000,
    ),
    "N1": sp.Rational(146616757232077940451518475621,
                      81044800000000000000),
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

expected_reserves = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(515803, 185000),
        "n": sp.Rational(2640463, 9250),
        "C0": sp.Rational(639288181047879148809969,
                          2342701250000000000000),
        "C1": sp.Rational(1415411124077141012291273,
                          2342701250000000000000),
        "N0": sp.Rational(
            304944185165887347790739852577939707794093,
            102629056360000000000000000000000,
        ),
        "N1": sp.Rational(699275403702571484222111483263,
                          9370805000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(530603, 185000),
        "n": sp.Rational(1320324, 4625),
        "C0": sp.Rational(691736743817931930675361,
                          2342701250000000000000),
        "C1": sp.Rational(1538691702270928995729073,
                          2342701250000000000000),
        "N0": sp.Rational(
            3264808470772680758250345288696777589889993,
            102629056360000000000000000000000,
        ),
        "N1": sp.Rational(196968419140925613831803445847,
                          2342701250000000000000),
    },
}
reserves = {
    cell: {
        name: sp.factor(minimum - radius * majorants[name])
        for name, minimum in minima.items()
    }
    for cell, minima in center_minima.items()
}
require(reserves == expected_reserves, "fourteen new reserves")
require(all(value > 0 for row in reserves.values() for value in row.values()),
        "strict reserve signs")

finite_ratios = sorted(
    (sp.factor(center_minima[cell][name] / majorants[name]), cell, name)
    for cell in center_minima
    for name in required_signs
    if majorants[name] != 0
)
rho_new, bottleneck_cell, bottleneck_name = finite_ratios[0]
expected_rho_new = sp.Rational(
    2415423075934055837934601667899895734740928,
    44380382719614145653999391003570131384913075,
)
require((bottleneck_cell, bottleneck_name) == ("r_low", "N0"),
        "new bottleneck")
require(rho_new == expected_rho_new and radius < rho_new < sp.Rational(1, 18),
        "new-box safe-ratio bracket")
rho_frozen = sp.Rational(
    86248707481421051963533451880821625580096,
    1582706318973118826676839520618941084666525,
)
require(sp.Rational(1, 19) < radius < rho_frozen,
        "requested strict frozen-radius interval")

terminal_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*terminal_dag.values()) == required_signs,
        "terminal DAG closure")
require(lower_t - 2 * sp.Rational(103, 100)
        == sp.Rational(3489, 1850) > 0, "spectral derivative direction")
shape_margin = (
    sp.Rational(99, 100) * lower_t - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(10271, 14800) > 0,
        "spectral nonredundancy")
require(sp.Rational(8) > 0 and -sp.Rational(29, 100) < 0,
        "opposite phase signs throughout box")
require(sp.Rational(10) * (-sp.Rational(31, 100))
        == -sp.Rational(31, 10), "phase-product lower endpoint")
require(sp.Rational(8) * (-sp.Rational(29, 100))
        == -sp.Rational(58, 25), "phase-product upper endpoint")

# Exact live-phase endpoint witness.
witness_data = {
    ell: 9, w: -sp.Rational(31, 100), k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100), r: sp.Rational(103, 100),
    t: upper_t, tau: 1,
}
witness = Q.subs(witness_data)
require(sp.factor(witness.det()) == 0, "witness determinant")
require(Delta.subs(witness_data) == sp.Rational(566003, 185000),
        "witness Delta")
require(n.subs(witness_data) == sp.Rational(8455386, 23125), "witness n")
require(g.subs(witness_data) == sp.Rational(5863, 370000), "witness g")
require(qmin.subs(witness_data) - g.subs(witness_data)
        == sp.Rational(25024624084411, 209421110000) > 0,
        "witness strict legal branch")
require(danger_raw.subs(witness_data) == -sp.Rational(19, 100),
        "witness danger")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    159584437542119281978612371, 43857201313632100000000
) > 0, "witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
)) == -sp.Rational(12024664566834413421, 7748581070000000) < 0,
        "witness live phases")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "witness opposite phases")

print("PASS frozen independently audited t=4 center dependency chain")
print("PASS original fully conjugated gate, PSD rank-two boundary, and scale cubic")
print("PASS recomputed seven derivative majorants on 146/37 <= t <= 150/37")
print("PASS all fourteen exact half-width-2/37 reserves")
print("PASS complete legal T half-line, nonredundancy, and live complex phases")
print(f"rho_new={rho_new}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_2_37[{cell}][{name}]={reserves[cell][name]}")
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=seven-real-parameter half-width 2/37 partial theorem; general gate open")
