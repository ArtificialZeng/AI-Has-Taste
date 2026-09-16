#!/usr/bin/env python3
"""Independent adversarial audit of the proposed finite-tree conjugacy.

This file intentionally does not import ``src.tree_model``.  It reconstructs
the word set, cellular update, missing-edge convention, phase rotation, graph,
and state permutation directly from the candidate statement received by the
breaker role.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterator, Sequence


ALPHABET = (0, 1, 2)
PHASE_COLOR = (1, 0, 2)
RULE_TABLE = (1, 1, 0, 0, 1, 1, 1, 0)


def legal_vertex(word: Sequence[int], depth: int) -> bool:
    size = len(word)
    return (
        0 <= size <= depth
        and all(letter in ALPHABET for letter in word)
        and all(left != right for left, right in zip(word, word[1:]))
        and (size == 0 or word[-1] != 0)
        and (size != depth or word[0] == 0)
    )


def enumerate_vertices(depth: int) -> Iterator[tuple[int, ...]]:
    """Generate from the defining constraints, without following tree edges."""

    if depth < 1:
        raise ValueError("depth must be positive")
    yield ()
    for size in range(1, depth + 1):
        def extend(prefix: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
            if len(prefix) == size:
                if prefix[-1] != 0 and (size != depth or prefix[0] == 0):
                    yield prefix
                return
            for letter in ALPHABET:
                if not prefix or prefix[-1] != letter:
                    yield from extend(prefix + (letter,))

        yield from extend(())


def rotate(letter: int, phase: int) -> int:
    if letter == 3:
        return 3
    return (letter + phase) % 3


def physical_encoding(vertex: Sequence[int], depth: int, phase: int) -> tuple[int, ...]:
    padded = (3,) * (depth - len(vertex)) + tuple(vertex)
    return tuple(rotate(letter, phase) for letter in padded)


def local_symbol_update(left: int, center: int, right: int) -> int:
    memory = center >> 1
    current = center & 1
    index = 4 * (left & 1) + 2 * current + (right & 1)
    following = memory ^ RULE_TABLE[index]
    return 2 * current + following


def update_physical_word(phase: int, word: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        local_symbol_update(
            phase if site == 0 else word[site - 1],
            center,
            phase if site + 1 == len(word) else word[site + 1],
        )
        for site, center in enumerate(word)
    )


def exterior_receivers(phase: int, word: Sequence[int]) -> tuple[int, int]:
    return (
        local_symbol_update(phase, phase, word[0]),
        local_symbol_update(word[-1], phase, phase),
    )


def attempted_front_toggle(vertex: Sequence[int], color: int) -> tuple[int, ...]:
    vertex = tuple(vertex)
    if vertex and vertex[0] == color:
        return vertex[1:]
    return (color,) + vertex


def lazy_edge(vertex: Sequence[int], color: int, depth: int) -> tuple[int, ...]:
    candidate = attempted_front_toggle(vertex, color)
    return candidate if legal_vertex(candidate, depth) else tuple(vertex)


def candidate_step(vertex: Sequence[int], phase: int, depth: int) -> tuple[tuple[int, ...], int]:
    return lazy_edge(vertex, PHASE_COLOR[phase], depth), (phase + 1) % 3


def first_internal_three(word: Sequence[int]) -> int | None:
    seen_non_three = False
    for index, letter in enumerate(word):
        if letter == 3 and seen_non_three:
            return index
        if letter != 3:
            seen_non_three = True
    return None


def normalized_after_unrotation(word: Sequence[int], next_phase: int) -> tuple[int, ...]:
    return tuple(3 if letter == 3 else (letter - next_phase) % 3 for letter in word)


def audit_local_toggle_table() -> list[dict[str, int]]:
    """Attack the claimed normalized local rule on all 3*4^3 inputs."""

    failures = []
    for phase in ALPHABET:
        selected = PHASE_COLOR[phase]
        for left in range(4):
            for center in range(4):
                for right in range(4):
                    physical = tuple(rotate(value, phase) for value in (left, center, right))
                    raw = local_symbol_update(*physical)
                    actual = 3 if raw == 3 else (raw - (phase + 1)) % 3
                    expected = center
                    if left in (selected, 3) and right in (ALPHABET[0], ALPHABET[1], ALPHABET[2]):
                        if right != selected and center == selected:
                            expected = 3
                        elif right != selected and center == 3:
                            expected = selected
                    if actual != expected:
                        failures.append(
                            {
                                "phase": phase,
                                "left": left,
                                "center": center,
                                "right": right,
                                "actual": actual,
                                "expected": expected,
                            }
                        )
    return failures


def audit_depth(depth: int) -> dict[str, object]:
    vertices = list(enumerate_vertices(depth))
    vertex_set = set(vertices)
    failures: list[dict[str, object]] = []
    internal_three_failures = 0
    exterior_failures = 0
    loop_reasons: Counter[str] = Counter()
    edges: set[frozenset[tuple[int, ...]]] = set()
    transition: dict[tuple[tuple[int, ...], int], tuple[tuple[int, ...], int]] = {}

    for vertex in vertices:
        for color in ALPHABET:
            attempted = attempted_front_toggle(vertex, color)
            neighbor = lazy_edge(vertex, color, depth)
            if neighbor == vertex:
                if len(attempted) > depth:
                    loop_reasons["full_depth"] += 1
                elif attempted and attempted[-1] == 0:
                    loop_reasons["terminal_zero"] += 1
                elif len(attempted) == depth and attempted[0] != 0:
                    loop_reasons["full_depth_first_not_zero"] += 1
                else:
                    loop_reasons["other"] += 1
            else:
                edges.add(frozenset((vertex, neighbor)))
                if lazy_edge(neighbor, color, depth) != vertex:
                    failures.append({"kind": "edge_not_involution", "vertex": vertex, "color": color})

        for phase in ALPHABET:
            physical = physical_encoding(vertex, depth, phase)
            actual = update_physical_word(phase, physical)
            expected_vertex, expected_phase = candidate_step(vertex, phase, depth)
            expected = physical_encoding(expected_vertex, depth, expected_phase)
            unrotated = normalized_after_unrotation(actual, expected_phase)
            internal_index = first_internal_three(unrotated)
            if internal_index is not None:
                internal_three_failures += 1
                if len(failures) < 10:
                    failures.append(
                        {
                            "kind": "internal_3",
                            "vertex": vertex,
                            "phase": phase,
                            "word": physical,
                            "actual_unrotated": unrotated,
                            "index": internal_index,
                        }
                    )
            outside = exterior_receivers(phase, physical)
            if outside != (expected_phase, expected_phase):
                exterior_failures += 1
                if len(failures) < 10:
                    failures.append(
                        {
                            "kind": "exterior",
                            "vertex": vertex,
                            "phase": phase,
                            "outside": outside,
                            "expected": expected_phase,
                        }
                    )
            if actual != expected and len(failures) < 10:
                failures.append(
                    {
                        "kind": "one_step_conjugacy",
                        "vertex": vertex,
                        "phase": phase,
                        "physical": physical,
                        "actual": actual,
                        "expected_vertex": expected_vertex,
                        "expected": expected,
                    }
                )
            transition[(vertex, phase)] = (expected_vertex, expected_phase)

    # Independent finite graph checks.
    adjacency: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for edge in edges:
        left, right = tuple(edge)
        adjacency[left].add(right)
        adjacency[right].add(left)
    reached = {()}
    frontier = [()]
    while frontier:
        here = frontier.pop()
        for neighbor in adjacency[here]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)

    indegrees = Counter(transition.values())
    states = set(transition)
    permutation = set(indegrees) == states and all(indegrees[state] == 1 for state in states)
    unseen = set(states)
    cycle_lengths: list[int] = []
    while unseen:
        start = min(unseen, key=repr)
        here = start
        cycle: list[tuple[tuple[int, ...], int]] = []
        positions: dict[tuple[tuple[int, ...], int], int] = {}
        while here not in positions:
            positions[here] = len(cycle)
            cycle.append(here)
            here = transition[here]
        if positions[here] != 0:
            failures.append({"kind": "tail_into_cycle", "depth": depth, "start": start})
        cycle_lengths.append(len(cycle) - positions[here])
        unseen.difference_update(cycle)

    return {
        "depth": depth,
        "vertices": len(vertices),
        "phase_states": len(states),
        "nonloop_edges": len(edges),
        "connected": reached == vertex_set,
        "acyclic_by_edge_count": reached == vertex_set and len(edges) == len(vertices) - 1,
        "edge_involution_failures": sum(failure["kind"] == "edge_not_involution" for failure in failures),
        "missing_edge_loops": sum(loop_reasons.values()),
        "missing_edge_loop_reasons": dict(sorted(loop_reasons.items())),
        "internal_three_failures": internal_three_failures,
        "exterior_failures": exterior_failures,
        "one_step_failures": sum(failure["kind"] == "one_step_conjugacy" for failure in failures),
        "transition_is_permutation": permutation,
        "cycle_count": len(cycle_lengths),
        "cycle_lengths": sorted(cycle_lengths, reverse=True),
        "single_full_cycle": cycle_lengths == [len(states)],
        "first_failures": failures,
    }


def mutation_witnesses() -> dict[str, object]:
    """Small witnesses showing that boundary and phase conventions matter."""

    # Removing the lazy-loop rule immediately leaves the vertex set.
    raw = attempted_front_toggle((), 0)

    wrong_generator = None
    wrong_colors = (0, 1, 2)
    wrong_rotation = None
    for depth in range(1, 5):
        for vertex in enumerate_vertices(depth):
            for phase in ALPHABET:
                physical = physical_encoding(vertex, depth, phase)
                actual = update_physical_word(phase, physical)
                wrong_vertex = lazy_edge(vertex, wrong_colors[phase], depth)
                wrong_expected = physical_encoding(wrong_vertex, depth, (phase + 1) % 3)
                if wrong_generator is None and actual != wrong_expected:
                    wrong_generator = {
                        "depth": depth,
                        "vertex": vertex,
                        "phase": phase,
                        "actual": actual,
                        "wrong_expected": wrong_expected,
                    }

                negative_physical = tuple(
                    3 if letter == 3 else (letter - phase) % 3
                    for letter in (3,) * (depth - len(vertex)) + tuple(vertex)
                )
                negative_actual = update_physical_word(phase, negative_physical)
                next_vertex, next_phase = candidate_step(vertex, phase, depth)
                negative_expected = tuple(
                    3 if letter == 3 else (letter - next_phase) % 3
                    for letter in (3,) * (depth - len(next_vertex)) + tuple(next_vertex)
                )
                if wrong_rotation is None and negative_actual != negative_expected:
                    wrong_rotation = {
                        "depth": depth,
                        "vertex": vertex,
                        "phase": phase,
                        "actual": negative_actual,
                        "wrong_expected": negative_expected,
                    }
    return {
        "no_missing_edge_loop": {
            "depth": 1,
            "vertex": [],
            "color": 0,
            "raw_result": list(raw),
            "result_is_legal": legal_vertex(raw, 1),
        },
        "wrong_generator_order": wrong_generator,
        "negative_phase_rotation": wrong_rotation,
    }


def run(max_depth: int) -> dict[str, object]:
    audits = [audit_depth(depth) for depth in range(1, max_depth + 1)]
    local_failures = audit_local_toggle_table()
    return {
        "schema_version": 1,
        "method": "independent exhaustive reconstruction; no imports from src.tree_model",
        "max_depth": max_depth,
        "environment": {"python": sys.version, "platform": platform.platform()},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "audits": audits,
        "normalized_local_table_inputs_checked": 3 * 4**3,
        "normalized_local_table_failures": local_failures,
        "mutation_witnesses": mutation_witnesses(),
        "all_candidate_checks_pass": all(
            not local_failures
            and not audit["first_failures"]
            and audit["connected"]
            and audit["acyclic_by_edge_count"]
            and audit["transition_is_permutation"]
            and audit["single_full_cycle"]
            for audit in audits
        ),
        "interpretation": "finite exhaustive audit only; not an all-depth proof",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=12)
    args = parser.parse_args()
    report = run(args.max_depth)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["all_candidate_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
