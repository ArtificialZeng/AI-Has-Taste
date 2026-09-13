#!/usr/bin/env python3
"""Independent referee for the seven-sign complex-scale t radius 1/20.

This verifier does not import the source verifier, any discovery program, the
older referee, or cached coefficient tensors.  It starts at the fully
conjugated Hermitian gate and the zero-Schur-complement boundary.  The two
40,595-control center certificates are rebuilt by direct affine power-to-
Bernstein conversion and then inverted exactly back to the source
polynomials.
"""

if not __debug__:
    raise RuntimeError("fail closed: run without python -O")

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
    "tmp/research/common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.md":
        "bfd4ffb334a57a3bd73d6694c4ff267d9c1a5d8a0bb6d1bcb5b18b6fd2794b57",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement.py":
        "06cb6cc79eb21714e43e1cfa7f3707f828552a7682c4da12710a709734b4e10f",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t20_monotonicity_enlargement_manifest.sha256":
        "1d5300088030659404aaccf098f748a33d1a3b44e8c6b37797e4297f1f797966",
    "tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md":
        "b049ead438ebbe295d39d76608afdba9d23cd0e5e1bb61f2a5fc346259387742",
    "tmp/research/common_metric_tilted_rankone_complex_scale_r_adjacent_theorem.md":
        "3e2dcc40cb2997499ac29f735c9956278fa2c40c10bd9068c441ed8c3b5bbe15",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}

if os.environ.get("T20_REFEREE_TEST_BAD_DEPENDENCY") == "1":
    first_dependency = next(iter(DEPENDENCIES))
    DEPENDENCIES[first_dependency] = "0" * 64

for relative_path, expected_hash in DEPENDENCIES.items():
    dependency_path = ROOT / relative_path
    require(dependency_path.is_file(), f"missing dependency {relative_path}")
    actual_hash = sha256(dependency_path.read_bytes()).hexdigest()
    require(actual_hash == expected_hash,
            f"dependency hash mismatch {relative_path}")


def check_source_manifest():
    manifest_path = ROOT / (
        "tmp/research/common_metric_tilted_rankone_complex_scale_t20_"
        "monotonicity_enlargement_manifest.sha256"
    )
    entries = []
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        require("  " in line, "malformed source manifest line")
        digest, relative_path = line.split("  ", 1)
        require(len(digest) == 64, "malformed source manifest digest")
        file_path = ROOT / relative_path
        require(file_path.is_file(), f"source manifest missing {relative_path}")
        require(sha256(file_path.read_bytes()).hexdigest() == digest,
                f"source manifest mismatch {relative_path}")
        entries.append(relative_path)
    require(len(entries) == 10, "source manifest entry count")
    require(len(set(entries)) == len(entries), "duplicate source manifest entry")


check_source_manifest()


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a_value, c_value):
    p_vector = sp.Matrix([a_value, 0, c_value])
    image = matrix * p_vector
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
shape_variables = (ell, w, k, z, r)
all_variables = (ell, w, k, z, r, t)
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

# Rebuild the boundary and the legal scale half-line from the definitions.
require(a > 0 and c > 0 and a**2 + c**2 == 1, "normalized target vector")
require(Q == sp.conjugate(Q.T), "fully conjugated Hermitian matrix")
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
last_leakage = sp.expand(
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q * free_Q)[2, 1]
)
require(sp.factor(sp.im(last_leakage) + tau * (qfree - g)) == 0,
        "free-middle gate center")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# First cubic derivation: extract even coupling powers from the original gate.
raw_tau = sp.Poly(sp.expand(4 * Delta**2 * original_gate(Q, a, c)), tau)
require(all(power[0] % 2 == 0 for power, _ in raw_tau.terms()),
        "unexpected odd coupling power")
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
        "scale cubic leading coefficient")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "quadratic coefficient identity")

# Second cubic derivation: an independent real-residual square decomposition.
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
require(sp.factor(P - square_formula) == 0, "independent square cubic")

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
        "strict-convexity identity")

sign_polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
if os.environ.get("T20_REFEREE_TEST_DROP_SIGN") == "1":
    sign_polynomials.pop("N1")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(sign_polynomials) == required_signs, "seven terminal sign groups")

