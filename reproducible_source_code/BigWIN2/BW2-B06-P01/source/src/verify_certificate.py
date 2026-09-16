#!/usr/bin/env python3
"""Independent standard-library verifier for the M_3(F_2) certificate.

The implementation deliberately does not import discovery code, NumPy, or
Numba.  Matrix products use row/column bit-parity rather than the discovery
program's triple loop.  Every claim is reconstructed from the JSON input.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from array import array
from pathlib import Path
from typing import Iterable


IDENTITY_MATRIX = 273  # bits 0, 4, and 8


def fail(message: str) -> "None":
    raise ValueError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def matrix_product(a: int, b: int) -> int:
    """Multiply row-major nine-bit matrices using parity of row/column masks."""
    result = 0
    columns = [
        ((b >> j) & 1) | (((b >> (3 + j)) & 1) << 1) | (((b >> (6 + j)) & 1) << 2)
        for j in range(3)
    ]
    for i in range(3):
        row = (a >> (3 * i)) & 7
        for j in range(3):
            result |= ((row & columns[j]).bit_count() & 1) << (3 * i + j)
    return result


def multiplication_table() -> list[array]:
    return [array("H", (matrix_product(a, b) for b in range(512))) for a in range(512)]


def all_words_through(degree: int) -> list[str]:
    words = [""]
    for length in range(1, degree + 1):
        words.extend("".join(letters) for letters in itertools.product("XY", repeat=length))
    return words


def word_values(words: Iterable[str], a: int, b: int,
                table: list[array]) -> dict[str, int]:
    ordered = sorted(set(words) | {""}, key=lambda word: (len(word), word))
    values = {"": IDENTITY_MATRIX}
    for word in ordered[1:]:
        require(word[:-1] in values, "word set is not prefix closed")
        right = a if word[-1] == "X" else b
        values[word] = table[values[word[:-1]]][right]
    return values


def prefix_closure(words: Iterable[str]) -> set[str]:
    return {word[:length] for word in words for length in range(len(word) + 1)}


def row_rank(rows: Iterable[int]) -> int:
    """GF(2) row rank using least-set-bit pivots."""
    basis: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = (row & -row).bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return len(basis)


def evaluation_rows(words: list[str], pairs: list[tuple[int, int]],
                    table: list[array]) -> list[int]:
    rows: list[int] = []
    for a, b in pairs:
        values = word_values(prefix_closure(words), a, b, table)
        for entry in range(9):
            row = 0
            for column, word in enumerate(words):
                row |= ((values[word] >> entry) & 1) << column
            rows.append(row)
    return rows


def validate_certificate(data: object) -> dict:
    require(isinstance(data, dict), "top level must be an object")
    required = {"schema", "claim", "field", "matrix_encoding", "word_convention",
                "identity", "lower_bound", "exhaustive_domain"}
    require(required <= set(data), "missing top-level field")
    require(data["schema"] == "m3f2-two-variable-pi-minimum-v1", "unknown schema")
    require(data["field"] == "F_2", "wrong field")
    require(data["claim"] == {"least_degree": 7, "lower_degree": 6}, "wrong claim")
    require(data["matrix_encoding"] == {
        "integer_range": [0, 511],
        "bit_index": "3*row+column",
        "row_and_column_indices": [0, 1, 2],
    }, "wrong matrix encoding")
    require(data["word_convention"] == {
        "alphabet": ["X", "Y"],
        "multiplication": "left to right",
        "empty_word": "I_3",
    }, "wrong word convention")
    require(data["exhaustive_domain"] == {
        "ordered_pairs": 262144,
        "enumeration": "A=0,...,511 outer; B=0,...,511 inner",
    }, "wrong exhaustive domain")

    identity = data["identity"]
    support = identity.get("support")
    require(isinstance(support, list) and support, "identity support must be nonempty")
    require(all(isinstance(word, str) and word and set(word) <= {"X", "Y"}
                for word in support), "malformed identity word")
    require(len(support) == len(set(support)) == identity.get("support_size") == 18,
            "identity support size/uniqueness mismatch")
    require(max(map(len, support)) == identity.get("degree") == 7,
            "identity degree mismatch")
    require(identity.get("coefficient") == 1, "nonunit support coefficient")

    lower = data["lower_bound"]
    require(lower.get("degree_6_columns") == 127, "wrong degree-six column count")
    require(lower.get("degree_6_minor_rank") == 127, "wrong claimed minor rank")
    raw_pairs = lower.get("witness_pairs")
    require(isinstance(raw_pairs, list) and len(raw_pairs) == 15, "need 15 witness pairs")
    require(all(isinstance(pair, list) and len(pair) == 2 and
                all(isinstance(x, int) and 0 <= x < 512 for x in pair)
                for pair in raw_pairs), "malformed witness pair")
    pairs = [tuple(pair) for pair in raw_pairs]
    require(len(set(pairs)) == len(pairs), "duplicate witness pair")
    minor = lower.get("selected_minor_rows")
    require(isinstance(minor, list) and len(minor) == 127, "minor must have 127 rows")
    coordinates = []
    for item in minor:
        require(isinstance(item, dict) and set(item) == {"entry", "pair_index"},
                "malformed minor coordinate")
        coordinate = (item["pair_index"], item["entry"])
        require(isinstance(coordinate[0], int) and 0 <= coordinate[0] < len(pairs),
                "minor pair index out of range")
        require(isinstance(coordinate[1], int) and 0 <= coordinate[1] < 9,
                "minor entry out of range")
        coordinates.append(coordinate)
    require(len(set(coordinates)) == 127, "duplicate minor row")
    return {"support": support, "pairs": pairs, "coordinates": coordinates,
            "rank_claims": lower.get("rank_by_degree")}


def verify(path: Path) -> dict:
    raw = path.read_bytes()
    data = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    parsed = validate_certificate(data)
    table = multiplication_table()

    support = parsed["support"]
    needed = prefix_closure(support)
    violations = 0
    for a in range(512):
        for b in range(512):
            values = word_values(needed, a, b, table)
            total = 0
            for word in support:
                total ^= values[word]
            if total:
                violations += 1
                fail(f"identity fails at encoded pair ({a}, {b}) with value {total}")

    pairs = parsed["pairs"]
    words_6 = all_words_through(6)
    rows_6 = evaluation_rows(words_6, pairs, table)
    minor_rows = [rows_6[9 * pair_index + entry]
                  for pair_index, entry in parsed["coordinates"]]
    minor_rank = row_rank(minor_rows)
    require(minor_rank == 127, f"degree-six minor rank is {minor_rank}, not 127")

    recomputed_ranks = []
    for degree in range(7):
        words = all_words_through(degree)
        rank = row_rank(evaluation_rows(words, pairs, table))
        recomputed_ranks.append({"degree": degree, "columns": len(words), "rank": rank})
        require(rank == len(words), f"degree {degree} does not have full column rank")
    require(recomputed_ranks == parsed["rank_claims"], "serialized rank claims mismatch")

    code_raw = Path(__file__).read_bytes()
    return {
        "status": "PASS",
        "claim": "least degree = 7",
        "ordered_pairs_checked": 262144,
        "identity_violations": violations,
        "degree_6_columns": 127,
        "degree_6_minor_rank": minor_rank,
        "ranks_0_through_6": [item["rank"] for item in recomputed_ranks],
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(code_raw).hexdigest(),
    }


def main() -> None:
    require(len(sys.argv) == 2, "usage: verify_certificate.py CERTIFICATE.json")
    result = verify(Path(sys.argv[1]))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        raise SystemExit(1)
