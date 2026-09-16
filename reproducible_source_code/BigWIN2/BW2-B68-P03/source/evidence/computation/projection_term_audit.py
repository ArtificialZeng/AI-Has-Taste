#!/usr/bin/env python3
"""Exact summand audit for formula (3.15) modulo 16.

This script expands the fourteen nonzero summands used in
``source_formula_mod16.py`` separately.  It records how they contribute on
the two conjectural progressions and verifies several whole-series
cancellations suggested by formal Frobenius identities modulo 2.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import source_formula_mod16 as sf

HERE = Path(__file__).resolve().parent

# (coefficient, q-shift, a(q)-power, a(q^3)-power, a(q^6)-power,
#  eta exponents), in the order of source_formula_mod16.py.
TERMS = [
    (1, 0, 6, 0, 1, {1:-18, 3:-6, 6:15, 12:-6}),
    (270, 1, 4, 0, 1, {1:-21, 2:2, 3:3, 4:-1, 6:9, 12:-3}),
    (7290, 2, 2, 0, 0, {1:-22, 2:-1, 3:6, 6:18, 12:-6}),
    (1080, 2, 3, 0, 0, {1:-20, 2:-1, 3:8, 4:1, 6:6, 12:-1}),
    (1080, 2, 3, 0, 0, {1:-22, 3:8, 4:1, 6:6, 9:2, 12:-1, 18:-1}),
    (1080, 2, 3, 0, 0, {1:-22, 2:1, 3:6, 4:-1, 6:12, 12:-3}),
    (14580, 3, 0, 0, 0, {1:-25, 2:1, 3:15, 4:-1, 6:12, 12:-3}),
    (29160, 3, 2, 0, 0, {1:-24, 2:3, 3:12, 6:2, 12:2}),
    (24, 3, 6, 0, 0, {1:-18, 3:-3, 6:5, 9:-1, 12:2, 18:2}),
    (29160, 4, 0, 0, 0, {1:-24, 2:2, 3:20, 4:-1, 6:-3, 12:5}),
    (13122, 4, 0, 0, 0, {1:-24, 3:16, 9:4, 18:5, 36:-2}),
    (29160, 4, 0, 0, 0, {1:-26, 2:3, 3:20, 4:-1, 6:-3, 9:2, 12:5, 18:-1}),
    (43740, 4, 1, 0, 0, {1:-24, 2:2, 3:12, 4:-1, 6:8, 12:-3, 18:3}),
    (8748, 4, 0, 1, 0, {1:-24, 3:16, 6:2, 9:4, 12:-1, 18:-1, 36:1}),
]


def digest(a: np.ndarray) -> str:
    return hashlib.sha256(bytes((a % sf.MOD).astype(np.uint8))).hexdigest()


def main() -> None:
    aq = sf.cubic_theta(1)
    aq3 = sf.cubic_theta(3)
    aq6 = sf.cubic_theta(6)
    apow = {p: sf.power(aq, p) for p in (1, 2, 3, 4, 6)}

    expanded = []
    for coefficient, shift, pa, pa3, pa6, exponents in TERMS:
        term = sf.eta_quotient(exponents)
        if pa:
            term = sf.mul(term, apow[pa])
        if pa3:
            term = sf.mul(term, aq3)
        if pa6:
            term = sf.mul(term, aq6)
        expanded.append(sf.shifted_scaled(term, coefficient, shift))

    total = sum(expanded, np.zeros(sf.N + 1, dtype=np.int64)) % sf.MOD
    recorded = np.frombuffer(
        (HERE / "source_formula_coefficients_mod16.bin").read_bytes(),
        dtype=np.uint8,
    ).astype(np.int64)
    assert np.array_equal(total, recorded)

    # These are identities of the complete truncated series, not merely of
    # the selected progressions.  The accompanying Markdown gives the formal
    # all-orders proof using f_d^2 == f_(2d) and a(q) == 1 modulo 2.
    cancellations = {
        "terms_4_and_5_sum_to_zero": (expanded[3] + expanded[4]) % sf.MOD,
        "terms_10_and_12_sum_to_zero": (expanded[9] + expanded[11]) % sf.MOD,
    }
    for value in cancellations.values():
        assert not np.any(value)

    term_summary = []
    target_vectors = []
    for index, term in enumerate(expanded, start=1):
        target = np.array(
            [term[30 * n + residue] for residue in (19, 25) for n in range(101)],
            dtype=np.uint8,
        )
        target_vectors.append(target.astype(np.int64))
        term_summary.append({
            "term": index,
            "coefficient_mod16": TERMS[index - 1][0] % sf.MOD,
            "whole_series_sha256": digest(term),
            "target_vector_sha256": hashlib.sha256(bytes(target)).hexdigest(),
            "nonzero_target_entries": int(np.count_nonzero(target)),
            "target_residues_seen": sorted({int(x) for x in target}),
        })

    surviving = [i for i in range(14) if i not in (3, 4, 9, 11)]
    reduced_total = sum(
        (expanded[i] for i in surviving),
        np.zeros(sf.N + 1, dtype=np.int64),
    ) % sf.MOD
    assert np.array_equal(reduced_total, total)

    target_zero_pairs = []
    for i in range(len(target_vectors)):
        for j in range(i + 1, len(target_vectors)):
            if not np.any((target_vectors[i] + target_vectors[j]) % sf.MOD):
                target_zero_pairs.append([i + 1, j + 1])

    projection_groups = {
        "1+2": [0, 1],
        "3+7": [2, 6],
        "4": [3],
        "5": [4],
        "6": [5],
        "8+9": [7, 8],
        "10": [9],
        "12": [11],
        "11+13+14": [10, 12, 13],
    }
    group_sections = {}
    for label, indices in projection_groups.items():
        poly = sum(
            (expanded[i] for i in indices),
            np.zeros(sf.N + 1, dtype=np.int64),
        ) % sf.MOD
        zero_classes = []
        for residue in range(5):
            selected = [
                poly[6 * m + 1]
                for m in range(residue, (sf.N - 1) // 6 + 1, 5)
            ]
            if not any(selected):
                zero_classes.append(residue)
        group_sections[label] = zero_classes

    report = {
        "coefficient_range": [0, sf.N],
        "arithmetic": "exact polynomial arithmetic modulo 16",
        "source_vector_verified": True,
        "formal_cancellation_pairs_one_based": [[4, 5], [10, 12]],
        "target_zero_pairs_one_based": target_zero_pairs,
        "observed_zero_m_classes_mod5_in_6m_plus_1_section": group_sections,
        "surviving_terms_one_based": [i + 1 for i in surviving],
        "reduced_total_sha256": digest(reduced_total),
        "all_202_target_residues_zero": all(
            reduced_total[30 * n + residue] == 0
            for residue in (19, 25) for n in range(101)
        ),
        "terms": term_summary,
    }
    (HERE / "projection_term_audit.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
