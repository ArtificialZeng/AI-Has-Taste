#!/usr/bin/env python3
"""Independent signed-z/Gram and 72-node referee for the moving-sheet family."""

if not __debug__:
    raise RuntimeError("referee verifier is fail-closed under python -O")

import sympy as sp


def is_zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                is_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    result = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if result != 0:
        raise AssertionError(f"{label}: {result}")


def mod_circle(expression, q, h):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: mod_circle(entry, q, h))
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    modulus = sp.Poly(q**2 + h**2 - 1, q)
    remainder = sp.Poly(sp.expand(numerator), q).rem(modulus).as_expr()
    return sp.factor(remainder / denominator)


def hermitian_inner(left, right):
    return sp.expand((left.conjugate().T * right)[0])


def interval_abs(poly, variables, radii):
    polynomial = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    total = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        total += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(total), len(polynomial.terms())


def interval_lower(poly, variables, radii):
    polynomial = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    origin = polynomial.coeff_monomial((0,) * len(variables))
    error = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        if any(powers):
            error += abs(coefficient) * sp.prod(
                radius**power for radius, power in zip(radii, powers)
            )
    return sp.factor(origin - error)


def main():
    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    j, kappa, ell = sp.symbols("j kappa ell", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)

    # Independent signed-z Cholesky and two-column Gram reconstruction.
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    frame = sp.Matrix.hstack(rvec, fvec, nvec)
    is_zero(mod_circle(frame.conjugate().T * frame - sp.eye(3), q, h),
            "orthonormal signed-z frame")

    cholesky = sp.Matrix([[h, 0], [j - I * kappa, ell]])
    signed_compression = sp.expand(cholesky * cholesky.conjugate().T)
    is_zero(signed_compression.det() - h**2 * ell**2,
            "signed compression determinant")
    is_zero(signed_compression.subs(ell, -ell) - signed_compression,
            "signed-z symmetry")
    basis = frame[:, :2]
    gram_column_1 = sp.expand(basis * cholesky[:, 0])
    gram_column_2 = sp.expand(basis * cholesky[:, 1])
    H_signed = sp.expand(
        gram_column_1 * gram_column_1.conjugate().T
        + gram_column_2 * gram_column_2.conjugate().T
    )
    is_zero(
        H_signed - basis * signed_compression * basis.conjugate().T,
        "two signed-z Gram columns",
    )
    is_zero(mod_circle(H_signed * nvec, q, h), "signed-z kernel")

    affine = {
        j: (1 + 5 * x) / (3 * sp.sqrt(5)),
        kappa: (-3 + 5 * y) / (3 * sp.sqrt(5)),
    }
    direct_compression = sp.Matrix([
        [h**2, h * (affine[j] + I * affine[kappa])],
        [h * (affine[j] - I * affine[kappa]),
         affine[j]**2 + affine[kappa]**2 + R(5, 9) * Z],
    ])
    signed_to_direct = signed_compression.subs(affine).subs(ell**2, R(5, 9) * Z)
    is_zero(signed_to_direct - direct_compression,
            "signed-z/direct compact compression")
    is_zero(direct_compression.det() - R(5, 9) * h**2 * Z,
            "direct compact determinant")

    H = sp.expand(basis * direct_compression * basis.conjugate().T)
    Q = sp.expand(lam * H)
    xi = mod_circle(Q * p, q, h)
    Q2 = mod_circle(Q * Q, q, h)
    first = c * sp.conjugate(xi[0]) + a * xi[2] + I * (
        a * c - Q2[2, 0]
    )
    leakage = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
    raw_gate = mod_circle(
        4 * a**2 * xi[1] * sp.conjugate(xi[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(xi[0])**2,
        q,
        h,
    )

    # Reconstruct the same scalar a second way from the constant/linear/
    # quadratic Gram vector.  This does not use source coefficient caches.
    H_on_p = mod_circle(H * p, q, h)
    H2_on_frame = mod_circle(H * H, q, h)
    constant = sp.Matrix([0, I * a * c, 0])
    linear = sp.Matrix([
        2 * a * H_on_p[1],
        c * sp.conjugate(H_on_p[0]) + a * H_on_p[2],
        c * sp.conjugate(H_on_p[1]),
    ])
    quadratic = sp.Matrix([0, -I * H2_on_frame[2, 0], -I * H2_on_frame[2, 1]])
    d = sp.re(H_on_p[0])
    vector_gate = mod_circle(
        hermitian_inner(constant + lam * linear + lam**2 * quadratic,
                        constant + lam * linear + lam**2 * quadratic)
        - 32 * a**2 * lam**2 * d**2,
        q,
        h,
    )
    is_zero(raw_gate - vector_gate, "Q,Q^2/vector Gram gate")
    danger = mod_circle(sp.re(Q * p)[0], q, h)
    danger_claim = (
        R(5, 36) * sp.sqrt(6) * lam * h**2
        * (x**2 + y**2 + Z - 1)
    )
    is_zero(danger - danger_claim, "independent danger identity")

    gate36_h = sp.expand(36 * vector_gate)
    gate36 = sp.expand(
        gate36_h.subs(h**8, S**4).subs(h**6, S**3)
        .subs(h**4, S**2).subs(h**2, S)
    )
    if gate36.has(h) or gate36.has(q):
        raise AssertionError("circle variables survived")
    quartic = sp.Poly(gate36, lam)
    if quartic.degree() != 4 or quartic.nth(0) != 5:
        raise AssertionError((quartic.degree(), quartic.nth(0)))
    print("PASS independent signed-z two-column Gram and Q,Q^2 reconstruction",
          flush=True)

    # Independent legality calculation.
    M, omega, nu, X, Y, mu = sp.symbols("M omega nu X Y mu", real=True)
    A = 1 + M
    yzero = R(12, 25) / A + nu
    wcenter = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Ymap = S * yzero
    Wmap = S * (wcenter + omega)
    Zmap = 3 * X - X**2 - Ymap**2 + Wmap
    xmap = -R(1, 5) + X
    ymap = R(3, 5) + Ymap
    is_zero(
        xmap**2 + ymap**2 + Zmap
        - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
        "referee moving danger identity",
    )
    Smax, Xmax = R(1, 10000), R(3, 10000)
    Mradius, tradius = R(1, 1000), R(1, 100)
    lower_A, upper_A = 1 - Mradius, 1 + Mradius
    lower_yzero = R(12, 25) / upper_A - tradius
    upper_yzero = R(12, 25) / lower_A + tradius
    lower_w = (18 - 45 * Mradius) / (25 * lower_A) - tradius \
        - R(3, 5) * Xmax
    upper_w = (18 + 45 * Mradius) / (25 * upper_A) + tradius
    upper_Y = sp.factor(Smax * upper_yzero)
    lower_Z_slope = sp.factor(lower_w - Smax * upper_yzero**2)
    upper_Z = sp.factor(3 * Xmax + Smax * upper_w)
    ball_reserve = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * upper_Y - Smax * upper_w
    )
    independent_legality = (
        lower_A == R(999, 1000)
        and upper_A == R(1001, 1000)
        and lower_yzero == R(46999, 100100)
        and upper_yzero == R(16333, 33300)
        and upper_Y == R(16333, 333000000)
        and lower_w == R(1311167, 1850000)
        and upper_w == R(73181, 100100)
        and lower_Z_slope == R(7858868231111, 11088900000000)
        and upper_Z == R(974081, 1001000000)
        and ball_reserve == R(332826352979, 555555000000)
        and lower_Z_slope > 0 and upper_Z < R(1, 1000)
        and ball_reserve > R(299, 500)
    )
    if not independent_legality:
        raise AssertionError("independent legality bounds")
    print("PASS independent positive-Z, danger, lambda and rank-two legality",
          flush=True)

    # Build N from the independently reconstructed vector quartic.  Recover
    # all coefficients by a 72-node exact tensor inversion rather than the
    # source verifier's sparse moving-map coefficient assembly.
    rescaled = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: A,
    }))
    raw_poly = sp.Poly(N, S, Z, X, Y)
    raw_terms = raw_poly.terms()
    if len(raw_terms) != 134:
        raise AssertionError(("raw support", len(raw_terms)))
    safe_S_degree = max(a0 + 2 * b0 + d0 - 2
                        for (a0, b0, _c0, d0), _ in raw_terms)
    safe_X_degree = max(c0 + 2 * b0
                        for (_a0, b0, c0, _d0), _ in raw_terms)
    if (safe_S_degree, safe_X_degree) != (7, 8):
        raise AssertionError(("safe nodal degrees", safe_S_degree, safe_X_degree))

    denominator_base = 25 * A
    y_numerator = 12 + 25 * A * nu
    w_numerator = 45 * M + 18 + 25 * A * omega
    s_nodes = [R(index) for index in range(1, safe_S_degree + 2)]
    x_nodes = [R(index) for index in range(safe_X_degree + 1)]
    values = []
    for row, svalue in enumerate(s_nodes, start=1):
        value_row = []
        for xvalue in x_nodes:
            z_numerator = (
                (3 * xvalue - xvalue**2) * denominator_base**2
                + svalue * (
                    w_numerator * denominator_base
                    - R(3, 5) * xvalue * denominator_base**2
                )
                - svalue**2 * y_numerator**2
            )
            value = sp.Integer(0)
            for (sdegree, zdegree, xdegree, ydegree), coefficient in raw_terms:
                denominator_power = 8 - 2 * zdegree - ydegree
                if denominator_power < 0:
                    raise AssertionError(("clearing exponent", zdegree, ydegree))
                value += (
                    coefficient * svalue**(sdegree + ydegree - 2)
                    * xvalue**xdegree * z_numerator**zdegree
                    * y_numerator**ydegree
                    * denominator_base**denominator_power
                )
            value = sp.expand(value)
            if sp.denom(sp.cancel(value)).free_symbols:
                raise AssertionError(("nodal denominator", row, xvalue))
            if row == 1 and xvalue == 0:
                calibration = {
                    M: R(1, 1000),
                    omega: R(1, 100),
                    nu: -R(1, 100),
                }
                direct_yzero = sp.factor(yzero.subs(calibration))
                direct_wcenter = sp.factor(wcenter.subs({
                    **calibration,
                    X: xvalue,
                }))
                direct_Y = svalue * direct_yzero
                direct_Z = sp.factor(
                    3 * xvalue - xvalue**2 - direct_Y**2
                    + svalue * (direct_wcenter + calibration[omega])
                )
                direct_value = sp.factor(
                    (25 * (1 + calibration[M]))**8
                    * N.subs({
                        S: svalue,
                        X: xvalue,
                        Y: direct_Y,
                        Z: direct_Z,
                        M: calibration[M],
                    })
                    / svalue**2
                )
                optimized_value = sp.factor(value.subs(calibration))
                is_zero(optimized_value - direct_value,
                        "d-adic nodal/direct-N calibration")
                print("PASS d-adic/direct raw N calibration", flush=True)
            value_row.append(value)
        values.append(value_row)
        print(f"NODAL_ROW {row}/{len(s_nodes)} PASS", flush=True)

    vandermonde_s = sp.Matrix([
        [node**degree for degree in range(safe_S_degree + 1)]
        for node in s_nodes
    ])
    vandermonde_x = sp.Matrix([
        [node**degree for degree in range(safe_X_degree + 1)]
        for node in x_nodes
    ])
    inverse_s = vandermonde_s.inv()
    inverse_x = vandermonde_x.inv()
    x_coefficients = []
    for row in range(len(s_nodes)):
        x_coefficients.append([
            sp.expand(sum(
                inverse_x[degree, column] * values[row][column]
                for column in range(len(x_nodes))
            ))
            for degree in range(safe_X_degree + 1)
        ])
    coefficients = {}
    for sdegree in range(safe_S_degree + 1):
        for xdegree in range(safe_X_degree + 1):
            coefficient = sp.expand(sum(
                inverse_s[sdegree, row] * x_coefficients[row][xdegree]
                for row in range(len(s_nodes))
            ))
            if coefficient != 0:
                coefficients[(sdegree, xdegree)] = sp.factor(coefficient)
    if len(coefficients) != 20:
        raise AssertionError(("nodal nonzero support", len(coefficients)))
    if max(i for i, _ in coefficients) != 5 \
            or max(j for _, j in coefficients) != 4:
        raise AssertionError(("nodal bidegree", coefficients.keys()))
    print("PASS 72-node exact inversion; high safe-degree coefficients vanish",
          flush=True)

    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    is_zero(coefficients[(1, 0)] - expected_h1, "nodal H1")
    rest = dict(coefficients)
    del rest[(1, 0)]
    variables = (M, omega, nu)
    radii = (Mradius, tradius, tradius)
    h2_lowers = {
        "SS": interval_lower(rest[(2, 0)], variables, radii),
        "SX": interval_lower(rest[(1, 1)], variables, radii),
        "XX": interval_lower(rest[(0, 2)], variables, radii),
    }
    h2_expected = {
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
    if h2_lowers != h2_expected:
        raise AssertionError(("nodal H2 reserves", h2_lowers))
    reserve = min(h2_lowers.values())

    layer_bounds = {}
    term_count = 0
    for (sdegree, xdegree), coefficient in rest.items():
        if sdegree + xdegree <= 2:
            continue
        bound, count = interval_abs(coefficient, variables, radii)
        layer_bounds[sdegree + xdegree - 2] = (
            layer_bounds.get(sdegree + xdegree - 2, 0) + bound
        )
        term_count += count
    expected_bounds = {
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
    if term_count != 947 or layer_bounds != expected_bounds:
        raise AssertionError(("nodal remainder", term_count, layer_bounds))
    margins = {}
    for chart, radius in (("C0", Smax), ("C1", Xmax)):
        error = sum(
            bound * radius**degree for degree, bound in layer_bounds.items()
        )
        margins[chart] = sp.factor(reserve - error)
    margin_expected = {
        "C0": R(
            2157675883946338861464573804693908853416834606352657354865271,
            1074954240000000000000000000000000000000000000000,
        ),
        "C1": R(
            89361321403752495288011515925096895113866165323668871164167,
            44789760000000000000000000000000000000000000000,
        ),
    }
    if margins != margin_expected or any(value <= 0 for value in margins.values()):
        raise AssertionError(("nodal chart margins", margins))
    print("PASS independent C0/C1 reserves and complete ordered cover", flush=True)
    print("PASS independent strict positive-Z moving-sheet family", flush=True)
    print("controls=947 nodal_values=72", flush=True)
    print("scope=parametric family only; full compact ball and fixed lens open",
          flush=True)


if __name__ == "__main__":
    main()
