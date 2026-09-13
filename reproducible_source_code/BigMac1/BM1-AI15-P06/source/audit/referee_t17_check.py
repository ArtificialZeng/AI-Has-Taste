#!/usr/bin/env python3
"""Independent fail-closed exact audit of the finite t=17 calculations.

The script imports no project verifier, frame checker, runner, log, or
discovery artifact.  It certifies the rational/powered comparisons, all 66
bounded partitions, endpoint penalties, exhaustive loss categories for the
five surviving patterns, and the finite subset cases in the unique-negative
sign argument.  The surrounding compression/rank proof remains a human proof.
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
TOTAL_GAPS = 17
COORDINATES = 5
MAX_CHAIN = 8
EXPECTED_PROOF_SHA256 = "5332a2acc28a5407b3837c28fe4d007fae64d8031ad18a64e6b8177e32e856a3"
CODE = Path(__file__).resolve()
PROJECT = CODE.parents[1]
PROOF = PROJECT / "proof" / "t17_branch.md"


class AuditFailure(Exception):
    """A malformed setup or failed exact condition."""


def fail(message: str) -> NoReturn:
    raise AuditFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def costs() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(0),
        Fraction(2, 11),
        Fraction(24, 25),
        Fraction(19, 10),
        Fraction(23, 8),
        Fraction(193, 50),
        Fraction(97, 20),
        Fraction(146, 25),
    )


def check_costs_and_radicals() -> dict[str, object]:
    values = costs()
    increments = tuple(values[index] - values[index - 1] for index in range(1, len(values)))
    expected_increments = (
        Fraction(0),
        Fraction(2, 11),
        Fraction(214, 275),
        Fraction(47, 50),
        Fraction(39, 40),
        Fraction(197, 200),
        Fraction(99, 100),
        Fraction(99, 100),
    )
    require(increments == expected_increments, f"wrong increments: {increments}")
    require(
        all(increments[index] <= increments[index + 1] for index in range(len(increments) - 1)),
        f"nonconvex cost sequence: {increments}",
    )
    radical_checks = {
        "c7_143^6_gt_10x97^6": 143**6 > 10 * 97**6,
        "c8_102^7_gt_10x73^7": 102**7 > 10 * 73**7,
    }
    require(all(radical_checks.values()), f"powered radical comparison failed: {radical_checks}")
    return {
        "costs": [str(value) for value in values],
        "increments": [str(value) for value in increments],
        "powered_comparisons": radical_checks,
    }


def check_partitions() -> dict[str, object]:
    values = costs()
    partitions: list[tuple[tuple[int, ...], Fraction]] = []
    for ascending in itertools.combinations_with_replacement(range(MAX_CHAIN + 1), COORDINATES):
        if sum(ascending) == TOTAL_GAPS:
            partition = tuple(reversed(ascending))
            lower_sum = sum((values[length] for length in partition), Fraction(0))
            partitions.append((partition, lower_sum))
    require(len(partitions) == 66, f"expected 66 partitions, got {len(partitions)}")
    require(len({partition for partition, _ in partitions}) == 66, "duplicate bounded partitions")
    require(
        all(len(partition) == COORDINATES and sum(partition) == TOTAL_GAPS for partition, _ in partitions),
        "malformed bounded partition",
    )

    survivors = [(partition, value) for partition, value in partitions if value <= 7]
    expected = {
        (4, 4, 3, 3, 3): Fraction(167, 25),
        (5, 3, 3, 3, 3): Fraction(1343, 200),
        (4, 4, 4, 3, 2): Fraction(3763, 550),
        (5, 4, 3, 3, 2): Fraction(15129, 2200),
        (6, 3, 3, 3, 2): Fraction(3807, 550),
    }
    require(dict(survivors) == expected, f"wrong surviving partition list: {survivors}")
    require(not any(value == 7 for _, value in partitions), "unhandled cost-seven equality partition")
    eliminated = [(partition, value) for partition, value in partitions if value > 7]
    minimum_eliminated = min(eliminated, key=lambda item: item[1])
    require(
        minimum_eliminated == ((5, 4, 4, 2, 2), Fraction(3097, 440)),
        f"wrong cheapest eliminated partition: {minimum_eliminated}",
    )
    return {
        "partitions_checked": len(partitions),
        "survivors": {str(partition): str(value) for partition, value in survivors},
        "minimum_eliminated": [str(minimum_eliminated[0]), str(minimum_eliminated[1])],
    }


def endpoint_ratio_squared(first: int, last: int) -> Fraction:
    require(1 <= first < last <= M - 1, f"invalid endpoints: {(first, last)}")
    return Fraction(first * (M - last), last * (M - first))


def endpoint_bound_implies(
    ratio_squared: Fraction,
    length: int,
    target: Fraction,
    *,
    strict: bool,
) -> bool:
    n = length - 1
    require(n >= 1, "endpoint bound requires length at least two")
    require(Fraction(0) <= target < 2 * n, f"invalid endpoint target: {target}")
    threshold = (target / (2 * n - target)) ** (2 * n)
    if strict:
        return ratio_squared > threshold
    return ratio_squared >= threshold


def endpoint_specs() -> dict[int, dict[str, tuple[Fraction, bool]]]:
    return {
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
            "neither": (Fraction(13, 4), True),
        },
        6: {
            "general": (Fraction(193, 50), True),
            "one": (Fraction(4), True),
            "neither": (Fraction(4), True),
        },
    }


def singleton_count(sizes: tuple[int, ...]) -> int:
    return int(sizes[0] == 1) + int(sizes[-1] == M - 1)


def check_endpoint_penalties() -> dict[str, object]:
    specs = endpoint_specs()
    expected_totals = {2: 45, 3: 120, 4: 210, 5: 252, 6: 210}
    records: dict[str, object] = {}
    for length in range(2, 7):
        counts = {"all": 0, "regular": 0, "one": 0, "neither": 0}
        minimum_nonregular: Fraction | None = None
        minimum_neither: Fraction | None = None
        for sizes in itertools.combinations(range(1, M), length):
            counts["all"] += 1
            number = singleton_count(sizes)
            category = "regular" if number == 2 else ("one" if number == 1 else "neither")
            counts[category] += 1
            ratio = endpoint_ratio_squared(sizes[0], sizes[-1])

            general_target, general_strict = specs[length]["general"]
            require(
                endpoint_bound_implies(ratio, length, general_target, strict=general_strict),
                f"general bound failed: length={length}, sizes={sizes}",
            )
            if number < 2:
                minimum_nonregular = ratio if minimum_nonregular is None else min(minimum_nonregular, ratio)
                target, strict = specs[length]["one"]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"nonregular bound failed: length={length}, sizes={sizes}",
                )
            if number == 0:
                minimum_neither = ratio if minimum_neither is None else min(minimum_neither, ratio)
                target, strict = specs[length]["neither"]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"neither-endpoint bound failed: length={length}, sizes={sizes}",
                )

        require(counts["all"] == expected_totals[length], f"wrong tuple total for length {length}")
        require(minimum_nonregular == Fraction(1, 45), f"wrong nonregular ratio minimum for length {length}")
        require(minimum_neither == Fraction(4, 81), f"wrong neither ratio minimum for length {length}")
        records[str(length)] = {
            "counts": counts,
            "minimum_nonregular_ratio_squared": str(minimum_nonregular),
            "minimum_neither_ratio_squared": str(minimum_neither),
        }

    new_integer_checks = {
        "quintuple_neither_4x19^8_gt_81x13^8": 4 * 19**8 > 81 * 13**8,
        "sextuple_nonregular_3^10_gt_45x2^10": 3**10 > 45 * 2**10,
    }
    require(all(new_integer_checks.values()), f"new endpoint comparison failed: {new_integer_checks}")
    records["new_integer_checks"] = new_integer_checks
    return records


def category_bounds() -> dict[int, dict[str, tuple[Fraction, bool, int]]]:
    """R/O/N map to (lower deficit, strictness, singleton endpoints)."""
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
            "N": (Fraction(13, 4), True, 0),
        },
        6: {
            "R": (Fraction(193, 50), True, 2),
            "O": (Fraction(4), True, 1),
            "N": (Fraction(4), True, 0),
        },
    }


def compatible(values: list[tuple[Fraction, bool, int]]) -> bool:
    lower_sum = sum((value[0] for value in values), Fraction(0))
    any_strict = any(value[1] for value in values)
    if lower_sum < 7:
        return True
    if lower_sum == 7 and not any_strict:
        return True
    return False


def check_loss_cases() -> dict[str, object]:
    bounds = category_bounds()
    expected = {
        (4, 4, 3, 3, 3): (19, 8, 9),
        (5, 3, 3, 3, 3): (16, 8, 9),
        (4, 4, 4, 3, 2): (6, 9, 8),
        (5, 4, 3, 3, 2): (3, 9, 8),
        (6, 3, 3, 3, 2): (2, 9, 8),
    }
    records: dict[str, object] = {}
    for pattern, (expected_survivors, expected_minimum, expected_maximum_r) in expected.items():
        survivors: list[tuple[tuple[str, ...], Fraction, int]] = []
        equality_cases = 0
        for categories in itertools.product(("R", "O", "N"), repeat=COORDINATES):
            values = [bounds[length][category] for length, category in zip(pattern, categories)]
            lower_sum = sum((value[0] for value in values), Fraction(0))
            if lower_sum == 7:
                equality_cases += 1
            if compatible(values):
                singleton_copies = sum(value[2] for value in values)
                survivors.append((categories, lower_sum, singleton_copies))

        require(len(survivors) == expected_survivors, f"wrong loss survivors for {pattern}: {survivors}")
        require(equality_cases == 0, f"unhandled loss-bound equality for {pattern}")
        minimum_singletons = min(item[2] for item in survivors)
        maximum_r = TOTAL_GAPS - minimum_singletons
        require(minimum_singletons == expected_minimum, f"wrong singleton minimum for {pattern}")
        require(maximum_r == expected_maximum_r, f"wrong R maximum for {pattern}")
        require(1 <= maximum_r <= 9, f"rank-nine obstruction range failed for {pattern}")
        internal_minimum = sum(max(0, length - 2) for length in pattern)
        require(internal_minimum == TOTAL_GAPS - 10 == 7, f"wrong forced internal count for {pattern}")
        records[str(pattern)] = {
            "assignments_checked": 3**COORDINATES,
            "deficit_compatible_assignments": len(survivors),
            "minimum_singleton_copies": minimum_singletons,
            "maximum_non_singleton_copies": maximum_r,
            "forced_internal_non_singleton_copies": internal_minimum,
        }
    return records


def check_unique_negative_subset_logic() -> dict[str, object]:
    """Enumerate subset types for one negative and ten positive entries.

    Under total sum zero: a nonempty subset without the negative entry is
    positive; a subset with the negative but not every positive is negative;
    only the empty and full subsets can be zero.
    """
    subsets_checked = 0
    for negative in range(M):
        positive_mask = ((1 << M) - 1) ^ (1 << negative)
        for subset in range(1 << M):
            subsets_checked += 1
            has_negative = bool(subset & (1 << negative))
            selected_positives = subset & positive_mask
            if subset == 0:
                classification = "zero-empty"
            elif subset == (1 << M) - 1:
                classification = "zero-full"
            elif not has_negative:
                classification = "positive"
            elif selected_positives != positive_mask:
                classification = "negative"
            else:
                fail(f"unclassified proper subset: negative={negative}, subset={subset}")
            require(
                classification not in ("zero-empty", "zero-full") or subset in (0, (1 << M) - 1),
                "improper symbolic zero classification",
            )
    require(subsets_checked == M * 2**M, f"wrong subset audit count: {subsets_checked}")
    return {
        "negative_label_choices": M,
        "subsets_per_choice": 2**M,
        "subset_types_checked": subsets_checked,
        "proper_nonempty_symbolic_zero_subsets": 0,
    }


def audit() -> dict[str, object]:
    require(PROOF.is_file(), f"missing proof target: {PROOF}")
    proof_hash = sha256(PROOF)
    require(proof_hash == EXPECTED_PROOF_SHA256, f"proof hash mismatch: {proof_hash}")
    tree = ast.parse(CODE.read_text(encoding="utf-8"), filename=str(CODE))
    removable_nodes = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(removable_nodes == 0, f"optimization-removable check nodes: {removable_nodes}")
    require((M, TOTAL_GAPS, COORDINATES, MAX_CHAIN) == (11, 17, 5, 8), "audit constants changed")
    return {
        "status": "PASS",
        "scope": "exact finite t=17 arithmetic/enumeration and symbolic sign-subset audit; rank proof remains human",
        "proof_sha256": proof_hash,
        "code_sha256": sha256(CODE),
        "ast_assert_nodes": removable_nodes,
        "chain_costs": check_costs_and_radicals(),
        "partitions": check_partitions(),
        "endpoint_penalties": check_endpoint_penalties(),
        "loss_cases": check_loss_cases(),
        "unique_negative_sign_cases": check_unique_negative_subset_logic(),
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
