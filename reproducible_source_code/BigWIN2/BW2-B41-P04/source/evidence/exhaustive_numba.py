#!/usr/bin/env python3
"""Exact exhaustive computation for win-00041-p04.

Requires Python, NumPy, and Numba.  Numba changes execution speed, not the
integer recurrence.  The output contains all S_9 maximizers and deterministic
aggregate checksums of every (permutation, count) pair.
"""

import json
import math
import sys
import time

import numpy as np
from numba import njit


@njit
def popcount(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@njit
def make_rows(p, n, rows, inv, upper, lower):
    """Construct across-word adjacency masks; return the number of words."""
    for i in range(n):
        inv[p[i]] = i
        upper[i] = -1
        lower[i] = -1
    down_count = 0
    for j in range(n):
        if inv[j] > 0:
            upper[j] = down_count
            down_count += 1
        if inv[j] + 1 < n:
            lower[j] = down_count
            down_count += 1
    rc = 0
    for i in range(n):
        if p[i] > 0:
            mask = 0
            for j in range(p[i]):
                word = upper[j] if i < inv[j] else lower[j]
                mask |= 1 << word
            rows[rc] = mask
            rc += 1
        if p[i] + 1 < n:
            mask = 0
            for j in range(p[i] + 1, n):
                word = upper[j] if i < inv[j] else lower[j]
                mask |= 1 << word
            rows[rc] = mask
            rc += 1
    if rc != 2 * n - 2 or down_count != 2 * n - 2:
        return -1
    return rc


@njit
def permanent(p, n, cur, nxt, live, next_live, rows, inv, upper, lower):
    """Permanent by the exact F_{i+1}(S union {D}) subset recurrence."""
    if n == 1:
        return np.uint64(1)
    m = make_rows(p, n, rows, inv, upper, lower)
    if m < 0:
        return np.uint64(0)

    # Row permutation leaves the permanent invariant.  Insertion sorting by
    # degree limits live subset states and has no effect on the count.
    for i in range(1, m):
        key = rows[i]
        d = popcount(key)
        j = i - 1
        while j >= 0 and popcount(rows[j]) > d:
            rows[j + 1] = rows[j]
            j -= 1
        rows[j + 1] = key

    live[0] = 0
    live_count = 1
    cur[0] = 1
    for i in range(m):
        next_count = 0
        row = rows[i]
        for q in range(live_count):
            s = live[q]
            avail = row & ~s
            while avail:
                bit = avail & -avail
                t = s | bit
                if nxt[t] == 0:
                    next_live[next_count] = t
                    next_count += 1
                nxt[t] += cur[s]
                avail -= bit
        for q in range(live_count):
            cur[live[q]] = 0
        tmp = cur
        cur = nxt
        nxt = tmp
        tmp_live = live
        live = next_live
        next_live = tmp_live
        live_count = next_count
    answer = cur[(1 << m) - 1]
    for q in range(live_count):
        cur[live[q]] = 0
    return answer


@njit
def next_permutation(p, n):
    i = n - 2
    while i >= 0 and p[i] >= p[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = n - 1
    while p[j] <= p[i]:
        j -= 1
    p[i], p[j] = p[j], p[i]
    a, b = i + 1, n - 1
    while a < b:
        p[a], p[b] = p[b], p[a]
        a += 1
        b -= 1
    return True


@njit
def enumerate_n(n):
    p = np.arange(n, dtype=np.int64)
    cur = np.zeros(1 << 16, dtype=np.uint64)
    nxt = np.zeros(1 << 16, dtype=np.uint64)
    live = np.empty(1 << 16, dtype=np.int64)
    next_live = np.empty(1 << 16, dtype=np.int64)
    rows = np.empty(16, dtype=np.int64)
    inv = np.empty(9, dtype=np.int64)
    upper = np.empty(9, dtype=np.int64)
    lower = np.empty(9, dtype=np.int64)
    # This fixed capacity equals 9! and therefore also bounds every n <= 9.
    maximizers = np.empty((362880, n), dtype=np.int8)

    permutations = 0
    maximum = np.uint64(0)
    max_count = 0
    sum_counts = np.uint64(0)
    sum_squares = np.uint64(0)
    fnv = np.uint64(14695981039346656037)
    prime = np.uint64(1099511628211)
    while True:
        c = permanent(p, n, cur, nxt, live, next_live, rows, inv, upper, lower)
        permutations += 1
        sum_counts += c
        sum_squares += c * c
        for i in range(n):
            fnv = (fnv ^ np.uint64(p[i] + 1)) * prime
        for k in range(8):
            fnv = (fnv ^ np.uint64((c >> np.uint64(8 * k)) & np.uint64(255))) * prime
        if max_count == 0 or c > maximum:
            maximum = c
            max_count = 1
            for i in range(n):
                maximizers[0, i] = p[i]
        elif c == maximum:
            for i in range(n):
                maximizers[max_count, i] = p[i]
            max_count += 1
        if not next_permutation(p, n):
            break
    return (permutations, maximum, max_count, sum_counts, sum_squares, fnv,
            maximizers[:max_count])


def incidence_masks_python(p):
    """Separate plain-Python incidence construction for the recount."""
    n = len(p)
    if n == 1:
        return []
    inv = [0] * n
    for i, x in enumerate(p):
        inv[x] = i
    upper = [-1] * n
    lower = [-1] * n
    word = 0
    for j in range(n):
        if inv[j] > 0:
            upper[j] = word
            word += 1
        if inv[j] < n - 1:
            lower[j] = word
            word += 1
    rows = []
    for i, black in enumerate(p):
        if black > 0:
            mask = 0
            for j in range(black):
                mask |= 1 << (upper[j] if i < inv[j] else lower[j])
            rows.append(mask)
        if black < n - 1:
            mask = 0
            for j in range(black + 1, n):
                mask |= 1 << (upper[j] if i < inv[j] else lower[j])
            rows.append(mask)
    assert len(rows) == word == 2 * n - 2
    return rows


def direct_backtrack(rows, i=0, used=0):
    """Direct recursive enumeration: no DP, memoization, or row sorting."""
    if i == len(rows):
        return 1
    total = 0
    avail = rows[i] & ~used
    while avail:
        bit = avail & -avail
        total += direct_backtrack(rows, i + 1, used | bit)
        avail -= bit
    return total


def main():
    output = sys.argv[1] if len(sys.argv) > 1 else "exhaustive-results.json"
    published = [1, 1, 1, 5, 17, 73, 469, 3493]
    records = []
    n9_maximizers = []
    # Compile before recording per-n timings.
    enumerate_n(1)
    for n in range(1, 10):
        before = time.monotonic()
        result = enumerate_n(n)
        elapsed = time.monotonic() - before
        permutations, maximum, max_count, sums, squares, fnv, maxes = result
        print(
            f"n={n} permutations={permutations} max={int(maximum)} "
            f"maximizers={max_count} seconds={elapsed:.3f}",
            file=sys.stderr,
            flush=True,
        )
        records.append({
            "n": n,
            "permutations": int(permutations),
            "maximum": int(maximum),
            "maximizer_count": int(max_count),
            "sum_counts": str(int(sums)),
            "sum_squares": str(int(squares)),
            "stream_fnv1a64": f"{int(fnv):016x}",
        })
        if n == 9:
            n9_maximizers = ["".join(str(int(x) + 1) for x in row) for row in maxes]

    recounts = []
    for word in n9_maximizers:
        p = [int(x) - 1 for x in word]
        recounts.append(direct_backtrack(incidence_masks_python(p)))
    artifact = {
        "method": "lexicographic exhaustive enumeration; exact uint64 subset-DP permanent",
        "coverage_check": all(r["permutations"] == math.factorial(r["n"]) for r in records),
        "published_n_le_8_check": [r["maximum"] for r in records[:8]] == published,
        "results": records,
        "n9_maximizers": n9_maximizers,
        "n9_direct_backtracking_recounts": recounts,
        "all_n9_recounts_match": all(c == records[8]["maximum"] for c in recounts),
    }
    with open(output, "w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=2, sort_keys=True)
        f.write("\n")
    if not (artifact["coverage_check"] and artifact["published_n_le_8_check"]
            and artifact["all_n9_recounts_match"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
