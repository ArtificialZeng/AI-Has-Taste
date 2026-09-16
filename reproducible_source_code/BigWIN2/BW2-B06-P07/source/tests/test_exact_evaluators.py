#!/usr/bin/env python3
"""Hand-computable exact tests for the two discovery evaluators."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from explore_trees import (  # noqa: E402
    distance_matrix,
    exact_md,
    is_resolving_shells,
    is_resolving_sorted,
    shell_masks,
)


def path(n: int) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[i].append(i + 1)
        adj[i + 1].append(i)
    return adj


def star(leaves: int) -> list[list[int]]:
    adj = [[] for _ in range(leaves + 1)]
    for i in range(1, leaves + 1):
        adj[0].append(i)
        adj[i].append(0)
    return adj


def check_both(adj: list[list[int]], chosen: tuple[int, ...], expected: bool) -> None:
    dist = distance_matrix(adj)
    mask = sum(1 << v for v in chosen)
    assert is_resolving_sorted(dist, chosen) is expected
    assert is_resolving_shells(shell_masks(dist), mask) is expected


def main() -> None:
    check_both(path(5), (0,), True)
    check_both(path(5), (0, 4), False)
    assert exact_md(distance_matrix(path(5)))[:2] == (1, (0,))

    # Three twin leaves force infinity: all subsets are checked by exact_md.
    md, witness, tested = exact_md(distance_matrix(star(3)))
    assert md is None and witness is None and tested == 16

    # P3 is a path despite also being a two-leaf star.
    assert exact_md(distance_matrix(star(2)))[0] == 1
    print("exact evaluator tests: PASS")


if __name__ == "__main__":
    main()
