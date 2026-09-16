#!/usr/bin/env python3
"""Independent exact verifier for the proposed equality s_1(4) = 9.

This implementation deliberately does not use combinations_with_replacement
or subsets of sequence positions.  It represents a residue multiset by its
12-coordinate multiplicity vector.  A recursive weak-composition generator
visits every such vector of the requested total exactly once.  For each vector,
the coefficient support of

    product_r (1 + y*x^r + ... + y^min(c_r,4)*x^(min(c_r,4)*r))

is computed through degree 4 in y, with exponents of x reduced modulo 16 and
Boolean coefficients.  Thus the degree-4 support is exactly the set of
residues obtainable by a four-element submultiset respecting multiplicities.

All arithmetic and all decisions are exact.  The lower-bound witness is also
checked by a separately written recursion over bounded submultiplicities.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from math import comb
import json


MODULUS = 16
PICK_COUNT = 4
ALLOWED = (1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15)
TARGET = (4, 8, 12)
TARGET_MASK = sum(1 << residue for residue in TARGET)
LOWER_WITNESS = (1, 1, 1, 2, 2, 2, 10, 13)


def multiplicity_vectors(total: int, coordinates: int = len(ALLOWED)):
    """Yield each weak composition of ``total`` into ``coordinates`` parts.

    The first coordinate ranges from 0 through ``total``; after each choice,
    the same rule is applied to the remainder, and the final coordinate is
    forced.  Hence every nonnegative vector of the named sum has one and only
    one root-to-leaf choice path.
    """

    prefix = [0] * coordinates

    def visit(position: int, remainder: int):
        if position == coordinates - 1:
            prefix[position] = remainder
            yield tuple(prefix)
            return
        for value in range(remainder + 1):
            prefix[position] = value
            yield from visit(position + 1, remainder - value)

    yield from visit(0, total)


def rotate_residue_mask(mask: int, shift: int) -> int:
    """Cyclically shift a 16-bit residue mask by ``shift`` modulo 16."""

    shift %= MODULUS
    if shift == 0:
        return mask
    all_bits = (1 << MODULUS) - 1
    return ((mask << shift) | (mask >> (MODULUS - shift))) & all_bits


def four_sum_mask(counts: tuple[int, ...]) -> int:
    """Return the exact 16-bit support of attainable four-submultiset sums."""

    degree_masks = [0] * (PICK_COUNT + 1)
    degree_masks[0] = 1  # residue 0 using zero terms
    for residue, available in zip(ALLOWED, counts):
        updated = [0] * (PICK_COUNT + 1)
        maximum_take = min(available, PICK_COUNT)
        for previous_degree, previous_mask in enumerate(degree_masks):
            if previous_mask == 0:
                continue
            for take in range(min(maximum_take, PICK_COUNT - previous_degree) + 1):
                updated[previous_degree + take] |= rotate_residue_mask(
                    previous_mask, take * residue
                )
        degree_masks = updated
    return degree_masks[PICK_COUNT]


def target_signature(sum_mask: int) -> int:
    """Encode reachability of residues 4, 8, and 12 as bits 0, 1, and 2."""

    signature = 0
    for bit, residue in enumerate(TARGET):
        if sum_mask & (1 << residue):
            signature |= 1 << bit
    return signature


def encode_counts(counts: tuple[int, ...]) -> bytes:
    """Canonical fixed-width encoding; totals here are below 256."""

    return bytes(counts)


def scan(total: int) -> dict[str, object]:
    """Exhaust all multiplicity vectors of the named total."""

    state_digest = sha256()
    avoiding_digest = sha256()
    signatures: Counter[int] = Counter()
    tested = 0
    avoiding = 0
    first_avoider = None

    for counts in multiplicity_vectors(total):
        tested += 1
        sum_mask = four_sum_mask(counts)
        signature = target_signature(sum_mask)
        signatures[signature] += 1
        encoded = encode_counts(counts)
        state_digest.update(encoded)
        state_digest.update(bytes((signature,)))
        if signature == 0:
            avoiding += 1
            avoiding_digest.update(encoded)
            if first_avoider is None:
                first_avoider = counts

    expected = comb(total + len(ALLOWED) - 1, len(ALLOWED) - 1)
    assert tested == expected
    assert sum(signatures.values()) == tested
    return {
        "length": total,
        "expected_weak_compositions": expected,
        "tested_multiplicity_vectors": tested,
        "avoiding_multiplicity_vectors": avoiding,
        "first_avoiding_counts": first_avoider,
        "target_signature_histogram": {
            str(signature): signatures[signature] for signature in range(8)
        },
        "counts_and_target_signature_sha256": state_digest.hexdigest(),
        "avoiding_counts_sha256": avoiding_digest.hexdigest(),
    }


def counts_for_sequence(sequence: tuple[int, ...]) -> tuple[int, ...]:
    multiplicities = Counter(sequence)
    assert set(multiplicities) <= set(ALLOWED)
    return tuple(multiplicities[residue] for residue in ALLOWED)


def direct_bounded_four_sums(counts: tuple[int, ...]) -> tuple[int, ...]:
    """Independently enumerate bounded take-counts summing to four.

    This routine does not call ``four_sum_mask``.  Its leaves are precisely the
    integer vectors q with 0 <= q_r <= c_r and sum(q_r) = 4.
    """

    sums: set[int] = set()

    def visit(position: int, remaining: int, running_sum: int) -> None:
        if position == len(ALLOWED):
            if remaining == 0:
                sums.add(running_sum % MODULUS)
            return
        for take in range(min(counts[position], remaining) + 1):
            visit(
                position + 1,
                remaining - take,
                running_sum + take * ALLOWED[position],
            )

    visit(0, PICK_COUNT, 0)
    return tuple(sorted(sums))


def main() -> None:
    witness_counts = counts_for_sequence(LOWER_WITNESS)
    witness_dp_mask = four_sum_mask(witness_counts)
    witness_dp_sums = tuple(
        residue for residue in range(MODULUS) if witness_dp_mask & (1 << residue)
    )
    witness_direct_sums = direct_bounded_four_sums(witness_counts)
    assert witness_dp_sums == witness_direct_sums
    assert not set(witness_direct_sums).intersection(TARGET)

    scans = (scan(8), scan(9))
    assert scans[0]["avoiding_multiplicity_vectors"] > 0
    assert scans[1]["avoiding_multiplicity_vectors"] == 0

    report = {
        "algorithm": {
            "domain": "recursive weak compositions (multiplicity vectors)",
            "predicate": "degree-4 Boolean generating-function DP modulo 16",
            "lower_witness_cross_check": "separate bounded-submultiplicity recursion",
            "uses_combinations_with_replacement": False,
            "uses_position_subsets": False,
        },
        "arithmetic": "exact integer and Boolean bit-mask arithmetic",
        "allowed_residues_mod_16": ALLOWED,
        "target_four_sum_residues_mod_16": TARGET,
        "lower_witness": LOWER_WITNESS,
        "lower_witness_counts": witness_counts,
        "lower_witness_four_sum_residues_mod_16": witness_direct_sums,
        "scans": scans,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
