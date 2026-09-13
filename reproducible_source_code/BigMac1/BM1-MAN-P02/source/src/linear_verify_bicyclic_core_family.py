#!/usr/bin/env python3
"""Independent exact audit of the ten-vertex bicyclic-core search.

No builder or discovery module is imported.  The domain is regenerated from
an independently implemented free-tree generator by adding two nonedges, and
is deduplicated with a second structural two-core code.  Determinants are
recomputed by Bareiss elimination, inverses by cofactor adjugates, and every
nonsingular profile graph is searched after an independent cyclic relabelling.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

from linear_verify_tree_core_family import generate_free_trees
from linear_verify_unicyclic_core_family import (
    TargetSearch,
    adjugate,
    determinant,
    multiply,
    permute_graph,
    profile_graph,
    selftest,
)


RANK = 10
TARGET = 53
EXPECTED_BICYCLIC = 2678
EXPECTED_NONSINGULAR = 719


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def neighbours(
    adjacency: Sequence[Sequence[int]],
    vertex: int,
    allowed: set[int] | None = None,
    forbidden: set[tuple[int, int]] | None = None,
) -> list[int]:
    blocked = forbidden or set()
    return [
        child
        for child, value in enumerate(adjacency[vertex])
        if value
        and (allowed is None or child in allowed)
        and (min(vertex, child), max(vertex, child)) not in blocked
    ]


def components(
    adjacency: Sequence[Sequence[int]],
    vertices: Iterable[int],
    forbidden: set[tuple[int, int]] | None = None,
) -> list[set[int]]:
    allowed = set(vertices)
    unseen = set(allowed)
    output = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        piece = {root}
        stack = [root]
        while stack:
            vertex = stack.pop()
            for child in neighbours(adjacency, vertex, allowed, forbidden):
                if child in unseen:
                    unseen.remove(child)
                    piece.add(child)
                    stack.append(child)
        output.append(piece)
    return output


def leaf_pruned_core(adjacency: Sequence[Sequence[int]]) -> set[int]:
    degree = [sum(map(int, row)) for row in adjacency]
    present = [True] * len(adjacency)
    leaves = [vertex for vertex, value in enumerate(degree) if value <= 1]
    while leaves:
        vertex = leaves.pop()
        if not present[vertex]:
            continue
        present[vertex] = False
        for child, value in enumerate(adjacency[vertex]):
            if value and present[child]:
                degree[child] -= 1
                if degree[child] == 1:
                    leaves.append(child)
    return {vertex for vertex, flag in enumerate(present) if flag}


def rooted_attachment(
    adjacency: Sequence[Sequence[int]], vertex: int, parent: int, core: set[int]
) -> str:
    children = [
        rooted_attachment(adjacency, child, vertex, core)
        for child in neighbours(adjacency, vertex)
        if child != parent and child not in core
    ]
    return "[" + "".join(sorted(children)) + "]"


def trace_path(
    adjacency: Sequence[Sequence[int]],
    vertices: set[int],
    start: int,
    finish: int,
    forbidden: set[tuple[int, int]] | None = None,
) -> list[int]:
    path = [start]
    previous = -1
    current = start
    while current != finish:
        options = [
            child
            for child in neighbours(adjacency, current, vertices, forbidden)
            if child != previous
        ]
        if len(options) != 1:
            raise ValueError("independent path trace is not unique")
        previous, current = current, options[0]
        if current in path:
            raise ValueError("independent path trace repeated a vertex")
        path.append(current)
    if set(path) != vertices:
        raise ValueError("independent path trace missed vertices")
    return path


def bridges(adjacency: Sequence[Sequence[int]], core: set[int]) -> set[tuple[int, int]]:
    output = set()
    for left in core:
        for right in core:
            if left >= right or not adjacency[left][right]:
                continue
            forbidden = {(left, right)}
            if len(components(adjacency, core, forbidden)) > 1:
                output.add((left, right))
    return output


def independent_code(adjacency: Sequence[Sequence[int]]) -> str:
    if len(adjacency) != RANK:
        raise ValueError("independent code expects order ten")
    if sum(sum(map(int, row)) for row in adjacency) // 2 != RANK + 1:
        raise ValueError("independent code expects eleven edges")
    if len(components(adjacency, range(RANK))) != 1:
        raise ValueError("independent code expects a connected graph")

    core = leaf_pruned_core(adjacency)
    core_size = len(core)
    core_edges = sum(adjacency[i][j] for i in core for j in core if i < j)
    if core_edges != core_size + 1:
        raise ValueError("independent two-core has wrong excess")
    label = {
        vertex: rooted_attachment(adjacency, vertex, -1, core)
        for vertex in core
    }
    degree = {vertex: len(neighbours(adjacency, vertex, core)) for vertex in core}
    branch_vertices = sorted(vertex for vertex in core if degree[vertex] > 2)

    if len(branch_vertices) == 1 and degree[branch_vertices[0]] == 4:
        center = branch_vertices[0]
        pieces = components(adjacency, core - {center})
        if len(pieces) != 2:
            raise ValueError("independent figure-eight decomposition failed")
        rings = []
        for piece in pieces:
            ends = sorted(vertex for vertex in piece if adjacency[center][vertex])
            if len(ends) != 2:
                raise ValueError("independent figure-eight endpoints failed")
            path = trace_path(adjacency, piece, ends[0], ends[1])
            word = tuple(label[vertex] for vertex in path)
            rings.append(min(word, tuple(reversed(word))))
        payload = ("8", label[center], tuple(sorted(rings)))
        return repr(payload)

    if len(branch_vertices) != 2 or any(degree[vertex] != 3 for vertex in branch_vertices):
        raise ValueError("independent code found invalid excess degrees")
    left, right = branch_vertices
    cut_edges = bridges(adjacency, core)

    if not cut_edges:
        paths: list[tuple[str, ...]] = []
        if adjacency[left][right]:
            paths.append(tuple())
        for piece in components(adjacency, core - {left, right}):
            starts = [vertex for vertex in piece if adjacency[left][vertex]]
            finishes = [vertex for vertex in piece if adjacency[right][vertex]]
            if len(starts) != 1 or len(finishes) != 1:
                raise ValueError("independent theta attachments failed")
            path = trace_path(adjacency, piece, starts[0], finishes[0])
            paths.append(tuple(label[vertex] for vertex in path))
        if len(paths) != 3:
            raise ValueError("independent theta path count failed")
        forward = ("H", label[left], tuple(sorted(paths)), label[right])
        reverse = (
            "H",
            label[right],
            tuple(sorted(tuple(reversed(path)) for path in paths)),
            label[left],
        )
        return min(repr(forward), repr(reverse))

    bridge_vertices = {vertex for edge in cut_edges for vertex in edge}
    bridge_path = trace_path(adjacency, bridge_vertices, left, right, set())
    cut_components = components(adjacency, core, cut_edges)
    left_cycle = next(piece for piece in cut_components if left in piece)
    right_cycle = next(piece for piece in cut_components if right in piece)
    if left_cycle == right_cycle:
        raise ValueError("independent dumbbell cycles did not separate")
    leftovers = set().union(
        *(piece for piece in cut_components if piece not in (left_cycle, right_cycle))
    ) if len(cut_components) > 2 else set()
    if leftovers != set(bridge_path[1:-1]):
        raise ValueError("independent dumbbell bridge leftovers failed")

    def ring_word(endpoint: int, piece: set[int]) -> tuple[str, ...]:
        starts = neighbours(adjacency, endpoint, piece, cut_edges)
        if len(starts) != 2:
            raise ValueError("independent dumbbell ring degree failed")
        alternatives = []
        for start in starts:
            word = []
            previous = endpoint
            current = start
            while current != endpoint:
                word.append(label[current])
                options = [
                    child
                    for child in neighbours(adjacency, current, piece, cut_edges)
                    if child != previous
                ]
                if len(options) != 1:
                    raise ValueError("independent dumbbell ring trace failed")
                previous, current = current, options[0]
            alternatives.append(tuple(word))
        return min(alternatives)

    left_ring = ring_word(left, left_cycle)
    right_ring = ring_word(right, right_cycle)
    middle = tuple(label[vertex] for vertex in bridge_path[1:-1])
    forward = ("B", left_ring, label[left], middle, label[right], right_ring)
    reverse = (
        "B",
        right_ring,
        label[right],
        tuple(reversed(middle)),
        label[left],
        left_ring,
    )
    return min(repr(forward), repr(reverse))


def add_edges(
    adjacency: Sequence[Sequence[int]], first: tuple[int, int], second: tuple[int, int]
) -> list[list[int]]:
    output = [list(map(int, row)) for row in adjacency]
    for left, right in (first, second):
        if left == right or output[left][right]:
            raise ValueError("independent generator attempted a repeated edge")
        output[left][right] = output[right][left] = 1
    return output


def independent_domain() -> tuple[dict[str, list[list[int]]], dict[str, object]]:
    trees, free_counts, rooted_counts = generate_free_trees()
    output: dict[str, list[list[int]]] = {}
    labelled_candidates = 0
    for tree in trees.values():
        nonedges = [
            (left, right)
            for left in range(RANK)
            for right in range(left + 1, RANK)
            if not tree[left][right]
        ]
        for first, second in itertools.combinations(nonedges, 2):
            candidate = add_edges(tree, first, second)
            output.setdefault(independent_code(candidate), candidate)
            labelled_candidates += 1
    if len(output) != EXPECTED_BICYCLIC:
        raise AssertionError(f"independent generator found {len(output)} bicyclic graphs")
    return output, {
        "route": "independent free-tree leaf extension plus two nonedges",
        "labelled_candidates": labelled_candidates,
        "free_tree_counts": free_counts,
        "rooted_tree_counts": rooted_counts,
    }


def adjacency_from_edges(raw: object) -> list[list[int]]:
    if not isinstance(raw, list):
        raise ValueError("source edge list is not a list")
    adjacency = [[0] * RANK for _ in range(RANK)]
    seen = set()
    for edge in raw:
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError("malformed source edge")
        left, right = map(int, edge)
        if not 0 <= left < right < RANK or (left, right) in seen:
            raise ValueError("invalid source edge")
        seen.add((left, right))
        adjacency[left][right] = adjacency[right][left] = 1
    if len(seen) != RANK + 1:
        raise ValueError("source core does not have eleven edges")
    independent_code(adjacency)
    return adjacency


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--expected-source-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    source_hash = sha256(args.source)
    if source_hash != args.expected_source_sha256:
        raise ValueError("source SHA-256 mismatch")
    source = json.loads(args.source.read_text(encoding="utf-8"))
    if source.get("counterexample_candidate_found") is not False:
        raise ValueError("source does not contain the expected negative conclusion")
    if source.get("all_domain_processed") is not True or source.get("exact_search_enabled") is not True:
        raise ValueError("source domain or exact search is incomplete")
    if int(source.get("target_noncore_clique_size", -1)) != TARGET:
        raise ValueError("source target mismatch")
    records = source.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_BICYCLIC:
        raise ValueError("source record count mismatch")

    generated, generation_report = independent_domain()
    source_by_code: dict[str, dict[str, object]] = {}
    for expected_index, record in enumerate(records):
        if int(record.get("bicyclic_index", -1)) != expected_index:
            raise ValueError("source indices are incomplete or reordered")
        core = adjacency_from_edges(record.get("canonical_edge_list"))
        code = independent_code(core)
        if code in source_by_code:
            raise ValueError("two source records are independently isomorphic")
        source_by_code[code] = record
    if set(source_by_code) != set(generated):
        raise ValueError("source edge lists differ from the independent bicyclic domain")

    engine_test = selftest()
    nonsingular = 0
    total_calls = 0
    determinant_counts: dict[int, int] = {}
    verified = []
    for position, code in enumerate(sorted(generated), 1):
        core = generated[code]
        record = source_by_code[code]
        det = determinant(core)
        determinant_counts[det] = determinant_counts.get(det, 0) + 1
        if det != int(record.get("determinant", 10**9)):
            raise ValueError("independent determinant disagrees with source")
        singular = det == 0
        if singular != bool(record.get("singular")):
            raise ValueError("source singularity mismatch")
        entry: dict[str, object] = {
            "independent_code": code,
            "source_index": record["bicyclic_index"],
            "determinant": det,
            "singular": singular,
        }
        if not singular:
            nonsingular += 1
            adj = adjugate(core)
            identity = [[det * int(i == j) for j in range(RANK)] for i in range(RANK)]
            if multiply(core, adj) != identity or multiply(adj, core) != identity:
                raise AssertionError("independent adjugate identity failed")
            profiles, graph, edge_count = profile_graph(core, det, adj)
            if len(profiles) != int(record.get("noncore_isotropic_count", -1)):
                raise ValueError("source profile count mismatch")
            if edge_count != int(record.get("compatibility_edge_count", -1)):
                raise ValueError("source compatibility edge count mismatch")
            relabelled = permute_graph(graph, 1, 2)
            decision = TargetSearch(relabelled, TARGET)
            if decision.solve():
                raise ValueError("independent verifier found a forbidden 53-clique")
            if record.get("target_clique_found") is not False:
                raise ValueError("source target conclusion mismatch")
            total_calls += decision.calls
            entry.update(
                {
                    "noncore_isotropic_count": len(profiles),
                    "compatibility_edge_count": edge_count,
                    "target": TARGET,
                    "target_clique_found": False,
                    "independent_calls": decision.calls,
                    "cardinality_prunes": decision.cardinality_prunes,
                    "colour_prunes": decision.colour_prunes,
                }
            )
        entry["status"] = "PASS"
        verified.append(entry)
        if not args.quiet or position % 100 == 0 or position == EXPECTED_BICYCLIC:
            print(
                f"VERIFY BICYCLIC {position}/{EXPECTED_BICYCLIC} "
                f"nonsingular={nonsingular}",
                flush=True,
            )

    if nonsingular != EXPECTED_NONSINGULAR:
        raise ValueError("independent nonsingular count mismatch")
    if nonsingular != int(source.get("nonsingular_cores_processed", -1)):
        raise ValueError("source nonsingular aggregate mismatch")
    payload = {
        "schema": "reduced-graph-rank10.bicyclic-core-independent-audit.v1",
        "status": "PASS",
        "source": str(args.source),
        "source_sha256": source_hash,
        "arithmetic": "integers only; Bareiss determinants, cofactor adjugates, exact bitset search",
        "independent_generation": generation_report,
        "source_edge_lists_match_independent_isomorphism_set": True,
        "bicyclic_graphs": len(verified),
        "nonsingular_cores": nonsingular,
        "singular_cores": len(verified) - nonsingular,
        "determinant_distribution": {
            str(key): determinant_counts[key] for key in sorted(determinant_counts)
        },
        "all_nonsingular_cores_exclude_noncore_clique_size": TARGET,
        "independent_search_total_calls": total_calls,
        "search_engine_selftest": engine_test,
        "counterexample_found": False,
        "records": verified,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
