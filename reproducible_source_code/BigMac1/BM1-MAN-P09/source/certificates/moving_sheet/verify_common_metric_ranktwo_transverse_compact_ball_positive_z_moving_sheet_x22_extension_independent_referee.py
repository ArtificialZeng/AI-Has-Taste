#!/usr/bin/env python3
"""Definition-level exact referee for the moving-sheet X<=1/22 extension.

This program deliberately does not import the candidate verifier, discovery
code, a cached quartic, or serialized coefficient data.  It reconstructs the
Hermitian matrix and the original conjugated gate from the displayed frame.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables assertions")

from hashlib import sha256
from itertools import product
import os
from pathlib import Path
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: independent referee accepts no arguments")

ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


DEPENDENCIES = {
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension.md":
        "5189571fc3913b3ff41dde268d2ce47cd89b18568748d76378007a1e0667d06d",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch.md":
        "c6d3ee1900d6274e7651d28ab8cdf89fdffe999c1f8a544bf22d4b368e5c7395",
    "audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch_independent_referee.py":
        "ec824fa0e5b0a040cd8aced25965540313b0ccae222d7113c07bc299c6f69cc6",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_POSITIVE_Z_MOVING_SHEET_CROSS_Z_CAP_STITCH_INDEPENDENT_REFEREE_AUDIT.md":
        "4340eb870f9af59cc7df574ff43cc633162369730a63759e66fce43193cfecec",
    "audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch_independent_referee_manifest.sha256":
        "27c46626dc24fe8aee0d4cea5d2baf5a618da6b949d16947c4d44ee26309b7a1",
    "requirements-portable.txt":
        "1f09771d05003a0467becdbf1184e7afa9e91a36c875ebe53a5926489ca4c070",
}

if os.environ.get("X22_REFEREE_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def reduce_frame_relations(expression, q, h, zcap, S, Z):
    """Reduce only q^2=1-h^2, zcap^2=Z, and h^2=S."""
    value = sp.expand(expression)
    value = sp.rem(value, q**2 - (1 - h**2), q)
    value = sp.rem(sp.expand(value), zcap**2 - Z, zcap)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    return sp.expand(value)


# Independent generic transverse frame.
lam, S, x, y, Z = sp.symbols("lam S x y Z", real=True)
h, q, zcap = sp.symbols("h q zcap", real=True)
sqrt5, sqrt6 = sp.sqrt(5), sp.sqrt(6)
a = 1 / sqrt6
c = sqrt5 / sqrt6
zeta = (4 + 3 * sp.I) / 5
p = sp.Matrix([a, 0, c])
r0 = sp.Matrix([-a, 0, c * zeta])
fh = sp.Matrix([-c * h, q, -a * h * zeta])
U = sp.Matrix.hstack(r0, fh)
j = (1 + 5 * x) / (3 * sqrt5)
kappa = (-3 + 5 * y) / (3 * sqrt5)
ell = sqrt5 * zcap / 3
C = sp.Matrix([
    [h**2, h * (j + sp.I * kappa)],
    [h * (j - sp.I * kappa), j**2 + kappa**2 + ell**2],
])
Hraw = sp.expand(U * C * sp.conjugate(U.T))
Qraw = sp.expand(lam * Hraw)
require(Hraw == sp.conjugate(Hraw.T), "Hermitian transverse matrix")

require(sp.simplify(sp.conjugate(r0).dot(r0) - 1) == 0,
        "first frame vector norm")
require(reduce_frame_relations(
    sp.conjugate(fh).dot(fh) - 1, q, h, zcap, S, Z
) == 0, "second frame vector norm")
require(sp.simplify(sp.conjugate(r0).dot(fh)) == 0,
        "frame orthogonality")
kernel = sp.Matrix([c * q * sp.conjugate(zeta),
                    h * sp.conjugate(zeta), a * q])
require(reduce_frame_relations(
    sp.conjugate(kernel).dot(kernel) - 1, q, h, zcap, S, Z
) == 0, "kernel unit norm")
require(sp.simplify(sp.conjugate(r0).dot(kernel)) == 0,
        "kernel orthogonal to r0")
require(reduce_frame_relations(
    sp.conjugate(fh).dot(kernel), q, h, zcap, S, Z
) == 0, "kernel orthogonal to fh")
require(all(reduce_frame_relations(entry, q, h, zcap, S, Z) == 0
            for entry in Hraw * kernel), "one-dimensional kernel witness")
require(reduce_frame_relations(
    sp.det(C) - sp.Rational(5, 9) * S * Z,
    q, h, zcap, S, Z
) == 0, "compression determinant")

# First gate derivation: the literal fully conjugated original formula.
xi_raw = sp.expand(Qraw * p)
Q2raw = sp.expand(Qraw * Qraw)
leak1 = sp.expand(
    c * sp.conjugate(xi_raw[0]) + a * xi_raw[2]
    + sp.I * (a * c - Q2raw[2, 0])
)
leak2 = sp.expand(c * sp.conjugate(xi_raw[1]) - sp.I * Q2raw[2, 1])
Gamma_direct_raw = sp.expand(
    4 * a**2 * modulus_square(xi_raw[1])
    + modulus_square(leak1) + modulus_square(leak2)
    - 32 * a**2 * sp.re(xi_raw[0])**2
)
Gamma_direct = reduce_frame_relations(
    Gamma_direct_raw, q, h, zcap, S, Z
)
require(not (Gamma_direct.has(q) or Gamma_direct.has(h)
             or Gamma_direct.has(zcap)), "frame radicals cancel")

# Second gate derivation: a three-component Gram vector.
v = sp.expand(Hraw * p)
H2 = sp.expand(Hraw * Hraw)
B0 = sp.Matrix([sp.I * a * c, 0, 0])
Lvec = sp.Matrix([
    c * sp.conjugate(v[0]) + a * v[2],
    c * sp.conjugate(v[1]),
    2 * a * v[1],
])
Mvec = sp.Matrix([-sp.I * H2[2, 0], -sp.I * H2[2, 1], 0])
Bvec = sp.expand(B0 + lam * Lvec + lam**2 * Mvec)
Gamma_gram_raw = sp.expand(
    sum(modulus_square(entry) for entry in Bvec)
    - 32 * a**2 * lam**2 * sp.re(v[0])**2
)
Gamma_gram = reduce_frame_relations(
    Gamma_gram_raw, q, h, zcap, S, Z
)
require(sp.expand(Gamma_direct - Gamma_gram) == 0,
        "original gate equals independent Gram-vector gate")

quartic = sp.Poly(sp.expand(36 * Gamma_direct), lam, S, x, y, Z,
                  domain=sp.QQ)
require(quartic.degree(lam) == 4, "scale quartic degree")
require(sp.Poly(36 * Gamma_direct, lam).coeff_monomial(1) == 5,
        "compact-normalized constant term")
Xchart, Ychart, Wchart = sp.symbols("Xchart Ychart Wchart", real=True)
chart_quartic = sp.Poly(sp.expand((36 * Gamma_direct).subs({
    x: -sp.Rational(1, 5) + Xchart,
    y: sp.Rational(3, 5) + Ychart,
    Z: 3 * Xchart - Xchart**2 - Ychart**2 + Wchart,
})), lam, S, Xchart, Ychart, Wchart, domain=sp.QQ)
require(len(quartic.terms()) == 339, "generic compact quartic support")
require(len(chart_quartic.terms()) == 94, "recentered chart quartic support")

# Exact moving sheet, reconstructed after the generic gate exists.
X, M, omega, nu, sigma = sp.symbols(
    "X M omega nu sigma", real=True
)
A = 1 + M
y0 = sp.Rational(12, 25) / A + nu
wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
Y = S * y0
Wsh = S * (wc + omega)
Zsheet = sp.factor(3 * X - X**2 - Y**2 + Wsh)
xsheet = -sp.Rational(1, 5) + X
ysheet = sp.Rational(3, 5) + Y

sheet_identity = sp.factor(
    xsheet**2 + ysheet**2 + Zsheet
    - (sp.Rational(2, 5) + sp.Rational(13, 5) * X
       + sp.Rational(6, 5) * Y + Wsh)
)
require(sheet_identity == 0, "compact-ball identity")
require(sp.factor((A / S) * S - A) == 0, "normalized scale identity")

# Legality bounds are derived from monotonic endpoint choices.
Amin, Amax = sp.Rational(999, 1000), sp.Rational(1001, 1000)
Smax = sp.Rational(1, 10000)
Xmin, Xmax = sp.Rational(1, 23), sp.Rational(1, 22)
small = sp.Rational(1, 100)
Mcap = sp.Rational(1, 1000)
y0min = sp.factor(sp.Rational(12, 25) / Amax - small)
y0max = sp.factor(sp.Rational(12, 25) / Amin + small)
require(y0min == sp.Rational(46999, 100100) > 0, "y0 lower bound")

wc_lower = sp.factor(wc.subs({X: Xmax, M: -Mcap}) - small)
wc_upper_sharp = sp.factor(wc.subs({X: Xmax, M: Mcap}) + small)
wc_upper = sp.Rational(73181, 100100)
require(wc_upper_sharp == sp.Rational(70451, 100100) < wc_upper,
        "independent sharp upper implies stated wc envelope")
require(wc_lower == sp.Rational(27743, 40700), "wc+omega lower")
bracket_lower = sp.factor(wc_lower - Smax * y0max**2)
require(bracket_lower == sp.Rational(
    83142836564221, 121977900000000
) > 0, "positive Z correction")
require(sp.factor(sp.diff(wc, X)) == -sp.Rational(3, 5),
        "wc decreases in X")
require(sp.factor(sp.diff(wc, M)) == 27 / (25 * A**2),
        "wc increases in M")

Zlower_base = sp.factor(3 * Xmin - Xmin**2)
require(Zlower_base == sp.Rational(68, 529), "strict Z lower base")
Zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * wc_upper)
require(Zupper == sp.Rational(1479554991, 11011000000),
        "Z upper bound")
require(Zupper < sp.Rational(1, 7), "strict upper cap")
danger_margin = sp.factor(
    sp.Rational(3, 5) - sp.Rational(13, 5) * Xmax
    - sp.Rational(6, 5) * Smax * y0max - Smax * wc_upper
)
require(danger_margin == sp.Rational(267603185879, 555555000000) > 0,
        "strict compact-ball danger")

# Moving quotient from the freshly derived generic quartic.
mapped = sp.cancel((36 * Gamma_direct).subs({
    lam: A / S, x: xsheet, y: ysheet, Z: Zsheet,
}))
N = sp.cancel(S**3 * mapped)
D = 25**8 * A**8
Qhat_raw = sp.cancel(D * N / S**2)
Qhat = sp.Poly(sp.expand(Qhat_raw), S, X, M, omega, nu,
               domain=sp.QQ).as_expr()
require(sp.factor(mapped - Qhat / (25**8 * A**8 * S)) == 0,
        "lossless quotient identity")

SX = sp.Poly(Qhat, S, X)
sx_terms = {(powers[0], powers[1]): sp.expand(coefficient)
            for powers, coefficient in SX.terms()}
require(len(sx_terms) == 20, "twenty quotient terms")
require(SX.degree(S) == 5 and SX.degree(X) == 4,
        "quotient bidegree")
first_layer = 25**8 * M**2 * S * A**8 * (5 * M**2 + 14 * M + 14)
require(sp.expand(sx_terms[(1, 0)] * S - first_layer) == 0,
        "nonnegative first layer")

if os.environ.get("X22_REFEREE_DROP_TERM") == "1":
    sx_terms.pop(next(iter(sx_terms)))
require(len(sx_terms) == 20, "complete quotient term set")

def centered_abs_bound(expression):
    polynomial = sp.Poly(sp.expand(expression), M, omega, nu, domain=sp.QQ)
    return sp.factor(sum(
        abs(coefficient) * Mcap**powers[0]
        * small**powers[1] * small**powers[2]
        for powers, coefficient in polynomial.terms()
    ))


def centered_lower_bound(expression):
    constant = sp.expand(expression).subs({M: 0, omega: 0, nu: 0})
    remainder = centered_abs_bound(sp.expand(expression - constant))
    return sp.factor(constant - remainder)


a2 = sx_terms[(2, 0)]
b2 = sx_terms[(1, 1)]
c2 = sx_terms[(0, 2)]
a0, b0, c0 = map(centered_lower_bound, (a2, b2, c2))
require(a0 > 0 and b0 > 0 and c0 > 0,
        "positive quadratic-layer centered bounds")
expected_c0 = sp.Rational(
    2564950982194530478444050838857341987999,
    1274019840000000000000000000,
)
require(c0 == expected_c0, "exact c0 reserve")

higher = {
    key: coefficient for key, coefficient in sx_terms.items()
    if sum(key) > 2
}
require(len(higher) == 16, "sixteen higher quotient terms")
require(sum(len(sp.Poly(coefficient, M, omega, nu).terms())
            for coefficient in higher.values()) == 947,
        "947 centered remainder monomials")

sigma_max = sp.factor(Smax / Xmin)
require(sigma_max == sp.Rational(23, 10000), "projective sigma bound")
Rabs = sp.factor(sum(
    centered_abs_bound(coefficient)
    * sigma_max**i * Xmax**(i + j - 2)
    for (i, j), coefficient in higher.items()
))
expected_Rabs = sp.Rational(
    45501595887352000690514390785303819932610237699051256372767272123253,
    16648891269120000000000000000000000000000000000000000000000,
)
require(Rabs == expected_Rabs, "exact higher-term absolute envelope")
strict_margin = sp.factor(c0 - Rabs)
expected_margin = sp.Rational(
    33473277839430772291616341971402441279238321762300948743627232727876747,
    16648891269120000000000000000000000000000000000000000000000,
)
require(strict_margin == expected_margin > 0, "strict continuum margin")

# Both endpoints and a symmetric exact rational falsification grid.
corner = {
    S: Smax, M: -Mcap, omega: -small, nu: -small,
}
left_value = sp.factor(mapped.subs(corner | {X: Xmin}))
right_value = sp.factor(mapped.subs(corner | {X: Xmax}))
require(left_value == sp.Rational(
    2851967535986553322459201051507517913149039,
    11193640000000000000000000000000000000000,
) > 0, "closed left endpoint witness")
require(right_value == sp.Rational(
    14817150110247071841775080222180418970749,
    53240000000000000000000000000000000000,
) > 0, "closed right endpoint witness")
left_Z = sp.factor(Zsheet.subs(corner | {X: Xmin}))
right_Z = sp.factor(Zsheet.subs(corner | {X: Xmax}))
left_danger = sp.factor(
    1 - xsheet**2 - ysheet**2 - Zsheet
).subs(corner | {X: Xmin})
right_danger = sp.factor(
    1 - xsheet**2 - ysheet**2 - Zsheet
).subs(corner | {X: Xmax})
require(left_Z > sp.Rational(68, 529) and left_Z < sp.Rational(1, 7),
        "left endpoint Z")
require(right_Z > sp.Rational(68, 529) and right_Z < sp.Rational(1, 7),
        "right endpoint Z")
require(left_danger > 0 and right_danger > 0,
        "endpoint strict compact-ball danger")

sample_S = (Smax, sp.Rational(1, 20000), sp.Rational(1, 100000))
sample_X = (Xmin, sp.Rational(45, 1012), Xmax)
sample_values = []
for Sv, Xv, Mv, ov, nv in product(
    sample_S, sample_X, (-Mcap, Mcap), (-small, small), (-small, small)
):
    value = sp.factor(mapped.subs({
        S: Sv, X: Xv, M: Mv, omega: ov, nu: nv,
    }))
    require(value > 0, "exact rational falsification node")
    sample_values.append((value, Sv, Xv, Mv, ov, nv))
require(len(sample_values) == 72, "falsification node count")
sample_min = min(sample_values)

print("PASS independent original-gate and Gram-vector reconstruction")
print("PASS lambda, Z, danger, determinant, rank-two, and endpoint legality")
print("PASS 20 quotient terms, 16 higher terms, and 947 centered monomials")
print("PASS strict continuum envelope and 72 exact falsification nodes")
print(f"c0={c0}")
print(f"Rabs={Rabs}")
print(f"strict_margin={strict_margin}")
print(f"endpoint_left_36Gamma={left_value}")
print(f"endpoint_right_36Gamma={right_value}")
print(f"endpoint_left_Z={left_Z}")
print(f"endpoint_right_Z={right_Z}")
print(f"endpoint_left_danger_margin={left_danger}")
print(f"endpoint_right_danger_margin={right_danger}")
print("sample_min=" + ":".join(str(item) for item in sample_min))
print("verifier_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
print("scope=X in [1/23,1/22] moving sheet only; general gate open")
