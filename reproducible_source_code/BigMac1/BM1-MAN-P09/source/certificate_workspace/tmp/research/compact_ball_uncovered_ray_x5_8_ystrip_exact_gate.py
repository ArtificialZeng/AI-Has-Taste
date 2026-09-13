#!/usr/bin/env python3
"""Exact source gate for the y-thickening of the audited x=5/8 ray."""

if not __debug__:
    raise RuntimeError("do not run with python -O")

from math import comb
import hashlib
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BOUND = {
    "tmp/research/compact_ball_uncovered_ray_x5_8_preflight.py":
        "9ed1c14f3616c88de59d8ff3c2b2aa93a772f40b488cdb2246144b74195f5e6f",
    "tmp/research/compact_ball_uncovered_ray_x5_8_source_freeze_manifest.sha256":
        "0859899d0d4c04a490eefab4bd219a8254e49c0cd4467ed7e31f8a6ce0176a21",
    "tmp/research/audit/verify_compact_ball_uncovered_ray_x5_8_independent_referee.py":
        "bd6c4464c329eed3d2726ef07e4d2d1bf5562483e17acff8933da88bec110af6",
    "audit/COMPACT_BALL_UNCOVERED_RAY_X5_8_INDEPENDENT_REFEREE_AUDIT.md":
        "6435049d14d61d28a8817d3d72e5e3eae9f131af8eadc48ea0176dab2c8dbab6",
    "tmp/research/audit/compact_ball_uncovered_ray_x5_8_independent_referee_manifest.sha256":
        "555b32688d91fb91de7b8ce0c56081758cb1bf7f1a50e10ae2db93df9a56633f",
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
    for index in __import__("itertools").product(*[range(d + 1) for d in degrees]):
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
        if os.environ.get("YSTRIP_BAD_PREDECESSOR") == "1" and "source_freeze" in rel:
            expected = "0" * 64
        if sha256(ROOT / rel) != expected:
            raise AssertionError(f"predecessor binding: {rel}")

    I = sp.I
    R = sp.Rational
    h, q, lam, S, y, u = sp.symbols("h q lambda S y u", real=True)
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

    x = R(5, 8)
    Z = R(1, 8)
    danger = sp.factor(1 - x**2 - y**2 - Z)
    if sp.factor(danger - (R(31, 64) - y**2)) != 0:
        raise AssertionError("shape danger identity")
    danger_lower = sp.factor(danger.subs(y**2, R(1, 10000)))
    if danger_lower != R(19371, 40000) or danger_lower <= 0:
        raise AssertionError("shape strip danger bound")

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    ell2 = R(5, 9) * Z
    if os.environ.get("YSTRIP_BAD_NORMALIZATION") == "1":
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
    danger_sign = 1 if os.environ.get("YSTRIP_FLIP_DANGER") != "1" else -1
    zero(
        sp.re(xi[0])
        + danger_sign * R(5, 36) * sp.sqrt(6) * lam * h**2 * danger,
        "strict-danger scalar identity",
    )

    Q2 = sp.expand(Q * Q)
    if os.environ.get("YSTRIP_DROP_Q2") == "1":
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
    if os.environ.get("YSTRIP_CORRUPT_COEFFICIENT") == "1":
        transformed += S * lam**4
    if transformed.has(h) or transformed.has(q):
        raise AssertionError("unresolved transverse radical")
    quartic = sp.Poly(transformed, lam, domain=sp.QQ[S, y])
    if quartic.degree() != 4:
        raise AssertionError("scale degree")

    mapped_y = -R(1, 100) + u / 50
    expected = [
        ([0, 0], 1, ((0, 0), R(5))),
        ([0, 2], 3, ((0, 2), R(2743, 4000))),
        ([1, 4], 10, ((0, 4), R(6994764611, 576000000))),
        ([2, 6], 21, ((0, 6), R(140490493103, 256000000000))),
        ([3, 8], 36, ((0, 8), R(205239422872780721, 55296000000000000))),
    ]
    total_controls = 0
    minima = []
    for power in range(5):
        coefficient = sp.factor(quartic.nth(power))
        if power == 0:
            residual = coefficient
        else:
            quotient = sp.cancel(coefficient / S)
            zero(coefficient - S * quotient, f"C{power} exact S factor")
            residual = quotient
        mapped = sp.factor(residual.subs(y, mapped_y))
        degrees, controls = power_to_bernstein(mapped, (S, u))
        minimum = min(controls.items(), key=lambda item: item[1])
        if any(value <= 0 for value in controls.values()):
            bad = [(index, value) for index, value in controls.items() if value <= 0]
            raise AssertionError(f"C{power} certificate insufficiency: {bad[:3]}")
        expected_degrees, expected_count, expected_minimum = expected[power]
        if degrees != expected_degrees:
            raise AssertionError(f"C{power} degree drift: {degrees}")
        if len(controls) != expected_count:
            raise AssertionError(f"C{power} control-count drift: {len(controls)}")
        if minimum != expected_minimum:
            raise AssertionError(f"C{power} minimum drift: {minimum}")
        print(f"C{power}={coefficient}")
        print(f"C{power}_DEGREES={degrees}")
        print(f"C{power}_CONTROLS={len(controls)}")
        print(f"C{power}_MIN={minimum[0]}:{minimum[1]}")
        total_controls += len(controls)
        minima.append(minimum)

    diagnostic_values = []
    for Sv in [R(1, 100), R(1, 2), R(1)]:
        for yv in [-R(1, 100), R(0), R(1, 100)]:
            for lv in [R(1, 10), R(1), R(10)]:
                value = sp.factor(transformed.subs({S: Sv, y: yv, lam: lv}))
                if value <= 0:
                    raise AssertionError(f"legal exact raw negative: {(Sv,yv,lv,value)}")
                diagnostic_values.append(value)
    print(f"TOTAL_CONTROLS={total_controls}")
    print(f"DIAGNOSTICS={len(diagnostic_values)}/27")
    print(f"DIAGNOSTIC_MIN={min(diagnostic_values)}")
    print("PASS predecessor bindings")
    print("PASS strict strip legality, rank two, and both signed-z lifts")
    print("PASS original fully conjugated Hermitian Q,Q^2 reconstruction")
    print("PASS exact positive coefficient certificates on (S,y) box")
    print("scope=x=5/8, Z=1/8, |y|<=1/100, 0<h<=1, lambda>0")


if __name__ == "__main__":
    main()
