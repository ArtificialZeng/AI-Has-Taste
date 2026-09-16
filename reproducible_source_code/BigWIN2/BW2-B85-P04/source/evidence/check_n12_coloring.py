#!/usr/bin/env python3
"""Solver-independent exhaustive checker for n12_coloring.txt."""

from hashlib import sha256
from itertools import combinations
from pathlib import Path


N = 12
MODEL = Path(__file__).resolve().with_name("n12_coloring.txt")


def edge(a, b):
    return (a, b) if a < b else (b, a)


def main():
    colors = {}
    for number, raw in enumerate(MODEL.read_text(encoding="ascii").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        fields = raw.split()
        assert len(fields) == 3 and fields[2] in {"R", "B"}, f"bad line {number}"
        a = tuple(map(int, fields[0].split(",")))
        b = tuple(map(int, fields[1].split(",")))
        assert (len(a) == len(b) == 3 and tuple(sorted(a)) == a
                and tuple(sorted(b)) == b and len(set(a + b)) == 6
                and all(1 <= x <= N for x in a + b)), f"bad edge on line {number}"
        assert edge(a, b) not in colors, f"duplicate edge on line {number}"
        colors[edge(a, b)] = fields[2]
    vertices = list(combinations(range(1, N + 1), 3))
    expected = {edge(a, b) for a, b in combinations(vertices, 2) if set(a).isdisjoint(b)}
    assert set(colors) == expected and len(colors) == 9240
    triangle_count = 0
    for nine in combinations(range(1, N + 1), 9):
        for a_tail in combinations(nine[1:], 2):
            a = (nine[0],) + a_tail
            remaining = tuple(x for x in nine if x not in a)
            for b_tail in combinations(remaining[1:], 2):
                b = (remaining[0],) + b_tail
                c = tuple(x for x in remaining if x not in b)
                triangle_count += 1
                assert len({colors[edge(a, b)], colors[edge(a, c)], colors[edge(b, c)]}) > 1, (a, b, c)
    assert triangle_count == 61600
    print("VERIFIED complete two-coloring with no monochromatic triangle")
    print("edges=9240")
    print("triangles=61600")
    print(f"coloring_sha256={sha256(MODEL.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
