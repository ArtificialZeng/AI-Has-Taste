#!/usr/bin/env python3
"""Exact finite sanity check for the bipyramid colouring.

This is not the proof of the unbounded claim.  It independently implements the
non-induced-copy definition and checks a documented finite range, while the
uniform argument is recorded in checkpoint.md.
"""

from itertools import combinations


def bipyramid(m):
    assert m >= 3
    vertices = ("a", "b") + tuple(range(m))
    red = {
        frozenset((apex, i))
        for apex in ("a", "b")
        for i in range(m)
    }
    blue = {frozenset((i, (i + 1) % m)) for i in range(m)}
    return vertices, red, blue


def neighbours(vertices, edges):
    result = {v: set() for v in vertices}
    for edge in edges:
        u, v = tuple(edge)
        result[u].add(v)
        result[v].add(u)
    return result


def contains_noninduced_fork_plus_edge(vertices, edges):
    """Return whether the graph contains S_{2,1,1} union K_2.

    Extra edges are deliberately ignored.  The search chooses the degree-three
    fork centre, its three neighbours, the distinguished length-two arm, and
    then an edge disjoint from all five fork vertices.
    """
    nbr = neighbours(vertices, edges)
    for centre in vertices:
        for first_arm_vertices in combinations(nbr[centre], 3):
            for middle in first_arm_vertices:
                for tip in nbr[middle] - {centre} - set(first_arm_vertices):
                    fork_vertices = {centre, *first_arm_vertices, tip}
                    if any(fork_vertices.isdisjoint(edge) for edge in edges):
                        return True
    return False


def face_incidence_certificate(m, all_edges):
    """Check the standard 2m triangular faces of the spherical bipyramid."""
    faces = []
    for i in range(m):
        j = (i + 1) % m
        faces.extend((frozenset(("a", i, j)), frozenset(("b", i, j))))
    incidences = {edge: 0 for edge in all_edges}
    for face in faces:
        assert len(face) == 3
        for edge in combinations(face, 2):
            frozen_edge = frozenset(edge)
            assert frozen_edge in incidences
            incidences[frozen_edge] += 1
    return len(faces) == 2 * m and set(incidences.values()) == {2}


def main():
    checked = range(3, 41)
    for m in checked:
        vertices, red, blue = bipyramid(m)
        all_edges = red | blue
        assert len(vertices) == m + 2
        assert len(all_edges) == 3 * len(vertices) - 6 == 3 * m
        assert face_incidence_certificate(m, all_edges)
        assert max(map(len, neighbours(vertices, blue).values())) == 2
        assert not contains_noninduced_fork_plus_edge(vertices, red)
        assert not contains_noninduced_fork_plus_edge(vertices, blue)
    print("PASS: exact checks for every m in [3,40]")
    print("orders checked: 5 through 42")
    print("each graph: |E|=3|V|-6 and spherical triangular face incidence verified")
    print("each colouring: no red or blue non-induced S_{2,1,1} union K_2")


if __name__ == "__main__":
    main()

