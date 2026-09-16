#!/usr/bin/env python3
"""Independently check n12.cnf using enumeration by 9-set partitions."""

from hashlib import sha256
from itertools import combinations
from pathlib import Path


N = 12
CNF = Path(__file__).resolve().with_name("n12.cnf")


def pair(a, b):
    return (a, b) if a < b else (b, a)


def main():
    vertices = list(combinations(range(1, N + 1), 3))
    edge_id = {
        pair(a, b): number
        for number, (a, b) in enumerate(
            ((a, b) for a, b in combinations(vertices, 2) if set(a).isdisjoint(b)), 1
        )
    }
    by_id = {number: edge for edge, number in edge_id.items()}
    assert len(edge_id) == 9240

    raw = CNF.read_bytes()
    lines = raw.decode("ascii").splitlines()
    assert lines[0] == "p cnf 9240 123200"
    assert len(lines) == 123201
    observed = set()
    clause_hasher = sha256()
    for offset in range(1, len(lines), 2):
        positive = tuple(map(int, lines[offset].split()))
        negative = tuple(map(int, lines[offset + 1].split()))
        assert len(positive) == 4 and positive[-1] == 0
        assert all(x > 0 for x in positive[:-1])
        assert negative == tuple(-x for x in positive[:-1]) + (0,)
        ids = positive[:-1]
        assert len(set(ids)) == 3 and all(1 <= x <= 9240 for x in ids)
        endpoint_vertices = set()
        for identifier in ids:
            endpoint_vertices.update(by_id[identifier])
        assert len(endpoint_vertices) == 3
        assert len(set().union(*endpoint_vertices)) == 9
        assert ids not in observed
        observed.add(ids)
        clause_hasher.update((lines[offset] + "\n" + lines[offset + 1] + "\n").encode("ascii"))

    expected = set()
    for nine in combinations(range(1, N + 1), 9):
        for a_tail in combinations(nine[1:], 2):
            a = (nine[0],) + a_tail
            remaining = tuple(x for x in nine if x not in a)
            for b_tail in combinations(remaining[1:], 2):
                b = (remaining[0],) + b_tail
                c = tuple(x for x in remaining if x not in b)
                blocks = sorted((a, b, c))
                expected.add(tuple(edge_id[pair(x, y)] for x, y in combinations(blocks, 2)))
    assert len(expected) == 61600
    assert observed == expected
    print("VERIFIED exact KG(12,3) ordinary two-color NAE CNF")
    print("vertices=220")
    print("edges=9240")
    print("triangles=61600")
    print("clauses=123200")
    print(f"clause_stream_sha256={clause_hasher.hexdigest()}")
    print(f"dimacs_sha256={sha256(raw).hexdigest()}")


if __name__ == "__main__":
    main()
