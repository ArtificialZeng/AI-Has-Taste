#!/usr/bin/env python3
"""Exhaust the direct-copy face rotations in an oriented vertex star.

A face in the oriented fan is recorded as (r_i, q_i, r_{i+1}).  Choosing a
rotation independently for every face covers every cyclic starting point.
Both possible orientations of the scalene reference triangle are checked.
All comparisons are exact string equalities.
"""

from itertools import product


def rotations(word):
    return tuple(word[i:] + word[:i] for i in range(3))


REFERENCE_WORDS = {
    "abc": ("a", "b", "c"),
    "acb": ("a", "c", "b"),
}


def valid_stars(word, degree):
    direct_faces = rotations(word)
    stars = []
    for faces in product(direct_faces, repeat=degree):
        # The last radial label in face i is the first radial label in the
        # next positively oriented face.  The final comparison closes the fan.
        if all(faces[i][2] == faces[(i + 1) % degree][0]
               for i in range(degree)):
            stars.append(faces)
    return stars


for name, word in REFERENCE_WORDS.items():
    counts = {}
    for degree in range(3, 9):
        stars = valid_stars(word, degree)
        counts[degree] = len(stars)
        assert bool(stars) == (degree % 3 == 0)
        if degree == 3:
            # q_{i+1}, the link edge opposite r_i, has the same label as r_i.
            assert all(
                faces[(i + 1) % 3][1] == faces[i][0]
                for faces in stars
                for i in range(3)
            )
    print(f"reference {name}: " + ", ".join(
        f"d={degree}:{counts[degree]}" for degree in sorted(counts)
    ))

print("verified exactly: both handedness classes have no degree-4 or degree-5 star")
print("verified exactly: every degree-3 star has equal opposite-edge labels")
