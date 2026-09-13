#!/usr/bin/env python3
"""Fail-closed reconstruction of serialized exact equilateral witnesses."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "certificate" / "equilateral_witnesses.json"
CODE = Path(__file__).resolve()


class VerificationError(Exception):
    """A malformed input or failed exact-distance check."""


def fail(message: str) -> NoReturn:
    raise VerificationError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def as_fraction(value: object, location: str) -> Fraction:
    require(type(value) in (int, str), f"{location} must be an integer or rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        fail(f"invalid rational at {location}: {exc}")


def verify(input_path: Path) -> dict[str, object]:
    raw_bytes = input_path.read_bytes()
    raw = json.loads(raw_bytes)
    require(isinstance(raw, dict), "certificate root must be an object")
    missing = sorted({"schema_version", "witnesses"} - set(raw))
    require(not missing, f"missing required root fields: {missing}")
    require(raw["schema_version"] == 1, "schema_version must equal 1")
    require(isinstance(raw["witnesses"], list), "witnesses must be a list")

    expected = {
        "cross_polytope_l1_5": {"dimension": 5, "points": 10, "distance": Fraction(2)},
        "sharp_q11_example_in_l1_6": {"dimension": 6, "points": 11, "distance": Fraction(2)},
    }
    require(len(raw["witnesses"]) == len(expected), "unexpected witness count")
    result = []
    seen_names: set[str] = set()
    for witness_index, witness in enumerate(raw["witnesses"]):
        require(isinstance(witness, dict), f"witness {witness_index} must be an object")
        fields = {"name", "dimension", "common_distance", "points"}
        missing_fields = sorted(fields - set(witness))
        require(not missing_fields, f"witness {witness_index} missing fields: {missing_fields}")
        name = witness["name"]
        require(type(name) is str and name in expected, f"unexpected witness name: {name!r}")
        require(name not in seen_names, f"duplicate witness name: {name}")
        seen_names.add(name)
        spec = expected[name]

        dim = witness["dimension"]
        require(type(dim) is int and dim == spec["dimension"], f"dimension mismatch for {name}")
        delta = as_fraction(witness["common_distance"], f"{name}.common_distance")
        require(delta > 0, f"common distance must be positive for {name}")
        require(delta == spec["distance"], f"common distance endpoint mismatch for {name}")
        require(isinstance(witness["points"], list), f"points must be a list for {name}")
        require(len(witness["points"]) == spec["points"], f"point count mismatch for {name}")

        points: list[tuple[Fraction, ...]] = []
        for point_index, point in enumerate(witness["points"]):
            require(isinstance(point, list), f"{name}.points[{point_index}] must be a list")
            require(len(point) == dim, f"coordinate count mismatch at {name}.points[{point_index}]")
            points.append(
                tuple(as_fraction(value, f"{name}.points[{point_index}][{coordinate}]") for coordinate, value in enumerate(point))
            )
        require(len(set(points)) == len(points), f"repeated point in {name}")

        checked = 0
        for x, y in itertools.combinations(points, 2):
            distance = sum((abs(a - b) for a, b in zip(x, y)), Fraction(0))
            require(distance == delta, f"distance mismatch in {name} at pair index {checked}: {distance} != {delta}")
            checked += 1
        expected_pairs = spec["points"] * (spec["points"] - 1) // 2
        require(checked == expected_pairs, f"pair count mismatch for {name}")
        result.append({"name": name, "points": len(points), "pairs": checked})

    require(seen_names == set(expected), "required witness set is incomplete")
    return {
        "status": "PASS",
        "witnesses": result,
        "input_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "code_sha256": digest(CODE),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    try:
        result = verify(args.certificate.resolve())
    except Exception as exc:
        print(
            json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
