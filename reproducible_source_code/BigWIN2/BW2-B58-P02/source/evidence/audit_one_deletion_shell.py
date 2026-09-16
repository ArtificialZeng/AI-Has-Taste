#!/usr/bin/env python3
"""Exact audit of one-deletion shells for the frozen 54/952 codebook.

This is a Python translation of the primary artifact's independent
``verify_one_deletion_range.mjs`` logic, specialized to a single odd total.
Unlike the published verifier it does not consume a precomputed certificate:
it searches for a killing local relation and falls back to exact CSP search.
"""

from __future__ import annotations

import argparse
import functools
import json
import operator
import time
from collections import defaultdict
from pathlib import Path


M = 54
K = 952
FULL = (1 << K) - 1


def square_free(word: tuple[int, ...]) -> bool:
    for start in range(len(word)):
        for period in range(1, (len(word) - start) // 2 + 1):
            if word[start : start + period] == word[start + period : start + 2 * period]:
                return False
    return True


@functools.lru_cache(maxsize=None)
def outer_words(length: int) -> tuple[tuple[int, ...], ...]:
    answer: list[tuple[int, ...]] = []

    def visit(prefix: tuple[int, ...]) -> None:
        if len(prefix) == length:
            answer.append(prefix)
            return
        for symbol in range(3):
            candidate = prefix + (symbol,)
            if square_free(candidate):
                visit(candidate)

    visit((0,))
    return tuple(answer)


def pattern(total: int, offset: int, deletion: int, orientation: str):
    longer = (total + 1) // 2
    shorter = longer - 1
    groups: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)

    def add(first: int, second: int) -> None:
        u, left = divmod(first, M)
        v, right = divmod(second, M)
        groups[(u, v)].append((left, right))

    if orientation == "left-longer":
        for j in range(shorter):
            add(offset + (j if j < deletion else j + 1), offset + longer + j)
    elif orientation == "right-longer":
        for i in range(shorter):
            add(offset + i, offset + shorter + (i if i < deletion else i + 1))
    else:
        raise ValueError(orientation)

    block_count = (offset + total - 1) // M + 1
    edges = tuple((u, v, tuple(groups[(u, v)])) for u, v in sorted(groups))
    return block_count, edges


class Relations:
    def __init__(self, words: tuple[tuple[int, ...], ...]):
        self.words = words
        self.incompatibility_cache: dict[tuple[int, tuple[tuple[int, int], ...]], bool] = {}
        self.group_cache: dict[
            tuple[int, tuple[tuple[int, int], ...]], tuple[tuple[int, int], ...]
        ] = {}

    @staticmethod
    def _getter(positions: tuple[int, ...]):
        if len(positions) == 1:
            get_one = operator.itemgetter(positions[0])
            return lambda row: (get_one(row),)
        return operator.itemgetter(*positions)

    def incompatible(self, delta: int, pairs: tuple[tuple[int, int], ...]) -> bool:
        key = (delta, pairs)
        cached = self.incompatibility_cache.get(key)
        if cached is not None:
            return cached
        get_left = self._getter(tuple(left for left, _ in pairs))
        get_right = self._getter(tuple(right for _, right in pairs))
        left = {get_left(word) for word in self.words}
        answer = True
        for word in self.words:
            signature = tuple((symbol + delta) % 3 for symbol in get_right(word))
            if signature in left:
                answer = False
                break
        self.incompatibility_cache[key] = answer
        return answer

    def relation_groups(
        self, delta: int, pairs: tuple[tuple[int, int], ...]
    ) -> tuple[tuple[int, int], ...]:
        key = (delta, pairs)
        cached = self.group_cache.get(key)
        if cached is not None:
            return cached
        get_left = self._getter(tuple(left for left, _ in pairs))
        get_right = self._getter(tuple(right for _, right in pairs))
        left: dict[tuple[int, ...], int] = defaultdict(int)
        right: dict[tuple[int, ...], int] = defaultdict(int)
        for index, word in enumerate(self.words):
            bit = 1 << index
            left[get_left(word)] |= bit
            shifted = tuple((symbol + delta) % 3 for symbol in get_right(word))
            right[shifted] |= bit
        answer = tuple((left[sig], right[sig]) for sig in left.keys() & right.keys())
        self.group_cache[key] = answer
        return answer


