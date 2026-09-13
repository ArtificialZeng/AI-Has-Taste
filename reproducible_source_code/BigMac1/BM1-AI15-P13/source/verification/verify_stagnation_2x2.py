#!/usr/bin/env python3
"""Fail-closed exact verifier for the 2x2 binary64 SM-IR certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


OFFICIAL_CERTIFICATE_SHA256 = (
    "662374272407d01b56fd18c86153d7fdfc69508a1cbbab0a51026524948c6e9a"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
TOP_KEYS = {
    "schema_version", "claim", "arithmetic", "parameters", "inputs",
    "exact_system", "expected_trace",
}
ARITHMETIC_KEYS = {
    "format", "precision_bits", "rounding", "unit_roundoff_exponent2",
}
PARAMETER_KEYS = {"p", "m"}
INPUT_KEYS = {
    "A_diagonal_integers", "u_integers", "v_integers", "b_integers",
}
EXACT_KEYS = {
    "B_diagonal_integers", "kappa2_A", "kappa2_B",
    "epsilon_times_kappa_A", "epsilon_times_kappa_B",
}
TRACE_KEYS = {
    "y", "z", "alpha", "beta_exact_before_round", "beta_rounded", "theta",
    "initial_x", "residual_at_zero", "next_x", "normwise_relative_backward_error",
}
RATIONAL_KEYS = {"numerator", "denominator"}


class CertificateError(Exception):
    pass


def reject_duplicate_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise CertificateError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def reject_nonstandard_constant(token: str) -> NoReturn:
    raise CertificateError(f"non-standard JSON numeric constant: {token}")


def exact_object(obj: object, keys: set[str], where: str) -> dict[str, object]:
    if type(obj) is not dict:
        raise CertificateError(f"{where} must be a JSON object")
    actual = set(obj)
    if actual != keys:
        raise CertificateError(
            f"{where} keys are not exact; missing={sorted(keys-actual)}, "
            f"extra={sorted(actual-keys)}"
        )
    return obj


def exact_int(value: object, where: str) -> int:
    if type(value) is not int:
        raise CertificateError(f"{where} must have exact type int")
    return value


def exact_str(value: object, where: str) -> str:
    if type(value) is not str:
        raise CertificateError(f"{where} must have exact type str")
    return value


def exact_int_vector(value: object, where: str) -> list[int]:
    if type(value) is not list or len(value) != 2:
        raise CertificateError(f"{where} must be a length-2 JSON array")
    return [exact_int(item, f"{where}[{i}]") for i, item in enumerate(value)]


def fraction_field(obj: object, where: str) -> Fraction:
    field = exact_object(obj, RATIONAL_KEYS, where)
    numerator = exact_int(field["numerator"], f"{where}.numerator")
    denominator = exact_int(field["denominator"], f"{where}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{where}.denominator must be positive")
    return Fraction(numerator, denominator)


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def parse_certificate(path: Path, expected_hash: str) -> tuple[dict[str, object], str]:
    if not SHA256_RE.fullmatch(expected_hash):
        raise CertificateError("expected SHA-256 must be 64 lowercase hex digits")
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    actual_hash = sha256_bytes(raw)
    if actual_hash != expected_hash:
        raise CertificateError(
            f"certificate SHA-256 mismatch: actual={actual_hash}, expected={expected_hash}"
        )
    try:
        text = raw.decode("utf-8", errors="strict")
        data = json.loads(
            text,
            object_pairs_hook=reject_duplicate_object,
            parse_constant=reject_nonstandard_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, CertificateError) as exc:
        raise CertificateError(f"invalid certificate JSON: {exc}") from exc
    return exact_object(data, TOP_KEYS, "top"), actual_hash


def verify(cert_path: Path, expected_hash: str) -> None:
    data, verified_certificate_hash = parse_certificate(cert_path, expected_hash)
    if exact_int(data["schema_version"], "schema_version") != 1:
        raise CertificateError("unsupported schema version")
    claim = exact_str(data["claim"], "claim")
    if claim != (
        "Exact 2x2 binary64 SM-IR stagnation with both condition numbers of "
        "square-root unit-roundoff scale"
    ):
        raise CertificateError("unexpected claim string")

    ar = exact_object(data["arithmetic"], ARITHMETIC_KEYS, "arithmetic")
    if (
        exact_str(ar["format"], "arithmetic.format"),
        exact_int(ar["precision_bits"], "arithmetic.precision_bits"),
        exact_str(ar["rounding"], "arithmetic.rounding"),
        exact_int(ar["unit_roundoff_exponent2"], "arithmetic.unit_roundoff_exponent2"),
    ) != ("IEEE-754 binary64", 53, "roundTiesToEven", -53):
        raise CertificateError("wrong arithmetic declaration")

    par = exact_object(data["parameters"], PARAMETER_KEYS, "parameters")
    p = exact_int(par["p"], "parameters.p")
    m = exact_int(par["m"], "parameters.m")
    if p != 53 or m != p // 2:
        raise CertificateError("wrong family parameters")

    inp = exact_object(data["inputs"], INPUT_KEYS, "inputs")
    A = exact_int_vector(inp["A_diagonal_integers"], "inputs.A_diagonal_integers")
    u = exact_int_vector(inp["u_integers"], "inputs.u_integers")
    v = exact_int_vector(inp["v_integers"], "inputs.v_integers")
    b = exact_int_vector(inp["b_integers"], "inputs.b_integers")
    if A != [1, 1 << m] or u != [1, 0] or v != [1 << p, 0] or b != [1, 0]:
        raise CertificateError("inputs differ from the audited 2x2 instance")

    exact = exact_object(data["exact_system"], EXACT_KEYS, "exact_system")
    B_serialized = exact_int_vector(
        exact["B_diagonal_integers"], "exact_system.B_diagonal_integers"
    )
    B = [A[0] + u[0] * v[0], A[1] + u[1] * v[1]]
    if B != B_serialized or 0 in A or 0 in B:
        raise CertificateError("exact feasibility check failed")
    kappa_A = Fraction(max(A), min(A))
    kappa_B = Fraction(max(B), min(B))
    eps = Fraction(1, 1 << p)
    if kappa_A != fraction_field(exact["kappa2_A"], "exact_system.kappa2_A"):
        raise CertificateError("kappa2(A) mismatch")
    if kappa_B != fraction_field(exact["kappa2_B"], "exact_system.kappa2_B"):
        raise CertificateError("kappa2(B) mismatch")
    if eps * kappa_A != fraction_field(
        exact["epsilon_times_kappa_A"], "exact_system.epsilon_times_kappa_A"
    ):
        raise CertificateError("epsilon*kappa2(A) mismatch")
    if eps * kappa_B != fraction_field(
        exact["epsilon_times_kappa_B"], "exact_system.epsilon_times_kappa_B"
    ):
        raise CertificateError("epsilon*kappa2(B) mismatch")
    if not (
        eps * kappa_A < Fraction(1, 1 << 26)
        and eps * kappa_B < Fraction(1, 1 << 25)
    ):
        raise CertificateError("condition numbers are not safely below epsilon^-1")

    expected = exact_object(data["expected_trace"], TRACE_KEYS, "expected_trace")
    for key in ("y", "z", "initial_x", "residual_at_zero", "next_x"):
        exact_int_vector(expected[key], f"expected_trace.{key}")
    for key in TRACE_KEYS - {"y", "z", "initial_x", "residual_at_zero", "next_x"}:
        exact_int(expected[key], f"expected_trace.{key}")

    y = [Fraction(1), Fraction(0)]
    z = [Fraction(1), Fraction(0)]
    alpha = Fraction(1 << p)
    beta_exact = Fraction((1 << p) + 1)
    lower, upper = Fraction(1 << p), Fraction((1 << p) + 2)
    if beta_exact - lower != upper - beta_exact:
        raise CertificateError("beta is not the exact midpoint")
    if (1 << (p - 1)) % 2 != 0 or ((1 << (p - 1)) + 1) % 2 != 1:
        raise CertificateError("tie parity check failed")
    beta = lower
    theta = alpha / beta
    x = [y[i] - theta * z[i] for i in range(2)]
    if [int(t) for t in y] != expected["y"] or [int(t) for t in z] != expected["z"]:
        raise CertificateError("solve trace mismatch")
    if (alpha, beta_exact, beta, theta) != (
        expected["alpha"], expected["beta_exact_before_round"],
        expected["beta_rounded"], expected["theta"],
    ) or x != list(map(Fraction, expected["initial_x"])):
        raise CertificateError("initial SM trace mismatch")

    residual = [Fraction(b[i]) - Fraction(B[i]) * x[i] for i in range(2)]
    yr = [residual[0] / A[0], residual[1] / A[1]]
    alpha_r = Fraction(v[0]) * yr[0] + Fraction(v[1]) * yr[1]
    theta_r = alpha_r / beta
    next_x = [x[i] + yr[i] - theta_r * z[i] for i in range(2)]
    if residual != list(map(Fraction, expected["residual_at_zero"])) or next_x != x:
        raise CertificateError("fixed-point check failed")
    if next_x != list(map(Fraction, expected["next_x"])):
        raise CertificateError("serialized next iterate mismatch")
    eta = Fraction(1)
    if eta != expected["normwise_relative_backward_error"]:
        raise CertificateError("backward error mismatch")

    code_path = Path(__file__).resolve()
    print("CERTIFIED: exact 2x2 binary64 SM-IR stagnation")
    print(
        f"kappa_A={kappa_A}; kappa_B={kappa_B}; "
        f"eps*kappa_A={eps*kappa_A}; eps*kappa_B={eps*kappa_B}"
    )
    print("all_iterates=(0,0); normwise_backward_error=1")
    print(f"certificate_sha256={verified_certificate_hash}")
    print(f"verifier_sha256={sha256_bytes(code_path.read_bytes())}")


def main() -> int:
    code_path = Path(__file__).resolve()
    default = code_path.parent.parent / "certificates" / "binary64_stagnation_2x2.json"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=default)
    parser.add_argument(
        "--expect-certificate-sha256", default=OFFICIAL_CERTIFICATE_SHA256
    )
    args = parser.parse_args()
    try:
        verify(args.certificate.resolve(), args.expect_certificate_sha256)
    except (CertificateError, ArithmeticError, AssertionError, ValueError) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
