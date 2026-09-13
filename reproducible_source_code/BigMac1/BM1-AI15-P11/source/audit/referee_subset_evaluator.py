#!/usr/bin/env python3
"""Independent exact evaluator for a serialized finite tree.

This audit program deliberately does not use rooted-tree dynamic programming.
It enumerates vertex subsets and tests every edge directly.  Its purpose is a
small, implementation-independent checker for discovery output, not scalable
discovery.

Input JSON schema:
    {"n": positive integer, "edges": [[u, v], ...]}
with vertices 0,...,n-1.  The graph must be a simple tree.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import pathlib
import sys
from typing import Iterable, Sequence


def _is_plain_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate_tree(data: object) -> tuple[int, tuple[tuple[int, int], ...]]:
    if not isinstance(data, dict) or set(data) != {"n", "edges"}:
        raise ValueError("input must be an object with exactly keys 'n' and 'edges'")
    n = data["n"]
    raw_edges = data["edges"]
    if not _is_plain_int(n) or n < 1:
        raise ValueError("n must be a positive integer")
    if not isinstance(raw_edges, list):
        raise ValueError("edges must be a list")

    seen: set[tuple[int, int]] = set()
    edges: list[tuple[int, int]] = []
    for item in raw_edges:
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError("each edge must be a two-element list")
        u, v = item
        if not _is_plain_int(u) or not _is_plain_int(v):
            raise ValueError("edge endpoints must be integers")
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError("edge endpoint outside 0,...,n-1")
        if u == v:
            raise ValueError("loops are not allowed")
        edge = (u, v) if u < v else (v, u)
        if edge in seen:
            raise ValueError("duplicate undirected edge")
        seen.add(edge)
        edges.append(edge)

    if len(edges) != n - 1:
        raise ValueError("a tree on n vertices must have exactly n-1 edges")

    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    reached = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in reached:
                reached.add(v)
                stack.append(v)
    if len(reached) != n:
        raise ValueError("graph is disconnected")
    return n, tuple(sorted(edges))


def independence_coeffs(
    n: int,
    edges: Sequence[tuple[int, int]],
    *,
    fixed_in: int = 0,
    fixed_out: int = 0,
) -> list[int]:
    """Count independent subsets by direct exhaustive inspection."""
    if fixed_in & fixed_out:
        return []
    counts = [0] * (n + 1)
    for mask in range(1 << n):
        if mask & fixed_in != fixed_in or mask & fixed_out:
            continue
        if any((mask & (1 << u)) and (mask & (1 << v)) for u, v in edges):
            continue
        counts[mask.bit_count()] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return counts


def triple_valley(coefficients: Sequence[int]) -> tuple[int | None, tuple[int, int, int] | None]:
    """Return exact Delta and a maximizing triple; None represents -infinity."""
    if len(coefficients) < 3:
        return None, None
    best: int | None = None
    witness: tuple[int, int, int] | None = None
    for k in range(len(coefficients) - 2):
        for ell in range(k + 1, len(coefficients) - 1):
            for m in range(ell + 1, len(coefficients)):
                value = min(
                    coefficients[k] - coefficients[ell],
                    coefficients[m] - coefficients[ell],
                )
                if best is None or value > best:
                    best = value
                    witness = (k, ell, m)
    return best, witness


def is_weakly_unimodal(coefficients: Sequence[int]) -> bool:
    return any(
        all(coefficients[j] <= coefficients[j + 1] for j in range(p))
        and all(coefficients[j] >= coefficients[j + 1] for j in range(p, len(coefficients) - 1))
        for p in range(len(coefficients))
    )


def _poly_add(a: Sequence[int], b: Sequence[int]) -> list[int]:
    result = [0] * max(len(a), len(b))
    for j, value in enumerate(a):
        result[j] += value
    for j, value in enumerate(b):
        result[j] += value
    return result


def _poly_mul(a: Sequence[int], b: Sequence[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for j, av in enumerate(a):
        for k, bv in enumerate(b):
            result[j + k] += av * bv
    return result


def _trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def _induced_relabel(
    vertices: Iterable[int], edges: Sequence[tuple[int, int]]
) -> tuple[int, tuple[tuple[int, int], ...], dict[int, int]]:
    ordered = sorted(vertices)
    relabel = {v: j for j, v in enumerate(ordered)}
    induced = tuple(
        (relabel[u], relabel[v]) for u, v in edges if u in relabel and v in relabel
    )
    return len(ordered), induced, relabel


def check_deletion_identity(n: int, edges: Sequence[tuple[int, int]], v: int) -> bool:
    lhs = independence_coeffs(n, edges)
    open_keep = [u for u in range(n) if u != v]
    n_open, e_open, _ = _induced_relabel(open_keep, edges)
    excluded = independence_coeffs(n_open, e_open) if n_open else [1]

    closed = {v}
    for a, b in edges:
        if a == v:
            closed.add(b)
        elif b == v:
            closed.add(a)
    closed_keep = [u for u in range(n) if u not in closed]
    n_closed, e_closed, _ = _induced_relabel(closed_keep, edges)
    remainder = independence_coeffs(n_closed, e_closed) if n_closed else [1]
    included = [0] + remainder
    return lhs == _trim(_poly_add(excluded, included))


def check_rooted_identity(n: int, edges: Sequence[tuple[int, int]], root: int) -> bool:
    """Check the rooted product formula using brute-force conditional counts."""
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent = [-2] * n
    parent[root] = -1
    order = [root]
    for u in order:
        for v in adjacency[u]:
            if parent[v] == -2:
                parent[v] = u
                order.append(v)

    whole_a = independence_coeffs(n, edges, fixed_out=1 << root)
    whole_b = independence_coeffs(n, edges, fixed_in=1 << root)
    rhs_a = [1]
    rhs_b_unshifted = [1]
    for child in adjacency[root]:
        vertices = [u for u in range(n) if u == child or _is_descendant(u, child, parent)]
        size, child_edges, relabel = _induced_relabel(vertices, edges)
        child_root = relabel[child]
        child_a = independence_coeffs(size, child_edges, fixed_out=1 << child_root)
        child_b = independence_coeffs(size, child_edges, fixed_in=1 << child_root)
        rhs_a = _poly_mul(rhs_a, _poly_add(child_a, child_b))
        rhs_b_unshifted = _poly_mul(rhs_b_unshifted, child_a)
    rhs_b = [0] + rhs_b_unshifted
    return whole_a == _trim(rhs_a) and whole_b == _trim(rhs_b)


def _is_descendant(vertex: int, ancestor: int, parent: Sequence[int]) -> bool:
    current = vertex
    while current >= 0:
        if current == ancestor:
            return True
        current = parent[current]
    return False


def _prufer_tree(code: Sequence[int]) -> tuple[int, tuple[tuple[int, int], ...]]:
    n = len(code) + 2
    degree = [1] * n
    for value in code:
        degree[value] += 1
    edges = []
    for value in code:
        leaf = next(j for j in range(n) if degree[j] == 1)
        edges.append((min(leaf, value), max(leaf, value)))
        degree[leaf] -= 1
        degree[value] -= 1
    leaves = [j for j in range(n) if degree[j] == 1]
    edges.append((leaves[0], leaves[1]))
    return n, tuple(sorted(edges))


def self_test() -> dict[str, int]:
    sequence_cases = 0
    for length in range(1, 8):
        for values in itertools.product(range(4), repeat=length):
            delta, _ = triple_valley(values)
            by_valley = delta is not None and delta > 0
            assert is_weakly_unimodal(values) == (not by_valley)
            sequence_cases += 1

    family_cases = 0
    for n in range(1, 16):
        path_edges = tuple((j, j + 1) for j in range(n - 1))
        path_expected = [math.comb(n - k + 1, k) for k in range((n + 1) // 2 + 1)]
        assert independence_coeffs(n, path_edges) == path_expected
        leaves = n - 1
        star_edges = tuple((0, j) for j in range(1, n))
        star_expected = [1] + [math.comb(leaves, k) + (1 if k == 1 else 0) for k in range(1, leaves + 1)]
        if n == 1:
            star_expected = [1, 1]
        assert independence_coeffs(n, star_edges) == star_expected
        family_cases += 2

    deletion_cases = 0
    for n in range(1, 6):
        possible_edges = list(itertools.combinations(range(n), 2))
        for edge_mask in range(1 << len(possible_edges)):
            edges = tuple(edge for j, edge in enumerate(possible_edges) if edge_mask & (1 << j))
            for v in range(n):
                assert check_deletion_identity(n, edges, v)
                deletion_cases += 1

    rooted_cases = 0
    assert check_rooted_identity(1, (), 0)
    rooted_cases += 1
    for n in range(2, 7):
        for code in itertools.product(range(n), repeat=n - 2):
            size, edges = _prufer_tree(code)
            for root in range(n):
                assert check_rooted_identity(size, edges, root)
                rooted_cases += 1

    malformed = [
        {},
        {"n": 1, "edges": [[0, 0]]},
        {"n": 3, "edges": [[0, 1]]},
        {"n": 3, "edges": [[0, 1], [1, 0]]},
        {"n": 4, "edges": [[0, 1], [1, 2], [0, 2]]},
    ]
    for value in malformed:
        try:
            validate_tree(value)
        except ValueError:
            pass
        else:
            raise AssertionError(f"malformed input was accepted: {value!r}")

    return {
        "sequence_characterization_cases": sequence_cases,
        "path_and_star_cases": family_cases,
        "deletion_identity_graph_vertex_cases": deletion_cases,
        "rooted_identity_tree_root_cases": rooted_cases,
        "malformed_inputs_rejected": len(malformed),
    }


def _weak_modes(values: Sequence[int]) -> set[int]:
    return {
        p
        for p in range(len(values))
        if all(values[j] <= values[j + 1] for j in range(p))
        and all(values[j] >= values[j + 1] for j in range(p, len(values) - 1))
    }


def rooted_hypothesis_audit(max_n: int) -> dict[str, object]:
    """Attack three tempting rooted-state closure hypotheses exactly."""
    if not 1 <= max_n <= 8:
        raise ValueError("rooted hypothesis audit max_n must lie in 1,...,8")
    rooted_cases = 0
    a_nonunimodal = 0
    b_nonunimodal = 0
    no_common_mode = 0
    cross_minor_changes_sign = 0
    first_no_common: dict[str, object] | None = None
    first_minor_change: dict[str, object] | None = None
    for n in range(1, max_n + 1):
        codes = [()] if n == 1 else itertools.product(range(n), repeat=n - 2)
        for code in codes:
            size, edges = (1, ()) if n == 1 else _prufer_tree(code)
            for root in range(n):
                a = independence_coeffs(size, edges, fixed_out=1 << root)
                b = independence_coeffs(size, edges, fixed_in=1 << root)
                rooted_cases += 1
                a_nonunimodal += not is_weakly_unimodal(a)
                b_nonunimodal += not is_weakly_unimodal(b)
                common_length = max(len(a), len(b))
                a_padded = a + [0] * (common_length - len(a))
                b_padded = b + [0] * (common_length - len(b))
                if not (_weak_modes(a_padded) & _weak_modes(b_padded)):
                    no_common_mode += 1
                    if first_no_common is None and n > 1:
                        first_no_common = {
                            "n": n,
                            "edges": edges,
                            "root": root,
                            "A": a_padded,
                            "B": b_padded,
                            "A_modes": sorted(_weak_modes(a_padded)),
                            "B_modes": sorted(_weak_modes(b_padded)),
                        }
                minors = [
                    a_padded[k] * b_padded[k + 1]
                    - a_padded[k + 1] * b_padded[k]
                    for k in range(common_length - 1)
                ]
                if minors and not (
                    all(value >= 0 for value in minors)
                    or all(value <= 0 for value in minors)
                ):
                    cross_minor_changes_sign += 1
                    if first_minor_change is None:
                        first_minor_change = {
                            "n": n,
                            "edges": edges,
                            "root": root,
                            "A": a_padded,
                            "B": b_padded,
                            "cross_minors": minors,
                        }
    return {
        "max_n": max_n,
        "rooted_labeled_cases": rooted_cases,
        "A_nonunimodal": a_nonunimodal,
        "B_nonunimodal": b_nonunimodal,
        "no_common_weak_mode": no_common_mode,
        "cross_minor_sign_changes": cross_minor_changes_sign,
        "first_nontrivial_no_common_mode": first_no_common,
        "first_cross_minor_sign_change": first_minor_change,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tree_json", nargs="?", type=pathlib.Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--rooted-audit-max-n", type=int)
    args = parser.parse_args()
    action_performed = False
    if args.self_test:
        print(json.dumps({"self_test": "PASS", **self_test()}, sort_keys=True))
        action_performed = True
    if args.rooted_audit_max_n is not None:
        try:
            result = rooted_hypothesis_audit(args.rooted_audit_max_n)
        except ValueError as exc:
            print(f"FAIL: {exc}", file=sys.stderr)
            return 2
        print(json.dumps({"rooted_hypothesis_audit": result}, sort_keys=True))
        action_performed = True
    if args.tree_json is None:
        if action_performed:
            return 0
        parser.error("tree_json is required unless --self-test is used")

    try:
        raw = args.tree_json.read_bytes()
        data = json.loads(raw)
        n, edges = validate_tree(data)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    coefficients = independence_coeffs(n, edges)
    delta, witness = triple_valley(coefficients)
    result = {
        "n": n,
        "edges": [list(edge) for edge in edges],
        "coefficients": coefficients,
        "alpha": len(coefficients) - 1,
        "delta": delta,
        "triple": list(witness) if witness is not None else None,
        "is_unimodal": is_weakly_unimodal(coefficients),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "code_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
