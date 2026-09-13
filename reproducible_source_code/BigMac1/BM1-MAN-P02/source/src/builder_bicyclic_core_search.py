#!/usr/bin/env python3
"""Exact rank-10 extension search over all ten-vertex bicyclic cores.

Two complete generation routes are compared before any rank calculation:
add one nonedge to every unlabelled connected unicyclic graph, and add two
nonedges to every unlabelled tree.  Isomorphism classes are identified by a
structural canonical code for the leaf-pruned two-core.  A connected simple
bicyclic two-core is exactly one of a theta, figure-eight, or dumbbell core.

For each nonsingular core, the standard exact binary-profile gate searches
for 53 compatible noncore profiles.  Such a clique, together with the ten
core columns, would give the requested order-63 counterexample.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Iterable, Sequence

from builder_core_deformation_search import TARGET_NONCORE, build_compatibility, greedy_clique
from builder_tree_core_search import (
    TargetDecisionTranscript,
    colour_partition,
    determinant_bareiss,
    edge_list,
    explicit_candidate,
    generate_free_trees,
    graph6,
)
from builder_unicyclic_core_search import add_edge, generate_unicyclic_graphs, rooted_branch_code


RANK = 10


def neighbours(adjacency: Sequence[Sequence[int]], vertex: int, allowed: set[int] | None = None) -> list[int]:
    return [
        index
        for index, value in enumerate(adjacency[vertex])
        if value and (allowed is None or index in allowed)
    ]


def connected_components(adjacency: Sequence[Sequence[int]], vertices: Iterable[int]) -> list[set[int]]:
    remaining = set(vertices)
    output: list[set[int]] = []
    while remaining:
        start = min(remaining)
        component = {start}
        stack = [start]
        remaining.remove(start)
        while stack:
            vertex = stack.pop()
            for child in neighbours(adjacency, vertex):
                if child in remaining:
                    remaining.remove(child)
                    component.add(child)
                    stack.append(child)
        output.append(component)
    return output


def two_core(adjacency: Sequence[Sequence[int]]) -> set[int]:
    degree = [sum(map(int, row)) for row in adjacency]
    alive = [True] * len(adjacency)
    stack = [vertex for vertex, value in enumerate(degree) if value <= 1]
    while stack:
        vertex = stack.pop()
        if not alive[vertex]:
            continue
        alive[vertex] = False
        for child, value in enumerate(adjacency[vertex]):
            if value and alive[child]:
                degree[child] -= 1
                if degree[child] == 1:
                    stack.append(child)
    core = {vertex for vertex, flag in enumerate(alive) if flag}
    if not core:
        raise ValueError("bicyclic graph has empty two-core")
    return core


def is_connected_without_edge(
    adjacency: Sequence[Sequence[int]], core: set[int], forbidden: tuple[int, int]
) -> bool:
    start = min(core)
    reached = {start}
    stack = [start]
    while stack:
        vertex = stack.pop()
        for child in neighbours(adjacency, vertex, core):
            if {vertex, child} == set(forbidden):
                continue
            if child not in reached:
                reached.add(child)
                stack.append(child)
    return reached == core


def core_bridges(adjacency: Sequence[Sequence[int]], core: set[int]) -> set[tuple[int, int]]:
    edges = {
        (left, right)
        for left in core
        for right in core
        if left < right and adjacency[left][right]
    }
    return {
        edge for edge in edges if not is_connected_without_edge(adjacency, core, edge)
    }


def trace_path(
    adjacency: Sequence[Sequence[int]], vertices: set[int], start: int, finish: int
) -> list[int]:
    if start == finish:
        return [start]
    path = [start]
    previous = -1
    current = start
    while current != finish:
        choices = [
            child
            for child in neighbours(adjacency, current, vertices)
            if child != previous
        ]
        if len(choices) != 1:
            raise ValueError("component is not a path")
        previous, current = current, choices[0]
        if current in path:
            raise ValueError("path trace repeated a vertex")
        path.append(current)
    if set(path) != vertices:
        raise ValueError("path trace missed component vertices")
    return path


def canonical_json(value: object) -> str:
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def bicyclic_code(adjacency: Sequence[Sequence[int]]) -> str:
    order = len(adjacency)
    edges = sum(sum(map(int, row)) for row in adjacency) // 2
    if edges != order + 1:
        raise ValueError("connected bicyclic graph must have order plus one edges")
    reached = connected_components(adjacency, range(order))
    if len(reached) != 1:
        raise ValueError("bicyclic graph must be connected")

    core = two_core(adjacency)
    core_edges = sum(adjacency[i][j] for i in core for j in core if i < j)
    if core_edges != len(core) + 1:
        raise ValueError("two-core has wrong cyclomatic number")
    branch = {
        vertex: rooted_branch_code(adjacency, vertex, -1, core)
        for vertex in core
    }
    degrees = {vertex: len(neighbours(adjacency, vertex, core)) for vertex in core}
    exceptional = sorted(vertex for vertex, degree in degrees.items() if degree > 2)

    if len(exceptional) == 1 and degrees[exceptional[0]] == 4:
        center = exceptional[0]
        components = connected_components(adjacency, core - {center})
        if len(components) != 2:
            raise ValueError("figure-eight core must split into two paths")
        cycles = []
        for component in components:
            endpoints = sorted(
                vertex for vertex in component if adjacency[center][vertex]
            )
            if len(endpoints) != 2:
                raise ValueError("figure-eight path has wrong center attachments")
            path = trace_path(adjacency, component, endpoints[0], endpoints[1])
            word = tuple(branch[vertex] for vertex in path)
            cycles.append(min(word, tuple(reversed(word))))
        return canonical_json(["F", branch[center], sorted(cycles)])

    if len(exceptional) != 2 or any(degrees[vertex] != 3 for vertex in exceptional):
        raise ValueError("bicyclic two-core has invalid excess-degree pattern")
    left, right = exceptional
    bridges = core_bridges(adjacency, core)

    if not bridges:
        interiors: list[tuple[str, ...]] = []
        if adjacency[left][right]:
            interiors.append(tuple())
        for component in connected_components(adjacency, core - {left, right}):
            left_ends = [vertex for vertex in component if adjacency[left][vertex]]
            right_ends = [vertex for vertex in component if adjacency[right][vertex]]
            if len(left_ends) != 1 or len(right_ends) != 1:
                raise ValueError("theta path has wrong endpoint attachments")
            path = trace_path(adjacency, component, left_ends[0], right_ends[0])
            interiors.append(tuple(branch[vertex] for vertex in path))
        if len(interiors) != 3:
            raise ValueError("theta core must have three paths")
        forward = ["T", branch[left], sorted(interiors), branch[right]]
        reverse = [
            "T",
            branch[right],
            sorted(tuple(reversed(word)) for word in interiors),
            branch[left],
        ]
        return min(canonical_json(forward), canonical_json(reverse))

    bridge_adjacency = {vertex: [] for vertex in core}
    for left_edge, right_edge in bridges:
        bridge_adjacency[left_edge].append(right_edge)
        bridge_adjacency[right_edge].append(left_edge)
    bridge_vertices = {vertex for vertex, row in bridge_adjacency.items() if row}
    bridge_path = trace_path_from_lists(bridge_adjacency, bridge_vertices, left, right)

    bridge_deleted_components = components_without_edges(adjacency, core, bridges)
    left_component = next(piece for piece in bridge_deleted_components if left in piece)
    right_component = next(piece for piece in bridge_deleted_components if right in piece)
    if left_component == right_component:
        raise ValueError("dumbbell cycles did not separate after deleting bridges")
    cycle_components = [left_component, right_component]
    bridge_internal = set(bridge_path[1:-1])
    leftovers = set().union(
        *(piece for piece in bridge_deleted_components if piece not in cycle_components)
    ) if len(bridge_deleted_components) > 2 else set()
    if leftovers != bridge_internal:
        raise ValueError("bridge deletion produced unexpected components")

    def cycle_word(endpoint: int) -> tuple[str, ...]:
        component = next(piece for piece in cycle_components if endpoint in piece)
        cycle_neighbours = neighbours_without_edges(adjacency, endpoint, component, bridges)
        if len(cycle_neighbours) != 2:
            raise ValueError("dumbbell endpoint has wrong cycle degree")
        words = []
        for start in cycle_neighbours:
            sequence = []
            previous = endpoint
            current = start
            while current != endpoint:
                sequence.append(branch[current])
                choices = [
                    child
                    for child in neighbours_without_edges(adjacency, current, component, bridges)
                    if child != previous
                ]
                if len(choices) != 1:
                    raise ValueError("failed to trace dumbbell cycle")
                previous, current = current, choices[0]
            words.append(tuple(sequence))
        return min(words)

    bridge_interior = tuple(branch[vertex] for vertex in bridge_path[1:-1])
    forward = [
        "D",
        cycle_word(left),
        branch[left],
        bridge_interior,
        branch[right],
        cycle_word(right),
    ]
    reverse = [
        "D",
        cycle_word(right),
        branch[right],
        tuple(reversed(bridge_interior)),
        branch[left],
        cycle_word(left),
    ]
    return min(canonical_json(forward), canonical_json(reverse))


def neighbours_without_edges(
    adjacency: Sequence[Sequence[int]], vertex: int, allowed: set[int], forbidden: set[tuple[int, int]]
) -> list[int]:
    return [
        child
        for child in neighbours(adjacency, vertex, allowed)
        if (min(vertex, child), max(vertex, child)) not in forbidden
    ]


def components_without_edges(
    adjacency: Sequence[Sequence[int]], vertices: set[int], forbidden: set[tuple[int, int]]
) -> list[set[int]]:
    remaining = set(vertices)
    output = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        component = {start}
        stack = [start]
        while stack:
            vertex = stack.pop()
            for child in neighbours_without_edges(adjacency, vertex, vertices, forbidden):
                if child in remaining:
                    remaining.remove(child)
                    component.add(child)
                    stack.append(child)
        output.append(component)
    return output


def trace_path_from_lists(
    adjacency: dict[int, list[int]], vertices: set[int], start: int, finish: int
) -> list[int]:
    path = [start]
    previous = -1
    current = start
    while current != finish:
        choices = [child for child in adjacency[current] if child != previous]
        if len(choices) != 1:
            raise ValueError("bridge subgraph is not a path")
        previous, current = current, choices[0]
        if current in path:
            raise ValueError("bridge path repeated a vertex")
        path.append(current)
    if set(path) != vertices:
        raise ValueError("bridge path missed bridge vertices")
    return path


def generate_from_unicyclic() -> dict[str, list[list[int]]]:
    output: dict[str, list[list[int]]] = {}
    for _, graph in generate_unicyclic_graphs():
        for left in range(RANK):
            for right in range(left + 1, RANK):
                if not graph[left][right]:
                    candidate = add_edge(graph, left, right)
                    output.setdefault(bicyclic_code(candidate), candidate)
    return output


def generate_from_trees() -> dict[str, list[list[int]]]:
    output: dict[str, list[list[int]]] = {}
    for _, tree in generate_free_trees(RANK):
        nonedges = [
            (left, right)
            for left in range(RANK)
            for right in range(left + 1, RANK)
            if not tree[left][right]
        ]
        for first_index, first in enumerate(nonedges):
            for second in nonedges[first_index + 1 :]:
                candidate = add_edge(add_edge(tree, *first), *second)
                output.setdefault(bicyclic_code(candidate), candidate)
    return output


def generate_bicyclic_graphs() -> list[tuple[str, list[list[int]]]]:
    from_unicyclic = generate_from_unicyclic()
    from_trees = generate_from_trees()
    if set(from_unicyclic) != set(from_trees):
        missing = sorted(set(from_unicyclic) - set(from_trees))[:3]
        extra = sorted(set(from_trees) - set(from_unicyclic))[:3]
        raise AssertionError(f"bicyclic generation routes disagree: missing={missing}, extra={extra}")
    graphs = sorted(from_unicyclic.items())
    for code, adjacency in graphs:
        if len(adjacency) != RANK or sum(sum(row) for row in adjacency) // 2 != RANK + 1:
            raise AssertionError("wrong bicyclic order or size")
        if bicyclic_code(adjacency) != code:
            raise AssertionError("bicyclic canonical round trip failed")
    return graphs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("work/builder/bicyclic_core_exact_search.json"))
    parser.add_argument(
        "--candidate-output",
        type=Path,
        default=Path("work/builder/bicyclic_core_counterexample_candidate.json"),
    )
    parser.add_argument("--seed", type=int, default=20260827)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--no-exact", action="store_true")
    parser.add_argument("--generate-only", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    graphs = generate_bicyclic_graphs()
    type_counts: dict[str, int] = {}
    for code, _ in graphs:
        kind = json.loads(code)[0]
        type_counts[kind] = type_counts.get(kind, 0) + 1
    if args.generate_only:
        print(json.dumps({"bicyclic_isomorphism_count": len(graphs), "type_counts": type_counts}, indent=2))
        return

    stop = len(graphs) if args.stop is None else min(args.stop, len(graphs))
    if not 0 <= args.start <= stop:
        raise ValueError("invalid start/stop interval")
    records: list[dict[str, object]] = []
    candidate: dict[str, object] | None = None
    nonsingular = 0
    started = time.monotonic()
    for index in range(args.start, stop):
        code, core = graphs[index]
        determinant = determinant_bareiss(core)
        record: dict[str, object] = {
            "bicyclic_index": index,
            "canonical_code": code,
            "canonical_graph6": graph6(core),
            "canonical_edge_list": edge_list(core),
            "core_type": json.loads(code)[0],
            "determinant": determinant,
            "singular": determinant == 0,
        }
        if not args.quiet:
            print(f"BEGIN bicyclic {index + 1}/{len(graphs)} det={determinant}", flush=True)
        if determinant:
            nonsingular += 1
            built = build_compatibility(core)
            if built is None:
                raise AssertionError("determinant and inverse disagree")
            masks, adjacency, core_masks, compatibility_edges = built
            colours = colour_partition(adjacency)
            greedy = greedy_clique(adjacency, args.seed + index)
            record.update(
                {
                    "noncore_isotropic_count": len(masks),
                    "compatibility_edge_count": compatibility_edges,
                    "root_greedy_colour_upper_bound": len(colours),
                    "greedy_clique_size": len(greedy),
                }
            )
            witness = greedy if len(greedy) >= TARGET_NONCORE else None
            if witness is not None:
                record["proof_mode"] = "target_witness_from_greedy"
            elif len(colours) < TARGET_NONCORE:
                record["proof_mode"] = "root_proper_colouring"
                record["root_colour_classes_by_column_mask"] = [
                    [masks[vertex] for vertex in colour] for colour in colours
                ]
            elif args.no_exact:
                record["proof_mode"] = "exact_search_not_run"
            else:
                solver = TargetDecisionTranscript(adjacency, TARGET_NONCORE)
                witness = solver.solve()
                record["proof_mode"] = "complete_exact_target_search"
                record["branch_and_bound"] = {
                    "target": TARGET_NONCORE,
                    "nodes": solver.nodes,
                    "prunes": solver.prunes,
                    "transcript_sha256": solver.digest.hexdigest(),
                    "vertex_order": "increasing binary column mask",
                    "colour_class_vertex_order": "least current index",
                }
            record["target_clique_found"] = witness is not None
            if witness is not None:
                candidate = explicit_candidate(core, core_masks, masks, witness)
                candidate["bicyclic_metadata"] = {
                    "bicyclic_index": index,
                    "canonical_code": code,
                    "canonical_graph6": record["canonical_graph6"],
                    "canonical_edge_list": record["canonical_edge_list"],
                }
                args.candidate_output.parent.mkdir(parents=True, exist_ok=True)
                args.candidate_output.write_text(json.dumps(candidate, indent=2) + "\n", encoding="utf-8")
                records.append(record)
                print(f"FROZEN CANDIDATE {args.candidate_output}", flush=True)
                break
        records.append(record)
        if not args.quiet:
            print(
                f"END bicyclic {index + 1} singular={record['singular']} "
                f"mode={record.get('proof_mode')} found={record.get('target_clique_found')}",
                flush=True,
            )
        elif (index + 1) % 100 == 0 or index + 1 == stop:
            print(
                f"PROGRESS {index + 1}/{stop} nonsingular={nonsingular} "
                f"candidate={candidate is not None}",
                flush=True,
            )

    payload = {
        "schema_version": 1,
        "theorem_scope": (
            "reduced rank-10 graphs containing a nonsingular induced principal "
            "core isomorphic to a connected ten-vertex bicyclic graph"
        ),
        "generation": {
            "unicyclic_plus_nonedge_count": len(graphs),
            "tree_plus_two_nonedges_count": len(graphs),
            "routes_agree": True,
            "type_counts": type_counts,
        },
        "domain_start": args.start,
        "domain_stop": stop,
        "all_domain_processed": args.start == 0 and stop == len(graphs) and len(records) == len(graphs),
        "nonsingular_cores_processed": nonsingular,
        "target_noncore_clique_size": TARGET_NONCORE,
        "exact_search_enabled": not args.no_exact,
        "counterexample_candidate_found": candidate is not None,
        "candidate_path": str(args.candidate_output) if candidate is not None else None,
        "elapsed_seconds": time.monotonic() - started,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "records"}, indent=2))
    print(f"output={args.output}", flush=True)


if __name__ == "__main__":
    main()
