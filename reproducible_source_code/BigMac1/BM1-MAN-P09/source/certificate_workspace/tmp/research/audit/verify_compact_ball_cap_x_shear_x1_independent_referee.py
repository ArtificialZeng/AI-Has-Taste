#!/usr/bin/env python3
"""Frozen formal no-builder-import referee for cap shear [497/500,1].

The reconstruction lives in the separately frozen literal-free scout.  The
candidate source and manifest remain opaque SHA-256 inputs; no builder module
is imported, executed, parsed, or read for mathematical data.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import sympy as sp

from cap_x_shear_x1_referee_literal_free_scout import (
    PREV_REFEREE,
    SOURCE,
    SOURCE_MANIFEST,
    reconstruct,
)


EXPECTED_STRUCTURE = {
    "cleared_terms": 48,
    "core_terms": 48,
    "centered_terms": 2263,
    "degree_s": 7,
    "degree_x": 8,
    "control_count": 72,
    "node_count": 72,
}
EXPECTED_WEAKEST = (7, 8)
EXPECTED_RESERVE = sp.Rational(
    79085602723906157917988882974367991904890648543683584180560419945180485170965315227,
    239735779200073728000000000000000000000000000000000000000000000000000000,
)
EXPECTED_POLYNOMIAL_SHA256 = (
    "6510213895aa636f0ef06dd2d903a7b9e6cdf33003d1d6d8c184ce1730a53ccf"
)
EXPECTED_LEGALITY = {
    "Zmin": sp.Rational(
        17798406223702873, 15857127000000000000),
    "Zupper": sp.Rational(10967, 2600000),
    "Tmax": -sp.Rational(1218219, 40625),
    "danger_left": sp.Rational(13993, 2600000),
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path, default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "bad-normalization", "drop-q2", "flip-danger", "drop-core"
    ), default="none")
    args = parser.parse_args()
    result = reconstruct(source_path=args.source_path,
                         manifest_path=args.manifest_path,
                         dependency_path=args.dependency_path,
                         attack=args.attack)
    for key, expected in EXPECTED_STRUCTURE.items():
        require(result[key] == expected, f"formal frozen structure: {key}")
    require(result["weakest"] == EXPECTED_WEAKEST,
            "formal weakest equals literal-free scout")
    require(result["reserve"] == EXPECTED_RESERVE,
            "formal reserve equals literal-free scout")
    polynomial_text = str(result["weakest_polynomial"]).encode("utf-8")
    require(hashlib.sha256(polynomial_text).hexdigest()
            == EXPECTED_POLYNOMIAL_SHA256,
            "complete weakest polynomial equals frozen scout polynomial")
    for key, expected in EXPECTED_LEGALITY.items():
        require(result[key] == expected, f"formal frozen legality: {key}")
    print("FORMAL_STRUCTURE", EXPECTED_STRUCTURE)
    print("FORMAL_WEAKEST", EXPECTED_WEAKEST)
    print("FORMAL_RESERVE", EXPECTED_RESERVE)
    print("FORMAL_WEAKEST_POLYNOMIAL_SHA256", EXPECTED_POLYNOMIAL_SHA256)
    print("VERDICT PASS exact cap-shear [497/500,1] local cell")
    print("VERDICT PASS old X=1 x,y family chart no-go for every S>0,Z>=0")
    print("SCOPE no raw CE, maximality, full-ball or common-metric conclusion")


if __name__ == "__main__":
    main()
