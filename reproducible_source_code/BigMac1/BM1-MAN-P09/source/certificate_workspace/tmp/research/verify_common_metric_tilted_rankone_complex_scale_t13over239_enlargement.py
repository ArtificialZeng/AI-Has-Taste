#!/usr/bin/env python3
"""Fail-closed exact verifier for the complex-scale half-width 13/239.

The audited t=4 center tensors supply exact minima.  This program does not
import an earlier verifier: it starts from the fully conjugated Hermitian
gate, reconstructs the rank-two Schur boundary and scale cubic, recomputes
all seven t-derivative majorants on 943/239 <= t <= 969/239, and checks the
fourteen new reserves.  No floating-point sign decision is made.
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
    "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_enlargement.md":
        "07475f67b6da62a7bde400a14c98317ddf4084a04a2f6c6a7f387fe73aa9e9d8",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t5over92_enlargement.py":
        "d357bbfaac1fd054c4bab671e488243f75bfc709acff2dde29e42c7e827043a7",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_enlargement_manifest.sha256":
        "a7725313d7dcda11207a625aab405f45ef967fea0a4b5bff0d559e6abd0df0cc",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T5OVER92_REFEREE_AUDIT.md":
        "2b71220d5a76f0824dbe2f3662dca284f9d101de16aa439c8ced791818d3a79e",
    "audit/verify_common_metric_tilted_rankone_complex_scale_t5over92_referee.py":
        "0df222da6d9b4a1f4bb58f2a7d1e842219ee3952dce022ce984cded57f9b3f7d",
    "audit/common_metric_tilted_rankone_complex_scale_t5over92_referee_manifest.sha256":
        "0583c61ae2fda9ae6ffcbeb0aef0f9e7d03542c7ac10a9d4cf2a55d464122f33",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}
if os.environ.get("T13OVER239_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64
for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def check_manifest(relative, expected_count):
    entries = []
    for line in (ROOT / relative).read_text(encoding="utf-8").splitlines():
        require("  " in line, f"malformed manifest line in {relative}")
        digest, target_relative = line.split("  ", 1)
        target = ROOT / target_relative
        require(len(digest) == 64 and target.is_file(),
                f"bad manifest entry {target_relative}")
        require(sha256(target.read_bytes()).hexdigest() == digest,
                f"manifest mismatch {target_relative}")
        entries.append(target_relative)
    require(len(entries) == expected_count and len(set(entries)) == expected_count,
            f"manifest entry set {relative}")


check_manifest(
    "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_"
    "enlargement_manifest.sha256", 10,
)
check_manifest(
    "audit/common_metric_tilted_rankone_complex_scale_t5over92_"
    "referee_manifest.sha256", 9,
)


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a_value, c_value):
    p = sp.Matrix([a_value, 0, c_value])
    image = matrix * p
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
a, c = sp.Rational(3, 5), sp.Rational(4, 5)
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

# First derivation: the fully conjugated original gate.
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

# Second derivation: a phase-retaining real residual-square expansion.
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
if os.environ.get("T13OVER239_TEST_DROP_SIGN") == "1":
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
    require(tuple(polynomial.degree(variable) for variable in variables)
            == expected_degrees[name], f"degree tuple {name}")

# Exact minima of the independently reconstructed t=4 tensors.
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

radius = sp.Rational(13, 239)
lower_t, upper_t = 4 - radius, 4 + radius
require((lower_t, upper_t) == (sp.Rational(943, 239), sp.Rational(969, 239)),
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
    "C0": sp.Rational(200590784794108703944733,
                      170648987500000000000),
    "C1": sp.Rational(1112340324693882698223071,
                      170648987500000000000),
    "N0": sp.Rational(
        19969311603488806236900116135180695471665523961,
        2495396048636800000000000000000000,
    ),
    "N1": sp.Rational(39522698574394712386666252421283,
                      21843070400000000000000),
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
        "Delta": sp.Rational(3331391, 1195000),
        "n": sp.Rational(682150121, 2390000),
        "C0": sp.Rational(1111293825162673563270681189,
                          4078510801250000000000000),
        "C1": sp.Rational(2454969488685104615121787013,
                          4078510801250000000000000),
        "N0": sp.Rational(
            1876344627798693774222427164702679015573805219,
            14909991390604880000000000000000000000,
        ),
        "N1": sp.Rational(9656890825168841739440201204364899,
                          130512345640000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(3426991, 1195000),
        "n": sp.Rational(682197921, 2390000),
        "C0": sp.Rational(1202603816040810026838373141,
                          4078510801250000000000000),
        "C1": sp.Rational(2669594025103356624891928813,
                          4078510801250000000000000),
        "N0": sp.Rational(
            431886641720977124948675156912551974889731707419,
            14909991390604880000000000000000000000,
        ),
        "N1": sp.Rational(10890847610179196455195994240445899,
                          130512345640000000000000000),
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
rho_wide, bottleneck_cell, bottleneck_name = finite_ratios[0]
expected_rho_wide = sp.Rational(
    27162772450885609710321172264010161955258866496,
    499232790087220155922502903379517386791638099025,
)
rho_five_over_92 = sp.Rational(
    896775556481533279336770926007341554681088,
    16481441167216725968620003969664490147404575,
)
require((bottleneck_cell, bottleneck_name) == ("r_low", "N0"),
        "wide-box bottleneck")
require(rho_wide == expected_rho_wide and radius < rho_wide < rho_five_over_92,
        "fresh wide-box safe ratio")
require(sp.Rational(5, 92) < radius < rho_five_over_92,
        "requested strict enlargement")

terminal_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*terminal_dag.values()) == required_signs,
        "terminal DAG closure")

require(lower_t - 2 * sp.Rational(103, 100)
        == sp.Rational(22533, 11950) > 0, "spectral derivative direction")
shape_margin = (
    sp.Rational(99, 100) * lower_t - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(66313, 95600) > 0,
        "spectral nonredundancy")
require(sp.Integer(10) * (-sp.Rational(31, 100))
        == -sp.Rational(31, 10), "phase-product lower endpoint")
require(sp.Integer(8) * (-sp.Rational(29, 100))
        == -sp.Rational(58, 25) < 0, "phase-product upper endpoint")

# Exact live-phase witness at the new upper t endpoint.
witness_data = {
    ell: 9, w: -sp.Rational(31, 100), k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100), r: sp.Rational(103, 100),
    t: upper_t, tau: 1,
}
witness = Q.subs(witness_data)
require(sp.factor(witness.det()) == 0, "witness determinant")
require(Delta.subs(witness_data) == sp.Rational(3656491, 1195000),
        "witness Delta")
require(n.subs(witness_data) == sp.Rational(873948591, 2390000),
        "witness n")
require(g.subs(witness_data) == sp.Rational(37061, 2390000), "witness g")
require(qmin.subs(witness_data) - g.subs(witness_data)
        == sp.Rational(1044233053032049, 8739013490000) > 0,
        "witness strict legal branch")
require(danger_raw.subs(witness_data) == -sp.Rational(19, 100),
        "witness danger")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    277875866038408051450137129651,
    76370356778401980100000000,
) > 0, "witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
)) == -sp.Rational(3241147859544180523713,
                   2088624224110000000) < 0,
        "witness live phases")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "witness opposite phases")

print("PASS audited t=4 center dependency chain")
print("PASS original conjugated gate, rank-two Schur boundary, and scale cubic")
print("PASS recomputed seven derivative majorants on 943/239 <= t <= 969/239")
print("PASS all fourteen exact half-width-13/239 reserves")
print("PASS complete legal T half-line, nonredundancy, and live complex phases")
print(f"rho_wide={rho_wide}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_13_239[{cell}][{name}]={reserves[cell][name]}")
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=seven-real-parameter half-width 13/239 partial theorem; general gate open")
