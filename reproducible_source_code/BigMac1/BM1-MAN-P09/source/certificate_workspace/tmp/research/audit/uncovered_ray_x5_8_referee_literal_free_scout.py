#!/usr/bin/env python3
"""Literal-free no-import referee scout for shape (5/8,0,1/8).

The current source, source note, source manifest, and coverage artifacts are
opaque SHA-256 inputs only.  The five lambda coefficients are reconstructed
from the original Hermitian frame and are not frozen in this scout.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_uncovered_ray_x5_8_preflight.py"
SOURCE_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_uncovered_ray_x5_8_source_candidate.md"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_uncovered_ray_x5_8_source_freeze_manifest.sha256"
COVERAGE_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_stitched_x_sheet_coverage_audit.md"
COVERAGE_MANIFEST = ROOT / "tmp/research/compact_ball_stitched_x_sheet_coverage_audit_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED_SOURCE_SHA = "9ed1c14f3616c88de59d8ff3c2b2aa93a772f40b488cdb2246144b74195f5e6f"
EXPECTED_MANIFEST_SHA = "0859899d0d4c04a490eefab4bd219a8254e49c0cd4467ed7e31f8a6ce0176a21"
EXPECTED_DEPENDENCIES = {
    SOURCE_NOTE: "15223a05f711dc819e43cfe43261a5c34858eb9abead5f88b133cfa578dd7002",
    COVERAGE_NOTE: "45837237f7772cffc2340e6f5f3b2fde773a480712e0b02124c8c5f98d5b6447",
    COVERAGE_MANIFEST: "5b84c3f0c4aa263b30265e0dfed65b288dd2eaafae474eee45d143c1d6585ab8",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def eliminate(expr: sp.Expr, z: sp.Symbol, h: sp.Symbol, q: sp.Symbol,
              Z: sp.Symbol, S: sp.Symbol) -> sp.Expr:
    """Different elimination order: signed z, h, then q."""
    value = sp.expand(expr)
    value = sp.rem(value, z**2 - Z, z)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    value = sp.rem(sp.expand(value), q**2 - (1 - S), q)
    return sp.factor(value)


def permuted_square(matrix: sp.Matrix) -> sp.Matrix:
    """Explicit Q^2 multiplication in the independent order 1,2,0."""
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sum(
        matrix[i, k] * matrix[k, j] for k in (1, 2, 0)
    )))


def positive_s_certificate(poly: sp.Expr, S: sp.Symbol) -> dict[str, object]:
    """Factor the exact S-adic order and certify the residual on [0,1]."""
    expanded = sp.Poly(sp.expand(poly), S)
    require(expanded.as_expr() != 0, "nonzero lambda coefficient")
    powers = [power[0] for power, coefficient in expanded.terms() if coefficient]
    order = min(powers)
    residual = sp.factor(expanded.as_expr() / S**order)
    residual_poly = sp.Poly(sp.expand(residual), S)
    degree = residual_poly.degree()
    power = {term[0][0]: term[1] for term in residual_poly.terms()}
    bernstein = []
    for i in range(degree + 1):
        value = sp.Rational(0)
        for k in range(i + 1):
            value += (power.get(k, 0)
                      * sp.Rational(math.comb(i, k), math.comb(degree, k)))
        bernstein.append(sp.factor(value))
    require(all(value > 0 for value in bernstein),
            "strict residual Bernstein coefficients")
    return {
        "order": order,
        "residual": residual,
        "degree": degree,
        "bernstein": tuple(bernstein),
    }


def reconstruct(*, source_path: Path = SOURCE,
                manifest_path: Path = SOURCE_MANIFEST,
                coverage_path: Path = COVERAGE_NOTE,
                attack: str = "none") -> dict[str, object]:
    require(__debug__, "optimized Python is forbidden")
    require(sha(source_path) == EXPECTED_SOURCE_SHA,
            "frozen candidate source SHA-256")
    require(sha(manifest_path) == EXPECTED_MANIFEST_SHA,
            "frozen source-manifest SHA-256")
    require(sha(coverage_path) == EXPECTED_DEPENDENCIES[COVERAGE_NOTE],
            "frozen coverage-note SHA-256")
    for path, expected in EXPECTED_DEPENDENCIES.items():
        if path != COVERAGE_NOTE:
            require(sha(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS opaque source/note/manifest and coverage/reduction hashes")
    print("INDEPENDENCE candidate and source note never parsed/imported/executed")

    R, I = sp.Rational, sp.I
    S, Z = sp.symbols("S Z", real=True)
    h, q, z = sp.symbols("h q z", real=True)
    lam = sp.symbols("lambda", real=True, positive=True)
    xb, yb = sp.symbols("x_ball y_ball", real=True)
    a, c = sp.sqrt(6) / 6, sp.sqrt(30) / 6
    phase = R(4, 5) + R(3, 5) * I
    p = sp.Matrix([a, 0, c])
    r = sp.Matrix([-a, 0, c * phase])
    f = sp.Matrix([-c * h, q, -a * h * phase])
    U = sp.Matrix.hstack(r, f)
    j = (1 + 5 * xb) / (3 * sp.sqrt(5))
    k = (-3 + 5 * yb) / (3 * sp.sqrt(5))
    ell = sp.sqrt(5) * z / 3
    C = sp.Matrix([[h**2, h * (j + I * k)],
                   [h * (j - I * k), j**2 + k**2 + ell**2]])
    H_direct = sp.expand(U * C * sp.conjugate(U.T))
    # Independent Gram order: mixed column first, signed-z column second.
    mixed_column = h * r + (j - I * k) * f
    signed_z_column = ell * f
    H_gram = sp.expand(mixed_column * sp.conjugate(mixed_column.T)
                       + signed_z_column * sp.conjugate(signed_z_column.T))
    require(all(zero(entry) for entry in H_direct - H_gram),
            "direct compression equals independent Gram columns")
    H = H_gram
    require(eliminate((sp.conjugate(r.T) * r)[0] - 1, z, h, q, Z, S) == 0,
            "r unit norm")
    require(eliminate((sp.conjugate(f.T) * f)[0] - 1, z, h, q, Z, S) == 0,
            "f unit norm")
    require(eliminate((sp.conjugate(r.T) * f)[0], z, h, q, Z, S) == 0,
            "frame orthogonal")
    require(all(zero(entry) for entry in H - sp.conjugate(H.T)), "H Hermitian")
    require(all(zero(entry) for entry in H - H.subs(z, -z)),
            "both signed-z lifts agree")
    require(eliminate(C.det() - R(5, 9) * S * Z, z, h, q, Z, S) == 0,
            "det(C)=(5/9)SZ")

    Q = sp.expand(lam * H)
    Q2 = permuted_square(Q)
    direct_Q2 = sp.expand(Q * Q)
    for row in range(3):
        for column in range(3):
            require(zero(Q2[row, column] - direct_Q2[row, column]),
                    f"Q^2 entry ({row},{column})")
    require(all(zero(entry) for entry in Q2 - sp.conjugate(Q2.T)),
            "Q^2 Hermitian")
    print("PASS original frame/compression and Q^2 9/9")

    xi = sp.expand(Q * p)
    q220 = 0 if attack == "drop-q2" else Q2[2, 0]
    literal_terms = [
        4 * a**2 * xi[1] * sp.conjugate(xi[1]),
        (c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - q220))
        * sp.conjugate(c * sp.conjugate(xi[0]) + a * xi[2]
                       + I * (a * c - q220)),
        (c * sp.conjugate(xi[1]) - I * Q2[2, 1])
        * sp.conjugate(c * sp.conjugate(xi[1]) - I * Q2[2, 1]),
        -32 * a**2 * ((xi[0] + sp.conjugate(xi[0])) / 2)**2,
    ]
    literal_gate = sp.expand(sum(literal_terms))
    eta = sp.expand(H * p)
    H2 = permuted_square(H)
    b0 = sp.Matrix([0, I * a * c, 0])
    linear = sp.Matrix([2 * a * eta[1],
                        c * sp.conjugate(eta[0]) + a * eta[2],
                        c * sp.conjugate(eta[1])])
    quadratic = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector = b0 + lam * linear + lam**2 * quadratic
    vector_gate = sp.expand((sp.conjugate(vector.T) * vector)[0]
                            - 32 * a**2 * lam**2
                            * ((eta[0] + sp.conjugate(eta[0])) / 2)**2)
    require(zero(literal_gate - vector_gate),
            "fully conjugated literal gate equals vector gate")
    gate_shape = eliminate(vector_gate, z, h, q, Z, S)
    require(not gate_shape.has(z, h, q), "all frame radicals cancel")
    require(zero(sp.im(gate_shape)), "raw gate real")
    print("PASS fully conjugated raw gate and radical elimination")

    # Strict legality of the fixed ray, independent of coverage claims.
    shape = {xb: R(5, 8), yb: 0, Z: R(1, 8)}
    danger_sign = -1 if attack == "flip-danger" else 1
    danger = sp.factor(1 - shape[xb]**2 - shape[yb]**2
                       - danger_sign * shape[Z])
    require(danger == R(31, 64), "strict danger reserve 31/64")
    det_ratio = R(5, 9) * shape[Z]
    require(det_ratio == R(5, 72) and det_ratio > 0,
            "strict det(C)/S=5/72")
    legality_gates = [
        danger > 0,
        det_ratio > 0,
        shape[Z] > 0,
        1 - shape[Z] > 0,
        all(zero(entry) for entry in
            H.subs(shape).subs(z, -z) - H.subs(shape)),
    ]
    if attack == "drop-gate":
        legality_gates.pop()
    require(len(legality_gates) == 5 and all(legality_gates),
            "complete fixed-ray legality gate list")
    print("PASS strict danger/det(C)/both-z/rank-two legality for every 0<S<=1")

    gamma36 = sp.factor(36 * gate_shape.subs(shape))
    gamma_poly = sp.Poly(sp.expand(gamma36), lam)
    lambda_degree = gamma_poly.degree()
    coefficients = tuple(sp.factor(gamma_poly.coeff_monomial(lam**power))
                         for power in range(lambda_degree + 1))
    require(lambda_degree == 4 and len(coefficients) == 5,
            "five independently derived lambda coefficients")
    checked_coefficients = list(coefficients)
    if attack == "corrupt-coefficient":
        checked_coefficients[2] = sp.expand(checked_coefficients[2] + 1)
    if attack == "drop-gate":
        checked_coefficients.pop()
    require(len(checked_coefficients) == lambda_degree + 1,
            "complete five lambda coefficient gates")
    rebuilt = sp.expand(sum(checked_coefficients[power] * lam**power
                            for power in range(len(checked_coefficients))))
    require(zero(rebuilt - gamma36), "derived coefficient reconstruction")
    certificates = tuple(positive_s_certificate(coefficient, S)
                         for coefficient in coefficients)
    for power, (coefficient, certificate) in enumerate(zip(coefficients, certificates)):
        print(f"LAMBDA_COEFFICIENT_{power} {coefficient}")
        print(f"S_CERTIFICATE_{power} order={certificate['order']} "
              f"degree={certificate['degree']} bernstein={certificate['bernstein']}")
    print("PASS all five lambda coefficients strictly positive for 0<S<=1")
    print("PASS 36*Gamma>0 for every lambda>0 on the fixed ray")

    diagnostic_count = 0
    diagnostic_minimum = None
    diagnostic_data = None
    for sval in (R(1, 1000000), R(1, 100), R(1)):
        for lval in (R(1, 1000), R(1), R(1000)):
            value = sp.factor(gamma36.subs({S: sval, lam: lval}))
            require(value > 0, "exact diagnostic gate value")
            if diagnostic_minimum is None or value < diagnostic_minimum:
                diagnostic_minimum = value
                diagnostic_data = (sval, lval)
            diagnostic_count += 1
    print(f"PASS {diagnostic_count} exact diagnostics only; "
          f"minimum={diagnostic_minimum} at {diagnostic_data}")
    print("SCOPE no numerical inference and no CE-046/048/059/060 reuse")
    return {
        "gamma36": gamma36,
        "lambda_degree": lambda_degree,
        "coefficients": coefficients,
        "certificates": certificates,
        "danger": danger,
        "det_ratio": det_ratio,
        "diagnostic_count": diagnostic_count,
        "diagnostic_minimum": diagnostic_minimum,
        "diagnostic_data": diagnostic_data,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--coverage-path", type=Path, default=COVERAGE_NOTE)
    parser.add_argument("--attack", choices=(
        "none", "drop-q2", "flip-danger", "corrupt-coefficient", "drop-gate"
    ), default="none")
    args = parser.parse_args()
    reconstruct(source_path=args.source_path,
                manifest_path=args.manifest_path,
                coverage_path=args.coverage_path,
                attack=args.attack)
    print("LITERAL_FREE_SCOUT PASS")


if __name__ == "__main__":
    main()
