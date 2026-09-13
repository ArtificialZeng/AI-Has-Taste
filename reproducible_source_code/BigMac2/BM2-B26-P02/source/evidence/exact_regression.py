#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Exact cross-check of two cover-time formulations on order-seven graphs.

Method A solves the visited-set recurrence, one visited subset at a time.
Method B uses inclusion-exclusion for the maximum of vertex hitting times;
each term is obtained from an absorbing hitting-time chain.  Both use exact
rational arithmetic, but their state spaces and recurrences are different.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def solve_fraction(matrix: list[list[int | Fraction]], rhs: list[int | Fraction]) -> list[Fraction]:
    """Gauss-Jordan elimination over Q (used only by Method A)."""
    n = len(rhs)
    a = [[Fraction(x) for x in row] + [Fraction(rhs[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            raise ArithmeticError("singular rational system")
        a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [x / q for x in a[col]]
        for r in range(n):
            if r == col or not a[r][col]:
                continue
            q = a[r][col]
            a[r] = [a[r][j] - q * a[col][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def visited_set_cover(adj: list[list[int]]) -> list[Fraction]:
    """Method A: exact visited-set recurrence C(x,A)."""
    n = len(adj)
    full = (1 << n) - 1
    degree = [sum(row) for row in adj]
    value: dict[tuple[int, int], Fraction] = {(full, x): Fraction(0) for x in range(n)}
    for size in range(n - 1, 0, -1):
        for mask in range(1, full):
            if mask.bit_count() != size:
                continue
            vertices = [x for x in range(n) if mask >> x & 1]
            matrix = []
            rhs = []
            for x in vertices:
                matrix.append([
                    degree[x] if x == y else -adj[x][y]
                    for y in vertices
                ])
                outside = sum(
                    value[(mask | (1 << y), y)]
                    for y in range(n)
                    if adj[x][y] and not (mask >> y & 1)
                )
                rhs.append(Fraction(degree[x]) + outside)
            solution = solve_fraction(matrix, rhs)
            for x, q in zip(vertices, solution):
                value[(mask, x)] = q
    return [value[(1 << s, s)] for s in range(n)]


def absorbing_ie_cover(adj: list[list[int]]) -> list[Fraction]:
    """Method B: inclusion-exclusion of exact absorbing-set hitting times.

    For nonempty S not containing s, E_s[min_{v in S} T_v] solves
    L[V\\S,V\\S] h = d.  Inclusion-exclusion for max_v T_v gives the
    cover time.  SymPy's exact-domain linear solver is intentionally used
    instead of Method A's Fraction eliminator.
    """
    n = len(adj)
    full = (1 << n) - 1
    degree = [sum(row) for row in adj]
    answer = [Fraction(0) for _ in range(n)]
    for unhit in range(1, full):
        vertices = [x for x in range(n) if unhit >> x & 1]
        matrix = sp.Matrix([
            [degree[x] if x == y else -adj[x][y] for y in vertices]
            for x in vertices
        ])
        rhs = sp.Matrix([degree[x] for x in vertices])
        solution = matrix.inv().multiply(rhs)
        targets = n - len(vertices)
        sign = 1 if targets % 2 else -1
        for x, q in zip(vertices, solution):
            answer[x] += sign * Fraction(int(q.p), int(q.q))
    return answer


def empty_graph(n: int) -> list[list[int]]:
    return [[0] * n for _ in range(n)]


def add_edges(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    adj = empty_graph(n)
    for u, v in edges:
        adj[u][v] = adj[v][u] = 1
    return adj


def with_edge(adj: list[list[int]], edge: tuple[int, int]) -> list[list[int]]:
    out = [row[:] for row in adj]
    u, v = edge
    assert not out[u][v]
    out[u][v] = out[v][u] = 1
    return out


def graph6(adj: list[list[int]]) -> str:
    n = len(adj)
    bits = [adj[i][j] for j in range(1, n) for i in range(j)]
    bits += [0] * (-len(bits) % 6)
    chars = [chr(n + 63)]
    for k in range(0, len(bits), 6):
        chars.append(chr(63 + sum(bits[k + j] << (5 - j) for j in range(6))))
    return "".join(chars)


def qstr(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def main() -> None:
    n = 7
    cycle_edges = [(i, (i + 1) % n) for i in range(n)]
    wheel_edges = [(0, i) for i in range(1, n)] + [
        (i, 1 + i % 6) for i in range(1, n)
    ]
    complete_minus_edges = [
        (i, j) for j in range(1, n) for i in range(j) if (i, j) != (0, 1)
    ]
    cases = [
        ("cycle7_plus_chord", add_edges(n, cycle_edges), (0, 2)),
        ("wheel7_plus_rim_chord", add_edges(n, wheel_edges), (1, 3)),
        ("complete7_minus_edge_to_complete7", add_edges(n, complete_minus_edges), (0, 1)),
    ]
    records = []
    for name, base, edge in cases:
        augmented = with_edge(base, edge)
        base_a = visited_set_cover(base)
        base_b = absorbing_ie_cover(base)
        aug_a = visited_set_cover(augmented)
        aug_b = absorbing_ie_cover(augmented)
        assert base_a == base_b, (name, "base mismatch")
        assert aug_a == aug_b, (name, "augmentation mismatch")
        assert all(x != y for x, y in zip(base_a, aug_a)), (name, "unexpected equality")
        records.append({
            "name": name,
            "base_graph6": graph6(base),
            "added_edge": list(edge),
            "augmented_graph6": graph6(augmented),
            "base_cover_times": [qstr(q) for q in base_a],
            "augmented_cover_times": [qstr(q) for q in aug_a],
            "differences": [qstr(y - x) for x, y in zip(base_a, aug_a)],
            "all_starts_agree_between_methods": True,
        })
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps({
        "arithmetic": "fractions.Fraction and SymPy Rational (exact)",
        "method_a": "visited-set same-layer recurrence",
        "method_b": "inclusion-exclusion of absorbing-set hitting chains",
        "order_seven_cases": len(records),
        "start_values_compared_per_graph": n,
        "records": records,
        "script_sha256": source_hash,
        "status": "pass",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
