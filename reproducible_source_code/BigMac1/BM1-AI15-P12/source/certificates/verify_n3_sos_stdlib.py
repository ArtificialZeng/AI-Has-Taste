#!/usr/bin/env python3
"""Pure-standard-library verifier for the serialized n=3 SOS certificate.

Polynomials are sparse dictionaries from six-variable exponent tuples to
integer coefficients.  The two permanents are reconstructed from all
permutations.  No CAS and no discovery-code import is used.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import pathlib
import sys


HERE = pathlib.Path(__file__).resolve().parent
CERT_PATH = HERE / "n3_sos_certificate.json"
EXPECTED_CERT_SHA256 = "b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0"
NVARS = 6  # c1,c2,c3,d1,d2,d3
ZERO_MONOMIAL = (0,) * NVARS

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
    """Decode strict JSON; duplicate keys and NaN/Infinity are invalid."""
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
    """Validate the complete schema, value types, and theorem-bound constants."""
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
    """Hash-bind and strictly validate a serialized certificate."""
    raw = path.read_bytes()
    actual_hash = hashlib.sha256(raw).hexdigest()
    if actual_hash != EXPECTED_CERT_SHA256:
        raise ValueError(
            "certificate sha256 mismatch: "
            f"expected {EXPECTED_CERT_SHA256}, got {actual_hash}"
        )
    return raw, validate_certificate(decode_certificate(raw))


def clean(poly):
    return {m: int(v) for m, v in poly.items() if v}


def constant(value):
    return {} if value == 0 else {ZERO_MONOMIAL: int(value)}


def variable(index):
    exponent = [0] * NVARS
    exponent[index] = 1
    return {tuple(exponent): 1}


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result)


def scale(poly, scalar):
    return clean({m: scalar * v for m, v in poly.items()})


def subtract(left, right):
    return add(left, scale(right, -1))


def multiply(left, right):
    result = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            result[monomial] = result.get(monomial, 0) + lv * rv
    return clean(result)


def square(poly):
    return multiply(poly, poly)


def product(polys):
    result = constant(1)
    for poly in polys:
        result = multiply(result, poly)
    return result


def permanent_by_definition(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("non-square permanent input")
    return add(*(
        product(matrix[i][sigma[i]] for i in range(n))
        for sigma in itertools.permutations(range(n))
    ))


def duplicated_block(matrix):
    n = len(matrix)
    return [[matrix[i % n][j % n] for j in range(2 * n)] for i in range(2 * n)]


def bracket(c, d, i, j):
    return subtract(multiply(d[i], c[j]), multiply(c[i], d[j]))


def verify_form(a, form_index):
    c = tuple(variable(i) for i in range(3))
    d = tuple(variable(i + 3) for i in range(3))
    matrix = [[add(c[j], scale(d[j], a[i])) for j in range(3)] for i in range(3)]
    p3 = permanent_by_definition(matrix)
    p6 = permanent_by_definition(duplicated_block(matrix))
    gap = subtract(scale(square(p3), 20), p6)
    if form_index == 0:
        rhs = scale(add(
            multiply(square(bracket(c, d, 1, 2)), add(square(d[0]), scale(square(c[0]), 3))),
            multiply(square(bracket(c, d, 0, 2)), add(square(d[1]), scale(square(c[1]), 3))),
            multiply(square(bracket(c, d, 0, 1)), add(square(d[2]), scale(square(c[2]), 3))),
        ), 16)
    elif form_index == 1:
        rhs = scale(add(
            multiply(square(bracket(c, d, 0, 1)), square(c[2])),
            multiply(square(bracket(c, d, 0, 2)), square(c[1])),
            multiply(square(bracket(c, d, 1, 2)), square(c[0])),
        ), 16)
    else:
        raise ValueError("unknown form index")
    remainder = subtract(gap, rhs)
    if remainder:
        first = next(iter(sorted(remainder.items())))
        raise AssertionError(f"nonzero remainder in form {form_index}: {first}")
    return {"form_index": form_index, "gap_monomials": len(gap), "remainder_monomials": 0}


def main():
    if len(sys.argv) > 2:
        raise SystemExit(f"usage: {pathlib.Path(sys.argv[0]).name} [CERTIFICATE.json]")
    cert_path = pathlib.Path(sys.argv[1]) if len(sys.argv) == 2 else CERT_PATH
    raw, cert = load_certificate(cert_path)
    expected_rows = [form["row_projective_parameters"] for form in EXPECTED_FORMS]
    results = [verify_form(rows, i) for i, rows in enumerate(expected_rows)]
    print(json.dumps({
        "status": "PASS",
        "arithmetic": "pure Python sparse integer polynomials",
        "forms": results,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
