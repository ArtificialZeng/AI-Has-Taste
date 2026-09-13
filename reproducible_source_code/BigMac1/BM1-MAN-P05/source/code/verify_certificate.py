#!/usr/bin/env python3
"""Primary exact verifier for certificates/local_sieve.json."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from lenhart_core import (
    all_face_identities,
    bad_projective_slopes,
    direct_space_norm,
    edges,
    face_diagonals,
    factored_space_norm,
    parameters,
    valuation,
)


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "local_sieve.json"


def main() -> None:
    data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1

    product = Fraction(1, 1)
    for item in data["local_sieve"]:
        p = item["prime"]
        finite, infinity_bad = bad_projective_slopes(p)
        assert finite == item["bad_finite_slopes"]
        assert infinity_bad == item["infinity_bad"]
        bad_count = len(finite) + int(infinity_bad)
        assert bad_count == item["bad_count"]
        assert item["projective_count"] == p + 1
        product *= Fraction(p + 1 - bad_count, p + 1)

    assert [product.numerator, product.denominator] == data["crt_good_fraction"]
    excluded = 1 - product
    assert [excluded.numerator, excluded.denominator] == data["crt_excluded_fraction"]
    assert excluded == Fraction(95, 102)

    for item in data["exponent_one_classes_mod_169"]:
        residue = item["r_mod_169"]
        value = factored_space_norm(residue, 1) % 169
        assert value == item["space_norm_mod_169"]
        assert value % 13 == 0 and value % 169 != 0
        assert (value // 13) % 13 == item["quotient_mod_13"]
        assert [x % 13 for x in edges(residue, 1)] == item["edges_mod_13"]
        assert all(item["edges_mod_13"])
        # Polynomial congruence: three further representatives of the class.
        for k in (1, 2, 19):
            assert factored_space_norm(residue + 169 * k, 1) % 169 == value

    sample = data["sample"]
    r, s = sample["r"], sample["s"]
    assert list(parameters(r, s)) == sample["parameters"]
    assert list(edges(r, s)) == sample["edges"]
    assert list(face_diagonals(r, s)) == sample["face_diagonals"]
    assert direct_space_norm(r, s) == sample["space_norm"]
    assert factored_space_norm(r, s) == sample["space_norm_factored"]
    assert valuation(sample["space_norm"], 13) == sample["valuation_at_13"] == 1
    assert all_face_identities(r, s)

    # Boundary and generic exact checks for the algebraic identities.
    for r in range(-12, 13):
        for s in range(-12, 13):
            u, v, w = parameters(r, s)
            assert u * u + v * v == 5 * w * w
            assert direct_space_norm(r, s) == factored_space_norm(r, s)
            assert all_face_identities(r, s)

    print("primary verifier: PASS")


if __name__ == "__main__":
    main()
