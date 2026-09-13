#!/usr/bin/env python3
"""Independent exact certificate for R_15(4,4) = R_16(4,4).

Unlike ``triage_enumeration.py``, this program never enumerates tuples of
summands.  It represents a four-term multiset from a four-element alphabet by
its vector of four nonnegative multiplicities, whose coordinates sum to four.
It also enumerates the alphabets with explicit increasing loops rather than an
iterator from ``itertools``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


Alphabet = tuple[int, int, int, int]
Vector = tuple[int, int, int, int]


def coefficient_vectors() -> tuple[Vector, ...]:
    vectors: list[Vector] = []
    for c0 in range(5):
        for c1 in range(5 - c0):
            for c2 in range(5 - c0 - c1):
                c3 = 4 - c0 - c1 - c2
                vectors.append((c0, c1, c2, c3))
    result = tuple(vectors)
    assert len(result) == math.comb(4 + 4 - 1, 4 - 1) == 35
    assert len(set(result)) == len(result)
    assert all(min(vector) >= 0 and sum(vector) == 4 for vector in result)
    return result


def alphabets(diameter: int):
    """Yield every increasing four-tuple in [0, diameter], exactly once."""
    for a in range(diameter - 2):
        for b in range(a + 1, diameter - 1):
            for c in range(b + 1, diameter):
                for d in range(c + 1, diameter + 1):
                    yield (a, b, c, d)


def label(alphabet: Alphabet, vectors: tuple[Vector, ...]) -> int:
    sums = {
        c0 * a + c1 * b + c2 * c + c3 * d
        for c0, c1, c2, c3 in vectors
        for a, b, c, d in (alphabet,)
    }
    return len(sums)


def diameter_data(diameter: int, vectors: tuple[Vector, ...]) -> dict[str, object]:
    frequencies: dict[int, int] = {}
    first_witnesses: dict[int, Alphabet] = {}
    alphabet_count = 0

    for alphabet in alphabets(diameter):
        alphabet_count += 1
        value = label(alphabet, vectors)
        frequencies[value] = frequencies.get(value, 0) + 1
        first_witnesses.setdefault(value, alphabet)

    expected_count = math.comb(diameter + 1, 4)
    assert alphabet_count == expected_count
    assert sum(frequencies.values()) == alphabet_count
    assert set(frequencies) == set(first_witnesses)

    witness_checks: dict[str, dict[str, object]] = {}
    for value, witness in sorted(first_witnesses.items()):
        assert 0 <= witness[0] < witness[1] < witness[2] < witness[3] <= diameter
        recomputed = label(witness, vectors)
        assert recomputed == value
        witness_checks[str(value)] = {
            "witness": list(witness),
            "recomputed_label": recomputed,
            "valid_alphabet": True,
        }

    return {
        "diameter": diameter,
        "expected_alphabet_count": expected_count,
        "enumerated_alphabet_count": alphabet_count,
        "coverage_check": alphabet_count == expected_count,
        "labels": sorted(frequencies),
        "label_frequencies": {
            str(value): frequency for value, frequency in sorted(frequencies.items())
        },
        "witness_checks": witness_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    vectors = coefficient_vectors()
    by_diameter = {
        str(diameter): diameter_data(diameter, vectors) for diameter in (15, 16)
    }
    labels_15 = set(by_diameter["15"]["labels"])
    labels_16 = set(by_diameter["16"]["labels"])

    script_digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = {
        "arithmetic": "exact Python integers",
        "method": (
            "For each explicitly enumerated increasing alphabet (a,b,c,d) in "
            "[0,D], form all dot products c0*a+c1*b+c2*c+c3*d over the 35 "
            "nonnegative coefficient vectors with c0+c1+c2+c3=4."
        ),
        "implementation_sha256": script_digest,
        "coefficient_vector_count": len(vectors),
        "coefficient_vectors": [list(vector) for vector in vectors],
        "by_diameter": by_diameter,
        "labels_in_16_not_15": sorted(labels_16 - labels_15),
        "labels_in_15_not_16": sorted(labels_15 - labels_16),
        "equal_label_sets": labels_15 == labels_16,
        "all_coverage_checks": all(
            bool(by_diameter[str(diameter)]["coverage_check"])
            for diameter in (15, 16)
        ),
        "all_witness_checks": all(
            all(
                item["valid_alphabet"]
                and item["recomputed_label"] == int(value)
                for value, item in by_diameter[str(diameter)][
                    "witness_checks"
                ].items()
            )
            for diameter in (15, 16)
        ),
    }
    assert payload["equal_label_sets"]
    assert payload["all_coverage_checks"]
    assert payload["all_witness_checks"]
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
