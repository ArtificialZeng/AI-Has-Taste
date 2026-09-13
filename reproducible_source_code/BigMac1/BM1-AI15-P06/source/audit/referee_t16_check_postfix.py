#!/usr/bin/env python3
"""Independent fail-closed exact audit of the finite t=16 calculations.

This program is deliberately separate from all project verifiers, frame
audits, runners, and logs.  It checks the rational/radical comparisons,
all 48 bounded partitions of 16 into five chain lengths, every endpoint-size
tuple used by the penalties, and all endpoint-category assignments for the
three surviving patterns.  The singleton-compression linear algebra remains
a human proof and is not claimed as a machine-checked result here.

Every decisive condition uses an explicit exception path that remains active
under Python optimization.
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
TOTAL_GAPS = 16
COORDINATES = 5
MAX_CHAIN = 7
EXPECTED_PROOF_SHA256 = "114d861529243e3eb96415e10f14920370b91f5085d1538fc0bb0f564e26d889"
CODE = Path(__file__).resolve()
PROJECT = CODE.parents[1]
PROOF = PROJECT / "proof" / "t16_branch.md"


class AuditFailure(Exception):
    """A malformed setup or failed exact check."""


def fail(message: str) -> NoReturn:
    raise AuditFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint_ratio_squared(first: int, last: int) -> Fraction:
    require(1 <= first < last <= M - 1, f"invalid endpoints: {(first, last)}")
    return Fraction(first * (M - last), last * (M - first))


def endpoint_bound_implies(
    ratio_squared: Fraction,
    chain_length: int,
    target: Fraction,
    *,
    strict: bool,
) -> bool:
    """Compare the Jensen endpoint bound with target without radicals."""
    n = chain_length - 1
    require(n >= 1, "chain length must be at least two")
    require(Fraction(0) <= target < 2 * n, f"invalid target: {target}")
    threshold = (target / (2 * n - target)) ** (2 * n)
    if strict:
        return ratio_squared > threshold
    return ratio_squared >= threshold


def chain_costs() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(0),
        Fraction(2, 11),
        Fraction(24, 25),
        Fraction(19, 10),
        Fraction(23, 8),
        Fraction(193, 50),
        Fraction(243, 50),
    )


def check_chain_costs_and_c7() -> dict[str, object]:
    costs = chain_costs()
    increments = tuple(costs[index] - costs[index - 1] for index in range(1, len(costs)))
    expected = (
        Fraction(0),
        Fraction(2, 11),
        Fraction(214, 275),
        Fraction(47, 50),
        Fraction(39, 40),
        Fraction(197, 200),
        Fraction(1),
    )
    require(increments == expected, f"increment list mismatch: {increments}")
    require(
        all(increments[index] <= increments[index + 1] for index in range(len(increments) - 1)),
        f"chain-cost sequence is not discretely convex: {increments}",
    )

    c7_radical = 119**6 > 10 * 81**6
    require(c7_radical, "c7 radical-free comparison failed")
    return {
        "costs": [str(value) for value in costs],
        "increments": [str(value) for value in increments],
        "c7_comparison_119^6_gt_10x81^6": c7_radical,
    }


def all_partitions() -> list[tuple[int, ...]]:
    partitions: list[tuple[int, ...]] = []
    for ascending in itertools.combinations_with_replacement(range(MAX_CHAIN + 1), COORDINATES):
        if sum(ascending) == TOTAL_GAPS:
            partitions.append(tuple(reversed(ascending)))
    return partitions


def check_partitions() -> dict[str, object]:
    costs = chain_costs()
    partitions = all_partitions()
    require(len(partitions) == 48, f"expected 48 bounded partitions, got {len(partitions)}")
    require(len(set(partitions)) == len(partitions), "duplicate partitions generated")
    require(
        all(len(partition) == COORDINATES and sum(partition) == TOTAL_GAPS for partition in partitions),
        "malformed partition generated",
    )
    survivors = []
    eliminated = []
    for partition in partitions:
        cost = sum((costs[length] for length in partition), Fraction(0))
        if cost <= 6:
            survivors.append((partition, cost))
        else:
            eliminated.append((partition, cost))
    expected = {
        (4, 3, 3, 3, 3): Fraction(287, 50),
        (4, 4, 3, 3, 2): Fraction(1623, 275),
        (5, 3, 3, 3, 2): Fraction(13061, 2200),
    }
    require(dict(survivors) == expected, f"unexpected deficit-compatible partitions: {survivors}")
    require(eliminated, "no eliminated partitions found")
    minimum_eliminated = min(eliminated, key=lambda item: item[1])
    require(
        minimum_eliminated == ((4, 4, 4, 2, 2), Fraction(667, 110)),
        f"wrong least-cost eliminated partition: {minimum_eliminated}",
    )
    require(not any(cost == 6 for _, cost in partitions_with_cost(partitions, costs)), "unhandled equality-six partition")
    return {
        "partitions_checked": len(partitions),
        "survivors": {str(partition): str(cost) for partition, cost in survivors},
        "minimum_eliminated": [str(minimum_eliminated[0]), str(minimum_eliminated[1])],
    }


def partitions_with_cost(
    partitions: list[tuple[int, ...]],
    costs: tuple[Fraction, ...],
) -> list[tuple[tuple[int, ...], Fraction]]:
    return [
        (partition, sum((costs[length] for length in partition), Fraction(0)))
        for partition in partitions
    ]


def singleton_endpoints(sizes: tuple[int, ...]) -> int:
    return int(sizes[0] == 1) + int(sizes[-1] == M - 1)


def check_endpoint_penalties() -> dict[str, object]:
    specifications: dict[int, dict[str, tuple[Fraction, bool]]] = {
        2: {
            "general": (Fraction(2, 11), False),
            "one": (Fraction(1, 4), True),
            "neither": (Fraction(4, 11), False),
        },
        3: {
            "general": (Fraction(24, 25), True),
            "one": (Fraction(11, 10), True),
            "neither": (Fraction(5, 4), True),
        },
        4: {
            "general": (Fraction(19, 10), True),
            "one": (Fraction(2), True),
            "neither": (Fraction(9, 4), True),
        },
        5: {
            "general": (Fraction(23, 8), True),
            "one": (Fraction(3), True),
            "neither": (Fraction(3), True),
        },
    }
    expected_totals = {2: 45, 3: 120, 4: 210, 5: 252}
    records: dict[str, object] = {}
    for length in range(2, 6):
        counts = {"all": 0, "regular": 0, "one": 0, "neither": 0}
        minimum_nonregular: Fraction | None = None
        minimum_neither: Fraction | None = None
        for sizes in itertools.combinations(range(1, M), length):
            counts["all"] += 1
            singletons = singleton_endpoints(sizes)
            require(singletons in (0, 1, 2), f"invalid singleton count: {sizes}")
            category = "regular" if singletons == 2 else ("one" if singletons == 1 else "neither")
            counts[category] += 1
            ratio = endpoint_ratio_squared(sizes[0], sizes[-1])

            target, strict = specifications[length]["general"]
            require(
                endpoint_bound_implies(ratio, length, target, strict=strict),
                f"general endpoint penalty failed: length={length}, sizes={sizes}",
            )
            if singletons < 2:
                minimum_nonregular = ratio if minimum_nonregular is None else min(minimum_nonregular, ratio)
                target, strict = specifications[length]["one"]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"nonregular endpoint penalty failed: length={length}, sizes={sizes}",
                )
            if singletons == 0:
                minimum_neither = ratio if minimum_neither is None else min(minimum_neither, ratio)
                target, strict = specifications[length]["neither"]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"neither-singleton endpoint penalty failed: length={length}, sizes={sizes}",
                )

        require(counts["all"] == expected_totals[length], f"tuple total mismatch at length {length}")
        require(minimum_nonregular == Fraction(1, 45), f"wrong nonregular ratio minimum at length {length}")
        require(minimum_neither == Fraction(4, 81), f"wrong neither ratio minimum at length {length}")
        records[str(length)] = {
            "counts": counts,
            "minimum_nonregular_ratio_squared": str(minimum_nonregular),
            "minimum_neither_ratio_squared": str(minimum_neither),
        }
    return records


def category_bounds() -> dict[int, dict[str, tuple[Fraction, bool, int]]]:
    """Map R/O/N to (deficit lower bound, strictness, singleton copies)."""
    return {
        2: {
            "R": (Fraction(2, 11), False, 2),
            "O": (Fraction(1, 4), True, 1),
            "N": (Fraction(4, 11), False, 0),
        },
        3: {
            "R": (Fraction(24, 25), True, 2),
            "O": (Fraction(11, 10), True, 1),
            "N": (Fraction(5, 4), True, 0),
        },
        4: {
            "R": (Fraction(19, 10), True, 2),
            "O": (Fraction(2), True, 1),
            "N": (Fraction(9, 4), True, 0),
        },
        5: {
            "R": (Fraction(23, 8), True, 2),
            "O": (Fraction(3), True, 1),
            "N": (Fraction(3), True, 0),
        },
    }


def assignment_is_deficit_compatible(values: list[tuple[Fraction, bool, int]]) -> bool:
    lower_sum = sum((value[0] for value in values), Fraction(0))
    any_strict = any(value[1] for value in values)
    if lower_sum < 6:
        return True
    if lower_sum == 6 and not any_strict:
        return True
    return False


def check_pattern_assignments() -> dict[str, object]:
    bounds = category_bounds()
    expected = {
        (4, 3, 3, 3, 3): (10, 8, 8),
        (4, 4, 3, 3, 2): (2, 9, 7),
        (5, 3, 3, 3, 2): (1, 10, 6),
    }
    records: dict[str, object] = {}
    for pattern, (expected_survivors, expected_min_singletons, expected_max_r) in expected.items():
        survivors: list[tuple[tuple[str, ...], Fraction, int]] = []
        for categories in itertools.product(("R", "O", "N"), repeat=COORDINATES):
            values = [bounds[length][category] for length, category in zip(pattern, categories)]
            if assignment_is_deficit_compatible(values):
                lower_sum = sum((value[0] for value in values), Fraction(0))
                singleton_copies = sum(value[2] for value in values)
                survivors.append((categories, lower_sum, singleton_copies))
        require(len(survivors) == expected_survivors, f"unexpected survivors for {pattern}: {survivors}")
        minimum_singletons = min(item[2] for item in survivors)
        maximum_r = TOTAL_GAPS - minimum_singletons
        require(minimum_singletons == expected_min_singletons, f"wrong singleton minimum for {pattern}")
        require(maximum_r == expected_max_r, f"wrong R maximum for {pattern}")
        require(1 <= maximum_r <= 8, f"compression range failed for {pattern}")

        internal_minimum = sum(max(0, length - 2) for length in pattern)
        require(internal_minimum > 0, f"R positivity not forced for {pattern}")
        records[str(pattern)] = {
            "category_assignments_checked": 3**COORDINATES,
            "deficit_compatible_assignments": len(survivors),
            "minimum_singleton_copies": minimum_singletons,
            "maximum_non_singleton_copies": maximum_r,
            "forced_internal_non_singleton_copies": internal_minimum,
        }
    return records


def audit() -> dict[str, object]:
    require(M == 11, f"audit is bound to eleven labels, got {M}")
    require(PROOF.is_file(), f"proof snapshot missing: {PROOF}")
    proof_hash = sha256(PROOF)
    require(proof_hash == EXPECTED_PROOF_SHA256, f"proof hash mismatch: {proof_hash}")

    tree = ast.parse(CODE.read_text(encoding="utf-8"), filename=str(CODE))
    removable_nodes = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(removable_nodes == 0, f"optimization-removable check nodes found: {removable_nodes}")

    return {
        "status": "PASS",
        "scope": "exact finite t=16 arithmetic/enumeration only; singleton compression remains a human proof",
        "proof_sha256": proof_hash,
        "code_sha256": sha256(CODE),
        "ast_assert_nodes": removable_nodes,
        "chain_costs": check_chain_costs_and_c7(),
        "partitions": check_partitions(),
        "endpoint_penalties": check_endpoint_penalties(),
        "patterns": check_pattern_assignments(),
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
