#!/usr/bin/env python3
"""Exact combinatorial intake check for the proper nonempty faces of B_3.

A vertex subset S is facial exactly when it contains every permutation vertex
whose support is contained in the union of the supports of vertices in S.
The script also quotients those subsets by row permutations, column
permutations, and transposition.  It uses only integer/set computations.
"""

from collections import Counter
from itertools import combinations, permutations, product


PERMS = tuple(permutations(range(3)))
INDEX = {p: i for i, p in enumerate(PERMS)}


def support(p):
    return frozenset((i, p[i]) for i in range(3))


SUPPORTS = tuple(support(p) for p in PERMS)


def face_closure(vertex_set):
    allowed = frozenset().union(*(SUPPORTS[i] for i in vertex_set))
    return frozenset(i for i, supp in enumerate(SUPPORTS) if supp <= allowed)


def affine_dimension(vertex_set):
    """Rank over Q of differences of flattened permutation matrices."""
    vertices = []
    for k in vertex_set:
        p = PERMS[k]
        vertices.append([int(p[i] == j) for i in range(3) for j in range(3)])
    rows = [[x - y for x, y in zip(v, vertices[0])] for v in vertices[1:]]
    rank = 0
    col = 0
    while rank < len(rows) and col < 9:
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        a = rows[rank][col]
        for r in range(len(rows)):
            if r != rank and rows[r][col]:
                b = rows[r][col]
                rows[r] = [a * x - b * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        col += 1
    return rank


def transform_vertex(p, row_perm, col_perm, transpose):
    edges = {(row_perm[i], col_perm[p[i]]) for i in range(3)}
    if transpose:
        edges = {(j, i) for i, j in edges}
    image = [None] * 3
    for i, j in edges:
        image[i] = j
    return INDEX[tuple(image)]


def main():
    faces = set()
    for size in range(1, 6):
        for subset in combinations(range(6), size):
            candidate = frozenset(subset)
            if face_closure(candidate) == candidate:
                faces.add(candidate)

    actions = set()
    for row_perm, col_perm, transpose in product(PERMS, PERMS, (False, True)):
        actions.add(tuple(transform_vertex(p, row_perm, col_perm, transpose) for p in PERMS))

    unseen = set(faces)
    orbits = []
    while unseen:
        face = min(unseen, key=lambda s: (len(s), tuple(sorted(s))))
        orbit = {
            frozenset(action[i] for i in face)
            for action in actions
        }
        assert orbit <= faces
        orbits.append(orbit)
        unseen -= orbit

    face_counts = Counter(affine_dimension(face) for face in faces)
    orbit_counts = Counter(affine_dimension(next(iter(orbit))) for orbit in orbits)
    print(f"vertices={len(PERMS)}")
    print(f"natural_group_actions={len(actions)}")
    print(f"proper_nonempty_faces={len(faces)}")
    print("faces_by_dimension=" + repr(dict(sorted(face_counts.items()))))
    print(f"face_orbits={len(orbits)}")
    print("orbits_by_dimension=" + repr(dict(sorted(orbit_counts.items()))))
    print("orbit_sizes_by_dimension=")
    for dim in sorted(orbit_counts):
        sizes = sorted(len(orbit) for orbit in orbits if affine_dimension(next(iter(orbit))) == dim)
        print(f"  dim {dim}: {sizes}")
    print("orbit_representatives=")
    for orbit in sorted(
        orbits,
        key=lambda o: (
            affine_dimension(next(iter(o))),
            len(o),
            tuple(sorted(min(o, key=lambda s: tuple(sorted(s))))),
        ),
    ):
        representative = min(orbit, key=lambda s: tuple(sorted(s)))
        labels = ["".join(str(j + 1) for j in PERMS[i]) for i in sorted(representative)]
        print(
            f"  dim={affine_dimension(representative)} orbit_size={len(orbit)} "
            f"vertices={labels}"
        )


if __name__ == "__main__":
    main()
