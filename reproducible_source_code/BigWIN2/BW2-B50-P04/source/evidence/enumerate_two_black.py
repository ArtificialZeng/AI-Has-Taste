#!/usr/bin/env python3
"""Exact census for two-black-square crossword rook placements.

For every unordered pair of black squares, this builds the word-incidence
bipartite graph and counts perfect matchings in two ways:

1. row-by-row subset dynamic programming for the permanent;
2. direct recursive graph matching, branching on a minimum-degree across word.

It also canonicalizes black-square pairs under all eight symmetries of the
square and checks orbit completeness and count invariance.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


Square = tuple[int, int]
Configuration = tuple[Square, Square]


def word_graph(n: int, black: Configuration) -> tuple[list[list[int]], int]:
    """Return across-to-down adjacency and the number of down words."""
    blocked = set(black)
    across: dict[Square, int] = {}
    down: dict[Square, int] = {}

    across_count = 0
    for row in range(n):
        active = None
        for col in range(n):
            if (row, col) in blocked:
                active = None
            else:
                if active is None:
                    active = across_count
                    across_count += 1
                across[(row, col)] = active

    down_count = 0
    for col in range(n):
        active = None
        for row in range(n):
            if (row, col) in blocked:
                active = None
            else:
                if active is None:
                    active = down_count
                    down_count += 1
                down[(row, col)] = active

    adjacency = [[] for _ in range(across_count)]
    for square, across_id in across.items():
        adjacency[across_id].append(down[square])
    for neighbors in adjacency:
        neighbors.sort()
        assert len(neighbors) == len(set(neighbors))
    return adjacency, down_count


def subset_dp_permanent(adjacency: list[list[int]], right_size: int) -> int:
    """Permanent by a row-ordered DP indexed by used-column bitmasks."""
    if len(adjacency) != right_size:
        return 0
    dp = [0] * (1 << right_size)
    dp[0] = 1
    for row, neighbors in enumerate(adjacency):
        next_dp = [0] * (1 << right_size)
        required_popcount = row
        for used, value in enumerate(dp):
            if value == 0 or used.bit_count() != required_popcount:
                continue
            for col in neighbors:
                bit = 1 << col
                if not used & bit:
                    next_dp[used | bit] += value
        dp = next_dp
    return dp[-1]


def recursive_matching_count(adjacency: list[list[int]], right_size: int) -> int:
    """Perfect matchings by direct deletion recursion on a bipartite graph."""
    if len(adjacency) != right_size:
        return 0

    remaining_left = tuple(range(len(adjacency)))

    def search(left: tuple[int, ...], available_right: frozenset[int]) -> int:
        if not left:
            return 1
        vertex = min(
            left,
            key=lambda item: sum(col in available_right for col in adjacency[item]),
        )
        choices = [col for col in adjacency[vertex] if col in available_right]
        if not choices:
            return 0
        smaller_left = tuple(item for item in left if item != vertex)
        total = 0
        for col in choices:
            total += search(smaller_left, available_right - {col})
        return total

    return search(remaining_left, frozenset(range(right_size)))


def transforms(n: int, square: Square) -> tuple[Square, ...]:
    row, col = square
    last = n - 1
    return (
        (row, col),
        (row, last - col),
        (last - row, col),
        (last - row, last - col),
        (col, row),
        (col, last - row),
        (last - col, row),
        (last - col, last - row),
    )


def orbit(n: int, black: Configuration) -> tuple[Configuration, ...]:
    images = set()
    first_images = transforms(n, black[0])
    second_images = transforms(n, black[1])
    for first, second in zip(first_images, second_images):
        images.add(tuple(sorted((first, second))))
    return tuple(sorted(images))


def census(n: int) -> dict[str, object]:
    squares = list(itertools.product(range(n), repeat=2))
    orbit_counts: dict[Configuration, int] = {}
    orbit_sizes: dict[Configuration, int] = {}
    configuration_count = 0
    zero_count = 0
    histogram: Counter[int] = Counter()

    for black_untyped in itertools.combinations(squares, 2):
        black: Configuration = black_untyped
        adjacency, right_size = word_graph(n, black)
        dp_count = subset_dp_permanent(adjacency, right_size)
        recursive_count = recursive_matching_count(adjacency, right_size)
        assert dp_count == recursive_count, (n, black, dp_count, recursive_count)

        configuration_count += 1
        histogram[dp_count] += 1
        zero_count += dp_count == 0
        black_orbit = orbit(n, black)
        representative = black_orbit[0]
        if representative in orbit_counts:
            assert orbit_counts[representative] == dp_count
        else:
            orbit_counts[representative] = dp_count
            orbit_sizes[representative] = len(black_orbit)

    expected = n * n * (n * n - 1) // 2
    assert configuration_count == expected
    assert sum(orbit_sizes.values()) == expected
    assert sum(histogram.values()) == expected

    maximum = max(orbit_counts.values())
    maximizing = sorted(rep for rep, value in orbit_counts.items() if value == maximum)

    def serialize_configuration(config: Configuration) -> list[list[int]]:
        # Evidence is human-facing, so convert coordinates from 0-based to 1-based.
        return [[row + 1, col + 1] for row, col in config]

    orbit_records = [
        {
            "representative": serialize_configuration(rep),
            "orbit_size": orbit_sizes[rep],
            "count": orbit_counts[rep],
        }
        for rep in sorted(orbit_counts)
    ]
    orbit_digest = hashlib.sha256(
        json.dumps(orbit_records, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    return {
        "n": n,
        "configurations": configuration_count,
        "orbits": len(orbit_counts),
        "zero_count_configurations": zero_count,
        "maximum": maximum,
        "maximizing_orbit_count": len(maximizing),
        "maximizing_orbits": [serialize_configuration(rep) for rep in maximizing],
        "histogram": [{"count": key, "configurations": histogram[key]} for key in sorted(histogram)],
        "orbit_records_sha256": orbit_digest,
        "orbit_records": orbit_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-n", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--output", type=Path, default=Path("evidence/census_n3_n8.json"))
    args = parser.parse_args()
    assert 1 <= args.min_n <= args.max_n

    result = {
        "method": {
            "first": "exact row-ordered subset-DP permanent",
            "second": "exact direct recursive graph matching with minimum-degree branching",
            "symmetry": "all eight horizontal/vertical reflection and transpose images",
            "coordinates": "1-based row-column coordinates",
        },
        "range": [args.min_n, args.max_n],
        "results": [census(n) for n in range(args.min_n, args.max_n + 1)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")

    for item in result["results"]:
        print(
            f"n={item['n']} configs={item['configurations']} orbits={item['orbits']} "
            f"M2={item['maximum']} max_orbits={item['maximizing_orbit_count']} "
            f"representatives={item['maximizing_orbits']}"
        )


if __name__ == "__main__":
    main()
