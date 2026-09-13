#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=7/8.

The old audited sheet loses legality because its squared z-coordinate crosses
zero.  This source keeps every other parameter and adds the exact lift

    Z_new = Z_old + 2 (X-Xanchor),  Xanchor=83059/100000.

It rebuilds the fully conjugated Hermitian Q,Q^2 gate through the frozen
definition-level endpoint source, proves exact splice and full-cell legality,
and tests one and only one new cell 17/20 <= X <= 7/8.  It is a source
candidate, not an independent referee.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from itertools import product
from pathlib import Path
import os
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: recentered-lift X7/8 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = {
    "tmp/research/compact_ball_inward_z_endpoint_extension.py":
        "2ab0f3f532fbfe0d2fc6b2aa3301ff4857f783161f109ad4d846cbcbf266df4f",
    "tmp/research/compact_ball_inward_z_legality_frontier_extension.py":
        "1a2ef5c669d1602a27641f05ae1d051e7f03d6db99a8280085b3ececd23667a4",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_source_candidate.md":
        "5e4109a188f3301412dd49f78039f2a0d4e107948f8e23c1bdc79cbcd4029aa0",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_independent_referee.py":
        "9d00fc3b026bd6751831e412205fb2803a9026c6eba38c408f5c861f886b1642",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_LEGALITY_FRONTIER_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md":
        "44ac690f65bf7b6ce7a4be8320ed8406e4e4dae167673117435d5f95b8865591",
    "tmp/research/compact_ball_inward_z_recentered_lift_x17_20_source_freeze_manifest.sha256":
        "d32d987a7ed49e3be0b68742e994fb6810b8e164022040bbafab0a305ad75a87",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_independent_referee.py":
        "f836630b4f987bf396c66304cdaa8c30bbe5510914acf2025d690201985182cd",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X17_20_INDEPENDENT_REFEREE_AUDIT.md":
        "ee88a84387602f040cefc6932d0d7521e59527d1c0d7debf0ae7781eaa291147",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_independent_referee_manifest.sha256":
        "aa5b0146e2c1bd6cd7386be7353596a91fef51784af4b0741f142b26be47189c",
}
if os.environ.get("INWARD_Z_X7_8_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"recentered-lift exact gate failed: {label}")


def sparse_add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return {key: sp.expand(value) for key, value in result.items()
            if value != 0}


def sparse_multiply(left, right):
    result = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si+sj, xi+xj)
            result[key] = result.get(key, 0) + left_value*right_value
    return {key: sp.expand(value) for key, value in result.items()
            if value != 0}


def sparse_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = sparse_multiply(result, base)
    return result


def modsq(value):
    return sp.expand_complex(value*sp.conjugate(value))


def reduce_relations(expression, q, h, zsigned, S, Z):
    value = sp.rem(sp.expand(expression), q**2-(1-h**2), q)
    value = sp.rem(sp.expand(value), zsigned**2-Z, zsigned)
    value = sp.rem(sp.expand(value), h**2-S, h)
    return sp.expand(value)


def centered_lower(expression, variables, radii):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    zero = (0,)*len(variables)
    center = polynomial.coeff_monomial(zero)
    variation = sum(
        abs(coefficient)*sp.prod(
            radius**degree for radius, degree in zip(radii, powers)
        )
        for powers, coefficient in polynomial.terms()
        if powers != zero
    )
    return sp.factor(center-variation)


def bernstein_controls_2d(expression, first, second):
    polynomial = sp.Poly(sp.expand(expression), first, second)
    degrees = polynomial.degree(first), polynomial.degree(second)
    power = {powers: coefficient for powers, coefficient in polynomial.terms()}
    controls = {}
    for i in range(degrees[0]+1):
        for j_index in range(degrees[1]+1):
            controls[i, j_index] = sp.factor(sum(
                power.get((k_index, ell_index), 0)
                * sp.Rational(sp.binomial(i, k_index),
                              sp.binomial(degrees[0], k_index))
                * sp.Rational(sp.binomial(j_index, ell_index),
                              sp.binomial(degrees[1], ell_index))
                for k_index in range(i+1)
                for ell_index in range(j_index+1)
            ))
    return degrees, controls


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")
print("PASS frozen definition/frontier dependency hashes", flush=True)

