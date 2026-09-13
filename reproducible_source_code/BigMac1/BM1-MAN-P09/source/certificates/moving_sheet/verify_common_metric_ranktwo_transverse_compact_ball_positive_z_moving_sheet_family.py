#!/usr/bin/env python3
"""Exact source verifier for the positive-Z moving-sheet parametric family."""

if not __debug__:
    raise RuntimeError("do not run this source verifier with python -O")

import sympy as sp


def zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if value != 0:
        raise AssertionError((label, value))


def reduce_q(expression, q, relation):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: reduce_q(entry, q, relation))
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.factor(remainder / denominator)


def sparse_add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value != 0}


def sparse_mul(left, right):
    out = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            out[key] = out.get(key, 0) + left_value * right_value
    return {key: value for key, value in out.items() if value != 0}


def sparse_pow(base, exponent):
    out = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        out = sparse_mul(out, base)
    return out


def parameter_poly(poly, variables):
    return sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)


def centered_box_abs(poly, variables, radii):
    expanded = parameter_poly(poly, variables)
    bound = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(expanded.terms())


def centered_box_lower(poly, variables, radii):
    expanded = parameter_poly(poly, variables)
    constant = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if not any(powers):
            continue
        variation += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(constant - variation)


def main():
    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)

    # Original Hermitian transverse compression and Q,Q^2 gate.
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
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    Wraw = j**2 + k**2 + R(5, 9) * Z
    compression = sp.Matrix([
        [h**2, h * (j + I * k)],
        [h * (j - I * k), Wraw],
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
        raise AssertionError("unresolved h or q in raw gate")
    quartic = sp.Poly(gate36, lam)
    if quartic.degree() != 4 or quartic.nth(0) != 5:
        raise AssertionError(("gate quartic", quartic.degree(), quartic.nth(0)))
    print("PASS original Hermitian Q,Q^2 gate and positive-scale quartic")

    # Moving-sheet map and exact legality bounds.
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

    Smax = R(1, 10000)
    Xmax = R(3, 10000)
    Mradius = R(1, 1000)
    tradius = R(1, 100)
    Amin = 1 - Mradius
    Amax = 1 + Mradius
    y0min = R(12, 25) / Amax - tradius
    y0max = R(12, 25) / Amin + tradius
    w0min = (18 - 45 * Mradius) / (25 * Amin) - tradius
    w0max = (18 + 45 * Mradius) / (25 * Amax) + tradius
    wbarmin = w0min - R(3, 5) * Xmax
    wbarmax = w0max
    yupper = sp.factor(Smax * y0max)
    zslope = sp.factor(wbarmin - Smax * y0max**2)
    zupper = sp.factor(3 * Xmax + Smax * wbarmax)
    reserve_danger = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * yupper - Smax * wbarmax
    )
    legality_claims = {
        "Amin": (Amin, R(999, 1000)),
        "Amax": (Amax, R(1001, 1000)),
        "y0min": (y0min, R(46999, 100100)),
        "y0max": (y0max, R(16333, 33300)),
        "yupper": (yupper, R(16333, 333000000)),
        "wbarmin": (wbarmin, R(1311167, 1850000)),
        "wbarmax": (wbarmax, R(73181, 100100)),
        "zslope": (zslope, R(7858868231111, 11088900000000)),
        "zupper": (zupper, R(974081, 1001000000)),
        "danger": (reserve_danger, R(332826352979, 555555000000)),
    }
    for label, (value, claim) in legality_claims.items():
        zero(value - claim, label)
    if not (
        Amin > 0 and y0min > 0 and yupper < R(1, 1000)
        and zslope > 0 and zupper < R(1, 1000)
        and reserve_danger > R(299, 500)
    ):
        raise AssertionError("legality inequality failed")
    # Thus for actual S>0: lambda=A/S>0, 0<Y<1/1000,
    # S*zslope<=Z<1/1000, and det(compression)=(5/9)SZ>0.
    print("PASS exact map legality, 0<Z<1/1000, rank-two PSD")
    print("DANGER_RESERVE", reserve_danger)

    # Reconstruct N=S^3(36 Gamma) after lambda=(1+M)/S and perform the
    # rational moving-sheet substitution sparsely in (S,X).
    rescaled = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: A,
    }))
    positive_denominator = 25 * A
    sparse_y0 = (12 + 25 * A * nu) / positive_denominator
    sparse_w0 = (45 * M + 18 + 25 * A * omega) / positive_denominator
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
    for (sdegree, zdegree, xdegree, ydegree), coefficient in raw_poly.terms():
        term = {(sdegree, xdegree): coefficient}
        term = sparse_mul(term, sparse_pow(z_sparse, zdegree))
        term = sparse_mul(term, sparse_pow(y_sparse, ydegree))
        mapped = sparse_add(mapped, term)
    clearing = positive_denominator**8
    cleared = {
        key: sp.factor(sp.cancel(value * clearing))
        for key, value in mapped.items()
    }
    symbolic_denominators = {
        sp.factor(sp.denom(value)) for value in cleared.values()
        if sp.denom(value).free_symbols
    }
    if symbolic_denominators:
        raise AssertionError(("positive clearing", symbolic_denominators))
    lost = {
        key: value for key, value in cleared.items()
        if value != 0 and key[0] < 2
    }
    if lost:
        raise AssertionError(("missing exact S^2 factor", lost))
    quotient = {
        (sdegree - 2, xdegree): value
        for (sdegree, xdegree), value in cleared.items()
        if value != 0
    }
    if len(quotient) != 20 or max(i for i, _ in quotient) != 5 \
            or max(j for _, j in quotient) != 4:
        raise AssertionError(("quotient support", len(quotient)))

    h1 = quotient.get((1, 0), 0)
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    zero(h1 - expected_h1, "nonnegative H1")
    rest = dict(quotient)
    del rest[(1, 0)]
    if any(i + j < 2 for i, j in rest):
        raise AssertionError("unexpected lower term after H1 removal")

    variables = (M, omega, nu)
    radii = (Mradius, tradius, tradius)
    h2_lowers = {
        "SS": centered_box_lower(rest[(2, 0)], variables, radii),
        "SX": centered_box_lower(rest[(1, 1)], variables, radii),
        "XX": centered_box_lower(rest[(0, 2)], variables, radii),
    }
    h2_claims = {
        "SS": R(
            481040550200263282578648409035494777132062079,
            114661785600000000000000000000000,
        ),
        "SX": R(
            2301835302565365212028445402384697058519239,
            191102976000000000000000000000,
        ),
        "XX": R(
            2564950982194530478444050838857341987999,
            1274019840000000000000000000,
        ),
    }
    for label in h2_claims:
        zero(h2_lowers[label] - h2_claims[label], f"H2 lower {label}")
    reserve = min(h2_lowers.values())
    if reserve != h2_claims["XX"] or reserve <= 0:
        raise AssertionError(("H2 common reserve", reserve))

    layer_bounds = {}
    parameter_terms = 0
    for (sdegree, xdegree), coefficient in rest.items():
        total = sdegree + xdegree
        if total <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        layer_bounds[total - 2] = layer_bounds.get(total - 2, 0) + bound
        parameter_terms += terms
    layer_claims = {
        1: R(
            1040210347071333285995390774300441067433076882959,
            17199267840000000000000000000000000,
        ),
        2: R(
            513625292315565411172470351664061881087569457669,
            28665446400000000000000000000000000,
        ),
        3: R(
            9574969116015939526109085821350045427090716403,
            6370099200000000000000000000000000,
        ),
        4: R(
            34218452213929153632941920549574435172203,
            1592524800000000000000000000000,
        ),
        5: R(
            1012066220495792924792495220066012001,
            530841600000000000000000000,
        ),
    }
    if parameter_terms != 947 or layer_bounds != layer_claims:
        raise AssertionError(("remainder accounting", parameter_terms, layer_bounds))

    chart_claims = {
        "C0": (
            Smax,
            R(
                2157675883946338861464573804693908853416834606352657354865271,
                1074954240000000000000000000000000000000000000000,
            ),
        ),
        "C1": (
            Xmax,
            R(
                89361321403752495288011515925096895113866165323668871164167,
                44789760000000000000000000000000000000000000000,
            ),
        ),
    }
    for chart, (radius, margin_claim) in chart_claims.items():
        remainder = sum(
            bound * radius**degree for degree, bound in layer_bounds.items()
        )
        margin = sp.factor(reserve - remainder)
        zero(margin - margin_claim, f"{chart} exact margin")
        if margin <= 0:
            raise AssertionError((chart, margin))
        print(chart, "MARGIN", margin)

    # C0: X=S*rho, 0<=rho<=1, handles X<=S and contains X=0.
    # C1: S=X*sigma, 0<=sigma<=1, handles S<=X through X=3/10000.
    # They overlap at X=S.  Since every nonnegative pair is ordered, they
    # cover the full target rectangle; C1 contains the old MAIN chart.
    print("PASS C0/C1 full remainder, overlap X=S, full rectangle covered")
    print("PASS strict raw 36Gamma for the positive-Z moving-sheet family")
    print("SCOPE parametric family only; full compact ball and fixed lens open")


if __name__ == "__main__":
    main()
