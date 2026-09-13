#!/usr/bin/env python3
"""Independent exact referee for the inward-Z endpoint cell.

The frozen discovery/source program is hash-checked but never imported,
executed, parsed, or read for coefficients.  This implementation starts from
reordered signed-z Gram columns, rebuilds the Hermitian Q and Q^2 gate, and
uses a direct dense monomial-to-Bernstein conversion on the new cell.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_endpoint_extension.py"
NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_source_candidate.md"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_endpoint_extension_source_freeze_manifest.sha256"
EXPECTED_SOURCE_SHA = "2ab0f3f532fbfe0d2fc6b2aa3301ff4857f783161f109ad4d846cbcbf266df4f"
EXPECTED_NOTE_SHA = "146743ebe254682bee761d0378b90a1e76ca139063ca83cb6f5a7c1b625243c9"
EXPECTED_MANIFEST_SHA = "ae3ede1048aad9625884963ffbff66437dbd6c36540244cdb82a94efb999a0a8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def exact_zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def reduce_even_relations(expr: sp.Expr, zz: sp.Symbol, hh: sp.Symbol,
                          qq: sp.Symbol, SS: sp.Symbol,
                          ZZ: sp.Symbol) -> sp.Expr:
    """Reduce in a different order from the source: signed z, h, then q."""
    value = sp.expand(expr)
    value = sp.rem(value, zz**2 - ZZ, zz)
    value = sp.rem(sp.expand(value), hh**2 - SS, hh)
    value = sp.rem(sp.expand(value), qq**2 - (1 - SS), qq)
    return sp.factor(value)


def centered_l1_lower(poly: sp.Expr, variables: tuple[sp.Symbol, ...],
                      radii: tuple[sp.Rational, ...]) -> sp.Rational:
    data = sp.Poly(sp.expand(poly), *variables)
    total = sp.Rational(0)
    for powers, coefficient in data.terms():
        magnitude = sp.Rational(1)
        for exponent, radius in zip(powers, radii):
            magnitude *= radius**exponent
        if all(exponent == 0 for exponent in powers):
            total += coefficient
        else:
            total -= abs(coefficient) * magnitude
    return sp.factor(total)


def dense_tensor_bernstein(poly: sp.Expr, first: sp.Symbol,
                           second: sp.Symbol, d_first: int,
                           d_second: int) -> dict[tuple[int, int], sp.Expr]:
    """Direct binomial transform of a dense monomial tensor."""
    dense = sp.Poly(sp.expand(poly), first, second)
    require(dense.degree(first) <= d_first and dense.degree(second) <= d_second,
            "declared Bernstein tensor degree")
    coefficients: dict[tuple[int, int], sp.Expr] = {}
    for (i, j), coefficient in dense.terms():
        coefficients[(i, j)] = coefficient
    controls: dict[tuple[int, int], sp.Expr] = {}
    for i in range(d_first + 1):
        for j in range(d_second + 1):
            value = sp.Rational(0)
            for a in range(i + 1):
                for b in range(j + 1):
                    value += (coefficients.get((a, b), 0)
                              * sp.Rational(math.comb(i, a), math.comb(d_first, a))
                              * sp.Rational(math.comb(j, b), math.comb(d_second, b)))
            controls[(i, j)] = sp.factor(value)
    return controls


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--attack-gate", choices=("none", "drop-core", "flip-sign"),
                        default="none")
    args = parser.parse_args()

    require(__debug__, "optimized Python is forbidden")
    require(sha256(args.source_path) == EXPECTED_SOURCE_SHA, "frozen source SHA-256")
    require(sha256(NOTE) == EXPECTED_NOTE_SHA, "frozen claim-note SHA-256")
    require(sha256(SOURCE_MANIFEST) == EXPECTED_MANIFEST_SHA,
            "frozen source-manifest SHA-256")
    print("PASS frozen dependency hashes (source bytes used only for SHA-256)")

    R = sp.Rational
    I = sp.I
    S, Z = sp.symbols("S Z", real=True)
    h, q, z = sp.symbols("h q z", real=True)
    lam = sp.symbols("lambda", real=True, positive=True)
    xx, yy = sp.symbols("x y", real=True)

    # Definition-level reconstruction with Gram columns ordered (z-column,
    # mixed-column), unlike the (r,f) compression-matrix construction.
    a = sp.sqrt(6) / 6
    c = sp.sqrt(30) / 6
    phase = R(4, 5) + R(3, 5) * I
    p = sp.Matrix([a, 0, c])
    r = sp.Matrix([-a, 0, c * phase])
    f = sp.Matrix([-c * h, q, -a * h * phase])
    j = (1 + 5 * xx) / (3 * sp.sqrt(5))
    k = (-3 + 5 * yy) / (3 * sp.sqrt(5))
    ell = sp.sqrt(5) * z / 3
    g_z = ell * f
    g_mix = h * r + (j - I * k) * f
    H = sp.simplify(g_z * sp.conjugate(g_z.T)
                    + g_mix * sp.conjugate(g_mix.T))
    require(exact_zero((sp.conjugate(r.T) * r)[0] - 1), "r has unit norm")
    require(reduce_even_relations((sp.conjugate(f.T) * f)[0] - 1,
                                  z, h, q, S, Z) == 0,
            "f has unit norm")
    require(reduce_even_relations((sp.conjugate(r.T) * f)[0],
                                  z, h, q, S, Z) == 0,
            "reordered compression frame is orthogonal")
    require(all(exact_zero(entry) for entry in (H - sp.conjugate(H.T))),
            "reordered signed-z Gram sum is Hermitian")
    compression = sp.Matrix([[h**2, h*(j + I*k)],
                             [h*(j - I*k), j**2 + k**2 + ell**2]])
    require(reduce_even_relations(compression.det() - R(5, 9)*S*Z,
                                  z, h, q, S, Z) == 0,
            "signed-z compression determinant is (5/9)SZ")
    require(all(exact_zero(entry) for entry in (H - H.subs(z, -z))),
            "both signed-z lifts give the same Hermitian compression")
    Q = lam * H
    Q2 = sp.expand(Q * Q)
    xi = sp.expand(Q * p)

    literal_terms = [
        4 * a**2 * xi[1] * sp.conjugate(xi[1]),
        (c * sp.conjugate(xi[0]) + a * xi[2] + I * (a*c - Q2[2, 0]))
        * sp.conjugate(c * sp.conjugate(xi[0]) + a * xi[2]
                       + I * (a*c - Q2[2, 0])),
        (c * sp.conjugate(xi[1]) - I * Q2[2, 1])
        * sp.conjugate(c * sp.conjugate(xi[1]) - I * Q2[2, 1]),
        -32 * a**2 * ((xi[0] + sp.conjugate(xi[0])) / 2)**2,
    ]
    if args.attack_gate == "drop-core":
        literal_terms[0] = 0
    elif args.attack_gate == "flip-sign":
        literal_terms[3] = -literal_terms[3]
    gamma_literal = sp.expand(sum(literal_terms))

    eta = sp.expand(H * p)
    H2 = sp.expand(H * H)
    B0 = sp.Matrix([0, I*a*c, 0])
    L = sp.Matrix([2*a*eta[1], c*sp.conjugate(eta[0]) + a*eta[2],
                   c*sp.conjugate(eta[1])])
    N = sp.Matrix([0, -I*H2[2, 0], -I*H2[2, 1]])
    vector = B0 + lam*L + lam**2*N
    gamma_vector = sp.expand((sp.conjugate(vector.T) * vector)[0]
                             - 32*a**2*lam**2
                             * ((eta[0] + sp.conjugate(eta[0])) / 2)**2)
    require(exact_zero(gamma_literal - gamma_vector),
            "literal fully conjugated Q,Q^2 gate equals cyclic Gram-vector gate")

    gamma_shape = reduce_even_relations(gamma_vector, z, h, q, S, Z)
    require(not gamma_shape.has(z, h, q), "both signed-z lifts and frame radicals cancel")
    require(exact_zero(sp.im(gamma_shape)), "reconstructed gate is real")
    print("PASS independent reordered signed-z/Q/Q^2 raw-gate reconstruction")

    M, omega, nu = sp.symbols("M omega nu", real=True)
    X, tau, u = sp.symbols("X tau u", real=True)
    A = 1 + M
    y0 = R(12, 25)/A + nu
    b = ((45*M + 18)/(25*A) - R(3, 5)*X + omega
         - R(10636, 275)*(X - R(1, 5)))
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S*y0
    Z_sheet = R(9, 13) - X**2 + S*b - S**2*y0**2
    sheet_gate = sp.cancel(gamma_shape.subs({xx: x_sheet, yy: y_sheet,
                                             Z: Z_sheet, lam: A/S}))
    cleared = sp.factor(25**8 * A**8 * S**3 * 36 * sheet_gate)
    require(sp.denom(sp.cancel(cleared)) == 1, "lossless positive clearing has no denominator")
    recovered = sp.cancel(cleared / (25**8*A**8*S**3*36) - sheet_gate)
    require(recovered == 0, "clearing is algebraically lossless")
    layer = S**3 * 25**8 * M**2 * A**8 * (5*M**2 + 14*M + 14)
    core = sp.expand(cleared - layer)
    cleared_sx_poly = sp.Poly(cleared, S, X)
    sx_poly = sp.Poly(core, S, X)
    require(len(cleared_sx_poly.terms()) == 32,
            "32 nonzero (S,X) coefficients before layer removal")
    require(len(sx_poly.terms()) == 32, "32 nonzero (S,X) coefficients")
    require(sx_poly.degree(S) == 7 and sx_poly.degree(X) == 4,
            "core bidegree (7,4)")
    require(len(sp.Poly(core, S, X, M, omega, nu).terms()) == 1581,
            "1,581 fully centered monomials")
    print("PASS lossless clearing, 32/32/1581 counts, and bidegree (7,4)")

    # New-cell transform: first u, then tau; direct dense tensor conversion.
    cell = sp.expand(core.subs(X, R(1, 4) + u/R(520)).subs(S, tau/R(10000)))
    controls = dense_tensor_bernstein(cell, tau, u, 7, 4)
    require(len(controls) == 40, "40 Bernstein controls")
    lowers = {index: centered_l1_lower(value, (M, omega, nu),
                                       (R(1, 1000), R(1, 100), R(1, 100)))
              for index, value in controls.items()}
    require(all(value > 0 for value in lowers.values()), "all 40 lower controls strict")
    zeros = [index for index, value in lowers.items() if value == 0]
    require(zeros == [], "no closure-zero lower controls")
    weakest = min(lowers, key=lowers.get)
    expected_reserve = R(987933779504207075207504779933987999,
                         7187610992640000000000000000)
    require(weakest == (0, 0), "unique weakest control index (0,0)")
    require(sum(value == lowers[weakest] for value in lowers.values()) == 1,
            "(0,0) is the unique global weakest lower control")
    require(lowers[weakest] == expected_reserve, "exact weakest lower reserve")
    tau_zero_row = [lowers[(0, j_index)] for j_index in range(5)]
    require(len(tau_zero_row) == 5 and all(value > 0 for value in tau_zero_row),
            "all five tau=0 row lower controls are strict")
    tau_zero = sp.factor(controls[(0, 0)])
    expected_tau_zero = R(95367431640625, 685464) * (M + 1)**12
    require(exact_zero(tau_zero - expected_tau_zero), "complete tau=0 polynomial")
    print("PASS 40/40 strict Bernstein controls, zero=[], min=(0,0)")
    print(f"RESERVE {expected_reserve}")

    # Independently rebuild the predecessor sheet and compare at X=1/4.
    X_old = sp.symbols("X_old", real=True)
    b_old = ((45*M + 18)/(25*A) - R(3, 5)*X_old + omega
             - R(10636, 275)*(X_old - R(1, 5)))
    y_old = R(3, 5) + S*y0
    Z_old = 3*X_old - X_old**2 - 3*(X_old - R(3, 13)) + S*b_old - S**2*y0**2
    old_gate = sp.cancel(gamma_shape.subs({xx: -R(1, 5) + X_old,
                                           yy: y_old, Z: Z_old, lam: A/S}))
    old_cleared = sp.factor(25**8*A**8*S**3*36*old_gate)
    require(exact_zero(old_cleared.subs(X_old, R(1, 4))
                       - cleared.subs(X, R(1, 4))),
            "termwise cleared-gate splice at old X=1/4/new u=0")
    print("PASS exact predecessor/new-cell cleared-gate splice")

    # Exact monotonicity and endpoint legality.
    Smax, Xlo, Xhi = R(1, 10000), R(1, 4), R(131, 520)
    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)
    require(sp.factor(sp.diff(b, M)) == 27/(25*A**2), "b monotonic in M")
    require(sp.diff(b, X) == -R(10801, 275), "b monotonic in X")
    require(sp.diff(b, omega) == 1, "b monotonic in omega")
    b_min = sp.factor(b.subs({M: Mlo, X: Xhi, omega: wlo}))
    require(b_min == -R(7674229, 5291000), "new-endpoint exact b_min")
    y0_max = sp.factor(y0.subs({M: Mlo, nu: nhi}))
    y0_min = sp.factor(y0.subs({M: Mhi, nu: nlo}))
    b_max = sp.factor(b.subs({M: Mhi, X: Xlo, omega: whi}))
    require(y0_min > 0 and b_max < 0, "global signs y0>0 and b<0")
    require(exact_zero(sp.diff(Z_sheet, X) + 2*X + S*R(10801, 275)),
            "Z strictly decreases with X on the positive cell")
    require(exact_zero(sp.diff(Z_sheet, omega) - S),
            "Z strictly increases with omega")
    require(exact_zero(sp.diff(Z_sheet, nu) + 2*S**2*y0),
            "Z strictly decreases with nu")
    require(exact_zero(sp.diff(Z_sheet, M)
                       - S*R(27, 25)/A**2
                       - S**2*R(24, 25)*y0/A**2),
            "Z strictly increases with M")
    require(exact_zero(sp.diff(Z_sheet, S) - b + 2*S*y0**2),
            "Z strictly decreases with S")
    Z_min = sp.factor(Z_sheet.subs({S: Smax, X: Xhi, M: Mlo,
                                    omega: wlo, nu: nhi}))
    expected_Z_min = R(129601350803598453349, 206142651000000000000)
    require(Z_min == expected_Z_min, "new-endpoint exact Z_min")
    require(R(131, 208) < R(108, 169), "strict global Z upper comparison")
    T = sp.factor(R(6, 5)*y0 + b)
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - Z_sheet)
    require(exact_zero(danger - (R(2, 5)*(X - R(3, 13)) - S*T)),
            "exact danger identity")
    T_upper = sp.factor(T.subs({M: Mhi, X: Xlo, omega: whi, nu: nhi}))
    require(T_upper <= -R(1, 100), "uniform T<=-1/100")
    danger_endpoint_bound = R(2, 5)*(Xhi - R(3, 13)) + Smax/R(100)
    require(danger_endpoint_bound == R(110013, 13000000),
            "stated outer-corner danger bound")
    det_bound = sp.factor(R(5, 9)*Smax*Z_min)
    expected_det = R(129601350803598453349, 3710567718000000000000000)
    require(det_bound == expected_det, "new-endpoint exact det(C) bound")
    require(Mlo + 1 > 0 and Z_min > 0 and b_min < 0,
            "lambda, Z, and signed-rank legality")
    print("PASS endpoint b/Z/danger/det(C) exact bounds and both z signs")
    print("NOTE danger fraction is the outer corner (X=131/520,S=1/10000);")
    print("     uniform endpoint-slice infimum for 0<S<=1/10000 is 11/1300.")

    # Exact rational nodes are adversarial diagnostics only.
    samples = [R(1, 1000000), R(1, 20000), R(1, 10000)]
    x_samples = [Xlo, (Xlo + Xhi)/2, Xhi]
    nodal_count = 0
    min_node = None
    for sv in samples:
        for xv in x_samples:
            for mv in (Mlo, Mhi):
                for wv in (wlo, whi):
                    for nv in (nlo, nhi):
                        value = sp.factor(36*sheet_gate.subs({S: sv, X: xv, M: mv,
                                                              omega: wv, nu: nv}))
                        require(value > 0, "exact diagnostic node gate positivity")
                        min_node = value if min_node is None or value < min_node else min_node
                        nodal_count += 1
    require(nodal_count == 72, "72 exact diagnostic nodes")
    print("PASS 72 exact rational attack nodes (diagnostic only, not proof)")
    print("SCOPE exact independently audited partial theorem on the displayed cell only;")
    print("      full compact ball/common metric/arbitrary-node/fixed-lens remain open")


if __name__ == "__main__":
    main()
