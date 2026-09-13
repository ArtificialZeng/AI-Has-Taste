#!/usr/bin/env python3
"""Independent exact referee verifier for the transverse compact-ball chart."""

if not __debug__:
    raise RuntimeError("referee verifier is fail-closed under python -O")

import sympy as sp


def zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if value != 0:
        raise AssertionError(f"{label}: {value}")


def inner(left, right):
    return sp.expand((left.conjugate().T * right)[0])


def reduce_circle(expression, q, h):
    """Remainder modulo q^2+h^2-1, rather than syntactic substitution."""
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: reduce_circle(entry, q, h))
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    polynomial = sp.Poly(sp.expand(numerator), q)
    modulus = sp.Poly(q**2 + h**2 - 1, q)
    return sp.factor(polynomial.rem(modulus).as_expr() / denominator)


def even_h_to_s(expression, h, s, variables):
    """Map an even polynomial in h to a polynomial in s=h^2 termwise."""
    polynomial = sp.Poly(sp.expand(expression), h, *variables)
    result = sp.S.Zero
    for powers, coefficient in polynomial.terms():
        if powers[0] % 2:
            raise AssertionError(f"odd h power survives: {powers}")
        monomial = s ** (powers[0] // 2)
        for variable, power in zip(variables, powers[1:]):
            monomial *= variable**power
        result += coefficient * monomial
    return sp.Poly(sp.expand(result), s, *variables)


def main():
    R = sp.Rational
    I = sp.I
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])

    h, q, lam = sp.symbols("h q lambda", real=True)
    j, kappa, ell = sp.symbols("j kappa ell", real=True)
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    basis = sp.Matrix.hstack(rvec, fvec)
    frame = sp.Matrix.hstack(rvec, fvec, nvec)
    zero(reduce_circle(frame.conjugate().T * frame - sp.eye(3), q, h),
         "orthonormal transverse frame")

    # A direct lower-triangular factor proves forward positivity, including
    # the rank-one boundary ell=0.
    cholesky = sp.Matrix([[h, 0], [j - I * kappa, ell]])
    compression = sp.expand(cholesky * cholesky.conjugate().T)
    W = j**2 + kappa**2 + ell**2
    compression_claim = sp.Matrix(
        [[h**2, h * (j + I * kappa)],
         [h * (j - I * kappa), W]]
    )
    zero(compression - compression_claim, "Cholesky compression")
    zero(compression.det() - h**2 * ell**2, "compression determinant")
    H = sp.expand(basis * compression * basis.conjugate().T)
    zero(reduce_circle(H * nvec, q, h), "kernel identity")

    # Reconstruct the unrestricted positive compression and its danger
    # scalar independently before invoking the chart.
    u, v, X, Y = sp.symbols("u v X Y", real=True)
    general_compression = sp.Matrix([[u, X + I * Y], [X - I * Y, v]])
    general_Q = sp.expand(basis * general_compression * basis.conjugate().T)
    general_image = sp.expand(general_Q * p)
    general_danger = reduce_circle(sp.re(general_image[0]), q, h)
    general_danger_claim = (
        sp.sqrt(6) * (3 * v * h**2 - u) / 12
        + sp.sqrt(30) * (-X + 3 * Y) * h / 30
    )
    zero(general_danger - general_danger_claim, "unrestricted danger")
    # If u=0, PSD forces X=Y=0 and the displayed expression is nonnegative.
    zero(general_danger_claim.subs({u: 0, X: 0, Y: 0})
         - sp.sqrt(6) * v * h**2 / 4, "u=0 danger boundary")

    delta = sp.symbols("delta", nonnegative=True, real=True)
    inverse = {
        lam: u / h**2,
        j: h * X / u,
        kappa: h * Y / u,
        ell: h * delta / u,
    }
    determinant_relation = {delta**2: u * v - X**2 - Y**2}
    inverse_compression = sp.expand(lam * compression).subs(inverse)
    inverse_compression = inverse_compression.applyfunc(
        lambda entry: sp.factor(entry.subs(determinant_relation))
    )
    zero(inverse_compression - general_compression, "inverse compression")
    # The inverse is valid for h>0,u>0.  delta=0 is included algebraically.

    image = reduce_circle(H * p, q, h)
    shape = sp.factor(3 * W - 1 + 2 * (-j + 3 * kappa) / sp.sqrt(5))
    H_danger = reduce_circle(sp.re(image[0]), q, h)
    zero(H_danger - h**2 * sp.sqrt(6) * shape / 12, "chart danger")

    x, y, z, s = sp.symbols("x y z s", real=True)
    affine = {
        j: (1 + 5 * x) / (3 * sp.sqrt(5)),
        kappa: (-3 + 5 * y) / (3 * sp.sqrt(5)),
        ell: sp.sqrt(5) * z / 3,
    }
    ball_expression = sp.factor(shape.subs(affine))
    zero(ball_expression - R(5, 3) * (x**2 + y**2 + z**2 - 1),
         "unit-ball completion")
    # z and -z give the same compression because only ell^2 occurs.
    zero(compression.subs(ell, -ell) - compression, "ell sign symmetry")

    # Rebuild the original Q,Q^2 gate, independently of the coefficient
    # vector identity, and then compare the two expressions.
    Q = sp.expand(lam * H)
    xi = reduce_circle(Q * p, q, h)
    Q2 = reduce_circle(Q * Q, q, h)
    first = c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
    raw_gate = reduce_circle(
        4 * a**2 * xi[1] * sp.conjugate(xi[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(xi[0]) ** 2,
        q,
        h,
    )

    base_image = reduce_circle(H * p, q, h)
    H2 = reduce_circle(H * H, q, h)
    constant = sp.Matrix([0, I * a * c, 0])
    linear = sp.Matrix(
        [
            2 * a * base_image[1],
            c * sp.conjugate(base_image[0]) + a * base_image[2],
            c * sp.conjugate(base_image[1]),
        ]
    )
    quadratic = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    d = sp.re(base_image[0])
    vector_gate = reduce_circle(
        inner(constant + lam * linear + lam**2 * quadratic,
              constant + lam * linear + lam**2 * quadratic)
        - 32 * a**2 * lam**2 * d**2,
        q,
        h,
    )
    zero(raw_gate - vector_gate, "raw gate/vector identity")

    polynomial = sp.Poly(sp.expand(vector_gate), lam)
    if polynomial.degree() != 4:
        raise AssertionError(polynomial.degree())
    coefficient_claims = [
        inner(constant, constant),
        2 * sp.re(inner(constant, linear)),
        inner(linear, linear) + 2 * sp.re(inner(constant, quadratic))
        - 32 * a**2 * d**2,
        2 * sp.re(inner(linear, quadratic)),
        inner(quadratic, quadratic),
    ]
    for power, claim in enumerate(coefficient_claims):
        zero(polynomial.nth(power) - reduce_circle(claim, q, h),
             f"lambda coefficient {power}")
    zero(polynomial.nth(0) - R(5, 36), "constant gate coefficient")

    # Transform each positive-lambda coefficient separately.  Polynomial
    # remainder first removes q, and an explicit parity map h^(2m)->s^m
    # avoids the official verifier's syntactic h^6,h^4,h^2 substitutions.
    expected_counts = [6, 38, 69, 225]
    compact_coefficients = []
    for power, expected_count in enumerate(expected_counts, start=1):
        coefficient = reduce_circle(36 * polynomial.nth(power), q, h)
        coefficient = sp.factor(coefficient.subs(affine) / h**2)
        compact = even_h_to_s(coefficient, h, s, (x, y, z))
        if compact.domain != sp.QQ:
            raise AssertionError((power, compact.domain))
        if len(compact.terms()) != expected_count:
            raise AssertionError((power, len(compact.terms())))
        if compact.degree(s) > power - 1:
            raise AssertionError(("s degree", power, compact.degree(s)))
        if max(sum(monomial[1:]) for monomial, _ in compact.terms()) > 2 * power:
            raise AssertionError(("ball total degree", power))
        compact_coefficients.append(compact)

    first_claim = R(10, 3) * (
        x**2 - 2 * x + y**2 - 6 * y + z**2 + 1
    )
    zero(compact_coefficients[0].as_expr() - first_claim, "F1")
    # Leading coefficient remains the exact Gram square after division by h^2.
    zero(
        compact_coefficients[3].as_expr()
        - even_h_to_s(
            sp.factor((36 * reduce_circle(inner(quadratic, quadratic), q, h))
                      .subs(affine) / h**2),
            h,
            s,
            (x, y, z),
        ).as_expr(),
        "leading Gram coefficient",
    )

    # h=0 is not an inverse-chart point: it is a separate planar face.
    # The frame itself remains orthonormal there, while the chart's first row
    # collapses.  This guards the exact quantifier boundary in the note.
    zero(reduce_circle(frame.subs({h: 0, q: 1}).conjugate().T
                       * frame.subs({h: 0, q: 1}) - sp.eye(3), q, h),
         "planar endpoint frame")
    collapsed = compression.subs(h, 0)
    zero(collapsed - sp.diag(0, W), "h=0 chart collapse")

    print("PASS independent forward Cholesky factor and inverse compression chart")
    print("PASS unrestricted PSD danger and exact open-unit-ball equivalence")
    print("PASS original Hermitian Q,Q^2 gate and lambda quartic coefficients")
    print("PASS compact F1..F4: counts 6,38,69,225 and claimed degree bounds")
    print("PASS h=0 is a separate planar face; s=0 is only polynomial closure")
    print("scope=lossless finite-dimensional reduction; quartic sign remains open")


if __name__ == "__main__":
    main()
