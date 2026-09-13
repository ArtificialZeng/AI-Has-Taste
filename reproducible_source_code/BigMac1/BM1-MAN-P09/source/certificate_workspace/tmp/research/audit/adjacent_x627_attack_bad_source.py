#!/usr/bin/env python3
"""Exact source gate for the adjacent +x box [313/500,627/1000]."""

if not __debug__:
    raise RuntimeError("do not run with python -O")

from itertools import product
from math import comb
import hashlib
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BOUND = {
    "tmp/research/compact_ball_uncovered_box_x5_8_xy_exact_gate.py":
        "5e84519227b8dcae5f52ec62159936d47db1047c9219fc92dc52191d446e9b33",
    "tmp/research/compact_ball_uncovered_box_x5_8_xy_source_freeze_manifest.sha256":
        "9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d",
    "tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_independent_referee.py":
        "ab81310af91de5d56e00caf8ae1cb5d285ab52edef5ea7c32bb6c6b85b27f8d1",
    "audit/COMPACT_BALL_UNCOVERED_BOX_X5_8_XY_INDEPENDENT_REFEREE_AUDIT.md":
        "d5560cb01f08bae6634f2b48710dacfda1e03bdd5f8752c651dc3c728586cb0a",
    "tmp/research/audit/compact_ball_uncovered_box_x5_8_xy_independent_referee_manifest.sha256":
        "dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for entry in expression:
            zero(entry, label)
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if value != 0:
        raise AssertionError(f"{label}: {value}")


def reduce_q(expression, q, h):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: reduce_q(entry, q, h))
    relation = sp.Poly(q**2 - (1 - h**2), q)
    return sp.expand(sp.rem(sp.Poly(sp.expand(expression), q), relation).as_expr())


def power_to_bernstein(polynomial, variables):
    poly = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    degrees = [poly.degree(variable) for variable in variables]
    controls = {}
    for index in product(*[range(degree + 1) for degree in degrees]):
        value = sp.Rational(0)
        for powers, coefficient in poly.terms():
            if all(power <= idx for power, idx in zip(powers, index)):
                weight = sp.Rational(1)
                for power, idx, degree in zip(powers, index, degrees):
                    weight *= sp.Rational(comb(idx, power), comb(degree, power))
                value += coefficient * weight
        controls[index] = sp.factor(value)
    return degrees, controls


