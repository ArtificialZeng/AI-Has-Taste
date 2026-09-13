#!/usr/bin/env python3
"""Independent exact referee for the inward-Z legality-frontier cell.

The frozen candidate program is read only for its SHA-256 digest.  No source
coefficient, Bernstein control, or intermediate expression is imported,
executed, parsed, or trusted.  This verifier starts from the compact-ball
compression matrix, independently rebuilds Q and Q^2, and converts a dense
monomial tensor to Bernstein form on the claimed cell.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_legality_frontier_extension.py"
NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_source_candidate.md"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"
PREDECESSOR_REFEREE = ROOT / "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_independent_referee.py"
PREDECESSOR_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_ENDPOINT_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md"

EXPECTED_HASHES = {
    SOURCE: "1a2ef5c669d1602a27641f05ae1d051e7f03d6db99a8280085b3ececd23667a4",
    NOTE: "5e4109a188f3301412dd49f78039f2a0d4e107948f8e23c1bdc79cbcd4029aa0",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
    PREDECESSOR_REFEREE: "0928e8ab3c9c6027feb646af68a7dc4d567d34970887eb672520d120c6a387ab",
    PREDECESSOR_AUDIT: "e217488778451a9745aaa630e943c974f8fc8671577ef40cd008deb36c0e7652",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def exact_zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def quotient_reduce(expr: sp.Expr, qq: sp.Symbol, zz: sp.Symbol,
                    hh: sp.Symbol, SS: sp.Symbol, ZZ: sp.Symbol) -> sp.Expr:
    """Eliminate q, then signed z, then h (different from the predecessor)."""
    value = sp.expand(expr)
    value = sp.rem(value, qq**2 - (1 - SS), qq)
    value = sp.rem(sp.expand(value), zz**2 - ZZ, zz)
    value = sp.rem(sp.expand(value), hh**2 - SS, hh)
    return sp.factor(value)


def centered_box_lower(poly: sp.Expr,
                       variables: tuple[sp.Symbol, ...],
                       radii: tuple[sp.Rational, ...]) -> sp.Rational:
    """Exact centered coefficient-l1 lower bound on a rational box."""
    total = sp.Rational(0)
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        radius_weight = sp.prod(radius**power
                                for radius, power in zip(radii, powers))
        if all(power == 0 for power in powers):
            total += coefficient
        else:
            total -= abs(coefficient) * radius_weight
    return sp.factor(total)


def monomial_tensor_to_bernstein(poly: sp.Expr,
                                 first: sp.Symbol,
                                 second: sp.Symbol,
                                 degree_first: int,
                                 degree_second: int) -> dict[tuple[int, int], sp.Expr]:
    """Convert a freshly expanded dense monomial tensor, without saved data."""
    dense = sp.Poly(sp.expand(poly), first, second)
    require(dense.degree(first) <= degree_first
            and dense.degree(second) <= degree_second,
            "declared Bernstein degrees contain the dense tensor")
    monomial = dict(dense.terms())
    result: dict[tuple[int, int], sp.Expr] = {}
    for i in range(degree_first + 1):
        for j in range(degree_second + 1):
            value = sp.Rational(0)
            for a_index in range(i + 1):
                for b_index in range(j + 1):
                    value += (
                        monomial.get((a_index, b_index), 0)
                        * sp.Rational(math.comb(i, a_index),
                                      math.comb(degree_first, a_index))
                        * sp.Rational(math.comb(j, b_index),
                                      math.comb(degree_second, b_index))
                    )
            result[(i, j)] = sp.factor(value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument(
        "--attack",
        choices=("none", "drop-square", "flip-danger", "delete-core"),
        default="none",
    )
    args = parser.parse_args()

    require(__debug__, "optimized Python is forbidden")
    source_expected = EXPECTED_HASHES[SOURCE]
    require(sha256(args.source_path) == source_expected,
            "frozen candidate source SHA-256")
    for path, expected in EXPECTED_HASHES.items():
        if path != SOURCE:
            require(sha256(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS frozen source/claim/reduction/predecessor hashes")
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
    f = sp.Matrix([-c * h, q, -a * h * phase])
    U = sp.Matrix.hstack(r, f)

    j = (1 + 5*x_ball) / (3*sp.sqrt(5))
    k = (-3 + 5*y_ball) / (3*sp.sqrt(5))
    ell = sp.sqrt(5)*z / 3
    W = j**2 + k**2 + ell**2
    C = sp.Matrix([[h**2, h*(j + I*k)],
                   [h*(j - I*k), W]])
    H = sp.expand(U * C * sp.conjugate(U.T))

    # Independent Cholesky reconstruction checks the direct compression.
    g_mix = h*r + (j - I*k)*f
    g_z = ell*f
    H_cholesky = sp.expand(g_mix*sp.conjugate(g_mix.T)
                           + g_z*sp.conjugate(g_z.T))
    require(all(exact_zero(entry) for entry in (H - H_cholesky)),
            "direct compression equals independent Gram-column construction")
    require(quotient_reduce((sp.conjugate(r.T)*r)[0] - 1,
                            q, z, h, S, Z) == 0, "r is a unit vector")
    require(quotient_reduce((sp.conjugate(f.T)*f)[0] - 1,
                            q, z, h, S, Z) == 0, "f is a unit vector")
    require(quotient_reduce((sp.conjugate(r.T)*f)[0],
                            q, z, h, S, Z) == 0, "r and f are orthogonal")
    require(all(exact_zero(entry) for entry in (H - sp.conjugate(H.T))),
            "direct compression is Hermitian")
    require(quotient_reduce(C.det() - R(5, 9)*S*Z,
                            q, z, h, S, Z) == 0,
            "compression determinant is (5/9)SZ")
    require(all(exact_zero(entry) for entry in (H - H.subs(z, -z))),
            "both signed-z lifts give the same compression")

    Q = sp.expand(lam*H)
    Q2 = sp.expand(Q*Q)
    xi = sp.expand(Q*p)
    terms = [
        4*a**2*xi[1]*sp.conjugate(xi[1]),
        (c*sp.conjugate(xi[0]) + a*xi[2] + I*(a*c - Q2[2, 0]))
        * sp.conjugate(c*sp.conjugate(xi[0]) + a*xi[2]
                       + I*(a*c - Q2[2, 0])),
        (c*sp.conjugate(xi[1]) - I*Q2[2, 1])
        * sp.conjugate(c*sp.conjugate(xi[1]) - I*Q2[2, 1]),
        -32*a**2*((xi[0] + sp.conjugate(xi[0]))/2)**2,
    ]
    if args.attack == "drop-square":
        terms[0] = 0
    elif args.attack == "flip-danger":
        terms[3] = -terms[3]
    gamma_literal = sp.expand(sum(terms))

    eta = sp.expand(H*p)
    H2 = sp.expand(H*H)
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
            "literal fully conjugated Q,Q^2 gate equals cyclic vector gate")

    gamma_shape = quotient_reduce(gamma_vector, q, z, h, S, Z)
    require(not gamma_shape.has(q, z, h),
            "frame and signed-lift radicals cancel exactly")
    require(exact_zero(sp.im(gamma_shape)), "the reconstructed gate is real")
    print("PASS independent compression/Q/Q^2/raw-gate reconstruction")

    M, omega, nu = sp.symbols("M omega nu", real=True)
    X, tau, u = sp.symbols("X tau u", real=True)
    A = 1 + M
    y0 = R(12, 25)/A + nu
    b = ((45*M + 18)/(25*A) - R(3, 5)*X + omega
         - R(10636, 275)*(X - R(1, 5)))
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S*y0
    Z_sheet = R(9, 13) - X**2 + S*b - S**2*y0**2
    sheet_gate = sp.cancel(gamma_shape.subs({x_ball: x_sheet,
                                             y_ball: y_sheet,
                                             Z: Z_sheet,
                                             lam: A/S}))
    positive_factor = 25**8*A**8*S**3*36
    cleared = sp.factor(positive_factor*sheet_gate)
    require(sp.denom(sp.cancel(cleared)) == 1,
            "positive clearing produces a polynomial")
    require(sp.cancel(cleared/positive_factor - sheet_gate) == 0,
            "positive clearing is exactly reversible")
    layer = S**3*25**8*M**2*A**8*(5*M**2 + 14*M + 14)
    core = sp.expand(cleared - layer)
    if args.attack == "delete-core":
        sx_terms = sp.Poly(core, S, X).terms()
        (s_power, x_power), coefficient = sx_terms[0]
        core = sp.expand(core - coefficient*S**s_power*X**x_power)

    before = sp.Poly(cleared, S, X)
    after = sp.Poly(core, S, X)
    require(len(before.terms()) == 32,
            "32 nonzero (S,X) coefficients before layer removal")
    require(len(after.terms()) == 32,
            "32 nonzero (S,X) coefficients after layer removal")
    require(after.degree(S) == 7 and after.degree(X) == 4,
            "core bidegree is (7,4)")
    require(len(sp.Poly(core, S, X, M, omega, nu).terms()) == 1581,
            "core has 1,581 centered monomials")
    print("PASS reversible clearing and 32/32/1581 structural counts")

    Smax = R(1, 10000)
    Xlo = R(131, 520)
    Xhi = R(83059, 100000)
    Xbad = R(4153, 5000)
    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)
    radii = (R(1, 1000), R(1, 100), R(1, 100))

    # Lossless new cell.  Expand X first, then S, and use a dense tensor.
    Xmap = Xlo + (Xhi - Xlo)*u
    cell = sp.expand(core.subs(X, Xmap).subs(S, Smax*tau))
    controls = monomial_tensor_to_bernstein(cell, u, tau, 4, 7)
    require(len(controls) == 40, "exactly 40 controls on the theorem cell")
    lowers = {index: centered_box_lower(value, (M, omega, nu), radii)
              for index, value in controls.items()}
    require(all(value > 0 for value in lowers.values()),
            "all 40 centered lower controls are strict")
    require([index for index, value in lowers.items() if value == 0] == [],
            "no closure-zero controls")
    weakest = min(lowers, key=lowers.get)
    expected_reserve = R(
        119539987320009056100108078372012547879,
        718761099264000000000000000000,
    )
    require(weakest == (0, 0), "unique weakest control index is (0,0)")
    require(sum(value == lowers[weakest] for value in lowers.values()) == 1,
            "the weakest lower control is unique")
    require(lowers[weakest] == expected_reserve,
            "exact weakest centered reserve")
    weakest_polynomial = sp.factor(controls[(0, 0)])
    expected_polynomial = (R(461578369140625, 2741856)*(M + 1)**12)
    require(exact_zero(weakest_polynomial - expected_polynomial),
            "complete weakest-control parameter polynomial")
    print("PASS theorem-cell bidegree (7,4), 40/40 strict controls")
    print(f"RESERVE {expected_reserve}")
    print(f"WEAKEST_POLYNOMIAL {expected_polynomial}")

    # Check the polynomial certificate remains strict to the illegal bracket end.
    bad_map = Xlo + (Xbad - Xlo)*u
    bad_cell = sp.expand(core.subs(X, bad_map).subs(S, Smax*tau))
    bad_controls = monomial_tensor_to_bernstein(bad_cell, u, tau, 4, 7)
    bad_lowers = {index: centered_box_lower(value, (M, omega, nu), radii)
                  for index, value in bad_controls.items()}
    require(len(bad_lowers) == 40 and all(value > 0 for value in bad_lowers.values()),
            "all 40 polynomial controls remain strict through X=4153/5000")
    print("PASS 40/40 polynomial controls remain strict to the illegal bracket end")

    # Rebuild the predecessor expression in its unsimplified chart and splice.
    Xold = sp.symbols("Xold", real=True)
    bold = ((45*M + 18)/(25*A) - R(3, 5)*Xold + omega
            - R(10636, 275)*(Xold - R(1, 5)))
    Zold = 3*Xold - Xold**2 - 3*(Xold - R(3, 13)) + S*bold - S**2*y0**2
    predecessor_inputs = (
        (-R(1, 5) + Xold).subs(Xold, Xlo),
        y_sheet,
        sp.factor(Zold.subs(Xold, Xlo)),
        A/S,
    )
    new_inputs = (
        x_sheet.subs(X, Xlo),
        y_sheet,
        sp.factor(Z_sheet.subs(X, Xlo)),
        A/S,
    )
    require(all(exact_zero(old_value - new_value)
                for old_value, new_value in zip(predecessor_inputs, new_inputs)),
            "every original raw-gate input splices at X=131/520")
    # Since gamma_shape is one fixed literal expression in exactly these four
    # inputs, equality here is a definition-level termwise gate splice, not a
    # comparison of imported predecessor coefficients.
    print("PASS exact predecessor/new-cell raw-gate input splice at X=131/520")

    # Exact full-cell legality, strict danger and rank-two conditions.
    require(exact_zero(sp.diff(b, M) - R(27, 25)/A**2),
            "exact b derivative in M")
    require(exact_zero(sp.diff(b, X) + R(10801, 275)),
            "exact b derivative in X")
    require(sp.diff(b, omega) == 1, "exact b derivative in omega")
    b_min = sp.factor(b.subs({M: Mlo, X: Xhi, omega: wlo}))
    require(b_min == -R(24601484583, 1017500000),
            "exact full-cell b minimum")
    y0_min = sp.factor(y0.subs({M: Mhi, nu: nlo}))
    b_max = sp.factor(b.subs({M: Mhi, X: Xlo, omega: whi}))
    require(y0_min > 0 and b_max < 0, "uniform signs y0>0 and b<0")

    require(exact_zero(sp.diff(Z_sheet, X) + 2*X + S*R(10801, 275)),
            "Z derivative in X")
    require(exact_zero(sp.diff(Z_sheet, omega) - S), "Z derivative in omega")
    require(exact_zero(sp.diff(Z_sheet, nu) + 2*S**2*y0), "Z derivative in nu")
    require(exact_zero(sp.diff(Z_sheet, M)
                       - S*R(27, 25)/A**2
                       - S**2*R(24, 25)*y0/A**2),
            "Z derivative in M")
    require(exact_zero(sp.diff(Z_sheet, S) - b + 2*S*y0**2),
            "Z derivative in S")
    Z_min = sp.factor(Z_sheet.subs({S: Smax, X: Xhi, M: Mlo,
                                    omega: wlo, nu: nhi}))
    expected_Z_min = R(160243869095653, 15857127000000000000)
    require(Z_min == expected_Z_min and Z_min > 0,
            "exact positive Z minimum on the theorem cell")
    Z_upper = sp.factor(R(9, 13) - Xlo**2)
    require(Z_upper == R(170039, 270400) and Z_upper < 1,
            "exact strict global Z upper bound")

    T = sp.factor(R(6, 5)*y0 + b)
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - Z_sheet)
    require(exact_zero(danger - (R(2, 5)*(X - R(3, 13)) - S*T)),
            "exact danger identity")
    T_upper = sp.factor(T.subs({M: Mhi, X: Xlo,
                                omega: whi, nu: nhi}))
    require(T_upper == -R(10931, 13000), "exact uniform T upper bound")
    danger_lower = R(11, 1300) + R(10931, 13000)*S
    require(exact_zero(R(2, 5)*(Xlo - R(3, 13))
                       - S*T_upper - danger_lower),
            "claimed full-cell danger lower bound")
    det_lower_coefficient = sp.factor(R(5, 9)*Z_min)
    require(det_lower_coefficient
            == R(160243869095653, 28542828600000000000),
            "claimed determinant lower coefficient")
    require(1 + Mlo > 0
            and R(11, 1300) > 0
            and R(10931, 13000) > 0,
            "lambda positivity and positive affine danger lower bound")
    print("PASS full-cell lambda/Z/danger/rank-two legality for both z signs")

    # Exact rational bracket: the worst legal coordinate crosses zero, while
    # the independently rebuilt polynomial certificate is still positive.
    worst_Z = sp.factor(Z_sheet.subs({S: Smax, M: Mlo,
                                      omega: wlo, nu: nhi}))
    Z_right = sp.factor(worst_Z.subs(X, Xhi))
    Z_bad = sp.factor(worst_Z.subs(X, Xbad))
    require(Z_right == expected_Z_min,
            "right-end exact worst-corner Z")
    require(Z_bad == -R(103795949201927, 15857127000000000000),
            "bad-end exact worst-corner Z")
    derivative = sp.factor(sp.diff(worst_Z, X))
    require(exact_zero(derivative + 2*X + Smax*R(10801, 275)),
            "exact decreasing derivative of worst-corner Z")
    require(derivative.subs(X, Xlo) < 0 and sp.diff(derivative, X) == -2,
            "worst-corner Z strictly decreases throughout the bracket")
    require(Z_right > 0 and Z_bad < 0,
            "exact rational chart-legality root bracket")
    print("PASS exact rational Z bracket: legal at 83059/100000, illegal at 4153/5000")

    # Original rational raw-gate diagnostics; continuum positivity rests on
    # the controls above, not on these nodes.
    sample_scales = [R(1, 1000000), R(1, 20000), Smax]
    sample_x = [Xlo, (Xlo + Xhi)/2, Xhi]
    count = 0
    minimum = None
    minimum_data = None
    for sval in sample_scales:
        for xval in sample_x:
            for mval in (Mlo, Mhi):
                for oval in (wlo, whi):
                    for nval in (nlo, nhi):
                        data = {S: sval, X: xval, M: mval,
                                omega: oval, nu: nval}
                        zvalue = sp.factor(Z_sheet.subs(data))
                        dvalue = sp.factor(danger.subs(data))
                        value = sp.factor(36*sheet_gate.subs(data))
                        require(zvalue > 0 and dvalue > 0,
                                "diagnostic node is legal and strictly dangerous")
                        require(value > 0, "diagnostic original raw gate is positive")
                        if minimum is None or value < minimum:
                            minimum = value
                            minimum_data = (sval, xval, mval, oval, nval)
                        count += 1
    require(count == 72, "72 exact rational diagnostic nodes")
    print("PASS 72/72 exact legal raw-gate diagnostic nodes")
    print(f"NODE_MIN {minimum} AT {minimum_data}")
    print("SCOPE exact independently audited partial theorem on the displayed cell only")
    print("OPEN full compact ball/common metric/arbitrary-node/fixed-lens problems")


if __name__ == "__main__":
    main()
