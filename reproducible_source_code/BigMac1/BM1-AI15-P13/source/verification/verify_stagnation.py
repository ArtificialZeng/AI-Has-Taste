#!/usr/bin/env python3
"""Fail-closed exact verifier for the scalar binary64 SM-IR certificate.

The decisive computation uses only Python integers and ``Fraction``.  JSON is
accepted only when every object has exactly the documented keys, every value
has the exact JSON/Python type, no key is duplicated, and the input bytes match
an explicit SHA-256 trust anchor.  Host floating point is never used.
"""

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
    "28c6865ee1d22bf1def7565758fc3ddb254563be31ef69d3e1578a8180366eea"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")

TOP_KEYS = {
    "schema_version",
    "claim",
    "arithmetic",
    "dimension",
    "inputs",
    "exact_system",
    "expected_trace",
    "theorem_endpoint",
}
ARITHMETIC_KEYS = {
    "format",
    "radix",
    "precision_bits",
    "emin",
    "emax",
    "rounding",
    "unit_roundoff",
    "fused_operations",
}
UNIT_ROUNDOFF_KEYS = {"numerator", "exponent2"}
INPUT_KEYS = {"A_integer", "u_integer", "v_integer", "b_integer"}
EXACT_SYSTEM_KEYS = {"B_integer", "kappa2_A", "kappa2_B"}
EXPECTED_TRACE_KEYS = {
    "y_integer",
    "z_integer",
    "alpha_integer",
    "beta_exact_before_round_integer",
    "beta_rounded_integer",
    "theta_integer",
    "initial_x_integer",
    "residual_at_zero_integer",
    "correction_y_integer",
    "correction_alpha_integer",
    "correction_theta_integer",
    "next_x_integer",
    "normwise_relative_backward_error_at_zero",
    "componentwise_relative_backward_error_at_zero",
}

EXPECTED_CLAIM = (
    "Exact binary64 fixed-point counterexample to universal SM-IR eventual "
    "backward stability"
)
EXPECTED_ENDPOINT = (
    "All SM-IR iterates are exactly zero and have relative backward error "
    "one; both exact scalar condition numbers equal one."
)
EXPECTED_ARITHMETIC = {
    "format": "IEEE-754 binary64",
    "radix": 2,
    "precision_bits": 53,
    "emin": -1022,
    "emax": 1023,
    "rounding": "roundTiesToEven",
    "fused_operations": False,
}
EXPECTED_INPUTS = {
    "A_integer": 1,
    "u_integer": 1,
    "v_integer": 1 << 53,
    "b_integer": 1,
}


class CertificateError(Exception):
    """A deterministic rejection of an untrusted certificate."""


def reject_duplicate_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise CertificateError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def reject_nonstandard_constant(token: str) -> NoReturn:
    raise CertificateError(f"non-standard JSON numeric constant: {token}")


def require_exact_keys(obj: object, expected: set[str], location: str) -> dict[str, object]:
    if type(obj) is not dict:
        raise CertificateError(f"{location} must be a JSON object, got {type(obj).__name__}")
    actual = set(obj)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise CertificateError(
            f"{location} keys are not exact; missing={missing}, extra={extra}"
        )
    return obj


def require_type(value: object, expected_type: type, location: str) -> None:
    if type(value) is not expected_type:
        raise CertificateError(
            f"{location} must have exact type {expected_type.__name__}, "
            f"got {type(value).__name__}"
        )


def require_integer_fields(obj: dict[str, object], keys: set[str], location: str) -> None:
    for key in keys:
        require_type(obj[key], int, f"{location}.{key}")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_certificate(
    path: Path, expected_sha256: str
) -> tuple[dict[str, object], str]:
    if not SHA256_RE.fullmatch(expected_sha256):
        raise CertificateError("expected certificate SHA-256 must be 64 lowercase hex digits")
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    actual_sha256 = sha256_bytes(raw)
    if actual_sha256 != expected_sha256:
        raise CertificateError(
            f"certificate SHA-256 mismatch: actual={actual_sha256}, "
            f"expected={expected_sha256}"
        )
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise CertificateError(f"certificate is not strict UTF-8: {exc}") from exc
    try:
        data = json.loads(
            text,
            object_pairs_hook=reject_duplicate_object,
            parse_constant=reject_nonstandard_constant,
        )
    except (json.JSONDecodeError, CertificateError) as exc:
        raise CertificateError(f"invalid certificate JSON: {exc}") from exc
    return require_exact_keys(data, TOP_KEYS, "top"), actual_sha256