def main():
    for rel, expected in BOUND.items():
        if os.environ.get("XADJ_BAD_PREDECESSOR") == "1" and "source_freeze" in rel:
            expected = "0" * 64
        if sha256(ROOT / rel) != expected:
            raise AssertionError(f"predecessor binding: {rel}")

    I = sp.I
    R = sp.Rational
    h, q, lam, S, x, y, u, v = sp.symbols(
        "h q lambda S x y u v", real=True
    )
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    U = sp.Matrix.hstack(rvec, fvec)
    zero(reduce_q(U.conjugate().T * U - sp.eye(2), q, h), "frame Gram")
    zero(U.conjugate().T * nvec, "kernel orthogonality")
    zero(reduce_q((nvec.conjugate().T * nvec)[0] - 1, q, h), "kernel norm")

    Z = R(1, 8)
    xlo, xhi = R(313, 500), R(627, 1000)
    danger = sp.factor(1 - x**2 - y**2 - Z)
    danger_lower = sp.factor(danger.subs({x: xhi, y**2: R(1, 10000)}))
    if danger_lower != R(481771, 1000000) or danger_lower <= 0:
        raise AssertionError(f"shape-box danger bound: {danger_lower}")

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    ell2 = R(5, 9) * Z
    if os.environ.get("XADJ_BAD_NORMALIZATION") == "1":
        ell2 += R(1, 100)
    W = sp.expand(j**2 + k**2 + ell2)
    C = sp.Matrix([[h**2, h * (j + I * k)], [h * (j - I * k), W]])
    zero(C.det() - R(5, 72) * h**2, "compression determinant")
    H = sp.expand(U * C * U.conjugate().T)

    ell = sp.sqrt(R(5, 72))
    g1 = sp.expand(h * rvec + (j - I * k) * fvec)
    for signed_ell, label in [(ell, "plus"), (-ell, "minus")]:
        g2 = sp.expand(signed_ell * fvec)
        Hsigned = sp.expand(g1 * g1.conjugate().T + g2 * g2.conjugate().T)
        zero(H - Hsigned, f"{label} signed-z lift")
    zero(H * nvec, "kernel identity")

    Q = sp.expand(lam * H)
    zero(Q - Q.conjugate().T, "Q Hermitian")
    xi = sp.expand(Q * p)
    danger_sign = 1 if os.environ.get("XADJ_FLIP_DANGER") != "1" else -1
    zero(
        sp.re(xi[0])
        + danger_sign * R(5, 36) * sp.sqrt(6) * lam * h**2 * danger,
        "strict-danger scalar identity",
    )

    Q2 = sp.expand(Q * Q)
    if os.environ.get("XADJ_DROP_Q2") == "1":
        Q2 = sp.zeros(3)
    first = c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(xi[1]) - I * Q2[2, 1]
    raw = sp.expand_complex(
        4 * a**2 * xi[1] * sp.conjugate(xi[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(xi[0])**2
    )
    raw = reduce_q(raw, q, h)

    Hp = sp.expand(H * p)
    H2 = sp.expand(H * H)
    B0 = sp.Matrix([0, I * a * c, 0])
    L = sp.Matrix([2 * a * Hp[1], c * sp.conjugate(Hp[0]) + a * Hp[2],
                   c * sp.conjugate(Hp[1])])
    N = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector = B0 + lam * L + lam**2 * N
    gram = sp.expand(
        (vector.conjugate().T * vector)[0]
        - 32 * a**2 * lam**2 * sp.re(Hp[0])**2
    )
    zero(reduce_q(raw - gram, q, h), "fully conjugated/cyclic gate")

    transformed = sp.expand(
        (36 * raw)
        .subs(h**8, S**4)
        .subs(h**6, S**3)
        .subs(h**4, S**2)
        .subs(h**2, S)
    )
    if os.environ.get("XADJ_CORRUPT_COEFFICIENT") == "1":
        transformed += S * lam**4
    if transformed.has(h) or transformed.has(q):
        raise AssertionError("unresolved transverse radical")
    quartic = sp.Poly(transformed, lam, domain=sp.QQ[S, x, y])
    if quartic.degree() != 4:
        raise AssertionError("scale degree")

    mapped_y = -R(1, 100) + u / 50
    mapped_x = xlo + v / 1000
    if os.environ.get("XADJ_BREAK_SEAM") == "1":
        mapped_x += R(1, 10000)
    predecessor_mapped_x = R(78, 125) + v / 500
    zero(mapped_x.subs(v, 0) - predecessor_mapped_x.subs(v, 1),
         "parameter seam")
    zero(
        transformed.subs(x, mapped_x).subs(v, 0)
        - transformed.subs(x, predecessor_mapped_x).subs(v, 1),
        "raw-gate seam",
    )
    expected = [
        (1, [0, 0, 0], 1, ((0, 0, 0), R(5))),
        (5, [0, 2, 2], 9, ((0, 2, 2), R(204229, 300000))),
        (26, [1, 4, 4], 50,
         ((0, 4, 0), R(153893289799, 12656250000))),
        (42, [2, 6, 6], 147,
         ((0, 6, 0), R(130268743001281, 237304687500000))),
        (120, [3, 8, 8], 324,
         ((0, 8, 0), R(99445552715982526441, 26696777343750000000))),
    ]
    total_controls = 0
    for power in range(5):
        coefficient = sp.factor(quartic.nth(power))
        if power == 0:
            residual = coefficient
        else:
            residual = sp.cancel(coefficient / S)
            zero(coefficient - S * residual, f"C{power} exact S factor")
        mapped = sp.factor(residual.subs({x: mapped_x, y: mapped_y}))
        degrees, controls = power_to_bernstein(mapped, (S, u, v))
        if os.environ.get("XADJ_DROP_CONTROL") == "1" and power == 4:
            controls.pop(max(controls))
        predecessor_mapped = sp.factor(
            residual.subs({x: predecessor_mapped_x, y: mapped_y})
        )
        predecessor_degrees, predecessor_controls = power_to_bernstein(
            predecessor_mapped, (S, u, v)
        )
        minimum = min(controls.items(), key=lambda item: item[1])
        minima = sorted(
            index for index, value in controls.items() if value == minimum[1]
        )
        if any(value <= 0 for value in controls.values()):
            bad = [(index, value) for index, value in controls.items() if value <= 0]
            raise AssertionError(f"C{power} certificate insufficiency: {bad[:3]}")
        term_count = len(sp.Poly(coefficient, S, x, y).terms())
        expected_terms, expected_degrees, expected_count, expected_minimum = expected[power]
        if term_count != expected_terms:
            raise AssertionError(f"C{power} term-count drift: {term_count}")
        if degrees != expected_degrees:
            raise AssertionError(f"C{power} degree drift: {degrees}")
        if len(controls) != expected_count:
            raise AssertionError(f"C{power} control-count drift: {len(controls)}")
        if expected_minimum is not None and minimum != expected_minimum:
            raise AssertionError(f"C{power} minimum drift: {minimum}")
        if expected_minimum is not None and minima != [expected_minimum[0]]:
            raise AssertionError(f"C{power} minimum multiplicity drift: {minima}")
        if degrees != predecessor_degrees:
            raise AssertionError(f"C{power} predecessor degree drift")
        for s_index in range(degrees[0] + 1):
            for y_index in range(degrees[1] + 1):
                if controls[(s_index, y_index, 0)] != predecessor_controls[
                    (s_index, y_index, degrees[2])
                ]:
                    raise AssertionError(
                        f"C{power} control seam: {(s_index, y_index)}"
                    )
        print(f"C{power}_TERMS={term_count}")
        print(f"C{power}_DEGREES={degrees}")
        print(f"C{power}_CONTROLS={len(controls)}")
        print(f"C{power}_MIN={minimum[0]}:{minimum[1]}")
        print(f"C{power}_ALL_GLOBAL_MINIMA={minima}")
        total_controls += len(controls)

    diagnostic_values = []
    for Sv, xv, yv, lv in product(
        [R(1, 100), R(1, 2), R(1)],
        [xlo, (xlo + xhi) / 2, xhi],
        [-R(1, 100), R(0), R(1, 100)],
        [R(1, 10), R(1), R(10)],
    ):
        value = sp.factor(transformed.subs({S: Sv, x: xv, y: yv, lam: lv}))
        if value <= 0:
            raise AssertionError(f"legal exact raw negative: {(Sv,xv,yv,lv,value)}")
        diagnostic_values.append(value)
    print(f"DANGER_LOWER={danger_lower}")
    print("DETC_OVER_S=5/72")
    print(f"TOTAL_CONTROLS={total_controls}")
    print(f"DIAGNOSTICS={len(diagnostic_values)}/81")
    diagnostic_minimum = min(diagnostic_values)
    expected_diagnostic_minimum = R(
        5250817175623018829949177505801319,
        1049760000000000000000000000000000,
    )
    if (
        len(diagnostic_values) != 81
        or diagnostic_minimum != expected_diagnostic_minimum
    ):
        raise AssertionError("diagnostic drift")
    print(f"DIAGNOSTIC_MIN={diagnostic_minimum}")
    print("PASS predecessor bindings")
    print("PASS strict adjacent-x legality, rank two, and both signed-z lifts")
    print("PASS original fully conjugated Hermitian Q,Q^2 reconstruction")
    print("PASS exact parameter/raw-gate/control seam at x=313/500")
    print("PASS exact positive coefficient certificates on adjacent (S,y,x) box")
    print("scope=313/500<=x<=627/1000, |y|<=1/100, Z=1/8, 0<h<=1, lambda>0")


if __name__ == "__main__":
    main()
x