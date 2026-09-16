#!/usr/bin/env python3
"""Exact finite check of the local cyclic-word constraint at a vertex."""

from itertools import product

LABELS = ("a", "b", "c")
DIRECT = {("a", "b", "c"), ("b", "c", "a"), ("c", "a", "b")}


def valid_stars(degree: int):
    """Return all radial/link label words obeying the direct face words."""
    stars = []
    for radial in product(LABELS, repeat=degree):
        link = []
        for i in range(degree):
            candidates = [
                q
                for q in LABELS
                if (radial[i], q, radial[(i + 1) % degree]) in DIRECT
            ]
            if len(candidates) != 1:
                break
            link.append(candidates[0])
        else:
            stars.append((radial, tuple(link)))
    return stars


for d in range(3, 13):
    stars = valid_stars(d)
    print(f"degree {d}: {len(stars)} valid labelled stars")
    assert bool(stars) == (d % 3 == 0)
    if d == 3:
        assert all(link[(i + 1) % 3] == radial[i]
                   for radial, link in stars for i in range(3))

print("verified: degrees 4 and 5 are impossible")
print("verified: at degree 3 every radial edge equals its opposite link edge")