def validate_schema(data: dict[str, object]) -> tuple[
    dict[str, object], dict[str, object], dict[str, object], dict[str, object]
]:
    require_type(data["schema_version"], int, "top.schema_version")
    require_type(data["claim"], str, "top.claim")
    require_type(data["dimension"], int, "top.dimension")
    require_type(data["theorem_endpoint"], str, "top.theorem_endpoint")
    if data["schema_version"] != 1:
        raise CertificateError("unsupported schema_version")
    if data["claim"] != EXPECTED_CLAIM:
        raise CertificateError("unexpected claim string")
    if data["dimension"] != 1:
        raise CertificateError("certificate is not the scalar case")
    if data["theorem_endpoint"] != EXPECTED_ENDPOINT:
        raise CertificateError("unexpected theorem endpoint")

    ar = require_exact_keys(data["arithmetic"], ARITHMETIC_KEYS, "arithmetic")
    require_type(ar["format"], str, "arithmetic.format")
    require_type(ar["radix"], int, "arithmetic.radix")
    require_type(ar["precision_bits"], int, "arithmetic.precision_bits")
    require_type(ar["emin"], int, "arithmetic.emin")
    require_type(ar["emax"], int, "arithmetic.emax")
    require_type(ar["rounding"], str, "arithmetic.rounding")
    require_type(ar["fused_operations"], bool, "arithmetic.fused_operations")
    for key, expected in EXPECTED_ARITHMETIC.items():
        if ar[key] != expected:
            raise CertificateError(f"unsupported arithmetic declaration at {key}")
    unit = require_exact_keys(
        ar["unit_roundoff"], UNIT_ROUNDOFF_KEYS, "arithmetic.unit_roundoff"
    )
    require_integer_fields(unit, UNIT_ROUNDOFF_KEYS, "arithmetic.unit_roundoff")
    if unit != {"numerator": 1, "exponent2": -53}:
        raise CertificateError("wrong unit-roundoff declaration")

    values = require_exact_keys(data["inputs"], INPUT_KEYS, "inputs")
    require_integer_fields(values, INPUT_KEYS, "inputs")
    if values != EXPECTED_INPUTS:
        raise CertificateError("certificate inputs differ from the audited instance")

    exact = require_exact_keys(
        data["exact_system"], EXACT_SYSTEM_KEYS, "exact_system"
    )
    require_integer_fields(exact, EXACT_SYSTEM_KEYS, "exact_system")

    expected = require_exact_keys(
        data["expected_trace"], EXPECTED_TRACE_KEYS, "expected_trace"
    )
    require_integer_fields(expected, EXPECTED_TRACE_KEYS, "expected_trace")
    return ar, values, exact, expected


def pow2(e: int) -> Fraction:
    return Fraction(1 << e, 1) if e >= 0 else Fraction(1, 1 << (-e))


def floor_log2(x: Fraction) -> int:
    if x <= 0:
        raise ValueError("floor_log2 requires a positive rational")
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < pow2(e):
        e -= 1
    elif x >= pow2(e + 1):
        e += 1
    assert pow2(e) <= x < pow2(e + 1)
    return e


def round_integer_ties_even(x: Fraction) -> int:
    if x < 0:
        return -round_integer_ties_even(-x)
    q, r = divmod(x.numerator, x.denominator)
    twice = 2 * r
    if twice < x.denominator:
        return q
    if twice > x.denominator:
        return q + 1
    return q if q % 2 == 0 else q + 1


def rn_binary(x: Fraction, precision: int, emin: int, emax: int) -> Fraction:
    """Correct rounding to a finite IEEE binary format, ties to even."""
    if x == 0:
        return Fraction(0)
    sign = -1 if x < 0 else 1
    ax = abs(x)
    e = floor_log2(ax)
    quantum = pow2(emin - (precision - 1)) if e < emin else pow2(e - (precision - 1))
    result = quantum * round_integer_ties_even(ax / quantum)
    if result != 0 and floor_log2(result) > emax:
        raise OverflowError("unexpected overflow in certificate trace")
    return sign * result