# Rebuild the signed frame, Hermitian Q, every entry of Q^2, and the fully
# conjugated raw gate directly.  No discovery source is imported or executed.
R, I = sp.Rational, sp.I
lam, S, x, y, Z = sp.symbols("lam S x y Z", real=True)
h, q, zsigned = sp.symbols("h q zsigned", real=True)
a, c = 1/sp.sqrt(6), sp.sqrt(5)/sp.sqrt(6)
zeta = (4+3*I)/5
p = sp.Matrix([a, 0, c])
rcol = sp.Matrix([-a, 0, c*zeta])
fcol = sp.Matrix([-c*h, q, -a*h*zeta])
U = sp.Matrix.hstack(fcol, rcol)
j = (1+5*x)/(3*sp.sqrt(5))
kappa = (-3+5*y)/(3*sp.sqrt(5))
ell = sp.sqrt(5)*zsigned/3
C = sp.Matrix([
    [j**2+kappa**2+ell**2, h*(j-I*kappa)],
    [h*(j+I*kappa), h**2],
])
H = sp.expand(U*C*sp.conjugate(U.T))
Q = sp.expand(lam*H)
xi = sp.expand(Q*p)
Q2 = sp.expand(Q*Q)
leak1 = c*sp.conjugate(xi[0])+a*xi[2]+I*(a*c-Q2[2, 0])
leak2 = c*sp.conjugate(xi[1])-I*Q2[2, 1]
Gamma = reduce_relations(sp.expand(
    4*a**2*modsq(xi[1])+modsq(leak1)+modsq(leak2)
    -32*a**2*sp.re(xi[0])**2
), q, h, zsigned, S, Z)
require(not Gamma.has(q, h, zsigned),
        "signed frame variables cancel in the raw gate")
require(sp.Poly(36*Gamma, lam).degree() == 4
        and sp.Poly(36*Gamma, lam).nth(0) == 5,
        "raw-gate quartic normalization")
raw_Z_degree = sp.Poly(36*Gamma, Z).degree()
require(raw_Z_degree <= 4, "finite low-degree raw-gate dependence on Z")
print("PASS original Hermitian Q,Q^2 raw-gate reconstruction", flush=True)
print("RAW_GATE_Z_DEGREE", raw_Z_degree, flush=True)

Xanchor = R(83059, 100000)
Xleft = R(17, 20)
Xright = R(7, 8)
K = R(2)
Smax = R(1, 10000)
Mrad, omega_rad, nu_rad = R(1, 1000), R(1, 100), R(1, 100)
X, M, omega, nu = sp.symbols("X M omega nu", real=True)
A = 1+M
tilt = -R(10636, 275)
y0 = R(12, 25)/A+nu
b = ((45*M+18)/(25*A)-R(3, 5)*X+omega
     +tilt*(X-R(1, 5)))
xsheet = -R(1, 5) + X
ysheet = R(3, 5) + S*y0
Zold = R(9, 13) - X**2 + S*b - S**2*y0**2
Znew = sp.expand(Zold + K*(X-Xanchor))

