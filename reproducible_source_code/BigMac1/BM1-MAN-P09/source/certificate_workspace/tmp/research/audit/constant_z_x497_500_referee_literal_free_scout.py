#!/usr/bin/env python3
"""Literal-free independent scout for the constant-Z [99/100,497/500] cell.

The current builder source and its manifest are opaque byte strings: this
module only hashes them.  All mathematics is reconstructed from the original
Hermitian compact-ball definitions.  In particular this file contains no
candidate control table, weakest index, weakest polynomial, or reserve.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x497_500_exact_gate.py"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x497_500_source_freeze_manifest.sha256"

PREV_SOURCE = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x99_100_exact_gate.py"
PREV_SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x99_100_source_freeze_manifest.sha256"
PREV_REFEREE = ROOT / "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee.py"
PREV_REPORT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X99_100_INDEPENDENT_REFEREE_AUDIT.md"
PREV_REF_MANIFEST = ROOT / "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED_SOURCE_SHA = "d38dba1bf18b5906765f217bd764edc974cad2821ee8630fc292cffa77994653"
EXPECTED_MANIFEST_SHA = "e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d"
EXPECTED_DEPENDENCIES = {
    PREV_SOURCE: "a99072346ca9d92e3a5e45600d1de371b2609185bef60b2c069d2a400e1d9322",
    PREV_SOURCE_MANIFEST: "e573ff4ab4ab1f2065ff6c40289aacd19e8629e3bbe53b177cd996c7624d7840",
    PREV_REFEREE: "4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3",
    PREV_REPORT: "cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f",
    PREV_REF_MANIFEST: "378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def is_zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def eliminate(expr: sp.Expr, q: sp.Symbol, z: sp.Symbol, h: sp.Symbol,
              S: sp.Symbol, Z: sp.Symbol) -> sp.Expr:
    """Independent reduction order: q, then signed z, then h."""
    value = sp.expand(expr)
    value = sp.rem(value, q**2 - (1 - S), q)
    value = sp.rem(sp.expand(value), z**2 - Z, z)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    return sp.factor(value)


def explicit_square(matrix: sp.Matrix) -> sp.Matrix:
    """Multiply in the cyclic column order 2,0,1."""
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sum(
        matrix[i, k] * matrix[k, j] for k in (2, 0, 1)
    )))


def centered_lower(poly: sp.Expr, variables: tuple[sp.Symbol, ...],
                   radii: tuple[sp.Rational, ...]) -> sp.Rational:
    result = sp.Rational(0)
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        radius = sp.prod(r**p for r, p in zip(radii, powers))
        result += coefficient if all(p == 0 for p in powers) else -abs(coefficient) * radius
    return sp.factor(result)


def u_then_tau_bernstein(poly: sp.Expr, u: sp.Symbol, tau: sp.Symbol,
                         du: int, dt: int) -> dict[tuple[int, int], sp.Expr]:
    """Dense u-first conversion; normalize indices as (tau,u)."""
    dense = sp.Poly(sp.expand(poly), u, tau)
    require(dense.degree(u) <= du and dense.degree(tau) <= dt,
            "declared bidegree contains dense polynomial")
    coefficients = dict(dense.terms())
    result: dict[tuple[int, int], sp.Expr] = {}
    for j in range(du + 1):
        for i in range(dt + 1):
            value = sp.Rational(0)
            for b in range(j + 1):
                for a in range(i + 1):
                    value += (coefficients.get((b, a), 0)
                              * sp.Rational(math.comb(j, b), math.comb(du, b))
                              * sp.Rational(math.comb(i, a), math.comb(dt, a)))
            result[(i, j)] = sp.factor(value)
    return result


def reconstruct(*, source_path: Path = SOURCE,
                manifest_path: Path = SOURCE_MANIFEST,
                dependency_path: Path = PREV_REFEREE,
                attack: str = "none", diagnostics: bool = True) -> dict[str, object]:
    require(__debug__, "optimized Python is forbidden")
    require(sha(source_path) == EXPECTED_SOURCE_SHA, "frozen candidate source SHA-256")
    require(sha(manifest_path) == EXPECTED_MANIFEST_SHA, "frozen source-manifest SHA-256")
    require(sha(dependency_path) == EXPECTED_DEPENDENCIES[PREV_REFEREE],
            "frozen predecessor-referee SHA-256")
    for path, expected in EXPECTED_DEPENDENCIES.items():
        if path != PREV_REFEREE:
            require(sha(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS opaque source/manifest and predecessor/reduction hashes")
    print("INDEPENDENCE current source and source manifest used only for SHA-256")

    R, I = sp.Rational, sp.I
    S, Z = sp.symbols("S Z", real=True)
    h, q, z = sp.symbols("h q z", real=True)
    lam = sp.symbols("lambda", real=True, positive=True)
    xb, yb = sp.symbols("x_ball y_ball", real=True)
    a, c = sp.sqrt(6) / 6, sp.sqrt(30) / 6
    phase = R(4, 5) + R(3, 5) * I
    p = sp.Matrix([a, 0, c])
    r = sp.Matrix([-a, 0, c * phase])
    f = sp.Matrix([-c * h, q, -a * h * phase])
    U = sp.Matrix.hstack(r, f)
    j = (1 + 5 * xb) / (3 * sp.sqrt(5))
    k = (-3 + 5 * yb) / (3 * sp.sqrt(5))
    ell = sp.sqrt(5) * z / 3
    C = sp.Matrix([[h**2, h * (j + I * k)],
                   [h * (j - I * k), j**2 + k**2 + ell**2]])
    H_direct = sp.expand(U * C * sp.conjugate(U.T))
    # Reversed signed-z Gram construction, independent of direct compression.
    col_z = ell * f
    col_mix = h * r + (j - I * k) * f
    H_gram = sp.expand(col_z * sp.conjugate(col_z.T)
                       + col_mix * sp.conjugate(col_mix.T))
    require(all(is_zero(entry) for entry in H_direct - H_gram),
            "direct compression equals reversed Gram sum")
    H = H_gram
    require(eliminate((sp.conjugate(r.T) * r)[0] - 1, q, z, h, S, Z) == 0,
            "r unit norm")
    require(eliminate((sp.conjugate(f.T) * f)[0] - 1, q, z, h, S, Z) == 0,
            "f unit norm")
    require(eliminate((sp.conjugate(r.T) * f)[0], q, z, h, S, Z) == 0,
            "frame orthogonal")
    require(all(is_zero(entry) for entry in H - sp.conjugate(H.T)), "H Hermitian")
    require(all(is_zero(entry) for entry in H - H.subs(z, -z)), "both signed-z lifts")
    require(eliminate(C.det() - R(5, 9) * S * Z, q, z, h, S, Z) == 0,
            "det(C)=(5/9)SZ")

    Q = sp.expand(lam * H)
    Q2 = explicit_square(Q)
    direct_Q2 = sp.expand(Q * Q)
    for row in range(3):
        for column in range(3):
            require(is_zero(Q2[row, column] - direct_Q2[row, column]),
                    f"Q^2 entry ({row},{column})")
    require(all(is_zero(entry) for entry in Q2 - sp.conjugate(Q2.T)), "Q^2 Hermitian")
    print("PASS signed frame, Hermitian compression and Q^2 9/9")

    xi = sp.expand(Q * p)
    q220 = 0 if attack == "drop-q2" else Q2[2, 0]
    pieces = [
        4 * a**2 * xi[1] * sp.conjugate(xi[1]),
        (c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - q220))
        * sp.conjugate(c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - q220)),
        (c * sp.conjugate(xi[1]) - I * Q2[2, 1])
        * sp.conjugate(c * sp.conjugate(xi[1]) - I * Q2[2, 1]),
        -32 * a**2 * ((xi[0] + sp.conjugate(xi[0])) / 2)**2,
    ]
    literal_gate = sp.expand(sum(pieces))
    eta = sp.expand(H * p)
    H2 = explicit_square(H)
    b0 = sp.Matrix([0, I * a * c, 0])
    linear = sp.Matrix([2 * a * eta[1],
                        c * sp.conjugate(eta[0]) + a * eta[2],
                        c * sp.conjugate(eta[1])])
    quadratic = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector = b0 + lam * linear + lam**2 * quadratic
    vector_gate = sp.expand((sp.conjugate(vector.T) * vector)[0]
                            - 32 * a**2 * lam**2
                            * ((eta[0] + sp.conjugate(eta[0])) / 2)**2)
    require(is_zero(literal_gate - vector_gate),
            "literal fully conjugated gate equals cyclic vector gate")
    gate_shape = eliminate(vector_gate, q, z, h, S, Z)
    require(not gate_shape.has(q, z, h), "all frame radicals cancel")
    require(is_zero(sp.im(gate_shape)), "raw gate real")
    require(sp.Poly(sp.expand(gate_shape), Z).degree() == 4, "raw gate deg_Z=4")
    print("PASS fully conjugated raw gate, radical cancellation and deg_Z=4")

    M, omega, nu = sp.symbols("M omega nu", real=True)
    X, Xprev, u, tau = sp.symbols("X Xprev u tau", real=True)
    A = 1 + M
    anchor = R(83059, 100000)
    Smax = R(1, 10000)
    Xstar = R(1019767, 1040000)
    # Re-derive Xstar from the prior recentered danger slope, not candidate data.
    recentered_base = sp.factor(R(2, 5) * (X - R(3, 13)) - 2 * (X - anchor))
    roots = sp.solve(sp.Eq(recentered_base, 0), X)
    require(roots == [Xstar], "independent recentered danger root")
    Xlo, Xhi = R(99, 100), R(497, 500)
    require(Xstar < Xlo < Xhi < 1, "new cell ordering")
    y0 = R(12, 25) / A + nu
    b = ((45 * M + 18) / (25 * A) - R(3, 5) * X + omega
         - R(10636, 275) * (X - R(1, 5)))
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S * y0
    Z_old = R(9, 13) - X**2 + S * b - S**2 * y0**2
    zfactor = R(2001, 1000) if attack == "bad-normalization" else R(2)
    Z_sheet = Z_old + zfactor * (Xstar - anchor)
    require(is_zero(Z_sheet - (Z_old + 2 * (Xstar - anchor))),
            "claimed constant-Z sparse normalization")

    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)
    require(is_zero(sp.diff(b, M) - R(27, 25) / A**2), "b derivative M")
    require(is_zero(sp.diff(b, X) + R(10801, 275)), "b derivative X")
    require(sp.diff(b, omega) == 1, "b derivative omega")
    require(y0.subs({M: Mhi, nu: nlo}) > 0, "y0 positive")
    require(b.subs({M: Mhi, X: Xlo, omega: whi}) < 0, "b negative")
    dZ = sp.factor(sp.diff(Z_sheet, X))
    require(is_zero(dZ - (-2 * X - R(10801, 275) * S)),
            "constant-Z derivative X")
    dZ_upper = sp.factor(dZ.subs({X: Xlo, S: 0}))
    require(dZ_upper < 0, "Z_X strictly negative")
    require(is_zero(sp.diff(Z_sheet, omega) - S), "Z derivative omega")
    require(is_zero(sp.diff(Z_sheet, nu) + 2 * S**2 * y0), "Z derivative nu")
    require(is_zero(sp.diff(Z_sheet, M) - S * R(27, 25) / A**2
                    - S**2 * R(24, 25) * y0 / A**2), "Z derivative M")
    require(is_zero(sp.diff(Z_sheet, S) - b + 2 * S * y0**2), "Z derivative S")
    Zmin = sp.factor(Z_sheet.subs({S: Smax, X: Xhi, M: Mlo,
                                   omega: wlo, nu: nhi}))
    Zupper = sp.factor(Z_sheet.subs({S: 0, X: Xlo}))
    require(Zmin > 0 and Zupper < 1, "full-cell 0<Z<1 bounds")
    T = sp.factor(R(6, 5) * y0 + b)
    Tmax = sp.factor(T.subs({M: Mhi, X: Xlo, omega: whi, nu: nhi}))
    require(Tmax < 0, "uniform exact Tmax")
    danger_sign = -1 if attack == "flip-danger" else 1
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - danger_sign * Z_sheet)
    danger_base = sp.factor(R(2, 5) * (X - R(3, 13))
                            - 2 * (Xstar - anchor))
    require(is_zero(danger - (danger_base - S * T)),
            "constant-Z danger identity with correct sign")
    danger_left = sp.factor(danger_base.subs(X, Xlo))
    require(danger_left > 0 and sp.diff(danger_base, X) == R(2, 5),
            "danger base positive and increasing on extension cell")
    require(R(5, 9) * Zmin > 0 and 1 + Mlo > 0,
            "det(C), scale and rank-two lower gates")
    print(f"LEGALITY Z_X_UPPER={dZ_upper} ZMIN={Zmin} ZUPPER={Zupper}")
    print(f"LEGALITY TMAX={Tmax} DANGER_BASE_LEFT={danger_left}")
    print("PASS complete Z/danger/det(C)/both-z/positive-scale/rank-two legality")

    # The old recentered X=1 preflight is a chart obstruction only.
    x1_base = sp.factor(recentered_base.subs(X, 1))
    x1_T = sp.factor(T.subs({X: 1, M: 0, omega: 0, nu: 0}))
    x1_sample_S = R(1, 1000000)
    x1_danger = sp.factor(x1_base - x1_sample_S * x1_T)
    require(x1_base < 0 and x1_danger < 0,
            "recentered X=1 has an exact physical chart-illegal sample")
    print(f"X1_PREFLIGHT recentered_base={x1_base} sample_danger={x1_danger}")
    print("X1_SCOPE chart illegality only; no raw-gate negative or maximality inference")

    sheet_gate = sp.cancel(gate_shape.subs({xb: x_sheet, yb: y_sheet,
                                            Z: Z_sheet, lam: A / S}))
    gate36 = sp.cancel(36 * sheet_gate)
    positive = 25**8 * A**8 * S**3
    cleared = sp.factor(positive * gate36)
    require(sp.denom(sp.cancel(cleared)) == 1, "positive clearing polynomial")
    require(sp.cancel(cleared / positive - gate36) == 0,
            "positive clearing reversible")
    layer = S**3 * 25**8 * M**2 * A**8 * (5 * M**2 + 14 * M + 14)
    core = sp.expand(cleared - layer)
    if attack == "drop-core":
        (si, xi_power), coefficient = sp.Poly(core, S, X).terms()[0]
        core = sp.expand(core - coefficient * S**si * X**xi_power)
    cleared_poly, core_poly = sp.Poly(cleared, S, X), sp.Poly(core, S, X)
    require(len(cleared_poly.terms()) == 32, "32 cleared coefficients")
    require(len(core_poly.terms()) == 32, "32 core coefficients")
    require(core_poly.degree(S) == 7 and core_poly.degree(X) == 4,
            "core bidegree (7,4)")
    require(len(sp.Poly(core, S, X, M, omega, nu).terms()) == 1581,
            "1,581 centered monomials")
    if attack == "none":
        (si, xi_power), coefficient = core_poly.terms()[0]
        attacked = sp.expand(core - coefficient * S**si * X**xi_power)
        require(len(sp.Poly(attacked, S, X).terms()) == 31,
                "internal drop-core attack detected")
    print("PASS positive reversible clearing and 32/32/1581 bidegree (7,4)")

    cell = sp.expand(core.subs(X, Xlo + (Xhi - Xlo) * u).subs(S, Smax * tau))
    controls = u_then_tau_bernstein(cell, u, tau, 4, 7)
    require(len(controls) == 40, "40 exact Bernstein controls")
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    lowers = {index: centered_lower(value, (M, omega, nu), radii)
              for index, value in controls.items()}
    require(all(value > 0 for value in lowers.values()), "40/40 strict controls")
    weakest = min(lowers, key=lowers.get)
    require(sum(value == lowers[weakest] for value in lowers.values()) == 1,
            "unique weakest control")
    reserve = sp.factor(lowers[weakest])
    weakest_polynomial = sp.factor(controls[weakest])
    require(centered_lower(weakest_polynomial, (M, omega, nu), radii) == reserve,
            "complete weakest polynomial reproduces reserve")
    print(f"SCOUT_WEAKEST {weakest}")
    print(f"SCOUT_RESERVE {reserve}")
    print(f"SCOUT_WEAKEST_POLYNOMIAL {weakest_polynomial}")
    print("PASS 40/40 strict and unique literal-free reserve derivation")

    # Independently rebuild the previous constant-Z chart with a separate X symbol.
    bprev = ((45 * M + 18) / (25 * A) - R(3, 5) * Xprev + omega
             - R(10636, 275) * (Xprev - R(1, 5)))
    xprev = -R(1, 5) + Xprev
    Zprev = (R(9, 13) - Xprev**2 + S * bprev - S**2 * y0**2
             + 2 * (Xstar - anchor))
    prev_gate = sp.cancel(gate_shape.subs({xb: xprev, yb: y_sheet,
                                           Z: Zprev, lam: A / S}))
    prev_cleared = sp.factor(positive * 36 * prev_gate)
    prev_core = sp.expand(prev_cleared - layer)
    prev_inputs = (xprev, y_sheet, Zprev, A / S)
    new_inputs = (x_sheet, y_sheet, Z_sheet, A / S)
    require(all(is_zero(old.subs(Xprev, Xlo) - new.subs(X, Xlo))
                for old, new in zip(prev_inputs, new_inputs)),
            "parameter splice at X=99/100")
    require(is_zero(prev_cleared.subs(Xprev, Xlo) - cleared.subs(X, Xlo)),
            "cleared raw-gate splice at X=99/100")
    require(is_zero(prev_core.subs(Xprev, Xlo) - core.subs(X, Xlo)),
            "cleared-core splice at X=99/100")
    print("PASS X=99/100 parameter/cleared-gate/cleared-core splice 3/3")

    node_count = 0
    node_minimum = None
    node_data = None
    if diagnostics:
        for sv in (R(1, 1000000), R(1, 20000), Smax):
            for xv in (Xlo, (Xlo + Xhi) / 2, Xhi):
                for mv in (Mlo, Mhi):
                    for ov in (wlo, whi):
                        for nv in (nlo, nhi):
                            data = {S: sv, X: xv, M: mv, omega: ov, nu: nv}
                            require(Z_sheet.subs(data) > 0 and danger.subs(data) > 0,
                                    "diagnostic node legal")
                            value = sp.factor(36 * sheet_gate.subs(data))
                            require(value > 0, "diagnostic raw gate positive")
                            if node_minimum is None or value < node_minimum:
                                node_minimum, node_data = value, (sv, xv, mv, ov, nv)
                            node_count += 1
        require(node_count == 72, "72 exact diagnostic nodes")
        print(f"PASS 72/72 exact nodes, diagnostics only; minimum={node_minimum} at {node_data}")

    print("ATTACK_SCOPE no numerical inference; no CE-046/048/059/060 route reuse")
    print("FORMAL_SCOPE one constant-Z cell only; no full ball/common metric/maximality")
    return {
        "weakest": weakest,
        "reserve": reserve,
        "weakest_polynomial": weakest_polynomial,
        "node_count": node_count,
        "Zmin": Zmin,
        "Zupper": Zupper,
        "Tmax": Tmax,
        "danger_left": danger_left,
        "x1_base": x1_base,
        "x1_danger": x1_danger,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path, default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "bad-normalization", "drop-q2", "flip-danger", "drop-core"
    ), default="none")
    args = parser.parse_args()
    reconstruct(source_path=args.source_path, manifest_path=args.manifest_path,
                dependency_path=args.dependency_path, attack=args.attack)
    print("LITERAL_FREE_SCOUT PASS")


if __name__ == "__main__":
    main()
