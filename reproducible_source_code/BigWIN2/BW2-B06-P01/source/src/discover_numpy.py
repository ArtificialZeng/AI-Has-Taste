#!/usr/bin/env python3
"""Exact GF(2) discovery for two-variable identities of M_3(F_2).

This is discovery code.  The release certificate is checked by a separate
implementation.  Matrices are nine-bit integers in row-major order.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import numpy as np
from numba import njit


@njit(cache=True)
def build_mul_table() -> np.ndarray:
    table = np.empty((512, 512), dtype=np.uint16)
    for a in range(512):
        for b in range(512):
            c = 0
            for i in range(3):
                for j in range(3):
                    bit = 0
                    for k in range(3):
                        bit ^= ((a >> (3 * i + k)) & 1) & ((b >> (3 * k + j)) & 1)
                    c |= bit << (3 * i + j)
            table[a, b] = c
    return table


def words_through(degree: int) -> list[str]:
    words = [""]
    for length in range(1, degree + 1):
        words.extend(format(code, f"0{length}b").translate(str.maketrans("01", "XY"))
                     for code in range(1 << length))
    return words


def deterministic_pairs(count: int) -> tuple[np.ndarray, np.ndarray]:
    """A reproducible permutation prefix of the 2^18 ordered pairs."""
    if not 0 <= count <= (1 << 18):
        raise ValueError("pair count outside [0, 262144]")
    # Multiplication by an odd number and addition are a permutation modulo 2^18.
    z = ((np.arange(count, dtype=np.uint32) * np.uint32(150045))
         + np.uint32(101390)) & np.uint32((1 << 18) - 1)
    return (z >> np.uint32(9)).astype(np.uint16), (z & np.uint32(511)).astype(np.uint16)


def evaluate_words(degree: int, a: np.ndarray, b: np.ndarray,
                   mul: np.ndarray) -> tuple[list[str], np.ndarray]:
    words = words_through(degree)
    values = np.empty((len(words), len(a)), dtype=np.uint16)
    values[0, :] = np.uint16(0o421)  # diagonal bits 0,4,8: I_3
    offset = 1
    previous_offset = 0
    for length in range(1, degree + 1):
        for code in range(1 << length):
            prefix = previous_offset + (code >> 1)
            right = a if (code & 1) == 0 else b
            values[offset + code, :] = mul[values[prefix, :], right]
        previous_offset = offset
        offset += 1 << length
    return words, values


def packed_columns(values: np.ndarray) -> list[int]:
    columns: list[int] = []
    for vals in values:
        bits = ((vals[:, None] >> np.arange(9, dtype=np.uint16)) & 1).astype(np.uint8)
        payload = np.packbits(bits.reshape(-1), bitorder="little").tobytes()
        columns.append(int.from_bytes(payload, "little"))
    return columns


def rank_and_first_relation(columns: list[int]) -> tuple[int, int | None, list[int]]:
    """Column echelon form; relation mask refers to original columns."""
    basis: dict[int, tuple[int, int]] = {}
    pivots: list[int] = []
    for j, original in enumerate(columns):
        vector = original
        relation = 1 << j
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (vector, relation)
                pivots.append(pivot)
                break
            vector ^= basis[pivot][0]
            relation ^= basis[pivot][1]
        else:
            return len(basis), relation, pivots
    return len(basis), None, pivots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=12)
    parser.add_argument("--pairs", type=int, default=4096)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    mul = build_mul_table()
    a, b = deterministic_pairs(args.pairs)
    ranks = []
    first = None
    for degree in range(args.max_degree + 1):
        words, values = evaluate_words(degree, a, b, mul)
        rank, relation, _ = rank_and_first_relation(packed_columns(values))
        item = {"degree": degree, "columns": len(words), "rank": rank,
                "nullity_at_least": len(words) - rank}
        ranks.append(item)
        print(json.dumps(item, sort_keys=True))
        if relation is not None:
            support = [words[j] or "1" for j in range(len(words)) if (relation >> j) & 1]
            first = {"degree": degree, "support": support, "support_size": len(support)}
            print(json.dumps(first, sort_keys=True))
            break

    report = {
        "arithmetic": "exact GF(2)",
        "matrix_encoding": "nine-bit row-major",
        "pair_schedule": "z=(150045*i+101390) mod 2^18; A=z>>9; B=z&511",
        "pair_count": args.pairs,
        "ranks": ranks,
        "first_sample_relation": first,
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
