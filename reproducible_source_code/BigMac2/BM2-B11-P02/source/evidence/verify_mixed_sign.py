#!/usr/bin/env python3
"""Exact finite regression checks for mixed_sign_obstructions.md.

The Markdown level-table arguments are the proofs.  This script uses exact
integer sorting to catch transcription and boundary-case errors; finite
coverage is not represented as an infinite proof.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE_SHA256 = "b7828252e7882bc261940004f89d319fcf4d7f3f2e6655b0674f6e3def45c0d5"


def phi(word: str, u: int, d: int, tie: str) -> str:
    level = 0
    atoms: list[tuple[int, int, str]] = []
    for position, letter in enumerate(word):
        atoms.append((level, position, letter))
        level += u if letter == "U" else d
    direction = 1 if tie == "L" else -1
    atoms.sort(key=lambda atom: (atom[0], direction * atom[1]))
    return "".join(letter for _, _, letter in atoms)


def p(m: int, n: int) -> str:
    return "U" * m + "D" * m + "U" * n + "D" * n


def z(m: int, n: int) -> str:
    return "UD" * m + "U" * n + "D" * n


def y(m: int, n: int) -> str:
    return "U" * m + "D" * m + "UD" * n


def right_height_formula(m: int, n: int) -> str:
    if n <= m:
        return "UU" + "DU" * (2 * n - 2) + "DD" + "UD" * (m - n)
    return "UU" + "DU" * (2 * m - 1) + "DD" + "UD" * (n - m - 1)


def left_height_formula(m: int, n: int) -> str:
    if m <= n:
        return "UU" + "UD" * (2 * m - 2) + "D" + "UD" * (n - m) + "D"
    return "UU" + "UD" * (2 * n - 2) + "UDD" + "UD" * (m - n - 1) + "D"


def main() -> None:
    source_digest = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
    assert source_digest == EXPECTED_SOURCE_SHA256

    formula_pairs = 0
    right_probe = re.compile(r"^UU(?:(?:DU){2})*DD(?:UD)*$")
    left_probe = re.compile(r"^UU(?:UD)(?:UDUD)*UDD(?:UD)*D$")
    for m in range(1, 81):
        for n in range(1, 81):
            right_output = phi(p(m, n), 1, -1, "R")
            left_output = phi(p(m, n), 1, -1, "L")
            assert right_output == right_height_formula(m, n)
            assert left_output == left_height_formula(m, n)
            assert bool(right_probe.fullmatch(right_output)) == (n <= m)
            if m >= 2 and n >= 2:
                assert bool(left_probe.fullmatch(left_output)) == (m <= n)
            formula_pairs += 1

    probe_pairs = 0
    for m in range(1, 161):
        for n in range(1, 161):
            assert phi(z(m, n), 1, -2, "L").endswith("UD") == (n >= m + 2)
            assert phi(z(m, n), 1, -2, "R").endswith("UUD") == (n >= m + 4)
            assert phi(y(m, n), 2, -1, "L").endswith("DUDD") == (n >= m + 1)
            assert phi(y(m, n), 2, -1, "R").endswith("DUDUDDD") == (n >= m + 3)
            probe_pairs += 1

    print(
        {
            "source_sha256": source_digest,
            "height_formula_pairs": formula_pairs,
            "suffix_probe_pairs": probe_pairs,
            "integer_sorting_only": True,
        }
    )


if __name__ == "__main__":
    main()