expected_six_degrees = {
    "danger": (0, 0, 0, 1, 1, 0),
    "Delta": (0, 2, 0, 2, 1, 1),
    "n": (2, 1, 2, 1, 1, 1),
    "C0": (0, 6, 0, 6, 4, 4),
    "C1": (2, 6, 2, 6, 3, 4),
    "N0": (5, 10, 5, 10, 6, 6),
    "N1": (4, 7, 4, 7, 4, 4),
}
for name, expression in sign_polynomials.items():
    polynomial = sp.Poly(expression, *all_variables, domain=sp.QQ)
    degrees = tuple(polynomial.degree(variable) for variable in all_variables)
    require(degrees == expected_six_degrees[name], f"six-axis degree {name}")


def add_to(mapping, index, value):
    if value:
        mapping[index] = mapping.get(index, sp.Integer(0)) + value


def affine_power_to_bernstein(expression, variables, bounds):
    """Return full exact Bernstein tensor and prove invertibility directly."""
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(polynomial.degree(variable) for variable in variables)
    original = dict(polynomial.terms())
    coefficients = dict(original)

    # On each axis substitute x=left+(right-left)u, then use
    # u^j=sum_{i=j}^d binom(i,j)/binom(d,j) B_i^d(u).
    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        width = right - left
        require(width > 0, f"positive Bernstein width axis {axis}")
        affine = {}
        for index, coefficient in coefficients.items():
            power = index[axis]
            for exponent in range(power + 1):
                target = list(index)
                target[axis] = exponent
                add_to(
                    affine,
                    tuple(target),
                    coefficient * sp.binomial(power, exponent)
                    * left**(power - exponent) * width**exponent,
                )
        bernstein = {}
        for index, coefficient in affine.items():
            power = index[axis]
            for control in range(power, degree + 1):
                target = list(index)
                target[axis] = control
                add_to(
                    bernstein,
                    tuple(target),
                    coefficient * sp.binomial(control, power)
                    / sp.binomial(degree, power),
                )
        coefficients = {index: sp.factor(value)
                        for index, value in bernstein.items() if value != 0}

    controls = dict(coefficients)

    # Invert the whole tensor independently.  Expand each Bernstein basis
    # polynomial to powers of u and then u=(x-left)/(right-left).
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
                add_to(
                    unit_power,
                    tuple(target),
                    coefficient * sp.binomial(degree, control)
                    * sp.binomial(degree - control, extra) * (-1)**extra,
                )
        source_power = {}
        for index, coefficient in unit_power.items():
            exponent = index[axis]
            for source_exponent in range(exponent + 1):
                target = list(index)
                target[axis] = source_exponent
                add_to(
                    source_power,
                    tuple(target),
                    coefficient * sp.binomial(exponent, source_exponent)
                    * (-left)**(exponent - source_exponent) / width**exponent,
                )
        reconstruction = {
            index: sp.factor(value)
            for index, value in source_power.items() if value != 0
        }

    require(reconstruction == original, "exact Bernstein inverse reconstruction")
    return degrees, controls


shape_bounds_common = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
    (-sp.Rational(301, 100), -sp.Rational(299, 100)),
    (-sp.Rational(101, 100), -sp.Rational(99, 100)),
)
cell_bounds = {
    "r_low": shape_bounds_common + ((sp.Rational(99, 100),
                                      sp.Rational(101, 100)),),
    "r_high": shape_bounds_common + ((sp.Rational(101, 100),
                                       sp.Rational(103, 100)),),
}
expected_center_degrees = {
    "danger": (0, 0, 0, 1, 1),
    "Delta": (0, 2, 0, 2, 1),
    "n": (2, 1, 2, 1, 1),
    "C0": (0, 6, 0, 6, 4),
    "C1": (2, 6, 2, 6, 3),
    "N0": (5, 10, 5, 10, 6),
    "N1": (4, 7, 4, 7, 4),
}
expected_control_counts = {
    name: prod(degree + 1 for degree in degrees)
    for name, degrees in expected_center_degrees.items()
}
require(sum(expected_control_counts.values()) == 40595,
        "40,595 controls per cell")
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
for cell_name, bounds in cell_bounds.items():
    center_minima[cell_name] = {}
    cell_count = 0
    for sign_name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        center_expression = sp.factor(sign_polynomials[sign_name].subs(t, 4))
        degrees, controls = affine_power_to_bernstein(
            center_expression, shape_variables, bounds
        )
        require(degrees == expected_center_degrees[sign_name],
                f"center degree {cell_name}/{sign_name}")
        require(len(controls) == expected_control_counts[sign_name],
                f"control count {cell_name}/{sign_name}")
        require(all(control > 0 for control in controls.values()),
                f"strict center controls {cell_name}/{sign_name}")
        minimum = min(controls.values())
        require(minimum == expected_center_minima[cell_name][sign_name],
                f"center minimum {cell_name}/{sign_name}")
        center_minima[cell_name][sign_name] = minimum
        cell_count += len(controls)
    require(cell_count == 40595, f"stitched cell count {cell_name}")

