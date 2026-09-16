#!/usr/bin/env python3
"""Independent exact replay of bondage5_classification.json.

Unlike enumerate_bondage5.py, this verifier rebuilds every deleted graph and
tests closed-neighborhood unions directly.  It enumerates automorphisms as
isometries of the all-pairs graph-distance matrix.  Only the standard library
is used.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CERTIFICATE = ROOT / "evidence" / "bondage5_classification.json"
OUTPUT = ROOT / "evidence" / "bondage5_verification.json"
V = tuple(range(18))
E = tuple(sorted({
    (0, 6), (0, 10), (0, 16), (1, 8), (1, 11), (1, 12),
    (2, 4), (2, 5), (2, 13), (3, 4), (3, 5), (3, 9),
    (4, 16), (5, 11), (6, 7), (6, 13), (7, 8), (7, 14),
    (8, 13), (9, 10), (9, 14), (10, 15), (11, 15),
    (12, 15), (12, 17), (14, 17), (16, 17),
}))
EDGE_NUMBER = {edge: i for i, edge in enumerate(E)}
FULL_V = (1 << len(V)) - 1


def deletion_mask(indices: tuple[int, ...] | list[int]) -> int:
    return sum(1 << i for i in indices)


def closed_neighborhoods(deleted: int) -> list[int]:
    closed = [1 << v for v in V]
    for i, (u, v) in enumerate(E):
        if not ((deleted >> i) & 1):
            closed[u] |= 1 << v
            closed[v] |= 1 << u
    return closed


def dominates(vertices: tuple[int, ...] | list[int], closed: list[int]) -> bool:
    covered = 0
    for v in vertices:
        covered |= closed[v]
    return covered == FULL_V


def base_dominators(k: int, base_closed: list[int]) -> list[tuple[int, ...]]:
    answer = [d for d in itertools.combinations(V, k) if dominates(d, base_closed)]

    def fragility(d: tuple[int, ...]) -> tuple[int, int, int]:
        chosen = set(d)
        counts = [0, 0, 0]
        for x in V:
            if x in chosen:
                continue
            cross_degree = sum(bool(base_closed[x] & (1 << y)) for y in d)
            counts[cross_degree - 1] += 1
        return tuple(counts)

    answer.sort(key=fragility)
    return answer


def all_pair_distances(base_closed: list[int]) -> list[list[int]]:
    distance = [[99] * len(V) for _ in V]
    for source in V:
        distance[source][source] = 0
        queue = deque([source])
        while queue:
            x = queue.popleft()
            neighbors = base_closed[x] & ~(1 << x)
            while neighbors:
                bit = neighbors & -neighbors
                y = bit.bit_length() - 1
                neighbors ^= bit
                if distance[source][y] == 99:
                    distance[source][y] = distance[source][x] + 1
                    queue.append(y)
    return distance


def distance_isometries(distance: list[list[int]]) -> list[tuple[int, ...]]:
    """Exhaustively enumerate all distance-preserving vertex bijections."""
    image = [-1] * len(V)
    preimage = [-1] * len(V)
    answer: list[tuple[int, ...]] = []

    def candidates(x: int) -> list[int]:
        ys = []
        for y in V:
            if preimage[y] != -1:
                continue
            if all(
                image[a] == -1 or distance[x][a] == distance[y][image[a]]
                for a in V
            ):
                ys.append(y)
        return ys

    def visit(done: int) -> None:
        if done == len(V):
            answer.append(tuple(image))
            return
        options = []
        for x in V:
            if image[x] == -1:
                cx = candidates(x)
                if not cx:
                    return
                options.append((len(cx), x, cx))
        _, x, cx = min(options)
        for y in cx:
            image[x], preimage[y] = y, x
            visit(done + 1)
            image[x], preimage[y] = -1, -1

    visit(0)
    return sorted(answer)


def act(deleted: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for i, (u, v) in enumerate(E):
        if (deleted >> i) & 1:
            mapped = tuple(sorted((permutation[u], permutation[v])))
            result |= 1 << EDGE_NUMBER[mapped]
    return result


def edge_tuple(deleted: int) -> tuple[tuple[int, int], ...]:
    return tuple(E[i] for i in range(len(E)) if (deleted >> i) & 1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    cert = json.loads(CERTIFICATE.read_text())
    assert tuple(map(tuple, cert["edges_lexicographic"])) == E
    base_closed = closed_neighborhoods(0)

    counts = {}
    gamma = None
    for k in range(len(V) + 1):
        count = sum(dominates(d, base_closed) for d in itertools.combinations(V, k))
        counts[str(k)] = count
        if count:
            gamma = k
            break
    assert gamma == cert["base_gamma"] == 6
    assert counts == cert["base_dominating_set_counts_through_gamma"]

    dominators6 = base_dominators(6, base_closed)
    assert len(dominators6) == 297
    direct_qualifying = []
    total = 0
    for indices in itertools.combinations(range(len(E)), 5):
        total += 1
        deleted = deletion_mask(indices)
        closed = closed_neighborhoods(deleted)
        if not any(dominates(d, closed) for d in dominators6):
            direct_qualifying.append(deleted)
    assert total == 80730

    certified_qualifying = [
        deletion_mask(indices) for indices in cert["qualifying_edge_index_sets"]
    ]
    assert set(direct_qualifying) == set(certified_qualifying)
    assert len(direct_qualifying) == cert["qualifying_set_count"] == 801

    # A separate direct size-7 search supplies a witness for every labelled set.
    dominators7 = base_dominators(7, base_closed)
    direct_witnesses = {}
    for deleted in direct_qualifying:
        closed = closed_neighborhoods(deleted)
        witness = next((d for d in dominators7 if dominates(d, closed)), None)
        assert witness is not None
        direct_witnesses[deleted] = witness

    distances = all_pair_distances(base_closed)
    autos = distance_isometries(distances)
    certified_autos = sorted(tuple(p) for p in cert["automorphism_permutations"])
    assert autos == certified_autos
    assert len(autos) == cert["automorphism_group_order"] == 6

    # Rebuild the orbit partition, canonical representatives, and stabilizers.
    remaining = set(direct_qualifying)
    rebuilt = {}
    while remaining:
        seed = next(iter(remaining))
        orbit = {act(seed, p) for p in autos}
        representative = min(orbit, key=edge_tuple)
        stabilizer = sorted(p for p in autos if act(representative, p) == representative)
        assert len(orbit) * len(stabilizer) == len(autos)
        rebuilt[edge_tuple(representative)] = (len(orbit), stabilizer)
        remaining -= orbit

    certified_records = {}
    for record in cert["orbits"]:
        representative_edges = tuple(map(tuple, record["canonical_edges"]))
        representative = deletion_mask(record["canonical_edge_indices"])
        assert edge_tuple(representative) == representative_edges
        closed = closed_neighborhoods(representative)
        assert record["gamma"] == 7
        assert not any(dominates(d, closed) for d in dominators6)
        assert dominates(record["dominating_7_witness"], closed)
        certified_records[representative_edges] = (
            record["orbit_size"],
            sorted(tuple(p) for p in record["stabilizer_permutations"]),
        )
        assert record["stabilizer_order"] == len(record["stabilizer_permutations"])
    assert rebuilt == certified_records
    assert len(rebuilt) == cert["orbit_count"] == 140
    assert sum(size for size, _ in rebuilt.values()) == cert["orbit_size_sum"] == 801

    raw_masks = b"".join(mask.to_bytes(4, "little") for mask in sorted(direct_qualifying))
    family_digest = hashlib.sha256(raw_masks).hexdigest()
    assert family_digest == cert["qualifying_masks_sorted_sha256"]

    orbit_size_distribution = {}
    stabilizer_order_distribution = {}
    for size, stabilizer in rebuilt.values():
        orbit_size_distribution[str(size)] = orbit_size_distribution.get(str(size), 0) + 1
        order = str(len(stabilizer))
        stabilizer_order_distribution[order] = stabilizer_order_distribution.get(order, 0) + 1

    report = {
        "schema": "win-00066-p03-independent-verification-v1",
        "verified": True,
        "independent_methods": {
            "domination": "direct closed-neighborhood union on every rebuilt deleted graph",
            "automorphisms": "exhaustive all-pairs-distance isometry backtrack",
        },
        "source_md_sha256": sha256(ROOT / "source.md"),
        "problem_md_sha256": sha256(ROOT / "problem.md"),
        "classification_json_sha256": sha256(CERTIFICATE),
        "five_edge_subsets_scanned": total,
        "base_gamma": gamma,
        "base_dominating_set_counts_through_gamma": counts,
        "qualifying_set_count": len(direct_qualifying),
        "qualifying_masks_sorted_sha256": family_digest,
        "every_qualifying_set_has_direct_size_7_witness": len(direct_witnesses) == 801,
        "gamma_distribution_labelled": {"7": 801},
        "automorphism_group_order": len(autos),
        "orbit_count": len(rebuilt),
        "orbit_size_sum": sum(size for size, _ in rebuilt.values()),
        "orbit_size_distribution": orbit_size_distribution,
        "stabilizer_order_distribution": stabilizer_order_distribution,
        "all_certificate_orbit_records_replayed": True,
    }
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
