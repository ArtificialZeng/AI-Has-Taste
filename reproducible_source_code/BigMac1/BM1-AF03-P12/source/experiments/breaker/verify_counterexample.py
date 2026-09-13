#!/usr/bin/env python3
"""Fail-closed independent verifier for a plactic membership-change witness.

This file imports no discovery module.  To reduce common-mode error, it obtains
the row-insertion tableau P(word) by *column insertion of the reversed word*,
not by the discovery program's row-bumping implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


EXPECTED_KEYS = {
    "schema_version",
    "claim",
    "u",
    "w",
    "k_a",
    "k_b",
    "membership_a",
    "membership_b",
}


def fail(message: str) -> "NoReturn":  # type: ignore[name-defined]
    raise ValueError(message)


def checked_word(value: Any, name: str) -> tuple[int, ...]:
    if not isinstance(value, list):
        fail(f"{name} must be a JSON list")
    if any(type(x) is not int or x <= 0 for x in value):
        fail(f"{name} must contain only positive JSON integers")
    return tuple(value)


def column_insert(tableau: list[list[int]], x: int) -> None:
    column = 0
    while True:
        first_ge: int | None = None
        for row in range(len(tableau)):
            if column >= len(tableau[row]):
                break
            if tableau[row][column] >= x:
                first_ge = row
                break
        if first_ge is None:
            row = 0
            while row < len(tableau) and column < len(tableau[row]):
                row += 1
            if row == len(tableau):
                if column != 0:
                    fail("internal column-insertion shape error")
                tableau.append([x])
            else:
                if len(tableau[row]) != column:
                    fail("internal nonpartition shape")
                tableau[row].append(x)
            return
        tableau[first_ge][column], x = x, tableau[first_ge][column]
        column += 1


def insertion_tableau_via_reverse_columns(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    tableau: list[list[int]] = []
    for x in reversed(word):
        column_insert(tableau, x)
    result = tuple(tuple(row) for row in tableau)
    for row in result:
        if any(a > b for a, b in zip(row, row[1:])):
            fail("internal row monotonicity failure")
    for i in range(1, len(result)):
        if len(result[i]) > len(result[i - 1]):
            fail("internal partition-shape failure")
        if any(result[i - 1][j] >= result[i][j] for j in range(len(result[i]))):
            fail("internal column strictness failure")
    return result


def centralizes(u: tuple[int, ...], w: tuple[int, ...], exponent: int) -> tuple[bool, tuple, tuple]:
    power = u * exponent
    left = insertion_tableau_via_reverse_columns(power + w)
    right = insertion_tableau_via_reverse_columns(w + power)
    return left == right, left, right


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail(f"unreadable certificate: {error}")
    if type(data) is not dict or set(data) != EXPECTED_KEYS:
        fail("certificate keys are missing or unexpected")
    if data["schema_version"] != 1 or data["claim"] != "membership_changes":
        fail("unsupported schema or claim")
    u = checked_word(data["u"], "u")
    w = checked_word(data["w"], "w")
    if set(u) != {1, 2, 3}:
        fail("u is not 3-packed")
    for name in ("k_a", "k_b"):
        if type(data[name]) is not int or data[name] < 3:
            fail(f"{name} must be an integer at least 3")
    if data["k_a"] == data["k_b"]:
        fail("the two exponents must differ")
    for name in ("membership_a", "membership_b"):
        if type(data[name]) is not bool:
            fail(f"{name} must be Boolean")
    if data["membership_a"] == data["membership_b"]:
        fail("claimed memberships do not differ")

    actual_a, left_a, right_a = centralizes(u, w, data["k_a"])
    actual_b, left_b, right_b = centralizes(u, w, data["k_b"])
    if actual_a != data["membership_a"] or actual_b != data["membership_b"]:
        fail("recomputed membership contradicts certificate")
    if actual_a == actual_b:
        fail("recomputed memberships do not change")
    return {
        "u": list(u),
        "w": list(w),
        "k_a": data["k_a"],
        "k_b": data["k_b"],
        "membership_a": actual_a,
        "membership_b": actual_b,
        "left_a": left_a,
        "right_a": right_a,
        "left_b": left_b,
        "right_b": right_b,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except ValueError as error:
        print(f"VERIFY_REJECTED reason={error}")
        return 1
    print(
        "VERIFY_OK"
        f" input_sha256={sha256(args.certificate)}"
        f" verifier_sha256={sha256(Path(__file__))}"
        f" k_a={result['k_a']} membership_a={str(result['membership_a']).lower()}"
        f" k_b={result['k_b']} membership_b={str(result['membership_b']).lower()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