# Rebuild all absolute power-monomial derivative majorants on the target box.
coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), sp.Rational(81, 20),
)
expected_term_counts = {
    "danger": 1,
    "Delta": 1,
    "n": 2,
    "C0": 62,
    "C1": 67,
    "N0": 1851,
    "N1": 326,
}
expected_majorants = {
    "danger": sp.Integer(0),
    "Delta": sp.Rational(103, 100),
    "n": sp.Rational(1090601, 10000),
    "C0": sp.Rational(7330309783059851, 6250000000000),
    "C1": sp.Rational(162718802887612103, 25000000000000),
    "N0": sp.Rational(
        102031510952390678261878426882374421,
        12800000000000000000000,
    ),
    "N1": sp.Rational(11554426319351381788185663,
                       6400000000000000),
}


def derivative_majorant(expression):
    terms = sp.Poly(sp.diff(expression, t), *all_variables,
                    domain=sp.QQ).terms()
    majorant = sum(
        abs(coefficient) * prod(
            cap**power for cap, power in zip(coordinate_caps, powers)
        )
        for powers, coefficient in terms
    )
    return len(terms), sp.factor(majorant)


majorants = {}
for sign_name, expression in sign_polynomials.items():
    term_count, majorant = derivative_majorant(expression)
    require(term_count == expected_term_counts[sign_name],
            f"derivative term count {sign_name}")
    require(majorant == expected_majorants[sign_name],
            f"derivative majorant {sign_name}")
    majorants[sign_name] = majorant

finite_ratios = sorted(
    (sp.factor(center_minima[cell][name] / majorants[name]), cell, name)
    for cell in center_minima
    for name in required_signs
    if majorants[name] != 0
)
rho_star, limiting_cell, limiting_name = finite_ratios[0]
expected_rho_star = sp.Rational(
    139329982333373668764509741946217216,
    2550787773809766956546960672059360525,
)
require((limiting_cell, limiting_name) == ("r_low", "N0"),
        "unique lower-r N0 bottleneck")
require(sum(1 for ratio, _, _ in finite_ratios if ratio == rho_star) == 1,
        "unique safe-radius bottleneck")
require(rho_star == expected_rho_star, "exact safe radius")
require(sp.Rational(1, 19) < rho_star < sp.Rational(1, 18),
        "safe-radius reciprocal bracket")


def reserves_at(radius):
    return {
        cell: {
            name: sp.factor(center_minima[cell][name]
                            - radius * majorants[name])
            for name in required_signs
        }
        for cell in center_minima
    }


radius = sp.Rational(1, 20)
reserves = reserves_at(radius)
require(radius < rho_star, "radius below exact bottleneck")
require(all(value > 0 for cell in reserves.values() for value in cell.values()),
        "all fourteen radius-1/20 reserves")
require((4 - radius, 4 + radius) == (
    sp.Rational(79, 20), sp.Rational(81, 20)
), "target derivative interval")
require(radius > sp.Rational(1, 100), "strict old-radius inclusion")

expected_reserves = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(27923, 10000),
        "n": sp.Rational(57179519, 200000),
        "C0": sp.Rational(347212475210945019, 1250000000000000),
        "C1": sp.Rational(1577604698086835071, 2500000000000000),
        "N0": sp.Rational(47162374571541283748646833372996759,
                           1280000000000000000000000),
        "N1": sp.Rational(52570927222411509536270309,
                           640000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(28723, 10000),
        "n": sp.Rational(57183519, 200000),
        "C0": sp.Rational(375197564416222891, 1250000000000000),
        "C1": sp.Rational(1709162849380974671, 2500000000000000),
        "N0": sp.Rational(84078102143731304081678909964839959,
                           1280000000000000000000000),
        "N1": sp.Rational(58621943611198152893726309,
                           640000000000000000),
    },
}
require(reserves == expected_reserves, "fourteen exact reserve table")

