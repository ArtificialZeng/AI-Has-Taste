#!/usr/bin/env python3
"""Literal-free no-import referee scout for the adjacent +x xy-cell.

The current candidate source and its freeze manifest are opaque SHA-256
inputs only.  No candidate coefficient, control, minimum, or result is read.
All frame, Hermitian, gate, coefficient, Bernstein, and predecessor-seam
objects are rebuilt from the original compact-ball definitions.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_exact_gate.py"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_source_freeze_manifest.sha256"
PREV_SOURCE = ROOT / "tmp/research/compact_ball_uncovered_box_x5_8_xy_exact_gate.py"
PREV_SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_uncovered_box_x5_8_xy_source_freeze_manifest.sha256"
PREV_REFEREE = ROOT / "tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_independent_referee.py"
PREV_REPORT = ROOT / "audit/COMPACT_BALL_UNCOVERED_BOX_X5_8_XY_INDEPENDENT_REFEREE_AUDIT.md"
PREV_MANIFEST = ROOT / "tmp/research/audit/compact_ball_uncovered_box_x5_8_xy_independent_referee_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED_SOURCE_SHA = "6ce356083b31927a41808ec54078e104358db2dcdce421cd3ccfc5dfaedf6c92"
EXPECTED_MANIFEST_SHA = "2ce9ef8ed0dface0c00328a65be9dc7c4c4a1f7c8cfb1053ac21ea96967ff15a"
EXPECTED_DEPENDENCIES = {
    PREV_SOURCE: "5e84519227b8dcae5f52ec62159936d47db1047c9219fc92dc52191d446e9b33",
    PREV_SOURCE_MANIFEST: "9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d",
    PREV_REFEREE: "ab81310af91de5d56e00caf8ae1cb5d285ab52edef5ea7c32bb6c6b85b27f8d1",
    PREV_REPORT: "d5560cb01f08bae6634f2b48710dacfda1e03bdd5f8752c651dc3c728586cb0a",
    PREV_MANIFEST: "dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd",
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
    """Independent elimination order: h, signed z, then q."""
    value = sp.expand(expr)
    value = sp.rem(value, h**2 - S, h)
    value = sp.rem(sp.expand(value), z**2 - Z, z)
    value = sp.rem(sp.expand(value), q**2 - (1 - S), q)
    return sp.factor(value)


def reordered_square(matrix: sp.Matrix) -> sp.Matrix:
    """Explicit Q^2 multiplication in the independent order 1,0,2."""
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sum(
        matrix[i, k] * matrix[k, j] for k in (1, 0, 2)
    )))


def bernstein_certificate(poly: sp.Expr, S: sp.Symbol, x: sp.Symbol,
                          y: sp.Symbol, v: sp.Symbol, u: sp.Symbol,
                          *, current: bool,
                          bad_normalization: bool = False,
                          drop_control: bool = False) -> dict[str, object]:
    """Own dense 3-variable power-to-Bernstein transform on [0,1]^3."""
    expanded = sp.Poly(sp.expand(poly), S, x, y)
    require(expanded.as_expr() != 0, "nonzero lambda coefficient")
    order = min(powers[0] for powers, coefficient in expanded.terms()
                if coefficient)
    residual = sp.factor(expanded.as_expr() / S**order)
    if current:
        denominator = 999 if bad_normalization else 1000
        x_map = sp.Rational(313, 500) + v / denominator
        require(zero(x_map.subs(v, 0) - sp.Rational(313, 500)),
                "current left x normalization")
        require(zero(x_map.subs(v, 1) - sp.Rational(627, 1000)),
                "current right x normalization")
    else:
        x_map = sp.Rational(78, 125) + v / 500
        require(zero(x_map.subs(v, 0) - sp.Rational(78, 125)),
                "predecessor left x normalization")
        require(zero(x_map.subs(v, 1) - sp.Rational(313, 500)),
                "predecessor right x normalization")
    y_map = -sp.Rational(1, 100) + u / 50
    require(zero(y_map.subs(u, 0) + sp.Rational(1, 100)),
            "lower y normalization")
    require(zero(y_map.subs(u, 1) - sp.Rational(1, 100)),
            "upper y normalization")
    mapped = sp.expand(residual.subs({x: x_map, y: y_map}))
    mapped_poly = sp.Poly(mapped, S, v, u)
    degrees = (mapped_poly.degree(S), mapped_poly.degree(v),
               mapped_poly.degree(u))
    power = {powers: coefficient for powers, coefficient in mapped_poly.terms()}
    bernstein: dict[tuple[int, int, int], sp.Expr] = {}
    for i in range(degrees[0] + 1):
        for j in range(degrees[1] + 1):
            for k in range(degrees[2] + 1):
                value = sp.Rational(0)
                for a in range(i + 1):
                    for b in range(j + 1):
                        for c in range(k + 1):
                            value += (
                                power.get((a, b, c), 0)
                                * sp.Rational(math.comb(i, a),
                                              math.comb(degrees[0], a))
                                * sp.Rational(math.comb(j, b),
                                              math.comb(degrees[1], b))
                                * sp.Rational(math.comb(k, c),
                                              math.comb(degrees[2], c))
                            )
                bernstein[(i, j, k)] = sp.factor(value)
    expected_count = math.prod(degree + 1 for degree in degrees)
    if drop_control:
        bernstein.pop(max(bernstein))
    require(len(bernstein) == expected_count,
            "complete independently derived box controls")
    require(all(value > 0 for value in bernstein.values()),
            "strict box Bernstein controls")
    weakest_index, weakest_value = min(bernstein.items(),
                                       key=lambda item: item[1])
    return {
        "order": order,
        "residual": residual,
        "mapped": mapped,
        "degrees": degrees,
        "bernstein": tuple(sorted(bernstein.items())),
        "weakest_index": weakest_index,
        "weakest_value": weakest_value,
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
            require(sha(path) == expected,
                    f"frozen dependency SHA-256: {path.name}")
    print("PASS opaque current source/manifest hashes")
    print("PASS predecessor source/referee/report/manifests and reduction hashes")
    print("INDEPENDENCE current candidate artifacts never parsed/imported/executed")

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
    mixed_column = h * r + (j - I * k) * f
    signed_z_column = ell * f
    # Reverse the predecessor's assembly: signed-z column is first.
    H_gram = sp.expand(signed_z_column * sp.conjugate(signed_z_column.T)
                       + mixed_column * sp.conjugate(mixed_column.T))
    require(all(zero(entry) for entry in H_direct - H_gram),
            "direct compression equals reverse signed-Gram assembly")
    H = H_gram
    require(eliminate((sp.conjugate(r.T) * r)[0] - 1,
                      h, q, z, Z, S) == 0, "r unit norm")
    require(eliminate((sp.conjugate(f.T) * f)[0] - 1,
                      h, q, z, Z, S) == 0, "f unit norm")
    require(eliminate((sp.conjugate(r.T) * f)[0],
                      h, q, z, Z, S) == 0, "frame orthogonal")
    require(all(zero(entry) for entry in H - sp.conjugate(H.T)),
            "H Hermitian")
    require(all(zero(entry) for entry in H - H.subs(z, -z)),
            "both signed-z lifts agree")
    require(eliminate(C.det() - R(5, 9) * S * Z,
                      h, q, z, Z, S) == 0, "det(C)=(5/9)SZ")

    Q = sp.expand(lam * H)
    Q2 = reordered_square(Q)
    direct_Q2 = sp.expand(Q * Q)
    for row in range(3):
        for column in range(3):
            require(zero(Q2[row, column] - direct_Q2[row, column]),
                    f"Q^2 entry ({row},{column})")
    require(all(zero(entry) for entry in Q2 - sp.conjugate(Q2.T)),
            "Q^2 Hermitian")
    print("PASS reverse signed-Gram/direct compression and Q^2 9/9")

    xi = sp.expand(Q * p)
    q220 = 0 if attack == "drop-q2" else Q2[2, 0]
    # Reverse component order relative to the previous referee.
    literal_terms = [
        -32 * a**2 * ((xi[0] + sp.conjugate(xi[0])) / 2)**2,
        (c * sp.conjugate(xi[1]) - I * Q2[2, 1])
        * sp.conjugate(c * sp.conjugate(xi[1]) - I * Q2[2, 1]),
        (c * sp.conjugate(xi[0]) + a * xi[2] + I * (a * c - q220))
        * sp.conjugate(c * sp.conjugate(xi[0]) + a * xi[2]
                       + I * (a * c - q220)),
        4 * a**2 * xi[1] * sp.conjugate(xi[1]),
    ]
    literal_gate = sp.expand(sum(literal_terms))
    eta = sp.expand(H * p)
    H2 = reordered_square(H)
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
    print("PASS fully conjugated raw gate and independent radical elimination")

    x, y = sp.symbols("x y", real=True)
    v, u, vp = sp.symbols("v u v_predecessor", real=True)
    shape = {xb: x, yb: y, Z: R(1, 8)}
    danger_sign = -1 if attack == "flip-danger" else 1
    danger = sp.factor(1 - x**2 - y**2 - danger_sign * shape[Z])
    require(zero(danger - (R(7, 8) - x**2 - y**2)),
            "exact adjacent-box danger scalar")
    danger_reserve = sp.factor(danger.subs(
        {x: R(627, 1000), y: R(1, 100)}))
    require(danger_reserve == R(481771, 1000000)
            and danger_reserve > 0,
            "strict adjacent-box danger reserve 481771/1000000")
    det_ratio = R(5, 9) * shape[Z]
    require(det_ratio == R(5, 72) and det_ratio > 0,
            "strict det(C)/S=5/72")
    require(shape[Z] > 0 and 1 - shape[Z] > 0,
            "strict signed-z and rank-two scalar gates")
    require(all(zero(entry) for entry in
                H.subs(shape).subs(z, -z) - H.subs(shape)),
            "complete both-z identity")
    print("PASS danger>=481771/1000000, det(C), both-z and rank-two legality")

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
    rebuilt = sp.expand(sum(checked_coefficients[power] * lam**power
                            for power in range(len(checked_coefficients))))
    require(zero(rebuilt - gamma36), "derived coefficient reconstruction")

    # Three-level predecessor seam: parameter, raw gate, and all five
    # S/u boundary-control faces.  No predecessor control table is read.
    x_current = R(313, 500) + v / 1000
    x_predecessor = R(78, 125) + vp / 500
    require(zero(x_current.subs(v, 0) - x_predecessor.subs(vp, 1)),
            "x=313/500 parameter seam")
    y_map = -R(1, 100) + u / 50
    H_current_seam = H.subs(shape).subs(
        {x: x_current.subs(v, 0), y: y_map})
    H_previous_seam = H.subs(shape).subs(
        {x: x_predecessor.subs(vp, 1), y: y_map})
    require(all(zero(entry) for entry in H_current_seam - H_previous_seam),
            "x=313/500 Hermitian parameter seam")
    gate_current_seam = gamma36.subs(
        {x: x_current.subs(v, 0), y: y_map})
    gate_previous_seam = gamma36.subs(
        {x: x_predecessor.subs(vp, 1), y: y_map})
    require(zero(gate_current_seam - gate_previous_seam),
            "x=313/500 raw-gate seam")

    certificates = tuple(bernstein_certificate(
        coefficient, S, x, y, v, u, current=True,
        bad_normalization=(attack == "bad-normalization"),
        drop_control=(attack == "drop-control" and power == lambda_degree),
    ) for power, coefficient in enumerate(coefficients))
    predecessor_certificates = tuple(bernstein_certificate(
        coefficient, S, x, y, vp, u, current=False,
    ) for coefficient in coefficients)
    seam_groups = []
    for power, (current, previous) in enumerate(
            zip(certificates, predecessor_certificates)):
        current_face = tuple(
            (i, k, value) for (i, j, k), value in current["bernstein"]
            if j == 0)
        previous_face = tuple(
            (i, k, value) for (i, j, k), value in previous["bernstein"]
            if j == previous["degrees"][1])
        if attack == "break-seam" and power == 4:
            current_face = current_face[:-1] + (
                (current_face[-1][0], current_face[-1][1],
                 current_face[-1][2] + 1),)
        require(current_face == previous_face,
                f"lambda^{power} boundary-control seam")
        seam_groups.append(current_face)
    require(tuple(len(group) for group in seam_groups) == (1, 3, 10, 21, 36),
            "five complete boundary-control seam groups")
    print("PASS x=313/500 parameter/raw-gate/five-control-group seam (71/71)")

    control_count = sum(len(certificate["bernstein"])
                        for certificate in certificates)
    coefficient_sha = hashlib.sha256(
        str(coefficients).encode("utf-8")).hexdigest()
    control_signature = tuple(
        (certificate["order"], certificate["degrees"],
         certificate["bernstein"])
        for certificate in certificates
    )
    control_sha = hashlib.sha256(
        str(control_signature).encode("utf-8")).hexdigest()
    seam_sha = hashlib.sha256(str(tuple(seam_groups)).encode("utf-8")).hexdigest()
    all_controls = tuple(
        (power, index, value)
        for power, certificate in enumerate(certificates)
        for index, value in certificate["bernstein"]
    )
    global_weakest = min(all_controls, key=lambda item: item[2])
    global_weakest_multiplicity = sum(
        value == global_weakest[2] for _, _, value in all_controls
    )
    require(global_weakest_multiplicity == 1,
            "unique global weakest exact control")
    for power, (coefficient, certificate) in enumerate(
            zip(coefficients, certificates)):
        print(f"BOX_COEFFICIENT_{power} {coefficient}")
        print(f"BOX_CERTIFICATE_{power} order={certificate['order']} "
              f"degrees={certificate['degrees']} "
              f"count={len(certificate['bernstein'])} "
              f"weakest=({certificate['weakest_index']},"
              f"{certificate['weakest_value']})")
    print(f"TOTAL_BOX_CONTROL_COUNT {control_count}")
    print(f"BOX_COEFFICIENTS_SHA256 {coefficient_sha}")
    print(f"BOX_CONTROLS_SHA256 {control_sha}")
    print(f"BOUNDARY_SEAM_SHA256 {seam_sha}")
    print(f"GLOBAL_WEAKEST_CONTROL {global_weakest}")
    print(f"GLOBAL_WEAKEST_MULTIPLICITY {global_weakest_multiplicity}")
    print("PASS all independently derived adjacent-box controls strictly positive")
    print("PASS 36*Gamma>0 throughout the claimed adjacent xy-cell")

    sample_s = (R(1, 1000000), R(1, 100), R(1))
    sample_x = (R(313, 500), R(1253, 2000), R(627, 1000))
    sample_y = (-R(1, 100), R(0), R(1, 100))
    sample_lambda = (R(1, 1000), R(1), R(1000))
    diagnostic_count = 0
    diagnostic_minimum = None
    diagnostic_data = None
    for sval in sample_s:
        for xval in sample_x:
            for yval in sample_y:
                for lval in sample_lambda:
                    value = sp.factor(gamma36.subs(
                        {S: sval, x: xval, y: yval, lam: lval}))
                    require(value > 0, "exact diagnostic gate value")
                    if diagnostic_minimum is None or value < diagnostic_minimum:
                        diagnostic_minimum = value
                        diagnostic_data = (sval, xval, yval, lval)
                    diagnostic_count += 1
    require(diagnostic_count == 81, "81 derived exact diagnostics")
    print(f"PASS {diagnostic_count} exact diagnostics only; "
          f"minimum={diagnostic_minimum} at {diagnostic_data}")
    print("SCOPE no numerical inference, no chart/maximality claim, "
          "no CE-046/048/059/060 reuse")
    return {
        "lambda_degree": lambda_degree,
        "coefficients": coefficients,
        "certificates": certificates,
        "control_count": control_count,
        "coefficient_sha": coefficient_sha,
        "control_sha": control_sha,
        "seam_sha": seam_sha,
        "seam_group_counts": tuple(len(group) for group in seam_groups),
        "global_weakest": global_weakest,
        "global_weakest_multiplicity": global_weakest_multiplicity,
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
        "none", "bad-normalization", "drop-q2", "flip-danger",
        "corrupt-coefficient", "drop-control", "break-seam",
    ), default="none")
    args = parser.parse_args()
    reconstruct(source_path=args.source_path,
                manifest_path=args.manifest_path,
                dependency_path=args.dependency_path,
                attack=args.attack)
    print("LITERAL_FREE_SCOUT PASS")


if __name__ == "__main__":
    main()
