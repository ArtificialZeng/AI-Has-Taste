#!/usr/bin/env python3
"""Literal-free no-import referee scout for the x=5/8, Z=1/8 y-strip.

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
SOURCE = ROOT / "tmp/research/compact_ball_uncovered_ray_x5_8_ystrip_exact_gate.py"
SOURCE_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_compact_ball_uncovered_ray_x5_8_ystrip_source_candidate.md"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_uncovered_ray_x5_8_ystrip_source_freeze_manifest.sha256"
PREV_REFEREE = ROOT / "tmp/research/audit/verify_compact_ball_uncovered_ray_x5_8_independent_referee.py"
PREV_REPORT = ROOT / "audit/COMPACT_BALL_UNCOVERED_RAY_X5_8_INDEPENDENT_REFEREE_AUDIT.md"
PREV_MANIFEST = ROOT / "tmp/research/audit/compact_ball_uncovered_ray_x5_8_independent_referee_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED_SOURCE_SHA = "f609a892135bd8de66bd164b153777419646ec9d134bbf4fb5f04031642cfbf3"
EXPECTED_MANIFEST_SHA = "b367f31b472726cc5b02a4263d26ff82582741f45a021b1595ac4debdf090545"
EXPECTED_DEPENDENCIES = {
    SOURCE_NOTE: "982976dc83a0cc7f85fbdccf9e37fdb3a8701220b2dcd2fdb12e12c8a599e154",
    PREV_REFEREE: "bd6c4464c329eed3d2726ef07e4d2d1bf5562483e17acff8933da88bec110af6",
    PREV_REPORT: "6435049d14d61d28a8817d3d72e5e3eae9f131af8eadc48ea0176dab2c8dbab6",
    PREV_MANIFEST: "555b32688d91fb91de7b8ce0c56081758cb1bf7f1a50e10ae2db93df9a56633f",
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


def eliminate(expr: sp.Expr, h: sp.Symbol, q: sp.Symbol, z: sp.Symbol,
              Z: sp.Symbol, S: sp.Symbol) -> sp.Expr:
    """Different elimination order: h, q, then signed z."""
    value = sp.expand(expr)
    value = sp.rem(sp.expand(value), h**2 - S, h)
    value = sp.rem(sp.expand(value), q**2 - (1 - S), q)
    value = sp.rem(value, z**2 - Z, z)
    return sp.factor(value)


def permuted_square(matrix: sp.Matrix) -> sp.Matrix:
    """Explicit Q^2 multiplication in the independent order 0,2,1."""
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sum(
        matrix[i, k] * matrix[k, j] for k in (0, 2, 1)
    )))


def strip_certificate(poly: sp.Expr, S: sp.Symbol, y: sp.Symbol,
                      u: sp.Symbol, *, drop_control: bool = False) -> dict[str, object]:
    """Factor S-adic order and certify the mapped (S,u) residual on [0,1]^2."""
    expanded = sp.Poly(sp.expand(poly), S, y)
    require(expanded.as_expr() != 0, "nonzero lambda coefficient")
    order = min(powers[0] for powers, coefficient in expanded.terms() if coefficient)
    residual = sp.factor(expanded.as_expr() / S**order)
    mapped = sp.expand(residual.subs(y, -sp.Rational(1, 100) + u / 50))
    mapped_poly = sp.Poly(mapped, S, u)
    degree_s, degree_u = mapped_poly.degree(S), mapped_poly.degree(u)
    power = {powers: coefficient for powers, coefficient in mapped_poly.terms()}
    bernstein: dict[tuple[int, int], sp.Expr] = {}
    for i in range(degree_s + 1):
        for j in range(degree_u + 1):
            value = sp.Rational(0)
            for a in range(i + 1):
                for b in range(j + 1):
                    value += (power.get((a, b), 0)
                              * sp.Rational(math.comb(i, a), math.comb(degree_s, a))
                              * sp.Rational(math.comb(j, b), math.comb(degree_u, b)))
            bernstein[(i, j)] = sp.factor(value)
    expected_count = (degree_s + 1) * (degree_u + 1)
    if drop_control:
        bernstein.pop(max(bernstein))
    require(len(bernstein) == expected_count,
            "complete independently derived strip controls")
    require(all(value > 0 for value in bernstein.values()),
            "strict strip Bernstein controls")
    return {
        "order": order,
        "residual": residual,
        "mapped": mapped,
        "degree_s": degree_s,
        "degree_u": degree_u,
        "bernstein": tuple(sorted(bernstein.items())),
    }


def reconstruct(*, source_path: Path = SOURCE,
                manifest_path: Path = SOURCE_MANIFEST,
                dependency_path: Path = PREV_REFEREE,
                attack: str = "none") -> dict[str, object]:
    require(__debug__, "optimized Python is forbidden")
    require(sha(source_path) == EXPECTED_SOURCE_SHA,
            "frozen candidate source SHA-256")
    require(sha(manifest_path) == EXPECTED_MANIFEST_SHA,
            "frozen source-manifest SHA-256")
    require(sha(dependency_path) == EXPECTED_DEPENDENCIES[PREV_REFEREE],
            "frozen predecessor-referee SHA-256")
    for path, expected in EXPECTED_DEPENDENCIES.items():
        if path != PREV_REFEREE:
            require(sha(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS opaque source/note/manifest and predecessor/reduction hashes")
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
    # Independent Gram order: signed-z column first, mixed column second.
    mixed_column = h * r + (j - I * k) * f
    signed_z_column = ell * f
    H_gram = sp.expand(signed_z_column * sp.conjugate(signed_z_column.T)
                       + mixed_column * sp.conjugate(mixed_column.T))
    require(all(zero(entry) for entry in H_direct - H_gram),
            "direct compression equals independent Gram columns")
    H = H_gram
    require(eliminate((sp.conjugate(r.T) * r)[0] - 1, h, q, z, Z, S) == 0,
            "r unit norm")
    require(eliminate((sp.conjugate(f.T) * f)[0] - 1, h, q, z, Z, S) == 0,
            "f unit norm")
    require(eliminate((sp.conjugate(r.T) * f)[0], h, q, z, Z, S) == 0,
            "frame orthogonal")
    require(all(zero(entry) for entry in H - sp.conjugate(H.T)), "H Hermitian")
    require(all(zero(entry) for entry in H - H.subs(z, -z)),
            "both signed-z lifts agree")
    require(eliminate(C.det() - R(5, 9) * S * Z, h, q, z, Z, S) == 0,
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
    gate_shape = eliminate(vector_gate, h, q, z, Z, S)
    require(not gate_shape.has(z, h, q), "all frame radicals cancel")
    require(zero(sp.im(gate_shape)), "raw gate real")
    print("PASS fully conjugated raw gate and radical elimination")

    # Strict legality of the complete y-strip, independently reconstructed.
    y, u = sp.symbols("y u", real=True)
    shape = {xb: R(5, 8), yb: y, Z: R(1, 8)}
    danger_sign = -1 if attack == "flip-danger" else 1
    danger = sp.factor(1 - shape[xb]**2 - shape[yb]**2
                       - danger_sign * shape[Z])
    require(zero(danger - (R(31, 64) - y**2)),
            "exact y-strip danger scalar")
    danger_reserve = sp.factor(danger.subs(y, R(1, 100)))
    require(danger_reserve == R(19371, 40000) and danger_reserve > 0,
            "strict danger reserve 19371/40000")
    det_ratio = R(5, 9) * shape[Z]
    require(det_ratio == R(5, 72) and det_ratio > 0,
            "strict det(C)/S=5/72")
    legality_gates = [
        danger_reserve > 0,
        det_ratio > 0,
        shape[Z] > 0,
        1 - shape[Z] > 0,
        all(zero(entry) for entry in
            H.subs(shape).subs(z, -z) - H.subs(shape)),
    ]
    require(len(legality_gates) == 5 and all(legality_gates),
            "complete y-strip legality gate list")
    print("PASS danger>=19371/40000, det(C), both-z and rank-two legality")

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
    require(len(checked_coefficients) == lambda_degree + 1,
            "complete five lambda coefficient gates")
    rebuilt = sp.expand(sum(checked_coefficients[power] * lam**power
                            for power in range(len(checked_coefficients))))
    require(zero(rebuilt - gamma36), "derived coefficient reconstruction")
    certificates = tuple(strip_certificate(
        coefficient, S, y, u,
        drop_control=(attack == "drop-control" and power == lambda_degree)
    ) for power, coefficient in enumerate(coefficients))
    control_count = sum(len(certificate["bernstein"])
                        for certificate in certificates)
    coefficient_sha = hashlib.sha256(
        str(coefficients).encode("utf-8")).hexdigest()
    control_signature = tuple(
        (certificate["order"], certificate["degree_s"],
         certificate["degree_u"], certificate["bernstein"])
        for certificate in certificates
    )
    control_sha = hashlib.sha256(
        str(control_signature).encode("utf-8")).hexdigest()
    for power, (coefficient, certificate) in enumerate(zip(coefficients, certificates)):
        print(f"STRIP_COEFFICIENT_{power} {coefficient}")
        print(f"STRIP_CERTIFICATE_{power} order={certificate['order']} "
              f"degrees=({certificate['degree_s']},{certificate['degree_u']}) "
              f"controls={certificate['bernstein']}")
    print(f"TOTAL_STRIP_CONTROL_COUNT {control_count}")
    print(f"STRIP_COEFFICIENTS_SHA256 {coefficient_sha}")
    print(f"STRIP_CONTROLS_SHA256 {control_sha}")
    print("PASS all independently derived strip controls strictly positive")
    print("PASS 36*Gamma>0 for every |y|<=1/100, 0<S<=1, lambda>0")

    diagnostic_count = 0
    diagnostic_minimum = None
    diagnostic_data = None
    sample_s = (R(1, 1000000), R(1, 100), R(1))
    sample_y = (-R(1, 100), R(0), R(1, 100))
    sample_lambda = (R(1, 1000), R(1), R(1000))
    expected_diagnostics = math.prod(map(len, (sample_s, sample_y,
                                                sample_lambda)))
    for sval in sample_s:
        for yval in sample_y:
            for lval in sample_lambda:
                value = sp.factor(gamma36.subs({S: sval, y: yval, lam: lval}))
                require(value > 0, "exact diagnostic gate value")
                if diagnostic_minimum is None or value < diagnostic_minimum:
                    diagnostic_minimum = value
                    diagnostic_data = (sval, yval, lval)
                diagnostic_count += 1
    require(diagnostic_count == expected_diagnostics,
            "derived exact diagnostic count")
    print(f"PASS {diagnostic_count} exact diagnostics only; "
          f"minimum={diagnostic_minimum} at {diagnostic_data}")
    print("SCOPE no numerical inference and no CE-046/048/059/060 reuse")
    return {
        "gamma36": gamma36,
        "lambda_degree": lambda_degree,
        "coefficients": coefficients,
        "certificates": certificates,
        "control_count": control_count,
        "coefficient_sha": coefficient_sha,
        "control_sha": control_sha,
        "danger": danger,
        "danger_reserve": danger_reserve,
        "det_ratio": det_ratio,
        "diagnostic_count": diagnostic_count,
        "diagnostic_minimum": diagnostic_minimum,
        "diagnostic_data": diagnostic_data,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path, default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "drop-q2", "flip-danger", "corrupt-coefficient", "drop-control"
    ), default="none")
    args = parser.parse_args()
    reconstruct(source_path=args.source_path,
                manifest_path=args.manifest_path,
                dependency_path=args.dependency_path,
                attack=args.attack)
    print("LITERAL_FREE_SCOUT PASS")


if __name__ == "__main__":
    main()
