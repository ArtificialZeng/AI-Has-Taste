#!/usr/bin/env python3
"""Exact verifier for the seam-correct transfer-automaton certificate.

The program reconstructs both automata from the literal graph constraints,
checks the integer positive-cone powers, and independently counts the finite
range by direct graph backtracking with one vertex colour fixed.  Correctness
checks are explicit and remain active under ``python -O``.
"""

from __future__ import annotations

import hashlib
import json
import sys
from itertools import product
from pathlib import Path
from typing import Callable, Sequence


HERE = Path(__file__).resolve().parent


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a: Sequence[Sequence[int]], b: Sequence[Sequence[int]]) -> list[list[int]]:
    n = len(a)
    require(n > 0 and len(b) == n, "matrix dimensions do not match")
    require(all(len(row) == n for row in a), "left matrix is not square")
    require(all(len(row) == n for row in b), "right matrix is not square")
    out = [[0] * n for _ in range(n)]
    for i, row in enumerate(a):
        for k, aik in enumerate(row):
            if aik:
                for j, bkj in enumerate(b[k]):
                    if bkj:
                        out[i][j] += aik * bkj
    return out


def matrix(
    states: Sequence[object], transition: Callable[[object, object], bool]
) -> list[list[int]]:
    return [[int(transition(source, target)) for target in states] for source in states]


