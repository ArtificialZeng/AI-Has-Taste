#!/usr/bin/env python3
"""Independent no-import audit of the ten-vertex unicyclic-core search.

This verifier imports no discovery module.  It independently generates the
unicyclic isomorphism domain by decorating cycles with rooted trees, uses a
different bracket code, reconstructs every integer adjugate from cofactors,
and reruns a cyclically relabelled exact target-clique decision.  Source
indices, canonical words, determinants, profile sets, and search transcripts
are not trusted.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from pathlib import Path
from typing import Sequence


RANK = 10
TARGET = 53
EXPECTED_UNICYCLIC = 657
EXPECTED_NONSINGULAR = 136
POPCOUNT16 = tuple(bin(value).count("1") for value in range(1 << 16))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def popcount(value: int) -> int:
    total = 0
    while value:
        total += POPCOUNT16[value & 0xFFFF]
        value >>= 16
    return total


def rooted_words(max_order: int) -> list[set[str]]:
    by_order = [set() for _ in range(max_order + 1)]
    by_order[1].add("[]")
    for order in range(2, max_order + 1):
        pieces = sorted(
            (word, size)
            for size in range(1, order)
            for word in by_order[size]
        )
        output: set[str] = set()

        def fill(first: int, remaining: int, children: list[str]) -> None:
            if remaining == 0:
                output.add("[" + "".join(children) + "]")
                return
            for index in range(first, len(pieces)):
                word, size = pieces[index]
                if size <= remaining:
                    children.append(word)
                    fill(index, remaining - size, children)
                    children.pop()

        fill(0, order - 1, [])
        by_order[order] = output
    return by_order


def parse_rooted(word: str, start: int = 0) -> tuple[tuple, int]:
    if start >= len(word) or word[start] != "[":
        raise ValueError("bad independent rooted word")
    children = []
    position = start + 1
    while position < len(word) and word[position] != "]":
        child, position = parse_rooted(word, position)
        children.append(child)
    if position >= len(word):
        raise ValueError("unterminated independent rooted word")
    return tuple(children), position + 1


def rooted_to_adjacency(tree: tuple) -> tuple[list[list[int]], int]:
    neighbours: list[list[int]] = []

    def add(subtree: tuple) -> int:
        root = len(neighbours)
        neighbours.append([])
        for child in subtree:
            vertex = add(child)
            neighbours[root].append(vertex)
            neighbours[vertex].append(root)
        return root

    root = add(tree)
    adjacency = [[0] * len(neighbours) for _ in neighbours]
    for i, row in enumerate(neighbours):
        for j in row:
            adjacency[i][j] = 1
    return adjacency, root


def dihedral_minimum(words: Sequence[str]) -> tuple[str, ...]:
    original = tuple(words)
    reverse = tuple(reversed(words))
    candidates = []
    for sequence in (original, reverse):
        for offset in range(len(sequence)):
            candidates.append(sequence[offset:] + sequence[:offset])
    return min(candidates)


def independent_cycle_code(words: Sequence[str]) -> str:
    canonical = dihedral_minimum(words)
    return f"C{len(canonical)};" + ";".join(canonical)


def decode_cycle_code(code: str) -> list[list[int]]:
    prefix, raw = code.split(";", 1)
    cycle_length = int(prefix[1:])
    words = raw.split(";")
    if len(words) != cycle_length:
        raise ValueError("independent cycle code has wrong length")
    pieces = []
    for word in words:
        tree, end = parse_rooted(word)
        if end != len(word):
            raise ValueError("trailing independent rooted data")
        pieces.append(rooted_to_adjacency(tree))
    order = sum(len(adjacency) for adjacency, _ in pieces)
    result = [[0] * order for _ in range(order)]
    roots = []
    offset = 0
    for adjacency, root in pieces:
        roots.append(offset + root)
        for i in range(len(adjacency)):
            for j in range(len(adjacency)):
                result[offset + i][offset + j] = adjacency[i][j]
        offset += len(adjacency)
    for index, left in enumerate(roots):
        right = roots[(index + 1) % len(roots)]
        result[left][right] = result[right][left] = 1
    return result


def generate_unicyclic() -> dict[str, list[list[int]]]:
    rooted = rooted_words(RANK - 2)
    catalog = sorted(
        (word, size)
        for size in range(1, RANK - 1)
        for word in rooted[size]
    )
    codes: set[str] = set()
    for cycle_length in range(3, RANK + 1):
        def fill(position: int, remaining: int, words: list[str]) -> None:
            slots = cycle_length - position
            if slots == 0:
                if remaining == 0:
                    codes.add(independent_cycle_code(words))
                return
            if remaining < slots:
                return
            for word, size in catalog:
                if size <= remaining - (slots - 1):
                    words.append(word)
                    fill(position + 1, remaining - size, words)
                    words.pop()

        fill(0, RANK, [])
    if len(codes) != EXPECTED_UNICYCLIC:
        raise AssertionError(f"independent generator found {len(codes)} unicyclic graphs")
    generated = {code: decode_cycle_code(code) for code in codes}
    for adjacency in generated.values():
        if len(adjacency) != RANK or sum(sum(row) for row in adjacency) // 2 != RANK:
            raise AssertionError("independent generator produced wrong order/size")
    return generated


def graph_cycle_vertices(adjacency: Sequence[Sequence[int]]) -> set[int]:
    degree = [sum(map(int, row)) for row in adjacency]
    alive = [True] * len(adjacency)
    stack = [i for i, value in enumerate(degree) if value == 1]
    while stack:
        leaf = stack.pop()
        if not alive[leaf]:
            continue
        alive[leaf] = False
        for vertex, value in enumerate(adjacency[leaf]):
            if value and alive[vertex]:
                degree[vertex] -= 1
                if degree[vertex] == 1:
                    stack.append(vertex)
    cycle = {i for i, flag in enumerate(alive) if flag}
    if len(cycle) < 3 or any(sum(adjacency[i][j] for j in cycle) != 2 for i in cycle):
        raise ValueError("source graph is not connected unicyclic")
    return cycle


def source_to_independent_code(adjacency: Sequence[Sequence[int]]) -> str:
    cycle = graph_cycle_vertices(adjacency)
    start = min(cycle)
    current = min(j for j in range(len(adjacency)) if adjacency[start][j] and j in cycle)
    previous = start
    order = [start]
    while current != start:
        order.append(current)
        choices = [
            j
            for j in range(len(adjacency))
            if adjacency[current][j] and j in cycle and j != previous
        ]
        if len(choices) != 1:
            raise ValueError("source cycle trace failed")
        previous, current = current, choices[0]

    def branch(vertex: int, parent: int) -> str:
        children = [
            branch(j, vertex)
            for j in range(len(adjacency))
            if adjacency[vertex][j] and j != parent and j not in cycle
        ]
        return "[" + "".join(sorted(children)) + "]"

    return independent_cycle_code([branch(vertex, -1) for vertex in order])


def adjacency_from_edges(raw: object) -> list[list[int]]:
    if not isinstance(raw, list):
        raise ValueError("source edges are not a list")
    adjacency = [[0] * RANK for _ in range(RANK)]
    seen = set()
    for edge in raw:
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError("malformed source edge")
        i, j = map(int, edge)
        if not 0 <= i < j < RANK or (i, j) in seen:
            raise ValueError("invalid source edge")
        seen.add((i, j))
        adjacency[i][j] = adjacency[j][i] = 1
    if len(seen) != RANK:
        raise ValueError("source object does not have ten edges")
    reached = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j, value in enumerate(adjacency[i]):
            if value and j not in reached:
                reached.add(j)
                stack.append(j)
    if len(reached) != RANK:
        raise ValueError("source object is disconnected")
    graph_cycle_vertices(adjacency)
    return adjacency


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    work = [list(map(int, row)) for row in matrix]
    sign = 1
    previous = 1
    for column in range(n - 1):
        pivot_row = next((i for i in range(column, n) if work[i][column]), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for i in range(column + 1, n):
            for j in range(column + 1, n):
                numerator = work[i][j] * pivot - work[i][column] * work[column][j]
                if column and numerator % previous:
                    raise ArithmeticError("independent Bareiss division failed")
                work[i][j] = numerator // previous
        for i in range(column + 1, n):
            work[i][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def minor(matrix: Sequence[Sequence[int]], row: int, column: int) -> list[list[int]]:
    return [
        [int(value) for j, value in enumerate(source_row) if j != column]
        for i, source_row in enumerate(matrix)
        if i != row
    ]


def adjugate(matrix: Sequence[Sequence[int]]) -> list[list[int]]:
    n = len(matrix)
    return [
        [((-1) ** (i + j)) * determinant(minor(matrix, j, i)) for j in range(n)]
        for i in range(n)
    ]


def multiply(left: Sequence[Sequence[int]], right: Sequence[Sequence[int]]) -> list[list[int]]:
    return [
        [sum(int(left[i][k]) * int(right[k][j]) for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def form(left: int, matrix: Sequence[Sequence[int]], right: int) -> int:
    return sum(
        int(matrix[i][j])
        for i in range(RANK)
        for j in range(RANK)
        if (left >> i) & 1 and (right >> j) & 1
    )


def profile_graph(
    core: Sequence[Sequence[int]], det: int, adj: Sequence[Sequence[int]]
) -> tuple[list[int], list[int], int]:
    isotropic = [mask for mask in range(1, 1 << RANK) if form(mask, adj, mask) == 0]
    core_masks = [
        sum(int(core[row][column]) << row for row in range(RANK))
        for column in range(RANK)
    ]
    if len(set(core_masks)) != RANK or not set(core_masks).issubset(isotropic):
        raise AssertionError("source core columns failed the independent gate")
    profiles = [mask for mask in isotropic if mask not in set(core_masks)]
    graph = [0] * len(profiles)
    edges = 0
    for i, left in enumerate(profiles):
        for j in range(i):
            if form(left, adj, profiles[j]) in (0, det):
                graph[i] |= 1 << j
                graph[j] |= 1 << i
                edges += 1
    return profiles, graph, edges


def permute_graph(adjacency: Sequence[int], multiplier: int, offset: int) -> list[int]:
    n = len(adjacency)
    if n == 0:
        return []
    while True:
        if __import__("math").gcd(multiplier, n) == 1:
            break
        multiplier += 1
    old_for_new = [(multiplier * i + offset) % n for i in range(n)]
    new_for_old = [0] * n
    for new, old in enumerate(old_for_new):
        new_for_old[old] = new
    result = [0] * n
    for new, old in enumerate(old_for_new):
        bits = adjacency[old]
        while bits:
            bit = bits & -bits
            neighbour = bit.bit_length() - 1
            result[new] |= 1 << new_for_old[neighbour]
            bits ^= bit
    return result


class TargetSearch:
    def __init__(self, adjacency: Sequence[int], target: int):
        self.adjacency = list(adjacency)
        self.target = target
        self.calls = 0
        self.cardinality_prunes = 0
        self.colour_prunes = 0

    def colouring(self, candidates: int) -> tuple[list[int], list[int]]:
        order: list[int] = []
        bounds: list[int] = []
        uncoloured = candidates
        colour = 0
        while uncoloured:
            colour += 1
            independent = uncoloured
            while independent:
                bit = independent & -independent
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(colour)
                uncoloured ^= bit
                independent ^= bit
                independent &= ~self.adjacency[vertex]
        return order, bounds

    def search(self, depth: int, candidates: int) -> bool:
        self.calls += 1
        if depth >= self.target:
            return True
        if popcount(candidates) < self.target - depth:
            self.cardinality_prunes += 1
            return False
        order, bounds = self.colouring(candidates)
        for position in range(len(order) - 1, -1, -1):
            if depth + bounds[position] < self.target:
                self.colour_prunes += 1
                return False
            vertex = order[position]
            bit = 1 << vertex
            if candidates & bit:
                if self.search(depth + 1, candidates & self.adjacency[vertex]):
                    return True
                candidates ^= bit
        return False

    def solve(self) -> bool:
        return self.search(0, (1 << len(self.adjacency)) - 1)


def brute_omega(adjacency: Sequence[int]) -> int:
    best = 0
    for subset in range(1 << len(adjacency)):
        if popcount(subset) <= best:
            continue
        bits = subset
        good = True
        while bits:
            bit = bits & -bits
            vertex = bit.bit_length() - 1
            if (subset ^ bit) & ~adjacency[vertex]:
                good = False
                break
            bits ^= bit
        if good:
            best = popcount(subset)
    return best


def selftest() -> dict[str, object]:
    tested = 0

    def check(graph: list[int]) -> None:
        nonlocal tested
        omega = brute_omega(graph)
        for target in range(1, len(graph) + 2):
            if TargetSearch(graph, target).solve() != (omega >= target):
                raise AssertionError("independent clique search failed self-test")
        tested += 1

    exhaustive = {}
    for n in range(6):
        edges = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            graph = [0] * n
            for index, (i, j) in enumerate(edges):
                if (mask >> index) & 1:
                    graph[i] |= 1 << j
                    graph[j] |= 1 << i
            check(graph)
        exhaustive[str(n)] = 1 << len(edges)
    rng = random.Random(2026082707)
    for n in range(6, 10):
        edges = list(itertools.combinations(range(n), 2))
        for _ in range(100):
            graph = [0] * n
            for i, j in edges:
                if rng.randrange(2):
                    graph[i] |= 1 << j
                    graph[j] |= 1 << i
            check(graph)
    return {"status": "PASS", "graphs_tested": tested, "exhaustive": exhaustive, "random_per_order_6_to_9": 100}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--expected-source-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
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
    if not isinstance(records, list) or len(records) != EXPECTED_UNICYCLIC:
        raise ValueError("source record count mismatch")

    generated = generate_unicyclic()
    source_by_code: dict[str, dict[str, object]] = {}
    for expected_index, record in enumerate(records):
        if int(record.get("unicyclic_index", -1)) != expected_index:
            raise ValueError("source indices are incomplete or reordered")
        adjacency = adjacency_from_edges(record.get("canonical_edge_list"))
        code = source_to_independent_code(adjacency)
        if code in source_by_code:
            raise ValueError("two source records are isomorphic")
        source_by_code[code] = record
    if set(source_by_code) != set(generated):
        raise ValueError("source edge lists differ from independent unicyclic domain")

    engine_test = selftest()
    nonsingular = 0
    total_calls = 0
    verified = []
    det_counts: dict[int, int] = {}
    for position, code in enumerate(sorted(generated), 1):
        core = generated[code]
        record = source_by_code[code]
        det = determinant(core)
        det_counts[det] = det_counts.get(det, 0) + 1
        if det != int(record.get("determinant", 10**9)):
            raise ValueError("independent determinant disagrees with source")
        singular = det == 0
        if singular != bool(record.get("singular")):
            raise ValueError("source singularity mismatch")
        print(f"VERIFY UNICYCLIC {position}/{EXPECTED_UNICYCLIC} source_index={record['unicyclic_index']} singular={singular}", flush=True)
        entry: dict[str, object] = {
            "independent_code": code,
            "source_index": record["unicyclic_index"],
            "determinant": det,
            "cycle_length": len(graph_cycle_vertices(core)),
            "singular": singular,
        }
        if not singular:
            nonsingular += 1
            adj = adjugate(core)
            identity = [[det * int(i == j) for j in range(RANK)] for i in range(RANK)]
            if multiply(core, adj) != identity or multiply(adj, core) != identity:
                raise AssertionError("independent adjugate identity failed")
            profiles, graph, edges = profile_graph(core, det, adj)
            if len(profiles) != int(record.get("noncore_isotropic_count", -1)):
                raise ValueError("source profile count mismatch")
            if edges != int(record.get("compatibility_edge_count", -1)):
                raise ValueError("source compatibility edge count mismatch")
            # A cyclic shift is enough to destroy reliance on the source
            # indices while retaining a stable branch-and-bound complexity.
            # More general affine permutations were tested during audit, but
            # some produce gratuitously exponential colour orderings without
            # strengthening the mathematical check.
            permuted = permute_graph(graph, 1, 1)
            solver = TargetSearch(permuted, TARGET)
            if solver.solve():
                raise ValueError("independent verifier found a forbidden 53-clique")
            if record.get("target_clique_found") is not False:
                raise ValueError("source target conclusion mismatch")
            total_calls += solver.calls
            entry.update(
                {
                    "noncore_isotropic_count": len(profiles),
                    "compatibility_edge_count": edges,
                    "target": TARGET,
                    "target_clique_found": False,
                    "independent_calls": solver.calls,
                    "cardinality_prunes": solver.cardinality_prunes,
                    "colour_prunes": solver.colour_prunes,
                }
            )
        entry["status"] = "PASS"
        verified.append(entry)

    if nonsingular != EXPECTED_NONSINGULAR:
        raise ValueError("independent nonsingular count mismatch")
    if nonsingular != int(source.get("nonsingular_cores_processed", -1)):
        raise ValueError("source nonsingular aggregate mismatch")
    payload = {
        "schema": "reduced-graph-rank10.unicyclic-core-independent-audit.v1",
        "status": "PASS",
        "source": str(args.source),
        "source_sha256": source_hash,
        "arithmetic": "integers only; Bareiss determinants, cofactor adjugates, exact bitset search",
        "independent_generation": "cycle decorations by independently generated bracket-coded rooted trees",
        "source_edge_lists_match_independent_isomorphism_set": True,
        "unicyclic_graphs": len(verified),
        "nonsingular_cores": nonsingular,
        "singular_cores": len(verified) - nonsingular,
        "determinant_distribution": {str(key): det_counts[key] for key in sorted(det_counts)},
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