# Avoid a monolithic substitution/expand.  The audited sparse pre-map has
# only 134 terms in (S,Z,X,Yaux); composition is then exact dictionary
# arithmetic in (S,X), followed by the positive denominator clearing.
mu, Yaux = sp.symbols("mu_recenter Yaux_recenter", real=True)
premap = sp.expand((S**3*sp.cancel((36*Gamma).subs(lam, mu/S))).subs({
    x: -R(1, 5)+X,
    y: R(3, 5)+Yaux,
    mu: A,
}))
premap_poly = sp.Poly(premap, S, Z, X, Yaux)
require(len(premap_poly.terms()) == 134, "134-term sparse pre-map")
denominator = 25*A
sparse_y = {(1, 0): (12+25*A*nu)/denominator}
sparse_z = {
    (0, 0): R(9, 13)-K*Xanchor,
    (0, 1): K,
    (0, 2): -R(1),
    (1, 0): (45*M+18+25*A*(omega-tilt*R(1, 5)))/denominator,
    (1, 1): tilt-R(3, 5),
    (2, 0): -((12+25*A*nu)/denominator)**2,
}
if os.environ.get("INWARD_Z_X7_8_BAD_SPARSE_NORMALIZATION") == "1":
    sparse_z[(0, 1)] += 1
require(sp.factor(sp.cancel(sum(value*S**sd*X**xd
                                for (sd, xd), value in sparse_y.items())
                            -S*y0)) == 0, "sparse/direct y map")
require(sp.factor(sp.cancel(sum(value*S**sd*X**xd
                                for (sd, xd), value in sparse_z.items())
                            -Znew)) == 0,
        "sparse/direct recentered Z map")

mapped_sparse = {}
for (s_degree, z_degree, x_degree, y_degree), coefficient in premap_poly.terms():
    term = {(s_degree, x_degree): coefficient}
    term = sparse_multiply(term, sparse_power(sparse_z, z_degree))
    term = sparse_multiply(term, sparse_power(sparse_y, y_degree))
    mapped_sparse = sparse_add(mapped_sparse, term)

cleared = {}
for key, coefficient in mapped_sparse.items():
    value = sp.cancel(denominator**8*coefficient)
    if value == 0:
        continue
    numerator, denominator_after = value.as_numer_denom()
    require(not denominator_after.free_symbols,
            f"symbolic quotient denominator at {key}")
    cleared[key] = sp.expand(numerator/denominator_after)
minimum_cleared_S_degree = min(sd for sd, _ in cleared)
cleared_polynomial = sum(
    coefficient*S**sd*X**xd
    for (sd, xd), coefficient in cleared.items()
)
Qhat = sp.Poly(cleared_polynomial/S**minimum_cleared_S_degree,
               S, X, M, omega, nu, domain=sp.QQ).as_expr()
require(minimum_cleared_S_degree == 0,
        "positive clearing is exactly 25^8 A^8 S^3")
first_layer = S**3*25**8*M**2*A**8*(5*M**2+14*M+14)
require(sp.factor(5*M**2+14*M+14
                  -(5*(M+R(7, 5))**2+R(21, 5))) == 0,
        "manifestly nonnegative first layer")
core = sp.expand(Qhat-first_layer)
sx = sp.Poly(Qhat, S, X)
core_sx = sp.Poly(core, S, X)
core_terms = {powers: sp.expand(value)
              for powers, value in core_sx.terms()}
if os.environ.get("INWARD_Z_X7_8_DROP_TERM") == "1":
    core_terms.pop(sorted(core_terms)[0])
    core = sp.expand(sum(
        value*S**powers[0]*X**powers[1]
        for powers, value in core_terms.items()
    ))
require(len(core_terms) == len(core_sx.terms()),
        "complete core coefficient table")
centered_monomials = sum(
    len(sp.Poly(value, M, omega, nu).terms())
    for value in core_terms.values()
)
print("PASS cleared/core structure",
      len(sx.terms()), len(core_terms), centered_monomials,
      "bidegree", (sx.degree(S), sx.degree(X)), flush=True)

# Exact splice: the global recentered formula is unchanged from the audited
# predecessor, and the new cell's u=0 face is exactly X=17/20.
require(raw_Z_degree == sp.Poly(36*Gamma, Z).degree(),
        "raw-gate Z-degree stable at splice")
