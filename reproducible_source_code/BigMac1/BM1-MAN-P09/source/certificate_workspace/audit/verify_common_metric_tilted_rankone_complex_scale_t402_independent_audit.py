#!/usr/bin/env python3
"""Independent exact audit of the active-block t radius 1/402 theorem.

This file does not import the t402 source verifier or any discovery module.
It rebuilds the Hermitian matrix, every entry of Q^2, the fully conjugated
original gate, the rank-two PSD boundary, the legal scale half-line, and the
scale cubic from definitions.  The already-audited t=4 centre certificates
are replayed sequentially; their seven relevant exact minima are then joined
to independently recomputed six-variable derivative majorants.

The cubic discriminant is intentionally absent from the terminal proof DAG.
Its previously audited negative m-M/402 lower bound is checked only as a
certificate-method diagnostic.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables audit checks")

from hashlib import sha256
from functools import lru_cache
import gc
from math import prod
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"audit failure: {label}")


# Bind the exact statement under review, its untrusted source verifier/package,
# the two original reductions, and the independently audited centre artifacts.
DEPENDENCIES = {
    "tmp/research/common_metric_tilted_rankone_complex_scale_t402_enlargement.md":
        "1f3a41767f8a668d51d22edf4edbd0bf9daf4b87356179859aea1e1b93818a82",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t402_enlargement.py":
        "c7bdce41a0a55dc31c3ad14a113a8dffd14d4a323c264a875c1238ae3412b473",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t402_enlargement_manifest.sha256":
        "57685250b623139e1b19361121b47c5b0a2f0215fa795ab681d52519b7966b2d",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
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
    "tmp/research/common_metric_tilted_rankone_complex_scale_t403_enlargement.md":
        "206551077ae5999cf454620aabdbbed62d648bdf84e8907a716aa7e4c19f1f6c",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t403_enlargement_manifest.sha256":
        "6910eb450987ecee2216041a126c9fb352fd65f8d2d9cc85bfb16e06e612ae3f",
    "audit/verify_common_metric_tilted_rankone_complex_scale_t403_enlargement_referee.py":
        "b439d7ff59698c7eb3f5f470d322378a8497ea64cc813efb5b6484a171193575",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_T403_ENLARGEMENT_REFEREE_AUDIT.md":
        "43a0f4d2eac5272fabece7af78749f4806d211c85a37cb18d9ff0c9295d43f95",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}

if os.environ.get("T402_AUDIT_TEST_BAD_DEPENDENCY") == "1":
    first = next(iter(DEPENDENCIES))
    DEPENDENCIES[first] = "0" * 64

for relative, expected_hash in DEPENDENCIES.items():
    dependency = ROOT / relative
    require(dependency.is_file(), f"missing dependency {relative}")
    actual_hash = sha256(dependency.read_bytes()).hexdigest()
    require(actual_hash == expected_hash, f"dependency hash mismatch {relative}")


def modulus_squared(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a, c):
    """Definition-level fully conjugated scalar gate."""
    p = sp.Matrix([a, 0, c])
    image = matrix * p
    square = matrix * matrix
    return sp.expand(
        a**2 * modulus_squared(image[1])
        + sp.Rational(1, 4) * modulus_squared(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * modulus_squared(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0])**2
    )


ell, w, k, z, r, t, tau, T, qfree = sp.symbols(
    "ell w k z r t tau T qfree", real=True
)
shape_variables = (ell, w, k, z, r, t)
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
require(a > 0 and c > 0 and a**2 + c**2 == 1, "p normalization")

Delta = sp.factor(r * t - z**2 - w**2)
n = sp.factor(t * (k**2 + ell**2) + r - 2 * (k * z + ell * w))
g = sp.factor(a * c * ell - z * k - w * ell - t)
qmin = tau**2 * n / Delta

Q = sp.Matrix([
    [r, tau * (k + sp.I * ell), z + sp.I * w],
    [tau * (k - sp.I * ell), qmin, tau],
    [z - sp.I * w, tau, t],
])
require(Q == sp.conjugate(Q.T), "fully conjugated Hermitian matrix")

# Independently spell out all nine entries of Q^2 and compare them with
# matrix multiplication.  This catches a lost conjugate or cyclic phase.
explicit_Q2 = sp.Matrix([
    [
        r**2 + tau**2 * (k**2 + ell**2) + z**2 + w**2,
        tau * ((r + qmin) * (k + sp.I * ell) + z + sp.I * w),
        (r + t) * (z + sp.I * w) + tau**2 * (k + sp.I * ell),
    ],
    [
        tau * ((r + qmin) * (k - sp.I * ell) + z - sp.I * w),
        tau**2 * (k**2 + ell**2 + 1) + qmin**2,
        tau * ((k - sp.I * ell) * (z + sp.I * w) + qmin + t),
    ],
    [
        (r + t) * (z - sp.I * w) + tau**2 * (k - sp.I * ell),
        tau * ((z - sp.I * w) * (k + sp.I * ell) + qmin + t),
        z**2 + w**2 + tau**2 + t**2,
    ],
])
for row in range(3):
    for column in range(3):
        require(sp.factor((Q * Q)[row, column] - explicit_Q2[row, column]) == 0,
                f"Q^2 entry ({row + 1},{column + 1})")
require(explicit_Q2 == sp.conjugate(explicit_Q2.T), "Q^2 Hermitian symmetry")

# PSD rank-two branch from the active block and an exact zero Schur complement.
active = Q.extract([0, 2], [0, 2])
coupling = Q.extract([0, 2], [1])
require(sp.factor(active.det() - Delta) == 0, "active determinant")
schur_value = (sp.conjugate(coupling).T * active.inv() * coupling)[0]
require(sp.factor(schur_value - qmin) == 0, "zero Schur complement")
require(sp.factor(Q.det()) == 0, "rank-two determinant")

p = sp.Matrix([a, 0, c])
danger = sp.factor(sp.re((Q * p)[0]))
require(sp.factor(danger - (a * r + c * z)) == 0, "danger scalar")

free_Q = Q.copy()
free_Q[1, 1] = qfree
free_image = free_Q * p
last_residual = sp.expand(
    c * sp.conjugate(free_image[1]) - sp.I * (free_Q * free_Q)[2, 1]
)
require(sp.factor(sp.im(last_residual) + tau * (qfree - g)) == 0,
        "unconstrained scalar centre q_g")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line identity")

# First cubic derivation: start with the original gate and replace tau^(2j)
# by T^j only after proving that every odd tau coefficient vanishes.
raw_in_tau = sp.Poly(
    sp.expand(4 * Delta**2 * original_gate(Q, a, c)), tau
)
require(all(monomial[0] % 2 == 0 for monomial, _ in raw_in_tau.terms()),
        "odd coupling power in original gate")
scale_polynomial = sp.Poly(sum(
    coefficient * T**(monomial[0] // 2)
    for monomial, coefficient in raw_in_tau.terms()
), T)
require(scale_polynomial.degree() == 3, "scale cubic degree")
P = scale_polynomial.as_expr()
C0 = sp.factor(scale_polynomial.coeff_monomial(1))
C1 = sp.factor(scale_polynomial.coeff_monomial(T))
C2 = sp.factor(scale_polynomial.coeff_monomial(T**2))
require(sp.factor(scale_polynomial.coeff_monomial(T**3) - n**2) == 0,
        "positive leading cubic coefficient")

# Second derivation: expand the two complex residuals into real squares.
x = a * r + c * z
L = a * k + c
A = a * c * (r + t) + z - w * (r + t)
B = a * c - w - z * (r + t)
C = c * L + z * ell - w * k
residual_square_cubic = sp.expand(
    Delta**2 * (
        (A - T * ell)**2 + (B - T * k)**2 - 32 * a**2 * x**2
        + T * (4 * a**2 * (L**2 + a**2 * ell**2) + C**2)
    )
    + T * (T * n - Delta * g)**2
)
require(sp.factor(P - residual_square_cubic) == 0,
        "phase-retaining residual-square cubic")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "C2 formula")

# Positive-g endpoint normalizations and strict curvature.
TL = sp.factor(Delta * g / n)
N0, endpoint_denominator = sp.cancel(P.subs(T, TL)).as_numer_denom()
raw_N1, derivative_denominator = sp.cancel(
    sp.diff(P, T).subs(T, TL)
).as_numer_denom()
N1 = -raw_N1
require(sp.factor(endpoint_denominator - 15625 * n**2) == 0,
        "endpoint denominator")
require(sp.factor(derivative_denominator + 625 * n) == 0,
        "endpoint derivative denominator")
endpoint_curvature = sp.factor(C2 + 3 * n**2 * TL)
require(sp.factor(endpoint_curvature - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature")
require(sp.factor(sp.diff(P, T, 2) - 2 * (C2 + 3 * n**2 * T)) == 0,
        "cubic second derivative")

# Seven and only seven certified sign groups enter legality and the two
# terminal proof branches.  An injected omission must fail closed.
sign_polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
if os.environ.get("T402_AUDIT_TEST_DROP_SIGN") == "1":
    sign_polynomials.pop("N1")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(sign_polynomials) == required_signs, "incomplete sign dependency set")

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
    degrees = tuple(
        sp.Poly(expression, *shape_variables, domain=sp.QQ).degree(variable)
        for variable in shape_variables
    )
    require(degrees == expected_degrees[name], f"six-variable degree {name}")


@lru_cache(maxsize=None)
def bernstein_collocation(degree):
    if degree == 0:
        matrix = sp.eye(1)
    else:
        matrix = sp.Matrix([
            [
                sp.binomial(degree, column)
                * sp.Rational(row, degree)**column
                * (1 - sp.Rational(row, degree))**(degree - column)
                for column in range(degree + 1)
            ]
            for row in range(degree + 1)
        ])
    return matrix, matrix.inv()


def apply_axis_transform(coefficients, degrees, axis, transform):
    dimension = len(degrees)
    degree = degrees[axis]
    other_axes = [index for index in range(dimension) if index != axis]
    groups = {
        tuple(index[other] for other in other_axes)
        for index in coefficients
    }
    converted = {}
    for group in groups:
        source_values = []
        for source in range(degree + 1):
            index = [0] * dimension
            index[axis] = source
            for other, exponent in zip(other_axes, group):
                index[other] = exponent
            source_values.append(coefficients.get(tuple(index), 0))
        for target in range(degree + 1):
            index = [0] * dimension
            index[axis] = target
            for other, exponent in zip(other_axes, group):
                index[other] = exponent
            converted[tuple(index)] = sum(
                transform[target, source] * source_values[source]
                for source in range(degree + 1)
            )
    return converted


def nodal_bernstein_statistics(expression, variables, bounds):
    """Recover every control from exact nodes and reconstruct every node."""
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(polynomial.degree(variable) for variable in variables)
    coefficients = dict(polynomial.terms())
    collocations = []

    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        points = [
            left + (right - left) * sp.Rational(index, degree)
            if degree else left
            for index in range(degree + 1)
        ]
        power_to_nodes = sp.Matrix([
            [point**power for power in range(degree + 1)]
            for point in points
        ])
        coefficients = apply_axis_transform(
            coefficients, degrees, axis, power_to_nodes
        )
        collocations.append(bernstein_collocation(degree))
    nodal_values = coefficients

    for axis, (_, inverse) in enumerate(collocations):
        coefficients = apply_axis_transform(
            coefficients, degrees, axis, inverse
        )
    count = len(coefficients)
    minimum = min(coefficients.values())
    positive = all(value > 0 for value in coefficients.values())

    reconstruction = coefficients
    del coefficients
    gc.collect()
    for axis, (collocation, _) in enumerate(collocations):
        reconstruction = apply_axis_transform(
            reconstruction, degrees, axis, collocation
        )
    require(reconstruction == nodal_values, "nodal round-trip reconstruction")
    return degrees, count, minimum, positive

# The exact minima below are not trusted builder output: each was recovered
# from every exact tensor node by the two centre-referee replays above.
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

center_variables = (ell, w, k, z, r)
common_center_bounds = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
    (-sp.Rational(301, 100), -sp.Rational(299, 100)),
    (-sp.Rational(101, 100), -sp.Rational(99, 100)),
)
center_five_degrees = {
    name: degrees[:5] for name, degrees in expected_degrees.items()
}
center_control_counts = {
    "danger": 4,
    "Delta": 18,
    "n": 72,
    "C0": 245,
    "C1": 1764,
    "N0": 30492,
    "N1": 8000,
}
center_statistics_hashes = []
for cell, r_bounds in (
    ("r_low", (sp.Rational(99, 100), sp.Rational(101, 100))),
    ("r_high", (sp.Rational(101, 100), sp.Rational(103, 100))),
):
    bounds = common_center_bounds + (r_bounds,)
    statistics_payload = []
    controls_in_cell = 0
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        degrees, count, minimum, positive = nodal_bernstein_statistics(
            sign_polynomials[name].subs(t, 4), center_variables, bounds
        )
        require(degrees == center_five_degrees[name],
                f"centre degree {cell}/{name}")
        require(count == center_control_counts[name],
                f"centre control count {cell}/{name}")
        require(positive, f"nonpositive centre control {cell}/{name}")
        require(minimum == center_minima[cell][name],
                f"centre minimum {cell}/{name}")
        controls_in_cell += count
        statistics_payload.append(f"{name}:{degrees}:{count}:{minimum}")
    require(controls_in_cell == 40595, f"seven-sign control total {cell}")
    center_statistics_hashes.append(sha256(
        (cell + "|" + "|".join(statistics_payload)).encode()
    ).hexdigest())

# Absolute power majorants for partial_t p on the wider six-dimensional box.
coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), sp.Rational(401, 100),
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
    terms = sp.Poly(
        sp.diff(expression, t), *shape_variables, domain=sp.QQ
    ).terms()
    bound = sum(
        abs(coefficient) * prod(
            cap**power for cap, power in zip(coordinate_caps, powers)
        )
        for powers, coefficient in terms
    )
    return len(terms), sp.factor(bound)


majorants = {}
for name, expression in sign_polynomials.items():
    term_count, majorant = absolute_power_majorant(expression)
    require(term_count == expected_term_counts[name],
            f"partial_t term count {name}")
    require(majorant == expected_majorants[name],
            f"partial_t majorant {name}")
    majorants[name] = majorant

radius = sp.Rational(1, 402)
target_left = 4 - radius
target_right = 4 + radius
require((target_left, target_right) == (
    sp.Rational(1607, 402), sp.Rational(1609, 402)
), "exact t endpoints")
require(sp.Rational(399, 100) <= target_left < target_right
        <= sp.Rational(401, 100), "target interval inside derivative box")
require(radius > sp.Rational(1, 403) > sp.Rational(1, 500),
        "strict interval inclusions")
require(4 - radius < 4 - sp.Rational(1, 403)
        < 4 + sp.Rational(1, 403) < 4 + radius,
        "strict containment of the t403 layer")

reserves = {
    cell: {
        name: sp.factor(minima[name] - radius * majorants[name])
        for name in required_signs
    }
    for cell, minima in center_minima.items()
}
for cell, cell_reserves in reserves.items():
    for name, reserve in cell_reserves.items():
        require(reserve > 0, f"nonpositive reserve {cell}/{name}")

least_reserves = {
    name: min(reserves[cell][name] for cell in reserves)
    for name in required_signs
}
expected_least_reserves = {
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
require(least_reserves == expected_least_reserves, "least-reserve table")

# Terminal proof DAG.  There is no discriminant node or edge.
dependency_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive_coefficients": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
terminal_dependencies = set().union(*dependency_dag.values())
require(terminal_dependencies == required_signs, "terminal DAG sign closure")
require("ND" not in terminal_dependencies, "discriminant leaked into terminal DAG")

# Audit every endpoint/zero case used by that DAG.
require(sp.factor(P.subs(T, 0) - C0) == 0, "T=0 endpoint")
G_aux = sp.symbols("G_aux", real=True)
C2_with_independent_g = Delta**2 * (k**2 + ell**2) - 2 * Delta * G_aux * n
require(sp.factor(C2 - C2_with_independent_g.subs(G_aux, g)) == 0,
        "independent-g C2 identity")
require(sp.factor(C2_with_independent_g.subs(G_aux, 0)
                  - Delta**2 * (k**2 + ell**2)) == 0,
        "g=0 curvature endpoint")
require(sp.factor(sp.diff(P, T).subs(T, TL) - N1 / (625 * n)) == 0,
        "positive-g endpoint derivative sign")
require(sp.factor(P.subs(T, TL) - N0 / (15625 * n**2)) == 0,
        "positive-g endpoint value sign")

# The discarded ND package: recompute its negative lower bound by exact
# arithmetic from the independently audited lower-cell centre minimum and
# exact safe-radius ratio.  This is deliberately not an original gate value.
nd_center_minimum = sp.Rational(
    16659627721252625696244381239255705449827376815068142600603001925331,
    3200000000000000000000000000000000000000000,
)
nd_safe_radius = sp.Rational(
    2445449940734330377430367888331112726580165404046699831281174594544000,
    983572318963523249183141112132550562552170261009318405958248648546787789,
)
nd_majorant = sp.factor(nd_center_minimum / nd_safe_radius)
nd_failed_reserve = sp.factor(nd_center_minimum - radius * nd_majorant)
expected_nd_failed_reserve = -sp.Rational(
    54657263927145682718521091555313864896870775497413042370594307870877001,
    20582400000000000000000000000000000000000000000000,
)
require(nd_failed_reserve == expected_nd_failed_reserve < 0,
        "discarded ND certificate diagnostic")

# t changes a scale-free spectral invariant; it is not the coupling scale T
# or a common active-block rescaling.
wide_left = sp.Rational(399, 100)
require(wide_left - 2 * sp.Rational(103, 100) > 0,
        "monotonicity in r for shape derivative lower bound")
shape_margin = (
    sp.Rational(99, 100) * wide_left
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(461, 625) > 0,
        "scale-free spectral-shape derivative")

# Exact interior simultaneous-phase witness, evaluated from the original gate.
witness_data = {
    ell: sp.Integer(9),
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(2001, 500),
    tau: sp.Integer(1),
}
witness = Q.subs(witness_data)
require(target_left < witness_data[t] < target_right,
        "phase witness outside t402 interval")
require(sp.factor(witness.det()) == 0, "phase witness determinant")
require(Delta.subs(witness_data) > 0 and n.subs(witness_data) > 0,
        "phase witness PSD denominators")
require(qmin.subs(witness_data) > g.subs(witness_data),
        "phase witness outside strict legal branch")
require(danger.subs(witness_data) == -sp.Rational(19, 100),
        "phase witness danger")
witness_gate = sp.factor(original_gate(witness, a, c))
require(witness_gate == sp.Rational(
    414461983319631411704949, 112939929245000000000
) > 0, "phase witness original gate")
real_witness = witness.applyfunc(sp.re)
phase_increment = sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
))
require(phase_increment == -sp.Rational(
    585660171418319979, 375732500000000
) < 0, "phase-integrity increment")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "opposite nonzero phase product")

for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve[{cell}][{name}]={reserves[cell][name]}")
print(f"discarded_ND_lower_cell_reserve={nd_failed_reserve}")
print("PASS dependency hashes and two independent 40595-control seven-sign centre replays")
print("PASS fully conjugated original gate, all Q^2 entries, PSD rank-two boundary")
print("PASS scale cubic, legal half-line, endpoints, zero cases, and terminal DAG")
print("PASS fourteen exact m-M/402 reserves; ND is absent and only method-negative")
print("PASS strict inclusions, nonredundancy, phase integrity, and fail-closed hooks")
print("center_statistics_sha256=" + ",".join(center_statistics_hashes))
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=seven-real-parameter partial theorem; unrestricted complex gate remains open")
