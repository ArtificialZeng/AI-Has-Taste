#!/usr/bin/env python3
"""Exact standard-library verifier for the ternary 4-cube certificate."""

from itertools import permutations, product
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "borsuk_ternary4.json"
VERTICES = list(product((-1, 0, 1), repeat=4))
INDEX = {v: i for i, v in enumerate(VERTICES)}
N = len(VERTICES)
UNIVERSE = (1 << N) - 1


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sqdist(x, y):
    return sum((a - b) ** 2 for a, b in zip(x, y))


DIST = [[sqdist(x, y) for y in VERTICES] for x in VERTICES]


def adjacency(predicate):
    out = [0] * N
    for i in range(N):
        for j in range(i):
            if predicate(DIST[i][j]):
                out[i] |= 1 << j
                out[j] |= 1 << i
    return out


def enumerate_maximal_cliques(adj):
    output = set()

    def bron_kerbosch(r, p, x):
        if not p and not x:
            output.add(r)
            return
        union = p | x
        pivot = -1
        pivot_score = -1
        scan = union
        while scan:
            bit = scan & -scan
            u = bit.bit_length() - 1
            scan ^= bit
            score = (p & adj[u]).bit_count()
            if score > pivot_score:
                pivot = u
                pivot_score = score
        candidates = p if pivot < 0 else p & ~adj[pivot] & UNIVERSE
        while candidates:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            candidates ^= bit
            bron_kerbosch(r | bit, p & adj[v], x & adj[v])
            p ^= bit
            x |= bit

    bron_kerbosch(0, UNIVERSE, 0)
    return output


def transformations():
    maps = []
    for perm in permutations(range(4)):
        for signs in product((-1, 1), repeat=4):
            maps.append(
                [
                    INDEX[tuple(signs[k] * v[perm[k]] for k in range(4))]
                    for v in VERTICES
                ]
            )
    return maps


def transform_mask(mask, mapping):
    out = 0
    while mask:
        bit = mask & -mask
        i = bit.bit_length() - 1
        mask ^= bit
        out |= 1 << mapping[i]
    return out


def check_coloring(vertices, colors, delta):
    require(len(vertices) == len(colors), "color list length mismatch")
    require(len(vertices) == len(set(vertices)), "repeated vertex in coloring")
    require(all(0 <= c < 4 for c in colors), "color outside {0,1,2,3}")
    assignment = dict(zip(vertices, colors))
    for i, u in enumerate(vertices):
        for v in vertices[:i]:
            if DIST[u][v] == delta:
                require(assignment[u] != assignment[v], f"bad delta={delta} coloring")


def main():
    raw = CERTIFICATE.read_bytes()
    data = json.loads(raw)
    require(data["schema_version"] == 1, "unsupported certificate schema")
    require(N == 81, "wrong ternary cube size")
    distance_values = sorted(
        {DIST[i][j] for i in range(N) for j in range(i)}
    )
    require(distance_values == data["distance_values"], "distance spectrum mismatch")
    require(
        distance_values == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 16],
        "unexpected distance spectrum",
    )

    # Every odd-distance graph is bipartite by parity of the coordinate sum.
    for delta in (1, 3, 5, 7, 9, 13):
        for i in range(N):
            for j in range(i):
                if DIST[i][j] == delta:
                    pi = sum(VERTICES[i]) & 1
                    pj = sum(VERTICES[j]) & 1
                    require(pi != pj, f"parity coloring failed at delta={delta}")

    # The remaining even layers except delta=6 have global four-colorings.
    for delta in (2, 4, 8, 10, 12, 16):
        colors = data["global_colorings"][str(delta)]
        require(len(colors) == N, f"global coloring length mismatch at {delta}")
        check_coloring(list(range(N)), colors, delta)

    # At delta=6, a diameter-bounded set is a clique in the <=6 graph.
    compatible = adjacency(lambda value: value <= 6)
    maximal = enumerate_maximal_cliques(compatible)
    delta6 = data["delta6"]
    require(len(maximal) == delta6["maximal_clique_count"] == 15056,
            "maximal-clique count mismatch")
    maps = transformations()
    require(len(maps) == delta6["symmetry_group_order"] == 384,
            "symmetry group order mismatch")
    covered = set()
    for record in delta6["orbits"]:
        verts = record["vertices"]
        colors = record["colors"]
        mask = sum(1 << v for v in verts)
        require(mask in maximal, "orbit representative is not maximal compatible")
        check_coloring(verts, colors, 6)
        members = {transform_mask(mask, mapping) for mapping in maps} & maximal
        require(len(members) == record["orbit_size"], "orbit size mismatch")
        require(not (covered & members), "duplicate symmetry orbit")
        covered |= members
    require(len(delta6["orbits"]) == delta6["orbit_count"] == 72,
            "orbit count mismatch")
    require(covered == maximal, "symmetry representatives do not cover all maximal cliques")

    # A regular tetrahedron inside the grid proves that four parts can be needed.
    lower = data["lower_bound"]
    witness = lower["vertices"]
    require(len(witness) == 4, "lower-bound witness has wrong size")
    for i, u in enumerate(witness):
        for v in witness[:i]:
            require(DIST[u][v] == lower["squared_distance"] == 2,
                    "lower-bound witness is not equidistant")

    cert_hash = hashlib.sha256(raw).hexdigest()
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("VERIFIED: max_S subset {-1,0,1}^4 b(S) = 4")
    print(f"distance_spectrum={distance_values}")
    print(f"delta6_maximal_cliques={len(maximal)} delta6_orbits={len(delta6['orbits'])}")
    print(f"certificate_sha256={cert_hash}")
    print(f"verifier_sha256={code_hash}")


if __name__ == "__main__":
    main()
