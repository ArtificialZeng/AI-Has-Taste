#!/usr/bin/env python3
"""Independent fail-closed exact audit of finite t=18 proof components.

This checker imports no project t=18 verifier, manifest, runner, or discovery
artifact.  It checks the exact chain-cost arithmetic, all 88 bounded
partitions, every endpoint tuple behind Tables (13)--(15), all 3^5 loss
assignments for each of the eight patterns, the symbolic basis coefficients
in (21), and every finite orientation case for two nested cuts.

The general real linear-algebra implications (positive definiteness,
Sherman--Morrison, and the antichain conclusion) remain a human proof.  Every
decisive program condition uses an explicit fail-closed exception path.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


M = 11
TOTAL_GAPS = 18
COORDINATES = 5
MAX_CHAIN = 9
EXPECTED_PROOF_SHA256 = "2a50ff367e65652e43e58a44319a86fdff61e04ca41b106260e192c6ee3f20c9"
CODE = Path(__file__).resolve()
DEFAULT_PROOF = CODE.parents[1] / "proof" / "t18_branch.md"


class AuditFailure(Exception):
    """A malformed setup or failed exact check."""


def fail(message: str) -> NoReturn:
    raise AuditFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chain_costs() -> tuple[Fraction, ...]:
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
        Fraction(683, 100),
    )


def check_costs() -> dict[str, object]:
    values = chain_costs()
    increments = tuple(values[index] - values[index - 1] for index in range(1, len(values)))
    expected = (
        Fraction(0),
        Fraction(2, 11),
        Fraction(214, 275),
        Fraction(47, 50),
        Fraction(39, 40),
        Fraction(197, 200),
        Fraction(99, 100),
        Fraction(99, 100),
        Fraction(99, 100),
    )
    require(increments == expected, f"wrong cost increments: {increments}")
    require(
        all(increments[index] <= increments[index + 1] for index in range(len(increments) - 1)),
        f"cost sequence is not discretely convex: {increments}",
    )
    c9_difference = 917**8 - 10 * 683**8
    require(c9_difference == 26432594300827948436631 > 0, f"wrong c9 comparison: {c9_difference}")
    return {
        "costs": [str(value) for value in values],
        "increments": [str(value) for value in increments],
        "c9_power_difference": c9_difference,
    }


def check_partitions() -> dict[str, object]:
    values = chain_costs()
    partitions: list[tuple[tuple[int, ...], Fraction]] = []
    for ascending in itertools.combinations_with_replacement(range(MAX_CHAIN + 1), COORDINATES):
        if sum(ascending) == TOTAL_GAPS:
            partition = tuple(reversed(ascending))
            value = sum((values[length] for length in partition), Fraction(0))
            partitions.append((partition, value))
    require(len(partitions) == 88, f"expected 88 bounded partitions, got {len(partitions)}")
    require(len({partition for partition, _ in partitions}) == 88, "duplicate partition generated")
    require(not any(value == 8 for _, value in partitions), "unhandled cost-eight partition")
    survivors = [(partition, value) for partition, value in partitions if value <= 8]
    expected = {
        (4, 4, 4, 3, 3): Fraction(381, 50),
        (5, 4, 3, 3, 3): Fraction(1531, 200),
        (6, 3, 3, 3, 3): Fraction(77, 10),
        (4, 4, 4, 4, 2): Fraction(428, 55),
        (5, 4, 4, 3, 2): Fraction(17197, 2200),
        (5, 5, 3, 3, 2): Fraction(8637, 1100),
        (6, 4, 3, 3, 2): Fraction(2162, 275),
        (7, 3, 3, 3, 2): Fraction(8703, 1100),
    }
    require(dict(survivors) == expected, f"wrong survivor list: {survivors}")
    eliminated = [(partition, value) for partition, value in partitions if value > 8]
    minimum_eliminated = min(eliminated, key=lambda item: item[1])
    require(
        minimum_eliminated == ((5, 5, 4, 2, 2), Fraction(1763, 220)),
        f"wrong least-cost eliminated partition: {minimum_eliminated}",
    )
    boundary_checks = {
        "minimum_one": Fraction(23, 8) + 3 * Fraction(19, 10) == Fraction(343, 40) > 8,
        "minimum_zero": 2 * Fraction(23, 8) + 2 * Fraction(19, 10) == Fraction(191, 20) > 8,
    }
    require(all(boundary_checks.values()), f"minimum-one/zero boundary failed: {boundary_checks}")
    return {
        "partitions_checked": len(partitions),
        "survivors": {str(partition): str(value) for partition, value in survivors},
        "minimum_eliminated": [str(minimum_eliminated[0]), str(minimum_eliminated[1])],
        "boundary_checks": boundary_checks,
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
    require(n >= 1, "chain length must be at least two")
    require(Fraction(0) <= target < 2 * n, f"invalid endpoint target: {target}")
    threshold = (target / (2 * n - target)) ** (2 * n)
    if strict:
        return ratio_squared > threshold
    return ratio_squared >= threshold


def endpoint_specs() -> dict[int, dict[int, tuple[Fraction, bool]]]:
    return {
        2: {0: (Fraction(2, 11), False), 1: (Fraction(1, 4), True), 2: (Fraction(4, 11), False)},
        3: {0: (Fraction(24, 25), True), 1: (Fraction(111, 100), True), 2: (Fraction(5, 4), True)},
        4: {0: (Fraction(19, 10), True), 1: (Fraction(207, 100), True), 2: (Fraction(9, 4), True)},
        5: {0: (Fraction(23, 8), True), 1: (Fraction(153, 50), True), 2: (Fraction(13, 4), True)},
        6: {0: (Fraction(193, 50), True), 1: (Fraction(81, 20), True), 2: (Fraction(17, 4), True)},
        7: {0: (Fraction(97, 20), True), 1: (Fraction(101, 20), True), 2: (Fraction(21, 4), True)},
    }


def endpoint_loss(sizes: tuple[int, ...]) -> int:
    singleton_copies = int(sizes[0] == 1) + int(sizes[-1] == M - 1)
    return 2 - singleton_copies


def check_endpoint_tables() -> dict[str, object]:
    specs = endpoint_specs()
    expected_counts = {2: 45, 3: 120, 4: 210, 5: 252, 6: 210, 7: 120}
    records: dict[str, object] = {}
    for length in range(2, 8):
        counts = {"all": 0, "loss0": 0, "loss1": 0, "loss2": 0}
        minimum_nonregular: Fraction | None = None
        minimum_neither: Fraction | None = None
        for sizes in itertools.combinations(range(1, M), length):
            counts["all"] += 1
            loss = endpoint_loss(sizes)
            require(loss in (0, 1, 2), f"invalid endpoint loss: {sizes}")
            counts[f"loss{loss}"] += 1
            ratio = endpoint_ratio_squared(sizes[0], sizes[-1])

            general_target, general_strict = specs[length][0]
            require(
                endpoint_bound_implies(ratio, length, general_target, strict=general_strict),
                f"general endpoint bound failed: length={length}, sizes={sizes}",
            )
            if loss >= 1:
                minimum_nonregular = ratio if minimum_nonregular is None else min(minimum_nonregular, ratio)
                target, strict = specs[length][1]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"middle endpoint bound failed: length={length}, sizes={sizes}",
                )
            if loss == 2:
                minimum_neither = ratio if minimum_neither is None else min(minimum_neither, ratio)
                target, strict = specs[length][2]
                require(
                    endpoint_bound_implies(ratio, length, target, strict=strict),
                    f"two-loss endpoint bound failed: length={length}, sizes={sizes}",
                )

        require(counts["all"] == expected_counts[length], f"wrong tuple total for length {length}")
        require(minimum_nonregular == Fraction(1, 45), f"wrong nonregular ratio minimum at {length}")
        require(minimum_neither == Fraction(4, 81), f"wrong neither ratio minimum at {length}")
        records[str(length)] = {
            "counts": counts,
            "minimum_nonregular_ratio_squared": str(minimum_nonregular),
            "minimum_neither_ratio_squared": str(minimum_neither),
        }

    middle_differences = (
        289**4 - 45 * 111**4,
        131**6 - 45 * 69**6,
        247**8 - 45 * 153**8,
        119**10 - 45 * 81**10,
        139**12 - 45 * 101**12,
    )
    expected_middle = (
        144440596,
        197595805636,
        341257329895839316,
        22373433354250690756,
        1313742681350448050257876,
    )
    require(middle_differences == expected_middle, f"Table (14) mismatch: {middle_differences}")
    require(all(value > 0 for value in middle_differences), "nonpositive Table (14) comparison")

    last_differences = (
        4 * 11**4 - 81 * 5**4,
        4 * 5**6 - 81 * 3**6,
        4 * 19**8 - 81 * 13**8,
        4 * 23**10 - 81 * 17**10,
        4 * 9**12 - 81 * 7**12,
    )
    expected_last = (7939, 3451, 1860063763, 2410538918227, 8573882643)
    require(last_differences == expected_last, f"Table (15) mismatch: {last_differences}")
    require(all(value > 0 for value in last_differences), "nonpositive Table (15) comparison")

    records["table14_differences"] = list(middle_differences)
    records["table15_differences"] = list(last_differences)
    return records


def loss_bounds() -> dict[int, dict[int, tuple[Fraction, bool]]]:
    return endpoint_specs()


def compatible_with_budget(values: list[tuple[Fraction, bool]]) -> bool:
    lower_sum = sum((value for value, _ in values), Fraction(0))
    any_strict = any(strict for _, strict in values)
    if lower_sum < 8:
        return True
    if lower_sum == 8 and not any_strict:
        return True
    return False


def check_loss_minima() -> dict[str, object]:
    patterns = {
        "A": (4, 4, 4, 3, 3),
        "B": (5, 4, 3, 3, 3),
        "C": (6, 3, 3, 3, 3),
        "D": (4, 4, 4, 4, 2),
        "E": (5, 4, 4, 3, 2),
        "F": (5, 5, 3, 3, 2),
        "G": (6, 4, 3, 3, 2),
        "H": (7, 3, 3, 3, 2),
    }
    expected = {
        "A": (Fraction(381, 50), Fraction(791, 100), Fraction(403, 50), 2, 8),
        "B": (Fraction(1531, 200), Fraction(1589, 200), Fraction(1619, 200), 2, 8),
        "C": (Fraction(77, 10), Fraction(799, 100), Fraction(407, 50), 2, 8),
        "D": (Fraction(428, 55), Fraction(438, 55), Fraction(8947, 1100), 2, 8),
        "E": (Fraction(17197, 2200), Fraction(17597, 2200), Fraction(17927, 2200), 2, 8),
        "F": (Fraction(8637, 1100), Fraction(8837, 1100), Fraction(4501, 550), 1, 9),
        "G": (Fraction(2162, 275), Fraction(2212, 275), Fraction(9013, 1100), 1, 9),
        "H": (Fraction(8703, 1100), Fraction(8903, 1100), Fraction(2267, 275), 1, 9),
    }
    bounds = loss_bounds()
    records: dict[str, object] = {}
    for label, pattern in patterns.items():
        assignments: list[tuple[int, Fraction, tuple[int, ...], bool]] = []
        for losses in itertools.product((0, 1, 2), repeat=COORDINATES):
            values = [bounds[length][loss] for length, loss in zip(pattern, losses)]
            lower_sum = sum((value for value, _ in values), Fraction(0))
            strict = any(flag for _, flag in values)
            assignments.append((sum(losses), lower_sum, losses, strict))
        require(len(assignments) == 3**COORDINATES, f"wrong assignment count for {label}")
        minima = []
        for threshold in (0, 2, 3):
            candidates = [item for item in assignments if item[0] >= threshold]
            minima.append(min(item[1] for item in candidates))
        expected_general, expected_two, expected_three, expected_max_loss, expected_singletons = expected[label]
        require(tuple(minima) == (expected_general, expected_two, expected_three), f"Table (16) mismatch for {label}: {minima}")

        compatible = []
        equality_eight = 0
        for total_loss, lower_sum, losses, strict in assignments:
            if lower_sum == 8:
                equality_eight += 1
            if compatible_with_budget([(lower_sum, strict)]):
                compatible.append((total_loss, lower_sum, losses))
        maximum_loss = max(item[0] for item in compatible)
        singleton_minimum = 10 - maximum_loss
        require(maximum_loss == expected_max_loss, f"wrong maximum loss for {label}")
        require(singleton_minimum == expected_singletons, f"wrong singleton minimum for {label}")
        records[label] = {
            "pattern": list(pattern),
            "assignments_checked": len(assignments),
            "general_minimum": str(minima[0]),
            "loss_at_least_2_minimum": str(minima[1]),
            "loss_at_least_3_minimum": str(minima[2]),
            "compatible_assignments": len(compatible),
            "maximum_compatible_loss": maximum_loss,
            "minimum_singleton_copies": singleton_minimum,
            "r_range_from_endpoint_count": [TOTAL_GAPS - 10, TOTAL_GAPS - singleton_minimum],
            "rational_sum_equal_to_8_cases": equality_eight,
        }
    return records


def outer(vector: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(left * right for right in vector) for left in vector)


def check_basis_coefficients() -> dict[str, object]:
    """Check the symbolic coefficients behind D_p+c_p J for every p."""
    coefficient_matrices_checked = 0
    for p in range(M):
        w = tuple(label for label in range(M) if label != p)
        position = {label: index for index, label in enumerate(w)}
        coordinates: dict[int, tuple[int, ...]] = {}
        for label in range(M):
            if label == p:
                coordinates[label] = (-1,) * (M - 1)
            else:
                coordinates[label] = tuple(int(index == position[label]) for index in range(M - 1))
        summed = tuple(sum(coordinates[label][index] for label in range(M)) for index in range(M - 1))
        require(summed == (0,) * (M - 1), f"s_p basis relation failed for p={p}")
        for label in range(M):
            matrix = outer(coordinates[label])
            coefficient_matrices_checked += 1
            for row in range(M - 1):
                for column in range(M - 1):
                    if label == p:
                        expected = 1
                    else:
                        expected = int(row == column == position[label])
                    require(matrix[row][column] == expected, f"basis coefficient failed: p={p}, label={label}")
    require(coefficient_matrices_checked == M * M, "wrong symbolic coefficient count")
    return {
        "reference_labels_checked": M,
        "symbolic_coefficient_matrices_checked": coefficient_matrices_checked,
        "identity": "sum c_r s_r s_r^T has basis matrix D_p+c_p J",
    }


def orient_away(mask: int, reference: int, full: int) -> int:
    if mask & (1 << reference):
        return full ^ mask
    return mask


def check_non_singleton_orientations() -> dict[str, object]:
    full = (1 << M) - 1
    cut_reference_pairs = 0
    for mask in range(1, full):
        size = mask.bit_count()
        if min(size, M - size) < 2:
            continue
        for reference in range(M):
            oriented = orient_away(mask, reference, full)
            cut_reference_pairs += 1
            require(not oriented & (1 << reference), "oriented block contains reference")
            require(2 <= oriented.bit_count() <= M - 2, "oriented non-singleton size outside [2,9]")
    require(cut_reference_pairs == 2024 * M, f"wrong non-singleton orientation count: {cut_reference_pairs}")
    return {
        "oriented_cut_representatives": 2024,
        "reference_cases_per_representative": M,
        "cut_reference_pairs_checked": cut_reference_pairs,
    }


def check_nested_cut_trichotomy() -> dict[str, object]:
    """Enumerate P strict-subset Q and all three reference positions."""
    full = (1 << M) - 1
    ternary_assignments = 3**M
    nested_pairs = 0
    reference_cases = 0
    case_counts = {"outside_both": 0, "inside_both": 0, "between": 0}
    for code in range(ternary_assignments):
        value = code
        p_mask = 0
        q_mask = 0
        for label in range(M):
            state = value % 3
            value //= 3
            if state == 2:
                p_mask |= 1 << label
                q_mask |= 1 << label
            elif state == 1:
                q_mask |= 1 << label
        if p_mask == 0 or q_mask == full or p_mask == q_mask:
            continue
        nested_pairs += 1
        require(p_mask & ~q_mask == 0, "ternary encoding lost nesting")
        for reference in range(M):
            reference_cases += 1
            up = orient_away(p_mask, reference, full)
            uq = orient_away(q_mask, reference, full)
            in_p = bool(p_mask & (1 << reference))
            in_q = bool(q_mask & (1 << reference))
            if not in_q:
                case_counts["outside_both"] += 1
                require(up == p_mask and uq == q_mask and up != uq and up & ~uq == 0, "outside nesting failed")
            elif in_p:
                case_counts["inside_both"] += 1
                require(up == (full ^ p_mask) and uq == (full ^ q_mask), "inside orientation failed")
                require(up != uq and uq & ~up == 0, "complement nesting failed")
            else:
                case_counts["between"] += 1
                require(up == p_mask and uq == (full ^ q_mask), "between orientation failed")
                require(up & uq == 0, "between blocks are not disjoint")
    require(nested_pairs > 0 and reference_cases == nested_pairs * M, "nested-pair count failure")
    require(sum(case_counts.values()) == reference_cases, "reference trichotomy incomplete")
    return {
        "ternary_assignments_scanned": ternary_assignments,
        "strict_nontrivial_nested_pairs": nested_pairs,
        "reference_cases_checked": reference_cases,
        "case_counts": case_counts,
    }


def audit(proof: Path) -> dict[str, object]:
    require((M, TOTAL_GAPS, COORDINATES, MAX_CHAIN) == (11, 18, 5, 9), "audit constants changed")
    require(proof.is_file(), f"missing proof target: {proof}")
    proof_hash = sha256(proof)
    require(proof_hash == EXPECTED_PROOF_SHA256, f"proof hash mismatch: {proof_hash}")
    tree = ast.parse(CODE.read_text(encoding="utf-8"), filename=str(CODE))
    removable_nodes = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
    require(removable_nodes == 0, f"optimization-removable check nodes: {removable_nodes}")
    return {
        "status": "PASS",
        "scope": "exact finite t=18 arithmetic, loss, basis-coefficient, and nested-cut orientation checks; general R=10 linear algebra remains human",
        "proof_path": str(proof.resolve()),
        "proof_sha256": proof_hash,
        "code_sha256": sha256(CODE),
        "ast_assert_nodes": removable_nodes,
        "chain_costs": check_costs(),
        "partitions": check_partitions(),
        "endpoint_tables": check_endpoint_tables(),
        "loss_minima": check_loss_minima(),
        "basis_coefficients": check_basis_coefficients(),
        "non_singleton_orientations": check_non_singleton_orientations(),
        "nested_cut_trichotomy": check_nested_cut_trichotomy(),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", type=Path, default=DEFAULT_PROOF, help="proof snapshot to hash-check")
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        result = audit(args.proof)
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
