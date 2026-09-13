#!/usr/bin/env python3
"""Exact discovery/falsification for the proposed inward-Z tilted sheet.

This is deliberately not a theorem verifier.  It rebuilds the normalized
Hermitian frame, Q, Q^2, and the literal fully conjugated raw gate from the
compact-ball definitions.  It then proves elementary legality bounds and
attacks the candidate at the requested 72 rational parameter nodes.  No
precomputed quartic or certificate table is imported.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from itertools import product
from pathlib import Path
import platform

import sympy as sp


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"discovery check failed: {label}")


def exact_zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                exact_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    require(value == 0, f"{label}: {value}")


def reduce_q(expression, q, relation):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: reduce_q(entry, q, relation))
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.factor(remainder / denominator)


def even_h_to_S(expression, h, S):
    result = 0
    for (degree,), coefficient in sp.Poly(sp.expand(expression), h).terms():
        require(degree % 2 == 0, f"odd h power {degree}")
        result += coefficient * S ** (degree // 2)
    return sp.expand(result)


def sparse_add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def sparse_multiply(left, right):
    result = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            result[key] = result.get(key, 0) + left_value * right_value
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def sparse_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = sparse_multiply(result, base)
    return result


def centered_lower(expression, variables, radii):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    zero = (0,) * len(variables)
    center = polynomial.coeff_monomial(zero)
    variation = sum(
        abs(coefficient) * sp.prod(
            radius**degree for radius, degree in zip(radii, powers)
        )
        for powers, coefficient in polynomial.terms()
        if powers != zero
    )
    return sp.factor(center - variation)


def bernstein_controls_2d(expression, first, second):
    polynomial = sp.Poly(sp.expand(expression), first, second)
    degrees = (polynomial.degree(first), polynomial.degree(second))
    power = {powers: coefficient for powers, coefficient in polynomial.terms()}
    controls = {}
    for i in range(degrees[0] + 1):
        for j_index in range(degrees[1] + 1):
            value = 0
            for k_index in range(i + 1):
                for ell_index in range(j_index + 1):
                    value += (
                        power.get((k_index, ell_index), 0)
                        * sp.Rational(
                            sp.binomial(i, k_index),
                            sp.binomial(degrees[0], k_index),
                        )
                        * sp.Rational(
                            sp.binomial(j_index, ell_index),
                            sp.binomial(degrees[1], ell_index),
                        )
                    )
            controls[(i, j_index)] = sp.factor(value)
    return degrees, controls


R, I = sp.Rational, sp.I
h, q, lam = sp.symbols("h q lambda", real=True)
S, Z, x, y = sp.symbols("S Z x y", real=True)
X, Mpar, omega, nu = sp.symbols("X Mpar omega nu", real=True)

# Lossless transverse compact-ball frame.
a, c = 1 / sp.sqrt(6), sp.sqrt(R(5, 6))
zeta = R(4, 5) + I * R(3, 5)
p = sp.Matrix([a, 0, c])
rvec = sp.Matrix([-a, 0, c * zeta])
fvec = sp.Matrix([-c * h, q, -a * h * zeta])
nvec = sp.Matrix([c * q, h, a * q * zeta])
U = sp.Matrix.hstack(rvec, fvec)
q_relation = sp.Poly(q**2 - (1 - h**2), q)
exact_zero(reduce_q(U.conjugate().T * U - sp.eye(2), q, q_relation),
           "frame Gram")
exact_zero(reduce_q(U.conjugate().T * nvec, q, q_relation),
           "frame/kernel orthogonality")
exact_zero(reduce_q((nvec.conjugate().T * nvec)[0] - 1, q, q_relation),
           "kernel norm")

j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
C = sp.Matrix([
    [h**2, h * (j + I * kappa)],
    [h * (j - I * kappa), j**2 + kappa**2 + R(5, 9) * Z],
])
exact_zero(C - C.conjugate().T, "compression Hermitian")
exact_zero(C.det() - R(5, 9) * h**2 * Z, "compression determinant")

# Preserve both real square-root lifts.  The compression and gate depend only
# on z^2=Z, but the signed relation is checked before eliminating z.
zsign = sp.symbols("zsign", real=True)
ell = sp.sqrt(5) * zsign / 3
C_signed = C.copy()
C_signed[1, 1] = j**2 + kappa**2 + ell**2
signed_remainder = sp.rem(
    sp.expand(C_signed[1, 1] - C[1, 1]), zsign**2 - Z, zsign
)
exact_zero(signed_remainder, "both signed-z compressions")

H = sp.expand(U * C * U.conjugate().T)
exact_zero(reduce_q(H * nvec, q, q_relation), "H kernel")
Q = sp.expand(lam * H)
exact_zero(Q - Q.conjugate().T, "Q Hermitian")
xi = sp.expand(Q * p)
Q2 = sp.expand(Q * Q)
danger_formula = R(5, 36) * sp.sqrt(6) * lam * h**2 * (
    x**2 + y**2 + Z - 1
)
exact_zero(reduce_q(sp.re(xi[0]) - danger_formula, q, q_relation),
           "danger identity")

# Literal fully conjugated original gate.
leak1 = c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - Q2[2, 0])
leak2 = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
raw_gate = reduce_q(sp.expand_complex(
    4 * a**2 * xi[1] * sp.conjugate(xi[1])
    + leak1 * sp.conjugate(leak1)
    + leak2 * sp.conjugate(leak2)
    - 32 * a**2 * sp.re(xi[0])**2
), q, q_relation)
gate36 = even_h_to_S(36 * raw_gate, h, S)
require(not gate36.has(h, q), "frame variables survived")
require(sp.Poly(gate36, lam).degree() == 4, "scale quartic")
require(sp.Poly(gate36, lam).nth(0) == 5, "constant five")

# Independent Gram-vector ordering before inserting the proposed sheet.
Hp = sp.expand(H * p)
H2 = sp.expand(H * H)
B0 = sp.Matrix([I * a * c, 0, 0])
Lvec = sp.Matrix([
    c * sp.conjugate(Hp[0]) + a * Hp[2],
    c * sp.conjugate(Hp[1]),
    2 * a * Hp[1],
])
Mvec = sp.Matrix([-I * H2[2, 0], -I * H2[2, 1], 0])
Bvec = B0 + lam * Lvec + lam**2 * Mvec
gram_gate = reduce_q(sp.expand_complex(
    (Bvec.conjugate().T * Bvec)[0]
    - 32 * a**2 * lam**2 * sp.re(Hp[0])**2
), q, q_relation)
exact_zero(raw_gate - gram_gate, "Hermitian/Gram-vector gate equality")
print("PASS fully conjugated raw gate reconstructed independently")

# Proposed inward-Z sheet.
Mrad, wrad, nrad = R(1, 1000), R(1, 100), R(1, 100)
Smax = R(1, 10000)
Xmin, Xmid, Xmax = R(3, 13), R(25, 104), R(1, 4)
tilt = -R(10636, 275)
A = 1 + Mpar
y0 = R(12, 25) / A + nu
omega_physical = omega + tilt * (X - R(1, 5))
b = (45 * Mpar + 18) / (25 * A) - R(3, 5) * X + omega_physical
xmap = -R(1, 5) + X
ymap = R(3, 5) + S * y0
Zold = 3 * X - X**2 + S * b - S**2 * y0**2
Zmap = sp.factor(Zold - 3 * (X - Xmin))
exact_zero(Zmap - (R(9, 13) - X**2 + S * b - S**2 * y0**2),
           "inward-Z simplified map")
exact_zero((Zmap - Zold).subs(X, Xmin), "exact X=3/13 Z seam")

# Uniform exact legality.  On the whole box b<0, so Z decreases with S and X.
Amin, Amax = 1 - Mrad, 1 + Mrad
y0min = sp.factor(R(12, 25) / Amax - nrad)
y0max = sp.factor(R(12, 25) / Amin + nrad)
exact_zero(sp.diff(b, Mpar) - R(27, 25) / A**2, "b increases in M")
exact_zero(sp.diff(b, omega) - 1, "b increases in omega")
exact_zero(sp.diff(b, X) - (tilt - R(3, 5)), "b decreases in X")
bmax = sp.factor(b.subs({X: Xmin, Mpar: Mrad, omega: wrad}))
bmin = sp.factor(b.subs({X: Xmax, Mpar: -Mrad, omega: -wrad}))
require(y0min > 0 and y0max > y0min, "positive y0 interval")
require(bmin < bmax < 0, "b is uniformly negative")
Zlower = sp.factor(
    R(9, 13) - Xmax**2 + Smax * bmin - Smax**2 * y0max**2
)
Zupper_open = sp.factor(R(9, 13) - Xmin**2)
require(0 < Zlower and Zupper_open < 1, "uniform 0<Z<1")

T = sp.factor(R(6, 5) * y0 + b)
Tclosed = sp.factor(
    R(9, 5) + omega + R(6, 5) * nu - R(63, 125) / A
    - R(3, 5) * X + tilt * (X - R(1, 5))
)
exact_zero(T - Tclosed, "closed danger coefficient")
Tmax = sp.factor(Tclosed.subs({Mpar: Mrad, omega: wrad, nu: nrad}))
exact_zero(sp.diff(Tclosed, Mpar) - R(63, 125) / A**2,
           "T increases in M")
exact_zero(sp.diff(Tclosed, omega) - 1, "T increases in omega")
exact_zero(sp.diff(Tclosed, nu) - R(6, 5), "T increases in nu")
exact_zero(sp.diff(Tclosed, X) - (tilt - R(3, 5)), "T decreases in X")
require(Tmax.subs(X, Xmin) == -R(1, 100), "seam Tmax=-1/100")

danger = sp.factor(1 - xmap**2 - ymap**2 - Zmap)
danger_claim = sp.factor(R(2, 5) * (X - Xmin) - S * T)
exact_zero(danger - danger_claim, "literal inward-Z danger")
danger_lower = sp.factor(R(2, 5) * (X - Xmin) + S / 100)
# Since T<=Tmax(X)<=Tmax(Xmin)=-1/100, danger>=danger_lower>0.
require(Xmin < Xmid < Xmax and Amin > 0 and Smax > 0,
        "parameter intervals")
require(sp.diff(Tmax, X) < 0, "uniform T envelope decreases")
print("PASS continuum legality lambda>0, 0<Z<1, strict danger, rank two")
print("PASS exact seam with v12 affine-omega sheet at X=3/13")

# Required endpoint/midpoint x three scales x eight centered corners.
scales = (R(1, 1000000), R(1, 20000), Smax)
Xvalues = (Xmin, Xmid, Xmax)
records = []
for Sv, Xv, Mv, ov, nv in product(
    scales, Xvalues, (-Mrad, Mrad), (-wrad, wrad), (-nrad, nrad)
):
    Av = 1 + Mv
    y0v = R(12, 25) / Av + nv
    omegav = ov + tilt * (Xv - R(1, 5))
    bv = (45 * Mv + 18) / (25 * Av) - R(3, 5) * Xv + omegav
    Zv = sp.factor(
        3 * Xv - Xv**2 - 3 * (Xv - Xmin)
        + Sv * bv - Sv**2 * y0v**2
    )
    xv = -R(1, 5) + Xv
    yv = R(3, 5) + Sv * y0v
    lv = Av / Sv
    danger_v = sp.factor(1 - xv**2 - yv**2 - Zv)
    det_v = sp.factor(R(5, 9) * Sv * Zv)
    value = sp.factor(gate36.subs({S: Sv, Z: Zv, x: xv, y: yv, lam: lv}))
    require(lv > 0 and 0 < Zv < 1 and danger_v > 0 and det_v > 0,
            f"legal node {(Sv, Xv, Mv, ov, nv)}")
    require(value > 0, f"negative raw gate node {(Sv, Xv, Mv, ov, nv)}")
    records.append(((Sv, Xv, Mv, ov, nv), value, Zv, danger_v, det_v))

require(len(records) == 72, "72 exact nodes")
minimum_gate = min(records, key=lambda record: record[1])
minimum_danger = min(records, key=lambda record: record[3])
minimum_Z = min(records, key=lambda record: record[2])
print("PASS 72/72 exact rational nodes legal and raw-gate positive")
print("NODE_MIN_GATE_ARGUMENT", minimum_gate[0])
print("NODE_MIN_36GAMMA", minimum_gate[1])
print("NODE_MIN_DANGER_ARGUMENT", minimum_danger[0])
print("NODE_MIN_DANGER", minimum_danger[3])
print("NODE_MIN_Z_ARGUMENT", minimum_Z[0])
print("NODE_MIN_Z", minimum_Z[2])

# Second discriminating test: reuse the v12 exact sparse quotient and the
# seam-preserving tau/u tensor-Bernstein architecture.  This remains a
# discovery certificate attempt until every centered lower control is strict.
mu, Yaux = sp.symbols("mu Yaux", real=True)
premap = sp.expand((S**3 * sp.cancel(gate36.subs(lam, mu / S))).subs({
    x: -R(1, 5) + X,
    y: R(3, 5) + Yaux,
    mu: A,
}))
premap_poly = sp.Poly(premap, S, Z, X, Yaux)
require(len(premap_poly.terms()) == 134, "134 pre-map terms")
denominator = 25 * A
sparse_y = {(1, 0): (12 + 25 * A * nu) / denominator}
sparse_z = {
    (0, 0): R(9, 13),
    (0, 2): -R(1),
    (1, 0): (
        45 * Mpar + 18 + 25 * A * (omega - tilt * R(1, 5))
    ) / denominator,
    (1, 1): tilt - R(3, 5),
    (2, 0): -((12 + 25 * A * nu) / denominator)**2,
}
sparse_y_expression = sp.expand(sum(
    coefficient * S**s_degree * X**x_degree
    for (s_degree, x_degree), coefficient in sparse_y.items()
))
sparse_z_expression = sp.expand(sum(
    coefficient * S**s_degree * X**x_degree
    for (s_degree, x_degree), coefficient in sparse_z.items()
))
exact_zero(sparse_y_expression - S * y0, "sparse/direct Y map")
exact_zero(sparse_z_expression - Zmap, "sparse/direct inward-Z map")

mapped = {}
for (s_degree, z_degree, x_degree, y_degree), coefficient in premap_poly.terms():
    term = {(s_degree, x_degree): coefficient}
    term = sparse_multiply(term, sparse_power(sparse_z, z_degree))
    term = sparse_multiply(term, sparse_power(sparse_y, y_degree))
    mapped = sparse_add(mapped, term)

cleared = {}
for key, coefficient in mapped.items():
    value = sp.cancel(denominator**8 * coefficient)
    if value == 0:
        continue
    require(not value.as_numer_denom()[1].free_symbols,
            f"symbolic quotient denominator at {key}")
    cleared[key] = sp.expand(value)
minimum_cleared_S_degree = min(s_degree for s_degree, _ in cleared)
cleared_polynomial = sp.expand(sum(
    coefficient * S**s_degree * X**x_degree
    for (s_degree, x_degree), coefficient in cleared.items()
))
qhat = sp.expand(cleared_polynomial / S**minimum_cleared_S_degree)
require(sp.Poly(qhat, S, X, Mpar, omega, nu).domain == sp.QQ,
        "rational quotient")
sx = sp.Poly(qhat, S, X, domain=sp.EX)
coefficients = {
    powers: sp.expand(coefficient) for powers, coefficient in sx.terms()
}
quotient_count = len(coefficients)
quotient_degree = (sx.degree(S), sx.degree(X))

# Preserve the manifestly nonnegative v12 layer as an exact summand.  The
# inward-Z displacement introduces lower S orders, so unlike v12 it need not
# remain an entire isolated coefficient after the new normalization.
expected_first = 25**8 * Mpar**2 * A**8 * (
    5 * Mpar**2 + 14 * Mpar + 14
)
first_layer_power = 3 - minimum_cleared_S_degree
require(first_layer_power >= 0, "nonnegative first-layer S power")
first_layer_term = S**first_layer_power * expected_first
exact_zero(
    5 * Mpar**2 + 14 * Mpar + 14
    - (5 * (Mpar + R(7, 5))**2 + R(21, 5)),
    "first-layer square",
)
qcore = sp.expand(qhat - first_layer_term)
exact_zero(qhat - (first_layer_term + qcore), "first-layer decomposition")

variables = (Mpar, omega, nu)
radii = (Mrad, wrad, nrad)
remainder_sx = sp.Poly(qcore, S, X, domain=sp.EX)
remainder_coefficients = {
    powers: sp.expand(coefficient)
    for powers, coefficient in remainder_sx.terms()
}
remainder_monomials = sum(
    len(sp.Poly(value, *variables).terms())
    for value in remainder_coefficients.values()
)

sigma_max = sp.factor(Smax / Xmin)
tau, useam = sp.symbols("tau useam", real=True)
Xaff = sp.factor(Xmin + (Xmax - Xmin) * useam)
exact_zero(Xaff.subs(useam, 0) - Xmin, "tau/u left seam")
exact_zero(Xaff.subs(useam, 1) - Xmax, "tau/u right endpoint")
recentered = sp.expand(qcore.subs({S: sigma_max * tau * Xaff, X: Xaff}))
bernstein_degree, controls = bernstein_controls_2d(recentered, tau, useam)
control_lowers = {
    key: centered_lower(value, variables, radii)
    for key, value in controls.items()
}
minimum_control = min(control_lowers.items(), key=lambda item: item[1])
nonpositive_controls = {
    key: value for key, value in control_lowers.items() if value <= 0
}
positive_controls = {
    key: value for key, value in control_lowers.items() if value > 0
}
minimum_positive_control = min(
    positive_controls.items(), key=lambda item: item[1]
)
expected_zero_controls = {(0, 0), (0, 1), (1, 0)}
require(set(nonpositive_controls) == expected_zero_controls,
        "exactly three boundary-zero controls")
for key in expected_zero_controls:
    require(nonpositive_controls[key] == 0, f"zero lower at {key}")
    exact_zero(controls[key], f"identically zero control {key}")
expected_positive_reserve = R(
    10071067674014002577317165966399410637259618083,
    128416777961472000000000000000000000000000000,
)
require(
    len(positive_controls) == 77
    and minimum_positive_control == ((2, 0), expected_positive_reserve),
    "77 strict controls and exact minimum reserve",
)

# Strictness on the physical domain does not require strict controls on the
# artificial tau=0 closure.  The tensor Bernstein weight of every i>=2 row is
# exactly the following positive expression.  For 0<tau<1 its i=2 summand is
# 21*tau^2*(1-tau)^5>0; at tau=1 the complete weight is exactly one.
strict_row_weight = sp.expand(sum(
    sp.binomial(7, i_index)
    * tau**i_index * (1 - tau)**(7 - i_index)
    for i_index in range(2, 8)
))
strict_row_weight_claim = sp.expand(
    1 - (1 - tau)**7 - 7 * tau * (1 - tau)**6
)
exact_zero(strict_row_weight - strict_row_weight_claim,
           "i>=2 Bernstein row weight identity")
require(strict_row_weight.subs(tau, 1) == 1,
        "strict row weight at tau=1")
print("CLEARED_MIN_S_DEGREE", minimum_cleared_S_degree)
print("QUOTIENT_COUNTS", quotient_count, len(remainder_coefficients), remainder_monomials)
print("QUOTIENT_DEGREE_S_X", quotient_degree)
print("FIRST_LAYER_S_POWER", first_layer_power)
print("BERNSTEIN_DEGREE_TAU_U", bernstein_degree)
print("BERNSTEIN_CONTROL_COUNT", len(controls))
print("BERNSTEIN_NONPOSITIVE_LOWER_COUNT", len(nonpositive_controls))
for key in sorted(nonpositive_controls):
    print("BERNSTEIN_NONPOSITIVE_LOWER", key, nonpositive_controls[key])
    print(
        "BERNSTEIN_NONPOSITIVE_CONTROL_CENTER",
        key,
        sp.factor(controls[key].subs({Mpar: 0, omega: 0, nu: 0})),
    )
    print("BERNSTEIN_NONPOSITIVE_CONTROL_POLYNOMIAL", key, controls[key])
print("BERNSTEIN_MIN_LOWER_INDEX", minimum_control[0])
print("BERNSTEIN_MIN_LOWER", minimum_control[1])
print("BERNSTEIN_MIN_POSITIVE_LOWER_INDEX", minimum_positive_control[0])
print("BERNSTEIN_MIN_POSITIVE_LOWER", minimum_positive_control[1])
print("BERNSTEIN_STRICT_ROW_WEIGHT", strict_row_weight_claim)
print("BERNSTEIN_STRICT_ROW_WEIGHT_AT_TAU_1", strict_row_weight.subs(tau, 1))
print("PASS continuum quotient: 3 closure zeros and 77 strict controls")
print("CONTINUUM_STATUS exact source certificate candidate; independent audit required")
print("B_MIN", bmin)
print("B_MAX", bmax)
print("Y0_MIN", y0min)
print("Y0_MAX", y0max)
print("Z_CONTINUUM_LOWER", Zlower)
print("Z_CONTINUUM_UPPER_OPEN", Zupper_open)
print("DANGER_LOWER_FORMULA", danger_lower)
print("PYTHON", platform.python_version())
print("SYMPY", sp.__version__)
print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact continuum source certificate candidate; independent referee pending")
print("SCOPE inward-Z discovery only; compact-ball/common-metric/fixed-lens open")
