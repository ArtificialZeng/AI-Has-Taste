#!/usr/bin/env python3
"""Exact F_11 triage checks for x^4 versus x^8; no external packages."""

from collections import Counter
from hashlib import sha256
from pathlib import Path


P = 11
EXPECTED_SOURCE_SHA256 = (
    "9b0a3b9fc1ae610c9ab9e3165640b060077794cfe36987fb04833f06c658b2dd"
)
M = ((1, 0, 0), (0, 0, 1), (0, 1, 0))  # swaps projective y and z


def det3(matrix):
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % P


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(3)) % P for row in matrix)


def projective_normalize(vector):
    for coordinate in vector:
        if coordinate % P:
            scale = pow(coordinate % P, P - 2, P)
            return tuple(scale * value % P for value in vector)
    raise ValueError("zero vector has no projective point")


def projective_set(exponent):
    affine = {
        projective_normalize((x, pow(x, exponent, P), 1)) for x in range(P)
    }
    return affine | {projective_normalize((0, 1, 0))}


def graph(exponent):
    return [(x, pow(x, exponent, P)) for x in range(P)]


def difference_table(exponent):
    table = {
        (a, b): 0
        for a in range(P)
        for b in range(P)
        if (a, b) != (0, 0)
    }
    points = graph(exponent)
    for point in points:
        for other in points:
            difference = (
                (point[0] - other[0]) % P,
                (point[1] - other[1]) % P,
            )
            if difference != (0, 0):
                table[difference] += 1
    return table


def print_table(exponent, table):
    print(f"Delta table for x^{exponent}; rows a=0,...,10, columns b=0,...,10")
    for a in range(P):
        entries = ["-" if (a, b) == (0, 0) else str(table[(a, b)]) for b in range(P)]
        print(f"a={a:2d}: " + " ".join(entries))


def main():
    project_dir = Path(__file__).resolve().parent.parent
    source_digest = sha256((project_dir / "source.md").read_bytes()).hexdigest()
    assert source_digest == EXPECTED_SOURCE_SHA256

    assert det3(M) == P - 1
    source_set = projective_set(4)
    target_set = projective_set(8)
    image_set = {projective_normalize(mat_vec(M, point)) for point in source_set}
    assert len(source_set) == len(target_set) == 12
    assert image_set == target_set

    # Explicitly check the two exceptional points exchanged by M.
    assert projective_normalize(mat_vec(M, (0, 0, 1))) == (0, 1, 0)
    assert projective_normalize(mat_vec(M, (0, 1, 0))) == (0, 0, 1)

    tables = {exponent: difference_table(exponent) for exponent in (4, 8)}
    histograms = {exponent: Counter(table.values()) for exponent, table in tables.items()}
    assert len(tables[4]) == len(tables[8]) == 120
    assert sum(tables[4].values()) == sum(tables[8].values()) == 110
    assert histograms[4] == Counter({0: 50, 1: 50, 3: 20})
    assert histograms[8] == Counter({0: 30, 1: 70, 2: 20})
    assert histograms[4] != histograms[8]

    print(f"source.md sha256: {source_digest}")
    print(f"det(M) mod 11: {det3(M)}")
    print("M(S_x^4) = S_x^8: PASS (all 12 projective points)")
    for exponent in (4, 8):
        print_table(exponent, tables[exponent])
        print(f"histogram x^{exponent}: {sorted(histograms[exponent].items())}")
    print("Difference-count multisets differ: PASS")


if __name__ == "__main__":
    main()
