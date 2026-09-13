#!/usr/bin/env python3
"""Fail-closed exact verifier for a serialized t=15 chain candidate."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


DEFAULT = Path(__file__).resolve().with_name("t15_exact_candidate.json")


class VerificationError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def rational(value: object, location: str) -> Fraction:
    require(type(value) in (int, str), f"{location} must be an integer or rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        fail(f"invalid rational at {location}: {exc}")


def verify(path: Path) -> dict[str, object]:
    raw_bytes = path.read_bytes()
    data = json.loads(raw_bytes)
    require(isinstance(data, dict), "root must be an object")
    required = {"schema", "labels", "dimension", "common_distance", "positive_gap_total", "coordinates"}
    require(required.issubset(data), f"missing root fields: {sorted(required - set(data))}")
    require(data["schema"] == "kusner.t15.exact-chain-candidate.v1", "schema mismatch")
    require(data["labels"] == 11 and data["dimension"] == 5, "endpoint mismatch")
    require(data["positive_gap_total"] == 15, "gap total mismatch")
    common_distance = rational(data["common_distance"], "common_distance")
    require(common_distance > 0, "common distance must be positive")
    coordinates = data["coordinates"]
    require(isinstance(coordinates, list) and len(coordinates) == 5, "coordinate list mismatch")

    all_cuts: list[tuple[int, ...]] = []
    all_gaps: list[Fraction] = []
    lengths: list[int] = []
    reconstructed_points = [[Fraction(0) for _ in range(5)] for _ in range(11)]
    for coordinate_index, coordinate in enumerate(coordinates):
        require(isinstance(coordinate, dict), f"coordinate {coordinate_index} must be an object")
        require(set(coordinate) == {"cut_sizes", "prefix_membership", "gaps"}, f"coordinate {coordinate_index} fields mismatch")
        cut_sizes = coordinate["cut_sizes"]
        cuts = coordinate["prefix_membership"]
        gaps = coordinate["gaps"]
        require(isinstance(cut_sizes, list) and all(type(value) is int for value in cut_sizes), f"bad cut sizes at coordinate {coordinate_index}")
        require(2 <= len(cut_sizes) <= 4, f"bad chain length at coordinate {coordinate_index}")
        require(all(1 <= cut_sizes[i] < cut_sizes[i + 1] <= 10 for i in range(len(cut_sizes) - 1)), f"cut sizes not strict at coordinate {coordinate_index}")
        require(isinstance(cuts, list) and len(cuts) == len(cut_sizes), f"cut count mismatch at coordinate {coordinate_index}")
        require(isinstance(gaps, list) and len(gaps) == len(cut_sizes), f"gap count mismatch at coordinate {coordinate_index}")
        parsed_gaps = [rational(value, f"coordinates[{coordinate_index}].gaps[{index}]") for index, value in enumerate(gaps)]
        require(all(value > 0 for value in parsed_gaps), f"nonpositive gap at coordinate {coordinate_index}")
        parsed_cuts: list[tuple[int, ...]] = []
        for cut_index, cut in enumerate(cuts):
            require(isinstance(cut, list) and len(cut) == 11, f"bad cut vector at {coordinate_index},{cut_index}")
            require(all(type(value) is int and value in (0, 1) for value in cut), f"nonbinary cut at {coordinate_index},{cut_index}")
            parsed = tuple(cut)
            require(sum(parsed) == cut_sizes[cut_index], f"cut cardinality mismatch at {coordinate_index},{cut_index}")
            if cut_index:
                require(all(parsed_cuts[-1][label] <= parsed[label] for label in range(11)), f"cuts not nested at coordinate {coordinate_index}")
            parsed_cuts.append(parsed)
        for label in range(11):
            reconstructed_points[label][coordinate_index] = sum(
                (parsed_gaps[index] for index, cut in enumerate(parsed_cuts) if not cut[label]), Fraction(0)
            )
        all_cuts.extend(parsed_cuts)
        all_gaps.extend(parsed_gaps)
        lengths.append(len(cut_sizes))

    require(sum(lengths) == 15, "reconstructed gap total mismatch")
    require(sorted(lengths, reverse=True) in ([3, 3, 3, 3, 3], [4, 3, 3, 3, 2]), "gap pattern mismatch")
    checked = 0
    for first, second in itertools.combinations(range(11), 2):
        cut_distance = sum(
            (gap for cut, gap in zip(all_cuts, all_gaps) if cut[first] != cut[second]), Fraction(0)
        )
        direct_distance = sum(
            (abs(a - b) for a, b in zip(reconstructed_points[first], reconstructed_points[second])), Fraction(0)
        )
        require(cut_distance == common_distance, f"cut distance mismatch at pair {checked}")
        require(direct_distance == common_distance, f"direct distance mismatch at pair {checked}")
        checked += 1
    require(checked == 55, "pair count mismatch")
    require(len({tuple(point) for point in reconstructed_points}) == 11, "repeated reconstructed point")
    return {
        "status": "PASS",
        "claim": "exact eleven-point equilateral witness in l1^5",
        "gap_pattern": sorted(lengths, reverse=True),
        "pairs": checked,
        "input_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    try:
        result = verify(args.candidate.resolve())
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
