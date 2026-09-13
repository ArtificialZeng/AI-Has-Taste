#!/usr/bin/env python3
"""Fail-closed exact source verifier for the next moving-sheet X layer."""

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


def centered_box_abs(poly, variables, radii):
    expanded = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    bound = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(expanded.terms())


def centered_box_lower(poly, variables, radii):
    expanded = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    constant = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if any(powers):
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

    # Fully conjugated original Hermitian transverse compression and Q,Q^2
    # gate.  Nothing is imported from the predecessor theorem or discovery.
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
    print("PASS independent fully conjugated Hermitian Q,Q^2 gate reconstruction")

    # Moving sheet and exact legality on the new closed X layer.
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
    Xmin = R(1, 31)
    Xmax = R(1, 30)
    Mradius = R(1, 1000)
    tradius = R(1, 100)
    Amin = 1 - Mradius
    Amax = 1 + Mradius
    y0min = R(12, 25) / Amax - tradius
    y0max = R(12, 25) / Amin + tradius
    w0min = (18 - 45 * Mradius) / (25 * Amin) - tradius
    w0max = (18 + 45 * Mradius) / (25 * Amax) + tradius
    wbarmin = w0min - R(3, 5) * Xmax
    yupper = Smax * y0max
    zslope = sp.factor(wbarmin - Smax * y0max**2)
    zupper = sp.factor(3 * Xmax + Smax * w0max)
    danger_reserve = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * yupper - Smax * w0max
    )
    legality_claims = {
        "wbarmin": (wbarmin, R(2549, 3700)),
        "zslope": (zslope, R(7639086233111, 11088900000000)),
        "zupper": (zupper, R(100173181, 1001000000)),
        "danger": (danger_reserve, R(95037195293, 185185000000)),
    }
    for label, (value, claim) in legality_claims.items():
        zero(value - claim, label)
    if not (
        0 < Smax < Xmin < Xmax < 3 and Amin > 0 and y0min > 0
        and zslope > 0 and zupper < R(1, 8)
        and danger_reserve > R(1, 2)
    ):
        raise AssertionError("new-layer legality")
    # Hence lambda=A/S>0, Z>=3X-X^2+S*zslope>0, and
    # det(compression)=(5/9)SZ>0 on every actual point.
    print("PASS exact lambda, positive-Z, Z<1/8, danger and rank-two legality")

    # Recompute the rational sparse moving-sheet quotient from the raw gate.
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
    if any(i + j < 2 for i, j in quotient):
        raise AssertionError("unexpected lower term after H1")

    variables = (M, omega, nu)
    radii = (Mradius, tradius, tradius)
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
        raise AssertionError(("H2 exact lower bounds", h2_lowers))

    # The decisive refinement: sigma=S/X satisfies sigma<=31/10000, not
    # merely sigma<=1.  Keep sigma^si in every absolute remainder term.
    sigmamax = sp.factor(Smax / Xmin)
    zero(sigmamax - R(31, 10000), "sigma maximum")
    closure_reserve = h2_lowers[(0, 2)]
    remainder = sp.Integer(0)
    sx_terms = 0
    parameter_monomials = 0
    for (si, xi), coefficient in quotient.items():
        total = si + xi
        if total <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        remainder += bound * sigmamax**si * Xmax**(total - 2)
        sx_terms += 1
        parameter_monomials += terms
    remainder = sp.factor(remainder)
    margin = sp.factor(closure_reserve - remainder)
    remainder_claim = R(
        46499117573964545715217879542445250542603528830310449624295476899453,
        17199267840000000000000000000000000000000000000000000000000,
    )
    margin_claim = R(
        34580339142052196913279468445031671587443896471169689550375704523100547,
        17199267840000000000000000000000000000000000000000000000000,
    )
    zero(remainder - remainder_claim, "sigma-sensitive remainder")
    zero(margin - margin_claim, "sigma-sensitive margin")
    if sx_terms != 16 or parameter_monomials != 947 or margin <= 0:
        raise AssertionError((sx_terms, parameter_monomials, margin))

    print("PASS raw 20-term moving-sheet quotient and nonnegative H1")
    print("PASS sigma-sensitive 16-term/947-monomial exact remainder")
    print("SIGMA_MAX", sigmamax)
    print("DANGER_RESERVE", danger_reserve)
    print("SIGMA_SENSITIVE_MARGIN", margin)
    print("PASS strict raw 36Gamma for 1/31<=X<=1/30")
    print("SCOPE adjacent moving-sheet cell only; full compact ball and fixed lens open")


if __name__ == "__main__":
    main()
