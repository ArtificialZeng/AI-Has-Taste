#!/usr/bin/env python3
"""Exact exhaustive verifier for the maximal-tubing flip graph of K_{3,3}.

Vertices are encoded as bit masks on p1,p2,p3,q1,q2,q3.  The full vertex
set is retained as a tube; it is common to every maximal tubing and therefore
does not affect flip distances.  All arithmetic and graph traversal are exact.
"""

from collections import Counter, deque
from hashlib import sha256
import json


N = 6
FULL = (1 << N) - 1
P = (1 << 3) - 1
Q = FULL ^ P


def connected(mask: int) -> bool:
    """Whether the nonempty induced subgraph of K_{3,3} is connected."""
    return bool(mask) and (
        mask & (mask - 1) == 0 or (mask & P and mask & Q)
    )


TUBES = tuple(mask for mask in range(1, FULL + 1) if connected(mask))


def compatible(a: int, b: int) -> bool:
    """Nested, or disjoint with disconnected union."""
    return (
        a & b == a
        or a & b == b
        or (a & b == 0 and not connected(a | b))
    )


COMPAT = {
    a: frozenset(b for b in TUBES if b != a and compatible(a, b))
    for a in TUBES
}


def maximal_tubings() -> tuple[tuple[int, ...], ...]:
    """Enumerate all maximal compatible tube sets by Bron--Kerbosch."""
    out: list[tuple[int, ...]] = []

    def visit(chosen: tuple[int, ...], candidates: set[int], excluded: set[int]):
        if not candidates and not excluded:
            out.append(tuple(sorted(chosen)))
            return
        pivot_pool = candidates | excluded
        pivot = max(pivot_pool, key=lambda x: len(candidates & COMPAT[x])) \
            if pivot_pool else None
        extension = candidates - (set(COMPAT[pivot]) if pivot is not None else set())
        for tube in tuple(extension):
            neighbors = set(COMPAT[tube])
            visit(
                chosen + (tube,),
                candidates & neighbors,
                excluded & neighbors,
            )
            candidates.remove(tube)
            excluded.add(tube)

    visit((), set(TUBES), set())
    return tuple(sorted(out))


TUBINGS = maximal_tubings()
INDEX = {tubing: i for i, tubing in enumerate(TUBINGS)}


def flip_graph() -> tuple[tuple[int, ...], ...]:
    """Join maximal tubings whose symmetric difference consists of two tubes."""
    owners: dict[tuple[int, ...], list[int]] = {}
    for i, tubing in enumerate(TUBINGS):
        for removed in tubing:
            # The full tube is mandatory under the convention used here.  Its
            # deletion is not a codimension-one face and hence not a flip.
            if removed == FULL:
                continue
            ridge = tuple(t for t in tubing if t != removed)
            owners.setdefault(ridge, []).append(i)
    adjacency = [set() for _ in TUBINGS]
    ridge_multiplicities = Counter(len(v) for v in owners.values())
    if ridge_multiplicities != Counter({2: len(owners)}):
        raise AssertionError(f"unexpected ridge multiplicities: {ridge_multiplicities}")
    for pair in owners.values():
        a, b = pair
        adjacency[a].add(b)
        adjacency[b].add(a)
    return tuple(tuple(sorted(neighbors)) for neighbors in adjacency)


ADJACENCY = flip_graph()


def all_eccentricities() -> tuple[tuple[int, ...], tuple[int, int]]:
    eccentricities: list[int] = []
    witness = (-1, -1)
    diameter = -1
    for start in range(len(TUBINGS)):
        dist = [-1] * len(TUBINGS)
        dist[start] = 0
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for nxt in ADJACENCY[current]:
                if dist[nxt] < 0:
                    dist[nxt] = dist[current] + 1
                    queue.append(nxt)
        if -1 in dist:
            raise AssertionError("flip graph is disconnected")
        ecc = max(dist)
        eccentricities.append(ecc)
        if ecc > diameter:
            diameter = ecc
            witness = (start, dist.index(ecc))
    return tuple(eccentricities), witness


def named(mask: int) -> list[str]:
    names = ("p1", "p2", "p3", "q1", "q2", "q3")
    return [name for i, name in enumerate(names) if mask & (1 << i)]


ECCENTRICITIES, WITNESS = all_eccentricities()
edge_count = sum(map(len, ADJACENCY)) // 2
canonical_edges = "\n".join(
    f"{i},{j}" for i, neighbors in enumerate(ADJACENCY) for j in neighbors if i < j
).encode()
result = {
    "graph": "K_{3,3}",
    "tube_count_including_full_set": len(TUBES),
    "maximal_tubing_count": len(TUBINGS),
    "maximal_tubing_size_histogram": dict(sorted(Counter(map(len, TUBINGS)).items())),
    "flip_edge_count": edge_count,
    "degree_histogram": dict(sorted(Counter(map(len, ADJACENCY)).items())),
    "diameter": max(ECCENTRICITIES),
    "eccentricity_histogram": dict(sorted(Counter(ECCENTRICITIES).items())),
    "diametral_pair_indices": list(WITNESS),
    "diametral_pair": [
        [named(tube) for tube in TUBINGS[index]] for index in WITNESS
    ],
    "canonical_edge_list_sha256": sha256(canonical_edges).hexdigest(),
}
print(json.dumps(result, indent=2, sort_keys=True))
