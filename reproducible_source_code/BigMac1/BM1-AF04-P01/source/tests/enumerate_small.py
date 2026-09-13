#!/usr/bin/env python3
"""Independent exhaustive baseline for small simple chord-labelled diagrams."""

from __future__ import annotations

from functools import lru_cache


def matchings(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for position in range(1, len(vertices)):
        second = vertices[position]
        rest = vertices[1:position] + vertices[position + 1:]
        for tail in matchings(rest):
            yield ((first, second),) + tail


def adjacent(x: int, y: int, size: int) -> bool:
    return (x-y) % size in (1, size-1)


def crosses(left: tuple[int, int], right: tuple[int, int]) -> bool:
    a, b = sorted(left)
    c, d = sorted(right)
    return (a < c < b < d) or (c < a < d < b)


def parallel(left: tuple[int, int], right: tuple[int, int], size: int) -> bool:
    if crosses(left, right):
        return False
    a, b = left
    c, d = right
    paired_1 = adjacent(a, c, size) and adjacent(b, d, size)
    paired_2 = adjacent(a, d, size) and adjacent(b, c, size)
    return paired_1 or paired_2


def simple(diagram: tuple[tuple[int, int], ...], size: int) -> bool:
    if any(adjacent(a, b, size) for a, b in diagram):
        return False
    for i, left in enumerate(diagram):
        for right in diagram[i + 1:]:
            if parallel(left, right, size):
                return False
    return True


@lru_cache(maxsize=None)
def count_simple(chords: int) -> int:
    size = 2*chords
    return sum(simple(diagram, size) for diagram in matchings(tuple(range(size))))


def main() -> int:
    expected = [0, 1, 1, 21, 168, 1968, 26094]
    actual = [count_simple(n) for n in range(1, len(expected) + 1)]
    if actual != expected:
        raise AssertionError(f"small enumeration mismatch: {actual} != {expected}")
    print("PASS: exhaustive simple chord-labelled counts n=1..7:", actual)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