# Close exactly the complete legal T half-line.  These terminal groups are
# sufficient: on g<=0 every coefficient is positive; on g>0 the endpoint
# value and slope are positive and the curvature stays positive for T>=TL.
terminal_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*terminal_dag.values()) == required_signs,
        "terminal DAG closure")
require(sp.Rational(99, 100) > 0 and sp.Rational(79, 20) > 0,
        "positive active diagonal")
require(sp.Rational(8) > 0, "nonzero ell for coefficient strictness")
phase_product_bounds = (-sp.Rational(31, 10), -sp.Rational(58, 25))
require(phase_product_bounds[0] <= phase_product_bounds[1] < 0,
        "uniform opposite nonzero phase domain")
phase_box = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
)
phase_degree_low, phase_controls_low = affine_power_to_bernstein(
    ell * w - phase_product_bounds[0], (ell, w), phase_box
)
phase_degree_high, phase_controls_high = affine_power_to_bernstein(
    phase_product_bounds[1] - ell * w, (ell, w), phase_box
)
require(phase_degree_low == phase_degree_high == (1, 1),
        "phase-product tensor degree")
require(all(value > 0 for value in phase_controls_low.values())
        and sp.factor((ell * w - phase_product_bounds[0]).subs({
            ell: 10, w: -sp.Rational(31, 100)
        })) == 0,
        "phase-product lower bound")
require(all(value > 0 for value in phase_controls_high.values())
        and sp.factor((phase_product_bounds[1] - ell * w).subs({
            ell: 8, w: -sp.Rational(29, 100)
        })) == 0,
        "phase-product upper bound")

# Varying t is not coupling rescaling or common active-block rescaling.
# The scale-free active-block invariant (r+t)/sqrt(Delta) has derivative
# numerator rt-r^2-2(z^2+w^2).  Its exact global lower bound is positive.
require(sp.Rational(79, 20) - 2 * sp.Rational(103, 100)
        == sp.Rational(189, 100) > 0,
        "spectral numerator increasing in r")
shape_derivative_lower = (
    sp.Rational(99, 100) * sp.Rational(79, 20)
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_derivative_lower == sp.Rational(349, 500) > 0,
        "nonredundant active spectral shape")

# Exact live-phase witness at the new upper t endpoint.
witness_data = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(81, 20),
    tau: 1,
}
witness = Q.subs(witness_data)
require(sp.factor(witness.det()) == 0, "phase witness determinant")
require(Delta.subs(witness_data) == sp.Rational(30553, 10000),
        "phase witness Delta")
require(n.subs(witness_data) == sp.Rational(73054641, 200000),
        "phase witness n")
require(g.subs(witness_data) == sp.Rational(199, 10000),
        "phase witness g")
require(qmin.subs(witness_data) - g.subs(witness_data)
        == sp.Rational(36521240453, 305530000) > 0,
        "phase witness strict legal half-line")
require(danger.subs(witness_data) == -sp.Rational(19, 100),
        "phase witness strict danger")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    679782423179948045013, 186697161800000000
) > 0, "phase witness original gate")
real_witness = witness.applyfunc(sp.re)
phase_increment = sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
))
require(phase_increment == -sp.Rational(
    948596098430067, 611060000000
) < 0, "phase integrity increment")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "opposite live phases")

code_hash = sha256(Path(__file__).read_bytes()).hexdigest()
print("PASS dependency hashes and source manifest")
print("PASS original fully conjugated gate, Schur boundary, and legal T half-line")
print("PASS independent affine/Bernstein/inverse reconstruction: 40595 controls per cell")
print("PASS seven derivative groups and all fourteen radius-1/20 reserves")
print("PASS unique lower-r N0 bottleneck and 1/19 < rho_star < 1/18")
print("PASS strict old-interval inclusion, spectral nonredundancy, and phase integrity")
print(f"rho_star={rho_star}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_1_20[{cell}][{name}]={reserves[cell][name]}")
print(f"verifier_sha256={code_hash}")
print("scope=seven-real-parameter partial theorem; unrestricted gate remains open")
