#!/usr/bin/env python3
"""Independent exact referee for the enlarged active-block t layer.

The verifier does not import the builder or discovery code.  It reconstructs
the fully conjugated Hermitian gate, the rank-two Schur boundary, the legal
scale half-line, the cubic and its discriminant from definitions.  The two
five-axis centre certificates are replayed by their immutable independent
nodal referee, and every t-derivative majorant/reserve is then recomputed here
from exact power coefficients.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables checks")

from hashlib import sha256
from math import prod
from pathlib import Path
import os
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


DEPENDENCIES = {
    "tmp/research/common_metric_tilted_rankone_complex_scale_t403_enlargement.md":
        "206551077ae5999cf454620aabdbbed62d648bdf84e8907a716aa7e4c19f1f6c",
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
}

if os.environ.get("T403_REFEREE_TEST_BAD_DEPENDENCY") == "1":
    first_dependency = next(iter(DEPENDENCIES))
    DEPENDENCIES[first_dependency] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def replay_center_certificate(adjacent):
    referee = ROOT / (
        "audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py"
    )
    command = [sys.executable, str(referee)]
    if adjacent:
        command.append("--adjacent-r")
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=environment,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    require(completed.returncode == 0,
            f"independent center replay failed: {completed.stdout}")
    require(
        "PASS independent nodal reconstruction of 734288 Bernstein controls"
        in completed.stdout,
        "center replay did not certify all controls",
    )
    expected_bounds = (
        "r_bounds= (101/100, 103/100)" if adjacent
        else "r_bounds= (99/100, 101/100)"
    )
    require(expected_bounds in completed.stdout, "wrong center cell replayed")
    return sha256(completed.stdout.encode()).hexdigest()


# These are not builder tables: both immutable independent nodal certificates
# are actually replayed before their exact minima are used in the t bridge.
center_output_hashes = (
    replay_center_certificate(False),
    replay_center_certificate(True),
)


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def raw_gate(matrix, a, c):
    p = sp.Matrix([a, 0, c])
    image = matrix * p
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
matrix = sp.Matrix([
    [r, tau * (k + sp.I * ell), z + sp.I * w],
    [tau * (k - sp.I * ell), qmin, tau],
    [z - sp.I * w, tau, t],
])

# Definition-level Hermitian, Schur-boundary, rank and danger reconstruction.
require(matrix == sp.conjugate(matrix.T), "matrix is not Hermitian")
active = matrix.extract([0, 2], [0, 2])
coupling = matrix.extract([0, 2], [1])
require(sp.factor(active.det() - Delta) == 0, "active determinant")
require(sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0, "Schur boundary")
require(sp.factor(matrix.det()) == 0, "rank-two determinant")
danger = sp.factor(sp.re((matrix * sp.Matrix([a, 0, c]))[0]))
require(sp.factor(danger - (a * r + c * z)) == 0, "danger scalar")

free_matrix = matrix.copy()
free_matrix[1, 1] = qfree
free_image = free_matrix * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1])
    - sp.I * (free_matrix**2)[2, 1]
)
require(sp.factor(sp.im(last_leak) + tau * (qfree - g)) == 0,
        "gate center q_g")
require(sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0,
        "legal half-line residual")

# Extract the scale cubic directly from the original fully conjugated gate.
raw_tau = sp.Poly(sp.expand(4 * Delta**2 * raw_gate(matrix, a, c)), tau)
require(all(power[0] % 2 == 0 for power, _ in raw_tau.terms()),
        "odd coupling powers in raw gate")
scale_poly = sp.Poly(sum(
    coefficient * T**(power[0] // 2)
    for power, coefficient in raw_tau.terms()
), T)
require(scale_poly.degree() == 3, "scale polynomial degree")
P = scale_poly.as_expr()
C0 = sp.factor(scale_poly.coeff_monomial(1))
C1 = sp.factor(scale_poly.coeff_monomial(T))
C2 = sp.factor(scale_poly.coeff_monomial(T**2))
require(sp.factor(scale_poly.coeff_monomial(T**3) - n**2) == 0,
        "leading cubic coefficient")
require(sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0, "quadratic coefficient")

# A second residual/square derivation checks that no complex phase vanished.
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
require(sp.factor(P - square_formula) == 0, "independent cubic formula")

TL = sp.factor(Delta * g / n)
N0, D0 = sp.cancel(P.subs(T, TL)).as_numer_denom()
N1_raw, D1 = sp.cancel(sp.diff(P, T).subs(T, TL)).as_numer_denom()
N1 = -N1_raw
require(sp.factor(D0 - 15625 * n**2) == 0, "endpoint denominator")
require(sp.factor(D1 + 625 * n) == 0, "derivative denominator")
require(sp.factor(C2 + 3 * n**2 * TL - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0, "endpoint curvature")

# Recompute the discriminant from the universal cubic formula, not a table.
bb, d2, d1, d0, X = sp.symbols("bb d2 d1 d0 X", real=True)
generic = bb * X**3 + d2 * X**2 + d1 * X + d0
generic_disc = (
    18 * bb * d2 * d1 * d0 - 4 * d2**3 * d0 + d2**2 * d1**2
    - 4 * bb * d1**3 - 27 * bb**2 * d0**2
)
require(sp.factor(sp.discriminant(generic, X) - generic_disc) == 0,
        "universal cubic discriminant")
pn = sp.Poly(n, *variables, domain=sp.QQ)
p0 = sp.Poly(C0, *variables, domain=sp.QQ)
p1 = sp.Poly(C1, *variables, domain=sp.QQ)
p2 = sp.Poly(C2, *variables, domain=sp.QQ)
minus_disc = -(
    18 * pn**2 * p2 * p1 * p0 - 4 * p2**3 * p0
    + p2**2 * p1**2 - 4 * pn**2 * p1**3 - 27 * pn**4 * p0**2
)
disc_den, disc_integer = minus_disc.clear_denoms(convert=True)
require(disc_den == 244140625, "discriminant normalization")
ND = disc_integer.as_expr()

sign_polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
    "ND": ND,
}

claimed_degrees = {
    "danger": (0, 0, 0, 1, 1, 0),
    "Delta": (0, 2, 0, 2, 1, 1),
    "n": (2, 1, 2, 1, 1, 1),
    "C0": (0, 6, 0, 6, 4, 4),
    "C1": (2, 6, 2, 6, 3, 4),
    "N0": (5, 10, 5, 10, 6, 6),
    "N1": (4, 7, 4, 7, 4, 4),
    "ND": (10, 20, 10, 20, 12, 13),
}
for name, expression in sign_polynomials.items():
    poly = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(poly.degree(variable) for variable in variables)
    require(degrees == claimed_degrees[name], f"degree tuple {name}")
require(prod(value + 1 for value in claimed_degrees["ND"]) == 9711702,
        "direct ND tensor size")
require(sum(prod(value + 1 for value in degrees)
            for degrees in claimed_degrees.values()) == 9975375,
        "direct six-axis tensor size")

# Exact minima independently reconstructed by the two nodal replays above.
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
        "ND": sp.Rational(
            16659627721252625696244381239255705449827376815068142600603001925331,
            3200000000000000000000000000000000000000000,
        ),
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
        "ND": sp.Rational(
            18942501765434648654554516142706963646914690725542726020966050250291,
            3200000000000000000000000000000000000000000,
        ),
    },
}

coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100),
    sp.Rational(401, 100),
)
claimed_term_counts = {
    "danger": 1, "Delta": 1, "n": 2, "C0": 62,
    "C1": 67, "N0": 1851, "N1": 326, "ND": 84595,
}


def absolute_power_majorant(expression):
    terms = sp.Poly(sp.diff(expression, t), *variables, domain=sp.QQ).terms()
    bound = sp.S.Zero
    for powers, coefficient in terms:
        bound += abs(coefficient) * prod(
            cap**power for cap, power in zip(coordinate_caps, powers)
        )
    return len(terms), sp.factor(bound)


majorants = {}
for name, expression in sign_polynomials.items():
    term_count, majorant = absolute_power_majorant(expression)
    require(term_count == claimed_term_counts[name],
            f"derivative term count {name}")
    majorants[name] = majorant

radius = sp.Rational(1, 403)
wide_left, wide_right = sp.Rational(399, 100), sp.Rational(401, 100)
target_left, target_right = 4 - radius, 4 + radius
require((target_left, target_right) == (
    sp.Rational(1611, 403), sp.Rational(1613, 403)
), "new t endpoints")
require(wide_left <= target_left < target_right <= wide_right,
        "target not inside derivative box")
require(radius > sp.Rational(1, 500), "old interval not strictly contained")

reserves = {}
for cell, minima in center_minima.items():
    reserves[cell] = {}
    for name in sign_polynomials:
        reserve = sp.factor(minima[name] - radius * majorants[name])
        require(reserve > 0, f"nonpositive t reserve {cell}/{name}")
        reserves[cell][name] = reserve

minimum_reserves = {
    name: min(reserves[cell][name] for cell in reserves)
    for name in sign_polynomials
}
claimed_minimum_reserves = {
    "danger": sp.Rational(87, 500),
    "Delta": sp.Rational(5725107, 2015000),
    "n": sp.Rational(1173052317, 4030000),
    "C0": sp.Rational(168031168212372292987, 503750000000000000),
    "C1": sp.Rational(473798761153505578829, 503750000000000000),
    "N0": sp.Rational(
        53688775478983631337804470500482797123,
        128960000000000000000000000,
    ),
    "N1": sp.Rational(10834008694368493232491091993,
                      64480000000000000000),
    "ND": sp.Rational(
        211896779612896328421389008272777422300367253543677239239053722934418999,
        20633600000000000000000000000000000000000000000000,
    ),
}
require(minimum_reserves == claimed_minimum_reserves,
        "displayed minimum reserve table")

# Reconstruct the exact all-sixteen-ratio ceiling.  Zero derivative groups
# have infinite radius and are not candidates for the finite minimum.
finite_ratios = []
for cell, minima in center_minima.items():
    for name, minimum in minima.items():
        if majorants[name] != 0:
            finite_ratios.append((sp.factor(minimum / majorants[name]),
                                  cell, name))
finite_ratios.sort(key=lambda item: item[0])
rho_star, limiting_cell, limiting_name = finite_ratios[0]
require((limiting_cell, limiting_name) == ("r_low", "ND"),
        "wrong method bottleneck")
require(sum(1 for value, _, _ in finite_ratios if value == rho_star) == 1,
        "method bottleneck is not unique")
claimed_rho_star = sp.Rational(
    2445449940734330377430367888331112726580165404046699831281174594544000,
    983572318963523249183141112132550562552170261009318405958248648546787789,
)
require(rho_star == claimed_rho_star, "rho_star value")
require(sp.Rational(1, 403) < rho_star < sp.Rational(1, 402),
        "rho_star reciprocal bracket")

failed_radius = sp.Rational(1, 402)
failed_nd_reserve = sp.factor(
    center_minima["r_low"]["ND"] - failed_radius * majorants["ND"]
)
claimed_failed_nd_reserve = -sp.Rational(
    54657263927145682718521091555313864896870775497413042370594307870877001,
    20582400000000000000000000000000000000000000000000,
)
require(failed_nd_reserve == claimed_failed_nd_reserve < 0,
        "1/402 ND certificate failure")
for cell, minima in center_minima.items():
    for name, minimum in minima.items():
        if (cell, name) != ("r_low", "ND"):
            require(minimum - failed_radius * majorants[name] > 0,
                    f"unexpected second 1/402 failure {cell}/{name}")

# The varying t coordinate is not a hidden copy of coupling scale or common
# active-block rescaling: this exact lower bound makes a scale-free spectral
# shape invariant strictly increase with t throughout the wider box.
require(wide_left - 2 * sp.Rational(103, 100) > 0,
        "spectral-shape numerator is not increasing in r")
shape_derivative_numerator = (
    sp.Rational(99, 100) * wide_left
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_derivative_numerator == sp.Rational(461, 625) > 0,
        "nonredundant spectral-shape coordinate")

# Exact interior phase witness, evaluated again with the original gate.
witness_data = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(2001, 500),
    tau: 1,
}
witness = matrix.subs(witness_data)
require(target_left < witness_data[t] < target_right,
        "phase witness not interior to new t interval")
require(sp.factor(witness.det()) == 0, "phase witness determinant")
require(Delta.subs(witness_data) == sp.Rational(150293, 50000),
        "phase witness Delta")
require(n.subs(witness_data) == sp.Rational(1804751601, 5000000),
        "phase witness n")
require(g.subs(witness_data) == sp.Rational(679, 10000),
        "phase witness g")
require(witness[1, 1] == sp.Rational(1804751601, 15029300),
        "phase witness qmin")
require(qmin.subs(witness_data) > g.subs(witness_data),
        "phase witness not on legal strict half-line")
require(danger.subs(witness_data) == -sp.Rational(19, 100),
        "phase witness danger")
witness_gate = sp.factor(raw_gate(witness, a, c))
require(witness_gate == sp.Rational(
    414461983319631411704949, 112939929245000000000
) > 0, "phase witness gate")
real_witness = witness.applyfunc(sp.re)
phase_increment = sp.factor(4 * (
    witness_gate - raw_gate(real_witness, a, c)
))
require(phase_increment == -sp.Rational(
    585660171418319979, 375732500000000
) < 0, "phase integrity increment")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "phase product")

code_hash = sha256(Path(__file__).read_bytes()).hexdigest()
print("PASS dependency hashes and both independent 734288-control center replays")
print("PASS original fully conjugated Hermitian gate, rank-two boundary, and legal half-line")
print("PASS all eight exact t-derivative sign groups on both stitched r cells")
print("PASS strict old-interval inclusion, nonredundancy, and phase integrity")
print("PASS unique eight-sign method ceiling 1/403 < rho_star < 1/402")
print("PASS 1/402 negative ND reserve classified only as a certificate failure")
print("center_output_sha256=", ",".join(center_output_hashes))
print("verifier_sha256=", code_hash)
print("scope=seven-real-parameter partial theorem; unrestricted gate remains open")
