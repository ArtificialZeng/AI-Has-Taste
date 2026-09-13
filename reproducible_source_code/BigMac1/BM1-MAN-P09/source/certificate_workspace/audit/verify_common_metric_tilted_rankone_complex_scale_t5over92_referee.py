#!/usr/bin/env python3
"""Independent exact referee for the complex-scale half-width 5/92.

No source or discovery module is imported.  The referee reconstructs the
fully conjugated original Hermitian gate, recomputes the two t=4 center
Bernstein tensors by exact nodal inversion (and reverses that transform),
recomputes all wider-box derivative majorants, and attacks 96 exact corners.
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
    "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_enlargement.md":
        "07475f67b6da62a7bde400a14c98317ddf4084a04a2f6c6a7f387fe73aa9e9d8",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_t5over92_enlargement.py":
        "d357bbfaac1fd054c4bab671e488243f75bfc709acff2dde29e42c7e827043a7",
    "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_enlargement_manifest.sha256":
        "a7725313d7dcda11207a625aab405f45ef967fea0a4b5bff0d559e6abd0df0cc",
    "tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md":
        "8d96bf8c42b306dbede2fb38197f8216f6f0d7399692bafb39f4eeebc31da5bd",
    "tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md":
        "d2e661e3a7a55fe888651631c14265dbad3743653b69b6e63cd67fc3de4bd89c",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}
if os.environ.get("T5OVER92_REFEREE_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64
for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def check_source_manifest():
    relative = (
        "tmp/research/common_metric_tilted_rankone_complex_scale_t5over92_"
        "enlargement_manifest.sha256"
    )
    entries = []
    for line in (ROOT / relative).read_text(encoding="utf-8").splitlines():
        require("  " in line, "malformed source manifest line")
        digest, target_relative = line.split("  ", 1)
        target = ROOT / target_relative
        require(len(digest) == 64 and target.is_file(),
                f"bad source manifest entry {target_relative}")
        require(sha256(target.read_bytes()).hexdigest() == digest,
                f"source manifest mismatch {target_relative}")
        entries.append(target_relative)
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

# Definition-level cubic extraction.
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

# A separate phase-retaining residual-square derivation.
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
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
}
if os.environ.get("T5OVER92_REFEREE_TEST_DROP_SIGN") == "1":
    signs.pop("N1")
required_signs = {"danger", "Delta", "n", "C0", "C1", "N0", "N1"}
require(set(signs) == required_signs, "seven terminal signs")


def transform_axis(coefficients, axis, matrix):
    """Apply one exact one-dimensional transform to a sparse tensor."""
    size = matrix.rows
    require(matrix.cols == size, f"square transform axis {axis}")
    groups = {}
    for index, coefficient in coefficients.items():
        rest = index[:axis] + index[axis + 1:]
        vector = groups.setdefault(rest, [sp.Integer(0)] * size)
        vector[index[axis]] += coefficient
    result = {}
    for rest, vector in groups.items():
        transformed = matrix * sp.Matrix(vector)
        for output_index, coefficient in enumerate(transformed):
            if coefficient:
                index = rest[:axis] + (output_index,) + rest[axis:]
                result[index] = sp.factor(coefficient)
    return result


def nodal_bernstein_with_inverse(expression, variables, bounds):
    """Exact nodal inversion to Bernstein controls, then inverse replay."""
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(polynomial.degree(variable) for variable in variables)
    original = {index: coefficient for index, coefficient in polynomial.terms()}
    transforms = []
    for degree, (left, right) in zip(degrees, bounds):
        require(right > left, "positive box width")
        if degree == 0:
            transforms.append(sp.eye(1))
            continue
        nodes = [sp.Rational(j, degree) for j in range(degree + 1)]
        value_matrix = sp.Matrix([
            [(left + (right - left) * node)**power
             for power in range(degree + 1)]
            for node in nodes
        ])
        bernstein_matrix = sp.Matrix([
            [sp.binomial(degree, control) * node**control
             * (1 - node)**(degree - control)
             for control in range(degree + 1)]
            for node in nodes
        ])
        require(bernstein_matrix.det() != 0, "invertible nodal matrix")
        transforms.append(bernstein_matrix.inv() * value_matrix)

    controls = dict(original)
    for axis, matrix in enumerate(transforms):
        controls = transform_axis(controls, axis, matrix)

    reconstruction = dict(controls)
    for axis in reversed(range(len(transforms))):
        reconstruction = transform_axis(
            reconstruction, axis, transforms[axis].inv()
        )
    require(reconstruction == original, "nodal Bernstein inverse reconstruction")
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
    "danger": (0, 0, 0, 1, 1),
    "Delta": (0, 2, 0, 2, 1),
    "n": (2, 1, 2, 1, 1),
    "C0": (0, 6, 0, 6, 4),
    "C1": (2, 6, 2, 6, 3),
    "N0": (5, 10, 5, 10, 6),
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
        degrees, controls = nodal_bernstein_with_inverse(
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

radius = sp.Rational(5, 92)
lower_t, upper_t = 4 - radius, 4 + radius
require((lower_t, upper_t) == (sp.Rational(363, 92), sp.Rational(373, 92)),
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
    "C0": sp.Rational(178768417937073716969, 152087500000000000),
    "C1": sp.Rational(1982672114117030883131, 304175000000000000),
    "N0": sp.Rational(659257646688669038744800158786579605896183,
                      82385190400000000000000000000),
    "N1": sp.Rational(140892023457352044459673332201,
                      77868800000000000000),
}


def derivative_majorant(expression):
    terms = sp.Poly(sp.diff(expression, t), *all_vars, domain=sp.QQ).terms()
    value = sum(
        abs(coefficient) * prod(
            cap**power for cap, power in zip(caps, powers)
        )
        for powers, coefficient in terms
    )
    return len(terms), sp.factor(value)


majorants = {}
for name, expression in signs.items():
    term_count, value = derivative_majorant(expression)
    require(term_count == expected_term_counts[name],
            f"derivative term count {name}")
    require(value == expected_majorants[name], f"majorant {name}")
    majorants[name] = value

expected_reserves = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(641199, 230000),
        "n": sp.Rational(262589547, 920000),
        "C0": sp.Rational(23832861558346092019441, 87450312500000000000),
        "C1": sp.Rational(421321424647050445290451, 699602500000000000000),
        "N0": sp.Rational(96145360217431855882905344352972293637221,
                          189485937920000000000000000000000),
        "N1": sp.Rational(13267008990845903837618573613659,
                          179098240000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(659599, 230000),
        "n": sp.Rational(262607947, 920000),
        "C0": sp.Rational(25790705395419633264029, 87450312500000000000),
        "C1": sp.Rational(458136789263353765094051, 699602500000000000000),
        "N0": sp.Rational(5560997909448393192811384868142570554242021,
                          189485937920000000000000000000000),
        "N1": sp.Rational(14960331468100346901412418109659,
                          179098240000000000000000),
    },
}
reserves = {
    cell: {
        name: sp.factor(center_minima[cell][name] - radius * majorants[name])
        for name in required_signs
    }
    for cell in center_minima
}
require(reserves == expected_reserves, "exact reserve table")
require(all(value > 0 for row in reserves.values() for value in row.values()),
        "all fourteen strict reserves")

ratios = sorted(
    (sp.factor(center_minima[cell][name] / majorants[name]), cell, name)
    for cell in center_minima for name in required_signs
    if majorants[name] != 0
)
rho_wide, limiting_cell, limiting_name = ratios[0]
expected_rho_wide = sp.Rational(
    896775556481533279336770926007341554681088,
    16481441167216725968620003969664490147404575,
)
rho_two_over_37 = sp.Rational(
    2415423075934055837934601667899895734740928,
    44380382719614145653999391003570131384913075,
)
require((limiting_cell, limiting_name) == ("r_low", "N0"),
        "wide-box bottleneck")
require(sum(1 for value, _, _ in ratios if value == rho_wide) == 1,
        "unique bottleneck")
require(rho_wide == expected_rho_wide and radius < rho_wide < rho_two_over_37,
        "fresh wide-box safe ratio")

terminal_dag = {
    "legality": {"danger", "Delta", "n"},
    "g_nonpositive": {"Delta", "n", "C0", "C1"},
    "g_positive_endpoint": {"Delta", "n", "N0", "N1"},
    "g_positive_curvature": {"Delta", "n"},
}
require(set().union(*terminal_dag.values()) == required_signs,
        "terminal DAG closure")
require(lower_t - 2 * sp.Rational(103, 100)
        == sp.Rational(4337, 2300) > 0, "shape derivative direction")
shape_margin = (
    sp.Rational(99, 100) * lower_t - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
require(shape_margin == sp.Rational(3191, 4600) > 0,
        "spectral nonredundancy")
require(sp.Integer(10) * (-sp.Rational(31, 100))
        == -sp.Rational(31, 10), "phase product lower")
require(sp.Integer(8) * (-sp.Rational(29, 100))
        == -sp.Rational(58, 25) < 0, "phase product upper")

# Exact endpoint/seam falsification attack.
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
                        require(delta_v > 0 and n_v > 0
                                and (-danger).subs(data) > 0,
                                "corner legality")
                        if g_v > 0:
                            positive_g += 1
                            tl_v = sp.factor(TL.subs(data))
                            require(tl_v > 0, "corner positive TL")
                            require(sp.factor(P.subs(data).subs(T, tl_v)) > 0,
                                    "corner endpoint gate")
                            require(sp.factor(
                                sp.diff(P, T).subs(data).subs(T, tl_v)
                            ) > 0, "corner endpoint slope")
                        else:
                            nonpositive_g += 1
                            require(sp.factor(P.subs(data).subs(T, 0)) > 0,
                                    "corner zero endpoint")
                        require(sp.factor(n_v - delta_v * g_v) > 0,
                                "corner T=1 legality")
                        matrix = Q.subs(data).subs(tau, 1)
                        direct = sp.factor(gate(matrix, a, c))
                        require(direct > 0, "corner direct gate")
                        require(sp.factor(
                            4 * delta_v**2 * direct - P.subs(data).subs(T, 1)
                        ) == 0, "corner direct/cubic agreement")
                        corner_gates.append(direct)
require(corner_count == 96 and positive_g + nonpositive_g == 96,
        "96-case branch partition")
minimum_corner_gate = min(corner_gates)

# Strict live-phase witness at the new endpoint.
witness_data = {
    ell: 9, w: -sp.Rational(31, 100), k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100), r: sp.Rational(103, 100),
    t: upper_t, tau: 1,
}
witness = Q.subs(witness_data)
require(sp.factor(witness.det()) == 0, "witness determinant")
require(Delta.subs(witness_data) == sp.Rational(703749, 230000),
        "witness Delta")
require(n.subs(witness_data) == sp.Rational(336411589, 920000),
        "witness n")
require(g.subs(witness_data) == sp.Rational(3577, 230000), "witness g")
require(qmin.subs(witness_data) - g.subs(witness_data)
        == sp.Rational(1137714650431, 9521310000) > 0,
        "witness strict legality")
witness_gate = sp.factor(gate(witness, a, c))
require(witness_gate == sp.Rational(
    659709262001662465543697, 181310688232200000000
) > 0, "witness gate")
real_witness = witness.applyfunc(sp.re)
require(sp.factor(4 * (witness_gate - gate(real_witness, a, c)))
        == -sp.Rational(226554899274721441, 145993420000000) < 0,
        "live-phase decrement")
require(sp.im(witness[0, 1]) * sp.im(witness[0, 2])
        == -sp.Rational(279, 100), "opposite witness phases")

print("PASS original conjugated gate, Schur boundary, and complete T half-line")
print("PASS independent nodal Bernstein/inverse reconstruction: 40595 controls per cell")
print("PASS recomputed 5/92-box derivative majorants and fourteen strict reserves")
print("PASS exact q comparison, unique low-cell N0 bottleneck, and seam coverage")
print(f"PASS exact 96-corner attack: g>0 {positive_g}, g<=0 {nonpositive_g}")
print(f"minimum_corner_gate_T1={minimum_corner_gate}")
print(f"rho_wide={rho_wide}")
for cell in ("r_low", "r_high"):
    for name in ("danger", "Delta", "n", "C0", "C1", "N0", "N1"):
        print(f"reserve_5_92[{cell}][{name}]={reserves[cell][name]}")
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=seven-real-parameter radius-5/92 partial theorem; general gate open")
