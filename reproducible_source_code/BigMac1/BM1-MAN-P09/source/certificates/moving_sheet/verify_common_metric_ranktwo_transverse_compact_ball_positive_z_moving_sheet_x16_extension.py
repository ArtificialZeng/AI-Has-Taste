#!/usr/bin/env python3
"""Fail-closed exact verifier for the closed moving-sheet X16 cell.

The program imports no discovery code, predecessor verifier, cached quartic,
or coefficient table.  It rebuilds the fully conjugated Hermitian Q,Q^2 gate,
an independent Gram-vector evaluator, the sparse moving quotient, every
actual compact-ball chart prerequisite, both z signs, the X=1/17 seam, and
the continuum certificate.  In particular, it does not assume Z<1/6: that
was only a descriptive bound on the predecessor cell.
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
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.md":
        "e9ed0d778a4754a3b7144754b0277cf67c282bae6879676b4d24a34239cf12fc",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
}
if os.environ.get("X16_TEST_BAD_DEPENDENCY") == "1":
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
        abs(coefficient) * sp.prod(r**d for r, d in zip(radii, powers))
        for powers, coefficient in polynomial.terms() if powers != zero
    )
    return sp.factor(center - variation)


def centered_absolute(expression, variables, radii):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    bound = sum(
        abs(coefficient) * sp.prod(r**d for r, d in zip(radii, powers))
        for powers, coefficient in polynomial.terms()
    )
    return sp.factor(bound), len(polynomial.terms())


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

# Signed-z construction: the literal ell formula reduces to this same C for
# either sign after ell^2=5Z/9.
zsign = sp.symbols("zsign", real=True)
ell = sp.sqrt(5) * zsign / 3
C_signed = C.copy()
C_signed[1, 1] = j**2 + kappa**2 + ell**2
signed_difference = sp.rem(sp.expand(C_signed[1, 1] - C[1, 1]), zsign**2 - Z, zsign)
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

# Independent component ordering of the Gram-vector gate.
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
print("PASS original fully conjugated Hermitian gate and independent Gram gate")

# Exact moving map and sparse quotient rebuilt from the original quartic.
A = 1 + Mpar
y0 = R(12, 25) / A + nu
wc = -3 * (5 * Mpar * X - 15 * Mpar + 5 * X - 6) / (25 * A)
Ymap = S * y0
Wmap = S * (wc + omega)
xmap = -R(1, 5) + X
ymap = R(3, 5) + Ymap
Zmap = 3 * X - X**2 - Ymap**2 + Wmap
exact_zero(xmap**2 + ymap**2 + Zmap
           - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
           "moving danger identity")

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
    (1, 0): (45 * Mpar + 18 + 25 * A * omega) / denominator,
    (1, 1): -R(3, 5),
    (2, 0): -((12 + 25 * A * nu) / denominator)**2,
}
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
coefficients = {powers: sp.expand(coefficient) for powers, coefficient in sx.terms()}
require(len(coefficients) == 20 and sx.degree(S) == 5 and sx.degree(X) == 4,
        "20-term bidegree-(5,4) quotient")
first_layer = coefficients.pop((1, 0))
expected_first = R(152587890625) * Mpar**2 * A**8 * (
    5 * Mpar**2 + 14 * Mpar + 14
)
exact_zero(first_layer - expected_first, "first layer")
exact_zero(5 * Mpar**2 + 14 * Mpar + 14
           - (5 * (Mpar + R(7, 5))**2 + R(21, 5)),
           "first-layer square")

variables = (Mpar, omega, nu)
radii = (R(1, 1000), R(1, 100), R(1, 100))
quadratic = {
    key: centered_lower(coefficients[key], variables, radii)
    for key in ((2, 0), (1, 1), (0, 2))
}
require(all(value > 0 for value in quadratic.values()), "positive quadratic core")
c0 = quadratic[(0, 2)]
expected_c0 = R(
    2564950982194530478444050838857341987999,
    1274019840000000000000000000,
)
require(c0 == expected_c0, "exact c0")

# Seam-preserving affine coordinate and lossless sigma chart.
u = sp.symbols("u", real=True)
X_from_u = (16 + u) / 272
exact_zero(X_from_u.subs(u, 0) - R(1, 17), "u=0 seam")
exact_zero(X_from_u.subs(u, 1) - R(1, 16), "u=1 endpoint")
Smax, Xmin, Xmax = R(1, 10000), R(1, 17), R(1, 16)
sigmamax = sp.factor(Smax / Xmin)
require(sigmamax == R(17, 10000), "sigma maximum")
if os.environ.get("X16_TEST_DROP_TERM") == "1":
    coefficients.pop(next(key for key in coefficients if sum(key) > 2))

remainder = 0
higher_terms = parameter_monomials = 0
for (sd, xd), coefficient in coefficients.items():
    if sd + xd <= 2:
        continue
    bound, terms = centered_absolute(coefficient, variables, radii)
    remainder += bound * sigmamax**sd * Xmax**(sd + xd - 2)
    higher_terms += 1
    parameter_monomials += terms
remainder = sp.factor(remainder)
margin = sp.factor(c0 - remainder)
require(higher_terms == 16 and parameter_monomials == 947,
        "16 higher terms and 947 parameter monomials")
expected_remainder = R(
    195558729458242556506677898727802762678086407732070733467174131616417,
    70448201072640000000000000000000000000000000000000000000000,
)
expected_margin = R(
    141635970781970514779535557286727779805714617592267929266532825868383583,
    70448201072640000000000000000000000000000000000000000000000,
)
require(remainder == expected_remainder, "exact remainder")
require(margin == expected_margin and margin > 0, "strict continuum margin")
print("PASS 20 quotient terms, 16 higher terms, 947 monomials, strict margin")

# Legality is independent of the gate envelope.
Mrad, wrad, nrad = radii
Amin, Amax = 1 - Mrad, 1 + Mrad
y0min = R(12, 25) / Amax - nrad
y0max = R(12, 25) / Amin + nrad
w0min = (18 - 45 * Mrad) / (25 * Amin) - wrad
w0max = (18 + 45 * Mrad) / (25 * Amax) + wrad
wlower = sp.factor(w0min - R(3, 5) * Xmax)
zslope = sp.factor(wlower - Smax * y0max**2)
zbase = sp.factor(3 * Xmin - Xmin**2)
zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * w0max)
danger = sp.factor(R(3, 5) - R(13, 5) * Xmax
                   - R(6, 5) * Smax * y0max - Smax * w0max)
claims = {
    "Amin": (Amin, R(999, 1000)),
    "y0min": (y0min, R(46999, 100100)),
    "wlower": (wlower, R(9937, 14800)),
    "zslope": (zslope, R(7445030483111, 11088900000000)),
    "zbase": (zbase, R(50, 289)),
    "zupper": (zupper, R(735402099, 4004000000)),
    "danger": (danger, R(242981998379, 555555000000)),
}
for label, (value, expected) in claims.items():
    exact_zero(value - expected, label)
endpoint_base = sp.factor(3 * Xmin - Xmin**2)
cross_reserve = sp.factor(endpoint_base - R(1, 6))
require(Smax < 1 and Xmin > 0, "real frame and positive X divisor")
require(Amin > 0 and y0min > 0 and zslope > 0, "positive scale and Z")
require(zbase > 0 and zupper < 1 and danger > 0, "open unit-ball legality")
require(cross_reserve == R(11, 1734) > 0,
        "cell lies strictly beyond predecessor Z=1/6 locator")
require(25**8 * Amin**8 * Smax > 0,
        "all moving-quotient clearing factors positive")
print("PASS lambda, 50/289<Z<1, open unit ball, rank-two PSD, both z signs")
print("PASS actual compact-ball prerequisites do not require Z<1/6")

# Endpoint/seam and exact rational falsification route.
sample_S = (R(1, 1000000), R(1, 20000), Smax)
sample_u = (R(0), R(1, 2), R(1))
records = []
for Sv, uv, Mv, ov, nv in product(
    sample_S, sample_u, (-Mrad, Mrad), (-wrad, wrad), (-nrad, nrad)
):
    Xv = sp.factor(X_from_u.subs(u, uv))
    Av = 1 + Mv
    y0v = R(12, 25) / Av + nv
    wcv = -3 * (5 * Mv * Xv - 15 * Mv + 5 * Xv - 6) / (25 * Av)
    Yv = Sv * y0v
    Zv = sp.factor(3 * Xv - Xv**2 - Yv**2 + Sv * (wcv + ov))
    xv, yv, lv = -R(1, 5) + Xv, R(3, 5) + Yv, Av / Sv
    danger_v = sp.factor(1 - xv**2 - yv**2 - Zv)
    det_v = sp.factor(R(5, 9) * Sv * Zv)
    value = sp.factor(gate36.subs({S: Sv, Z: Zv, x: xv, y: yv, lam: lv}))
    require(lv > 0 and Zv > 0 and danger_v > 0 and det_v > 0, "legal node")
    require(value > 0, "negative exact original gate node")
    records.append(((Sv, uv, Mv, ov, nv), value, Zv, danger_v, det_v))
require(len(records) == 72, "72 exact nodes")
minimum = min(records, key=lambda item: item[1])
left_arg = (Smax, R(0), -Mrad, -wrad, -nrad)
right_arg = (Smax, R(1), -Mrad, -wrad, -nrad)
left = next(record for record in records if record[0] == left_arg)
right = next(record for record in records if record[0] == right_arg)
left_claim = R(
    1552541492892247573695625585542882277607759,
    3340840000000000000000000000000000000000,
)
right_claim = R(
    5243094533770053746415166844845583951,
    10000000000000000000000000000000000,
)
require(minimum[1] > 0, "falsification minimum")
require(left[1] == left_claim and right[1] == right_claim,
        "exact endpoint witnesses")
print("PASS closed X=1/17 seam, X=1/16 endpoint, and 72 legal exact nodes")

print("SIGMA_MAX", sigmamax)
print("REMAINDER_ABS", remainder)
print("STRICT_MARGIN", margin)
print("Z_UPPER", zupper)
print("DANGER_RESERVE", danger)
print("Z_EQUALS_ONE_SIXTH_CROSS_RESERVE", cross_reserve)
print("LEFT_SEAM_36GAMMA", left[1])
print("RIGHT_ENDPOINT_36GAMMA", right[1])
print("VERIFIER_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact strict original gate for 1/17<=X<=1/16")
print("SCOPE moving-sheet partial theorem; compact ball/common metric/fixed lens open")
