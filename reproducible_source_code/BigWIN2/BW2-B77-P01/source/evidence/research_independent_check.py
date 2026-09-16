#!/usr/bin/env python3
"""Independent exact sanity checks for the research proof.

The all-m conclusion is proved symbolically in the research audit.  This
script separately enumerates every labelled fork embedding in each colour,
then tests whether any same-colour edge is disjoint from that embedding.
It also checks the advertised spherical face list combinatorially.
"""

from itertools import combinations, permutations


def construction(m):
    assert m >= 3
    apices = {"a", "b"}
    rim = tuple(range(m))
    vertices = ("a", "b", *rim)
    red = {
        frozenset((q, i))
        for q in apices
        for i in rim
    }
    blue = {
        frozenset((i, (i + 1) % m))
        for i in rim
    }
    faces = {
        frozenset((q, i, (i + 1) % m))
        for q in apices
        for i in rim
    }
    return vertices, apices, red, blue, faces


def fork_embeddings(vertices, edges):
    """Yield all images (s,x,y,z,w) of the four fork edges.

    The use of permutations enforces injectivity.  Only required edges are
    tested, so this is an ordinary (non-induced) subgraph search.
    """
    required = ((0, 1), (0, 2), (0, 3), (3, 4))
    for image in permutations(vertices, 5):
        if all(frozenset((image[i], image[j])) in edges for i, j in required):
            yield image


def has_fork_plus_disjoint_edge(vertices, edges):
    for image in fork_embeddings(vertices, edges):
        used = set(image)
        if any(used.isdisjoint(edge) for edge in edges):
            return True
    return False


def check_faces(vertices, edges, faces):
    # This checks the face certificate used by the explicit spherical drawing.
    incidence = {edge: 0 for edge in edges}
    for face in faces:
        assert len(face) == 3
        for pair in combinations(face, 2):
            edge = frozenset(pair)
            assert edge in incidence
            incidence[edge] += 1
    assert len(vertices) - len(edges) + len(faces) == 2
    assert set(incidence.values()) == {2}


def main():
    for m in range(3, 19):
        vertices, apices, red, blue, faces = construction(m)
        all_edges = red | blue
        assert red.isdisjoint(blue)
        assert len(vertices) == m + 2
        assert len(all_edges) == 3 * m == 3 * len(vertices) - 6
        assert len(faces) == 2 * m
        check_faces(vertices, all_edges, faces)

        red_forks = list(fork_embeddings(vertices, red))
        assert len(red_forks) == 2 * m * (m - 1) * (m - 2)
        assert all(apices.issubset(image) for image in red_forks)
        assert not any(fork_embeddings(vertices, blue))
        assert not has_fork_plus_disjoint_edge(vertices, red)
        assert not has_fork_plus_disjoint_edge(vertices, blue)

        if m == 3:
            # The boundary host is exactly K_5 with the apex edge deleted.
            complete = {frozenset(pair) for pair in combinations(vertices, 2)}
            assert complete - all_edges == {frozenset(apices)}

    print("PASS: independent labelled-embedding checks for every m in [3,18]")
    print("red fork count = 2*m*(m-1)*(m-2), and every one uses both apices")
    print("blue fork count = 0; neither colour contains fork union disjoint edge")
    print("boundary m=3 is K5 minus the apex edge; face certificates pass")


if __name__ == "__main__":
    main()
