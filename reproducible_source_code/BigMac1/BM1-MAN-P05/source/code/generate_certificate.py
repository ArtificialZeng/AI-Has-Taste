#!/usr/bin/env python3
"""Generate the finite certificate accompanying the local-sieve theorem."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from lenhart_core import (
    bad_projective_slopes,
    direct_space_norm,
    edges,
    face_diagonals,
    factored_space_norm,
    parameters,
    valuation,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "certificates" / "local_sieve.json"


def main() -> None:
    primes = (23, 31, 67)
    local_data = []
    good_fraction = Fraction(1, 1)
    for p in primes:
        finite, infinity_bad = bad_projective_slopes(p)
        bad_count = len(finite) + int(infinity_bad)
        good_count = p + 1 - bad_count
        good_fraction *= Fraction(good_count, p + 1)
        local_data.append(
            {
                "prime": p,
                "bad_finite_slopes": finite,
                "infinity_bad": infinity_bad,
                "bad_count": bad_count,
                "projective_count": p + 1,
            }
        )

    progression_residues = []
    for residue in (3, 4, 7, 11):
        value = factored_space_norm(residue, 1) % 169
        progression_residues.append(
            {
                "r_mod_169": residue,
                "space_norm_mod_169": value,
                "quotient_mod_13": (value // 13) % 13,
                "edges_mod_13": [x % 13 for x in edges(residue, 1)],
            }
        )

    r, s = 3, 1
    sample = {
        "r": r,
        "s": s,
        "parameters": list(parameters(r, s)),
        "edges": list(edges(r, s)),
        "face_diagonals": list(face_diagonals(r, s)),
        "space_norm": direct_space_norm(r, s),
        "space_norm_factored": factored_space_norm(r, s),
        "valuation_at_13": valuation(direct_space_norm(r, s), 13),
    }

    certificate = {
        "schema_version": 1,
        "family": {
            "parameters": [
                "u=r^2-4rs-s^2",
                "v=-2(r^2+rs-s^2)",
                "w=r^2+s^2",
            ],
            "edges": [
                "abs((u^2-w^2)(v^2-w^2))",
                "abs(4uvw^2)",
                "abs(2uw(v^2-w^2))",
            ],
            "space_norm_factorization": "(u^2+4w^2)(u^6-10u^4w^2+25u^2w^4+4w^6)",
        },
        "exponent_one_classes_mod_169": progression_residues,
        "local_sieve": local_data,
        "crt_good_fraction": [good_fraction.numerator, good_fraction.denominator],
        "crt_excluded_fraction": [
            good_fraction.denominator - good_fraction.numerator,
            good_fraction.denominator,
        ],
        "sample": sample,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
