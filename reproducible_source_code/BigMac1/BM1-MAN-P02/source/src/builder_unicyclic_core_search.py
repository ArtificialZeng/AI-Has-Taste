#!/usr/bin/env python3
"""Exact rank-10 extension search over all ten-vertex unicyclic cores.

The discovery domain is generated twice.  First, every nonedge is added to
every unlabelled ten-vertex tree.  Secondly, a cycle of length 3 through 10 is
decorated by rooted unlabelled trees whose total order is ten.  A canonical
dihedral word for the unique cycle proves that the two routes give the same
isomorphism set.

For every nonsingular core B, all nonzero binary isotropic profiles are
constructed from the exact scaled inverse of B.  A reduced rank-ten graph of
order at least 63 containing B would yield 53 pairwise compatible noncore
profiles.  The script therefore searches exactly for a 53-clique, freezing a
complete adjacency-matrix candidate immediately if one is found.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Sequence

from builder_core_deformation_search import (
    TARGET_NONCORE,
    build_compatibility,
    greedy_clique,
)
from builder_tree_core_search import (
    TargetDecisionTranscript,
    colour_partition,
    determinant_bareiss,
    edge_list,
    explicit_candidate,
    generate_free_trees,
    generate_rooted_codes,
    graph6,
    parse_rooted,
    rooted_to_adjacency,
)


RANK = 10


def neighbours(adjacency: Sequence[Sequence[int]], vertex: int) -> list[int]:
    return [index for index, value in enumerate(adjacency[vertex]) if value]


def cycle_vertices(adjacency: Sequence[Sequence[int]]) -> set[int]:
    """Return the unique cycle by deleting leaves."""
    order = len(adjacency)
    degree = [sum(map(int, row)) for row in adjacency]
    active = [True] * order
    stack = [vertex for vertex, value in enumerate(degree) if value == 1]
    while stack:
        leaf = stack.pop()
        if not active[leaf]:
            continue
        active[leaf] = False
        for vertex, value in enumerate(adjacency[leaf]):
            if value and active[vertex]:
                degree[vertex] -= 1
                if degree[vertex] == 1:
                    stack.append(vertex)
    cycle = {vertex for vertex, flag in enumerate(active) if flag}
    if len(cycle) < 3:
        raise ValueError("graph has no simple cycle")
    if any(sum(adjacency[v][w] for w in cycle) != 2 for v in cycle):
        raise ValueError("cycle core is not 2-regular")
    return cycle


def rooted_branch_code(
    adjacency: Sequence[Sequence[int]], root: int, parent: int, cycle: set[int]
) -> str:
    branches = [
        rooted_branch_code(adjacency, child, root, cycle)
        for child in neighbours(adjacency, root)
        if child != parent and child not in cycle
    ]
    return "(" + "".join(sorted(branches)) + ")"


def dihedral_minimum(words: Sequence[str]) -> tuple[str, ...]:
    if len(words) < 3:
        raise ValueError("a simple cycle needs at least three vertices")
    forward = tuple(words)
    reverse = tuple(reversed(words))
    candidates = []
    for sequence in (forward, reverse):
        candidates.extend(sequence[offset:] + sequence[:offset] for offset in range(len(sequence)))
    return min(candidates)


def unicyclic_code(adjacency: Sequence[Sequence[int]]) -> str:
    order = len(adjacency)
    edges = sum(sum(map(int, row)) for row in adjacency) // 2
    if edges != order:
        raise ValueError("connected unicyclic graph must have order many edges")
    cycle = cycle_vertices(adjacency)
    start = min(cycle)
    cycle_neighbours = sorted(v for v in neighbours(adjacency, start) if v in cycle)
    previous = start
    current = cycle_neighbours[0]
    cyclic_order = [start]
    while current != start:
        cyclic_order.append(current)
        next_vertices = [
            vertex
            for vertex in neighbours(adjacency, current)
            if vertex in cycle and vertex != previous
        ]
        if len(next_vertices) != 1:
            raise ValueError("failed to trace the unique cycle")
        previous, current = current, next_vertices[0]
    if len(cyclic_order) != len(cycle):
        raise ValueError("cycle trace did not visit every cycle vertex")
    words = [rooted_branch_code(adjacency, vertex, -1, cycle) for vertex in cyclic_order]
    canonical = dihedral_minimum(words)
    return f"U{len(canonical)}:" + "|".join(canonical)


def canonical_unicyclic_adjacency(code: str) -> list[list[int]]:
    if not code.startswith("U") or ":" not in code:
        raise ValueError("bad unicyclic code")
    prefix, raw = code.split(":", 1)
    cycle_length = int(prefix[1:])
    words = raw.split("|")
    if len(words) != cycle_length:
        raise ValueError("cycle length and branch count disagree")
    pieces: list[tuple[list[list[int]], int]] = []
    for word in words:
        tree, end = parse_rooted(word)
        if end != len(word):
            raise ValueError("trailing rooted-tree data")
        pieces.append(rooted_to_adjacency(tree))
    order = sum(len(adjacency) for adjacency, _ in pieces)
    result = [[0] * order for _ in range(order)]
    roots: list[int] = []
    offset = 0
    for adjacency, root in pieces:
        roots.append(offset + root)
        for i in range(len(adjacency)):
            for j in range(len(adjacency)):
                result[offset + i][offset + j] = adjacency[i][j]
        offset += len(adjacency)
    for index, left in enumerate(roots):
        right = roots[(index + 1) % cycle_length]
        result[left][right] = result[right][left] = 1
    if unicyclic_code(result) != code:
        raise AssertionError("unicyclic canonical round trip failed")
    return result


def add_edge(adjacency: Sequence[Sequence[int]], i: int, j: int) -> list[list[int]]:
    result = [list(map(int, row)) for row in adjacency]
    if i == j or result[i][j]:
        raise ValueError("edge to add must be a nonedge")
    result[i][j] = result[j][i] = 1
    return result


def generate_from_trees() -> set[str]:
    codes: set[str] = set()
    for _, tree in generate_free_trees(RANK):
        for i in range(RANK):
            for j in range(i + 1, RANK):
                if not tree[i][j]:
                    codes.add(unicyclic_code(add_edge(tree, i, j)))
    return codes


def generate_from_cycle_decorations() -> set[str]:
    rooted = generate_rooted_codes(RANK - 2)
    catalog = sorted(
        (code, order)
        for order in range(1, RANK - 1)
        for code in rooted[order]
    )
    codes: set[str] = set()
    for cycle_length in range(3, RANK + 1):
        def extend(position: int, remaining: int, words: list[str]) -> None:
            slots = cycle_length - position
            if slots == 0:
                if remaining == 0:
                    canonical = dihedral_minimum(words)
                    codes.add(f"U{cycle_length}:" + "|".join(canonical))
                return
            if remaining < slots:
                return
            for word, size in catalog:
                if size > remaining - (slots - 1):
                    continue
                words.append(word)
                extend(position + 1, remaining - size, words)
                words.pop()

        extend(0, RANK, [])
    return codes


def generate_unicyclic_graphs() -> list[tuple[str, list[list[int]]]]:
    from_trees = generate_from_trees()
    from_cycles = generate_from_cycle_decorations()
    if from_trees != from_cycles:
        missing = sorted(from_trees - from_cycles)[:3]
        extra = sorted(from_cycles - from_trees)[:3]
        raise AssertionError(f"generation routes disagree: missing={missing}, extra={extra}")
    graphs = [(code, canonical_unicyclic_adjacency(code)) for code in sorted(from_trees)]
    for code, adjacency in graphs:
        if len(adjacency) != RANK:
            raise AssertionError("wrong graph order")
        if sum(sum(row) for row in adjacency) // 2 != RANK:
            raise AssertionError("wrong unicyclic edge count")
        if unicyclic_code(adjacency) != code:
            raise AssertionError("canonical code mismatch")
    return graphs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("work/builder/unicyclic_core_exact_search.json"))
    parser.add_argument(
        "--candidate-output",
        type=Path,
        default=Path("work/builder/unicyclic_core_counterexample_candidate.json"),
    )
    parser.add_argument("--seed", type=int, default=20260827)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--no-exact", action="store_true")
    args = parser.parse_args()

    graphs = generate_unicyclic_graphs()
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
            "unicyclic_index": index,
            "canonical_code": code,
            "canonical_graph6": graph6(core),
            "canonical_edge_list": edge_list(core),
            "cycle_length": len(cycle_vertices(core)),
            "determinant": determinant,
            "singular": determinant == 0,
        }
        print(f"BEGIN unicyclic {index + 1}/{len(graphs)} det={determinant}", flush=True)
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
                candidate["unicyclic_metadata"] = {
                    "unicyclic_index": index,
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
        print(
            f"END unicyclic {index + 1} singular={record['singular']} "
            f"mode={record.get('proof_mode')} found={record.get('target_clique_found')}",
            flush=True,
        )

    payload = {
        "schema_version": 1,
        "theorem_scope": (
            "reduced rank-10 graphs containing a nonsingular induced principal "
            "core isomorphic to a connected ten-vertex unicyclic graph"
        ),
        "generation": {
            "tree_plus_nonedge_count": len(graphs),
            "cycle_decoration_count": len(graphs),
            "routes_agree": True,
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
