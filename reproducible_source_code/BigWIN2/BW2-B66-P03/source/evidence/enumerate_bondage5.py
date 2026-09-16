#!/usr/bin/env python3
"""Exact exhaustive classification for win-00066-p03.

This program uses only the Python standard library.  It enumerates every
five-edge subset, tests domination with integer bitsets, obtains Aut(G) by an
adjacency-preserving backtrack, and writes a replayable JSON certificate.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


VERTICES = tuple(range(18))
EDGES = tuple(sorted({
    (0, 6), (0, 10), (0, 16), (1, 8), (1, 11), (1, 12),
    (2, 4), (2, 5), (2, 13), (3, 4), (3, 5), (3, 9),
    (4, 16), (5, 11), (6, 7), (6, 13), (7, 8), (7, 14),
    (8, 13), (9, 10), (9, 14), (10, 15), (11, 15),
    (12, 15), (12, 17), (14, 17), (16, 17),
}))
N = len(VERTICES)
ALL_VERTICES = (1 << N) - 1
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def vertex_mask(xs: tuple[int, ...]) -> int:
    ans = 0
    for x in xs:
        ans |= 1 << x
    return ans


ADJ = [0] * N
INCIDENT_EDGE_BITS = [[0] * N for _ in VERTICES]
for i, (u, v) in enumerate(EDGES):
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
    INCIDENT_EDGE_BITS[u][v] = 1 << i
    INCIDENT_EDGE_BITS[v][u] = 1 << i
CLOSED = [(1 << v) | ADJ[v] for v in VERTICES]


def dominates_base(dmask: int) -> bool:
    covered = 0
    todo = dmask
    while todo:
        bit = todo & -todo
        covered |= CLOSED[bit.bit_length() - 1]
        todo ^= bit
    return covered == ALL_VERTICES


def critical_edge_masks(dmask: int) -> tuple[int, ...]:
    """Edge masks that must not be wholly deleted for D to dominate."""
    answer = []
    for v in VERTICES:
        if (dmask >> v) & 1:
            continue
        crossing = 0
        neighbors_in_d = ADJ[v] & dmask
        while neighbors_in_d:
            bit = neighbors_in_d & -neighbors_in_d
            u = bit.bit_length() - 1
            crossing |= INCIDENT_EDGE_BITS[v][u]
            neighbors_in_d ^= bit
        if crossing == 0:
            raise AssertionError("base-nondominating set passed to critical masks")
        answer.append(crossing)
    return tuple(answer)


def domination_candidates(k: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    answer = []
    for vertices in itertools.combinations(VERTICES, k):
        dmask = vertex_mask(vertices)
        if dominates_base(dmask):
            answer.append((vertices, critical_edge_masks(dmask)))
    # Robust sets are tried first.  This affects speed but not the result.
    answer.sort(key=lambda item: tuple(
        sum(c.bit_count() == width for c in item[1]) for width in (1, 2, 3)
    ))
    return answer


def survives(deleted: int, criticals: tuple[int, ...]) -> bool:
    return all((deleted & c) != c for c in criticals)


def automorphisms() -> list[tuple[int, ...]]:
    """Enumerate all adjacency-preserving vertex bijections from scratch."""
    mapping = [-1] * N
    inverse = [-1] * N
    output: list[tuple[int, ...]] = []

    def domain(x: int) -> list[int]:
        possible = []
        for y in VERTICES:
            if inverse[y] != -1 or ADJ[x].bit_count() != ADJ[y].bit_count():
                continue
            valid = True
            for a in VERTICES:
                b = mapping[a]
                if b == -1:
                    continue
                if bool(ADJ[x] & (1 << a)) != bool(ADJ[y] & (1 << b)):
                    valid = False
                    break
            if valid:
                possible.append(y)
        return possible

    def search(assigned: int) -> None:
        if assigned == N:
            output.append(tuple(mapping))
            return
        best_x = -1
        best_domain: list[int] | None = None
        for x in VERTICES:
            if mapping[x] != -1:
                continue
            dx = domain(x)
            if not dx:
                return
            if best_domain is None or len(dx) < len(best_domain):
                best_x, best_domain = x, dx
        assert best_domain is not None
        for y in best_domain:
            mapping[best_x] = y
            inverse[y] = best_x
            search(assigned + 1)
            inverse[y] = -1
            mapping[best_x] = -1

    search(0)
    return sorted(output)


def transform_edge_mask(mask: int, permutation: tuple[int, ...]) -> int:
    answer = 0
    todo = mask
    while todo:
        bit = todo & -todo
        u, v = EDGES[bit.bit_length() - 1]
        image = tuple(sorted((permutation[u], permutation[v])))
        answer |= 1 << EDGE_INDEX[image]
        todo ^= bit
    return answer


def edge_list(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1)


def main() -> None:
    assert N == 18 and len(EDGES) == 27 and len(set(EDGES)) == 27
    assert all(u < v for u, v in EDGES)
    assert all(ADJ[v].bit_count() == 3 for v in VERTICES)

    base_domination_counts = {}
    base_gamma = None
    for k in range(N + 1):
        count = sum(
            dominates_base(vertex_mask(vertices))
            for vertices in itertools.combinations(VERTICES, k)
        )
        base_domination_counts[str(k)] = count
        if count and base_gamma is None:
            base_gamma = k
            break
    assert base_gamma == 6

    candidates6 = domination_candidates(6)
    assert len(candidates6) == base_domination_counts["6"]
    qualifying: list[int] = []
    scanned = 0
    for deleted_indices in itertools.combinations(range(len(EDGES)), 5):
        scanned += 1
        deleted = sum(1 << i for i in deleted_indices)
        if not any(survives(deleted, crits) for _, crits in candidates6):
            qualifying.append(deleted)
    assert scanned == 80730

    # Since edge deletion cannot improve domination, lack of a size-6
    # dominator gives gamma >= 7.  Find an exact size-7 witness for every set.
    candidates7 = domination_candidates(7)
    gamma_witness: dict[int, tuple[int, ...]] = {}
    for deleted in qualifying:
        for vertices, crits in candidates7:
            if survives(deleted, crits):
                gamma_witness[deleted] = vertices
                break
        else:
            raise AssertionError(f"no size-7 dominator for deletion mask {deleted}")

    autos = automorphisms()
    auto_set = set(autos)
    identity = tuple(VERTICES)
    assert identity in auto_set
    for p in autos:
        assert sorted(p) == list(VERTICES)
        assert all(
            bool(ADJ[u] & (1 << v)) == bool(ADJ[p[u]] & (1 << p[v]))
            for u in VERTICES for v in VERTICES
        )
    for p in autos:
        for q in autos:
            assert tuple(p[q[v]] for v in VERTICES) in auto_set

    qualifying_set = set(qualifying)
    unseen = set(qualifying)
    orbit_records = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {transform_edge_mask(seed, p) for p in autos}
        assert orbit <= qualifying_set
        canonical = min(orbit, key=edge_list)
        orbit = {transform_edge_mask(canonical, p) for p in autos}
        stabilizer = [p for p in autos if transform_edge_mask(canonical, p) == canonical]
        assert len(orbit) * len(stabilizer) == len(autos)
        assert all(mask in gamma_witness for mask in orbit)
        record = {
            "canonical_edges": [list(e) for e in edge_list(canonical)],
            "canonical_edge_indices": [
                i for i in range(len(EDGES)) if (canonical >> i) & 1
            ],
            "gamma": 7,
            "dominating_7_witness": list(gamma_witness[canonical]),
            "orbit_size": len(orbit),
            "stabilizer_order": len(stabilizer),
            "stabilizer_permutations": [list(p) for p in stabilizer],
        }
        orbit_records.append(record)
        unseen -= orbit
    orbit_records.sort(key=lambda record: tuple(map(tuple, record["canonical_edges"])))

    raw = b"".join(mask.to_bytes(4, "little") for mask in sorted(qualifying))
    output = {
        "schema": "win-00066-p03-exact-enumeration-v1",
        "method": {
            "language": "Python standard library only",
            "domination": "exhaustive vertex subsets encoded as integer bitsets",
            "automorphisms": "complete adjacency-preserving bijection backtrack",
            "five_edge_subsets_scanned": scanned,
        },
        "vertices": list(VERTICES),
        "edges_lexicographic": [list(e) for e in EDGES],
        "base_gamma": base_gamma,
        "base_dominating_set_counts_through_gamma": base_domination_counts,
        "dominating_6_set_count": len(candidates6),
        "dominating_7_set_count": len(candidates7),
        "automorphism_group_order": len(autos),
        "automorphism_permutations": [list(p) for p in autos],
        "qualifying_set_count": len(qualifying),
        "qualifying_masks_sorted_sha256": hashlib.sha256(raw).hexdigest(),
        "qualifying_edge_index_sets": [
            [i for i in range(len(EDGES)) if (mask >> i) & 1]
            for mask in sorted(qualifying)
        ],
        "orbit_count": len(orbit_records),
        "orbit_size_sum": sum(record["orbit_size"] for record in orbit_records),
        "gamma_distribution_labelled": {
            "7": len(qualifying),
        },
        "orbits": orbit_records,
    }
    target = Path(__file__).with_name("bondage5_classification.json")
    target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(target),
        "base_gamma": base_gamma,
        "dominating_6_set_count": len(candidates6),
        "automorphism_group_order": len(autos),
        "qualifying_set_count": len(qualifying),
        "orbit_count": len(orbit_records),
        "orbit_size_sum": sum(record["orbit_size"] for record in orbit_records),
        "gamma_distribution_labelled": {"7": len(qualifying)},
        "qualifying_masks_sorted_sha256": hashlib.sha256(raw).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
