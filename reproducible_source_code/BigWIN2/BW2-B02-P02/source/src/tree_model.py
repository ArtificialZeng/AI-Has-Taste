#!/usr/bin/env python3
"""Exact symbolic tree model for the RESOCA-115 odd-k orbit.

This module is a certification aid, not the proof itself.  It uses only integer
and bit operations.  A site symbol is ``2 * previous + current``.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable, Iterator, Sequence


COLORS = (0, 1, 2)
GENERATOR_BY_PHASE = (1, 0, 2)


def rule115(left: int, center: int, right: int) -> int:
    """Return ECA rule 115 by direct Wolfram-table lookup."""
    index = (left << 2) | (center << 1) | right
    return (115 >> index) & 1


def rotate_symbol(symbol: int, amount: int) -> int:
    """Apply the color cycle (0 1 2)^amount, fixing symbol 3."""
    if symbol == 3:
        return 3
    return (symbol + amount) % 3


def symbol_step(left: int, center: int, right: int) -> int:
    """One RESOCA step on a site's three-symbol neighborhood."""
    previous = center >> 1
    current = center & 1
    next_current = previous ^ rule115(left & 1, current, right & 1)
    return (current << 1) | next_current


def physical_step(phase: int, word: Sequence[int]) -> tuple[int, ...]:
    """Step a finite word whose two exterior symbols are the phase color."""
    if phase not in COLORS:
        raise ValueError("phase must be 0, 1, or 2")
    if not word:
        raise ValueError("word must be nonempty")
    result = []
    for index, center in enumerate(word):
        left = phase if index == 0 else word[index - 1]
        right = phase if index + 1 == len(word) else word[index + 1]
        result.append(symbol_step(left, center, right))
    return tuple(result)


def vertex_ok(vertex: Sequence[int], length: int) -> bool:
    """Check the reduced-word vertex set V_length."""
    size = len(vertex)
    if size > length:
        return False
    if any(letter not in COLORS for letter in vertex):
        return False
    if any(a == b for a, b in zip(vertex, vertex[1:])):
        return False
    if size and vertex[-1] == 0:
        return False
    if size == length and vertex[0] != 0:
        return False
    return True


def vertices(length: int) -> Iterator[tuple[int, ...]]:
    """Enumerate V_length without trusting the closed count formula."""
    if length < 1:
        raise ValueError("length must be positive")
    yield ()
    for size in range(1, length + 1):
        for vertex in product(COLORS, repeat=size):
            if vertex_ok(vertex, length):
                yield vertex


def normalized_word(vertex: Sequence[int], length: int) -> tuple[int, ...]:
    if not vertex_ok(vertex, length):
        raise ValueError("not a tree vertex")
    return (3,) * (length - len(vertex)) + tuple(vertex)


def word_to_vertex(word: Sequence[int]) -> tuple[int, ...]:
    """Remove the leading run of symbol 3."""
    cut = 0
    while cut < len(word) and word[cut] == 3:
        cut += 1
    vertex = tuple(word[cut:])
    if not vertex_ok(vertex, len(word)):
        raise ValueError("word is not normalized admissible")
    return vertex


def physical_word(vertex: Sequence[int], length: int, phase: int) -> tuple[int, ...]:
    return tuple(rotate_symbol(symbol, phase) for symbol in normalized_word(vertex, length))


def edge_involution(vertex: Sequence[int], color: int, length: int) -> tuple[int, ...]:
    """Traverse the color edge, or stay when that edge is missing."""
    if color not in COLORS or not vertex_ok(vertex, length):
        raise ValueError("invalid color or vertex")
    vertex = tuple(vertex)
    if vertex and vertex[0] == color:
        candidate = vertex[1:]
    else:
        candidate = (color,) + vertex
    return candidate if vertex_ok(candidate, length) else vertex


def tree_state_step(
    vertex: Sequence[int], phase: int, length: int
) -> tuple[tuple[int, ...], int]:
    color = GENERATOR_BY_PHASE[phase]
    return edge_involution(vertex, color, length), (phase + 1) % 3


def conjugacy_holds(vertex: Sequence[int], phase: int, length: int) -> bool:
    physical = physical_word(vertex, length, phase)
    stepped = physical_step(phase, physical)
    expected_vertex, expected_phase = tree_state_step(vertex, phase, length)
    expected = physical_word(expected_vertex, length, expected_phase)
    return stepped == expected


def tree_edges(length: int) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    result = set()
    for vertex in vertices(length):
        for color in COLORS:
            neighbor = edge_involution(vertex, color, length)
            if neighbor != vertex:
                result.add(tuple(sorted((vertex, neighbor))))
    return result


def orbit(vertex: Sequence[int], phase: int, length: int) -> list[tuple[tuple[int, ...], int]]:
    start = (tuple(vertex), phase)
    state = start
    result = []
    seen = set()
    while state not in seen:
        seen.add(state)
        result.append(state)
        state = tree_state_step(*state, length)
    if state != start:
        raise AssertionError("entered a cycle away from the start")
    return result


def odd_k_initial_vertex(k: int) -> tuple[int, ...]:
    """Return the normalized phase-zero word/vertex for the locked initial pair."""
    if k < 1 or k % 2 == 0:
        raise ValueError("k must be a positive odd integer")
    sites = range(-k - 1, k + 1)
    symbols = []
    for site in sites:
        previous = int(site == 0)
        current = int(-k <= site <= k and (site + k) % 2 == 0)
        symbols.append((previous << 1) | current)
    vertex = word_to_vertex(symbols)
    if len(vertex) != 2 * k + 2:
        raise AssertionError("odd-k initial word should have no leading 3")
    return vertex


def predicted_vertex_count(length: int) -> int:
    if length % 2:
        raise ValueError("closed target count is used only for even length")
    return ((1 << (length + 2)) - 1) // 3


def exhaustive_audit(max_length: int = 8) -> None:
    """Exhaustively audit all vertices and phases through max_length."""
    for length in range(1, max_length + 1):
        all_vertices = list(vertices(length))
        for vertex in all_vertices:
            for phase in COLORS:
                if not conjugacy_holds(vertex, phase, length):
                    raise AssertionError(("conjugacy", length, vertex, phase))
        edges = tree_edges(length)
        if len(edges) != len(all_vertices) - 1:
            raise AssertionError(("not a tree", length, len(edges), len(all_vertices)))
        tour = orbit((), 0, length)
        if len(tour) != 3 * len(all_vertices):
            raise AssertionError(("not one tour", length, len(tour), len(all_vertices)))
        if length % 2 == 0 and len(all_vertices) != predicted_vertex_count(length):
            raise AssertionError(("count", length, len(all_vertices)))


if __name__ == "__main__":
    exhaustive_audit(12)
    print("PASS: conjugacy, tree, one-tour, and even-length counts through N=12")
