#!/usr/bin/env python3
"""No-cache independent signed-z Gram audit of the affine omega tilt.

This script imports neither discovery/source code nor serialized polynomial
data.  It constructs signed-z Gram columns first, forms the literal fully
conjugated Hermitian gate, substitutes the tilted sheet directly, and uses a
tau-first dense Bernstein transform rather than the source sparse pipeline.
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
    raise SystemExit("usage: independent referee accepts no arguments")

HERE = Path(__file__).resolve()
if (HERE.parent.name == "audit"
        and HERE.parent.parent.name == "research"
        and HERE.parents[2].name == "tmp"
        and HERE.parents[3].name == "certificate_workspace"):
    RELEASE_ROOT = HERE.parents[4]
elif (HERE.parent.name == "moving_sheet"
        and HERE.parent.parent.name == "certificates"):
    RELEASE_ROOT = HERE.parents[2]
else:
    raise RuntimeError("fail closed: unsupported packaged referee layout")
ROOT = (RELEASE_ROOT / "certificate_workspace").resolve()
if not ROOT.is_dir() or ROOT.parent != RELEASE_ROOT:
    raise RuntimeError("fail closed: packaged certificate workspace is missing")
DEPENDENCIES = {
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension.md":
        "e3f37ef598110eaad6c96a45eabff1e6313256923950057e8145568dbde865e0",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.py":
        "84587eef3507682eab241256444b559d3f800836001627d95831b10d4bb72cb8",
}
if os.environ.get("AFFINE_OMEGA_TILT_REFEREE_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"independent verification failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), f"dependency escapes package {relative}")
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def reduce_relations(expression, q, h, zsigned, S, Z):
    value = sp.expand(expression)
    value = sp.rem(value, q**2 - (1 - h**2), q)
    value = sp.rem(sp.expand(value), zsigned**2 - Z, zsigned)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    return sp.expand(value)


R, I = sp.Rational, sp.I
lam, S, x, y, Z = sp.symbols("lam S x y Z", real=True)
h, q, zsigned = sp.symbols("h q zsigned", real=True)
a, c = 1 / sp.sqrt(6), sp.sqrt(5) / sp.sqrt(6)
zeta = (4 + 3 * I) / 5
p = sp.Matrix([a, 0, c])
r0 = sp.Matrix([-a, 0, c * zeta])
fh = sp.Matrix([-c * h, q, -a * h * zeta])
U = sp.Matrix.hstack(r0, fh)
j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
ell = sp.sqrt(5) * zsigned / 3
C = sp.Matrix([
    [h**2, h * (j + I * kappa)],
    [h * (j - I * kappa), j**2 + kappa**2 + ell**2],
])
Hraw = sp.expand(U * C * sp.conjugate(U.T))
Qraw = sp.expand(lam * Hraw)
require(Hraw == sp.conjugate(Hraw.T), "Hermitian signed-z Gram reconstruction")

# Independently oriented kernel and literal signed-z rank checks.
kernel = sp.Matrix([
    c * q * sp.conjugate(zeta), h * sp.conjugate(zeta), a * q
])
require(sp.simplify(sp.conjugate(r0).dot(r0) - 1) == 0, "r0 norm")
require(reduce_relations(sp.conjugate(fh).dot(fh) - 1,
                         q, h, zsigned, S, Z) == 0, "fh norm")
require(sp.simplify(sp.conjugate(r0).dot(fh)) == 0,
        "frame orthogonality")
require(reduce_relations(sp.conjugate(kernel).dot(kernel) - 1,
                         q, h, zsigned, S, Z) == 0, "kernel norm")
require(sp.simplify(sp.conjugate(r0).dot(kernel)) == 0,
        "kernel/r0 orthogonality")
require(reduce_relations(sp.conjugate(fh).dot(kernel),
                         q, h, zsigned, S, Z) == 0,
        "kernel/fh orthogonality")
require(all(reduce_relations(entry, q, h, zsigned, S, Z) == 0
            for entry in Hraw * kernel), "one-dimensional kernel")
require(reduce_relations(sp.det(C) - R(5, 9) * S * Z,
                         q, h, zsigned, S, Z) == 0,
        "signed-z rank-two determinant")

# Fully conjugated literal original gate.
xi = sp.expand(Qraw * p)
Q2 = sp.expand(Qraw * Qraw)
leak1 = sp.expand(c * sp.conjugate(xi[0]) + a * xi[2]
                  + I * (a * c - Q2[2, 0]))
leak2 = sp.expand(c * sp.conjugate(xi[1]) - I * Q2[2, 1])
Gamma_direct = reduce_relations(sp.expand(
    4 * a**2 * modulus_square(xi[1])
    + modulus_square(leak1) + modulus_square(leak2)
    - 32 * a**2 * sp.re(xi[0])**2
), q, h, zsigned, S, Z)
require(not Gamma_direct.has(q, h, zsigned), "frame variables cancel")

# Different Gram-vector component order from the source.
v = sp.expand(Hraw * p)
H2 = sp.expand(Hraw * Hraw)
B0 = sp.Matrix([0, I * a * c, 0])
Lvec = sp.Matrix([
    2 * a * v[1],
    c * sp.conjugate(v[0]) + a * v[2],
    c * sp.conjugate(v[1]),
])
Mvec = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
Bvec = sp.expand(B0 + lam * Lvec + lam**2 * Mvec)
Gamma_gram = reduce_relations(sp.expand(
    sum(modulus_square(entry) for entry in Bvec)
    - 32 * a**2 * lam**2 * sp.re(v[0])**2
), q, h, zsigned, S, Z)
require(sp.expand(Gamma_direct - Gamma_gram) == 0,
        "literal Hermitian gate equals independent Gram-vector gate")
require(sp.Poly(36 * Gamma_direct, lam).degree() == 4,
        "scale quartic degree")
require(sp.Poly(36 * Gamma_direct, lam).nth(0) == 5,
        "compact normalization")
print("PASS independent signed-z Gram columns and original Hermitian gate")

# Direct affine substitution, not the source sparse map.
X, Mpar, omega, nu, useam = sp.symbols(
    "X Mpar omega nu useam", real=True
)
A = 1 + Mpar
Xmin, Xmax, Smax = R(1, 5), R(3, 13), R(1, 10000)
tilt = -R(10636, 275)
y0 = R(12, 25) / A + nu
omega_center = tilt * (X - Xmin)
physical_omega = omega + omega_center
base_w = (45 * Mpar + 18) / (25 * A) - R(3, 5) * X
Ysheet = S * y0
Wsheet = S * (base_w + physical_omega)
Zsheet = sp.factor(3 * X - X**2 - Ysheet**2 + Wsheet)
xsheet = -R(1, 5) + X
ysheet = R(3, 5) + Ysheet
require(sp.factor(xsheet**2 + ysheet**2 + Zsheet
                  - (R(2, 5) + R(13, 5) * X
                     + R(6, 5) * Ysheet + Wsheet)) == 0,
        "direct moving identity")

mapped = sp.cancel((36 * Gamma_direct).subs({
    lam: A / S, x: xsheet, y: ysheet, Z: Zsheet,
}))
Qhat_raw = sp.cancel(25**8 * A**8 * S**3 * mapped / S**2)
Qhat = sp.Poly(sp.expand(Qhat_raw), S, X, Mpar, omega, nu,
               domain=sp.QQ).as_expr()
require(sp.factor(mapped - Qhat / (25**8 * A**8 * S)) == 0,
        "lossless direct quotient identity")
SX = sp.Poly(Qhat, S, X)
terms = {
    (powers[0], powers[1]): sp.expand(coefficient)
    for powers, coefficient in SX.terms()
}
if os.environ.get("AFFINE_OMEGA_TILT_REFEREE_DROP_TERM") == "1":
    terms.pop(next(iter(terms)))
require(len(terms) == 22 and SX.degree(S) == 5 and SX.degree(X) == 4,
        "22-term bidegree-(5,4) direct quotient")
first_expected = 25**8 * Mpar**2 * A**8 * (
    5 * Mpar**2 + 14 * Mpar + 14
)
require(sp.expand(terms.pop((1, 0)) - first_expected) == 0,
        "independent nonnegative M^2 first layer")
higher = {key: value for key, value in terms.items() if sum(key) > 2}
require(len(higher) == 18, "18 direct higher terms")
require(sum(len(sp.Poly(value, Mpar, omega, nu).terms())
            for value in higher.values()) == 1013,
        "1013 direct centered monomials")

# Different-order no-cache tensor transform: dense tau transform first, then u.
sigma_max = sp.factor(Smax / Xmin)
require(sigma_max == R(1, 2000), "lossless sigma maximum")
tau = sp.symbols("tau", real=True)
Xaff = Xmin + (Xmax - Xmin) * useam
require(Xaff.subs(useam, 0) == Xmin, "exact X=1/5 seam")
require(Xaff.subs(useam, 1) == Xmax, "exact X=3/13 endpoint")
qcore = sp.expand(sum(
    coefficient * S**sd * X**xd
    for (sd, xd), coefficient in terms.items()
))
affine_power = sp.Poly(sp.expand(qcore.subs({
    X: Xaff, S: sigma_max * tau * Xaff,
})), tau, useam)
dt, du = affine_power.degree(tau), affine_power.degree(useam)
require((dt, du) == (5, 7), "direct affine bidegree")
power = [[affine_power.coeff_monomial(tau**k * useam**ell)
          for ell in range(du + 1)] for k in range(dt + 1)]
tau_stage = [[sum(
    sp.Rational(sp.binomial(i, k), sp.binomial(dt, k)) * power[k][ell]
    for k in range(i + 1)
) for ell in range(du + 1)] for i in range(dt + 1)]
controls = {(i, j): sp.factor(sum(
    sp.Rational(sp.binomial(j, ell), sp.binomial(du, ell))
    * tau_stage[i][ell]
    for ell in range(j + 1)
)) for i in range(dt + 1) for j in range(du + 1)}
require(len(controls) == 48, "48 direct tensor controls")

Mcap, small = R(1, 1000), R(1, 100)


def centered_abs(expression):
    polynomial = sp.Poly(sp.expand(expression), Mpar, omega, nu, domain=sp.QQ)
    return sp.factor(sum(
        abs(coefficient) * Mcap**powers[0]
        * small**powers[1] * small**powers[2]
        for powers, coefficient in polynomial.terms()
    ))


def centered_lower(expression):
    center = sp.expand(expression).subs({Mpar: 0, omega: 0, nu: 0})
    return sp.factor(center - centered_abs(sp.expand(expression - center)))


lowers = {key: centered_lower(value) for key, value in controls.items()}
minimum_index, reserve = min(lowers.items(), key=lambda item: item[1])
expected_reserve = R(
    2564950982194530478444050838857341987999,
    31850496000000000000000000000,
)
require(all(value > 0 for value in lowers.values()),
        "independent 48/48 strict controls")
require(minimum_index == (0, 0) and reserve == expected_reserve,
        "independent exact decisive reserve")
print("PASS direct 22/18/1013 quotient and 48/48 strict controls")

# Independently ordered legality proof and endpoint obstruction.
Amin, Amax = 1 - Mcap, 1 + Mcap
require(Amin == R(999, 1000) > 0, "positive A")
y0min = sp.factor(y0.subs({Mpar: Mcap, nu: -small}))
y0max = sp.factor(y0.subs({Mpar: -Mcap, nu: small}))
require(y0min > 0, "positive y center")
b = sp.factor(base_w + physical_omega)
require(sp.factor(sp.diff(b, Mpar)) == R(27, 25) / A**2,
        "independent b M monotonicity")
require(sp.factor(sp.diff(b, X)) == tilt - R(3, 5),
        "independent b X monotonicity")
bmin = sp.factor(b.subs({X: Xmax, Mpar: -Mcap, omega: -small}))
bmax = sp.factor(b.subs({X: Xmin, Mpar: Mcap, omega: small}))
zlower = sp.factor(3 * Xmin - Xmin**2 + Smax * bmin - Smax**2 * y0max**2)
zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * bmax)
require(bmin == R(-1639111, 2645500), "independent bmin")
require(zlower == R(
    8879008598718934873, 15857127000000000000
) > 0, "independent Z lower")
require(zupper == R(8316795197, 13013000000) < 1,
        "independent Z upper")

T = sp.factor(R(6, 5) * y0 + b)
danger = sp.factor(R(3, 5) - R(13, 5) * X - S * T)
require(sp.factor(1 - xsheet**2 - ysheet**2 - Zsheet - danger) == 0,
        "direct danger equality")
require(sp.factor(sp.diff(T, Mpar)) == R(63, 125) / A**2,
        "independent T M monotonicity")
require(sp.factor(sp.diff(T, omega)) == 1
        and sp.factor(sp.diff(T, nu)) == R(6, 5),
        "independent centered monotonicity")
require(sp.factor(sp.diff(T, X)) == tilt - R(3, 5),
        "independent T X monotonicity")
Tmax = sp.factor(T.subs({Mpar: Mcap, omega: small, nu: small}))
require(Tmax.subs(X, Xmax) == -R(1, 100), "endpoint T maximum")
Fworst = sp.factor(
    R(3, 5) - R(13, 5) * X - Smax * (Tmax + R(1, 100))
)
require(Fworst.subs(X, Xmax) == 0 and sp.diff(Fworst, X) < 0,
        "independent D>=S/100 envelope")
endpoint_formula = sp.factor(danger.subs({
    X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
require(endpoint_formula == S / 100, "sharp endpoint danger formula")
epsilon = sp.symbols("epsilon", positive=True)
limit_tail = sp.factor(sp.limit(danger, S, 0, dir="+").subs(
    X, Xmax + epsilon
))
require(limit_tail == -R(13, 5) * epsilon,
        "independent X>3/13 small-scale obstruction")
require(Smax < 1 and 25**8 * Amin**8 * Smax > 0,
        "real frame and positive clearing factors")
print("PASS independent lambda/Z/rank/signed-z and D>=S/100 legality")
print("PASS independent X>3/13 S->0 obstruction")

# Direct exact grid, with the order reversed relative to the source.
records = []
for nv, ov, Mv, uv, Sv in product(
    (-small, small), (-small, small), (-Mcap, Mcap),
    (R(1), R(1, 2), R(0)), (Smax, R(1, 20000), R(1, 1000000)),
):
    value = sp.factor(mapped.subs({
        S: Sv, X: Xaff.subs(useam, uv), Mpar: Mv, omega: ov, nu: nv,
    }))
    Zv = sp.factor(Zsheet.subs({
        S: Sv, X: Xaff.subs(useam, uv), Mpar: Mv, omega: ov, nu: nv,
    }))
    danger_v = sp.factor(danger.subs({
        S: Sv, X: Xaff.subs(useam, uv), Mpar: Mv, omega: ov, nu: nv,
    }))
    det_v = sp.factor(R(5, 9) * Sv * Zv)
    require(value > 0 and 0 < Zv < 1 and danger_v > 0 and det_v > 0,
            "independent exact legal gate node")
    records.append((value, Sv, uv, Mv, ov, nv, Zv, danger_v, det_v))
require(len(records) == 72, "72 independent exact nodes")
minimum = min(records)
left = sp.factor(mapped.subs({
    S: Smax, X: Xmin, Mpar: -Mcap, omega: -small, nu: -small,
}))
right = sp.factor(mapped.subs({
    S: Smax, X: Xmax, Mpar: -Mcap, omega: -small, nu: -small,
}))
danger_gate = sp.factor(mapped.subs({
    S: Smax, X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
danger_Z = sp.factor(Zsheet.subs({
    S: Smax, X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
danger_det = sp.factor(R(5, 9) * Smax * danger_Z)
require(left == R(
    213355344357890421512795094325969057679,
    40000000000000000000000000000000000,
) > 0, "independent left seam gate")
require(right == R(
    184421770823082033734271204948812328298851568079,
    16726464040000000000000000000000000000000000,
) > 0, "independent right endpoint gate")
require(danger_gate == R(
    2875017794276661652931485545294665330527919,
    262440000000000000000000000000000000000,
) > 0, "independent endpoint danger gate")
require(danger_Z == R(
    640272135596701999, 1002001000000000000
) and danger_det == R(
    640272135596701999, 18036018000000000000000
), "independent endpoint rank data")
require(minimum[0] == left, "independent exact grid minimum")
print("PASS independent seam/endpoint data and 72/72 legal nodes")

print("TILT_SLOPE", tilt)
print("QUOTIENT_COUNTS", 22, 18, 1013)
print("BERNSTEIN_DEGREE", (dt, du))
print("BERNSTEIN_CONTROLS", len(controls))
print("STRICT_RESERVE", reserve)
print("Z_LOWER", zlower)
print("Z_UPPER", zupper)
print("ENDPOINT_TMAX", Tmax.subs(X, Xmax))
print("ENDPOINT_DANGER", endpoint_formula.subs(S, Smax))
print("LEFT_SEAM_36GAMMA", left)
print("RIGHT_ENDPOINT_36GAMMA", right)
print("REFEREE_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT independent exact tilted gate on closed 1/5<=X<=3/13")
print("SCOPE moving-sheet partial theorem; compact ball/common metric/fixed lens open")
