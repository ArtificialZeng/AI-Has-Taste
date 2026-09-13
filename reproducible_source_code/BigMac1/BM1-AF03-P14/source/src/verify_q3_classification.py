#!/usr/bin/env python3
"""Fail-closed exact verifier for the positive Q3 critical classification."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


EXPECTED = {
    "schema": "q3-positive-critical-classification-v1",
    "normalization": "ordered balanced positive coordinates (a,b,1)",
    "box_spline_numerator": "T^2-sum_i(T-a_i)^2",
    "cleared_derivative": "H_q=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
    "positive_saturation": ["a", "b"],
    "resultant_variable": "a",
    "primitive_resultant": "-64*b^2*(b-1)^6*(b^2+b+1)^3",
    "surviving_positive_branch": "b=1, a=1",
    "claim": "the balanced positive Q3 critical orbit is diagonal",
}


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        raise ValueError(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


def verify(path: Path) -> None:
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys
        )
    except Exception as exc:
        raise ValueError(f"unreadable certificate: {exc}") from exc
    reject_booleans(data)
    if data != EXPECTED:
        raise ValueError("schema or semantic claim mismatch")

    a, b = sp.symbols("a b")
    coordinates = (a, b, sp.Integer(1))
    T = sum(coordinates) / 2
    S = sum(q * q for q in coordinates)
    D = a * b
    P = sp.expand(T**2 - sum((T - q) ** 2 for q in coordinates))
    H = [
        sp.expand(
            sp.diff(S, q) * P * D
            + 2 * S * sp.diff(P, q) * D
            - 2 * S * P * sp.diff(D, q)
        )
        for q in (a, b)
    ]
    # Positive coordinates justify only these two divisions.
    h_a = sp.cancel(H[0] / b)
    h_b = sp.cancel(H[1] / a)
    if sp.denom(h_a) != 1 or sp.denom(h_b) != 1:
        raise ValueError("positive saturation did not produce polynomials")

    resultant = sp.factor(sp.resultant(h_a, h_b, a))
    wanted = -64 * b**2 * (b - 1) ** 6 * (b**2 + b + 1) ** 3
    if sp.expand(resultant - wanted) != 0:
        raise ValueError("reconstructed resultant mismatch")
    # For real b>0, the only vanishing factor is b-1, since
    # b^2+b+1=(b+1/2)^2+3/4>0.
    if sp.expand(b**2 + b + 1 - ((b + sp.Rational(1, 2)) ** 2 + sp.Rational(3, 4))) != 0:
        raise ValueError("positivity identity failed")
    at_b_one = (sp.factor(h_a.subs(b, 1)), sp.factor(h_b.subs(b, 1)))
    if at_b_one != (-2 * a**2 * (a - 1) ** 2, a**2 * (a - 1) ** 2):
        raise ValueError("surviving branch mismatch")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_q3_classification.py CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        verify(Path(sys.argv[1]))
    except Exception as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        return 1
    print("PASS: the balanced positive Q3 critical orbit is diagonal")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
