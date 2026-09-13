#!/usr/bin/env python3
"""Independent fail-closed exact audit of the finite t=15 calculations.

This script checks only the finite cut-size, endpoint-deficit, regularity-case,
and counting calculations in proof/t15_dense_branch.md.  It is not a machine
proof of the kernel/rank or singleton-compression linear algebra.

All decisive checks use explicit branches that remain active under python -O.
No project verifier, frame audit, runner, log, or discovery output is imported.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


M = 11
CODE = Path(__file__).resolve()
PROOF = CODE.parents[1] / "proof" / "t15_dense_branch.md"


class AuditError(Exception):
    """A malformed audit setup or failed exact check."""


def fail(message: str) -> NoReturn:
    raise AuditError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint_ratio_squared(first: int, last: int) -> Fraction:
    """Return theta^2 for centered prefixes of sizes first < last."""
    require(1 <= first < last <= M - 1, "invalid endpoint sizes")
    return Fraction(first * (M - last), last * (M - first))


def endpoint_bound_implies(
    ratio_squared: Fraction,
    chain_length: int,
    target: Fraction,
    *,
    strict: bool,
) -> bool:
    """Check the radical-free form of the endpoint deficit comparison.

    For n=chain_length-1 and u=(theta)^(1/n), the bound is
    2*n*u/(1+u).  It exceeds target exactly when
    ratio_squared > (target/(2*n-target))^(2*n).
    """
    n = chain_length - 1
    require(n >= 1, "chain length must be at least two")
    require(Fraction(0) <= target < 2 * n, "invalid deficit target")
    threshold = (target / (2 * n - target)) ** (2 * n)
    return ratio_squared > threshold if strict else ratio_squared >= threshold


def singleton_ray_count(sizes: tuple[int, ...]) -> int:
    return int(sizes[0] == 1) + int(sizes[-1] == M - 1)


def check_endpoint_enumeration() -> dict[str, object]:
    specifications = {
        2: {
            "general": (Fraction(2, 11), False),
            "nonregular": (Fraction(1, 4), True),
        },
        3: {
            "general": (Fraction(24, 25), True),
            "nonregular": (Fraction(11, 10), True),
            "neither": (Fraction(5, 4), True),
        },
        4: {
            "general": (Fraction(19, 10), True),
            "nonregular": (Fraction(2), True),
        },
    }
    expected_counts = {
        2: {"total": 45, "regular": 1, "nonregular": 44, "neither": 28},
        3: {"total": 120, "regular": 8, "nonregular": 112, "neither": 56},
        4: {"total": 210, "regular": 28, "nonregular": 182, "neither": 70},
    }
    records: dict[str, object] = {}
    for chain_length in (2, 3, 4):
        counts = {"total": 0, "regular": 0, "nonregular": 0, "neither": 0}
        minimum_nonregular: Fraction | None = None
        minimum_neither: Fraction | None = None
        for sizes in itertools.combinations(range(1, M), chain_length):
            counts["total"] += 1
            regular = sizes[0] == 1 and sizes[-1] == M - 1
            neither = sizes[0] >= 2 and sizes[-1] <= M - 2
            category = "regular" if regular else "nonregular"
            counts[category] += 1
            if neither:
                counts["neither"] += 1

            rays = singleton_ray_count(sizes)
            require(rays == (2 if regular else (0 if neither else 1)), f"singleton-ray classification failed: {sizes}")
            require(chain_length - rays >= 0, f"negative non-singleton count: {sizes}")

            ratio = endpoint_ratio_squared(sizes[0], sizes[-1])
            target, strict = specifications[chain_length]["general"]
            require(
                endpoint_bound_implies(ratio, chain_length, target, strict=strict),
                f"general deficit bound failed: length={chain_length}, sizes={sizes}",
            )
            if not regular:
                minimum_nonregular = ratio if minimum_nonregular is None else min(minimum_nonregular, ratio)
                target, strict = specifications[chain_length]["nonregular"]
                require(
                    endpoint_bound_implies(ratio, chain_length, target, strict=strict),
                    f"nonregular deficit bound failed: length={chain_length}, sizes={sizes}",
                )
            if neither:
                minimum_neither = ratio if minimum_neither is None else min(minimum_neither, ratio)
                if "neither" in specifications[chain_length]:
                    target, strict = specifications[chain_length]["neither"]
                    require(
                        endpoint_bound_implies(ratio, chain_length, target, strict=strict),
                        f"neither-endpoint deficit bound failed: length={chain_length}, sizes={sizes}",
                    )

        require(counts == expected_counts[chain_length], f"cut-size counts differ for length {chain_length}: {counts}")
        require(minimum_nonregular == Fraction(1, 45), f"wrong nonregular endpoint minimum for length {chain_length}")
        require(minimum_neither == Fraction(4, 81), f"wrong no-singleton endpoint minimum for length {chain_length}")
        records[str(chain_length)] = {
            "counts": counts,
            "minimum_nonregular_ratio_squared": str(minimum_nonregular),
            "minimum_neither_ratio_squared": str(minimum_neither),
        }
    return records


def check_strict_integer_comparisons() -> dict[str, bool]:
    checks = {
        "triple_nonregular": 29**4 > 45 * 11**4,
        "triple_no_singletons": 2 * 121 > 25 * 9,
        "quadruple_nonregular": 64 > 45,
        "double_nonregular": 49 > 45,
    }
    require(all(checks.values()), f"strict powered comparison failed: {checks}")
    return checks


def check_pattern_33333() -> dict[str, object]:
    lower = {
        "R": Fraction(24, 25),
        "O": Fraction(11, 10),
        "N": Fraction(5, 4),
    }
    survivors: list[tuple[str, ...]] = []
    for categories in itertools.product(("R", "O", "N"), repeat=5):
        conservative_sum = sum((lower[value] for value in categories), Fraction(0))
        if conservative_sum < 5:
            survivors.append(categories)
    expected = [("R",) * 5]
    expected.extend(
        tuple("O" if index == exceptional else "R" for index in range(5))
        for exceptional in range(5)
    )
    require(sorted(survivors) == sorted(expected), f"unexpected (3,3,3,3,3) regularity survivors: {survivors}")
    require(2 * lower["O"] + 3 * lower["R"] == Fraction(127, 25) > 5, "two-nonregular triple budget failed")
    require(lower["N"] + 4 * lower["R"] == Fraction(509, 100) > 5, "no-singleton triple budget failed")

    all_regular = {"singleton_copies": 10, "R": 5, "h_min": 6, "endpoint_capacity": 5}
    one_exception = {"singleton_copies": 9, "R": 6, "h_min": 5, "endpoint_capacity": 5}
    require(all_regular["h_min"] > all_regular["endpoint_capacity"], "Case A endpoint contradiction absent")
    require(one_exception["h_min"] == one_exception["endpoint_capacity"] == M - one_exception["R"], "Case B equality compression absent")
    return {
        "category_assignments_checked": 3**5,
        "surviving_assignments": len(survivors),
        "surviving_histograms": ["R^5", "R^4 O"],
        "case_A": all_regular,
        "case_B": one_exception,
    }


def check_pattern_43332() -> dict[str, object]:
    lengths = (4, 3, 3, 3, 2)
    regular = {4: Fraction(19, 10), 3: Fraction(24, 25), 2: Fraction(2, 11)}
    nonregular = {4: Fraction(2), 3: Fraction(11, 10), 2: Fraction(1, 4)}
    survivors: list[tuple[bool, ...]] = []
    for flags in itertools.product((False, True), repeat=5):
        conservative_sum = sum(
            (nonregular[length] if flag else regular[length])
            for length, flag in zip(lengths, flags)
        )
        if conservative_sum < 5:
            survivors.append(flags)
    require(survivors == [(False,) * 5], f"unexpected (4,3,3,3,2) regularity survivors: {survivors}")
    require(nonregular[4] + 3 * regular[3] + regular[2] > 5, "nonregular quadruple budget failed")
    require(regular[4] + nonregular[3] + 2 * regular[3] + regular[2] > 5, "nonregular triple budget failed")
    require(regular[4] + 3 * regular[3] + nonregular[2] > 5, "nonregular double budget failed")

    counts = {"singleton_copies": 10, "R": 5, "h_min": 6, "endpoint_capacity": 4 + 2}
    require(counts["h_min"] == counts["endpoint_capacity"] == M - counts["R"], "pattern (4,3,3,3,2) equality compression absent")
    require(2 + 3 + 0 == counts["R"], "internal non-singleton count mismatch")
    return {
        "regularity_assignments_checked": 2**5,
        "surviving_assignments": len(survivors),
        "survivor": "all regular",
        "compression_counts": counts,
    }


def audit() -> dict[str, object]:
    require(M == 11, f"audit is bound to eleven labels, got {M}")
    require(PROOF.is_file(), f"missing proof file: {PROOF}")
    tree = ast.parse(CODE.read_text(encoding="utf-8"), filename=str(CODE))
    assert_nodes = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(assert_nodes == 0, f"optimization-removable assert nodes found: {assert_nodes}")

    endpoint_records = check_endpoint_enumeration()
    strict_checks = check_strict_integer_comparisons()
    pattern_33333 = check_pattern_33333()
    pattern_43332 = check_pattern_43332()
    return {
        "status": "PASS",
        "scope": "finite cut-size/deficit/counting audit; singleton-compression linear algebra remains a human proof",
        "m": M,
        "endpoint_records": endpoint_records,
        "strict_integer_comparisons": strict_checks,
        "pattern_33333": pattern_33333,
        "pattern_43332": pattern_43332,
        "ast_assert_nodes": assert_nodes,
        "proof_sha256": sha256(PROOF),
        "code_sha256": sha256(CODE),
    }


def main() -> int:
    try:
        result = audit()
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
