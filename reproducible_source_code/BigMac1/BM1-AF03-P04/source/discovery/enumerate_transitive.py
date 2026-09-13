#!/usr/bin/env python3
"""Generate canonical transitive n x n arrays for 2 <= n <= 5.

This is discovery/certificate-generation code.  Completeness uses the
classification in Proposition 3.14 of arXiv:2602.02342v2: two-color arrays
come from a set partition, a permutation of its blocks, and one diagonal bit
per block; arrays with at least three colors are row-constant or
column-constant on a set partition of [n].
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


def set_partitions_rgs(n: int, blocks: int):
    """Yield restricted-growth strings of length n with exactly blocks values."""
    if n < 1 or blocks < 1 or blocks > n:
        return

    def extend(prefix: list[int], current_max: int):
        if len(prefix) == n:
            if current_max + 1 == blocks:
                yield tuple(prefix)
            return
        upper = min(current_max + 1, blocks - 1)
        for value in range(upper + 1):
            prefix.append(value)
            yield from extend(prefix, max(current_max, value))
            prefix.pop()

    yield from extend([0], 0)


def canonicalize(values: tuple[int, ...] | list[int]) -> str:
    labels: dict[int, int] = {}
    result: list[str] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        result.append(str(labels[value]))
    return "".join(result)


def is_transitive(array: str, n: int) -> bool:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if array[i * n + k] not in (
                    array[i * n + j],
                    array[j * n + k],
                ):
                    return False
    return True


def two_color_types(n: int) -> set[str]:
    result: set[str] = set()
    for block_count in range(1, n + 1):
        for partition in set_partitions_rgs(n, block_count):
            for permutation in itertools.permutations(range(block_count)):
                for diagonal_mask in range(1 << block_count):
                    values: list[int] = []
                    for i in range(n):
                        bi = partition[i]
                        for j in range(n):
                            bj = partition[j]
                            if bi == bj:
                                value = (diagonal_mask >> bi) & 1
                            else:
                                value = int(permutation[bj] > permutation[bi])
                            values.append(value)
                    canonical = canonicalize(values)
                    if len(set(canonical)) == 2:
                        result.add(canonical)
    return result


def at_least_three_color_types(n: int) -> set[str]:
    result: set[str] = set()
    for block_count in range(3, n + 1):
        for partition in set_partitions_rgs(n, block_count):
            row_constant = [partition[i] for i in range(n) for _ in range(n)]
            column_constant = [partition[j] for _ in range(n) for j in range(n)]
            result.add(canonicalize(row_constant))
            result.add(canonicalize(column_constant))
    return result


def stirling_second(n: int, k: int) -> int:
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def expected_histogram(n: int) -> dict[int, int]:
    bitransitive_count = sum(
        stirling_second(n, k) * (2**k) * factorial(k)
        for k in range(1, n + 1)
    )
    histogram = {1: 1, 2: bitransitive_count // 2 - 1}
    for k in range(3, n + 1):
        histogram[k] = 2 * stirling_second(n, k)
    return histogram


def factorial(n: int) -> int:
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


def arrays_digest(arrays: list[str]) -> str:
    return hashlib.sha256(("\n".join(arrays) + "\n").encode()).hexdigest()


def build_entry(n: int) -> dict[str, object]:
    arrays = {"0" * (n * n)}
    arrays.update(two_color_types(n))
    arrays.update(at_least_three_color_types(n))
    ordered = sorted(arrays)
    if not all(is_transitive(array, n) for array in ordered):
        raise AssertionError(f"generator produced a nontransitive array for n={n}")
    histogram = Counter(len(set(array)) for array in ordered)
    expected = expected_histogram(n)
    if dict(sorted(histogram.items())) != expected:
        raise AssertionError(
            f"classification count mismatch for n={n}: {histogram} != {expected}"
        )
    return {
        "n": n,
        "type_count": len(ordered),
        "color_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "residual_instances": len(ordered) * n**3,
        "arrays_sha256": arrays_digest(ordered),
        "arrays": ordered,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("certificates/transitive_arrays_n_le_5.json"),
    )
    args = parser.parse_args()
    data = {
        "schema_version": 1,
        "certificate_kind": "canonical_transitive_array_enumeration",
        "source_version": "arXiv:2602.02342v2, Proposition 3.14",
        "theorem_endpoint": "transitive-CYBE Conjecture 1.5 for n=5",
        "construction": "color relabeling quotient; no index-permutation quotient",
        "n_values": {str(n): build_entry(n) for n in range(2, 6)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output}")
    for n, entry in data["n_values"].items():
        print(
            f"n={n}: types={entry['type_count']}, "
            f"residual_instances={entry['residual_instances']}, "
            f"sha256={entry['arrays_sha256']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