v_previous = sp.symbols("v_previous", real=True)
X_previous = Xanchor+(Xleft-Xanchor)*v_previous
X_new_left = Xleft
previous_inputs = (
    A/S,
    xsheet.subs(X, X_previous),
    ysheet.subs(X, X_previous),
    Znew.subs(X, X_previous),
)
new_inputs = (
    A/S,
    xsheet.subs(X, X_new_left),
    ysheet.subs(X, X_new_left),
    Znew.subs(X, X_new_left),
)
require(all(sp.factor(sp.cancel(old.subs(v_previous, 1)-new)) == 0
            for old, new in zip(previous_inputs, new_inputs)),
        "raw-gate input splice parameter by parameter at X=17/20")
print("PASS exact old/new chart and raw-gate splice", flush=True)

# One exact Bernstein cell only.  Centered L1 lower controls are sufficient,
# and failure of one such control would mean certificate insufficiency, not a
# negative raw gate.
tau, u = sp.symbols("tau_recenter u_recenter", real=True)
Xaff = Xleft + (Xright-Xleft)*u
cell = sp.expand(core.subs({X: Xaff, S: Smax*tau}))
require(sp.expand(core.subs(X, Xleft)-cell.subs({u: 0, tau: S/Smax})) == 0,
        "exact cleared-gate splice at X=17/20")
degrees, controls = bernstein_controls_2d(cell, tau, u)
variables = (M, omega, nu)
radii = (Mrad, omega_rad, nu_rad)
lowers = {
    key: centered_lower(value, variables, radii)
    for key, value in controls.items()
}
nonpositive = {key: value for key, value in lowers.items() if value <= 0}
if nonpositive:
    first = min(nonpositive.items(), key=lambda item: item[1])
    raise RuntimeError(
        "CERTIFICATE_INSUFFICIENCY: nonpositive centered control "
        f"{first[0]} = {first[1]}"
    )
minimum_index, reserve = min(lowers.items(), key=lambda item: item[1])
minimum_polynomial = sp.factor(controls[minimum_index])
require(centered_lower(minimum_polynomial, variables, radii)
        == reserve, "minimum control/lower consistency")
print("PASS exact centered Bernstein controls", len(controls),
      "degree", degrees, "minimum", minimum_index, reserve, flush=True)

# Full-cell legality.  Z is increasing in X and decreasing in S at its worst
# centered corner.  The old left endpoint supplies the exact positive Z
# reserve.  Danger is decreasing in X but has a positive S=0 lower reserve;
# its S correction is positive because T=(6/5)y0+b is uniformly negative.
Zderivative = sp.factor(sp.diff(Znew, X))
require(sp.factor(Zderivative-(K-2*X-R(10801, 275)*S)) == 0,
        "exact Z derivative")
Zderivative_lower = sp.factor(K-2*Xright-R(10801, 275)*Smax)
require(Zderivative_lower == R(676699, 2750000) > 0,
        "Z increases on the full cell")
y0min = sp.factor(y0.subs({M: Mrad, nu: -nu_rad}))
y0max = sp.factor(y0.subs({M: -Mrad, nu: nu_rad}))
bmax = sp.factor(b.subs({X: Xleft, M: Mrad, omega: omega_rad}))
bmin_left = sp.factor(b.subs({X: Xleft, M: -Mrad,
                              omega: -omega_rad}))
require(0 < y0min <= y0max and bmin_left <= bmax < 0,
        "uniform y0/b signs")
require(sp.factor(sp.diff(b, M)-R(27, 25)/A**2) == 0
        and sp.diff(b, omega) == 1
        and sp.diff(b, X) == -R(10801, 275),
        "exact b monotonicity")
require(sp.factor(sp.diff(y0, M)+R(12, 25)/A**2) == 0
        and sp.diff(y0, nu) == 1,
        "exact y0 monotonicity")
Zmin = sp.factor(Znew.subs({X: Xleft, S: Smax, M: -Mrad,
                            omega: -omega_rad, nu: nu_rad}))
require(Zmin == R(97261562093134873, 15857127000000000000) > 0,
        "exact inherited positive Z reserve")
