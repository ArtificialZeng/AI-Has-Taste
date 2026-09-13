#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent metadata and block-coverage checks for the h^4 certificate.

This does not repeat the 1.48-billion-signature C++ sweep.  It regenerates the
words independently, checks both word digests and all completed-sweep counts,
and verifies the four cyclic-difference representatives used in the global
short-factor bound.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


BASE = tuple(map(int, "01213101314310"))
ROOT = Path(__file__).resolve().parent


def morph(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % 5 for a in word for b in BASE)


def iterate(power: int, seed: int = 0) -> tuple[int, ...]:
    word = (seed,)
    for _ in range(power):
        word = morph(word)
    return word


def digest(word: tuple[int, ...]) -> str:
    return hashlib.sha256(bytes(word)).hexdigest()


def main() -> None:
    certificate = json.loads((ROOT / "h4_collinearity.json").read_text())
    h3 = iterate(3)
    h4 = iterate(4)

    assert len(h3) == 2_744
    assert len(h4) == 38_416
    assert digest(h3) == certificate["h3_crosscheck"]["prefix_sha256"]
    assert digest(h4) == certificate["prefix_sha256"]
    assert certificate["h3_crosscheck"]["outcome"] == "no_violation_in_finite_prefix"
    assert certificate["outcome"] == "no_violation_in_finite_prefix"
    assert certificate["witness"] is None

    expected_h3 = len(h3) * (len(h3) - 1) // 2
    expected_h4 = len(h4) * (len(h4) - 1) // 2
    assert certificate["h3_crosscheck"]["left_signatures_inserted"] == expected_h3
    assert certificate["h3_crosscheck"]["right_signatures_queried"] == expected_h3
    assert certificate["left_signatures_inserted_before_stop"] == expected_h4
    assert certificate["right_signatures_queried_before_stop"] == expected_h4
    assert certificate["expected_each_side_if_complete"] == expected_h4
    assert certificate["splits_completed"] == len(h4) - 1

    # Internal adjacencies of h(0) are unequal.  Since its first and last
    # symbols are both 0, applying h preserves the property "adjacent letters
    # are unequal", including image boundaries.
    assert BASE[0] == BASE[-1] == 0
    assert all(a != b for a, b in zip(BASE, BASE[1:]))

    # BASE contains an adjacent representative for every possible nonzero
    # cyclic difference.  The corresponding h^3 block pairs occur literally
    # in h^4(0), and equivariance is checked for every starting letter.
    representatives: dict[int, tuple[int, int, int]] = {}
    for i, (a, b) in enumerate(zip(BASE, BASE[1:])):
        representatives.setdefault((b - a) % 5, (i, a, b))
    assert set(representatives) == {1, 2, 3, 4}

    block = len(h3)
    for difference, (i, c, d) in representatives.items():
        literal_pair = iterate(3, c) + iterate(3, d)
        assert h4[i * block : (i + 2) * block] == literal_pair
        for a in range(5):
            b = (a + difference) % 5
            shift = (c - a) % 5
            arbitrary_pair = iterate(3, a) + iterate(3, b)
            shifted_pair = tuple((letter + shift) % 5 for letter in arbitrary_pair)
            assert shifted_pair == literal_pair

    print(
        json.dumps(
            {
                "outcome": "verified",
                "h3_sha256": digest(h3),
                "h4_sha256": digest(h4),
                "h4_factors_processed_each_side": expected_h4,
                "covered_cyclic_differences": sorted(representatives),
                "global_factor_length_bound_from_two_level3_blocks": block + 1,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
