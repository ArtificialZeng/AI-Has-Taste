#!/usr/bin/env python3
"""Exact rank-10 extension search over all ten-vertex tree cores.

The script generates the 106 unlabelled free trees on ten vertices without
external graph packages.  Generation is independently self-checked against
the classical rooted-tree counts 1,1,2,4,9,20,48,115,286,719 and the free
tree count 106.  Each free tree receives an AHU canonical code, a
deterministically labelled graph6 string, and an edge list.

For every nonsingular tree adjacency matrix B, the rank-preserving extension
model is exact.  A new vertex is represented by a nonzero binary column y,
looplessness is y^T B^{-1} y = 0, and two columns are compatible precisely
when y^T B^{-1} z is 0 or 1.  Since the ten columns of B are universal in the
compatibility graph, a reduced graph of order at least 63 containing B would
give a clique of 53 noncore columns.

If a root greedy colouring has fewer than 53 colours, its colour classes are
serialized as a directly checkable upper-bound certificate.  Otherwise a
complete exact target-clique search is run and a deterministic transcript
commitment is recorded for independent replay.  Discovery of a 53-clique
immediately freezes an explicit integer adjacency matrix candidate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
from pathlib import Path
from typing import Sequence

from builder_core_deformation_search import (
    TARGET_NONCORE,
    build_compatibility,
    greedy_clique,
    scaled_inverse,
)


RANK = 10
EXPECTED_ROOTED_COUNTS = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719]
EXPECTED_FREE_COUNTS = [0, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106]
EXPECTED_FREE_COUNT = 106


RootedTree = tuple["RootedTree", ...]


def parse_rooted(code: str, start: int = 0) -> tuple[RootedTree, int]:
    if start >= len(code) or code[start] != "(":
        raise ValueError("bad rooted-tree code")
    children: list[RootedTree] = []
    position = start + 1
    while position < len(code) and code[position] != ")":
        child, position = parse_rooted(code, position)
        children.append(child)
    if position >= len(code):
        raise ValueError("unterminated rooted-tree code")
    return tuple(children), position + 1


def rooted_code(tree: RootedTree) -> str:
    return "(" + "".join(sorted(rooted_code(child) for child in tree)) + ")"


def generate_rooted_codes(max_order: int) -> list[set[str]]:
    """Generate rooted unlabelled trees by multisets of rooted branches."""
    by_order: list[set[str]] = [set() for _ in range(max_order + 1)]
    by_order[1].add("()")
    for order in range(2, max_order + 1):
        catalog = sorted(
            ((code, size) for size in range(1, order) for code in by_order[size]),
            key=lambda item: item[0],
        )
        output: set[str] = set()

        def choose(start: int, remaining: int, children: list[str]) -> None:
            if remaining == 0:
                output.add("(" + "".join(children) + ")")
                return
            for index in range(start, len(catalog)):
                code, size = catalog[index]
                if size <= remaining:
                    children.append(code)
                    choose(index, remaining - size, children)
                    children.pop()

        choose(0, order - 1, [])
        by_order[order] = output
        expected = EXPECTED_ROOTED_COUNTS[order]
        if len(output) != expected:
            raise AssertionError(
                f"rooted-tree generator failed at order {order}: "
                f"got {len(output)}, expected {expected}"
            )
    return by_order


def rooted_to_adjacency(tree: RootedTree) -> tuple[list[list[int]], int]:
    adjacency_lists: list[list[int]] = []

    def add(subtree: RootedTree) -> int:
        root = len(adjacency_lists)
        adjacency_lists.append([])
        for child in subtree:
            child_root = add(child)
            adjacency_lists[root].append(child_root)
            adjacency_lists[child_root].append(root)
        return root

    root = add(tree)
    order = len(adjacency_lists)
    adjacency = [[0] * order for _ in range(order)]
    for i, neighbours in enumerate(adjacency_lists):
        for j in neighbours:
            adjacency[i][j] = 1
    return adjacency, root


def tree_centres(adjacency: Sequence[Sequence[int]]) -> list[int]:
    order = len(adjacency)
    degrees = [sum(row) for row in adjacency]
    active = [True] * order
    leaves = [i for i, degree in enumerate(degrees) if degree <= 1]
    remaining = order
    while remaining > 2:
        current = leaves
        leaves = []
        remaining -= len(current)
        for leaf in current:
            active[leaf] = False
            for neighbour, value in enumerate(adjacency[leaf]):
                if value and active[neighbour]:
                    degrees[neighbour] -= 1
                    if degrees[neighbour] == 1:
                        leaves.append(neighbour)
    return [i for i, flag in enumerate(active) if flag]


def rooted_at(adjacency: Sequence[Sequence[int]], root: int, parent: int) -> str:
    children = [
        rooted_at(adjacency, child, root)
        for child, value in enumerate(adjacency[root])
        if value and child != parent
    ]
    return "(" + "".join(sorted(children)) + ")"


def free_tree_code(adjacency: Sequence[Sequence[int]]) -> str:
    centres = tree_centres(adjacency)
    if len(centres) == 1:
        return "U" + rooted_at(adjacency, centres[0], -1)
    if len(centres) != 2 or not adjacency[centres[0]][centres[1]]:
        raise AssertionError("tree centre computation failed")
    left = rooted_at(adjacency, centres[0], centres[1])
    right = rooted_at(adjacency, centres[1], centres[0])
    first, second = sorted((left, right))
    return "B" + first + "|" + second


def canonical_adjacency(code: str) -> list[list[int]]:
    """Decode an AHU free-tree code to one deterministic labelled tree."""
    if code.startswith("U"):
        tree, end = parse_rooted(code, 1)
        if end != len(code):
            raise ValueError("trailing data in unicentred code")
        adjacency, _ = rooted_to_adjacency(tree)
        return adjacency
    if not code.startswith("B") or "|" not in code:
        raise ValueError("bad free-tree code")
    left_code, right_code = code[1:].split("|", 1)
    left, left_end = parse_rooted(left_code)
    right, right_end = parse_rooted(right_code)
    if left_end != len(left_code) or right_end != len(right_code):
        raise ValueError("trailing data in bicentred code")
    left_adjacency, left_root = rooted_to_adjacency(left)
    right_adjacency, right_root = rooted_to_adjacency(right)
    left_order = len(left_adjacency)
    order = left_order + len(right_adjacency)
    adjacency = [[0] * order for _ in range(order)]
    for i in range(left_order):
        for j in range(left_order):
            adjacency[i][j] = left_adjacency[i][j]
    for i in range(len(right_adjacency)):
        for j in range(len(right_adjacency)):
            adjacency[left_order + i][left_order + j] = right_adjacency[i][j]
    right_root += left_order
    adjacency[left_root][right_root] = 1
    adjacency[right_root][left_root] = 1
    return adjacency


def generate_free_trees(order: int = RANK) -> list[tuple[str, list[list[int]]]]:
    """Generate free trees by adding one leaf and AHU deduplication.

    The generation route requested for the finite structural class is the
    classical leaf-extension recursion.  Rooted-tree generation above is
    retained as an independent cross-check on the final canonical-code set.
    """
    rooted = generate_rooted_codes(order)
    rooted_free_codes: set[str] = set()
    for code in rooted[order]:
        tree, end = parse_rooted(code)
        if end != len(code) or rooted_code(tree) != code:
            raise AssertionError("rooted-tree round trip failed")
        adjacency, _ = rooted_to_adjacency(tree)
        rooted_free_codes.add(free_tree_code(adjacency))

    layer: dict[str, list[list[int]]] = {"U()": [[0]]}
    if EXPECTED_FREE_COUNTS[1] != len(layer):
        raise AssertionError("order-one free-tree count failed")
    for size in range(2, order + 1):
        next_layer: dict[str, list[list[int]]] = {}
        for adjacency in layer.values():
            for parent in range(size - 1):
                extended = [row + [0] for row in adjacency]
                extended.append([0] * size)
                extended[parent][size - 1] = 1
                extended[size - 1][parent] = 1
                code = free_tree_code(extended)
                next_layer.setdefault(code, canonical_adjacency(code))
        layer = next_layer
        if size <= RANK and len(layer) != EXPECTED_FREE_COUNTS[size]:
            raise AssertionError(
                f"free-tree leaf generator failed at order {size}: "
                f"got {len(layer)}, expected {EXPECTED_FREE_COUNTS[size]}"
            )
    free_codes = set(layer)
    if free_codes != rooted_free_codes:
        raise AssertionError("leaf and rooted free-tree generators disagree")
    if order == RANK and len(free_codes) != EXPECTED_FREE_COUNT:
        raise AssertionError(
            f"free-tree generator produced {len(free_codes)}, expected {EXPECTED_FREE_COUNT}"
        )
    trees = [(code, canonical_adjacency(code)) for code in sorted(free_codes)]
    for code, adjacency in trees:
        if free_tree_code(adjacency) != code:
            raise AssertionError("free-tree canonical round trip failed")
        edges = sum(sum(row) for row in adjacency) // 2
        if len(adjacency) != order or edges != order - 1:
            raise AssertionError("decoded object is not a tree")
    return trees


def graph6(adjacency: Sequence[Sequence[int]]) -> str:
    order = len(adjacency)
    if not 0 <= order <= 62:
        raise ValueError("only short graph6 headers are supported")
    bits = [adjacency[i][j] for j in range(1, order) for i in range(j)]
    while len(bits) % 6:
        bits.append(0)
    chars = [chr(order + 63)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | int(bit)
        chars.append(chr(value + 63))
    return "".join(chars)


def determinant_bareiss(matrix: Sequence[Sequence[int]]) -> int:
    order = len(matrix)
    work = [list(map(int, row)) for row in matrix]
    sign = 1
    previous = 1
    for column in range(order - 1):
        pivot_row = next((row for row in range(column, order) if work[row][column]), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        for i in range(column + 1, order):
            for j in range(column + 1, order):
                numerator = work[i][j] * pivot - work[i][column] * work[column][j]
                if numerator % previous:
                    raise AssertionError("Bareiss division was not exact")
                work[i][j] = numerator // previous
        for i in range(column + 1, order):
            work[i][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def colour_partition(adjacency: Sequence[int]) -> list[list[int]]:
    classes: list[list[int]] = []
    uncoloured = (1 << len(adjacency)) - 1
    while uncoloured:
        available = uncoloured
        colour: list[int] = []
        while available:
            bit = available & -available
            vertex = bit.bit_length() - 1
            colour.append(vertex)
            uncoloured ^= bit
            available ^= bit
            available &= ~adjacency[vertex]
        classes.append(colour)
    return classes


def colour_sort(adjacency: Sequence[int], candidates: int) -> tuple[list[int], list[int]]:
    order: list[int] = []
    bounds: list[int] = []
    uncoloured = candidates
    colour = 0
    while uncoloured:
        colour += 1
        available = uncoloured
        while available:
            bit = available & -available
            vertex = bit.bit_length() - 1
            order.append(vertex)
            bounds.append(colour)
            uncoloured ^= bit
            available ^= bit
            available &= ~adjacency[vertex]
    return order, bounds


class TargetDecisionTranscript:
    def __init__(self, adjacency: Sequence[int], target: int):
        self.adjacency = list(adjacency)
        self.target = target
        self.nodes = 0
        self.prunes = 0
        self.digest = hashlib.sha256()
        self.width = (len(adjacency) + 7) // 8
        self.witness: list[int] | None = None

    def expand(self, clique: list[int], candidates: int) -> bool:
        self.nodes += 1
        self.digest.update(len(clique).to_bytes(2, "big"))
        self.digest.update(candidates.to_bytes(self.width, "big"))
        if len(clique) >= self.target:
            self.digest.update(b"W")
            self.witness = list(clique)
            return True
        order, bounds = colour_sort(self.adjacency, candidates)
        self.digest.update(len(order).to_bytes(2, "big"))
        for position in range(len(order) - 1, -1, -1):
            if len(clique) + bounds[position] < self.target:
                self.prunes += 1
                self.digest.update(b"P")
                self.digest.update(bounds[position].to_bytes(2, "big"))
                return False
            vertex = order[position]
            bit = 1 << vertex
            if not candidates & bit:
                continue
            self.digest.update(b"B")
            self.digest.update(vertex.to_bytes(2, "big"))
            if self.expand(clique + [vertex], candidates & self.adjacency[vertex]):
                return True
            candidates ^= bit
        self.digest.update(b"R")
        return False

    def solve(self) -> list[int] | None:
        self.expand([], (1 << len(self.adjacency)) - 1)
        return self.witness


def edge_list(adjacency: Sequence[Sequence[int]]) -> list[list[int]]:
    return [
        [i, j]
        for i in range(len(adjacency))
        for j in range(i + 1, len(adjacency))
        if adjacency[i][j]
    ]


def explicit_candidate(
    core: Sequence[Sequence[int]],
    core_masks: Sequence[int],
    masks: Sequence[int],
    witness: Sequence[int],
) -> dict[str, object]:
    scaled = scaled_inverse(core)
    if scaled is None:
        raise AssertionError("candidate core became singular")
    scale, inverse = scaled
    selected = list(core_masks) + [masks[index] for index in witness[:TARGET_NONCORE]]

    def pair(left: int, right: int) -> int:
        return sum(
            inverse[i][j]
            for i in range(RANK)
            for j in range(RANK)
            if (left >> i) & 1 and (right >> j) & 1
        )

    adjacency: list[list[int]] = []
    for left in selected:
        row: list[int] = []
        for right in selected:
            value = pair(left, right)
            if value not in (0, scale):
                raise AssertionError("selected columns do not define a simple graph")
            row.append(value // scale)
        adjacency.append(row)
    if any(adjacency[i][i] for i in range(len(adjacency))):
        raise AssertionError("candidate has a loop")
    if any(sum(row) == 0 for row in adjacency):
        raise AssertionError("candidate has an isolate")
    open_neighbourhoods = [tuple(row) for row in adjacency]
    if len(set(open_neighbourhoods)) != len(adjacency):
        raise AssertionError("candidate has open twins")
    return {
        "graph_order": len(adjacency),
        "core_matrix": core,
        "core_determinant": determinant_bareiss(core),
        "scaled_inverse_denominator": scale,
        "scaled_inverse": inverse,
        "column_masks": selected,
        "adjacency_matrix": adjacency,
        "rank_upper_certificate": "A = X^T (scaled_inverse/denominator) X exactly",
        "rank_lower_certificate": "the leading 10 by 10 principal core has nonzero determinant",
        "reduced_checks": {
            "isolated_vertices": [],
            "duplicate_open_neighbourhoods": [],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("work/builder/tree_core_exact_search.json"),
    )
    parser.add_argument(
        "--candidate-output",
        type=Path,
        default=Path("work/builder/tree_core_counterexample_candidate.json"),
    )
    parser.add_argument("--seed", type=int, default=20260827)
    args = parser.parse_args()

    trees = generate_free_trees()
    records: list[dict[str, object]] = []
    candidate: dict[str, object] | None = None
    started = time.monotonic()
    nonsingular_count = 0
    for index, (code, core) in enumerate(trees):
        determinant = determinant_bareiss(core)
        record: dict[str, object] = {
            "tree_index": index,
            "ahu_canonical_code": code,
            "canonical_graph6": graph6(core),
            "canonical_edge_list": edge_list(core),
            "determinant": determinant,
            "singular": determinant == 0,
        }
        print(
            f"BEGIN tree {index + 1}/{len(trees)} det={determinant} "
            f"g6={record['canonical_graph6']}",
            flush=True,
        )
        if determinant:
            nonsingular_count += 1
            built = build_compatibility(core)
            if built is None:
                raise AssertionError("determinant and inverse tests disagree")
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
                candidate["tree_metadata"] = {
                    "tree_index": index,
                    "ahu_canonical_code": code,
                    "canonical_graph6": record["canonical_graph6"],
                    "canonical_edge_list": record["canonical_edge_list"],
                }
                args.candidate_output.parent.mkdir(parents=True, exist_ok=True)
                args.candidate_output.write_text(
                    json.dumps(candidate, indent=2) + "\n", encoding="utf-8"
                )
                records.append(record)
                print(f"FROZEN CANDIDATE {args.candidate_output}", flush=True)
                break
        records.append(record)
        print(
            f"END tree {index + 1} singular={record['singular']} "
            f"mode={record.get('proof_mode')} found={record.get('target_clique_found')}",
            flush=True,
        )

    payload = {
        "schema_version": 1,
        "theorem_scope": (
            "reduced rank-10 graphs containing a nonsingular induced principal "
            "core isomorphic to a ten-vertex tree"
        ),
        "rooted_tree_count_self_check": EXPECTED_ROOTED_COUNTS[1:],
        "free_tree_layer_count_self_check": EXPECTED_FREE_COUNTS[1:],
        "free_tree_count_self_check": len(trees),
        "all_106_trees_processed": len(records) == EXPECTED_FREE_COUNT,
        "nonsingular_tree_cores_processed": nonsingular_count,
        "target_noncore_clique_size": TARGET_NONCORE,
        "counterexample_candidate_found": candidate is not None,
        "candidate_path": str(args.candidate_output) if candidate is not None else None,
        "elapsed_seconds": time.monotonic() - started,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            indent=2,
        ),
        flush=True,
    )
    print(f"output={args.output}", flush=True)


if __name__ == "__main__":
    main()
