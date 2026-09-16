#!/usr/bin/env python3
"""Exact audit of a two-deletion shell for the frozen 54/952 codebook.

This is a Python replay of the primary artifact's
``verify_two_deletion_shell.mjs``.  It accepts any positive even total, checks
all three length modes, all 54 offsets, and every deletion pattern.  Relations
are represented by maximal diagonal runs rather than rebuilt one coordinate at
a time.  As in the primary program, a pattern is first killed by a local
relation for all alphabet shifts, then by the required normalized square-free
outer contexts.  Unlike that program, any context surviving the local tests is
sent to an exact finite-domain CSP before it is reported as a witness.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import operator
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Iterator


M = 54
K = 952
FULL = (1 << K) - 1
MODES = ("left-longer", "right-longer", "equal")
SHIFT_TABLES = tuple(
    bytes.maketrans(b"012", bytes((48 + delta, 48 + (1 + delta) % 3, 48 + (2 + delta) % 3)))
    for delta in range(3)
)

Run = tuple[int, int, int]
Edge = tuple[int, int, tuple[Run, ...]]


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

    # Alphabet-shift normalization: every context orbit has one word starting 0.
    visit((0,))
    return tuple(answer)


def affine_segments(half: int, mode: str, deletions: tuple[int, int]):
    """Yield (k_start, k_stop, first_bias, second_bias) matching segments."""
    if mode in ("left-longer", "right-longer"):
        first, second = deletions
        breaks = (0, first, second - 1, half - 1)
        for index, (start, stop) in enumerate(zip(breaks, breaks[1:])):
            if start >= stop:
                continue
            survivor_bias = index
            if mode == "left-longer":
                yield start, stop, survivor_bias, half + 1
            else:
                yield start, stop, 0, half - 1 + survivor_bias
        return

    left, right = deletions
    breaks = sorted({0, left, right, half - 1})
    for start, stop in zip(breaks, breaks[1:]):
        if start < stop:
            yield start, stop, int(start >= left), half + int(start >= right)


def grouped_edges(offset: int, half: int, mode: str, deletions: tuple[int, int]):
    """Return block count and sorted relation edges, encoded as diagonal runs."""
    groups: dict[tuple[int, int], list[Run]] = defaultdict(list)
    for start, stop, first_bias, second_bias in affine_segments(half, mode, deletions):
        k = start
        while k < stop:
            first = offset + k + first_bias
            second = offset + k + second_bias
            take = min(stop - k, M - first % M, M - second % M)
            u, left = divmod(first, M)
            v, right = divmod(second, M)
            runs = groups[(u, v)]
            if runs and runs[-1][0] + runs[-1][2] == left and runs[-1][1] + runs[-1][2] == right:
                old_left, old_right, old_take = runs[-1]
                runs[-1] = (old_left, old_right, old_take + take)
            else:
                runs.append((left, right, take))
            k += take
    block_count = (offset + 2 * half - 1) // M + 1
    edges = tuple((u, v, tuple(groups[(u, v)])) for u, v in sorted(groups))
    return block_count, edges


def expand_positions(runs: tuple[Run, ...]):
    left: list[int] = []
    right: list[int] = []
    for first, second, length in runs:
        left.extend(range(first, first + length))
        right.extend(range(second, second + length))
    return tuple(left), tuple(right)


class Relations:
    def __init__(self, words: tuple[bytes, ...]):
        self.words = words
        # Bit delta is one precisely when that alphabet shift is compatible.
        self.compatibility_cache: dict[tuple[Run, ...], int] = {}
        self.group_cache: dict[tuple[int, tuple[Run, ...]], tuple[tuple[int, int], ...]] = {}

    @staticmethod
    def _getter(positions: tuple[int, ...]):
        if len(positions) == 1:
            get_one = operator.itemgetter(positions[0])
            return lambda row: bytes((get_one(row),))
        get_many = operator.itemgetter(*positions)
        return lambda row: bytes(get_many(row))

    def compatibility_mask(self, runs: tuple[Run, ...]) -> int:
        cached = self.compatibility_cache.get(runs)
        if cached is not None:
            return cached
        left_positions, right_positions = expand_positions(runs)
        get_left = self._getter(left_positions)
        get_right = self._getter(right_positions)
        left = {get_left(word) for word in self.words}
        unresolved = 0b111
        compatible = 0
        for word in self.words:
            signature = get_right(word)
            for delta in range(3):
                bit = 1 << delta
                if unresolved & bit and signature.translate(SHIFT_TABLES[delta]) in left:
                    compatible |= bit
                    unresolved &= ~bit
            if not unresolved:
                break
        self.compatibility_cache[runs] = compatible
        return compatible

    def relation_groups(self, delta: int, runs: tuple[Run, ...]) -> tuple[tuple[int, int], ...]:
        key = (delta, runs)
        cached = self.group_cache.get(key)
        if cached is not None:
            return cached
        left_positions, right_positions = expand_positions(runs)
        get_left = self._getter(left_positions)
        get_right = self._getter(right_positions)
        left: dict[bytes, int] = defaultdict(int)
        right: dict[bytes, int] = defaultdict(int)
        table = SHIFT_TABLES[delta]
        for index, word in enumerate(self.words):
            bit = 1 << index
            left[get_left(word)] |= bit
            right[get_right(word).translate(table)] |= bit
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


def deletion_patterns(half: int, mode: str) -> Iterator[tuple[int, int]]:
    stop = half if mode == "equal" else half + 1
    if mode == "equal":
        for left in range(stop):
            for right in range(stop):
                yield left, right
    else:
        for first in range(stop):
            for second in range(first + 1, stop):
                yield first, second


def construct_witness(words, total, half, mode, offset, deletions, outer, indices):
    blocks = [bytes((48 + (symbol + (byte - 48)) % 3 for byte in words[index]))
              for symbol, index in zip(outer, indices)]
    ambient = b"".join(blocks)
    if mode == "left-longer":
        left_length, right_length = half + 1, half - 1
        left = ambient[offset : offset + left_length]
        right = ambient[offset + left_length : offset + total]
        survivor = bytes(byte for i, byte in enumerate(left) if i not in deletions)
        matched = survivor == right
    elif mode == "right-longer":
        left_length, right_length = half - 1, half + 1
        left = ambient[offset : offset + left_length]
        right = ambient[offset + left_length : offset + total]
        survivor = bytes(byte for i, byte in enumerate(right) if i not in deletions)
        matched = left == survivor
    else:
        left_length = right_length = half
        left = ambient[offset : offset + half]
        right = ambient[offset + half : offset + total]
        survivor_left = left[: deletions[0]] + left[deletions[0] + 1 :]
        survivor_right = right[: deletions[1]] + right[deletions[1] + 1 :]
        matched = survivor_left == survivor_right
    if not matched:
        raise AssertionError("CSP assignment did not reconstruct its deletion match")
    return {
        "status": "TWO_DELETION_SHELL_NONEMPTY",
        "total": total,
        "mode": mode,
        "lengths": [left_length, right_length],
        "offset": offset,
        "deletions_zero_based": list(deletions),
        "outer": list(outer),
        "codeword_indices_zero_based": list(indices),
        "left": left.decode("ascii"),
        "right": right.decode("ascii"),
        "certified_edit_distance_upper_bound": 2,
        "bad_event_check": f"2*226={2*226}<{total}",
    }


def audit(source: Path, total: int, progress: bool = False) -> dict[str, object]:
    if total <= 0 or total % 2:
        raise ValueError("two-deletion total must be positive and even")
    raw = source.read_bytes()
    lines = raw.splitlines()
    if len(lines) != K or len(set(lines)) != K:
        raise ValueError("expected 952 distinct canonical codewords")
    if lines != sorted(lines) or any(len(word) != M or set(word) - set(b"012") for word in lines):
        raise ValueError("malformed canonical codebook")
    if {word[::-1] for word in lines} != set(lines):
        raise ValueError("codebook is not reversal closed")
    words = tuple(lines)
    half = total // 2
    relation_factory = Relations(words)
    started = time.perf_counter()
    results = []
    totals = {"patterns": 0, "universal": 0, "contexts": 0, "context_killed": 0,
              "csp_residuals": 0, "csp_infeasible": 0}

    for mode in MODES:
        counts = {"mode": mode, "patterns": 0, "universal": 0, "contexts": 0,
                  "context_killed": 0, "csp_residuals": 0, "csp_infeasible": 0}
        mode_started = time.perf_counter()
        for offset in range(M):
            for deletions in deletion_patterns(half, mode):
                counts["patterns"] += 1
                block_count, edges = grouped_edges(offset, half, mode, deletions)
                masks = tuple(relation_factory.compatibility_mask(runs) for _, _, runs in edges)
                if 0 in masks:
                    counts["universal"] += 1
                    continue
                for outer in outer_words(block_count):
                    counts["contexts"] += 1
                    killed = False
                    for (u, v, _), mask in zip(edges, masks):
                        delta = (outer[v] - outer[u]) % 3
                        if not (mask & (1 << delta)):
                            counts["context_killed"] += 1
                            killed = True
                            break
                    if killed:
                        continue
                    counts["csp_residuals"] += 1
                    relations = []
                    incident = [[] for _ in range(block_count)]
                    for u, v, runs in edges:
                        delta = (outer[v] - outer[u]) % 3
                        relation = (u, v, relation_factory.relation_groups(delta, runs))
                        index = len(relations)
                        relations.append(relation)
                        incident[u].append(index)
                        incident[v].append(index)
                    witness = solve([FULL] * block_count, relations, incident)
                    if witness is not None:
                        indices = tuple(mask.bit_length() - 1 for mask in witness)
                        answer = construct_witness(
                            words, total, half, mode, offset, deletions, outer, indices
                        )
                        answer.update({"counts_before_witness": counts,
                                       "relation_cache_entries": len(relation_factory.compatibility_cache),
                                       "wall_seconds": round(time.perf_counter() - started, 6),
                                       "source_sha256": hashlib.sha256(raw).hexdigest()})
                        return answer
                    counts["csp_infeasible"] += 1
            if progress:
                elapsed = time.perf_counter() - mode_started
                print(f"progress mode={mode} offset={offset + 1}/54 patterns={counts['patterns']} "
                      f"elapsed={elapsed:.3f}s", file=sys.stderr, flush=True)
        counts["wall_seconds"] = round(time.perf_counter() - mode_started, 6)
        results.append(counts)
        for key in totals:
            totals[key] += counts[key]

    expected_per_unequal = M * (half + 1) * half // 2
    expected_equal = M * half * half
    expected_patterns = 2 * expected_per_unequal + expected_equal
    if [result["patterns"] for result in results] != [expected_per_unequal] * 2 + [expected_equal]:
        raise AssertionError("mode coverage count mismatch")
    if totals["patterns"] != expected_patterns:
        raise AssertionError("total coverage count mismatch")
    if totals["context_killed"] + totals["csp_residuals"] != totals["contexts"]:
        raise AssertionError("context partition mismatch")
    if totals["csp_residuals"] != totals["csp_infeasible"]:
        raise AssertionError("unresolved CSP residual")
    return {
        "status": "TWO_DELETION_SHELL_EMPTY",
        "total": total,
        "length_modes": [[half + 1, half - 1], [half - 1, half + 1], [half, half]],
        "offsets_per_mode": M,
        "results": results,
        "totals": totals,
        "expected_pattern_formula": f"2*54*C({half + 1},2)+54*{half}^2={expected_patterns}",
        "outer_context_counts": {str(length): len(outer_words(length)) for length in (9, 10)},
        "relation_cache_entries": len(relation_factory.compatibility_cache),
        "csp_relation_cache_entries": len(relation_factory.group_cache),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "wall_seconds": round(time.perf_counter() - started, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("total", type=int)
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()
    print(json.dumps(audit(args.source, args.total, args.progress), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
