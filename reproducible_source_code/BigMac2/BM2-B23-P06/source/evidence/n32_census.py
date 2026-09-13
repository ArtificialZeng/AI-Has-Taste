#!/usr/bin/env python3
"""Exact perfectness census for all ICG_n(D), 1 <= n <= 32.

The decisive routine searches every possible length of an induced odd cycle
through vertex 0.  This is complete for a circulant graph: translation by a
cycle vertex is an automorphism, so every induced cycle has a translate through
0.  The same statement applies to the complement, which is again an ICG.

Only integer arithmetic and bit sets are used.  The JSON output is canonical
(sorted keys, compact separators, UTF-8, final newline).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from collections import deque
from pathlib import Path


ALGORITHM = "icg-n32-odd-hole-dfs-v1"


def strict_divisors(n: int) -> list[int]:
    return [d for d in range(1, n) if n % d == 0]


def adjacency(n: int, selected: frozenset[int]) -> list[int]:
    adj = [0] * n
    for x in range(n):
        row = 0
        for y in range(n):
            if x != y and math.gcd(x - y, n) in selected:
                row |= 1 << y
        adj[x] = row
    return adj


def complement(adj: list[int]) -> list[int]:
    n = len(adj)
    universe = (1 << n) - 1
    return [universe ^ (1 << v) ^ adj[v] for v in range(n)]


def _bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def find_shortest_odd_hole(adj: list[int]) -> tuple[list[int] | None, int]:
    """Return a shortest induced odd cycle, or None, and DFS-state count.

    Completeness invariant: ``path`` is an induced path beginning at 0.  A
    candidate adjacent to 0 can only close the path; a candidate not adjacent
    to 0 is extended exactly when it has no edge to an earlier non-predecessor.
    Iterating target lengths 5,7,... gives a shortest odd hole.
    """

    n = len(adj)
    if n < 5:
        return None, 0
    states = 0
    start = 0

    for target in range(5, n + 1, 2):
        path = [start]

        def dfs(used: int) -> list[int] | None:
            nonlocal states
            states += 1
            last = path[-1]
            candidates = adj[last] & ~used
            for w in _bits(candidates):
                if len(path) == 1:
                    path.append(w)
                    answer = dfs(used | (1 << w))
                    if answer is not None:
                        return answer
                    path.pop()
                    continue

                closes = bool(adj[start] & (1 << w))
                earlier_nonpredecessors = used ^ (1 << last)
                has_chord = bool(adj[w] & earlier_nonpredecessors)
                if closes:
                    # The start edge is intended, not a chord.
                    has_chord = bool(adj[w] & (earlier_nonpredecessors ^ 1))
                    if len(path) + 1 == target and not has_chord:
                        return path + [w]
                    continue
                if len(path) + 1 >= target or has_chord:
                    continue
                path.append(w)
                answer = dfs(used | (1 << w))
                if answer is not None:
                    return answer
                path.pop()
            return None

        answer = dfs(1)
        if answer is not None:
            return answer, states
    return None, states


def canonical_cycle(n: int, cycle: list[int]) -> list[int]:
    """Canonicalize under affine unit automorphisms and cycle dihedral order."""

    best: tuple[int, ...] | None = None
    for unit in range(n):
        if math.gcd(unit, n) != 1:
            continue
        transformed = [(unit * vertex) % n for vertex in cycle]
        for oriented in (transformed, list(reversed(transformed))):
            for shift in range(len(oriented)):
                rotated = oriented[shift:] + oriented[:shift]
                translate = (-rotated[0]) % n
                candidate = tuple((vertex + translate) % n for vertex in rotated)
                if best is None or candidate < best:
                    best = candidate
    assert best is not None
    return list(best)


def components(adj: list[int], vertices: int) -> list[int]:
    result: list[int] = []
    unseen = vertices
    while unseen:
        seed = unseen & -unseen
        comp = 0
        frontier = seed
        unseen ^= seed
        while frontier:
            comp |= frontier
            nbrs = 0
            for v in _bits(frontier):
                nbrs |= adj[v]
            frontier = nbrs & unseen
            unseen ^= frontier
        result.append(comp)
    return result


def is_bipartite(adj: list[int]) -> bool:
    n = len(adj)
    color = [-1] * n
    for root in range(n):
        if color[root] != -1:
            continue
        color[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in _bits(adj[v]):
                if color[w] == -1:
                    color[w] = 1 - color[v]
                    queue.append(w)
                elif color[w] == color[v]:
                    return False
    return True


def is_complete_on(adj: list[int], vertices: int) -> bool:
    for v in _bits(vertices):
        if (adj[v] & vertices) != (vertices ^ (1 << v)):
            return False
    return True


def is_complete_multipartite(adj: list[int]) -> bool:
    cadj = complement(adj)
    all_vertices = (1 << len(adj)) - 1
    return all(is_complete_on(cadj, comp) for comp in components(cadj, all_vertices))


def is_chordal(adj: list[int]) -> bool:
    """Exact simplicial-elimination recognition."""

    remaining = (1 << len(adj)) - 1
    while remaining:
        simplicial = None
        for v in _bits(remaining):
            neighborhood = adj[v] & remaining
            if is_complete_on(adj, neighborhood):
                simplicial = v
                break
        if simplicial is None:
            return False
        remaining ^= 1 << simplicial
    return True


def is_cograph(adj: list[int]) -> bool:
    cadj = complement(adj)

    def rec(vertices: int) -> bool:
        if vertices.bit_count() <= 1:
            return True
        comps = components(adj, vertices)
        if len(comps) > 1:
            return all(rec(comp) for comp in comps)
        cocomps = components(cadj, vertices)
        if len(cocomps) > 1:
            return all(rec(comp) for comp in cocomps)
        return False

    return rec((1 << len(adj)) - 1)


def structural_certificates(adj: list[int]) -> list[str]:
    cadj = complement(adj)
    labels: list[str] = []
    if is_bipartite(adj):
        labels.append("bipartite")
    if is_bipartite(cadj):
        labels.append("co-bipartite")
    if is_complete_multipartite(adj):
        labels.append("complete-multipartite")
    if is_complete_multipartite(cadj):
        labels.append("cluster")
    if is_chordal(adj):
        labels.append("chordal")
    if is_chordal(cadj):
        labels.append("co-chordal")
    if is_cograph(adj):
        labels.append("cograph")
    return labels


def adjacency_digest(adj: list[int]) -> str:
    width = (len(adj) + 7) // 8
    payload = b"".join(row.to_bytes(width, "little") for row in adj)
    return hashlib.sha256(payload).hexdigest()


def canonical_bytes(value) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def build_manifest() -> dict:
    records = []
    structure_counts: dict[str, int] = {}
    total_states = 0
    for n in range(1, 33):
        divisors = strict_divisors(n)
        for dmask in range(1 << len(divisors)):
            selected = frozenset(
                divisors[i] for i in range(len(divisors)) if dmask & (1 << i)
            )
            adj = adjacency(n, selected)
            cadj = complement(adj)
            hole, graph_states = find_shortest_odd_hole(adj)
            antihole = None
            complement_states = 0
            if hole is None:
                antihole, complement_states = find_shortest_odd_hole(cadj)
            total_states += graph_states + complement_states
            witness = None
            labels: list[str] = []
            if hole is not None:
                witness = {"side": "graph", "cycle": canonical_cycle(n, hole)}
            elif antihole is not None:
                witness = {"side": "complement", "cycle": canonical_cycle(n, antihole)}
            else:
                labels = structural_certificates(adj)
                for label in labels:
                    structure_counts[label] = structure_counts.get(label, 0) + 1
            records.append(
                {
                    "D": sorted(selected),
                    "adjacency_sha256": adjacency_digest(adj),
                    "divisors": divisors,
                    "dmask": dmask,
                    "n": n,
                    "search_states": {
                        "complement": complement_states,
                        "graph": graph_states,
                    },
                    "status": "imperfect" if witness else "perfect",
                    "structural_certificates": labels,
                    "witness": witness,
                }
            )

    expected = sum(1 << len(strict_divisors(n)) for n in range(1, 33))
    assert expected == 539
    assert len(records) == expected
    record_digest = hashlib.sha256(canonical_bytes(records)).hexdigest()
    perfect = sum(record["status"] == "perfect" for record in records)
    structurally_covered = sum(
        record["status"] == "perfect" and bool(record["structural_certificates"])
        for record in records
    )
    return {
        "algorithm": ALGORITHM,
        "completeness_basis": (
            "All 539 divisor masks are enumerated. Translation makes every "
            "induced cycle have a copy through 0; induced-path DFS exhausts "
            "every odd length 5..n in both graph and complement."
        ),
        "domain": {"n_max": 32, "n_min": 1, "pair_count": expected},
        "records": records,
        "records_sha256": record_digest,
        "runtime": {"implementation": platform.python_implementation(), "python": platform.python_version()},
        "summary": {
            "imperfect": len(records) - perfect,
            "perfect": perfect,
            "perfect_structurally_covered": structurally_covered,
            "perfect_structural_residue": perfect - structurally_covered,
            "structure_counts_overlapping": dict(sorted(structure_counts.items())),
            "total_search_states": total_states,
        },
        "witness_canonicalization": (
            "Lexicographic minimum under translations, multiplication by units "
            "modulo n, cycle rotations, and reversal; divisor sets are fixed by "
            "these unit automorphisms."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    manifest = build_manifest()
    args.output.write_bytes(canonical_bytes(manifest) + b"\n")
    print(json.dumps(manifest["summary"], sort_keys=True))
    print("records_sha256", manifest["records_sha256"])
    print("manifest_sha256", hashlib.sha256(args.output.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
