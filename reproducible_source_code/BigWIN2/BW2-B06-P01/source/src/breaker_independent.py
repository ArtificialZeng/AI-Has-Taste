#!/usr/bin/env python3
"""Independent adversarial rank search using only the Python standard library.

This program uses a pair schedule unrelated to the Builder's schedule and a
row/column parity product unrelated to the Builder's multiplication loop.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from array import array
from pathlib import Path


I3 = 273


def product(a: int, b: int) -> int:
    result = 0
    for row_index in range(3):
        row = (a >> (3 * row_index)) & 7
        for column_index in range(3):
            column = (((b >> column_index) & 1)
                      | (((b >> (column_index + 3)) & 1) << 1)
                      | (((b >> (column_index + 6)) & 1) << 2))
            result |= ((row & column).bit_count() & 1) << (3 * row_index + column_index)
    return result


def make_table() -> list[array]:
    return [array("H", (product(a, b) for b in range(512))) for a in range(512)]


def words(degree: int) -> list[str]:
    answer = [""]
    for length in range(1, degree + 1):
        answer += ["".join(item) for item in itertools.product(("X", "Y"), repeat=length)]
    return answer


def pair_schedule(count: int) -> list[tuple[int, int]]:
    encoded = [((110351 * index + 54321) & ((1 << 18) - 1)) for index in range(count)]
    return [(item >> 9, item & 511) for item in encoded]


def column_vectors(degree: int, pairs: list[tuple[int, int]],
                   table: list[array]) -> tuple[list[str], list[int]]:
    word_list = words(degree)
    columns = [0] * len(word_list)
    for pair_index, (a, b) in enumerate(pairs):
        values = {"": I3}
        for word_index, word in enumerate(word_list):
            if word:
                values[word] = table[values[word[:-1]]][a if word[-1] == "X" else b]
            columns[word_index] |= values[word] << (9 * pair_index)
    return word_list, columns


def rank_relation(columns: list[int]) -> tuple[int, int | None]:
    basis: dict[int, tuple[int, int]] = {}
    for column_index, original in enumerate(columns):
        vector = original
        relation = 1 << column_index
        while vector:
            pivot = (vector & -vector).bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (vector, relation)
                break
            vector ^= basis[pivot][0]
            relation ^= basis[pivot][1]
        else:
            return len(basis), relation
    return len(basis), None


def main() -> None:
    table = make_table()
    pairs = pair_schedule(50)
    ranks = []
    relation_support = None
    for degree in range(8):
        word_list, columns = column_vectors(degree, pairs, table)
        rank, relation = rank_relation(columns)
        ranks.append({"degree": degree, "columns": len(columns), "rank": rank})
        if relation is not None:
            relation_support = [word_list[index] or "1" for index in range(len(word_list))
                                if (relation >> index) & 1]
            break
    report = {
        "status": "PASS" if ranks[-1] == {"degree": 7, "columns": 255, "rank": 207}
                  and relation_support is not None else "FAIL",
        "arithmetic": "exact GF(2), Python standard library",
        "pair_schedule": "z=(110351*i+54321) mod 2^18; A=z>>9; B=z&511",
        "pair_count": 50,
        "ranks": ranks,
        "first_relation_support": relation_support,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path("experiments/breaker_independent.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
