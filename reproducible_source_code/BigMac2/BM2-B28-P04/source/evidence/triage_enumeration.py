#!/usr/bin/env python3
"""Exact finite comparison suggested by Shin's Corollary 10.5."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def label_data(diameter: int) -> dict[int, tuple[int, int, int, int]]:
    first_witness: dict[int, tuple[int, int, int, int]] = {}
    for alphabet in itertools.combinations(range(diameter + 1), 4):
        sums = {
            sum(terms)
            for terms in itertools.combinations_with_replacement(alphabet, 4)
        }
        first_witness.setdefault(len(sums), alphabet)
    return first_witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    by_diameter = {diameter: label_data(diameter) for diameter in (15, 16)}
    labels_15 = set(by_diameter[15])
    labels_16 = set(by_diameter[16])
    payload = {
        "method": (
            "Enumerate every 4-subset of [0,D] and every nondecreasing "
            "4-tuple of its elements; count the distinct integer sums."
        ),
        "alphabet_counts": {"15": 1820, "16": 2380},
        "labels": {
            str(diameter): sorted(by_diameter[diameter])
            for diameter in (15, 16)
        },
        "first_witnesses": {
            str(diameter): {
                str(label): list(alphabet)
                for label, alphabet in sorted(by_diameter[diameter].items())
            }
            for diameter in (15, 16)
        },
        "labels_in_16_not_15": sorted(labels_16 - labels_15),
        "labels_in_15_not_16": sorted(labels_15 - labels_16),
        "equal_label_sets": labels_15 == labels_16,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
