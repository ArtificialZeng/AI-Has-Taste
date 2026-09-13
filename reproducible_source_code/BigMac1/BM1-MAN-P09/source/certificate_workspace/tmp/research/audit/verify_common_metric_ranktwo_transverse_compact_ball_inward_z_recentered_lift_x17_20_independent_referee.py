#!/usr/bin/env python3
"""Independent exact referee for the recentered inward-Z X17/20 lift.

The frozen candidate source is read only as opaque bytes for its SHA-256.
No candidate coefficient, control, intermediate expression, or helper is
imported, executed, parsed, or otherwise reused.  This verifier starts from
reversed signed-z Gram columns, forms all nine entries of Q^2 by explicit
matrix multiplication, reconstructs the fully conjugated raw gate, and uses
a dense tau-first Bernstein conversion on the claimed cell.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_recentered_lift_x17_20_exact_gate.py"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_recentered_lift_x17_20_source_freeze_manifest.sha256"
CLAIM_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x17_20_source_candidate.md"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"
PREDECESSOR_REFEREE = ROOT / "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_independent_referee.py"
PREDECESSOR_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_LEGALITY_FRONTIER_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md"

EXPECTED_HASHES = {
    SOURCE: "9875a6d365c0ed8a52deccd85415b7e1e3288778e420ef5415d7f6ce2c827e4d",
    SOURCE_MANIFEST: "d32d987a7ed49e3be0b68742e994fb6810b8e164022040bbafab0a305ad75a87",
    CLAIM_NOTE: "d4e4e011e67169e272412cf848a4f31863f0e3f20afcbf3d27cb9a20b8d99db3",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
    PREDECESSOR_REFEREE: "9d00fc3b026bd6751831e412205fb2803a9026c6eba38c408f5c861f886b1642",
    PREDECESSOR_AUDIT: "44ac690f65bf7b6ce7a4be8320ed8406e4e4dae167673117435d5f95b8865591",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def exact_zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def quotient_reduce(expr: sp.Expr, hh: sp.Symbol, qq: sp.Symbol,
                    zz: sp.Symbol, SS: sp.Symbol, ZZ: sp.Symbol) -> sp.Expr:
    """Eliminate h, then q, then signed z; no source reduction is reused."""
    value = sp.expand(expr)
    value = sp.rem(value, hh**2 - SS, hh)
    value = sp.rem(sp.expand(value), qq**2 - (1 - SS), qq)
    value = sp.rem(sp.expand(value), zz**2 - ZZ, zz)
    return sp.factor(value)


def manual_square(matrix: sp.Matrix) -> sp.Matrix:
    """Build every square entry from its three scalar products."""
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sum(
        matrix[i, k] * matrix[k, j] for k in range(3)
    )))


def centered_l1_lower(poly: sp.Expr,
                      variables: tuple[sp.Symbol, ...],
                      radii: tuple[sp.Rational, ...]) -> sp.Rational:
    """Exact centered coefficient-l1 lower bound on a symmetric box."""
    total = sp.Rational(0)
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        weight = sp.prod(radius**power for radius, power in zip(radii, powers))
        total += coefficient if all(power == 0 for power in powers) else -abs(coefficient) * weight
    return sp.factor(total)


def tau_first_bernstein(poly: sp.Expr, tau: sp.Symbol, u: sp.Symbol,
                        degree_tau: int, degree_u: int) -> dict[tuple[int, int], sp.Expr]:
    """Dense monomial-to-Bernstein transform, tau axis before u axis."""
    dense = sp.Poly(sp.expand(poly), tau, u)
    require(dense.degree(tau) <= degree_tau and dense.degree(u) <= degree_u,
            "declared Bernstein degree contains the dense polynomial")
    monomial = dict(dense.terms())
    controls: dict[tuple[int, int], sp.Expr] = {}
    for i in range(degree_tau + 1):
        for j in range(degree_u + 1):
            value = sp.Rational(0)
            for a_index in range(i + 1):
                for b_index in range(j + 1):
                    value += (
                        monomial.get((a_index, b_index), 0)
                        * sp.Rational(math.comb(i, a_index), math.comb(degree_tau, a_index))
                        * sp.Rational(math.comb(j, b_index), math.comb(degree_u, b_index))
                    )
            controls[(i, j)] = sp.factor(value)
    return controls


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument(
        "--attack",
        choices=("none", "bad-normalization", "drop-q2", "flip-danger", "drop-core"),
        default="none",
    )
    args = parser.parse_args()

    require(__debug__, "optimized Python is forbidden")
    require(sha256(args.source_path) == EXPECTED_HASHES[SOURCE],
            "frozen candidate source SHA-256")
    for path, expected in EXPECTED_HASHES.items():
        if path != SOURCE:
            require(sha256(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS frozen source/manifest/claim/reduction/predecessor hashes")
    print("INDEPENDENCE candidate source bytes were used only for SHA-256")

    R = sp.Rational
    I = sp.I
    S, Z = sp.symbols("S Z", real=True)
    h, q, z = sp.symbols("h q z", real=True)
    lam = sp.symbols("lambda", real=True, positive=True)
    x_ball, y_ball = sp.symbols("x_ball y_ball", real=True)

    a = sp.sqrt(6) / 6
    c = sp.sqrt(30) / 6
    phase = R(4, 5) + R(3, 5) * I
    p = sp.Matrix([a, 0, c])
    r = sp.Matrix([-a, 0, c * phase])
    f = sp.Matrix([-c*h, q, -a*h*phase])
    j = (1 + 5*x_ball) / (3*sp.sqrt(5))
    k = (-3 + 5*y_ball) / (3*sp.sqrt(5))
    ell = sp.sqrt(5)*z / 3

    # Reversed Gram-column order rather than the candidate sparse pre-map.
    g_z = ell*f
    g_mix = h*r + (j - I*k)*f
    H = sp.expand(g_z*sp.conjugate(g_z.T) + g_mix*sp.conjugate(g_mix.T))
    require(quotient_reduce((sp.conjugate(r.T)*r)[0] - 1, h, q, z, S, Z) == 0,
            "r is a unit vector")
    require(quotient_reduce((sp.conjugate(f.T)*f)[0] - 1, h, q, z, S, Z) == 0,
            "f is a unit vector")
    require(quotient_reduce((sp.conjugate(r.T)*f)[0], h, q, z, S, Z) == 0,
            "r and f are orthogonal")
    require(all(exact_zero(entry) for entry in H - sp.conjugate(H.T)),
            "H is Hermitian")
    require(all(exact_zero(entry) for entry in H - H.subs(z, -z)),
            "both signed-z lifts give identical H")

    compression = sp.Matrix([[h**2, h*(j + I*k)],
                             [h*(j - I*k), j**2 + k**2 + ell**2]])
    require(quotient_reduce(compression.det() - R(5, 9)*S*Z,
                            h, q, z, S, Z) == 0,
            "compression determinant is (5/9)SZ")

    Q = sp.expand(lam*H)
    Q2 = manual_square(Q)
    matrix_Q2 = sp.expand(Q*Q)
    for row in range(3):
        for column in range(3):
            require(exact_zero(Q2[row, column] - matrix_Q2[row, column]),
                    f"Q^2 entry ({row},{column})")
    require(all(exact_zero(entry) for entry in Q2 - sp.conjugate(Q2.T)),
            "all nine Q^2 entries are Hermitian")
    print("PASS all 9/9 Q^2 entries reconstructed by explicit multiplication")

    xi = sp.expand(Q*p)
    raw_Q2_20 = 0 if args.attack == "drop-q2" else Q2[2, 0]
    literal_terms = [
        4*a**2*xi[1]*sp.conjugate(xi[1]),
        (c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - raw_Q2_20))
        * sp.conjugate(c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - raw_Q2_20)),
        (c*sp.conjugate(xi[1]) - I*Q2[2, 1])
        * sp.conjugate(c*sp.conjugate(xi[1]) - I*Q2[2, 1]),
        -32*a**2*((xi[0] + sp.conjugate(xi[0]))/2)**2,
    ]
    if args.attack == "flip-danger":
        literal_terms[3] = -literal_terms[3]
    gamma_literal = sp.expand(sum(literal_terms))

    eta = sp.expand(H*p)
    H2 = manual_square(H)
    B0 = sp.Matrix([0, I*a*c, 0])
    linear = sp.Matrix([2*a*eta[1],
                        c*sp.conjugate(eta[0]) + a*eta[2],
                        c*sp.conjugate(eta[1])])
    quadratic = sp.Matrix([0, -I*H2[2, 0], -I*H2[2, 1]])
    vector = B0 + lam*linear + lam**2*quadratic
    gamma_vector = sp.expand((sp.conjugate(vector.T)*vector)[0]
                             - 32*a**2*lam**2
                             * ((eta[0] + sp.conjugate(eta[0]))/2)**2)
    require(exact_zero(gamma_literal - gamma_vector),
            "literal fully conjugated raw gate equals cyclic vector gate")
    gamma_shape = quotient_reduce(gamma_vector, h, q, z, S, Z)
    require(not gamma_shape.has(h, q, z), "frame and signed-z radicals cancel")
    require(exact_zero(sp.im(gamma_shape)), "reconstructed raw gate is real")
    require(sp.Poly(sp.expand(gamma_shape), Z).degree() == 4,
            "exact compact raw gate degree in Z is four")
    print("PASS fully conjugated raw gate and exact deg_Z=4")

    M, omega, nu = sp.symbols("M omega nu", real=True)
    X, tau, u = sp.symbols("X tau u", real=True)
    A = 1 + M
    X0 = R(83059, 100000)
    X1 = R(17, 20)
    Smax = R(1, 10000)
    y0 = R(12, 25)/A + nu
    b = ((45*M + 18)/(25*A) - R(3, 5)*X + omega
         - R(10636, 275)*(X - R(1, 5)))
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S*y0
    lift_coefficient = R(1999, 1000) if args.attack == "bad-normalization" else R(2)
    Z_old = R(9, 13) - X**2 + S*b - S**2*y0**2
    Z_sheet = Z_old + lift_coefficient*(X - X0)
    require(exact_zero(Z_sheet - (Z_old + 2*(X - X0))),
            "claimed sparse recentered-Z normalization")

    sheet_gate = sp.cancel(gamma_shape.subs({x_ball: x_sheet,
                                             y_ball: y_sheet,
                                             Z: Z_sheet,
                                             lam: A/S}))
    gate36 = sp.cancel(36*sheet_gate)
    positive_factor = 25**8*A**8*S**3
    cleared = sp.factor(positive_factor*gate36)
    require(sp.denom(sp.cancel(cleared)) == 1,
            "positive clearing produces a polynomial")
    require(sp.cancel(cleared/positive_factor - gate36) == 0,
            "positive clearing is exactly reversible")
    layer = S**3*25**8*M**2*A**8*(5*M**2 + 14*M + 14)
    core = sp.expand(cleared - layer)
    if args.attack == "drop-core":
        (s_power, x_power), coefficient = sp.Poly(core, S, X).terms()[0]
        core = sp.expand(core - coefficient*S**s_power*X**x_power)

    before = sp.Poly(cleared, S, X)
    after = sp.Poly(core, S, X)
    require(len(before.terms()) == 34,
            "34 nonzero (S,X) coefficients before layer removal")
    require(len(after.terms()) == 34,
            "34 nonzero (S,X) coefficients after layer removal")
    require(after.degree(S) == 7 and after.degree(X) == 4,
            "core bidegree is (7,4)")
    require(len(sp.Poly(core, S, X, M, omega, nu).terms()) == 1659,
            "core has 1,659 centered monomials")
    if args.attack == "none":
        attacked = sp.expand(core - after.terms()[0][1]
                             * S**after.terms()[0][0][0] * X**after.terms()[0][0][1])
        require(len(sp.Poly(attacked, S, X).terms()) == 33,
                "internal drop-core attack is detected by the 34-term gate")
    print("PASS reversible positive clearing and 34/34/1659 structure")
    print("PASS internal deleted-core attack changes the structural count")

    Xmap = X0 + (X1 - X0)*u
    cell = sp.expand(core.subs(X, Xmap).subs(S, Smax*tau))
    controls = tau_first_bernstein(cell, tau, u, 7, 4)
    require(len(controls) == 40, "exactly 40 Bernstein controls")
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    lowers = {index: centered_l1_lower(value, (M, omega, nu), radii)
              for index, value in controls.items()}
    require(all(value > 0 for value in lowers.values()),
            "all 40 centered lower controls are strict")
    weakest = min(lowers, key=lowers.get)
    expected_reserve = R(
        4989868253428042904100458867373768732890103155600729500817292846407383462088295685657449907,
        37458715500011520000000000000000000000000000000000000000000000000000000000000000,
    )
    require(weakest == (7, 0), "weakest Bernstein control index is (7,0)")
    require(sum(value == lowers[weakest] for value in lowers.values()) == 1,
            "the weakest centered lower control is unique")
    require(lowers[weakest] == expected_reserve,
            "exact weakest centered reserve")
    weakest_polynomial = sp.factor(controls[weakest])
    require(centered_l1_lower(weakest_polynomial, (M, omega, nu), radii)
            == expected_reserve,
            "complete weakest-control polynomial reproduces the reserve")
    print("PASS bidegree (7,4) and 40/40 strict exact Bernstein controls")
    print(f"WEAKEST_INDEX {weakest}")
    print(f"WEAKEST_RESERVE {expected_reserve}")
    print(f"WEAKEST_POLYNOMIAL {weakest_polynomial}")

    # Definition-level predecessor splice: compare every raw-gate input.
    Xold = sp.symbols("Xold", real=True)
    bold = ((45*M + 18)/(25*A) - R(3, 5)*Xold + omega
            - R(10636, 275)*(Xold - R(1, 5)))
    Zold_predecessor = R(9, 13) - Xold**2 + S*bold - S**2*y0**2
    old_inputs = (-R(1, 5) + Xold, y_sheet, Zold_predecessor, A/S)
    new_inputs = (x_sheet, y_sheet, Z_sheet, A/S)
    require(all(exact_zero(old.subs(Xold, X0) - new.subs(X, X0))
                for old, new in zip(old_inputs, new_inputs)),
            "old endpoint/new cell splice for every raw-gate input")
    old_gate = sp.cancel(gamma_shape.subs({x_ball: old_inputs[0],
                                           y_ball: old_inputs[1],
                                           Z: old_inputs[2], lam: old_inputs[3]}))
    old_cleared = sp.factor(positive_factor*36*old_gate)
    require(exact_zero(old_cleared.subs(Xold, X0) - cleared.subs(X, X0)),
            "termwise cleared-gate splice at X=83059/100000")
    print("PASS exact parameter-by-parameter predecessor splice")

    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)
    require(exact_zero(sp.diff(b, M) - R(27, 25)/A**2), "b derivative in M")
    require(exact_zero(sp.diff(b, X) + R(10801, 275)), "b derivative in X")
    require(sp.diff(b, omega) == 1, "b derivative in omega")
    y0_min = sp.factor(y0.subs({M: Mhi, nu: nlo}))
    b_max = sp.factor(b.subs({M: Mhi, X: X0, omega: whi}))
    require(y0_min > 0 and b_max < 0, "uniform y0>0 and b<0")

    dZ_dX = sp.factor(sp.diff(Z_sheet, X))
    require(exact_zero(dZ_dX - (2 - 2*X - R(10801, 275)*S)),
            "exact positive X derivative of Z")
    derivative_lower = sp.factor(dZ_dX.subs({X: X1, S: Smax}))
    require(derivative_lower == R(814199, 2750000) and derivative_lower > 0,
            "full-cell positive X derivative lower bound")
    require(exact_zero(sp.diff(Z_sheet, omega) - S), "Z derivative in omega")
    require(exact_zero(sp.diff(Z_sheet, nu) + 2*S**2*y0), "Z derivative in nu")
    require(exact_zero(sp.diff(Z_sheet, M)
                       - S*R(27, 25)/A**2
                       - S**2*R(24, 25)*y0/A**2),
            "Z derivative in M")
    require(exact_zero(sp.diff(Z_sheet, S) - b + 2*S*y0**2),
            "Z derivative in S")
    Z_min = sp.factor(Z_sheet.subs({S: Smax, X: X0, M: Mlo,
                                    omega: wlo, nu: nhi}))
    expected_Z_min = R(160243869095653, 15857127000000000000)
    require(Z_min == expected_Z_min and Z_min > 0, "exact positive Z minimum")
    Z_upper = sp.factor(Z_sheet.subs({S: 0, X: X1}))
    require(Z_upper == R(701, 81250) and Z_upper < 1,
            "strict global Z upper endpoint")

    T = sp.factor(R(6, 5)*y0 + b)
    T_max = sp.factor(T.subs({M: Mhi, X: X0, omega: whi, nu: nhi}))
    require(T_max == -R(8425838367, 357500000) and T_max < 0,
            "exact negative full-cell T maximum")
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - Z_sheet)
    danger_identity = (R(2, 5)*(X - R(3, 13))
                       - 2*(X - X0) - S*T)
    require(exact_zero(danger - danger_identity), "literal danger identity")
    danger_floor = sp.factor(R(2, 5)*(X1 - R(3, 13)) - 2*(X1 - X0))
    require(danger_floor == R(135767, 650000) and danger_floor > 0,
            "exact full-cell danger lower bound")
    det_coefficient = sp.factor(R(5, 9)*Z_min)
    require(det_coefficient
            == R(160243869095653, 28542828600000000000),
            "exact determinant lower coefficient")
    require(1 + Mlo > 0, "lambda is positive")
    print("PASS complete lambda/Z/danger/det(C)/rank-two legality for both signed-z lifts")

    # Exact nodes are breaker diagnostics only; the continuum proof is above.
    sample_S = [R(1, 1000000), R(1, 20000), Smax]
    sample_X = [X0, (X0 + X1)/2, X1]
    count = 0
    minimum = None
    minimum_data = None
    for s_value in sample_S:
        for x_value in sample_X:
            for m_value in (Mlo, Mhi):
                for o_value in (wlo, whi):
                    for n_value in (nlo, nhi):
                        data = {S: s_value, X: x_value, M: m_value,
                                omega: o_value, nu: n_value}
                        z_value = sp.factor(Z_sheet.subs(data))
                        d_value = sp.factor(danger.subs(data))
                        gate_value = sp.factor(36*sheet_gate.subs(data))
                        require(z_value > 0 and d_value > 0,
                                "exact diagnostic node is legal")
                        require(gate_value > 0, "exact diagnostic raw gate is positive")
                        if minimum is None or gate_value < minimum:
                            minimum = gate_value
                            minimum_data = (s_value, x_value, m_value, o_value, n_value)
                        count += 1
    require(count == 72, "72 exact rational diagnostic nodes")
    print("PASS 72/72 exact legal raw-gate diagnostic nodes")
    print(f"NODE_MIN {minimum} AT {minimum_data}")
    print("DIAGNOSTIC_POLICY nodes are falsification checks, not the continuum proof")
    print("ROUTE_POLICY no real-part monotonicity, feasible-center absorption,")
    print("             fixed s=-2 allocation, or Z=0 quadratic remainder is used")
    print("SCOPE one recentered local chart only; no raw negative or maximality claim")
    print("OPEN full compact ball, unrestricted common metric, arbitrary nodes/dimension,")
    print("     and the fixed crossing-lens optimal constant")


if __name__ == "__main__":
    main()
