#!/usr/bin/env python3
"""Definition-level exact source for the uncovered rational shape ray."""

if not __debug__:
    raise RuntimeError("do not run with python -O")

import hashlib
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COVERAGE_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_stitched_x_sheet_coverage_audit.md"
COVERAGE_MANIFEST = ROOT / "tmp/research/compact_ball_stitched_x_sheet_coverage_audit_manifest.sha256"
EXPECTED_COVERAGE_NOTE = "45837237f7772cffc2340e6f5f3b2fde773a480712e0b02124c8c5f98d5b6447"
EXPECTED_COVERAGE_MANIFEST = "5b84c3f0c4aa263b30265e0dfed65b288dd2eaafae474eee45d143c1d6585ab8"


def file_sha256(path):
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


def main():
    expected_note = EXPECTED_COVERAGE_NOTE
    if os.environ.get("UNCOVERED_RAY_BAD_COVERAGE") == "1":
        expected_note = "0" * 64
    if file_sha256(COVERAGE_NOTE) != expected_note:
        raise AssertionError("coverage note hash")
    if file_sha256(COVERAGE_MANIFEST) != EXPECTED_COVERAGE_MANIFEST:
        raise AssertionError("coverage manifest hash")

    I = sp.I
    R = sp.Rational
    h, q, lam, S = sp.symbols("h q lambda S", real=True)
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
    y = R(0)
    Z = R(1, 8)
    radius2 = x**2 + y**2 + Z
    if radius2 != R(33, 64) or not radius2 < 1:
        raise AssertionError("shape legality")
    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    ell2 = R(5, 9) * Z
    if os.environ.get("UNCOVERED_RAY_BAD_NORMALIZATION") == "1":
        ell2 += R(1, 100)
    W = sp.factor(j**2 + k**2 + ell2)
    if W != R(373, 576):
        raise AssertionError(f"W={W}")

    C = sp.Matrix([[h**2, h * (j + I * k)], [h * (j - I * k), W]])
    zero(C.det() - R(5, 72) * h**2, "compression determinant")
    H = sp.expand(U * C * U.conjugate().T)
    ell = sp.sqrt(R(5, 9) * Z)
    g1 = sp.expand(h * rvec + (j - I * k) * fvec)
    g2plus = sp.expand(ell * fvec)
    g2minus = sp.expand(-ell * fvec)
    Hplus = sp.expand(g1 * g1.conjugate().T + g2plus * g2plus.conjugate().T)
    Hminus = sp.expand(g1 * g1.conjugate().T + g2minus * g2minus.conjugate().T)
    zero(H - Hplus, "positive signed-z Gram lift")
    zero(H - Hminus, "negative signed-z Gram lift")
    zero(H * nvec, "kernel identity")
    Q = sp.expand(lam * H)
    zero(Q - Q.conjugate().T, "Q Hermitian")
    xi = sp.expand(Q * p)
    danger_sign = 1
    if os.environ.get("UNCOVERED_RAY_FLIP_DANGER") == "1":
        danger_sign = -1
    zero(sp.re(xi[0]) + danger_sign * R(155, 2304) * sp.sqrt(6) * lam * h**2,
         "strict danger")

    Q2 = sp.expand(Q * Q)
    if os.environ.get("UNCOVERED_RAY_DROP_Q2") == "1":
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
    gram = sp.expand(
        ((B0 + lam * L + lam**2 * N).conjugate().T
         * (B0 + lam * L + lam**2 * N))[0]
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
    if transformed.has(h) or transformed.has(q):
        raise AssertionError("unresolved radical")
    quartic = sp.Poly(transformed, lam, domain=sp.QQ[S])
    if quartic.degree() != 4:
        raise AssertionError("scale degree")

    claims = [
        R(5),
        R(85, 96) * S,
        R(215, 331776) * S * (21249 * S + 19037),
        R(5, 31850496) * S * (2654208 * S**2 + 8572032 * S + 4083977),
        R(1, 110075314176) * S * (
            987426091008 * S**3
            + 2214366284160 * S**2
            + 1677691247279 * S
            + 423511736838
        ),
    ]
    if os.environ.get("UNCOVERED_RAY_BAD_EXPECTED") == "1":
        claims[-1] += S
    for power, claim in enumerate(claims):
        zero(quartic.nth(power) - claim, f"quartic coefficient C{power}")
        coefficient = sp.factor(quartic.nth(power))
        print(f"C{power}={coefficient}")
        if power:
            quotient = sp.factor(sp.cancel(coefficient / S))
            poly = sp.Poly(sp.expand(quotient), S, domain=sp.QQ)
            coefficients = poly.all_coeffs()
            if any(value <= 0 for value in coefficients):
                raise AssertionError(f"C{power}/S coefficient sign")
            print(f"C{power}/S_coeffs={coefficients}")
    print("PASS coverage dependency binding")
    print("PASS exact strict rank-two compact-ball legality")
    print("PASS both signed-z Gram lifts")
    print("PASS original fully conjugated Hermitian Q,Q^2 gate reconstruction")
    print("PASS all five scale-quartic coefficients strictly positive")
    print("scope=(x,y,Z)=(5/8,0,1/8), 0<h<=1, lambda>0; full ball open")


if __name__ == "__main__":
    main()
