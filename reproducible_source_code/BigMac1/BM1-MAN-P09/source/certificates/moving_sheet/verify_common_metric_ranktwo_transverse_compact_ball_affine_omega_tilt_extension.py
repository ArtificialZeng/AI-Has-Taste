#!/usr/bin/env python3
"""Fail-closed exact verifier for the affine-omega tilted moving sheet.

No discovery program, predecessor verifier, cached quartic, or coefficient
table is imported.  The script rebuilds the fully conjugated Hermitian
Q,Q^2 gate, an internal Gram-vector evaluator, the tilted moving quotient,
and the exact two-stage Bernstein certificate from the original definitions.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables verification")

from hashlib import sha256
from itertools import product
import os
from pathlib import Path
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: verifier accepts no arguments")

HERE = Path(__file__).resolve()
if (HERE.parent.name == "research"
        and HERE.parent.parent.name == "tmp"
        and HERE.parents[2].name == "certificate_workspace"):
    RELEASE_ROOT = HERE.parents[3]
elif (HERE.parent.name == "moving_sheet"
        and HERE.parent.parent.name == "certificates"):
    RELEASE_ROOT = HERE.parents[2]
else:
    raise RuntimeError("fail closed: unsupported packaged verifier layout")
ROOT = (RELEASE_ROOT / "certificate_workspace").resolve()
if not ROOT.is_dir() or ROOT.parent != RELEASE_ROOT:
    raise RuntimeError("fail closed: packaged certificate workspace is missing")
DEPENDENCIES = {
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension.md":
        "e3f37ef598110eaad6c96a45eabff1e6313256923950057e8145568dbde865e0",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
}
if os.environ.get("AFFINE_OMEGA_TILT_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), f"dependency escapes package {relative}")
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


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
    for (si, xi), lv in left.items():
        for (sj, xj), rv in right.items():
            key = (si + sj, xi + xj)
            result[key] = result.get(key, 0) + lv * rv
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
        abs(coefficient) * sp.prod(radius**degree
                                   for radius, degree in zip(radii, powers))
        for powers, coefficient in polynomial.terms() if powers != zero
    )
    return sp.factor(center - variation)


def bernstein_controls_2d(expression, first, second):
    polynomial = sp.Poly(sp.expand(expression), first, second)
    dfirst, dsecond = polynomial.degree(first), polynomial.degree(second)
    power = {powers: coefficient for powers, coefficient in polynomial.terms()}
    controls = {}
    for i in range(dfirst + 1):
        for j in range(dsecond + 1):
            value = 0
            for k in range(i + 1):
                for ell in range(j + 1):
                    value += (
                        power.get((k, ell), 0)
                        * sp.Rational(sp.binomial(i, k), sp.binomial(dfirst, k))
                        * sp.Rational(sp.binomial(j, ell), sp.binomial(dsecond, ell))
                    )
            controls[(i, j)] = sp.factor(value)
    return (dfirst, dsecond), controls


R, I = sp.Rational, sp.I
h, q, lam = sp.symbols("h q lambda", real=True)
S, Z, x, y = sp.symbols("S Z x y", real=True)
X, Mpar, omega, nu = sp.symbols("X Mpar omega nu", real=True)
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
zsign = sp.symbols("zsign", real=True)
ell = sp.sqrt(5) * zsign / 3
C_signed = C.copy()
C_signed[1, 1] = j**2 + kappa**2 + ell**2
signed_difference = sp.rem(
    sp.expand(C_signed[1, 1] - C[1, 1]), zsign**2 - Z, zsign
)
exact_zero(signed_difference, "both signed z compressions")

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
leak1 = c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - Q2[2, 0])
leak2 = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
raw_gate = reduce_q(sp.expand_complex(
    4 * a**2 * xi[1] * sp.conjugate(xi[1])
    + leak1 * sp.conjugate(leak1) + leak2 * sp.conjugate(leak2)
    - 32 * a**2 * sp.re(xi[0])**2
), q, q_relation)
gate36 = even_h_to_S(36 * raw_gate, h, S)
require(not gate36.has(h, q), "frame variables survived")
require(sp.Poly(gate36, lam).degree() == 4, "scale quartic")
require(sp.Poly(gate36, lam).nth(0) == 5, "constant five")

# A separate component order checks the literal gate before any moving map.
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
exact_zero(raw_gate - gram_gate, "Hermitian/Gram-vector equality")
print("PASS original fully conjugated Hermitian gate and Gram gate")

# Tilted moving map.  The centered radii are unchanged.
A = 1 + Mpar
Xmin, Xmax, Smax = R(1, 5), R(3, 13), R(1, 10000)
tilt = -R(10636, 275)
y0 = R(12, 25) / A + nu
omega_physical = omega + tilt * (X - Xmin)
wc = (45 * Mpar + 18) / (25 * A) - R(3, 5) * X
Ymap = S * y0
Wmap = S * (wc + omega_physical)
xmap = -R(1, 5) + X
ymap = R(3, 5) + Ymap
Zmap = 3 * X - X**2 - Ymap**2 + Wmap
exact_zero(xmap**2 + ymap**2 + Zmap
           - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
           "moving danger identity")

# Sparse quotient rebuilt from the original fully conjugated gate.
mu, Yaux = sp.symbols("mu Yaux", real=True)
premap = sp.expand((S**3 * sp.cancel(gate36.subs(lam, mu / S))).subs({
    x: -R(1, 5) + X, y: R(3, 5) + Yaux, mu: A,
}))
premap_poly = sp.Poly(premap, S, Z, X, Yaux)
require(len(premap_poly.terms()) == 134, "134 pre-map terms")
denominator = 25 * A
sparse_y = {(1, 0): (12 + 25 * A * nu) / denominator}
sparse_z = {
    (0, 1): R(3), (0, 2): -R(1),
    (1, 0): (45 * Mpar + 18
             + 25 * A * (omega - tilt * Xmin)) / denominator,
    (1, 1): tilt - R(3, 5),
    (2, 0): -((12 + 25 * A * nu) / denominator)**2,
}
sparse_y_expression = sp.expand(sum(
    coefficient * S**sd * X**xd
    for (sd, xd), coefficient in sparse_y.items()
))
sparse_z_expression = sp.expand(sum(
    coefficient * S**sd * X**xd
    for (sd, xd), coefficient in sparse_z.items()
))
exact_zero(sparse_y_expression - Ymap, "sparse/direct Y map equality")
exact_zero(sparse_z_expression - Zmap, "sparse/direct Z map equality")
mapped = {}
for (sd, zd, xd, yd), coefficient in premap_poly.terms():
    term = {(sd, xd): coefficient}
    term = sparse_multiply(term, sparse_power(sparse_z, zd))
    term = sparse_multiply(term, sparse_power(sparse_y, yd))
    mapped = sparse_add(mapped, term)
cleared = {}
for key, coefficient in mapped.items():
    value = sp.cancel(denominator**8 * coefficient)
    if value == 0:
        continue
    require(not value.as_numer_denom()[1].free_symbols,
            f"symbolic denominator {key}")
    cleared[key] = sp.expand(value)
require(all(sd >= 2 for sd, _ in cleared), "exact S^2 factor")
qhat = sp.expand(sum(
    coefficient * S**(sd - 2) * X**xd
    for (sd, xd), coefficient in cleared.items()
))
require(sp.Poly(qhat, S, X, Mpar, omega, nu).domain == sp.QQ,
        "rational quotient")
sx = sp.Poly(qhat, S, X, domain=sp.EX)
coefficients = {
    powers: sp.expand(coefficient) for powers, coefficient in sx.terms()
}
require(len(coefficients) == 22 and sx.degree(S) == 5 and sx.degree(X) == 4,
        "22-term bidegree-(5,4) quotient")
first_layer = coefficients.pop((1, 0))
expected_first = 25**8 * Mpar**2 * A**8 * (
    5 * Mpar**2 + 14 * Mpar + 14
)
exact_zero(first_layer - expected_first, "M^2 first layer")
exact_zero(5 * Mpar**2 + 14 * Mpar + 14
           - (5 * (Mpar + R(7, 5))**2 + R(21, 5)),
           "first-layer square")
if os.environ.get("AFFINE_OMEGA_TILT_TEST_DROP_TERM") == "1":
    coefficients.pop(next(key for key in coefficients if sum(key) > 2))
require(len(coefficients) == 21, "complete post-first-layer term set")

variables = (Mpar, omega, nu)
radii = (R(1, 1000), R(1, 100), R(1, 100))
higher = {key: value for key, value in coefficients.items() if sum(key) > 2}
require(len(higher) == 18, "18 higher terms")
require(sum(len(sp.Poly(value, *variables).terms()) for value in higher.values())
        == 1013, "1013 centered parameter monomials")

# Lossless sigma chart, seam-preserving X recenter, and tensor Bernstein.
sigma_max = sp.factor(Smax / Xmin)
require(sigma_max == R(1, 2000), "lossless sigma maximum")
tau, useam = sp.symbols("tau useam", real=True)
Xaff = Xmin + (Xmax - Xmin) * useam
exact_zero(Xaff.subs(useam, 0) - Xmin, "X=1/5 seam")
exact_zero(Xaff.subs(useam, 1) - Xmax, "X=3/13 endpoint")
qcore = sp.expand(sum(
    coefficient * S**sd * X**xd
    for (sd, xd), coefficient in coefficients.items()
))
recentered = sp.expand(qcore.subs({S: sigma_max * tau * Xaff, X: Xaff}))
degree, controls = bernstein_controls_2d(recentered, tau, useam)
require(degree == (5, 7) and len(controls) == 48,
        "48 tensor Bernstein controls of degree (5,7)")
control_lowers = {
    key: centered_lower(value, variables, radii)
    for key, value in controls.items()
}
minimum_index, reserve = min(control_lowers.items(), key=lambda item: item[1])
expected_reserve = R(
    2564950982194530478444050838857341987999,
    31850496000000000000000000000,
)
require(all(value > 0 for value in control_lowers.values()),
        "48/48 strict centered controls")
require(minimum_index == (0, 0) and reserve == expected_reserve,
        "exact decisive reserve")
print("PASS 22/18/1013 quotient counts and 48/48 strict controls")

# Exact legality, strict danger, and the scale-uniform obstruction beyond 3/13.
Mrad, wrad, nrad = radii
Amin, Amax = 1 - Mrad, 1 + Mrad
y0min = sp.factor(R(12, 25) / Amax - nrad)
y0max = sp.factor(R(12, 25) / Amin + nrad)
b = sp.factor(wc + omega_physical)
exact_zero(sp.diff(b, Mpar) - R(27, 25) / A**2, "b increases in M")
exact_zero(sp.diff(b, omega) - 1, "b increases in omega")
exact_zero(sp.diff(b, X) - (tilt - R(3, 5)), "b X slope")
bmin = sp.factor(b.subs({X: Xmax, Mpar: -Mrad, omega: -wrad}))
bmax = sp.factor(b.subs({X: Xmin, Mpar: Mrad, omega: wrad}))
zlower = sp.factor(3 * Xmin - Xmin**2 + Smax * bmin - Smax**2 * y0max**2)
zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * bmax)
require(y0min > 0 and bmin == R(-1639111, 2645500), "positive y0 and exact bmin")
require(zlower == R(
    8879008598718934873, 15857127000000000000
) > 0, "strict positive Z lower")
require(zupper == R(8316795197, 13013000000) < 1,
        "strict Z upper")

T = sp.factor(R(6, 5) * y0 + b)
Tclosed = sp.factor(
    R(9, 5) + omega + R(6, 5) * nu - R(63, 125) / A
    - R(3, 5) * X + tilt * (X - Xmin)
)
exact_zero(T - Tclosed, "closed danger coefficient")
danger = sp.factor(R(3, 5) - R(13, 5) * X - S * T)
exact_zero(1 - xmap**2 - ymap**2 - Zmap - danger,
           "literal danger equality")
Tmax = sp.factor(Tclosed.subs({Mpar: Mrad, omega: wrad, nu: nrad}))
exact_zero(sp.diff(Tclosed, Mpar) - R(63, 125) / A**2,
           "T increases in M")
exact_zero(sp.diff(Tclosed, omega) - 1, "T increases in omega")
exact_zero(sp.diff(Tclosed, nu) - R(6, 5), "T increases in nu")
exact_zero(sp.diff(Tclosed, X) - (tilt - R(3, 5)), "T X slope")
require(Tmax.subs(X, Xmax) == -R(1, 100), "endpoint Tmax")
danger_minus = sp.factor(danger - S / 100)
worst_danger_minus = sp.factor(
    R(3, 5) - R(13, 5) * X - Smax * (Tmax + R(1, 100))
)
require(worst_danger_minus.subs(X, Xmax) == 0
        and sp.diff(worst_danger_minus, X) < 0,
        "uniform D>=S/100 envelope")
endpoint_danger = sp.factor(danger.subs({
    X: Xmax, Mpar: Mrad, omega: wrad, nu: nrad,
}))
exact_zero(endpoint_danger - S / 100, "sharp endpoint danger")
tail_epsilon = sp.symbols("tail_epsilon", positive=True)
small_scale_limit = sp.factor(sp.limit(danger, S, 0, dir="+"))
exact_zero(small_scale_limit.subs(X, Xmax + tail_epsilon)
           + R(13, 5) * tail_epsilon,
           "X>3/13 small-scale obstruction")
require(Amin > 0 and Smax < 1 and Xmin > 0,
        "positive scale and real frame")
require(25**8 * Amin**8 * Smax > 0, "positive clearing factors")
print("PASS lambda, 0<Z<1, rank-two PSD, both signed z, D>=S/100")
print("PASS exact S->0 obstruction for every X>3/13")

# Exact seam/interior/endpoint attack grid in the original gate.
records = []
for Sv, uv, Mv, ov, nv in product(
    (R(1, 1000000), R(1, 20000), Smax),
    (R(0), R(1, 2), R(1)),
    (-Mrad, Mrad), (-wrad, wrad), (-nrad, nrad),
):
    Xv = sp.factor(Xaff.subs(useam, uv))
    Av = 1 + Mv
    y0v = R(12, 25) / Av + nv
    omegav = ov + tilt * (Xv - Xmin)
    bv = (45 * Mv + 18) / (25 * Av) - R(3, 5) * Xv + omegav
    Zv = sp.factor(3 * Xv - Xv**2 + Sv * bv - Sv**2 * y0v**2)
    xv, yv, lv = -R(1, 5) + Xv, R(3, 5) + Sv * y0v, Av / Sv
    danger_v = sp.factor(1 - xv**2 - yv**2 - Zv)
    det_v = sp.factor(R(5, 9) * Sv * Zv)
    value = sp.factor(gate36.subs({S: Sv, Z: Zv, x: xv, y: yv, lam: lv}))
    require(lv > 0 and 0 < Zv < 1 and danger_v > 0 and det_v > 0,
            "legal rank-two exact node")
    require(value > 0, "negative exact original gate node")
    records.append(((Sv, uv, Mv, ov, nv), value, Zv, danger_v, det_v))
require(len(records) == 72, "72 exact nodes")
minimum = min(records, key=lambda item: item[1])
left_arg = (Smax, R(0), -Mrad, -wrad, -nrad)
right_arg = (Smax, R(1), -Mrad, -wrad, -nrad)
danger_arg = (Smax, R(1), Mrad, wrad, nrad)
left = next(record for record in records if record[0] == left_arg)
right = next(record for record in records if record[0] == right_arg)
danger_corner = next(record for record in records if record[0] == danger_arg)
require(left[1] == R(
    213355344357890421512795094325969057679,
    40000000000000000000000000000000000,
) > 0, "exact left seam gate")
require(right[1] == R(
    184421770823082033734271204948812328298851568079,
    16726464040000000000000000000000000000000000,
) > 0, "exact right endpoint gate")
require(danger_corner[1] == R(
    2875017794276661652931485545294665330527919,
    262440000000000000000000000000000000000,
) > 0, "exact worst-danger endpoint gate")
require(danger_corner[2] == R(
    640272135596701999, 1002001000000000000
) and danger_corner[3] == R(1, 1000000)
        and danger_corner[4] == R(
            640272135596701999, 18036018000000000000000
        ), "exact worst-danger endpoint legality")
require(minimum[1] == left[1], "exact grid minimum")
print("PASS X=1/5 seam, X=3/13 endpoint, 72/72 exact legal nodes")

print("TILT_SLOPE", tilt)
print("QUOTIENT_COUNTS", 22, 18, 1013)
print("BERNSTEIN_DEGREE", degree)
print("BERNSTEIN_CONTROLS", len(controls))
print("STRICT_RESERVE", reserve)
print("Z_LOWER", zlower)
print("Z_UPPER", zupper)
print("ENDPOINT_TMAX", Tmax.subs(X, Xmax))
print("ENDPOINT_DANGER", danger_corner[3])
print("LEFT_SEAM_36GAMMA", left[1])
print("RIGHT_ENDPOINT_36GAMMA", right[1])
print("VERIFIER_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact tilted gate on closed 1/5<=X<=3/13 with strict danger")
print("SCOPE moving-sheet partial theorem; compact ball/common metric/fixed lens open")
