#!/usr/bin/env python3
"""No-import verifier for the exhaustive ten-vertex tree-core search."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Sequence


RANK = 10
TARGET = 53
EXPECTED_FREE_COUNTS = [0, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106]


RootedTree = tuple["RootedTree", ...]


def parse_rooted(code: str, start: int = 0) -> tuple[RootedTree, int]:
    if start >= len(code) or code[start] != "(":
        raise ValueError("bad rooted code")
    children: list[RootedTree] = []
    position = start + 1
    while position < len(code) and code[position] != ")":
        child, position = parse_rooted(code, position)
        children.append(child)
    if position >= len(code):
        raise ValueError("unterminated rooted code")
    return tuple(children), position + 1


def rooted_to_adjacency(tree: RootedTree) -> tuple[list[list[int]], int]:
    lists: list[list[int]] = []

    def add(subtree: RootedTree) -> int:
        root = len(lists)
        lists.append([])
        for child in subtree:
            child_root = add(child)
            lists[root].append(child_root)
            lists[child_root].append(root)
        return root

    root = add(tree)
    adjacency = [[0] * len(lists) for _ in lists]
    for i, neighbours in enumerate(lists):
        for j in neighbours:
            adjacency[i][j] = 1
    return adjacency, root


def centres(adjacency: Sequence[Sequence[int]]) -> list[int]:
    size = len(adjacency)
    degree = [sum(row) for row in adjacency]
    alive = [True] * size
    leaves = [i for i, value in enumerate(degree) if value <= 1]
    remaining = size
    while remaining > 2:
        layer = leaves
        leaves = []
        remaining -= len(layer)
        for leaf in layer:
            alive[leaf] = False
            for neighbour, value in enumerate(adjacency[leaf]):
                if value and alive[neighbour]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        leaves.append(neighbour)
    return [i for i, value in enumerate(alive) if value]


def rooted_at(adjacency: Sequence[Sequence[int]], root: int, parent: int) -> str:
    children = [
        rooted_at(adjacency, child, root)
        for child, value in enumerate(adjacency[root])
        if value and child != parent
    ]
    return "(" + "".join(sorted(children)) + ")"


def canonical_code(adjacency: Sequence[Sequence[int]]) -> str:
    tree_centres = centres(adjacency)
    if len(tree_centres) == 1:
        return "U" + rooted_at(adjacency, tree_centres[0], -1)
    left = rooted_at(adjacency, tree_centres[0], tree_centres[1])
    right = rooted_at(adjacency, tree_centres[1], tree_centres[0])
    left, right = sorted((left, right))
    return "B" + left + "|" + right


def decode_canonical(code: str) -> list[list[int]]:
    if code.startswith("U"):
        tree, end = parse_rooted(code, 1)
        if end != len(code):
            raise ValueError("bad unicentred code")
        return rooted_to_adjacency(tree)[0]
    if not code.startswith("B") or "|" not in code:
        raise ValueError("bad bicentred code")
    left_code, right_code = code[1:].split("|", 1)
    left, left_end = parse_rooted(left_code)
    right, right_end = parse_rooted(right_code)
    if left_end != len(left_code) or right_end != len(right_code):
        raise ValueError("bad bicentred branch code")
    a, left_root = rooted_to_adjacency(left)
    b, right_root = rooted_to_adjacency(right)
    offset = len(a)
    adjacency = [[0] * (len(a) + len(b)) for _ in range(len(a) + len(b))]
    for i in range(len(a)):
        for j in range(len(a)):
            adjacency[i][j] = a[i][j]
    for i in range(len(b)):
        for j in range(len(b)):
            adjacency[offset + i][offset + j] = b[i][j]
    adjacency[left_root][offset + right_root] = 1
    adjacency[offset + right_root][left_root] = 1
    return adjacency


def generate_free_trees() -> list[tuple[str, list[list[int]]]]:
    layer: dict[str, list[list[int]]] = {"U()": [[0]]}
    for size in range(2, RANK + 1):
        next_layer: dict[str, list[list[int]]] = {}
        for adjacency in layer.values():
            for parent in range(size - 1):
                extended = [row + [0] for row in adjacency]
                extended.append([0] * size)
                extended[parent][size - 1] = 1
                extended[size - 1][parent] = 1
                code = canonical_code(extended)
                next_layer.setdefault(code, decode_canonical(code))
        layer = next_layer
        if len(layer) != EXPECTED_FREE_COUNTS[size]:
            raise ValueError(f"free-tree count mismatch at order {size}")
    return sorted(layer.items())


def graph6(adjacency: Sequence[Sequence[int]]) -> str:
    bits = [adjacency[i][j] for j in range(1, len(adjacency)) for i in range(j)]
    while len(bits) % 6:
        bits.append(0)
    output = [chr(len(adjacency) + 63)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = 2 * value + int(bit)
        output.append(chr(value + 63))
    return "".join(output)


def edge_list(adjacency: Sequence[Sequence[int]]) -> list[list[int]]:
    return [
        [i, j]
        for i in range(len(adjacency))
        for j in range(i + 1, len(adjacency))
        if adjacency[i][j]
    ]


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    work = [list(map(int, row)) for row in matrix]
    sign = 1
    previous = 1
    for column in range(len(work) - 1):
        pivot_row = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        for i in range(column + 1, len(work)):
            for j in range(column + 1, len(work)):
                numerator = work[i][j] * pivot - work[i][column] * work[column][j]
                if numerator % previous:
                    raise ValueError("non-exact Bareiss division")
                work[i][j] = numerator // previous
        for i in range(column + 1, len(work)):
            work[i][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def inverse(matrix: Sequence[Sequence[int]]) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [
        [Fraction(value) for value in row]
        + [Fraction(int(i == j)) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]), None
        )
        if pivot is None:
            raise ValueError("singular matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        value = augmented[column][column]
        augmented[column] = [entry / value for entry in augmented[column]]
        for row in range(size):
            if row != column and augmented[row][column]:
                value = augmented[row][column]
                augmented[row] = [
                    left - value * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [row[size:] for row in augmented]


def compatibility(core: Sequence[Sequence[int]]) -> tuple[list[int], list[int], int]:
    rational_inverse = inverse(core)
    scale = 1
    for row in rational_inverse:
        for value in row:
            scale = math.lcm(scale, value.denominator)
    scaled = [[int(value * scale) for value in row] for row in rational_inverse]

    def pair(left: int, right: int) -> int:
        return sum(
            scaled[i][j]
            for i in range(RANK)
            for j in range(RANK)
            if (left >> i) & 1 and (right >> j) & 1
        )

    core_masks = {
        sum(int(core[i][j]) << i for i in range(RANK)) for j in range(RANK)
    }
    isotropic = [mask for mask in range(1, 1 << RANK) if pair(mask, mask) == 0]
    masks = [mask for mask in isotropic if mask not in core_masks]
    adjacency = [0] * len(masks)
    edges = 0
    for i, left in enumerate(masks):
        for j in range(i):
            if pair(left, masks[j]) in (0, scale):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
                edges += 1
    return masks, adjacency, edges


def colour_partition(adjacency: Sequence[int]) -> list[list[int]]:
    colours: list[list[int]] = []
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
        colours.append(colour)
    return colours


def colour_sort(adjacency: Sequence[int], candidates: int) -> tuple[list[int], list[int]]:
    order: list[int] = []
    bounds: list[int] = []
    uncoloured = candidates
    colour_number = 0
    while uncoloured:
        colour_number += 1
        available = uncoloured
        while available:
            bit = available & -available
            vertex = bit.bit_length() - 1
            order.append(vertex)
            bounds.append(colour_number)
            uncoloured ^= bit
            available ^= bit
            available &= ~adjacency[vertex]
    return order, bounds


def replay(adjacency: Sequence[int]) -> tuple[bool, int, int, str]:
    nodes = 0
    prunes = 0
    digest = hashlib.sha256()
    width = (len(adjacency) + 7) // 8

    def expand(depth: int, candidates: int) -> bool:
        nonlocal nodes, prunes
        nodes += 1
        digest.update(depth.to_bytes(2, "big"))
        digest.update(candidates.to_bytes(width, "big"))
        if depth >= TARGET:
            digest.update(b"W")
            return True
        order, bounds = colour_sort(adjacency, candidates)
        digest.update(len(order).to_bytes(2, "big"))
        for position in range(len(order) - 1, -1, -1):
            if depth + bounds[position] < TARGET:
                prunes += 1
                digest.update(b"P")
                digest.update(bounds[position].to_bytes(2, "big"))
                return False
            vertex = order[position]
            bit = 1 << vertex
            if not candidates & bit:
                continue
            digest.update(b"B")
            digest.update(vertex.to_bytes(2, "big"))
            if expand(depth + 1, candidates & adjacency[vertex]):
                return True
            candidates ^= bit
        digest.update(b"R")
        return False

    found = expand(0, (1 << len(adjacency)) - 1)
    return found, nodes, prunes, digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--expected-sha256",
        help="fail closed unless the input bytes have this exact SHA-256",
    )
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    source_sha256 = hashlib.sha256(raw).hexdigest()
    if args.expected_sha256 and source_sha256 != args.expected_sha256:
        raise ValueError(
            f"source SHA-256 mismatch: got {source_sha256}, "
            f"expected {args.expected_sha256}"
        )
    data = json.loads(raw)
    if data.get("counterexample_candidate_found"):
        raise ValueError("this upper-bound verifier does not accept a candidate run")
    trees = generate_free_trees()
    records = data["records"]
    if len(records) != len(trees) or not data.get("all_106_trees_processed"):
        raise ValueError("incomplete tree enumeration")
    nonsingular = 0
    root_colour_proofs = 0
    branch_proofs = 0
    replayed_nodes = 0
    for index, ((code, core), record) in enumerate(zip(trees, records)):
        if record["tree_index"] != index or record["ahu_canonical_code"] != code:
            raise ValueError("canonical tree ordering mismatch")
        if record["canonical_graph6"] != graph6(core):
            raise ValueError("graph6 mismatch")
        if record["canonical_edge_list"] != edge_list(core):
            raise ValueError("edge-list mismatch")
        det = determinant(core)
        if record["determinant"] != det or record["singular"] != (det == 0):
            raise ValueError("determinant mismatch")
        if not det:
            continue
        nonsingular += 1
        masks, adjacency, edges = compatibility(core)
        if record["noncore_isotropic_count"] != len(masks):
            raise ValueError("isotropic profile mismatch")
        if record["compatibility_edge_count"] != edges:
            raise ValueError("compatibility edge count mismatch")
        colours = colour_partition(adjacency)
        if record["root_greedy_colour_upper_bound"] != len(colours):
            raise ValueError("root colouring count mismatch")
        if record.get("target_clique_found"):
            raise ValueError("unexpected target-clique flag")
        mode = record["proof_mode"]
        if mode == "root_proper_colouring":
            root_colour_proofs += 1
            serialized = record["root_colour_classes_by_column_mask"]
            if len(serialized) >= TARGET:
                raise ValueError("serialized colouring is too large to prove the bound")
            mask_to_index = {mask: i for i, mask in enumerate(masks)}
            flattened: list[int] = []
            for colour in serialized:
                vertices = [mask_to_index[int(mask)] for mask in colour]
                flattened.extend(vertices)
                for i, left in enumerate(vertices):
                    for right in vertices[:i]:
                        if (adjacency[left] >> right) & 1:
                            raise ValueError("serialized colour class is not independent")
            if sorted(flattened) != list(range(len(masks))):
                raise ValueError("serialized colour classes do not partition candidates")
        elif mode == "complete_exact_target_search":
            branch_proofs += 1
            found, nodes, prunes, transcript = replay(adjacency)
            if found:
                raise ValueError("replay found a forbidden 53-clique")
            expected = record["branch_and_bound"]
            if (
                nodes != expected["nodes"]
                or prunes != expected["prunes"]
                or transcript != expected["transcript_sha256"]
            ):
                raise ValueError("branch transcript mismatch")
            replayed_nodes += nodes
        else:
            raise ValueError(f"unsupported proof mode {mode}")
    if nonsingular != data["nonsingular_tree_cores_processed"]:
        raise ValueError("nonsingular count mismatch")
    result = {
        "status": "PASS",
        "certificate_sha256": source_sha256,
        "free_trees_verified": len(trees),
        "nonsingular_tree_cores_verified": nonsingular,
        "root_colouring_proofs_verified": root_colour_proofs,
        "complete_branch_proofs_replayed": branch_proofs,
        "total_branch_nodes_replayed": replayed_nodes,
        "counterexample_found": False,
        "conclusion": (
            "every reduced rank-10 graph containing a nonsingular induced "
            "ten-vertex tree core has order at most 62"
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
