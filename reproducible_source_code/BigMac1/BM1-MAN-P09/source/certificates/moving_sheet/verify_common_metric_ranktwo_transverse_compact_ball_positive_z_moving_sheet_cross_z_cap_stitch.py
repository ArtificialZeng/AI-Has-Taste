#!/usr/bin/env python3
"""Fail-closed exact source verifier for the moving-sheet Z=1/8 stitch."""

if not __debug__:
    raise RuntimeError("do not run this source verifier with python -O")

import sympy as sp

from verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_next_x_sigma_layer import (
    centered_box_abs,
    centered_box_lower,
    reduce_q,
    sparse_add,
    sparse_mul,
    sparse_pow,
    zero,
)


def main():
    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)

    # Fully conjugated original Hermitian Q,Q^2 gate.
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    basis = sp.Matrix.hstack(rvec, fvec)
    relation = sp.Poly(q**2 - (1 - h**2), q)
    zero(reduce_q(basis.conjugate().T * basis - sp.eye(2), q, relation),
         "transverse basis Gram")

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
    Wraw = j**2 + kappa**2 + R(5, 9) * Z
    compression = sp.Matrix([
        [h**2, h * (j + I * kappa)],
        [h * (j - I * kappa), Wraw],
    ])
    zero(compression - compression.conjugate().T, "Hermitian compression")
    zero(compression.det() - R(5, 9) * h**2 * Z,
         "compression determinant")
    H = sp.expand(basis * compression * basis.conjugate().T)
    zero(reduce_q(H * nvec, q, relation), "kernel identity")
    Q = sp.expand(lam * H)
    image = sp.expand(Q * p)
    danger_claim = (
        R(5, 36) * sp.sqrt(6) * lam * h**2
        * (x**2 + y**2 + Z - 1)
    )
    zero(reduce_q(sp.re(image[0]) - danger_claim, q, relation),
         "danger identity")
    Q2 = sp.expand(Q * Q)
    first = c * sp.conjugate(image[0]) + a * image[2] + I * (
        a * c - Q2[2, 0]
    )
    leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * image[1] * sp.conjugate(image[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(image[0])**2
    )
    raw_gate = sp.expand(sp.rem(sp.Poly(raw_gate, q), relation).as_expr())
    gate36 = sp.expand(
        (36 * raw_gate).subs(h**8, S**4).subs(h**6, S**3)
        .subs(h**4, S**2).subs(h**2, S)
    )
    if gate36.has(h) or gate36.has(q):
        raise AssertionError("unresolved h or q")
    quartic = sp.Poly(gate36, lam)
    if quartic.degree() != 4 or quartic.nth(0) != 5:
        raise AssertionError(("raw quartic", quartic.degree(), quartic.nth(0)))
    print("PASS fully conjugated Hermitian Q,Q^2 gate reconstructed")

    # Moving-sheet map and the exact failure of outer-box inclusion.
    A = 1 + M
    y0 = R(12, 25) / A + nu
    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Ymap = S * y0
    Wmap = S * (wc + omega)
    Zmap = 3 * X - X**2 - Ymap**2 + Wmap
    xmap = -R(1, 5) + X
    ymap = R(3, 5) + Ymap
    zero(
        xmap**2 + ymap**2 + Zmap
        - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
        "moving danger identity",
    )

    smax = R(1, 10000)
    xmin = R(1, 24)
    xmax = R(1, 23)
    mradius = R(1, 1000)
    tradius = R(1, 100)
    amin = 1 - mradius
    amax = 1 + mradius
    y0min = R(12, 25) / amax - tradius
    y0max = R(12, 25) / amin + tradius
    w0min = (18 - 45 * mradius) / (25 * amin) - tradius
    w0max = (18 + 45 * mradius) / (25 * amax) + tradius
    xraw_min = -R(1, 5) + xmin
    xraw_max = -R(1, 5) + xmax
    y_gap_upper = R(1, 10) + smax * y0max
    inclusion_claims = {
        "x lower": (xraw_min, -R(19, 120)),
        "x upper": (xraw_max, -R(18, 115)),
        "y gap infimum": (R(1, 10), R(1, 10)),
        "y gap upper": (y_gap_upper, R(33316333, 333000000)),
    }
    for label, (value, claim) in inclusion_claims.items():
        zero(value - claim, label)
    if not (
        -R(1, 4) < xraw_min < xraw_max < R(1, 2)
        and y0min > 0 and R(1, 10) > 0
    ):
        raise AssertionError("outer-box non-inclusion")
    # Every actual y-1/2=1/10+S*y0 is strictly greater than 1/10.
    print("PASS exact outer-box non-inclusion; y-gap infimum=1/10")

    # Uniform positive-Z, danger, scale, and rank-two legality across the cap.
    wbarmin = w0min - R(3, 5) * xmax
    zslope = sp.factor(wbarmin - smax * y0max**2)
    zupper = sp.factor(3 * xmax - xmax**2 + smax * w0max)
    danger_reserve = sp.factor(
        R(3, 5) - R(13, 5) * xmax
        - R(6, 5) * smax * y0max - smax * w0max
    )
    legality_claims = {
        "wbarmin": (wbarmin, R(58109, 85100)),
        "zslope": (zslope, R(174146537361553, 255044700000000)),
        "zupper": (zupper, R(68106712749, 529529000000)),
        "danger": (danger_reserve, R(6220529775217, 12777765000000)),
    }
    for label, (value, claim) in legality_claims.items():
        zero(value - claim, label)
    if not (
        0 < smax < xmin < xmax < 3 and amin > 0 and y0min > 0
        and zslope > 0 and zupper < R(1, 7) and danger_reserve > 0
    ):
        raise AssertionError("cross-cap legality")
    print("PASS positive-Z, strict danger, lambda and rank-two legality")

    # Raw sparse moving-sheet quotient and sigma-sensitive sign.
    rescaled = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: A,
    }))
    denominator = 25 * A
    sparse_y0 = (12 + 25 * A * nu) / denominator
    sparse_w0 = (45 * M + 18 + 25 * A * omega) / denominator
    y_sparse = {(1, 0): sparse_y0}
    z_sparse = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): sparse_w0,
        (1, 1): -R(3, 5),
        (2, 0): -sparse_y0**2,
    }
    raw_poly = sp.Poly(N, S, Z, X, Y)
    if len(raw_poly.terms()) != 134:
        raise AssertionError(("raw monomial count", len(raw_poly.terms())))
    mapped = {}
    for (si, zi, xi, yi), coefficient in raw_poly.terms():
        term = {(si, xi): coefficient}
        term = sparse_mul(term, sparse_pow(z_sparse, zi))
        term = sparse_mul(term, sparse_pow(y_sparse, yi))
        mapped = sparse_add(mapped, term)
    cleared = {
        key: sp.factor(sp.cancel(value * denominator**8))
        for key, value in mapped.items()
    }
    if {
        sp.factor(sp.denom(value)) for value in cleared.values()
        if sp.denom(value).free_symbols
    }:
        raise AssertionError("uncleared symbolic denominator")
    lost = {
        key: value for key, value in cleared.items()
        if value != 0 and key[0] < 2
    }
    if lost:
        raise AssertionError(("missing S^2 factor", lost))
    quotient = {
        (si - 2, xi): value
        for (si, xi), value in cleared.items() if value != 0
    }
    if len(quotient) != 20 or max(i for i, _ in quotient) != 5 \
            or max(j for _, j in quotient) != 4:
        raise AssertionError(("quotient support", len(quotient)))
    h1 = quotient.pop((1, 0))
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    zero(h1 - expected_h1, "nonnegative H1")

    variables = (M, omega, nu)
    radii = (mradius, tradius, tradius)
    h2_lowers = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    h2_claims = {
        (2, 0): R(
            481040550200263282578648409035494777132062079,
            114661785600000000000000000000000,
        ),
        (1, 1): R(
            2301835302565365212028445402384697058519239,
            191102976000000000000000000000,
        ),
        (0, 2): R(
            2564950982194530478444050838857341987999,
            1274019840000000000000000000,
        ),
    }
    if h2_lowers != h2_claims or any(value <= 0 for value in h2_lowers.values()):
        raise AssertionError(("H2 bounds", h2_lowers))

    sigmamax = sp.factor(smax / xmin)
    zero(sigmamax - R(3, 1250), "sigma maximum")
    closure_reserve = h2_lowers[(0, 2)]
    remainder = sp.Integer(0)
    sx_terms = 0
    parameter_monomials = 0
    for (si, xi), coefficient in quotient.items():
        total = si + xi
        if total <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        remainder += bound * sigmamax**si * xmax**(total - 2)
        sx_terms += 1
        parameter_monomials += terms
    remainder = sp.factor(remainder)
    margin = sp.factor(closure_reserve - remainder)
    remainder_claim = R(
        341349404790343639470527055781196276834417458615095418095466792141,
        125122507920000000000000000000000000000000000000000000000,
    )
    margin_claim = R(
        83854846318555455131346013627095055256473934297852585381468177735953,
        41707502640000000000000000000000000000000000000000000000,
    )
    zero(remainder - remainder_claim, "cross-cap remainder")
    zero(margin - margin_claim, "cross-cap margin")
    if sx_terms != 16 or parameter_monomials != 947 or margin <= 0:
        raise AssertionError((sx_terms, parameter_monomials, margin))
    print("PASS sigma-sensitive raw-gate margin across the full cap band")

    # Two exact legal raw-gate points on opposite sides of Z=1/8.
    witness_specs = (
        ("below", xmin, -mradius, -tradius, tradius),
        ("above", xmax, mradius, tradius, -tradius),
    )
    witness_claims = {
        "below": {
            "z": R(13676193016733111, 110889000000000000),
            "t": -R(184931983266889, 110889000000000000),
            "gate": R(
                9365830377568041224106345521801146679,
                40000000000000000000000000000000000,
            ),
        },
        "above": {
            "z": R(68173435531857725471, 530058529000000000000),
            "t": R(1916119406857725471, 530058529000000000000),
            "gate": R(
                18787436399685005999560713886421176269952340879,
                73441472040000000000000000000000000000000000,
            ),
        },
    }
    signed_caps = {}
    for label, xv, mv, ov, nv in witness_specs:
        av = 1 + mv
        y0v = R(12, 25) / av + nv
        w0v = (45 * mv + 18 + 25 * av * ov) / (25 * av)
        zv = sp.factor(
            3 * xv - xv**2 + smax * (w0v - R(3, 5) * xv)
            - smax**2 * y0v**2
        )
        xrv = -R(1, 5) + xv
        yrv = R(3, 5) + smax * y0v
        lv = av / smax
        dv = sp.factor(1 - xrv**2 - yrv**2 - zv)
        detv = sp.factor(R(5, 9) * smax * zv)
        gv = sp.factor(quartic.as_expr().subs({
            S: smax, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        zero(zv - witness_claims[label]["z"], label + " Z")
        zero(zv - R(1, 8) - witness_claims[label]["t"], label + " cap")
        zero(gv - witness_claims[label]["gate"], label + " raw gate")
        if not (lv > 0 and zv > 0 and dv > 0 and detv > 0 and gv > 0):
            raise AssertionError(("illegal crossing witness", label))
        signed_caps[label] = zv - R(1, 8)
    if not (signed_caps["below"] < 0 < signed_caps["above"]):
        raise AssertionError("cap not crossed")

    print("SIGMA_MAX", sigmamax)
    print("Y_GAP_INFIMUM", R(1, 10))
    print("DANGER_RESERVE", danger_reserve)
    print("CROSS_CAP_MARGIN", margin)
    print("PASS exact legal witnesses on both sides of Z=1/8")
    print("PASS strict raw 36Gamma for 1/24<=X<=1/23")
    print("SCOPE moving-sheet stitch only; outer y-gap and full fixed lens remain open")


if __name__ == "__main__":
    main()
