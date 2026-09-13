#!/usr/bin/env python3
"""Fail-closed independent referee for the inward-Z affine-omega sheet.

The discovery program and its polynomial tables are never imported, executed,
parsed, or evaluated.  This verifier reconstructs the signed-z Gram columns,
the fully conjugated Q,Q^2 gate, the inward sheet, and every Bernstein control
from the definitions.  Its Gram-vector component order and its u-first tensor
Bernstein conversion differ from the source-certificate implementation.
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
    raise SystemExit("usage: inward-Z independent referee accepts no arguments")

ROOT = Path(__file__).resolve().parents[3]
DEPENDENCIES = {
    "tmp/research/compact_ball_inward_z_tilt_discovery.py":
        "6ee91b88c1835f44183a8da833239c817cdd6d079d73cd5b9e9c42428661f6ca",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_source_candidate.md":
        "7b78d77ef418de755f41d8fcbd7b8aaa15eae1b1052276fe1a90274c1989e563",
    "tmp/research/compact_ball_inward_z_tilt_source_freeze_manifest.sha256":
        "dddb1e18ed0e0972d75d7099ccc75409f7ac609db9bead51a61046ff3f05d614",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.md":
        "bd127112e0cd59e9f0ed8c565480a612c2c75ba83edd979c3552896b18395067",
}
if os.environ.get("INWARD_Z_REFEREE_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"independent verification failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing frozen dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")
print("PASS frozen source and analytic dependency hashes")


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

# Signed-z columns in (f_h,r) order, rather than the source's (r,f_h) order.
rcol = sp.Matrix([-a, 0, c * zeta])
fcol = sp.Matrix([-c * h, q, -a * h * zeta])
U = sp.Matrix.hstack(fcol, rcol)
j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
ell = sp.sqrt(5) * zsigned / 3
# The compression is conjugated by the same permutation as the columns.
C = sp.Matrix([
    [j**2 + kappa**2 + ell**2, h * (j - I * kappa)],
    [h * (j + I * kappa), h**2],
])
Hraw = sp.expand(U * C * sp.conjugate(U.T))
Qraw = sp.expand(lam * Hraw)
require(Hraw == sp.conjugate(Hraw.T), "Hermitian signed-z Gram reconstruction")

# Orthonormal frame and signed-rank checks reconstructed from definitions.
ncol = sp.Matrix([c * q * sp.conjugate(zeta),
                  h * sp.conjugate(zeta), a * q])
require(sp.simplify(sp.conjugate(rcol).dot(rcol) - 1) == 0, "r norm")
require(reduce_relations(sp.conjugate(fcol).dot(fcol) - 1,
                         q, h, zsigned, S, Z) == 0, "f norm")
require(sp.simplify(sp.conjugate(rcol).dot(fcol)) == 0,
        "r/f orthogonality")
require(reduce_relations(sp.conjugate(ncol).dot(ncol) - 1,
                         q, h, zsigned, S, Z) == 0, "kernel norm")
require(sp.simplify(sp.conjugate(rcol).dot(ncol)) == 0,
        "r/kernel orthogonality")
require(reduce_relations(sp.conjugate(fcol).dot(ncol),
                         q, h, zsigned, S, Z) == 0,
        "f/kernel orthogonality")
require(all(reduce_relations(entry, q, h, zsigned, S, Z) == 0
            for entry in Hraw * ncol), "one-dimensional kernel")
require(reduce_relations(sp.det(C) - R(5, 9) * S * Z,
                         q, h, zsigned, S, Z) == 0,
        "signed-z rank-two determinant")

# Literal, fully conjugated original Hermitian scalar gate.
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
require(not Gamma_direct.has(q, h, zsigned),
        "signed frame variables and z sign cancel")

# Independent decomposition with cyclic component order (third, first, second).
v = sp.expand(Hraw * p)
H2 = sp.expand(Hraw * Hraw)
Bcyc = sp.Matrix([-I * H2[2, 1], 0, -I * H2[2, 0]])
Lcyc = sp.Matrix([
    c * sp.conjugate(v[1]),
    2 * a * v[1],
    c * sp.conjugate(v[0]) + a * v[2],
])
Kcyc = sp.Matrix([0, 0, I * a * c])
gram_vector = sp.expand(Kcyc + lam * Lcyc + lam**2 * Bcyc)
Gamma_gram = reduce_relations(sp.expand(
    sum(modulus_square(entry) for entry in gram_vector)
    - 32 * a**2 * lam**2 * sp.re(v[0])**2
), q, h, zsigned, S, Z)
require(sp.expand(Gamma_direct - Gamma_gram) == 0,
        "literal Q,Q^2 gate equals cyclic Gram-vector gate")
require(sp.Poly(36 * Gamma_direct, lam).degree() == 4,
        "scale quartic degree")
require(sp.Poly(36 * Gamma_direct, lam).nth(0) == 5,
        "compact normalization")
print("PASS independent signed-z/Q/Q^2 reconstruction and cyclic Gram identity")

# Direct inward-Z substitution.  The predecessor is reconstructed only as a
# formula and compared symbolically at X=3/13; no predecessor code is imported.
X, Mpar, omega, nu, u = sp.symbols("X Mpar omega nu u", real=True)
A = 1 + Mpar
Xmin, Xmax, Smax = R(3, 13), R(1, 4), R(1, 10000)
Mcap, small = R(1, 1000), R(1, 100)
tilt = -R(10636, 275)
y0 = R(12, 25) / A + nu
omega_phys = omega + tilt * (X - R(1, 5))
b = (45 * Mpar + 18) / (25 * A) - R(3, 5) * X + omega_phys
xsheet = -R(1, 5) + X
ysheet = R(3, 5) + S * y0
Z_v12 = sp.factor(3 * X - X**2 + S * b - S**2 * y0**2)
Zsheet = sp.factor(Z_v12 - 3 * (X - Xmin))
require(sp.factor(Zsheet - (R(9, 13) - X**2 + S*b - S**2*y0**2)) == 0,
        "inward-Z equivalent formula")
require(sp.factor((Zsheet - Z_v12).subs(X, Xmin)) == 0,
        "parameter-by-parameter predecessor seam")
predecessor_tuple = (A/S, -R(1, 5)+X, R(3, 5)+S*y0, b, Z_v12)
inward_tuple = (A/S, xsheet, ysheet, b, Zsheet)
require(all(sp.factor((new-old).subs(X, Xmin)) == 0
            for old, new in zip(predecessor_tuple, inward_tuple)),
        "full lambda/x/y/b/Z parameter-by-parameter predecessor seam")

mapped = sp.cancel((36 * Gamma_direct).subs({
    lam: A / S, x: xsheet, y: ysheet, Z: Zsheet,
}))
Qhat_raw = sp.cancel(25**8 * A**8 * S**3 * mapped)
Qhat = sp.Poly(sp.expand(Qhat_raw), S, X, Mpar, omega, nu,
               domain=sp.QQ).as_expr()
require(sp.factor(mapped - Qhat / (25**8 * A**8 * S**3)) == 0,
        "lossless direct cleared quotient")
SX = sp.Poly(Qhat, S, X)
terms = {(powers[0], powers[1]): sp.expand(coefficient)
         for powers, coefficient in SX.terms()}
require(len(terms) == 32 and SX.degree(S) == 7 and SX.degree(X) == 4,
        "32-term bidegree-(7,4) direct quotient")
first_layer = S**3 * 25**8 * Mpar**2 * A**8 * (
    5 * Mpar**2 + 14 * Mpar + 14
)
require(sp.factor(5*Mpar**2 + 14*Mpar + 14
                  - (5*(Mpar + R(7, 5))**2 + R(21, 5))) == 0,
        "manifestly positive first layer factor")
qcore = sp.expand(Qhat - first_layer)
core_sx = sp.Poly(qcore, S, X)
core_terms = {(powers[0], powers[1]): sp.expand(coefficient)
              for powers, coefficient in core_sx.terms()}
if os.environ.get("INWARD_Z_REFEREE_DROP_TERM") == "1":
    key = sorted(core_terms)[0]
    core_terms.pop(key)
    qcore = sp.expand(sum(coefficient * S**sd * X**xd
                         for (sd, xd), coefficient in core_terms.items()))
require(len(core_terms) == 32, "32 direct core coefficients")
require(sum(len(sp.Poly(value, Mpar, omega, nu).terms())
            for value in core_terms.values()) == 1581,
        "1581 centered core monomials")
print("PASS direct quotient/core counts 32/32/1581 and bidegree (7,4)")

# Exact rectangle enlargement and u-first, tau-second dense Bernstein map.
tau = sp.symbols("tau", real=True)
Xaff = Xmin + u / 52
sigma = R(13, 30000)
require(Xaff.subs(u, 0) == Xmin and Xaff.subs(u, 1) == Xmax,
        "exact seam-to-X=1/4 affine map")
require(sp.factor(Smax / Xmin) == sigma,
        "lossless scale-to-X enlargement")
affine_power = sp.Poly(sp.expand(qcore.subs({
    X: Xaff, S: sigma * tau * Xaff,
})), tau, u)
dt, du = affine_power.degree(tau), affine_power.degree(u)
require((dt, du) == (7, 9), "direct affine bidegree (7,9)")
power = [[affine_power.coeff_monomial(tau**i * u**j)
          for j in range(du + 1)] for i in range(dt + 1)]
# First convert every tau-power row in u; then convert each u-control column
# in tau.  This order is independent of the source's nested sparse map.
u_stage = [[sum(
    sp.Rational(sp.binomial(j, ell), sp.binomial(du, ell)) * power[i][ell]
    for ell in range(j + 1)
) for j in range(du + 1)] for i in range(dt + 1)]
controls = {(i, j): sp.factor(sum(
    sp.Rational(sp.binomial(i, k), sp.binomial(dt, k)) * u_stage[k][j]
    for k in range(i + 1)
)) for i in range(dt + 1) for j in range(du + 1)}
require(len(controls) == 80, "80 independently transformed controls")


def centered_abs(expression):
    poly = sp.Poly(sp.expand(expression), Mpar, omega, nu, domain=sp.QQ)
    return sp.factor(sum(
        abs(coefficient) * Mcap**powers[0]
        * small**powers[1] * small**powers[2]
        for powers, coefficient in poly.terms()
    ))


def centered_lower(expression):
    center = sp.expand(expression).subs({Mpar: 0, omega: 0, nu: 0})
    return sp.factor(center - centered_abs(sp.expand(expression - center)))


lowers = {key: centered_lower(value) for key, value in controls.items()}
zero_indices = sorted(key for key, value in lowers.items() if value == 0)
strict = {key: value for key, value in lowers.items() if value > 0}
require(zero_indices == [(0, 0), (0, 1), (1, 0)],
        "exactly three artificial closure zero controls")
require(len(strict) == 77 and all(value > 0 for value in strict.values()),
        "remaining 77 controls strictly positive")
minimum_index, reserve = min(strict.items(), key=lambda item: item[1])
expected_reserve = R(
    10071067674014002577317165966399410637259618083,
    128416777961472000000000000000000000000000000,
)
require(minimum_index == (2, 0) and reserve == expected_reserve,
        "same exact strict reserve R* at control (2,0)")

# Independent polynomial check of the positive-row Bernstein weight.
Wsum = sp.expand(sum(sp.binomial(7, i) * tau**i * (1-tau)**(7-i)
                     for i in range(2, 8)))
Wclosed = sp.expand(1 - (1-tau)**7 - 7*tau*(1-tau)**6)
require(sp.expand(Wsum - Wclosed) == 0, "exact row-weight identity")
require(sp.expand(Wsum.subs(tau, 1) - 1) == 0, "W(1)=1")
require(sp.binomial(7, 2) > 0, "strict positive i=2 summand on 0<tau<1")
print("PASS 80 controls: three closure zeros, 77 strict, identical R* and W")

# Continuum legality, reconstructed through monotonic endpoint bounds.
Amin = 1 - Mcap
require(Amin == R(999, 1000) > 0, "lambda positive")
y0min = sp.factor(y0.subs({Mpar: Mcap, nu: -small}))
y0max = sp.factor(y0.subs({Mpar: -Mcap, nu: small}))
require((y0min, y0max) == (R(46999, 100100), R(16333, 33300)),
        "exact y0 interval")
require(sp.factor(sp.diff(b, Mpar)) == R(27, 25) / A**2,
        "b monotone in M")
require(sp.factor(sp.diff(b, X)) == tilt - R(3, 5),
        "b monotone in X")
bmin = sp.factor(b.subs({X: Xmax, Mpar: -Mcap, omega: -small}))
bmax = sp.factor(b.subs({X: Xmin, Mpar: Mcap, omega: small}))
require((bmin, bmax) == (R(-69948, 50875), R(-299011, 500500)),
        "exact b interval")
zlower = sp.factor(R(9, 13) - Xmax**2 + Smax*bmin - Smax**2*y0max**2)
zupper_strict = sp.factor(R(9, 13) - Xmin**2)
require(zlower == R(
    9984760329129934873, 15857127000000000000
) > 0, "exact Z lower")
require(zupper_strict == R(108, 169) < 1, "strict Z upper supremum")

T = sp.factor(R(6, 5) * y0 + b)
danger = sp.factor(1 - xsheet**2 - ysheet**2 - Zsheet)
danger_formula = sp.factor(R(2, 5)*(X-Xmin) - S*T)
require(sp.factor(danger - danger_formula) == 0, "exact inward danger formula")
require(sp.factor(sp.diff(T, Mpar)) == R(63, 125)/A**2,
        "T monotone in M")
require(sp.factor(sp.cancel(sp.diff(T, omega))) == 1
        and sp.factor(sp.cancel(sp.diff(T, nu))) == R(6, 5),
        "T centered monotonicity")
require(sp.factor(sp.diff(T, X)) == tilt - R(3, 5),
        "T decreases in X")
Tmax_seam = sp.factor(T.subs({X: Xmin, Mpar: Mcap,
                              omega: small, nu: small}))
require(Tmax_seam == -R(1, 100), "seam T maximum")
worst_gap = sp.factor((
    danger_formula - (R(2, 5)*(X-Xmin) + S/R(100))
).subs({Mpar: Mcap, omega: small, nu: small}))
require(worst_gap == R(10801, 3575) * S * (13*X - 3),
        "exact nonnegative danger lower envelope")
require(25**8 * Amin**8 * Smax**3 > 0, "positive clearing factor")
print("PASS continuum lambda/Z/danger/rank-two legality for both z signs")

# 72 exact rational falsification nodes in a different loop order.
Xmid = R(25, 104)
records = []
for nv, ov, Mv, Xv, Sv in product(
    (-small, small), (-small, small), (-Mcap, Mcap),
    (Xmax, Xmid, Xmin), (Smax, R(1, 20000), R(1, 1000000)),
):
    subs = {S: Sv, X: Xv, Mpar: Mv, omega: ov, nu: nv}
    value = sp.factor(mapped.subs(subs))
    Zv = sp.factor(Zsheet.subs(subs))
    Dv = sp.factor(danger.subs(subs))
    detv = sp.factor(R(5, 9) * Sv * Zv)
    require(value > 0 and 0 < Zv < 1 and Dv > 0 and detv > 0,
            "exact legal raw-gate node")
    records.append((value, Sv, Xv, Mv, ov, nv, Zv, Dv, detv))
require(len(records) == 72, "72 exact rational nodes")
minimum = min(records, key=lambda row: row[0])
expected_node_min = R(
    182249907370437372958214245586018359494715888079,
    16726464040000000000000000000000000000000000,
)
require(minimum[:6] == (expected_node_min, Smax, Xmin,
                        -Mcap, small, -small),
        "same exact nodal minimum and location")
require(min(row[7] for row in records) == R(1, 100000000),
        "smallest nodal danger 1e-8")
print("PASS independent 72/72 exact legal raw-gate nodes")

print("SOURCE_HASH", DEPENDENCIES["tmp/research/compact_ball_inward_z_tilt_discovery.py"])
print("QUOTIENT_COUNTS", len(terms), len(core_terms), 1581)
print("BERNSTEIN_DEGREE", (dt, du))
print("BERNSTEIN_CONTROLS", len(controls), len(zero_indices), len(strict))
print("ZERO_CONTROLS", zero_indices)
print("STRICT_RESERVE", reserve)
print("Z_LOWER", zlower)
print("Z_UPPER_STRICT", zupper_strict)
print("GRID_MIN_36GAMMA", minimum[0])
print("REFEREE_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT independently audited inward-Z partial theorem")
print("SCOPE full compact ball/common metric/fixed lens remain open")
