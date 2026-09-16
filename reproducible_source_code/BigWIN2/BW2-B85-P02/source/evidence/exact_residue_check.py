#!/usr/bin/env python3
"""Exact finite check supporting triage of the s_1(4) problem.

This program is deliberately self-contained and uses only Python's standard
library.  It enumerates each multiset once, then tests every four-element
choice of sequence positions.  All arithmetic is exact.
"""

from hashlib import sha256
from itertools import combinations, combinations_with_replacement
from math import comb
import json


MODULUS = 16
ALLOWED = tuple(r for r in range(MODULUS) if r % 4 != 0)
TARGET = (4, 8, 12)


def has_target_four_sum(sequence):
    """Return a witnessing index tuple, or None if none exists."""
    for indices in combinations(range(len(sequence)), 4):
        if sum(sequence[i] for i in indices) % MODULUS in TARGET:
            return indices
    return None


def scan(length):
    domain_digest = sha256()
    avoider_digest = sha256()
    tested = 0
    avoiders = 0
    first_avoider = None
    for sequence in combinations_with_replacement(ALLOWED, length):
        tested += 1
        witness = has_target_four_sum(sequence)
        encoding = bytes(sequence)
        domain_digest.update(encoding)
        domain_digest.update(b"\x01" if witness is not None else b"\x00")
        if witness is None:
            avoiders += 1
            avoider_digest.update(encoding)
            if first_avoider is None:
                first_avoider = sequence

    expected = comb(len(ALLOWED) + length - 1, length)
    assert tested == expected
    return {
        "length": length,
        "expected_multisets": expected,
        "tested_multisets": tested,
        "avoiding_multisets": avoiders,
        "first_avoider": first_avoider,
        "domain_and_outcome_sha256": domain_digest.hexdigest(),
        "avoider_sha256": avoider_digest.hexdigest(),
    }


def main():
    scans = [scan(8), scan(9)]
    lower_witness = scans[0]["first_avoider"]
    assert lower_witness is not None
    lower_witness_four_sums = sorted(
        {
            sum(lower_witness[i] for i in indices) % MODULUS
            for indices in combinations(range(8), 4)
        }
    )
    assert not set(lower_witness_four_sums).intersection(TARGET)
    assert scans[1]["avoiding_multisets"] == 0

    report = {
        "arithmetic": "exact integer arithmetic",
        "allowed_residues_mod_16": ALLOWED,
        "target_four_sum_residues_mod_16": TARGET,
        "scans": scans,
        "lower_witness_four_sum_residues_mod_16": lower_witness_four_sums,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
