#!/usr/bin/env python3
"""Independent exact referee for the complex-scale half-width 2/37.

No source/discovery module or cached tensor is imported.  The checker starts
from the fully conjugated original Hermitian gate, rebuilds both t=4 center
Bernstein tensors with exact inverse reconstruction, recomputes derivative
majorants on 146/37 <= t <= 150/37, and attacks all 96 endpoint/seam cases.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables checks")

from hashlib import sha256
from math import prod
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


DEPENDENCIES = {
    "tmp/research/common_metric_tilted_rankone_complex_scale_t2over37_enlargement.md":
        "cbc3de7f0e9682dce10a4d7b09475d27ec5619c1768515159aa54171e0d9474c",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t2over37_enlargement.py":
        "dc922ca310873a5c52a99175ab776ff98fe9149350ccda1229c1198007f0b23c",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t2over37_enlargement_manifest.sha256":
        "60f6935ff986851a8d8f10f36fc17c2b518b6136d20bad231b30948ccfdcbe83",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}
if os.environ.get("T2OVER37_REFEREE_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64
for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def check_source_manifest():
    path = ROOT / (
        "tmp/research/common_metric_tilted_rankone_complex_scale_t2over37_"
        "enlargement_manifest.sha256"
    )
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        require("  " in line, "malformed source manifest line")
        digest, relative = line.split("  ", 1)
        target = ROOT / relative
        require(len(digest) == 64 and target.is_file(),
                f"bad source manifest entry {relative}")
        require(sha256(target.read_bytes()).hexdigest() == digest,
                f"source manifest mismatch {relative}")
        entries.append(relative)
    require(len(entries) == 10 and len(set(entries)) == 10,
            "source manifest entry set")


check_source_manifest()


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def gate(matrix, a_value, c_value):
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
shape_vars = (ell, w, k, z, r)
all_vars = shape_vars + (t,)
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

danger = sp.factor(sp.re((Q * sp.Matrix([a, 0, c]))[0]))
require(sp.factor(danger - (a * r + c * z)) == 0, "danger scalar")
free_Q = Q.copy()
free_Q[1, 1] = qfree
free_image = free_Q * sp.Matrix([a, 0, c])
leak = sp.expand(
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q * free_Q)[2, 1]
)
require(sp.factor(sp.im(leak) + tau * (qfree - g)) == 0,
        "free-middle center")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# First derivation: exact extraction from the original conjugated gate.
raw_tau = sp.Poly(sp.expand(4 * Delta**2 * gate(Q, a, c)), tau)
require(all(power[0] % 2 == 0 for power, _ in raw_tau.terms()),
        "even coupling powers")
poly = sp.Poly(sum(
    coefficient * T**(power[0] // 2)
    for power, coefficient in raw_tau.terms()
), T)
require(poly.degree() == 3, "scale cubic degree")
P = poly.as_expr()
C0 = sp.factor(poly.coeff_monomial(1))
C1 = sp.factor(poly.coeff_monomial(T))
C2 = sp.factor(poly.coeff_monomial(T**2))
require(sp.factor(poly.coeff_monomial(T**3) - n**2) == 0,
        "leading coefficient")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "C2 identity")

# Second derivation: phase-retaining real residual squares.
x = a * r + c * z
L = a * k + c
A = a * c * (r + t) + z - w * (r + t)
B = a * c - w - z * (r + t)
C = c * L + z * ell - w * k
square_P = sp.expand(
    Delta**2 * (
        (A - T * ell)**2 + (B - T * k)**2 - 32 * a**2 * x**2
        + T * (4 * a**2 * (L**2 + a**2 * ell**2) + C**2)
    )
    + T * (T * n - Delta * g)**2
)
require(sp.factor(P - square_P) == 0, "independent square cubic")

TL = sp.factor(Delta * g / n)
N0, D0 = sp.cancel(P.subs(T, TL)).as_numer_denom()
N1_raw, D1 = sp.cancel(sp.diff(P, T).subs(T, TL)).as_numer_denom()
N1 = -N1_raw
require(sp.factor(D0 - 15625 * n**2) == 0, "endpoint denominator")
require(sp.factor(D1 + 625 * n) == 0, "slope denominator")
require(sp.factor(C2 + 3 * n**2 * TL - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature")
require(sp.factor(sp.diff(P, T, 2) - 2 * (C2 + 3 * n**2 * T)) == 0,
        "convexity identity")

signs = {
    "danger": -danger, "Delta": Delta, "n": n, "C0": C0,
    "C1": C1, "N0": N0, "N1": N1,
}
if os.environ.get("T2OVER37_REFEREE_TEST_DROP_SIGN") == "1":
    signs.pop("N1")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(signs) == required_signs, "seven terminal signs")


def add_to(mapping, index, value):
    if value:
        mapping[index] = mapping.get(index, sp.Integer(0)) + value


def bernstein_with_inverse(expression, variables, bounds):
    """Exact affine power-to-Bernstein tensor plus inverse reconstruction."""
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(polynomial.degree(variable) for variable in variables)
    original = dict(polynomial.terms())
    coefficients = dict(original)
    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        width = right - left
        require(width > 0, f"positive box width axis {axis}")
        affine = {}
        for index, coefficient in coefficients.items():
            power = index[axis]
            for exponent in range(power + 1):
                target = list(index)
                target[axis] = exponent
                add_to(affine, tuple(target), coefficient
                       * sp.binomial(power, exponent)
                       * left**(power - exponent) * width**exponent)
        converted = {}
        for index, coefficient in affine.items():
            power = index[axis]
            for control in range(power, degree + 1):
                target = list(index)
                target[axis] = control
                add_to(converted, tuple(target), coefficient
                       * sp.binomial(control, power)
                       / sp.binomial(degree, power))
        coefficients = {index: sp.factor(value)
                        for index, value in converted.items() if value != 0}
    controls = dict(coefficients)

    reconstruction = dict(controls)
    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        width = right - left
        unit_power = {}
        for index, coefficient in reconstruction.items():
            control = index[axis]
            for extra in range(degree - control + 1):
                exponent = control + extra
                target = list(index)
                target[axis] = exponent
                add_to(unit_power, tuple(target), coefficient
                       * sp.binomial(degree, control)
                       * sp.binomial(degree - control, extra) * (-1)**extra)
        source_power = {}
        for index, coefficient in unit_power.items():
            exponent = index[axis]
            for source_exponent in range(exponent + 1):
                target = list(index)
                target[axis] = source_exponent
                add_to(source_power, tuple(target), coefficient
                       * sp.binomial(exponent, source_exponent)
                       * (-left)**(exponent - source_exponent) / width**exponent)
        reconstruction = {index: sp.factor(value)
                          for index, value in source_power.items() if value != 0}
    require(reconstruction == original, "Bernstein inverse reconstruction")
    return degrees, controls


common_bounds = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
    (-sp.Rational(301, 100), -sp.Rational(299, 100)),
    (-sp.Rational(101, 100), -sp.Rational(99, 100)),
)
cell_bounds = {
    "r_low": common_bounds + ((sp.Rational(99, 100), sp.Rational(101, 100)),),
    "r_high": common_bounds + ((sp.Rational(101, 100), sp.Rational(103, 100)),),
}
expected_center_degrees = {
    "danger": (0, 0, 0, 1, 1), "Delta": (0, 2, 0, 2, 1),
    "n": (2, 1, 2, 1, 1), "C0": (0, 6, 0, 6, 4),
    "C1": (2, 6, 2, 6, 3), "N0": (5, 10, 5, 10, 6),
    "N1": (4, 7, 4, 7, 4),
}
expected_center_minima = {
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

center_minima = {}
for cell, bounds in cell_bounds.items():
    center_minima[cell] = {}
    count = 0
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        degrees, controls = bernstein_with_inverse(
            sp.factor(signs[name].subs(t, 4)), shape_vars, bounds
        )
        require(degrees == expected_center_degrees[name],
                f"center degrees {cell}/{name}")
        expected_count = prod(degree + 1 for degree in degrees)
        require(len(controls) == expected_count,
                f"center control count {cell}/{name}")
        require(all(value > 0 for value in controls.values()),
                f"positive center controls {cell}/{name}")
        minimum = min(controls.values())
        require(minimum == expected_center_minima[cell][name],
                f"center minimum {cell}/{name}")
        center_minima[cell][name] = minimum
        count += len(controls)
    require(count == 40595, f"40595 controls {cell}")

radius = sp.Rational(2, 37)
lower_t, upper_t = 4 - radius, 4 + radius
require((lower_t, upper_t) == (sp.Rational(146, 37), sp.Rational(150, 37)),
        "new t interval")
caps = (
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
    "N0": sp.Rational(1775215308784565826159975640142805255396523,
                      221900662400000000000000000000),
    "N1": sp.Rational(146616757232077940451518475621,
                      81044800000000000000),
}


def derivative_majorant(expression):
    terms = sp.Poly(sp.diff(expression, t), *all_vars, domain=sp.QQ).terms()
    value = sum(abs(coefficient) * prod(
        cap**power for cap, power in zip(caps, powers)
    ) for powers, coefficient in terms)
    return len(terms), sp.factor(value)


majorants = {}
for name, expression in signs.items():
    term_count, value = derivative_majorant(expression)
    require(term_count == expected_term_counts[name],
            f"derivative term count {name}")
    require(value == expected_majorants[name], f"majorant {name}")
    majorants[name] = value

reserves = {
    cell: {name: sp.factor(center_minima[cell][name] - radius * majorants[name])
           for name in required_signs}
    for cell in center_minima
}
require(all(value > 0 for row in reserves.values() for value in row.values()),
        "all fourteen strict reserves")
expected_reserves = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(515803, 185000),
        "n": sp.Rational(2640463, 9250),
        "C0": sp.Rational(639288181047879148809969, 2342701250000000000000),
        "C1": sp.Rational(1415411124077141012291273, 2342701250000000000000),
        "N0": sp.Rational(304944185165887347790739852577939707794093,
                          102629056360000000000000000000000),
        "N1": sp.Rational(699275403702571484222111483263,
                          9370805000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(530603, 185000),
        "n": sp.Rational(1320324, 4625),
        "C0": sp.Rational(691736743817931930675361, 2342701250000000000000),
        "C1": sp.Rational(1538691702270928995729073, 2342701250000000000000),
        "N0": sp.Rational(3264808470772680758250345288696777589889993,
                          102629056360000000000000000000000),
        "N1": sp.Rational(196968419140925613831803445847,
                          2342701250000000000000),
    },
}
require(reserves == expected_reserves, "exact reserve table")

ratios = sorted(
    (sp.factor(center_minima[cell][name] / majorants[name]), cell, name)
    for cell in center_minima for name in required_signs
    if majorants[name] != 0
)
rho_new, limiting_cell, limiting_name = ratios[0]
expected_rho_new = sp.Rational(
    2415423075934055837934601667899895734740928,
    44380382719614145653999391003570131384913075,
)
require((limiting_cell, limiting_name) == ("r_low", "N0"),
        "new-box bottleneck")
require(sum(1 for value, _, _ in ratios if value == rho_new) == 1,
        "unique bottleneck")
require(rho_new == expected_rho_new and radius < rho_new < sp.Rational(1, 18),
        "new-box safe ratio")
rho_frozen = sp.Rational(
    86248707481421051963533451880821625580096,
    1582706318973118826676839520618941084666525,
)
require(sp.Rational(1, 19) < radius < rho_frozen,
        "strict requested enlargement")

terminal_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*terminal_dag.values()) == required_signs,
        "terminal DAG closure")
require(sp.Rational(99, 100) > 0 and lower_t > 0, "active diagonal signs")

# Prove the nonzero opposite-phase interval by a small exact tensor.
phase_bounds = (-sp.Rational(31, 10), -sp.Rational(58, 25))
phase_box = common_bounds[:2]
_, phase_low = bernstein_with_inverse(
    ell * w - phase_bounds[0], (ell, w), phase_box
)
_, phase_high = bernstein_with_inverse(
    phase_bounds[1] - ell * w, (ell, w), phase_box
)
require(all(value >= 0 for value in phase_low.values())
        and all(value >= 0 for value in phase_high.values())
        and phase_bounds[1] < 0, "uniform live opposite phases")
require(lower_t - 2 * sp.Rational(103, 100)
        == sp.Rational(3489, 1850) > 0, "shape derivative direction")
shape_margin = (
    sp.Rational(99, 100) * lower_t - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(10271, 14800) > 0,
        "spectral nonredundancy")

# Exact falsification attack at endpoints and the stitched r seam.
corner_axes = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
    (-sp.Rational(301, 100), -sp.Rational(299, 100)),
    (-sp.Rational(101, 100), -sp.Rational(99, 100)),
    (sp.Rational(99, 100), sp.Rational(101, 100), sp.Rational(103, 100)),
    (lower_t, upper_t),
)
corner_count = positive_g = nonpositive_g = 0
corner_gates = []
for ell_v in corner_axes[0]:
    for w_v in corner_axes[1]:
        for k_v in corner_axes[2]:
            for z_v in corner_axes[3]:
                for r_v in corner_axes[4]:
                    for t_v in corner_axes[5]:
                        data = {ell: ell_v, w: w_v, k: k_v,
                                z: z_v, r: r_v, t: t_v}
                        corner_count += 1
                        delta_v = sp.factor(Delta.subs(data))
                        n_v = sp.factor(n.subs(data))
                        g_v = sp.factor(g.subs(data))
                        require(delta_v > 0 and n_v > 0 and (-danger).subs(data) > 0,
                                "corner legality")
                        if g_v > 0:
                            positive_g += 1
                            tl_v = sp.factor(TL.subs(data))
                            require(tl_v > 0, "corner positive TL")
                            require(sp.factor(P.subs(data).subs(T, tl_v)) > 0,
                                    "corner endpoint gate")
                            require(sp.factor(sp.diff(P, T).subs(data).subs(T, tl_v)) > 0,
                                    "corner endpoint slope")
                        else:
                            nonpositive_g += 1
                            require(sp.factor(P.subs(data).subs(T, 0)) > 0,
                                    "corner zero endpoint")
                        require(sp.factor(n_v - delta_v * g_v) > 0,
                                "corner T=1 legality")
                        matrix = Q.subs(data).subs(tau, 1)
                        direct = sp.factor(gate(matrix, a, c))
                        require(direct > 0, "corner direct gate")
                        require(sp.factor(4 * delta_v**2 * direct
                                          - P.subs(data).subs(T, 1)) == 0,
                                "corner direct/cubic agreement")
                        corner_gates.append(direct)
require(corner_count == 96 and positive_g + nonpositive_g == 96,
        "96-case branch partition")
minimum_corner_gate = min(corner_gates)

# A strictly legal new-endpoint witness prevents phase erasure.
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
        "witness strict legality")
witness_gate = sp.factor(gate(witness, a, c))
require(witness_gate == sp.Rational(
    159584437542119281978612371, 43857201313632100000000
) > 0, "witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (witness_gate - gate(real_witness, a, c)))
        == -sp.Rational(12024664566834413421, 7748581070000000) < 0,
        "live-phase decrement")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "opposite witness phases")

print("PASS original conjugated gate, Schur boundary, and complete T half-line")
print("PASS independent Bernstein/inverse reconstruction: 40595 controls per cell")
print("PASS recomputed wider-box derivative majorants and fourteen strict reserves")
print("PASS exact q comparison, unique low-cell N0 bottleneck, and seam coverage")
print(f"PASS exact 96-corner falsification attack: g>0 {positive_g}, g<=0 {nonpositive_g}")
print(f"minimum_corner_gate_T1={minimum_corner_gate}")
print(f"rho_new={rho_new}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_2_37[{cell}][{name}]={reserves[cell][name]}")
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=seven-real-parameter radius-2/37 partial theorem; general gate open")
