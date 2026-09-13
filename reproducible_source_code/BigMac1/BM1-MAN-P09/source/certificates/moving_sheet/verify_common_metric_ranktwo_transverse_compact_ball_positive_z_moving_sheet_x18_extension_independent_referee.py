#!/usr/bin/env python3
"""No-cache independent Gram audit for the moving-sheet X18 cell.

This script imports neither discovery/source code nor serialized polynomial
data.  It reconstructs the signed-z Gram columns, the literal Hermitian gate,
a differently ordered Gram-vector gate, and the continuum certificate by a
direct affine-power expansion rather than the source verifier's sparse map.
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
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.md":
        "cac9bdfdc7fddebfc31ff110bd77d5cfa79360e8fbc7a0ec3c9f04f90e5a9142",
    "tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.py":
        "dc4d586680587a369478154b5273b43b55e598c5bdb5451578df3592c0cea29b",
}
if os.environ.get("X18_REFEREE_BAD_DEPENDENCY") == "1":
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
require(Hraw == sp.conjugate(Hraw.T), "Hermitian Gram reconstruction")

# Independent kernel orientation and signed-z frame checks.
kernel = sp.Matrix([c * q * sp.conjugate(zeta),
                    h * sp.conjugate(zeta), a * q])
require(sp.simplify(sp.conjugate(r0).dot(r0) - 1) == 0, "r0 norm")
require(reduce_relations(sp.conjugate(fh).dot(fh) - 1,
                         q, h, zsigned, S, Z) == 0, "fh norm")
require(sp.simplify(sp.conjugate(r0).dot(fh)) == 0, "frame orthogonality")
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
        "rank-two determinant")

# Literal fully conjugated original gate.
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
require(not Gamma_direct.has(q, h, zsigned), "radicals cancel")

# Independent Gram-vector ordering: constant/linear/quadratic components are
# permuted relative to the source verifier.
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
        "original gate equals independent Gram-vector gate")
require(sp.Poly(36 * Gamma_direct, lam).degree() == 4,
        "scale quartic degree")
require(sp.Poly(36 * Gamma_direct, lam).nth(0) == 5,
        "compact normalization")
print("PASS independent signed-z Gram columns and original Hermitian gate")

# Exact moving sheet and seam-preserving affine coordinate.
X, Mpar, omega, nu, useam = sp.symbols(
    "X Mpar omega nu useam", real=True
)
A = 1 + Mpar
y0 = R(12, 25) / A + nu
wc = -3 * (5 * Mpar * X - 15 * Mpar + 5 * X - 6) / (25 * A)
Ysheet = S * y0
Wsheet = S * (wc + omega)
Zsheet = sp.factor(3 * X - X**2 - Ysheet**2 + Wsheet)
xsheet = -R(1, 5) + X
ysheet = R(3, 5) + Ysheet
require(sp.factor(xsheet**2 + ysheet**2 + Zsheet
                  - (R(2, 5) + R(13, 5) * X
                     + R(6, 5) * Ysheet + Wsheet)) == 0,
        "moving danger identity")
X_from_u = (18 + useam) / 342
require(X_from_u.subs(useam, 0) == R(1, 19), "closed predecessor seam")
require(X_from_u.subs(useam, 1) == R(1, 18), "closed right endpoint")

# Direct affine-power quotient, rather than the source sparse substitution.
mapped = sp.cancel((36 * Gamma_direct).subs({
    lam: A / S, x: xsheet, y: ysheet, Z: Zsheet,
}))
Qhat_raw = sp.cancel(25**8 * A**8 * S**3 * mapped / S**2)
Qhat = sp.Poly(sp.expand(Qhat_raw), S, X, Mpar, omega, nu,
               domain=sp.QQ).as_expr()
require(sp.factor(mapped - Qhat / (25**8 * A**8 * S)) == 0,
        "lossless quotient identity")
SX = sp.Poly(Qhat, S, X)
terms = {(powers[0], powers[1]): sp.expand(coefficient)
         for powers, coefficient in SX.terms()}
require(len(terms) == 20 and SX.degree(S) == 5 and SX.degree(X) == 4,
        "20-term bidegree-(5,4) quotient")
first = 25**8 * Mpar**2 * A**8 * (5 * Mpar**2 + 14 * Mpar + 14)
require(sp.expand(terms[(1, 0)] - first) == 0,
        "nonnegative first layer")
if os.environ.get("X18_REFEREE_DROP_TERM") == "1":
    terms.pop(next(iter(terms)))
require(len(terms) == 20, "complete term set")

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


a0, b0, c0 = map(centered_lower,
                  (terms[(2, 0)], terms[(1, 1)], terms[(0, 2)]))
require(a0 > 0 and b0 > 0 and c0 > 0, "positive quadratic core")
expected_c0 = R(
    2564950982194530478444050838857341987999,
    1274019840000000000000000000,
)
require(c0 == expected_c0, "exact c0")
higher = {key: coefficient for key, coefficient in terms.items()
          if sum(key) > 2}
require(len(higher) == 16, "sixteen higher terms")
require(sum(len(sp.Poly(coefficient, Mpar, omega, nu).terms())
            for coefficient in higher.values()) == 947,
        "947 centered monomials")
Smax, Xmin, Xmax = R(1, 10000), R(1, 19), R(1, 18)
sigma_max = sp.factor(Smax / Xmin)
require(sigma_max == R(19, 10000), "lossless sigma bound")
Rabs = sp.factor(sum(
    centered_abs(coefficient) * sigma_max**i * Xmax**(i + j - 2)
    for (i, j), coefficient in higher.items()
))
expected_Rabs = R(
    276675774066955888671433955119085619971144287904209914384809259360019,
    100306130042880000000000000000000000000000000000000000000000,
)
reserve = sp.factor(c0 - Rabs)
expected_reserve = R(
    201667044956072817740185576689797163779166123712095790085615190740639981,
    100306130042880000000000000000000000000000000000000000000000,
)
require(Rabs == expected_Rabs, "independent exact remainder")
require(reserve == expected_reserve and reserve > 0,
        "independent strict continuum reserve")
print("PASS no-cache direct quotient and strict continuum reserve")

# Independent legality from derivative/endpoint choices.
Amin, Amax = R(999, 1000), R(1001, 1000)
y0min = sp.factor(R(12, 25) / Amax - small)
y0max = sp.factor(R(12, 25) / Amin + small)
require(y0min == R(46999, 100100) > 0, "y0 lower")
require(sp.factor(sp.diff(wc, X)) == -R(3, 5), "wc X monotonicity")
require(sp.factor(sp.diff(wc, Mpar)) == 27 / (25 * A**2),
        "wc M monotonicity")
wlower = sp.factor(wc.subs({X: Xmax, Mpar: -Mcap}) - small)
wupper = sp.factor(wc.subs({X: Xmax, Mpar: Mcap}) + small)
require(wlower == R(7499, 11100), "wc lower")
require(wupper == R(209533, 300300), "wc upper")
zslope = sp.factor(wlower - Smax * y0max**2)
zbase = sp.factor(3 * Xmin - Xmin**2)
zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * wupper)
danger = sp.factor(R(3, 5) - R(13, 5) * Xmax
                   - R(6, 5) * Smax * y0max - Smax * wupper)
require(zslope == R(7491234233111, 11088900000000) > 0, "Z slope")
require(zbase == R(56, 361) > R(1, 8), "Z lower")
require(zupper == R(13268907391, 81081000000) < R(1, 6), "Z upper")
require(danger == R(759044113187, 1666665000000) > 0, "strict danger")
print("PASS lambda, signed z, danger, determinant, rank two, and closed seam")

# Exact seam/endpoints and 72 rational falsification nodes.
sample_S = (Smax, R(1, 20000), R(1, 1000000))
sample_u = (R(0), R(1, 2), R(1))
records = []
for Sv, uv, Mv, ov, nv in product(
    sample_S, sample_u, (-Mcap, Mcap), (-small, small), (-small, small)
):
    Xv = X_from_u.subs(useam, uv)
    value = sp.factor(mapped.subs({
        S: Sv, X: Xv, Mpar: Mv, omega: ov, nu: nv,
    }))
    Zv = sp.factor(Zsheet.subs({
        S: Sv, X: Xv, Mpar: Mv, omega: ov, nu: nv,
    }))
    danger_v = sp.factor((1 - xsheet**2 - ysheet**2 - Zsheet).subs({
        S: Sv, X: Xv, Mpar: Mv, omega: ov, nu: nv,
    }))
    require(value > 0 and Zv > 0 and danger_v > 0,
            "legal positive exact node")
    records.append((value, Sv, uv, Mv, ov, nv, Zv, danger_v))
require(len(records) == 72, "72 falsification nodes")
minimum = min(records)
left = sp.factor(mapped.subs({
    S: Smax, X: Xmin, Mpar: -Mcap, omega: -small, nu: -small,
}))
right = sp.factor(mapped.subs({
    S: Smax, X: Xmax, Mpar: -Mcap, omega: -small, nu: -small,
}))
require(left == R(
    1941635149051525232795626443278240808984959,
    5212840000000000000000000000000000000000,
) > 0, "left seam gate")
require(right == R(
    16590441965844177687836029861184257679,
    40000000000000000000000000000000000,
) > 0, "right endpoint gate")
require(minimum[0] > 0, "strict exact falsification minimum")

print("PASS endpoint/seam values and 72 exact legal falsification nodes")
print("STRICT_RESERVE", reserve)
print("Z_UPPER", zupper)
print("DANGER_RESERVE", danger)
print("LEFT_SEAM_36GAMMA", left)
print("RIGHT_ENDPOINT_36GAMMA", right)
print("REFEREE_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT independent exact positivity on 1/19<=X<=1/18")
print("SCOPE moving-sheet partial theorem; full compact ball remains open")