def verify(cert_path: Path, expected_sha256: str) -> None:
    data, verified_certificate_sha256 = parse_certificate(cert_path, expected_sha256)
    ar, values, exact, expected = validate_schema(data)
    p = ar["precision_bits"]
    emin = ar["emin"]
    emax = ar["emax"]
    assert type(p) is int and type(emin) is int and type(emax) is int

    A = Fraction(values["A_integer"])
    u = Fraction(values["u_integer"])
    v = Fraction(values["v_integer"])
    b = Fraction(values["b_integer"])
    if A == 0:
        raise CertificateError("A is singular")
    for name, value in (("A", A), ("u", u), ("v", v), ("b", b)):
        if rn_binary(value, p, emin, emax) != value:
            raise CertificateError(f"input {name} is not exactly representable")

    B = A + u * v
    if B == 0:
        raise CertificateError("B is singular")
    if B != exact["B_integer"]:
        raise CertificateError("serialized exact B is wrong")
    kappa_A = abs(A) * abs(1 / A)
    kappa_B = abs(B) * abs(1 / B)
    if (kappa_A, kappa_B) != (1, 1):
        raise CertificateError("condition number check failed")
    if (kappa_A, kappa_B) != (exact["kappa2_A"], exact["kappa2_B"]):
        raise CertificateError("serialized condition numbers are wrong")
    unit = ar["unit_roundoff"]
    assert type(unit) is dict
    eps = Fraction(unit["numerator"]) * pow2(unit["exponent2"])
    if eps != Fraction(1, 1 << 53) or not (max(kappa_A, kappa_B) * eps < 1):
        raise CertificateError("unit-roundoff safety check failed")

    def fl(x: Fraction) -> Fraction:
        return rn_binary(x, p, emin, emax)

    # Algorithm 1 / source Section 4 operation graph.
    y = fl(b / A)
    z = fl(u / A)
    alpha = fl(v * y)
    vz = fl(v * z)
    beta_exact_before_round = Fraction(1) + vz
    beta = fl(beta_exact_before_round)
    if beta == 0:
        raise CertificateError("unexpected computed zero beta")
    theta = fl(alpha / beta)
    initial_x = fl(y - fl(theta * z))

    first_trace = {
        "y_integer": y,
        "z_integer": z,
        "alpha_integer": alpha,
        "beta_exact_before_round_integer": beta_exact_before_round,
        "beta_rounded_integer": beta,
        "theta_integer": theta,
        "initial_x_integer": initial_x,
    }
    for key, actual in first_trace.items():
        if actual != expected[key]:
            raise CertificateError(
                f"trace mismatch at {key}: {actual} != {expected[key]}"
            )

    lower = Fraction(1 << 53)
    upper = lower + 2
    if beta_exact_before_round - lower != upper - beta_exact_before_round:
        raise CertificateError("decisive beta value is not an exact midpoint")
    lower_significand = 1 << 52
    upper_significand = lower_significand + 1
    if lower_significand % 2 != 0 or upper_significand % 2 != 1 or beta != lower:
        raise CertificateError("ties-to-even midpoint certificate failed")

    def residual(x: Fraction) -> Fraction:
        # Source residual proof: p=fl(b-fl(A*x)), q=fl(fl(v*x)*u), r=fl(p-q).
        return fl(fl(b - fl(A * x)) - fl(fl(v * x) * u))

    def refine(x: Fraction) -> tuple[Fraction, dict[str, Fraction]]:
        r = residual(x)
        yr = fl(r / A)
        alpha_r = fl(v * yr)
        theta_r = fl(alpha_r / beta)
        # Literal Algorithm 2 Step 5 left association: (x+y_r)-theta_r*z.
        next_x = fl(fl(x + yr) - fl(theta_r * z))
        return next_x, {"r": r, "yr": yr, "alpha_r": alpha_r, "theta_r": theta_r}

    next_x, correction = refine(initial_x)
    correction_expected = {
        "r": expected["residual_at_zero_integer"],
        "yr": expected["correction_y_integer"],
        "alpha_r": expected["correction_alpha_integer"],
        "theta_r": expected["correction_theta_integer"],
    }
    if correction != correction_expected or next_x != expected["next_x_integer"]:
        raise CertificateError("correction/fixed-point trace mismatch")

    # The other natural Step 5 association is separately certified.
    right_associated = fl(initial_x + fl(correction["yr"] - fl(correction["theta_r"] * z)))
    if right_associated != next_x or right_associated != 0:
        raise CertificateError("Step 5 association robustness check failed")

    x = initial_x
    for _ in range(32):
        x, _ = refine(x)
        if x != 0:
            raise CertificateError("zero failed to remain an exact fixed point")

    r0 = b - B * Fraction(0)
    eta_norm = abs(r0) / (abs(B) * abs(Fraction(0)) + abs(b))
    eta_componentwise = eta_norm
    if eta_norm != 1 or eta_componentwise != 1:
        raise CertificateError("exact backward-error calculation failed")
    if eta_norm != expected["normwise_relative_backward_error_at_zero"]:
        raise CertificateError("serialized normwise backward error is wrong")
    if eta_componentwise != expected["componentwise_relative_backward_error_at_zero"]:
        raise CertificateError("serialized componentwise backward error is wrong")
    if b == 0:
        raise CertificateError("matrix-only backward-error obstruction disappeared")

    here = Path(__file__).resolve()
    print("CERTIFIED: exact binary64 SM-IR stagnation counterexample")
    print(
        f"condition_numbers={kappa_A},{kappa_B}; "
        f"beta_exact={beta_exact_before_round}; beta_fl={beta}"
    )
    print(
        f"all_iterates=0; normwise_backward_error={eta_norm}; "
        "checked_iterations=32"
    )
    print(f"certificate_sha256={verified_certificate_sha256}")
    print(f"verifier_sha256={sha256(here)}")


def main() -> int:
    here = Path(__file__).resolve()
    default = here.parent.parent / "certificates" / "binary64_stagnation.json"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=default)
    parser.add_argument(
        "--expect-certificate-sha256",
        default=OFFICIAL_CERTIFICATE_SHA256,
        help="explicit lowercase SHA-256 trust anchor (default: audited certificate hash)",
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
