#!/usr/bin/env python3
"""Exact endpoint preflight for the recentered inward-Z chart on 39/40<=X<=1.

This is deliberately not a Bernstein source candidate.  It binds the frozen
X<=39/40 source and independent referee artifacts, rebuilds the original
fully conjugated Hermitian Q,Q^2 gate through the frozen self-contained
builder, checks the three splice layers at X=39/40, and then decides the
complete chart-legality gate before any 40-control expansion is attempted.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run endpoint preflight with -O")

from hashlib import sha256
from pathlib import Path
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: X=1 endpoint preflight accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    "tmp/research/compact_ball_inward_z_recentered_lift_x39_40_exact_gate.py":
        "fd2478e01760b932f1e331022b9719720e0a228170314920288fac433d307087",
    "tmp/research/compact_ball_inward_z_recentered_lift_x39_40_source_freeze_manifest.sha256":
        "517866298fbb674efbfc90c0b93cd6494a2bb4b26c5037f638ecafd63eb8852d",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x39_40_independent_referee.py":
        "b7b84114d358e65b8bc6f16419cfa3ffde1b0b32c1b58399712ac44d44ae58ba",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X39_40_INDEPENDENT_REFEREE_AUDIT.md":
        "61536f6e9a4155ce456495eb6132ef244996b79dda0ef070dc0cb245ee82dbad",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x39_40_independent_referee_manifest.sha256":
        "a5af10c556602ba6ad49ced87718805fbb1e5af0123f4191ce6266b3a460fd8d",
}


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"X=1 endpoint preflight failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")
print("PASS frozen X<=39/40 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    actual = source.count(old)
    require(actual == count,
            f"specialization multiplicity {old!r}: expected {count}, got {actual}")
    return source.replace(old, new)


# Execute only the original-definition reconstruction and splice portion of
# the frozen builder.  The cut occurs before cell substitution and therefore
# before any 40-control Bernstein expansion.
source = (ROOT / BUILDER).read_text(encoding="utf-8")
source = replace_exact(source, "Xleft = R(17, 20)",
                       "Xleft = R(39, 40)", 1)
source = replace_exact(source, "Xright = R(7, 8)",
                       "Xright = R(1)", 1)
source = replace_exact(source, "at X=17/20", "at X=39/40", 2)
marker = "# One exact Bernstein cell only."
require(source.count(marker) == 1, "unique pre-control cut marker")
source = source.split(marker, 1)[0]

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)

sp = namespace["sp"]
R = namespace["R"]
S, X = namespace["S"], namespace["X"]
M, omega, nu = namespace["M"], namespace["omega"], namespace["nu"]
Xanchor = namespace["Xanchor"]
Xleft, Xright = namespace["Xleft"], namespace["Xright"]
K, Smax = namespace["K"], namespace["Smax"]
Mrad = namespace["Mrad"]
omega_rad, nu_rad = namespace["omega_rad"], namespace["nu_rad"]
A, y0, b = namespace["A"], namespace["y0"], namespace["b"]
xsheet, ysheet, Znew = (namespace["xsheet"], namespace["ysheet"],
                        namespace["Znew"])
Qhat, core = namespace["Qhat"], namespace["core"]
v_previous = namespace["v_previous"]
X_previous = namespace["X_previous"]

# The raw-input splice was checked by the executed builder.  Check the two
# polynomial layers separately, without constructing a Bernstein cell.
require(sp.expand(Qhat.subs(X, X_previous).subs(v_previous, 1)
                  - Qhat.subs(X, Xleft)) == 0,
        "cleared raw-gate splice at X=39/40")
require(sp.expand(core.subs(X, X_previous).subs(v_previous, 1)
                  - core.subs(X, Xleft)) == 0,
        "cleared core splice at X=39/40")
print("PASS three-layer X=39/40 parameter/cleared-gate/core splice",
      flush=True)

# Z bounds.  The exact derivative changes sign close to X=1, so the proof
# does not make a false monotonicity claim.  Concavity in X makes an endpoint
# minimum sufficient, while b<0 gives a simple strict upper bound by the
# S=0 parabola.
Zderivative = sp.factor(sp.diff(Znew, X))
require(sp.factor(Zderivative-(K-2*X-R(10801, 275)*S)) == 0,
        "exact Z derivative")
dZ_lower = sp.factor(K-2*Xright-R(10801, 275)*Smax)
dZ_upper = sp.factor(K-2*Xleft)
require(dZ_lower < 0 < dZ_upper, "exact derivative sign change bracket")
require(sp.diff(Znew, X, 2) == -2, "strict X-concavity")

y0min = sp.factor(y0.subs({M: Mrad, nu: -nu_rad}))
y0max = sp.factor(y0.subs({M: -Mrad, nu: nu_rad}))
bmax = sp.factor(b.subs({X: Xleft, M: Mrad, omega: omega_rad}))
require(0 < y0min <= y0max and bmax < 0, "uniform y0>0 and b<0")
require(sp.factor(sp.diff(b, M)-R(27, 25)/A**2) == 0
        and sp.diff(b, omega) == 1
        and sp.diff(b, X) == -R(10801, 275),
        "exact b monotonicity")
require(sp.factor(sp.diff(y0, M)+R(12, 25)/A**2) == 0
        and sp.diff(y0, nu) == 1,
        "exact y0 monotonicity")

worst_corner = {S: Smax, M: -Mrad,
                omega: -omega_rad, nu: nu_rad}
Zleft_worst = sp.factor(Znew.subs({X: Xleft, **worst_corner}))
Zright_worst = sp.factor(Znew.subs({X: Xright, **worst_corner}))
Zmin = min(Zleft_worst, Zright_worst)
Zupper = sp.factor(R(9, 13)-Xright**2+K*(Xright-Xanchor))
require(0 < Zmin and Zupper < 1, "uniform 0<Z<1")

# Danger and rank-two determinant.  det C=(5/9)SZ stays strictly positive
# for both square-root signs, but the unit-ball danger is negative at an
# explicit legal-parameter point near S=0.  Hence the full cell fails by
# chart illegality, not by a raw-gate sign or a Bernstein certificate.
T = sp.factor(R(6, 5)*y0+b)
Tmax = sp.factor(T.subs({X: Xleft, M: Mrad,
                         omega: omega_rad, nu: nu_rad}))
require(Tmax < 0, "uniform negative danger correction")
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
        "exact danger identity")
danger_base_right = sp.factor(
    R(2, 5)*(Xright-R(3, 13))-K*(Xright-Xanchor)
)
witness = {X: Xright, S: R(1, 1000000), M: R(0),
           omega: R(0), nu: R(0)}
danger_witness = sp.factor(danger_new.subs(witness))
Z_witness = sp.factor(Znew.subs(witness))
require(danger_base_right < 0 and danger_witness < 0,
        "exact X=1 chart-illegality witness")
require(0 < Z_witness < 1, "witness retains a real nonzero z coordinate")
det_coefficient = sp.factor(R(5, 9)*Zmin)
require(det_coefficient > 0,
        "uniform det C coefficient for S>0 and both z signs")

print("CELL", Xleft, Xright, flush=True)
print("Z_LEFT_WORST", Zleft_worst, flush=True)
print("Z_RIGHT_WORST", Zright_worst, flush=True)
print("Z_MIN", Zmin, flush=True)
print("Z_UPPER_STRICT", Zupper, flush=True)
print("DZ_DX_LOWER", dZ_lower, flush=True)
print("DZ_DX_UPPER_STRICT", dZ_upper, flush=True)
print("T_MAX", Tmax, flush=True)
print("DANGER_BASE_AT_1", danger_base_right, flush=True)
print("DANGER_WITNESS_S_1E6_M0_O0_N0", danger_witness, flush=True)
print("Z_WITNESS", Z_witness, flush=True)
print("DET_C_LOWER_COEFFICIENT", det_coefficient, flush=True)
print("PASS both-z/rank-two determinant algebra", flush=True)
print("CLASSIFICATION CHART_ILLEGAL_AT_X_1", flush=True)
print("NOT_BERNSTEIN_TESTED", flush=True)
print("NOT_RAW_GATE_NEGATIVE", flush=True)
print("NOT_IMPLEMENTATION_OR_RESOURCE_FAILURE", flush=True)
