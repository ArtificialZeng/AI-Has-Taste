#!/usr/bin/env python3
"""Exact verifier for the compact-ball transverse-cone reduction."""

if not __debug__:
    raise RuntimeError("do not run this verifier with python -O")

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


def main():
    I = sp.I
    R = sp.Rational
    h, q, lam = sp.symbols("h q lambda", real=True)
    j, k, ell = sp.symbols("j k ell", real=True)
    x, y, z, s = sp.symbols("x y z s", real=True)
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    basis = sp.Matrix.hstack(rvec, fvec)

    # Orthonormality is polynomial modulo q^2=1-h^2.
    relation = {q**2: 1 - h**2}
    gram = sp.expand(basis.conjugate().T * basis - sp.eye(2))
    kernel_gram = sp.expand(basis.conjugate().T * nvec)
    norm_kernel = sp.expand(inner(nvec, nvec) - 1)
    for row in range(gram.rows):
        for column in range(gram.cols):
            zero(gram[row, column].subs(relation), "basis Gram")
    for row in range(kernel_gram.rows):
        zero(kernel_gram[row, 0], "kernel orthogonality")
    zero(norm_kernel.subs(relation), "kernel norm")

    W = j**2 + k**2 + ell**2
    compression = sp.Matrix([[h**2, h * (j + I * k)],
                             [h * (j - I * k), W]])
    zero(compression.det() - h**2 * ell**2, "Cholesky determinant")
    H = sp.expand(basis * compression * basis.conjugate().T)
    zero(H * nvec, "kernel identity")

    # Exact inverse map from the original compression variables.
    u, v, X, Y, delta = sp.symbols("u v X Y delta", positive=True, real=True)
    inverse = {
        lam: u / h**2,
        j: h * X / u,
        k: h * Y / u,
        ell: h * delta / u,
    }
    W_inverse = sp.factor(W.subs(inverse).subs(delta**2, u * v - X**2 - Y**2))
    zero(W_inverse - h**2 * v / u, "inverse W")
    zero((lam * h**2).subs(inverse) - u, "inverse u")
    zero((lam * h * (j + I * k)).subs(inverse) - X - I * Y,
         "inverse off diagonal")
    zero((lam * W).subs(inverse).subs(delta**2, u * v - X**2 - Y**2) - v,
         "inverse v")

    image = sp.expand(H * p)
    danger = sp.factor(sp.re(image[0]))
    danger_shape = 3 * W - 1 + R(2, 1) / sp.sqrt(5) * (-j + 3 * k)
    zero(danger - h**2 * sp.sqrt(6) * danger_shape / 12,
         "danger shape")

    affine = {
        j: (1 + 5 * x) / (3 * sp.sqrt(5)),
        k: (-3 + 5 * y) / (3 * sp.sqrt(5)),
        ell: sp.sqrt(5) * z / 3,
    }
    ball = sp.factor(danger_shape.subs(affine))
    zero(ball - R(5, 3) * (x**2 + y**2 + z**2 - 1),
         "danger unit ball")

    # Reconstruct the original Hermitian gate and the quartic vector identity.
    H2 = sp.expand(H * H)
    linear = sp.Matrix(
        [
            2 * a * image[1],
            c * sp.conjugate(image[0]) + a * image[2],
            c * sp.conjugate(image[1]),
        ]
    )
    quadratic = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    constant = sp.Matrix([0, I * a * c, 0])
    d = sp.re(image[0])
    vector_gate = sp.expand_complex(
        inner(constant + lam * linear + lam**2 * quadratic,
              constant + lam * linear + lam**2 * quadratic)
        - 32 * a**2 * lam**2 * d**2
    )

    Q = sp.expand(lam * H)
    xi = sp.expand(Q * p)
    Q2 = sp.expand(Q * Q)
    first = c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * xi[1] * sp.conjugate(xi[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(xi[0])**2
    )
    zero(raw_gate - vector_gate, "raw gate/vector quartic")

    polynomial = sp.Poly(sp.expand(vector_gate), lam)
    if polynomial.degree() != 4:
        raise AssertionError("quartic degree")
    coefficients = [sp.factor(polynomial.nth(index)) for index in range(5)]
    claims = [
        inner(constant, constant),
        2 * sp.re(inner(constant, linear)),
        inner(linear, linear) + 2 * sp.re(inner(constant, quadratic))
        - 32 * a**2 * d**2,
        2 * sp.re(inner(linear, quadratic)),
        inner(quadratic, quadratic),
    ]
    for index, (actual, claim) in enumerate(zip(coefficients, claims)):
        zero(actual - claim, f"quartic coefficient {index}")
    zero(coefficients[0] - R(5, 36), "constant coefficient")

    # The affine ball chart removes every radical and every odd power of h.
    transformed = sp.expand((36 * vector_gate).subs(affine))
    transformed = sp.expand(transformed.subs(q**2, 1 - h**2))
    transformed_polynomial = sp.Poly(transformed, lam)
    zero(transformed_polynomial.nth(0) - 5, "compact constant")
    expected_term_counts = [6, 38, 69, 225]
    for power, expected_count in enumerate(expected_term_counts, start=1):
        coefficient = sp.expand(transformed_polynomial.nth(power) / h**2)
        coefficient = coefficient.subs(h**6, s**3).subs(h**4, s**2).subs(h**2, s)
        rational_polynomial = sp.Poly(sp.expand(coefficient), s, x, y, z)
        if rational_polynomial.domain != sp.QQ:
            raise AssertionError(f"nonrational compact coefficient {power}")
        if len(rational_polynomial.terms()) != expected_count:
            raise AssertionError((power, len(rational_polynomial.terms())))
        if rational_polynomial.degree(s) > power - 1:
            raise AssertionError(f"scale-shape degree {power}")
        if max(sum(monomial[1:]) for monomial, _ in rational_polynomial.terms()) > 2 * power:
            raise AssertionError(f"ball degree {power}")
        if power == 1:
            first_claim = R(10, 3) * (
                x**2 - 2 * x + y**2 - 6 * y + z**2 + 1
            )
            zero(rational_polynomial.as_expr() - first_claim,
                 "compact linear coefficient")

    print("PASS lossless Cholesky chart and inverse")
    print("PASS strict danger equals the open unit ball")
    print("PASS raw Hermitian Q/Q^2 gate equals compact quartic")
    print("PASS rational compact coefficients: term counts 6,38,69,225")
    print("scope=exact reduction; compact-ball quartic sign remains open")


if __name__ == "__main__":
    main()