Zupper = sp.factor((R(9, 13)-Xright**2+K*(Xright-Xanchor)))
require(Zupper == R(40307, 2600000) < 1, "uniform Z upper bound")

T = sp.factor(R(6, 5)*y0+b)
Tmax = sp.factor(T.subs({X: Xleft, M: Mrad,
                         omega: omega_rad, nu: nu_rad}))
require(Tmax == -R(434919, 17875) < 0,
        "uniform negative danger correction")
require(sp.factor(sp.cancel(sp.diff(T, M)-R(63, 125)/A**2)) == 0
        and sp.factor(sp.cancel(sp.diff(T, omega)-1)) == 0
        and sp.factor(sp.cancel(sp.diff(T, nu)-R(6, 5))) == 0
        and sp.factor(sp.cancel(sp.diff(T, X)+R(10801, 275))) == 0,
        "exact T monotonicity")
danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)
danger_identity = sp.factor(
    R(2, 5)*(X-R(3, 13))-K*(X-Xanchor)-S*T
)
require(sp.factor(danger_new-danger_identity) == 0,
        "exact new danger identity")
danger_base = sp.factor(
    R(2, 5)*(Xright-R(3, 13))-K*(Xright-Xanchor)
)
require(danger_base == R(109767, 650000) > 0,
        "strict full-cell danger lower bound")
det_coefficient = sp.factor(R(5, 9)*Zmin)
require(det_coefficient > 0, "strict rank-two determinant lower bound")
print("PASS full-cell lambda/Z/danger/rank-two legality for both z signs",
      flush=True)

# Definition-level diagnostic nodes.  They are breaker checks only; the
# continuum result is supplied by the exact Bernstein tensor above.
middle = sp.factor((Xleft+Xright)/2)
records = []
for Sv, Xv, Mv, ov, nv in product(
    (R(1, 1000000), R(1, 20000), Smax),
    (Xleft, middle, Xright),
    (-Mrad, Mrad),
    (-omega_rad, omega_rad),
    (-nu_rad, nu_rad),
):
    subs = {S: Sv, X: Xv, M: Mv, omega: ov, nu: nv}
    Zv = sp.factor(Znew.subs(subs))
    Dv = sp.factor(danger_new.subs(subs))
    Av = 1+Mv
    value = sp.factor((36*Gamma).subs({
        S: Sv,
        lam: Av/Sv,
        x: (-R(1, 5)+Xv),
        y: (R(3, 5)+Sv*y0.subs({M: Mv, nu: nv})),
        Z: Zv,
    }))
    require(value > 0 and 0 < Zv < 1 and Dv > 0,
            "exact legal raw-gate-positive diagnostic node")
    records.append((value, Zv, Dv, Sv, Xv, Mv, ov, nv))
require(len(records) == 72, "72 exact diagnostic nodes")
node_minimum = min(records, key=lambda row: row[0])
print("PASS 72/72 original raw-gate diagnostic nodes", flush=True)

print("CELL", Xleft, Xright)
print("GLOBAL_Z_ANCHOR", Xanchor)
print("Z_LIFT_SLOPE", K)
print("STRUCTURE", len(sx.terms()), len(core_terms), centered_monomials,
      (sx.degree(S), sx.degree(X)))
print("CONTROL", degrees, len(controls), minimum_index, reserve)
print("MIN_CONTROL_POLYNOMIAL", minimum_polynomial)
print("Z_MIN", Zmin)
print("Z_UPPER", Zupper)
print("Z_DERIVATIVE_LOWER", Zderivative_lower)
print("T_MAX", Tmax)
print("DANGER_LOWER", danger_base)
print("DET_C_LOWER", S*det_coefficient)
print("NODE_MIN", node_minimum)
print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact source candidate on one recentered-lift cell")
print("CLASSIFICATION proof candidate; no chart illegality and no raw-gate negative")
print("SCOPE one local cell only; full compact ball/common metric/arbitrary-node/fixed-lens open")
