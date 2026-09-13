#!/usr/bin/env python3
"""Independent fail-closed referee for the high-Z complex-phase tube.

This program imports neither the source verifier nor the discovery program
and reads no cached polynomial or Bernstein table.  It starts with signed z,
builds the Hermitian compression as two Gram atoms, forms Q and Q^2 directly,
and recovers every Bernstein tensor by exact rational collocation inversion.
"""

if not __debug__:
    raise RuntimeError("fail closed: independent referee cannot run with -O")

from hashlib import sha256
from itertools import product
from math import comb
import os
from pathlib import Path
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: independent referee accepts no arguments")

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = {
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_theorem.md":
        "057fea74222974dbde883868c5f99a3b415d30b1b5994475a2cf334c806b4bff",
    "tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_theorem.py":
        "4b5aa909e84d449f5b05813c4e15266eec4742ca366cbbde3de6ca17dbae9202",
}
if os.environ.get("AXIS_CAP_PHASE_TUBE_REFEREE_BAD_DEPENDENCY") == "1":
    first = next(iter(DEPENDENCIES))
    DEPENDENCIES[first] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"independent verification failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def exact_zero(expression, label):
    """Reject any nonzero exact scalar or matrix residue."""
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                exact_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    residue = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    require(residue == 0, f"{label}: {residue}")


def reduce_unit_circle(expression, q, h):
    """Take the polynomial remainder modulo q^2+h^2-1."""
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(
            lambda entry: reduce_unit_circle(entry, q, h)
        )
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    relation = sp.Poly(q**2 + h**2 - 1, q)
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.factor(remainder / denominator)


