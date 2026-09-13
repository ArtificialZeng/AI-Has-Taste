#!/usr/bin/env python3
"""Independent exact verifier for the two ternary SOS normal forms.

The verifier trusts only the small JSON schema and reconstructs both
permanents directly from their permutation definitions.  It does not import
the discovery evaluator or stored polynomial coefficients.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
CERT_PATH = HERE / "n3_sos_certificate.json"
EXPECTED_CERT_SHA256 = "b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0"
TOP_LEVEL_KEYS = frozenset({
    "schema_version", "theorem", "normal_forms", "permanent_convention",
    "block_convention", "coefficient",
})
NORMAL_FORM_KEYS = frozenset({
    "name", "row_projective_parameters", "entries", "claimed_gap",
})
EXPECTED_THEOREM = (
    "For every real 3 by 3 matrix T of rank at most 2, "
    "per([[T,T],[T,T]]) <= 20*per(T)^2."
)
EXPECTED_PERMANENT_CONVENTION = "sum over all permutations, with no signs"
EXPECTED_BLOCK_CONVENTION = (
    "B_ij = A_(i mod 3),(j mod 3) for 0-based indices"
)
EXPECTED_ENTRIES = "A_ij = c_j + a_i*d_j"
EXPECTED_FORMS = (
    {
        "name": "three_distinct_nonzero_row_lines",
        "row_projective_parameters": [-1, 0, 1],
        "entries": EXPECTED_ENTRIES,
        "claimed_gap": (
            "16*((d2*c3-c2*d3)^2*(d1^2+3*c1^2)+"
            "(d1*c3-c1*d3)^2*(d2^2+3*c2^2)+"
            "(d1*c2-c1*d2)^2*(d3^2+3*c3^2))"
        ),
    },
    {
        "name": "one_repeated_nonzero_row_line",
        "row_projective_parameters": [0, 0, 1],
        "entries": EXPECTED_ENTRIES,
        "claimed_gap": (
            "16*((d1*c2-c1*d2)^2*c3^2+"
            "(d1*c3-c1*d3)^2*c2^2+"
            "(d2*c3-c2*d3)^2*c1^2)"
        ),
    },
)


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _reject_nonfinite_constant(token):
    raise ValueError(f"non-JSON numeric constant: {token}")


def decode_certificate(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("certificate is not valid UTF-8") from exc
    return json.loads(
        text,
        object_pairs_hook=_reject_duplicate_keys,
        parse_constant=_reject_nonfinite_constant,
    )


def _require_exact_keys(value, expected, location):
    if type(value) is not dict:
        raise ValueError(f"{location} must be a JSON object")
    actual = frozenset(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValueError(
            f"{location} keys mismatch: missing={missing}, extra={extra}"
        )


def validate_certificate(cert):
    _require_exact_keys(cert, TOP_LEVEL_KEYS, "certificate")
    if type(cert["schema_version"]) is not int or cert["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    if type(cert["coefficient"]) is not int or cert["coefficient"] != 20:
        raise ValueError("coefficient must be integer 20")
    if type(cert["theorem"]) is not str or cert["theorem"] != EXPECTED_THEOREM:
        raise ValueError("theorem string does not match the verified endpoint")
    if (
        type(cert["permanent_convention"]) is not str
        or cert["permanent_convention"] != EXPECTED_PERMANENT_CONVENTION
    ):
        raise ValueError("unexpected permanent convention")
    if (
        type(cert["block_convention"]) is not str
        or cert["block_convention"] != EXPECTED_BLOCK_CONVENTION
    ):
        raise ValueError("unexpected block convention")

    forms = cert["normal_forms"]
    if type(forms) is not list or len(forms) != len(EXPECTED_FORMS):
        raise ValueError("normal_forms must be a two-element JSON array")
    for index, (form, expected) in enumerate(zip(forms, EXPECTED_FORMS)):
        location = f"normal_forms[{index}]"
        _require_exact_keys(form, NORMAL_FORM_KEYS, location)
        for key in ("name", "entries", "claimed_gap"):
            if type(form[key]) is not str or form[key] != expected[key]:
                raise ValueError(f"{location}.{key} has an unexpected value")
        rows = form["row_projective_parameters"]
        if type(rows) is not list or len(rows) != 3:
            raise ValueError(
                f"{location}.row_projective_parameters must be a length-3 array"
            )
        if any(type(value) is not int for value in rows):
            raise ValueError(
                f"{location}.row_projective_parameters must contain integers"
            )
        if rows != expected["row_projective_parameters"]:
            raise ValueError(
                f"{location}.row_projective_parameters has unexpected values"
            )
    return cert


def load_certificate(path):
    raw = path.read_bytes()
    actual_hash = hashlib.sha256(raw).hexdigest()
    if actual_hash != EXPECTED_CERT_SHA256:
        raise ValueError(
            "certificate sha256 mismatch: "
            f"expected {EXPECTED_CERT_SHA256}, got {actual_hash}"
        )
    return raw, validate_certificate(decode_certificate(raw))


def permanent_by_definition(matrix: list[list[sp.Expr]]) -> sp.Expr:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("permanent input is not square")
    return sp.expand(
        sum(
            sp.prod(matrix[i][sigma[i]] for i in range(n))
            for sigma in itertools.permutations(range(n))
        )
    )


def duplicated_block(matrix: list[list[sp.Expr]]) -> list[list[sp.Expr]]:
    n = len(matrix)
    return [[matrix[i % n][j % n] for j in range(2 * n)] for i in range(2 * n)]


def bracket(c: tuple[sp.Symbol, ...], d: tuple[sp.Symbol, ...], i: int, j: int) -> sp.Expr:
    return d[i] * c[j] - c[i] * d[j]


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit(f"usage: {pathlib.Path(sys.argv[0]).name} [CERTIFICATE.json]")
    cert_path = pathlib.Path(sys.argv[1]) if len(sys.argv) == 2 else CERT_PATH
    raw, cert = load_certificate(cert_path)
    forms = cert["normal_forms"]
    expected_rows = [form["row_projective_parameters"] for form in EXPECTED_FORMS]

    c = sp.symbols("c1:4")
    d = sp.symbols("d1:4")
    verified = []
    for index, a in enumerate(expected_rows):
        matrix = [[c[j] + a[i] * d[j] for j in range(3)] for i in range(3)]
        p3 = permanent_by_definition(matrix)
        p6 = permanent_by_definition(duplicated_block(matrix))
        gap = sp.expand(20 * p3**2 - p6)
        if index == 0:
            rhs = 16 * (
                bracket(c, d, 1, 2) ** 2 * (d[0] ** 2 + 3 * c[0] ** 2)
                + bracket(c, d, 0, 2) ** 2 * (d[1] ** 2 + 3 * c[1] ** 2)
                + bracket(c, d, 0, 1) ** 2 * (d[2] ** 2 + 3 * c[2] ** 2)
            )
        else:
            rhs = 16 * (
                bracket(c, d, 0, 1) ** 2 * c[2] ** 2
                + bracket(c, d, 0, 2) ** 2 * c[1] ** 2
                + bracket(c, d, 1, 2) ** 2 * c[0] ** 2
            )
        remainder = sp.Poly(sp.expand(gap - rhs), *c, *d, domain=sp.ZZ)
        if not remainder.is_zero:
            raise AssertionError(f"normal form {index} failed: {remainder.as_expr()}")
        verified.append({"form": forms[index]["name"], "gap_terms": len(gap.as_ordered_terms())})

    code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "exact symbolic integer coefficients",
        "forms": verified,
        "certificate_sha256": input_hash,
        "verifier_sha256": code_hash,
        "sympy": sp.__version__,
        "python": sys.version.split()[0]
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
