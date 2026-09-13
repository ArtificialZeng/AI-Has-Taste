#!/usr/bin/env python3
"""No-import exact referee for the recentered inward-Z X=17/20..7/8 cell.

The frozen candidate source is opaque: this program reads its bytes only to
compute SHA-256.  It reconstructs the Hermitian compression, all nine Q^2
entries, the conjugated raw gate, and a fresh dense tau-first Bernstein
tensor directly from definitions.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_source_freeze_manifest.sha256"
CLAIM_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x7_8_source_candidate.md"
PREVIOUS_SOURCE = ROOT / "tmp/research/compact_ball_inward_z_recentered_lift_x17_20_exact_gate.py"
PREVIOUS_REFEREE = ROOT / "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_independent_referee.py"
PREVIOUS_REPORT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X17_20_INDEPENDENT_REFEREE_AUDIT.md"
PREVIOUS_MANIFEST = ROOT / "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_independent_referee_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED = {
    SOURCE: "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    SOURCE_MANIFEST: "bf68bd1522118abb2d04fff5aeb70443b766250ade53702a9259eaeb88aa384b",
    CLAIM_NOTE: "ebcbadeaa6b69e924a01fefc0ce873aa241abf1a33f1fcc3e217c871a456bc48",
    PREVIOUS_SOURCE: "9875a6d365c0ed8a52deccd85415b7e1e3288778e420ef5415d7f6ce2c827e4d",
    PREVIOUS_REFEREE: "f836630b4f987bf396c66304cdaa8c30bbe5510914acf2025d690201985182cd",
    PREVIOUS_REPORT: "ee88a84387602f040cefc6932d0d7521e59527d1c0d7debf0ae7781eaa291147",
    PREVIOUS_MANIFEST: "aa5b0146e2c1bd6cd7386be7353596a91fef51784af4b0741f142b26be47189c",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def reduce_relations(expr: sp.Expr, zz: sp.Symbol, hh: sp.Symbol,
                     qq: sp.Symbol, SS: sp.Symbol, ZZ: sp.Symbol) -> sp.Expr:
    """Eliminate signed z, then h, then q in a fixed independent order."""
    value = sp.expand(expr)
    value = sp.rem(value, zz**2 - ZZ, zz)
    value = sp.rem(sp.expand(value), hh**2 - SS, hh)
    value = sp.rem(sp.expand(value), qq**2 - (1 - SS), qq)
    return sp.factor(value)


def square_nine(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(3, 3, lambda i, j: sp.expand(
        matrix[i, 0]*matrix[0, j]
        + matrix[i, 1]*matrix[1, j]
        + matrix[i, 2]*matrix[2, j]
    ))


def box_lower(poly: sp.Expr, variables: tuple[sp.Symbol, ...],
              radii: tuple[sp.Rational, ...]) -> sp.Rational:
    total = sp.Rational(0)
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        size = sp.prod(radius**power for radius, power in zip(radii, powers))
        total += coefficient if all(power == 0 for power in powers) else -abs(coefficient)*size
    return sp.factor(total)


def bernstein_tau_then_u(poly: sp.Expr, tau: sp.Symbol, u: sp.Symbol,
                         dt: int, du: int) -> dict[tuple[int, int], sp.Expr]:
    dense = sp.Poly(sp.expand(poly), tau, u)
    require(dense.degree(tau) <= dt and dense.degree(u) <= du,
            "dense tensor lies in declared bidegree")
    coefficients = dict(dense.terms())
    result: dict[tuple[int, int], sp.Expr] = {}
    for i in range(dt + 1):
        for j in range(du + 1):
            value = sp.Rational(0)
            for a in range(i + 1):
                for b in range(j + 1):
                    value += (coefficients.get((a, b), 0)
                              * sp.Rational(math.comb(i, a), math.comb(dt, a))
                              * sp.Rational(math.comb(j, b), math.comb(du, b)))
            result[(i, j)] = sp.factor(value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--dependency-path", type=Path, default=PREVIOUS_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "bad-normalization", "drop-q2", "flip-danger", "drop-core"
    ), default="none")
    args = parser.parse_args()

    require(__debug__, "optimized Python is forbidden")
    require(digest(args.source_path) == EXPECTED[SOURCE], "frozen candidate source SHA-256")
    require(digest(args.dependency_path) == EXPECTED[PREVIOUS_REFEREE],
            "frozen predecessor-referee SHA-256")
    for path, expected in EXPECTED.items():
        if path not in (SOURCE, PREVIOUS_REFEREE):
            require(digest(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS frozen source/manifest/claim/reduction/predecessor hashes")
    print("INDEPENDENCE candidate source bytes used only for SHA-256")

    R, I = sp.Rational, sp.I
    S, Z = sp.symbols("S Z", real=True)
    h, q, z = sp.symbols("h q z", real=True)
    lam = sp.symbols("lambda", real=True, positive=True)
    xb, yb = sp.symbols("x_ball y_ball", real=True)
    a, c = sp.sqrt(6)/6, sp.sqrt(30)/6
    phase = R(4, 5) + R(3, 5)*I
    p = sp.Matrix([a, 0, c])
    r = sp.Matrix([-a, 0, c*phase])
    f = sp.Matrix([-c*h, q, -a*h*phase])
    U = sp.Matrix.hstack(r, f)
    j = (1 + 5*xb)/(3*sp.sqrt(5))
    k = (-3 + 5*yb)/(3*sp.sqrt(5))
    ell = sp.sqrt(5)*z/3
    C = sp.Matrix([[h**2, h*(j + I*k)],
                   [h*(j - I*k), j**2 + k**2 + ell**2]])
    H = sp.expand(U*C*sp.conjugate(U.T))
    # A separately ordered Gram sum attacks mistakes in the compression path.
    g_mix = h*r + (j - I*k)*f
    g_z = ell*f
    H_gram = sp.expand(g_mix*sp.conjugate(g_mix.T) + g_z*sp.conjugate(g_z.T))
    require(all(zero(entry) for entry in H - H_gram), "compression equals Gram sum")
    require(reduce_relations((sp.conjugate(r.T)*r)[0] - 1, z, h, q, S, Z) == 0,
            "r unit norm")
    require(reduce_relations((sp.conjugate(f.T)*f)[0] - 1, z, h, q, S, Z) == 0,
            "f unit norm")
    require(reduce_relations((sp.conjugate(r.T)*f)[0], z, h, q, S, Z) == 0,
            "r and f orthogonal")
    require(all(zero(entry) for entry in H - sp.conjugate(H.T)), "H Hermitian")
    require(all(zero(entry) for entry in H - H.subs(z, -z)), "both signed-z lifts")
    require(reduce_relations(C.det() - R(5, 9)*S*Z, z, h, q, S, Z) == 0,
            "det(C)=(5/9)SZ")

    Q = sp.expand(lam*H)
    Q2 = square_nine(Q)
    Q2_reference = sp.expand(Q*Q)
    for row in range(3):
        for column in range(3):
            require(zero(Q2[row, column] - Q2_reference[row, column]),
                    f"Q^2 entry ({row},{column})")
    require(all(zero(entry) for entry in Q2 - sp.conjugate(Q2.T)), "Q^2 Hermitian")
    print("PASS 9/9 Q^2 entries by explicit scalar multiplication")

    xi = sp.expand(Q*p)
    q220 = 0 if args.attack == "drop-q2" else Q2[2, 0]
    pieces = [
        4*a**2*xi[1]*sp.conjugate(xi[1]),
        (c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - q220))
        * sp.conjugate(c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - q220)),
        (c*sp.conjugate(xi[1]) - I*Q2[2, 1])
        * sp.conjugate(c*sp.conjugate(xi[1]) - I*Q2[2, 1]),
        -32*a**2*((xi[0] + sp.conjugate(xi[0]))/2)**2,
    ]
    if args.attack == "flip-danger":
        pieces[3] = -pieces[3]
    literal_gate = sp.expand(sum(pieces))
    eta = sp.expand(H*p)
    H2 = square_nine(H)
    b0 = sp.Matrix([0, I*a*c, 0])
    linear = sp.Matrix([2*a*eta[1],
                        c*sp.conjugate(eta[0]) + a*eta[2],
                        c*sp.conjugate(eta[1])])
    quadratic = sp.Matrix([0, -I*H2[2, 0], -I*H2[2, 1]])
    vector = b0 + lam*linear + lam**2*quadratic
    vector_gate = sp.expand((sp.conjugate(vector.T)*vector)[0]
                            - 32*a**2*lam**2
                            *((eta[0] + sp.conjugate(eta[0]))/2)**2)
    require(zero(literal_gate - vector_gate), "literal raw gate equals cyclic vector gate")
    gate_shape = reduce_relations(vector_gate, z, h, q, S, Z)
    require(not gate_shape.has(z, h, q), "radicals cancel")
    require(zero(sp.im(gate_shape)), "raw gate real")
    require(sp.Poly(sp.expand(gate_shape), Z).degree() == 4, "raw gate deg_Z=4")
    print("PASS fully conjugated raw gate and exact deg_Z=4")

    M, omega, nu = sp.symbols("M omega nu", real=True)
    X, tau, u = sp.symbols("X tau u", real=True)
    A = 1 + M
    anchor = R(83059, 100000)
    Xlo, Xhi, Smax = R(17, 20), R(7, 8), R(1, 10000)
    y0 = R(12, 25)/A + nu
    b = ((45*M + 18)/(25*A) - R(3, 5)*X + omega
         - R(10636, 275)*(X - R(1, 5)))
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S*y0
    Z_old = R(9, 13) - X**2 + S*b - S**2*y0**2
    multiplier = R(2001, 1000) if args.attack == "bad-normalization" else R(2)
    Z_sheet = Z_old + multiplier*(X - anchor)
    require(zero(Z_sheet - (Z_old + 2*(X - anchor))), "claimed sparse-Z normalization")
    sheet_gate = sp.cancel(gate_shape.subs({xb: x_sheet, yb: y_sheet,
                                            Z: Z_sheet, lam: A/S}))
    gate36 = sp.cancel(36*sheet_gate)
    positive = 25**8*A**8*S**3
    cleared = sp.factor(positive*gate36)
    require(sp.denom(sp.cancel(cleared)) == 1, "positive clearing polynomial")
    require(sp.cancel(cleared/positive - gate36) == 0, "positive clearing reversible")
    layer = S**3*25**8*M**2*A**8*(5*M**2 + 14*M + 14)
    core = sp.expand(cleared - layer)
    if args.attack == "drop-core":
        (si, xi_power), coefficient = sp.Poly(core, S, X).terms()[0]
        core = sp.expand(core - coefficient*S**si*X**xi_power)
    cleared_poly, core_poly = sp.Poly(cleared, S, X), sp.Poly(core, S, X)
    require(len(cleared_poly.terms()) == 34, "34 cleared (S,X) coefficients")
    require(len(core_poly.terms()) == 34, "34 core (S,X) coefficients")
    require(core_poly.degree(S) == 7 and core_poly.degree(X) == 4,
            "core bidegree (7,4)")
    require(len(sp.Poly(core, S, X, M, omega, nu).terms()) == 1659,
            "1,659 centered monomials")
    if args.attack == "none":
        (si, xi_power), coefficient = core_poly.terms()[0]
        attacked = sp.expand(core - coefficient*S**si*X**xi_power)
        require(len(sp.Poly(attacked, S, X).terms()) == 33,
                "internal deleted-core attack detected")
    print("PASS reversible clearing and 34/34/1659 structure")

    cell = sp.expand(core.subs(X, Xlo + (Xhi - Xlo)*u).subs(S, Smax*tau))
    controls = bernstein_tau_then_u(cell, tau, u, 7, 4)
    require(len(controls) == 40, "40 Bernstein controls")
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    lowers = {index: box_lower(value, (M, omega, nu), radii)
              for index, value in controls.items()}
    require(all(value > 0 for value in lowers.values()), "40/40 strict controls")
    weakest = min(lowers, key=lowers.get)
    reserve = R(
        36396400755316082608953526916356109068914066995807402520780718071668303870073911227,
        239735779200073728000000000000000000000000000000000000000000000000000000,
    )
    require(weakest == (7, 0), "weakest=(7,0)")
    require(sum(value == lowers[weakest] for value in lowers.values()) == 1,
            "unique weakest control")
    require(lowers[weakest] == reserve, "exact weakest reserve")
    weakest_polynomial = sp.factor(controls[weakest])
    require(box_lower(weakest_polynomial, (M, omega, nu), radii) == reserve,
            "complete weakest polynomial reproduces reserve")
    print("PASS bidegree (7,4), 40/40 strict controls, unique weakest=(7,0)")
    print(f"WEAKEST_RESERVE {reserve}")
    print(f"WEAKEST_POLYNOMIAL {weakest_polynomial}")

    # Reconstruct the preceding restriction with a separately named variable.
    Xprevious = sp.symbols("Xprevious", real=True)
    b_previous = ((45*M + 18)/(25*A) - R(3, 5)*Xprevious + omega
                  - R(10636, 275)*(Xprevious - R(1, 5)))
    Z_previous = (R(9, 13) - Xprevious**2 + S*b_previous - S**2*y0**2
                  + 2*(Xprevious - anchor))
    previous_gate = sp.cancel(gate_shape.subs({xb: -R(1, 5) + Xprevious,
                                               yb: y_sheet, Z: Z_previous,
                                               lam: A/S}))
    previous_cleared = sp.factor(positive*36*previous_gate)
    previous_core = sp.expand(previous_cleared - layer)
    require(zero(previous_cleared.subs(Xprevious, Xlo) - cleared.subs(X, Xlo)),
            "cleared-gate splice at X=17/20")
    require(zero(previous_core.subs(Xprevious, Xlo) - core.subs(X, Xlo)),
            "cleared-core splice at X=17/20")
    old_inputs = (-R(1, 5) + Xprevious, y_sheet, Z_previous, A/S)
    new_inputs = (x_sheet, y_sheet, Z_sheet, A/S)
    require(all(zero(old.subs(Xprevious, Xlo) - new.subs(X, Xlo))
                for old, new in zip(old_inputs, new_inputs)),
            "parameter splice at X=17/20")
    print("PASS parameter, cleared-gate, and cleared-core splice at X=17/20")

    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)
    require(zero(sp.diff(b, M) - R(27, 25)/A**2), "b derivative M")
    require(zero(sp.diff(b, X) + R(10801, 275)), "b derivative X")
    require(sp.diff(b, omega) == 1, "b derivative omega")
    require(y0.subs({M: Mhi, nu: nlo}) > 0, "y0 positive")
    require(b.subs({M: Mhi, X: Xlo, omega: whi}) < 0, "b negative")
    dZ = sp.factor(sp.diff(Z_sheet, X))
    require(zero(dZ - (2 - 2*X - R(10801, 275)*S)), "Z derivative X")
    require(dZ.subs({X: Xhi, S: Smax}) == R(676699, 2750000),
            "positive dZ/dX lower")
    require(zero(sp.diff(Z_sheet, omega) - S), "Z derivative omega")
    require(zero(sp.diff(Z_sheet, nu) + 2*S**2*y0), "Z derivative nu")
    require(zero(sp.diff(Z_sheet, M) - S*R(27, 25)/A**2
                 - S**2*R(24, 25)*y0/A**2), "Z derivative M")
    require(zero(sp.diff(Z_sheet, S) - b + 2*S*y0**2), "Z derivative S")
    Zmin = sp.factor(Z_sheet.subs({S: Smax, X: Xlo, M: Mlo,
                                   omega: wlo, nu: nhi}))
    require(Zmin == R(97261562093134873, 15857127000000000000) and Zmin > 0,
            "exact Z lower")
    Zupper = sp.factor(Z_sheet.subs({S: 0, X: Xhi}))
    require(Zupper == R(40307, 2600000) and Zupper < 1, "strict Z upper")
    T = sp.factor(R(6, 5)*y0 + b)
    Tmax = sp.factor(T.subs({M: Mhi, X: Xlo, omega: whi, nu: nhi}))
    require(Tmax == -R(434919, 17875) and Tmax < 0, "exact T maximum")
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - Z_sheet)
    danger_formula = R(2, 5)*(X - R(3, 13)) - 2*(X - anchor) - S*T
    require(zero(danger - danger_formula), "exact danger identity")
    danger_floor = sp.factor(R(2, 5)*(Xhi - R(3, 13)) - 2*(Xhi - anchor))
    require(danger_floor == R(109767, 650000) and danger_floor > 0,
            "exact danger lower")
    require(R(5, 9)*Zmin
            == R(97261562093134873, 28542828600000000000),
            "exact det(C) coefficient")
    require(1 + Mlo > 0, "lambda positive")
    print("PASS full lambda/Z/danger/det(C)/rank-two legality for both signed-z lifts")

    sample_S = [R(1, 1000000), R(1, 20000), Smax]
    sample_X = [Xlo, (Xlo + Xhi)/2, Xhi]
    count, minimum, minimum_data = 0, None, None
    for sv in sample_S:
        for xv in sample_X:
            for mv in (Mlo, Mhi):
                for ov in (wlo, whi):
                    for nv in (nlo, nhi):
                        data = {S: sv, X: xv, M: mv, omega: ov, nu: nv}
                        require(Z_sheet.subs(data) > 0 and danger.subs(data) > 0,
                                "diagnostic node legal")
                        value = sp.factor(36*sheet_gate.subs(data))
                        require(value > 0, "diagnostic raw gate positive")
                        if minimum is None or value < minimum:
                            minimum, minimum_data = value, (sv, xv, mv, ov, nv)
                        count += 1
    require(count == 72, "72 exact nodes")
    print("PASS 72/72 exact legal raw-gate nodes (diagnostic only)")
    print(f"NODE_MIN {minimum} AT {minimum_data}")
    print("ROUTE no real-part monotonicity, center absorption, fixed s=-2, or Z=0 remainder")
    print("SCOPE adjacent local chart only; no raw negative/maximality/full-ball/common-metric claim")


if __name__ == "__main__":
    main()
