#!/usr/bin/env python3
"""Solver-independent exhaustive checker for n11_coloring.txt."""

from hashlib import sha256
from itertools import combinations
from pathlib import Path


N = 11
MODEL = Path(__file__).with_name("n11_coloring.txt")


def edge(a, b):
    return (a, b) if a < b else (b, a)


def main():
    colors = {}
    for number, raw in enumerate(MODEL.read_text(encoding="ascii").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        fields = raw.split()
        if len(fields) != 3 or fields[2] not in {"R", "B"}:
            raise AssertionError(f"bad line {number}: {raw!r}")
        a = tuple(map(int, fields[0].split(",")))
        b = tuple(map(int, fields[1].split(",")))
        if (len(a) != 3 or len(b) != 3 or tuple(sorted(a)) != a
                or tuple(sorted(b)) != b or len(set(a + b)) != 6
                or not all(1 <= x <= N for x in a + b)):
            raise AssertionError(f"invalid KG edge on line {number}")
        e = edge(a, b)
        if e in colors:
            raise AssertionError(f"duplicate edge on line {number}")
        colors[e] = fields[2]

    vertices = list(combinations(range(1, N + 1), 3))
    expected = {
        edge(a, b) for a, b in combinations(vertices, 2)
        if set(a).isdisjoint(b)
    }
    if set(colors) != expected:
        raise AssertionError(
            f"edge coverage mismatch: got {len(colors)}, expected {len(expected)}"
        )

    triangle_count = 0
    for a, b, c in combinations(vertices, 3):
        if len(set(a + b + c)) == 9:
            triangle_count += 1
            triangle_colors = {colors[edge(a, b)], colors[edge(a, c)], colors[edge(b, c)]}
            if len(triangle_colors) == 1:
                raise AssertionError(f"monochromatic triangle: {a}, {b}, {c}")

    if triangle_count != 15400:
        raise AssertionError(f"triangle count {triangle_count} != 15400")
    print("VERIFIED complete two-coloring with no monochromatic triangle")
    print(f"edges={len(colors)}")
    print(f"triangles={triangle_count}")
    print(f"coloring_sha256={sha256(MODEL.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
