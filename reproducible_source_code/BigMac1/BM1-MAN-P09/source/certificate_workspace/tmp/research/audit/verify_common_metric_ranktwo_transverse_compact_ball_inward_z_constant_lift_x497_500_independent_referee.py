#!/usr/bin/env python3
"""Frozen formal no-builder-import referee for constant-Z [99/100,497/500].

The mathematical reconstruction is the separately frozen literal-free scout
module in this directory.  It imports or executes no builder artifact; the
current candidate source and manifest are accessed only for SHA-256 binding.
This wrapper adds the post-scout frozen weakest/reserve/polynomial assertions.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import sympy as sp

from constant_z_x497_500_referee_literal_free_scout import (
    PREV_REFEREE,
    SOURCE,
    SOURCE_MANIFEST,
    reconstruct,
)


EXPECTED_WEAKEST = (7, 0)
EXPECTED_RESERVE = sp.Rational(
    237983128275106868164816372024450404725835762778737426332055936856452553581744586321,
    719207337600221184000000000000000000000000000000000000000000000000000000,
)
EXPECTED_WEAKEST_POLYNOMIAL_SHA256 = (
    "7135ba124304e7fa5688e925f44f698b052919a1aab86af36073dabe15d68f7b"
)


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
    require(result["weakest"] == EXPECTED_WEAKEST,
            "formal weakest index equals literal-free scout")
    require(result["reserve"] == EXPECTED_RESERVE,
            "formal reserve equals literal-free scout")
    polynomial_text = str(result["weakest_polynomial"]).encode("utf-8")
    require(hashlib.sha256(polynomial_text).hexdigest()
            == EXPECTED_WEAKEST_POLYNOMIAL_SHA256,
            "complete weakest polynomial equals frozen scout polynomial")
    require(result["node_count"] == 72, "formal 72 diagnostic nodes")
    print("FORMAL_WEAKEST", EXPECTED_WEAKEST)
    print("FORMAL_RESERVE", EXPECTED_RESERVE)
    print("FORMAL_WEAKEST_POLYNOMIAL_SHA256",
          EXPECTED_WEAKEST_POLYNOMIAL_SHA256)
    print("VERDICT PASS exact constant-Z [99/100,497/500] local cell")
    print("SCOPE no raw-negative/maximality/full-ball/common-metric conclusion")


if __name__ == "__main__":
    main()