def matrix_sha256(value: Sequence[Sequence[int]]) -> str:
    canonical = json.dumps(value, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(canonical).hexdigest()


def triple_states() -> list[tuple[int, int, int]]:
    return [
        state
        for state in product(range(3), repeat=3)
        if state[0] != state[1] and state[1] != state[2]
    ]


def triple_transition(source: object, target: object) -> bool:
    x = source
    y = target
    require(isinstance(x, tuple) and isinstance(y, tuple), "internal state type mismatch")
    return x[1:] == y[:2] and y[2] != x[2] and y[2] != x[0]


def paired_states(
    triples: Sequence[tuple[int, int, int]],
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    return [
        (upper, lower)
        for upper in triples
        for lower in triples
        if all(x != y for x, y in zip(upper, lower))
    ]


def paired_transition(source: object, target: object) -> bool:
    q = source
    r = target
    require(isinstance(q, tuple) and isinstance(r, tuple), "internal paired-state type mismatch")
    return triple_transition(q[0], r[0]) and triple_transition(q[1], r[1])


def graph_edges(n: int) -> tuple[tuple[int, int], ...]:
    edges: set[tuple[int, int]] = set()
    offsets = [1, 3] + ([n // 2] if n % 2 == 0 else [])
    for i in range(n):
        for offset in offsets:
            j = (i + offset) % n
            if i != j:
                edges.add((min(i, j), max(i, j)))
    return tuple(sorted(edges))


def direct_count_with_c0_zero(n: int) -> tuple[int, int]:
    """Complete exact graph-colouring recursion; no product-word enumeration."""
    neighbors = [set() for _ in range(n)]
    for i, j in graph_edges(n):
        neighbors[i].add(j)
        neighbors[j].add(i)
    colors = [-1] * n
    colors[0] = 0
    visited_nodes = 0

    def recurse(colored: int) -> int:
        nonlocal visited_nodes
        visited_nodes += 1
        if colored == n:
            return 1
        uncolored = [v for v in range(n) if colors[v] < 0]
        vertex = max(
            uncolored,
            key=lambda v: (
                len({colors[w] for w in neighbors[v] if colors[w] >= 0}),
                len(neighbors[v]),
                -v,
            ),
        )
        forbidden = {colors[w] for w in neighbors[vertex] if colors[w] >= 0}
        total = 0
        for color in range(3):
            if color not in forbidden:
                colors[vertex] = color
                total += recurse(colored + 1)
                colors[vertex] = -1
        return total

    return recurse(1), visited_nodes


def validate_schema(raw_data: object) -> dict:
    require(isinstance(raw_data, dict), "certificate root must be an object")
    data = raw_data
    require(
        set(data)
        == {
            "schema",
            "graph",
            "odd_automaton",
            "even_automaton",
            "finite_direct_counts_with_c0_fixed_to_zero",
            "claimed_zeros",
            "eventual_positivity_threshold",
        },
        "top-level certificate schema mismatch",
    )
    require(data["schema"] == "a383733-transfer-automata-certificate-v1", "schema name mismatch")
    require(
        data["graph"]
        == {
            "minimum_n": 6,
            "colors": [0, 1, 2],
            "cyclic_offsets": [1, 3],
            "even_diameter": True,
        },
        "literal graph definition mismatch",
    )
    odd = data["odd_automaton"]
    require(isinstance(odd, dict), "odd_automaton must be an object")
    require(
        set(odd)
        == {
            "state_rule",
            "transition_rule",
            "acceptance",
            "expected_state_count",
            "expected_transition_count",
            "transition_matrix_sha256",
            "full_positive_power",
            "positive_power_matrix_sha256",
            "power_min_entry",
            "power_max_entry",
            "power_entry_sum",
            "separate_positive_trace_n",
            "separate_trace_value",
        },
        "odd automaton schema mismatch",
    )
    require(
        odd["state_rule"] == "triples (x0,x1,x2) with x0!=x1 and x1!=x2"
        and odd["transition_rule"]
        == "(x0,x1,x2)->(x1,x2,x3) iff x3!=x2 and x3!=x0"
        and odd["acceptance"] == "a(n)=trace(O^n) for odd n>=7",
        "odd automaton definition text mismatch",
    )
    even = data["even_automaton"]
    require(isinstance(even, dict), "even_automaton must be an object")
    require(
        set(even)
        == {
            "state_rule",
            "transition_rule",
            "closure_rule",
            "acceptance",
            "expected_state_count",
            "expected_transition_count",
            "transition_matrix_sha256",
            "full_positive_half_power",
            "positive_power_matrix_sha256",
            "power_min_entry",
            "power_max_entry",
            "power_entry_sum",
            "naive_trace_counterexamples",
        },
        "even automaton schema mismatch",
    )
    require(
        even["state_rule"] == "ordered pairs of odd states with coordinatewise unequal colors"
        and even["transition_rule"] == "coordinatewise odd-automaton transition"
        and even["closure_rule"] == "after m steps end at the track-swap of the initial state"
        and even["acceptance"] == "a(2m)=trace(E^m P), where P is track swap",
        "even automaton definition text mismatch",
    )
    finite = data["finite_direct_counts_with_c0_fixed_to_zero"]
    require(isinstance(finite, dict), "finite direct counts must be an object")
    require(set(finite) == {str(n) for n in range(6, 26)}, "finite direct-count keys mismatch")
    require(
        all(type(value) is int and value >= 0 for value in finite.values()),
        "finite direct counts must be nonnegative integers",
    )
    require(data["claimed_zeros"] == [7, 8, 12, 16], "claimed zero list mismatch")
    require(data["eventual_positivity_threshold"] == 26, "eventual threshold mismatch")
    return data


def main() -> None:
    if len(sys.argv) > 2:
        fail("usage: verify_transfer_automata.py [certificate.json]")
    certificate_path = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) == 2
        else HERE.parent / "certificates" / "transfer_automata_certificate.json"
    )
    try:
        raw = certificate_path.read_bytes()
    except OSError as exc:
        fail(f"cannot read certificate: {exc}")
    try:
        parsed = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON: {exc}")
    data = validate_schema(parsed)

    odd_data = data["odd_automaton"]
    odd_states = triple_states()
    odd_matrix = matrix(odd_states, triple_transition)
    require(len(odd_states) == odd_data["expected_state_count"] == 12, "odd state count mismatch")
    require(sum(map(sum, odd_matrix)) == odd_data["expected_transition_count"] == 18, "odd edge count mismatch")
    require(matrix_sha256(odd_matrix) == odd_data["transition_matrix_sha256"], "odd matrix hash mismatch")
    require(all(any(row[j] for row in odd_matrix) for j in range(len(odd_matrix))), "odd matrix has a zero column")

    even_data = data["even_automaton"]
    even_states = paired_states(odd_states)
    even_matrix = matrix(even_states, paired_transition)
    require(len(even_states) == even_data["expected_state_count"] == 54, "even state count mismatch")
    require(sum(map(sum, even_matrix)) == even_data["expected_transition_count"] == 114, "even edge count mismatch")
    require(matrix_sha256(even_matrix) == even_data["transition_matrix_sha256"], "even matrix hash mismatch")
    require(all(any(row[j] for row in even_matrix) for j in range(len(even_matrix))), "even matrix has a zero column")
    even_index = {state: i for i, state in enumerate(even_states)}
    swap = [even_index[(lower, upper)] for upper, lower in even_states]
    require(all(swap[swap[i]] == i for i in range(len(swap))), "track swap is not an involution")
    require(
        all(even_matrix[i][j] == even_matrix[swap[i]][swap[j]] for i in range(54) for j in range(54)),
        "track swap does not preserve transitions",
    )

    odd_powers: dict[int, list[list[int]]] = {0: identity(12)}
    for exponent in range(1, 26):
        odd_powers[exponent] = matmul(odd_powers[exponent - 1], odd_matrix)
    odd_power = odd_powers[odd_data["full_positive_power"]]
    odd_entries = [value for row in odd_power for value in row]
    require(matrix_sha256(odd_power) == odd_data["positive_power_matrix_sha256"], "odd positive-power hash mismatch")
    require(min(odd_entries) > 0, "claimed odd power is not strictly positive")
    require(min(odd_entries) == odd_data["power_min_entry"], "odd power minimum mismatch")
    require(max(odd_entries) == odd_data["power_max_entry"], "odd power maximum mismatch")
    require(sum(odd_entries) == odd_data["power_entry_sum"], "odd power entry sum mismatch")
    base_n = odd_data["separate_positive_trace_n"]
    base_trace = sum(odd_powers[base_n][i][i] for i in range(12))
    require(base_trace == odd_data["separate_trace_value"] > 0, "separate odd base trace mismatch")

    even_powers: dict[int, list[list[int]]] = {0: identity(54)}
    for exponent in range(1, even_data["full_positive_half_power"] + 1):
        even_powers[exponent] = matmul(even_powers[exponent - 1], even_matrix)
    even_power = even_powers[even_data["full_positive_half_power"]]
    even_entries = [value for row in even_power for value in row]
    require(matrix_sha256(even_power) == even_data["positive_power_matrix_sha256"], "even positive-power hash mismatch")
    require(min(even_entries) > 0, "claimed even power is not strictly positive")
    require(min(even_entries) == even_data["power_min_entry"], "even power minimum mismatch")
    require(max(even_entries) == even_data["power_max_entry"], "even power maximum mismatch")
    require(sum(even_entries) == even_data["power_entry_sum"], "even power entry sum mismatch")

    naive = even_data["naive_trace_counterexamples"]
    require(set(naive) == {"6", "8"}, "naive-trace counterexample keys mismatch")
    for n_text, expected in naive.items():
        require(set(expected) == {"ordinary_trace", "twisted_trace"}, "naive-trace record schema mismatch")
        m = int(n_text) // 2
        power = even_powers[m]
        ordinary = sum(power[i][i] for i in range(54))
        twisted = sum(power[i][swap[i]] for i in range(54))
        require(
            {"ordinary_trace": ordinary, "twisted_trace": twisted} == expected,
            f"naive-trace counterexample mismatch at n={n_text}",
        )

    finite_expected = data["finite_direct_counts_with_c0_fixed_to_zero"]
    finite_actual: dict[str, int] = {}
    recursion_nodes: dict[str, int] = {}
    automaton_counts: dict[str, int] = {}
    for n in range(6, 26):
        count, nodes = direct_count_with_c0_zero(n)
        finite_actual[str(n)] = count
        recursion_nodes[str(n)] = nodes
        if n % 2:
            automaton_count = sum(odd_powers[n][i][i] for i in range(12))
        else:
            m = n // 2
            power = even_powers[m]
            automaton_count = sum(power[i][swap[i]] for i in range(54))
        automaton_counts[str(n)] = automaton_count
        require(automaton_count == 3 * count, f"automaton/direct count mismatch at n={n}")
    require(finite_actual == finite_expected, "finite direct graph counts mismatch")
    zeros = [n for n in range(6, 26) if finite_actual[str(n)] == 0]
    require(zeros == data["claimed_zeros"], "finite zero set mismatch")

    # Exact cone certificate: A^r is strictly positive, and every column of A
    # is nonzero, so A^(r+t) is strictly positive for every t>=0.  Hence odd
    # trace positivity holds from n=10 (with n=9 checked separately), and the
    # swap-twisted even trace is positive for every m>=13, i.e. n>=26.
    require(odd_data["full_positive_power"] == 10, "odd propagation endpoint mismatch")
    require(even_data["full_positive_half_power"] == 13, "even propagation endpoint mismatch")
    require(data["eventual_positivity_threshold"] == 2 * 13, "global threshold is inconsistent")

    certificate_hash = hashlib.sha256(raw).hexdigest()
    verifier_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "status": "PASS",
                "certificate_sha256": certificate_hash,
                "verifier_sha256": verifier_hash,
                "odd_states": 12,
                "odd_transitions": 18,
                "odd_full_positive_power": 10,
                "even_states": 54,
                "even_transitions": 114,
                "even_full_positive_half_power": 13,
                "eventual_positivity_threshold_n": 26,
                "finite_direct_range": [6, 25],
                "finite_zeros": zeros,
                "finite_automaton_counts": automaton_counts,
                "direct_recursion_nodes": recursion_nodes,
                "naive_trace_counterexamples": naive,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
