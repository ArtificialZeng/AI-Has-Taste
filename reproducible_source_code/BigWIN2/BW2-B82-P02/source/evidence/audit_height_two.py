#!/usr/bin/env python3
"""Exact finite audit for the height-two coefficient identities.

The audit enumerates integer partitions of N-1 (the branch-order multisets),
constructs the corresponding rooted tree, and independently enumerates every
edge subset.  It obtains Psi from connected components of each spanning
forest; the proposed coefficient formulas are not used in that computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from typing import Iterable


def partitions(n: int, largest: int | None = None) -> Iterable[tuple[int, ...]]:
    """Yield all nonincreasing positive integer partitions of n."""
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    for first in range(largest, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def height_two_edges(branch_orders: tuple[int, ...]) -> tuple[int, list[tuple[int, int]]]:
    """Return vertex count and edges, with vertex 0 the root."""
    edges: list[tuple[int, int]] = []
    next_vertex = 1
    for order in branch_orders:
        center = next_vertex
        next_vertex += 1
        edges.append((0, center))
        for _ in range(order - 1):
            leaf = next_vertex
            next_vertex += 1
            edges.append((center, leaf))
    return next_vertex, edges


def forest_profile(
    vertex_count: int, edges: list[tuple[int, int]], mask: int
) -> tuple[int, tuple[int, ...]]:
    """Return (root-component size, sorted nonroot-component sizes)."""
    parent = list(range(vertex_count))
    size = [1] * vertex_count

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]

    for edge_index, (u, v) in enumerate(edges):
        if mask & (1 << edge_index):
            union(u, v)

    component_sizes: Counter[int] = Counter(find(v) for v in range(vertex_count))
    root_rep = find(0)
    root_size = component_sizes.pop(root_rep)
    return root_size, tuple(sorted(component_sizes.values()))


def profile_counter(branch_orders: tuple[int, ...]) -> Counter[tuple[int, tuple[int, ...]]]:
    vertex_count, edges = height_two_edges(branch_orders)
    profiles: Counter[tuple[int, tuple[int, ...]]] = Counter()
    for mask in range(1 << len(edges)):
        profiles[forest_profile(vertex_count, edges, mask)] += 1
    return profiles


def psi_from_profiles(
    profiles: Counter[tuple[int, tuple[int, ...]]], g: int
) -> Counter[tuple[int, ...]]:
    """Represent a monomial by its sorted tuple of variable subscripts."""
    polynomial: Counter[tuple[int, ...]] = Counter()
    for (root_size, other_sizes), multiplicity in profiles.items():
        monomial = tuple(sorted((g - 1 + root_size,) + other_sizes))
        polynomial[monomial] += multiplicity
    return polynomial


def elementary(values: tuple[int, ...]) -> list[int]:
    coefficients = [1]
    for value in values:
        coefficients.append(0)
        for k in range(len(coefficients) - 1, 0, -1):
            coefficients[k] += value * coefficients[k - 1]
    return coefficients


def canonical_signature(polynomial: Counter[tuple[int, ...]]) -> tuple:
    return tuple(sorted(polynomial.items()))


@dataclass
class AuditStats:
    rooted_types: int = 0
    edge_subsets: int = 0
    parameter_instances: int = 0
    coefficient_checks: int = 0
    root_degree_checks: int = 0
    polynomial_mass_checks: int = 0
    injectivity_checks: int = 0


def run(max_n: int, max_g: int) -> dict:
    if max_n < 1:
        raise ValueError("max_n must be at least 1")
    if max_g < 3:
        raise ValueError("max_g must be at least 3")

    stats = AuditStats()
    digest = hashlib.sha256()
    for n_vertices in range(1, max_n + 1):
        seen_by_g: dict[int, dict[tuple, tuple[int, ...]]] = {
            g: {} for g in range(3, max_g + 1)
        }
        for branch_orders in partitions(n_vertices - 1):
            stats.rooted_types += 1
            profiles = profile_counter(branch_orders)
            subset_count = 1 << (n_vertices - 1)
            stats.edge_subsets += subset_count
            if sum(profiles.values()) != subset_count:
                raise AssertionError(("profile mass", n_vertices, branch_orders))

            leaf_counts = tuple(order - 1 for order in branch_orders)
            expected_elementary = elementary(leaf_counts)
            max_k = (n_vertices - 1) // 2
            root_degree = len(branch_orders)

            for g in range(3, max_g + 1):
                stats.parameter_instances += 1
                polynomial = psi_from_profiles(profiles, g)
                if sum(polynomial.values()) != subset_count:
                    raise AssertionError(("Psi mass", n_vertices, g, branch_orders))
                stats.polynomial_mass_checks += 1

                for k in range(max_k + 1):
                    target = tuple(
                        sorted(
                            (g,)
                            + (2,) * k
                            + (1,) * (n_vertices - 1 - 2 * k)
                        )
                    )
                    actual = polynomial[target]
                    expected = (
                        expected_elementary[k]
                        if k < len(expected_elementary)
                        else 0
                    )
                    if actual != expected:
                        raise AssertionError(
                            (
                                "elementary coefficient",
                                n_vertices,
                                g,
                                branch_orders,
                                k,
                                actual,
                                expected,
                            )
                        )
                    stats.coefficient_checks += 1

                if n_vertices >= 2:
                    target = tuple(sorted((g + 1,) + (1,) * (n_vertices - 2)))
                    actual = polynomial[target]
                    if actual != root_degree:
                        raise AssertionError(
                            (
                                "root degree coefficient",
                                n_vertices,
                                g,
                                branch_orders,
                                actual,
                                root_degree,
                            )
                        )
                    stats.root_degree_checks += 1

                signature = canonical_signature(polynomial)
                prior = seen_by_g[g].get(signature)
                if prior is not None and prior != branch_orders:
                    raise AssertionError(
                        ("noninjective", n_vertices, g, prior, branch_orders)
                    )
                seen_by_g[g][signature] = branch_orders
                stats.injectivity_checks += 1

                digest.update(
                    repr((n_vertices, g, branch_orders, signature)).encode("ascii")
                )

    return {
        "audit": "height-two loopy-polynomial coefficient and injectivity audit",
        "method": (
            "integer partitions of N-1; explicit rooted graph; all 2^(N-1) "
            "edge subsets; union-find components; exact integer coefficients"
        ),
        "range": {"N": [1, max_n], "g": [3, max_g]},
        "status": "pass",
        "stats": stats.__dict__,
        "canonical_data_sha256": digest.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=14)
    parser.add_argument("--max-g", type=int, default=14)
    args = parser.parse_args()
    print(json.dumps(run(args.max_n, args.max_g), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
