#!/usr/bin/env python3
"""Exhaustive exact search over two-chain presentations of width-two posets.

For chains A_0<...<A_{a-1} and B_0<...<B_{b-1}, L_i is the number
of B's below A_i and U_i is the first index of a B above A_i.  Precisely
the nondecreasing pairs 0 <= L_i <= U_i <= b define transitive orders.
Every width-at-most-two poset occurs because of Dilworth's theorem.  We use
a <= b because the two chains can be swapped.

Linear-extension counts and rank sums are computed as exact uint64 integers
by lattice-path prefix/suffix DP.  The command is deliberately limited to
n <= 19: n*n! < 2**64 there, certifying that every intermediate value fits.
The criterion is tested without enumerating maximal chains.  A maximal chain
has gap <= 4 exactly when the cover graph has a minimal-to-maximal path all of
whose endpoint and edge rank-sum differences are <= 4*e(P).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from typing import Iterator

import numba as nb
import numpy as np


@nb.njit(cache=True)
def test_one(L: np.ndarray, U: np.ndarray, a: int, b: int):
    """Return (is_width_two, qualifies, extension_count, rank_sums)."""
    n = a + b
    incomparable = False
    for i in range(a):
        if L[i] < U[i]:
            incomparable = True
    empty_sums = np.zeros(19, dtype=np.uint64)
    if not incomparable:  # all cross-pairs comparable: the order is a chain
        return False, False, np.uint64(0), empty_sums

    K = np.zeros(b, dtype=np.int8)
    for j in range(b):
        for i in range(a):
            if U[i] <= j:
                K[j] += 1

    F = np.zeros((a + 1, b + 1), dtype=np.uint64)
    G = np.zeros((a + 1, b + 1), dtype=np.uint64)
    F[0, 0] = 1
    for i in range(a + 1):
        for j in range(b + 1):
            z = F[i, j]
            if i < a and j >= L[i]:
                F[i + 1, j] += z
            if j < b and i >= K[j]:
                F[i, j + 1] += z
    G[a, b] = 1
    for i in range(a, -1, -1):
        for j in range(b, -1, -1):
            if i == a and j == b:
                continue
            if i < a and j >= L[i]:
                G[i, j] += G[i + 1, j]
            if j < b and i >= K[j]:
                G[i, j] += G[i, j + 1]
    extensions = F[a, b]
    S = np.zeros(19, dtype=np.uint64)
    for i in range(a):
        for j in range(L[i], b + 1):
            S[i] += F[i, j] * G[i + 1, j] * np.uint64(i + j + 1)
    for j in range(b):
        for i in range(K[j], a + 1):
            S[a + j] += F[i, j] * G[i, j + 1] * np.uint64(i + j + 1)

    # below[y] has bit x iff x<y; above is its transpose.
    below = np.zeros(n, dtype=np.uint64)
    above = np.zeros(n, dtype=np.uint64)
    one = np.uint64(1)
    for i in range(a):
        for x in range(i):
            below[i] |= one << np.uint64(x)
        for j in range(L[i]):
            below[i] |= one << np.uint64(a + j)
    for j in range(b):
        for k in range(j):
            below[a + j] |= one << np.uint64(a + k)
        for i in range(a):
            if U[i] <= j:
                below[a + j] |= one << np.uint64(i)
    for y in range(n):
        for x in range(n):
            if (below[y] >> np.uint64(x)) & one:
                above[x] |= one << np.uint64(y)

    reachable = np.zeros(n, dtype=np.bool_)
    four_e = np.uint64(4) * extensions
    for x in range(n):
        if below[x] == 0 and S[x] <= four_e:
            reachable[x] = True
    # A-elements precede B-elements in the array, which need not be a
    # topological order when some B<A.  Repeated relaxation is label-agnostic.
    for unused in range(n):
        changed = False
        for x in range(n):
            if not reachable[x]:
                continue
            for y in range(n):
                if ((above[x] >> np.uint64(y)) & one) == 0:
                    continue
                if (above[x] & below[y]) != 0:  # x<y, but not a cover
                    continue
                if S[y] - S[x] <= four_e and not reachable[y]:
                    reachable[y] = True
                    changed = True
        if not changed:
            break
    for x in range(n):
        if above[x] == 0 and reachable[x]:
            if np.uint64(n + 1) * extensions - S[x] <= four_e:
                return True, False, extensions, S
    return True, True, extensions, S


@nb.njit(cache=True, parallel=True)
def test_batch(Ls: np.ndarray, Us: np.ndarray, a: int, b: int):
    m = Ls.shape[0]
    width = np.zeros(m, dtype=np.uint8)
    good = np.zeros(m, dtype=np.uint8)
    for r in nb.prange(m):
        w, q, _, _ = test_one(Ls[r], Us[r], a, b)
        width[r] = w
        good[r] = q
    return width, good


def presentations(a: int, b: int) -> Iterator[tuple[tuple[int, ...], tuple[int, ...]]]:
    """Generate every pair of nondecreasing L,U with L_i<=U_i."""
    L = [0] * a
    U = [0] * a

    def rec(i: int, last_l: int, last_u: int):
        if i == a:
            yield tuple(L), tuple(U)
            return
        for ell in range(last_l, b + 1):
            L[i] = ell
            for upper in range(max(last_u, ell), b + 1):
                U[i] = upper
                yield from rec(i + 1, ell, upper)

    yield from rec(0, 0, 0)


def witness_record(L, U, a, b):
    w, q, e, sums = test_one(
        np.asarray(L, dtype=np.int8), np.asarray(U, dtype=np.int8), a, b
    )
    assert w and q
    n = a + b
    below = []
    for i in range(a):
        mask = sum(1 << x for x in range(i))
        mask |= sum(1 << (a + j) for j in range(L[i]))
        below.append(format(mask, "x"))
    for j in range(b):
        mask = sum(1 << (a + k) for k in range(j))
        mask |= sum(1 << i for i in range(a) if U[i] <= j)
        below.append(format(mask, "x"))
    return {
        "n": n, "a": a, "b": b, "L": list(L), "U": list(U),
        "extensions": int(e), "rank_sums": [int(x) for x in sums[:n]],
        "below_hex": below,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("max_n", type=int, nargs="?", default=12)
    parser.add_argument("--min-n", type=int, default=4)
    parser.add_argument("--batch-size", type=int, default=100_000)
    parser.add_argument("--stop-at-first", action="store_true")
    args = parser.parse_args()
    if not 4 <= args.max_n <= 19:
        parser.error("max_n must lie in [4,19], the certified uint64 range")
    if not 4 <= args.min_n <= args.max_n:
        parser.error("min_n must lie in [4,max_n]")

    # Force compilation outside the timed order records.
    test_one(np.array([0], np.int8), np.array([1], np.int8), 1, 1)
    test_batch(np.array([[0]], np.int8), np.array([[1]], np.int8), 1, 1)
    report = {"format": "width2-search-v1", "orders": [], "witnesses": []}
    for n in range(args.min_n, args.max_n + 1):
        started = time.monotonic()
        order_p = order_w = order_q = 0
        stop = False
        for a in range(1, n // 2 + 1):
            b = n - a
            iterator = presentations(a, b)
            while True:
                rows = []
                try:
                    for _ in range(args.batch_size):
                        rows.append(next(iterator))
                except StopIteration:
                    pass
                if not rows:
                    break
                Ls = np.asarray([x[0] for x in rows], dtype=np.int8)
                Us = np.asarray([x[1] for x in rows], dtype=np.int8)
                width, good = test_batch(Ls, Us, a, b)
                order_p += len(rows)
                order_w += int(width.sum())
                indices = np.flatnonzero(good)
                order_q += len(indices)
                for r in indices:
                    report["witnesses"].append(witness_record(*rows[int(r)], a, b))
                if len(rows) < args.batch_size:
                    break
                if indices.size and args.stop_at_first:
                    stop = True
                    break
            if stop:
                break
        entry = {
            "n": n, "presentations": order_p,
            "width_two_presentations": order_w,
            "qualifying_presentations": order_q,
            "seconds": round(time.monotonic() - started, 6),
        }
        report["orders"].append(entry)
        print(json.dumps(entry, sort_keys=True), file=sys.stderr, flush=True)
        if stop:
            break
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
