#!/usr/bin/env python3
"""Produce the compact exact certificate located during discovery."""

from __future__ import annotations

import json
import platform
from pathlib import Path

import numpy as np
import numba

from discover_numpy import (build_mul_table, deterministic_pairs, evaluate_words,
                            packed_columns, rank_and_first_relation)


IDENTITY_SUPPORT = [
    "XXXYXY", "XXXYYX", "XYXXXY", "XYYXXX", "YXXXYX", "YXYXXX",
    "XXXXYXY", "XXXXYYX", "XXXYXXY", "XXXYYXX", "XXYXXXY",
    "XXYYXXX", "XYXXXXY", "XYYXXXX", "YXXXXYX", "YXXXYXX",
    "YXXYXXX", "YXYXXXX",
]

WITNESS_SCHEDULE_INDICES = [0, 1, 16, 21, 22, 23, 25, 27, 28, 33, 36, 38, 46, 48, 2]


def independent_row_indices(rows: list[int]) -> list[int]:
    basis: dict[int, int] = {}
    selected: list[int] = []
    for row_index, original in enumerate(rows):
        vector = original
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = vector
                selected.append(row_index)
                break
            vector ^= basis[pivot]
    return selected


def main() -> None:
    mul = build_mul_table()
    all_a, all_b = deterministic_pairs(4096)
    a = all_a[WITNESS_SCHEDULE_INDICES]
    b = all_b[WITNESS_SCHEDULE_INDICES]
    words, values = evaluate_words(6, a, b, mul)

    coordinate_rows: list[int] = []
    coordinates: list[dict[str, int]] = []
    for pair_index in range(len(a)):
        for entry in range(9):
            row = 0
            for word_index in range(len(words)):
                row |= int((values[word_index, pair_index] >> entry) & 1) << word_index
            coordinate_rows.append(row)
            coordinates.append({"pair_index": pair_index, "entry": entry})
    selected = independent_row_indices(coordinate_rows)
    if len(selected) != 127:
        raise RuntimeError(f"expected rank 127, obtained {len(selected)}")

    ranks = []
    for degree in range(7):
        d_words, d_values = evaluate_words(degree, a, b, mul)
        rank, relation, _ = rank_and_first_relation(packed_columns(d_values))
        if relation is not None or rank != len(d_words):
            raise RuntimeError(f"degree {degree} is unexpectedly deficient")
        ranks.append({"degree": degree, "columns": len(d_words), "rank": rank})

    cert = {
        "schema": "m3f2-two-variable-pi-minimum-v1",
        "claim": {"least_degree": 7, "lower_degree": 6},
        "field": "F_2",
        "matrix_encoding": {
            "integer_range": [0, 511],
            "bit_index": "3*row+column",
            "row_and_column_indices": [0, 1, 2],
        },
        "word_convention": {
            "alphabet": ["X", "Y"],
            "multiplication": "left to right",
            "empty_word": "I_3",
        },
        "identity": {
            "coefficient": 1,
            "support": IDENTITY_SUPPORT,
            "support_size": len(IDENTITY_SUPPORT),
            "degree": 7,
        },
        "lower_bound": {
            "witness_pairs": [[int(x), int(y)] for x, y in zip(a, b)],
            "selected_minor_rows": [coordinates[i] for i in selected],
            "rank_by_degree": ranks,
            "degree_6_columns": 127,
            "degree_6_minor_rank": 127,
        },
        "exhaustive_domain": {
            "ordered_pairs": 262144,
            "enumeration": "A=0,...,511 outer; B=0,...,511 inner",
        },
        "provenance": {
            "generator": "src/make_certificate.py",
            "arithmetic": "exact GF(2)",
            "python": platform.python_version(),
            "numpy": np.__version__,
            "numba": numba.__version__,
        },
    }
    destination = Path("certificates/min_degree_7.json")
    destination.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(destination)


if __name__ == "__main__":
    main()