def revise(domains: list[int], relation, reverse: bool) -> bool:
    u, v, groups = relation
    if reverse:
        u, v = v, u
    old = domains[u]
    new = 0
    for left_mask, right_mask in groups:
        if reverse:
            left_mask, right_mask = right_mask, left_mask
        if old & left_mask and domains[v] & right_mask:
            new |= old & left_mask
    if new == old:
        return False
    domains[u] = new
    return True


def propagate(domains: list[int], relations, incident) -> bool:
    queue = [(index, reverse) for index in range(len(relations)) for reverse in (False, True)]
    head = 0
    while head < len(queue):
        index, reverse = queue[head]
        head += 1
        relation = relations[index]
        if not revise(domains, relation, reverse):
            continue
        u = relation[1] if reverse else relation[0]
        if domains[u] == 0:
            return False
        for other in incident[u]:
            if other != index:
                queue.append((other, relations[other][0] == u))
    return True


def solve(domains: list[int], relations, incident):
    domains = domains.copy()
    if not propagate(domains, relations, incident):
        return None
    variable = next((i for i, mask in enumerate(domains) if mask & (mask - 1)), -1)
    if variable < 0:
        return domains
    choices = domains[variable]
    while choices:
        bit = choices & -choices
        choices -= bit
        branch = domains.copy()
        branch[variable] = bit
        answer = solve(branch, relations, incident)
        if answer is not None:
            return answer
    return None


def audit(source: Path, total: int) -> dict[str, object]:
    if total % 2 != 1:
        raise ValueError("one-deletion total must be odd")
    lines = source.read_text(encoding="ascii").splitlines()
    if len(lines) != K or len(set(lines)) != K:
        raise ValueError("expected 952 distinct codewords")
    if lines != sorted(lines) or any(len(word) != M or set(word) - set("012") for word in lines):
        raise ValueError("malformed canonical codebook")
    if {word[::-1] for word in lines} != set(lines):
        raise ValueError("codebook is not reversal closed")
    words = tuple(tuple(ord(symbol) - 48 for symbol in word) for word in lines)
    relation_factory = Relations(words)
    longer = (total + 1) // 2
    cases = 0
    local_kills = 0
    residual_infeasible = 0
    selected_histogram: dict[int, int] = defaultdict(int)
    started = time.perf_counter()

    for orientation in ("left-longer", "right-longer"):
        for offset in range(M):
            block_count, _ = pattern(total, offset, 0, orientation)
            outers = outer_words(block_count)
            for deletion in range(longer):
                block_count, edges = pattern(total, offset, deletion, orientation)
                for outer in outers:
                    cases += 1
                    for edge_index, (u, v, pairs) in enumerate(edges):
                        delta = (outer[v] - outer[u]) % 3
                        if relation_factory.incompatible(delta, pairs):
                            local_kills += 1
                            selected_histogram[edge_index] += 1
                            break
                    else:
                        relations = []
                        incident = [[] for _ in range(block_count)]
                        for u, v, pairs in edges:
                            delta = (outer[v] - outer[u]) % 3
                            relation = (u, v, relation_factory.relation_groups(delta, pairs))
                            index = len(relations)
                            relations.append(relation)
                            incident[u].append(index)
                            incident[v].append(index)
                        witness = solve([FULL] * block_count, relations, incident)
                        if witness is not None:
                            indices = tuple(mask.bit_length() - 1 for mask in witness)
                            return {
                                "status": "ONE_DELETION_SHELL_NONEMPTY",
                                "total": total,
                                "orientation": orientation,
                                "offset": offset,
                                "deletion": deletion,
                                "outer": outer,
                                "codeword_indices_zero_based": indices,
                                "cases_before_witness": cases,
                            }
                        residual_infeasible += 1

    return {
        "status": "ONE_DELETION_SHELL_EMPTY",
        "total": total,
        "lengths": [longer, longer - 1],
        "cases": cases,
        "local_kills": local_kills,
        "residual_infeasible": residual_infeasible,
        "selected_edge_index_histogram": dict(sorted(selected_histogram.items())),
        "outer_context_counts": {str(length): len(outer_words(length)) for length in (5, 6)},
        "incompatibility_cache_entries": len(relation_factory.incompatibility_cache),
        "relation_cache_entries": len(relation_factory.group_cache),
        "wall_seconds": round(time.perf_counter() - started, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("total", type=int)
    args = parser.parse_args()
    print(json.dumps(audit(args.source, args.total), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