def replace_even_power(expression, old, new, label):
    """Replace old^(2k) by new^k and reject every odd power."""
    polynomial = sp.Poly(sp.expand(expression), old)
    result = sp.S.Zero
    for (degree,), coefficient in polynomial.terms():
        require(degree % 2 == 0, f"{label}: odd {old} power {degree}")
        result += coefficient * new ** (degree // 2)
    return sp.expand(result)


def bernstein_basis(degree, index, value):
    return sp.Rational(comb(degree, index)) * value**index \
        * (1 - value) ** (degree - index)


def interior_nodes(degree):
    """A rational grid different from the source and prior endpoint grid."""
    if degree == 0:
        return [sp.Rational(1, 3)]
    return [sp.Rational(2 * index + 1, 2 * degree + 2)
            for index in range(degree + 1)]


def bernstein_controls_by_collocation(polynomial, variables, degrees):
    """Recover tensor controls via independent exact nodal inversion.

    We sample on interior rational nodes and invert the Bernstein collocation
    matrix one axis at a time.  No monomial/binomial conversion is used.
    """
    require(len(variables) == len(degrees), "collocation arity")
    poly = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    natural = tuple(poly.degree(variable) for variable in variables)
    require(all(actual <= declared
                for actual, declared in zip(natural, degrees)),
            f"declared degrees too small: {natural} versus {degrees}")

    ranges = [range(degree + 1) for degree in degrees]
    nodes = [interior_nodes(degree) for degree in degrees]
    data = {}
    for grid_index in product(*ranges):
        substitution = {
            variable: nodes[axis][grid_index[axis]]
            for axis, variable in enumerate(variables)
        }
        data[grid_index] = sp.factor(poly.as_expr().subs(substitution))

    for axis, degree in enumerate(degrees):
        matrix = sp.Matrix([
            [bernstein_basis(degree, control, node)
             for control in range(degree + 1)]
            for node in nodes[axis]
        ])
        require(matrix.det() != 0, f"singular collocation axis {axis}")
        inverse = matrix.inv()
        other_axes = [entry for entry in range(len(variables))
                      if entry != axis]
        other_ranges = [ranges[entry] for entry in other_axes]
        transformed = dict(data)
        for fixed in product(*other_ranges):
            def index_with(axis_index):
                index = [0] * len(variables)
                index[axis] = axis_index
                for other_axis, fixed_value in zip(other_axes, fixed):
                    index[other_axis] = fixed_value
                return tuple(index)

            values = sp.Matrix([
                data[index_with(sample)] for sample in range(degree + 1)
            ])
            controls = inverse * values
            for control, value in enumerate(controls):
                transformed[index_with(control)] = sp.factor(value)
        data = transformed
    return natural, data


def strict_controls(polynomial, variables, degrees, count, minimum, label):
    natural, controls = bernstein_controls_by_collocation(
        polynomial, variables, degrees
    )
    require(natural == degrees, f"{label} natural degrees {natural}")
    require(len(controls) == count, f"{label} control count")
    require(all(value > 0 for value in controls.values()),
            f"{label} strict control positivity")
    actual_minimum = min(controls.items(), key=lambda item: item[1])
    require(actual_minimum == minimum,
            f"{label} minimum {actual_minimum}")
    return controls


R, I = sp.Rational, sp.I
h, q, lam, signed_z = sp.symbols("h q lambda signed_z", real=True)
S, Z, x, y = sp.symbols("S Z x y", real=True)
u, v, tau = sp.symbols("u v tau", real=True)

# The original frame and signed Cholesky atoms.
a = 1 / sp.sqrt(6)
c = sp.sqrt(R(5, 6))
zeta = R(4, 5) + I * R(3, 5)
p = sp.Matrix([a, 0, c])
rvec = sp.Matrix([-a, 0, c * zeta])
fvec = sp.Matrix([-c * h, q, -a * h * zeta])
frame = sp.Matrix.hstack(rvec, fvec)
exact_zero(reduce_unit_circle(frame.conjugate().T * frame - sp.eye(2), q, h),
           "frame isometry")

j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
ell = sp.sqrt(5) * signed_z / 3
atom_one = sp.expand(h * rvec + (j - I * kappa) * fvec)
atom_two = sp.expand(ell * fvec)
H = sp.expand(atom_one * atom_one.conjugate().T
              + atom_two * atom_two.conjugate().T)
exact_zero(reduce_unit_circle(H - H.conjugate().T, q, h), "H Hermitian")
exact_zero(reduce_unit_circle(H - H.subs(signed_z, -signed_z), q, h),
           "both signed-z Gram matrices coincide")

compression = sp.Matrix([
    [h**2, h * (j + I * kappa)],
    [h * (j - I * kappa), j**2 + kappa**2 + ell**2],
])
exact_zero(compression - compression.conjugate().T,
           "compression Hermitian")
exact_zero(compression.det() - R(5, 9) * h**2 * signed_z**2,
           "signed-z compression determinant")
exact_zero(reduce_unit_circle(H - frame * compression * frame.conjugate().T,
                              q, h),
           "Gram atoms equal compressed-frame construction")

# Rebuild the fully conjugated gate from Q and every entry of Q^2.
Q = sp.expand(lam * H)
exact_zero(reduce_unit_circle(Q - Q.conjugate().T, q, h), "Q Hermitian")
image = sp.expand(Q * p)
Q2 = sp.expand(Q * Q)
exact_zero(reduce_unit_circle(Q2 - Q2.conjugate().T, q, h), "Q^2 Hermitian")
exact_zero(reduce_unit_circle(Q2 - lam**2 * H * H, q, h),
           "all Q^2 entries reconstructed")

gate_coordinate_1 = 2 * a * image[1]
gate_coordinate_2 = (
    c * sp.conjugate(image[0]) + a * image[2]
    + I * (a * c - Q2[2, 0])
)
gate_coordinate_3 = c * sp.conjugate(image[1]) - I * Q2[2, 1]
raw_unreduced = sp.expand_complex(
    gate_coordinate_1 * sp.conjugate(gate_coordinate_1)
    + gate_coordinate_2 * sp.conjugate(gate_coordinate_2)
    + gate_coordinate_3 * sp.conjugate(gate_coordinate_3)
    - 32 * a**2 * sp.re(image[0])**2
)
raw_gate = reduce_unit_circle(raw_unreduced, q, h)

danger_claim = R(5, 36) * sp.sqrt(6) * lam * h**2 \
    * (x**2 + y**2 + signed_z**2 - 1)
exact_zero(reduce_unit_circle(sp.re(image[0]) - danger_claim, q, h),
           "signed-z danger identity")

# Eliminate signed z only after the raw Hermitian calculation, then set S=h^2.
gate36_Z_h = replace_even_power(36 * raw_gate, signed_z, Z,
                                "signed-z elimination")
gate36 = replace_even_power(gate36_Z_h, h, S, "h-to-S elimination")
require(not gate36.has(h, q, signed_z), "frame variables survived")
raw_quartic = sp.Poly(gate36, lam)
require(raw_quartic.degree() == 4, "raw positive-scale degree four")
require(raw_quartic.nth(0) == 5, "raw constant coefficient five")
coefficients_Z = [sp.factor(raw_quartic.nth(power))
                  for power in range(5)]

for power in range(1, 5):
    quotient, remainder = sp.div(
        sp.Poly(coefficients_Z[power], S, Z, x, y),
        sp.Poly(S, S, Z, x, y),
    )
    require(remainder.is_zero, f"C{power} exact S factor")
    require(quotient.domain == sp.QQ, f"C{power}/S rational")

# Deliberately delete one actual pre-tube C4 monomial under attack.
deleted_term = -R(25, 81) * S**4 * x**4
deleted_coefficient = sp.Poly(coefficients_Z[4], S, Z, x, y).coeff_monomial(
    S**4 * x**4
)
require(deleted_coefficient == -R(25, 81),
        f"bound C4 deletion monomial: {deleted_coefficient}")
if os.environ.get("AXIS_CAP_PHASE_TUBE_REFEREE_DROP_TERM") == "1":
    coefficients_Z[4] = sp.expand(coefficients_Z[4] - deleted_term)

exact_zero(
    sum(coefficients_Z[power] * lam**power for power in range(5)) - gate36,
    "raw coefficient reconstruction",
)

# Tube coordinates.  The variable order below is intentionally different
# from the source verifier: (v,u,S), then (tau,v,u,S).
tube_map = {
    x: u / 8,
    y: (2 * v - 1) / 64,
    Z: (63 - u**2) / 64,
}
reserve = sp.factor(1 - tube_map[x]**2 - tube_map[y]**2 - tube_map[Z])
exact_zero(reserve - (R(1, 64) - tube_map[y]**2),
           "tube danger reserve")
exact_zero(reserve - R(63, 4096) - v * (1 - v) / 1024,
           "uniform tube reserve decomposition")
require(reserve.subs(v, 0) == R(63, 4096), "y=-1/64 reserve")
require(reserve.subs(v, 1) == R(63, 4096), "y=+1/64 reserve")
require(tube_map[Z].subs(u, 0) == R(63, 64), "Z upper endpoint")
require(tube_map[Z].subs(u, 1) == R(31, 32), "Z lower endpoint")
exact_zero(tube_map[Z] - R(31, 32) - (1 - u**2) / 64,
           "Z lower-bound decomposition")
exact_zero(R(63, 64) - tube_map[Z] - u**2 / 64,
           "Z upper-bound decomposition")

coefficients = [sp.expand(coefficient.subs(tube_map))
                for coefficient in coefficients_Z]
gate36_tube = sp.expand(sum(coefficients[power] * lam**power
                            for power in range(5)))
exact_zero(gate36_tube - gate36.subs(tube_map), "tube-map reconstruction")

# A different exact nonzero-phase calibration, evaluated with both signs of z.
calibration_plus = {
    h: R(5, 13), q: R(12, 13), lam: R(11, 7),
    x: R(3, 32), y: -R(1, 192), signed_z: sp.sqrt(999) / 32,
}
calibration_minus = dict(calibration_plus)
calibration_minus[signed_z] = -sp.sqrt(999) / 32
calibration_reduced = {
    S: R(25, 169), u: R(3, 4), v: R(1, 3), lam: R(11, 7),
}
raw_plus = sp.factor(36 * raw_unreduced.subs(calibration_plus))
raw_minus = sp.factor(36 * raw_unreduced.subs(calibration_minus))
exact_zero(raw_plus - raw_minus, "both z signs at independent calibration")
exact_zero(raw_plus - gate36_tube.subs(calibration_reduced),
           "independent raw/reduced calibration")

INDEPENDENT_EXPECTED = R(
    507808337442291510363664286054448005,
    23731153358933650583505546925572096,
)
require(raw_plus == INDEPENDENT_EXPECTED, "independent calibration value")

expected_coefficient_data = {
    1: ((2, 1, 0), 6, ((2, 1, 0), R(33605, 6144))),
    2: ((4, 2, 1), 30,
        ((4, 2, 0), R(15241448155, 1358954496))),
    3: ((6, 3, 2), 84,
        ((6, 3, 0), R(49463834927165, 8349416423424))),
    4: ((8, 4, 3), 180,
        ((8, 4, 0), R(1152452992382662513, 307792887033102336))),
}
coefficient_control_count = 0
for power, (degrees, count, minimum) in expected_coefficient_data.items():
    quotient, remainder = sp.div(
        sp.Poly(coefficients[power], v, u, S),
        sp.Poly(S, v, u, S),
    )
    require(remainder.is_zero, f"tube C{power} exact S factor")
    controls = strict_controls(
        quotient.as_expr(), (v, u, S), degrees, count, minimum,
        f"tube C{power}/S",
    )
    coefficient_control_count += len(controls)
require(coefficient_control_count == 300, "300 coefficient controls")

# Lossless finite-positive-scale compactification tau=lambda/(1+lambda).
compactified = sp.expand(sum(
    coefficients[power] * tau**power * (1 - tau)**(4 - power)
    for power in range(5)
))
full_natural, full_controls = bernstein_controls_by_collocation(
    compactified, (tau, v, u, S), (4, 8, 4, 4)
)
require(full_natural == (4, 8, 4, 4),
        f"full natural degrees {full_natural}")
require(len(full_controls) == 1125, "1125 compactified controls")
require(all(value >= 0 for value in full_controls.values()),
        "compactified control nonnegativity")
expected_zeros = {
    (tau_index, v_index, u_index, 0)
    for tau_index in range(1, 5)
    for v_index in range(9)
    for u_index in range(5)
}
actual_zeros = {index for index, value in full_controls.items() if value == 0}
require(actual_zeros == expected_zeros,
        "exactly 180 and only S=0 closure zeros")
positive_full = [(index, value) for index, value in full_controls.items()
                 if value > 0]
require(len(positive_full) == 945, "945 positive compactified controls")
require(min(positive_full, key=lambda item: item[1])
        == ((1, 8, 4, 1), R(33605, 98304)),
        "least positive compactified control")

# Projective endpoints.
tau_zero_natural, tau_zero_controls = bernstein_controls_by_collocation(
    compactified.subs(tau, 0), (v, u, S), (0, 0, 0)
)
require(tau_zero_natural == (0, 0, 0), "tau=0 natural degree")
require(tau_zero_controls == {(0, 0, 0): R(5)}, "tau=0 face")

tau_one_quotient, tau_one_remainder = sp.div(
    sp.Poly(compactified.subs(tau, 1), v, u, S),
    sp.Poly(S, v, u, S),
)
require(tau_one_remainder.is_zero, "tau=1 exact S factor")
strict_controls(
    tau_one_quotient.as_expr(), (v, u, S), (8, 4, 3), 180,
    ((8, 4, 0), R(1152452992382662513, 307792887033102336)),
    "tau=1 face / S",
)

# x and y endpoint faces, with closure zeros classified exactly.
face_data = (
    ("x=0", u, 0, (tau, v, S), (4, 8, 4), 225, 36,
     ((3, 8, 1), R(51090800938045, 133590662774784))),
    ("x=1/8", u, 1, (tau, v, S), (4, 8, 4), 225, 36,
     ((1, 8, 1), R(33605, 98304))),
    ("y=-1/64", v, 0, (tau, u, S), (4, 4, 4), 125, 20,
     ((1, 4, 1), R(37445, 98304))),
    ("y=+1/64", v, 1, (tau, u, S), (4, 4, 4), 125, 20,
     ((1, 4, 1), R(33605, 98304))),
)
for label, variable, endpoint, variables, degrees, count, zero_count, minimum in face_data:
    natural, controls = bernstein_controls_by_collocation(
        compactified.subs(variable, endpoint), variables, degrees
    )
    require(natural == degrees, f"{label} natural degrees {natural}")
    require(len(controls) == count, f"{label} control count")
    require(all(value >= 0 for value in controls.values()),
            f"{label} nonnegative controls")
    zeros = {index for index, value in controls.items() if value == 0}
    require(len(zeros) == zero_count, f"{label} closure zero count")
    require(all(index[-1] == 0 and index[0] >= 1 for index in zeros),
            f"{label} zeros only at S=0 with positive tau index")
    positives = [(index, value) for index, value in controls.items()
                 if value > 0]
    require(min(positives, key=lambda item: item[1]) == minimum,
            f"{label} least positive control")

print(f"PASS independent nonzero-y signed-z calibration {raw_plus}")
print("PASS signed-z two-atom Gram chart, Hermitian Q,Q^2, det C=(5/9)SZ")
print("PASS reserve >=63/4096 and 31/32<=Z<=63/64")
print("PASS 300/300 coefficient controls strictly positive")
print("PASS 1125 tau controls: 945 positive and exactly 180 S=0 zeros")
print("PASS tau=0, tau=1, x=0, x=1/8, y=-1/64, y=+1/64 faces")
print("VERDICT exact independently audited partial theorem")
print("SCOPE phase tube only; caps/full ball/common metric/fixed lens remain open")
