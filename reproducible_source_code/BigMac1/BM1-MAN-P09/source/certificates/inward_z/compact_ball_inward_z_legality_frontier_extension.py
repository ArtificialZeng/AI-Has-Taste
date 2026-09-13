#!/usr/bin/env python3
"""Exact source candidate up to the inward-Z chart-legality frontier.

The audited predecessor source is executed from its frozen hash, which
rebuilds the signed-z fully conjugated Q,Q^2 raw gate and exact cleared core
from definitions.  This script then generates fresh controls for the new
cell [131/520,83059/100000], tests the rational point just beyond the first
legality root, and checks exact raw-gate nodes.  No predecessor control table
is parsed or reused.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from itertools import product
from pathlib import Path
import os
import runpy
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: legality-frontier source accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = {
    "tmp/research/compact_ball_inward_z_endpoint_extension.py":
        "2ab0f3f532fbfe0d2fc6b2aa3301ff4857f783161f109ad4d846cbcbf266df4f",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_source_candidate.md":
        "146743ebe254682bee761d0378b90a1e76ca139063ca83cb6f5a7c1b625243c9",
    "tmp/research/compact_ball_inward_z_endpoint_extension_source_freeze_manifest.sha256":
        "ae3ede1048aad9625884963ffbff66437dbd6c36540244cdb82a94efb999a0a8",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_independent_referee.py":
        "0928e8ab3c9c6027feb646af68a7dc4d567d34970887eb672520d120c6a387ab",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_ENDPOINT_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md":
        "e217488778451a9745aaa630e943c974f8fc8671577ef40cd008deb36c0e7652",
    "tmp/research/compact_ball_inward_z_endpoint_extension_independent_referee_manifest.sha256":
        "0d4df995e699d2b14206951153838ba0a8a2522a5154fc95a3b9594a6f3de015",
}
if os.environ.get("INWARD_Z_FRONTIER_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"legality-frontier source failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")
print("PASS audited predecessor dependency hashes")

# This execution redoes the predecessor's signed-z frame, Q, Q^2, literal
# fully conjugated gate, clearing, and 40-control proof from definitions.
ns = runpy.run_path(str(ROOT / next(iter(DEPENDENCIES))))
R = sp.Rational
S, X, M = ns["S"], ns["X"], ns["M"]
omega, nu = ns["omega"], ns["nu"]
core, Qhat, mapped = ns["core"], ns["Qhat"], ns["mapped"]
Zsheet, danger = ns["Zsheet"], ns["danger"]
A = ns["A"]
require(not ns["Gamma"].has(ns["q"], ns["h"], ns["zsigned"]),
        "both signed-z lifts cancel from raw gate")
require(sp.factor(mapped-Qhat/(25**8*A**8*S**3)) == 0,
        "lossless positive clearing")
sx = sp.Poly(Qhat, S, X)
require(len(sx.terms()) == 32 and (sx.degree(S), sx.degree(X)) == (7, 4),
        "cleared 32-term bidegree-(7,4) quotient")
core_sx = sp.Poly(core, S, X)
core_terms = {powers: sp.expand(value) for powers, value in core_sx.terms()}
if os.environ.get("INWARD_Z_FRONTIER_DROP_TERM") == "1":
    core_terms.pop(sorted(core_terms)[0])
    core = sp.expand(sum(value*S**powers[0]*X**powers[1]
                         for powers, value in core_terms.items()))
require(len(core_terms) == 32, "32 core coefficients")
require(sum(len(sp.Poly(value, M, omega, nu).terms())
            for value in core_terms.values()) == 1581,
        "1581 centered core monomials")
print("PASS raw gate clearing/core counts 32/32/1581")

tau, u = sp.symbols("tau_frontier u_frontier", real=True)
Smax = R(1, 10000)
left = R(131, 520)
right = R(83059, 100000)
right_bad = R(4153, 5000)
radii = (R(1, 1000), R(1, 100), R(1, 100))
variables = (M, omega, nu)


def controls_for(endpoint):
    Xaff = left + (endpoint-left)*u
    polynomial = sp.expand(core.subs({X: Xaff, S: Smax*tau}))
    degrees, controls = ns["bernstein_controls_2d"](polynomial, tau, u)
    lowers = {key: ns["centered_lower"](value, variables, radii)
              for key, value in controls.items()}
    return Xaff, degrees, controls, lowers


Xaff, degrees, controls, lowers = controls_for(right)
require(degrees == (7, 4) and len(controls) == 40,
        "new-cell bidegree/control count")
require(all(value > 0 for value in lowers.values()),
        "all 40 new-cell centered controls strict")
minimum_index, reserve = min(lowers.items(), key=lambda item: item[1])
expected_reserve = R(
    119539987320009056100108078372012547879,
    718761099264000000000000000000,
)
require((minimum_index, reserve) == ((0, 0), expected_reserve),
        "exact weakest new-cell control")
minimum_polynomial = sp.factor(controls[minimum_index])
expected_factor = R(
    461578369140625,
    2741856,
)
require(sp.factor(minimum_polynomial-expected_factor*A**12) == 0,
        "complete weakest-control polynomial")
require(ns["centered_lower"](minimum_polynomial, variables, radii)
        == expected_reserve, "weakest polynomial/lower consistency")
require(sp.expand(core.subs(X, left)-core.subs(X, Xaff).subs(u, 0)) == 0,
        "exact splice to audited X=131/520 endpoint")

# Prove that centered-control positivity persists through the rational point
# just above the first legality root; therefore legality, not L1/Bernstein,
# is the first detected event.
_, bad_degrees, bad_controls, bad_lowers = controls_for(right_bad)
require(bad_degrees == (7, 4) and len(bad_controls) == 40,
        "frontier-bracket control count")
require(all(value > 0 for value in bad_lowers.values()),
        "controls remain strict beyond legality root")
print("PASS 40/40 strict controls through legality-root bracket")

# Full-cell legality by exact monotonicity.  Keep the two equal numerical
# radii named separately so an implementation cannot silently exchange the
# omega and nu roles in the b and y0/T bounds.
Mrad, omega_rad, nu_rad = radii
y0 = ns["y0"]
b = ns["b"]
y0min = sp.factor(y0.subs({M: Mrad, nu: -nu_rad}))
y0max = sp.factor(y0.subs({M: -Mrad, nu: nu_rad}))
bmax = sp.factor(b.subs({X: left, M: Mrad, omega: omega_rad}))
bmin = sp.factor(b.subs({X: right, M: -Mrad, omega: -omega_rad}))
require(0 < y0min <= y0max and bmin <= bmax < 0,
        "uniform y0/b signs")
Zmin_function = sp.factor(
    R(9, 13)-X**2+Smax*b.subs({M: -Mrad, omega: -omega_rad})
    - Smax**2*y0max**2
)
Zmin_derivative = sp.factor(sp.diff(Zmin_function, X))
require(sp.factor(Zmin_derivative+2*X+Smax*R(10801, 275)) == 0,
        "exact worst-case Z derivative")
require(Zmin_derivative.subs(X, left) < 0
        and sp.diff(Zmin_derivative, X) == -2,
        "worst-case Z strictly decreases on the whole frontier bracket")
Zmin = sp.factor(Zmin_function.subs(X, right))
Zbad = sp.factor(Zmin_function.subs(X, right_bad))
require(Zmin == R(160243869095653, 15857127000000000000) > 0,
        "exact positive Z at frozen endpoint")
require(Zbad == -R(103795949201927, 15857127000000000000) < 0,
        "exact rational isolation above first legality root")
Zupper = sp.factor(R(9, 13)-left**2)
require(Zupper < 1, "uniform Z upper bound")

T = sp.factor(R(6, 5)*y0+b)
Tmax = sp.factor(T.subs({X: left, M: Mrad,
                         omega: omega_rad, nu: nu_rad}))
require(Tmax == -R(10931, 13000)
        and sp.factor(sp.diff(T, X)+R(10801, 275)) == 0,
        "danger coefficient improves to the right")
danger_identity = sp.factor(R(2, 5)*(X-R(3, 13))-S*T)
require(sp.factor(danger-danger_identity) == 0,
        "exact full-cell danger identity")
danger_lower = R(11, 1300)+R(10931, 13000)*S
det_coefficient = sp.factor(R(5, 9)*Zmin)
require(det_coefficient
        == R(160243869095653, 28542828600000000000) > 0,
        "rank-two determinant coefficient")
print("PASS full-cell lambda/Z/danger/rank-two legality for both z signs")

# Exact falsification nodes from the original rational raw gate.
middle = sp.factor((left+right)/2)
records = []
for Sv, Xv, Mv, ov, nv in product(
    (R(1, 1000000), R(1, 20000), Smax),
    (left, middle, right),
    (-Mrad, Mrad),
    (-omega_rad, omega_rad),
    (-nu_rad, nu_rad),
):
    subs = {S: Sv, X: Xv, M: Mv, omega: ov, nu: nv}
    value = sp.factor(mapped.subs(subs))
    Zv = sp.factor(Zsheet.subs(subs))
    Dv = sp.factor(danger.subs(subs))
    require(value > 0 and 0 < Zv < 1 and Dv > 0,
            "exact legal raw-gate node")
    records.append((value, Zv, Dv, Sv, Xv, Mv, ov, nv))
require(len(records) == 72, "72 exact new-cell nodes")
node_minimum = min(records, key=lambda row: row[0])
print("PASS 72/72 exact legal raw-gate-positive diagnostic nodes")

print("CELL_ENDPOINTS", left, right)
print("CLEARING_CORE_COUNTS", len(sx.terms()), len(core_terms), 1581)
print("BIDEGREE_CONTROL_COUNT", degrees, len(controls))
print("STRICT_ZERO_COUNTS", len(lowers), 0)
print("MIN_STRICT_INDEX", minimum_index)
print("MIN_STRICT_RESERVE", reserve)
print("MIN_CONTROL_POLYNOMIAL", minimum_polynomial)
print("SPLICE_X", left)
print("B_MIN", bmin)
print("Z_MIN", Zmin)
print("Z_UPPER", Zupper)
print("DANGER_LOWER", danger_lower)
print("DET_C_LOWER", S*det_coefficient)
print("LEGALITY_ROOT_BRACKET", right, right_bad)
print("Z_AT_BRACKET_RIGHT", Zbad)
print("NODE_MIN", node_minimum)
print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact source candidate to rational legality frontier")
print("CLASSIFICATION next event is chart obstruction, not gate counterexample")
print("SCOPE full compact ball/common metric/arbitrary-node/fixed-lens open")
