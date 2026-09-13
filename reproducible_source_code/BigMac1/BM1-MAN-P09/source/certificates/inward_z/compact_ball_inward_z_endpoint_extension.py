#!/usr/bin/env python3
"""Exact continuation gate for the inward-Z sheet beyond X=1/4.

This program starts from the signed compact-ball Gram columns and rebuilds
the fully conjugated Q,Q^2 gate.  It does not import the frozen discovery or
referee program and does not reuse their Bernstein table.  The first tested
cell is the exact rational interval [1/4,131/520].
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: endpoint extension verifier accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = {
    "tmp/research/compact_ball_inward_z_tilt_discovery.py":
        "6ee91b88c1835f44183a8da833239c817cdd6d079d73cd5b9e9c42428661f6ca",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_independent_referee.py":
        "e6cb94c9ecd322190e959ede9ce19131e57a6964dfb29ccd88f76c076abff3c0",
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_source_candidate.md":
        "7b78d77ef418de755f41d8fcbd7b8aaa15eae1b1052276fe1a90274c1989e563",
}
if os.environ.get("INWARD_Z_EXTENSION_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"endpoint extension failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")
print("PASS frozen inward-Z dependency hashes")


def modsq(value):
    return sp.expand_complex(value * sp.conjugate(value))


def reduce_relations(expression, q, h, zsigned, S, Z):
    value = sp.rem(sp.expand(expression), q**2 - (1 - h**2), q)
    value = sp.rem(sp.expand(value), zsigned**2 - Z, zsigned)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    return sp.expand(value)


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
    degrees = polynomial.degree(first), polynomial.degree(second)
    power = {powers: coefficient for powers, coefficient in polynomial.terms()}
    controls = {}
    for i in range(degrees[0] + 1):
        for j in range(degrees[1] + 1):
            controls[i, j] = sp.factor(sum(
                power.get((k, ell), 0)
                * sp.Rational(sp.binomial(i, k), sp.binomial(degrees[0], k))
                * sp.Rational(sp.binomial(j, ell), sp.binomial(degrees[1], ell))
                for k in range(i + 1) for ell in range(j + 1)
            ))
    return degrees, controls


R, I = sp.Rational, sp.I
lam, S, x, y, Z = sp.symbols("lam S x y Z", real=True)
h, q, zsigned = sp.symbols("h q zsigned", real=True)
a, c = 1 / sp.sqrt(6), sp.sqrt(5) / sp.sqrt(6)
zeta = (4 + 3 * I) / 5
p = sp.Matrix([a, 0, c])

# Rebuild the signed-z raw gate in the referee's permuted column order.
rcol = sp.Matrix([-a, 0, c * zeta])
fcol = sp.Matrix([-c * h, q, -a * h * zeta])
U = sp.Matrix.hstack(fcol, rcol)
j = (1 + 5*x) / (3*sp.sqrt(5))
kappa = (-3 + 5*y) / (3*sp.sqrt(5))
ell = sp.sqrt(5) * zsigned / 3
C = sp.Matrix([
    [j**2 + kappa**2 + ell**2, h*(j - I*kappa)],
    [h*(j + I*kappa), h**2],
])
H = sp.expand(U*C*sp.conjugate(U.T))
Q = sp.expand(lam*H)
xi = sp.expand(Q*p)
Q2 = sp.expand(Q*Q)
leak1 = c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - Q2[2, 0])
leak2 = c*sp.conjugate(xi[1]) - I*Q2[2, 1]
Gamma = reduce_relations(sp.expand(
    4*a**2*modsq(xi[1]) + modsq(leak1) + modsq(leak2)
    - 32*a**2*sp.re(xi[0])**2
), q, h, zsigned, S, Z)
require(not Gamma.has(q, h, zsigned), "signed frame variables cancel")
require(sp.Poly(36*Gamma, lam).degree() == 4, "raw scale quartic")
require(sp.Poly(36*Gamma, lam).nth(0) == 5, "constant normalization")
print("PASS signed-z fully conjugated Q,Q^2 raw gate")

# Same inward-Z sheet, but on the first new rational cell.
X, M, omega, nu = sp.symbols("X M omega nu", real=True)
tau, u = sp.symbols("tau u", real=True)
X0, X1 = R(1, 4), R(131, 520)
Smax = R(1, 10000)
Mrad, small = R(1, 1000), R(1, 100)
A = 1 + M
tilt = -R(10636, 275)
y0 = R(12, 25)/A + nu
b = ((45*M + 18)/(25*A) - R(3, 5)*X
     + omega + tilt*(X - R(1, 5)))
xsheet = -R(1, 5) + X
ysheet = R(3, 5) + S*y0
Zsheet = R(9, 13) - X**2 + S*b - S**2*y0**2

mapped = sp.cancel((36*Gamma).subs({
    lam: A/S, x: xsheet, y: ysheet, Z: Zsheet,
}))
Qhat_raw = sp.cancel(25**8*A**8*S**3*mapped)
Qhat = sp.Poly(sp.expand(Qhat_raw), S, X, M, omega, nu,
               domain=sp.QQ).as_expr()
require(sp.factor(mapped - Qhat/(25**8*A**8*S**3)) == 0,
        "lossless clearing identity")
SX = sp.Poly(Qhat, S, X)
require(len(SX.terms()) == 32 and (SX.degree(S), SX.degree(X)) == (7, 4),
        "32-term bidegree-(7,4) quotient")
first_layer = S**3*25**8*M**2*A**8*(5*M**2 + 14*M + 14)
require(sp.factor(5*M**2 + 14*M + 14
                  - (5*(M+R(7, 5))**2 + R(21, 5))) == 0,
        "nonnegative first layer")
core = sp.expand(Qhat - first_layer)
core_sx = sp.Poly(core, S, X)
core_terms = {powers: coefficient for powers, coefficient in core_sx.terms()}
if os.environ.get("INWARD_Z_EXTENSION_DROP_TERM") == "1":
    core_terms.pop(sorted(core_terms)[0])
    core = sp.expand(sum(value*S**powers[0]*X**powers[1]
                         for powers, value in core_terms.items()))
require(len(core_terms) == 32, "32 core coefficients")
require(sum(len(sp.Poly(value, M, omega, nu).terms())
            for value in core_terms.values()) == 1581,
        "1581 centered core monomials")
print("PASS direct quotient/core counts 32/32/1581")

# Recompute all controls on [1/4,131/520] x [0,1/10000].
Xaff = X0 + (X1-X0)*u
cell = sp.expand(core.subs({X: Xaff, S: Smax*tau}))
# Direct splice at the level of the exact cleared gate, before either
# rectangle's Bernstein transform.  This is the X=1/4 endpoint of the frozen
# theorem and the u=0 endpoint of the new cell with the same symbolic S.
old_endpoint_expression = sp.expand(core.subs(X, X0))
new_left_expression = sp.expand(core.subs(X, Xaff).subs(u, 0))
require(sp.expand(old_endpoint_expression-new_left_expression) == 0,
        "exact old/new X=1/4 cleared-gate splice")
degrees, controls = bernstein_controls_2d(cell, tau, u)
radii = (Mrad, small, small)
variables = (M, omega, nu)
lowers = {key: centered_lower(value, variables, radii)
          for key, value in controls.items()}
zeros = sorted(key for key, value in lowers.items() if value == 0)
negative = {key: value for key, value in lowers.items() if value < 0}
strict = {key: value for key, value in lowers.items() if value > 0}
require(not negative, f"negative centered controls {negative}")
# The new cell lies strictly to the right of the old X=3/13 seam.  Its
# artificial S=0 face therefore has a positive inward-displacement reserve;
# unlike the predecessor rectangle, no closure control is expected to vanish.
expected_zeros = []
require(zeros == expected_zeros, f"unexpected closure zero set {zeros}")
require(all(sp.expand(controls[key]) == 0 for key in zeros),
        "closure controls identically zero")
require(len(strict) == len(controls), "every cell control is strict")
minimum_index, reserve = min(strict.items(), key=lambda item: item[1])
tau_zero_strict = {(i, jidx): value for (i, jidx), value in strict.items()
                   if i == 0}
require(len(tau_zero_strict) == degrees[1]+1,
        "complete tau=0 row is strict on the new cell")
tau_zero_minimum_index, tau_zero_reserve = min(
    tau_zero_strict.items(), key=lambda item: item[1]
)
tau_zero_polynomial = sp.factor(controls[tau_zero_minimum_index])
require(centered_lower(tau_zero_polynomial, variables, radii)
        == tau_zero_reserve, "tau=0 minimum polynomial/lower match")
# At the old global cell's left seam, the same core vanishes at S=0.  The
# new cell starts strictly to its right, so the predecessor's artificial
# closure zeros are not invariants of the polynomial and need not recur.
require(sp.expand(core.subs({S: 0, X: R(3, 13)})) == 0,
        "old S=0 left-seam core zero")

# Every physical tau>0 gets positive Bernstein weight from a strict row.
strict_rows = sorted({i for i, _ in strict})
require(2 in strict_rows, "strict tau^2 row retained")
row_weight = sp.expand(sum(
    sp.binomial(degrees[0], i)*tau**i*(1-tau)**(degrees[0]-i)
    for i in strict_rows
))
require(row_weight.subs(tau, 1) == 1, "strict row weight at tau=1")
print("PASS first endpoint cell exact centered Bernstein certificate")

# Exact endpoint legality and classification.
y0max = sp.factor(y0.subs({M: -Mrad, nu: small}))
bmin_endpoint = sp.factor(b.subs({X: X1, M: -Mrad, omega: -small}))
Zmin_endpoint = sp.factor(
    R(9, 13) - X1**2 + Smax*bmin_endpoint - Smax**2*y0max**2
)
T = sp.factor(R(6, 5)*y0 + b)
danger = sp.factor(1 - xsheet**2 - ysheet**2 - Zsheet)
danger_formula = sp.factor(R(2, 5)*(X-R(3, 13)) - S*T)
require(sp.factor(danger-danger_formula) == 0, "exact danger identity")
Tmax = sp.factor(T.subs({M: Mrad, omega: small, nu: small}))
require(sp.diff(Tmax, X) < 0, "danger envelope improves in X")
danger_lower_endpoint = sp.factor(
    R(2, 5)*(X1-R(3, 13)) + Smax/R(100)
)
require(Zmin_endpoint > 0 and danger_lower_endpoint > 0,
        "strict endpoint legality")
det_lower_endpoint = sp.factor(R(5, 9)*Smax*Zmin_endpoint)
require(det_lower_endpoint > 0, "rank-two endpoint determinant")

print("CELL_ENDPOINTS", X0, X1)
print("BERNSTEIN_DEGREE_TAU_U", degrees)
print("BERNSTEIN_CONTROL_COUNT", len(controls))
print("BERNSTEIN_ZERO_SET", zeros)
print("BERNSTEIN_STRICT_COUNT", len(strict))
print("BERNSTEIN_MIN_STRICT_INDEX", minimum_index)
print("BERNSTEIN_MIN_STRICT_RESERVE", reserve)
print("TAU_ZERO_MIN_INDEX", tau_zero_minimum_index)
print("TAU_ZERO_MIN_RESERVE", tau_zero_reserve)
print("TAU_ZERO_MIN_CONTROL_POLYNOMIAL", tau_zero_polynomial)
print("SPLICE_X", X0)
print("SPLICE_CLEARED_GATE_IDENTITY", "PASS")
print("BERNSTEIN_STRICT_ROWS", strict_rows)
print("BERNSTEIN_STRICT_ROW_WEIGHT", row_weight)
print("B_MIN_ENDPOINT", bmin_endpoint)
print("Z_MIN_ENDPOINT", Zmin_endpoint)
print("DANGER_LOWER_ENDPOINT", danger_lower_endpoint)
print("DET_C_LOWER_ENDPOINT", det_lower_endpoint)
print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact proof candidate on [1/4,131/520]")
print("SCOPE endpoint cell only; full compact ball/common metric/fixed lens open")
