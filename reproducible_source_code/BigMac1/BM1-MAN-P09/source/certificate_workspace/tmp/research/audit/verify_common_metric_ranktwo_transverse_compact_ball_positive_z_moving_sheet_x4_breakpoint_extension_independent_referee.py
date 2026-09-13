#!/usr/bin/env python3
"""No-cache independent Gram audit for the maximal X4 danger breakpoint.

This script imports neither discovery/source code nor serialized polynomial
data.  It reconstructs the signed-z Gram columns, the literal Hermitian gate,
a differently ordered Gram-vector gate, and the continuum certificate by a
direct affine-power expansion rather than the source verifier's sparse map.
It checks the actual compact-ball chart prerequisites directly and does not
inherit the predecessor's merely descriptive bound `Z<1/6`.
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
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension.md":
        "a86dbe3eea4d9bfaf2772383407e65a5960e6941344713377068ff048ffc5f4d",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension.py":
        "137765b9fe8afe9feaf51b8a71caa069908fc04ffd1eee4fac48b4b15da77289",
}
if os.environ.get("X4_BREAKPOINT_REFEREE_BAD_DEPENDENCY") == "1":
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
Xstar = R(428905727, 1858957100)
X_from_u = R(1, 5) + (Xstar - R(1, 5)) * useam
require(X_from_u.subs(useam, 0) == R(1, 5), "closed predecessor seam")
require(X_from_u.subs(useam, 1) == Xstar, "closed gate breakpoint")

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
if os.environ.get("X4_BREAKPOINT_REFEREE_DROP_TERM") == "1":
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
Smax, Xmin, Xmax = R(1, 10000), R(1, 5), Xstar
sigma_max = sp.factor(Smax / Xmin)
require(sigma_max == R(1, 2000), "lossless sigma bound")
Rabs = sp.factor(sum(
    centered_abs(coefficient) * sigma_max**i * Xmax**(i + j - 2)
    for (i, j), coefficient in higher.items()
))
expected_Rabs = R(
    311837602694763856953654581992404505154268305263846785274456274343807875982376092575027407,
    103541941206646325492097536439091200000000000000000000000000000000000000000000000,
)
reserve = sp.factor(c0 - Rabs)
expected_reserve = R(
    208146457517980767271040318929344719831500991336682480497608668045656192124017623907424972593,
    103541941206646325492097536439091200000000000000000000000000000000000000000000000,
)
require(Rabs == expected_Rabs, "independent exact remainder")
require(reserve == expected_reserve and reserve > 0,
        "independent strict continuum reserve")
print("PASS no-cache direct quotient and strict continuum reserve")

# Independent legality and equality classification from the coupled danger.
Amin, Amax = R(999, 1000), R(1001, 1000)
y0min = sp.factor(R(12, 25) / Amax - small)
y0max = sp.factor(R(12, 25) / Amin + small)
require(y0min == R(46999, 100100) > 0, "y0 lower")
require(sp.factor(sp.diff(wc, X)) == -R(3, 5), "wc X monotonicity")
require(sp.factor(sp.diff(wc, Mpar)) == 27 / (25 * A**2),
        "wc M monotonicity")
wlower = sp.factor(wc.subs({X: Xmax, Mpar: -Mcap}) - small)
wupper = sp.factor(wc.subs({X: Xmax, Mpar: Mcap}) + small)
require(wlower == R(49048421992, 85976765875), "wc lower")
require(wupper == R(2754252287, 4647392750), "wc upper")
zslope = sp.factor(wlower - Smax * y0max**2)
zbase = sp.factor(3 * Xmin - Xmin**2)
zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * wupper)
require(zslope == R(
    117593537485995685381, 206137893861900000000
) > 0, "Z slope")
require(zbase == R(14, 25) > 0, "Z lower")
require(zupper == R(
    552049179533075241627, 863930374910102500000
) < 1, "Z upper")

Tdirect = sp.factor(R(6, 5) * y0 + wc + omega)
Tclosed = sp.factor(
    R(9, 5) + omega + R(6, 5) * nu
    - R(63, 125) / A - R(3, 5) * X
)
require(sp.factor(Tdirect - Tclosed) == 0, "coupled danger coefficient")
danger_expr = sp.factor(R(3, 5) - R(13, 5) * X - S * Tdirect)
require(sp.factor(1 - xsheet**2 - ysheet**2 - Zsheet
                  - danger_expr) == 0, "literal danger equality")
Tmin = sp.factor(Tclosed.subs({
    X: Xmax, Mpar: -Mcap, omega: -small, nu: -small,
}))
require(Tmin == R(585533340809, 515860595250) > 0,
        "positive danger coefficient")
require(sp.factor(sp.diff(Tclosed, Mpar)) == R(63, 125) / A**2,
        "A monotonicity")
require(sp.factor(sp.diff(Tclosed, omega) - 1) == 0
        and sp.factor(sp.diff(Tclosed, nu) - R(6, 5)) == 0,
        "centered-variable monotonicity")
require(sp.factor(sp.diff(Tclosed, X) + R(3, 5)) == 0,
        "coefficient X monotonicity")
require(sp.factor(sp.diff(danger_expr, X)
                  + R(13, 5) - R(3, 5) * S) == 0,
        "danger decreases in X")
require(sp.factor(sp.diff(danger_expr, S) + Tclosed) == 0,
        "danger decreases in positive scale")
boundary_danger = sp.factor(danger_expr.subs({
    S: Smax, X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
require(boundary_danger == 0, "exact unique monotone danger boundary")
danger_safe = sp.factor(danger_expr.subs({
    S: Smax, X: R(2, 9), Mpar: Mcap, omega: small, nu: small,
}))
require(danger_safe == R(142237343, 6435000000) > 0,
        "strict two-ninth diagnostic")
cross_reserve = sp.factor(zbase - R(1, 6))
require(cross_reserve == R(59, 150) > 0,
        "new cell lies beyond the old Z=1/6 locator")
require(Smax < 1 and Xmin > 0 and Amin > 0,
        "real frame and positive denominators")
require(25**8 * Amin**8 * Smax > 0,
        "positive direct-quotient clearing factors")
print("PASS lambda, signed z, Z bounds, determinant, rank two")
print("PASS strict danger X<Xstar and unique equality corner at Xstar")

# Exact seam/breakpoint and 72 rational falsification nodes.
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
    det_v = sp.factor(R(5, 9) * Sv * Zv)
    boundary = (
        Sv == Smax and uv == 1 and Mv == Mcap
        and ov == small and nv == small
    )
    require(value > 0 and Zv > 0 and det_v > 0,
            "positive exact scale/rank node")
    if boundary:
        require(danger_v == 0, "classified exact boundary")
    else:
        require(danger_v > 0, "strict legal exact node")
    records.append((value, Sv, uv, Mv, ov, nv, Zv, danger_v, det_v, boundary))
require(len(records) == 72, "72 falsification nodes")
require(sum(record[9] for record in records) == 1, "one boundary node")
minimum = min(records)
left = sp.factor(mapped.subs({
    S: Smax, X: Xmin, Mpar: -Mcap, omega: -small, nu: -small,
}))
right = sp.factor(mapped.subs({
    S: Smax, X: Xmax, Mpar: -Mcap, omega: -small, nu: -small,
}))
boundary_gate = sp.factor(mapped.subs({
    S: Smax, X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
boundary_Z = sp.factor(Zsheet.subs({
    S: Smax, X: Xmax, Mpar: Mcap, omega: small, nu: small,
}))
boundary_det = sp.factor(R(5, 9) * Smax * boundary_Z)
require(left == R(
    213355344357890421512795094325969057679,
    40000000000000000000000000000000000,
) > 0, "left seam gate")
require(right == R(
    440192380473245412784529502413179004647222033560333676023602100187,
    62036421210789424476671714120000000000000000000000000000000000,
) > 0, "right breakpoint gate")
require(boundary_gate == R(
    31769777656530376672684788597449530147261943789366551863977,
    4459366315900461674520000000000000000000000000000000000,
) > 0, "boundary gate")
require(boundary_Z == R(
    220819670985134517424899959,
    345572149964041000000000000,
) > 0, "boundary Z")
require(boundary_det == R(
    220819670985134517424899959,
    6220298699352738000000000000000,
) > 0, "boundary determinant")
require(minimum[0] > 0, "strict exact falsification minimum")

print("PASS seam/breakpoint values, 71 legal nodes, one exact boundary")
print("XSTAR", Xstar)
print("STRICT_RESERVE", reserve)
print("Z_UPPER", zupper)
print("DANGER_AT_TWO_NINTH", danger_safe)
print("Z_EQUALS_ONE_SIXTH_CROSS_RESERVE", cross_reserve)
print("LEFT_SEAM_36GAMMA", left)
print("RIGHT_BREAKPOINT_36GAMMA", right)
print("BOUNDARY_36GAMMA", boundary_gate)
print("BOUNDARY_Z", boundary_Z)
print("BOUNDARY_DANGER", boundary_danger)
print("BOUNDARY_DET", boundary_det)
print("REFEREE_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT independent gate on closed X<=Xstar; strict danger for X<Xstar")
print("SCOPE maximal moving-sheet partial theorem; full compact ball remains open")
