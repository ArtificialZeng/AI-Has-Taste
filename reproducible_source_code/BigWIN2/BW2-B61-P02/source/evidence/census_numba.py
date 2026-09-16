#!/usr/bin/env python3
"""Numba implementation of the exact census described in census.cpp.

This is the executable implementation for the recorded run because the job
container has no C/C++ compiler.  All predicates use integer bit operations;
NumPy is used only for storage and deterministic bit packing.
"""

import csv
import sys
from pathlib import Path

import numpy as np
from numba import njit, prange


@njit(cache=True)
def popcount(x):
    answer = 0
    while x:
        x &= x - 1
        answer += 1
    return answer


@njit(cache=True)
def adjacency(n, edge_mask):
    result = np.zeros(n, dtype=np.int64)
    k = 0
    for v in range(1, n):
        for u in range(v):
            if (edge_mask >> k) & 1:
                result[u] |= 1 << v
                result[v] |= 1 << u
            k += 1
    return result


@njit(cache=True)
def is_connected(subset, adj):
    if subset == 0:
        return False
    seen = subset & -subset
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        v = 0
        temp = bit
        while temp > 1:
            temp >>= 1
            v += 1
        add = adj[v] & subset & ~seen
        seen |= add
        frontier |= add
    return seen == subset


@njit(cache=True)
def h_tables(n):
    m = n * (n - 1) // 2
    hn = 1 << m
    vn = 1 << n
    alpha = np.zeros((hn, vn), dtype=np.uint8)
    connected = np.zeros((hn, vn), dtype=np.uint8)
    for h in range(hn):
        adj = adjacency(n, h)
        for subset in range(1, vn):
            bit = subset & -subset
            v = 0
            temp = bit
            while temp > 1:
                temp >>= 1
                v += 1
            without = subset ^ bit
            a0 = alpha[h, without]
            a1 = 1 + alpha[h, without & ~adj[v]]
            alpha[h, subset] = a0 if a0 >= a1 else a1
            if is_connected(subset, adj):
                connected[h, subset] = 1
    return alpha, connected


@njit(cache=True)
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


@njit(cache=True)
def colorable_status(n, lists, hn):
    histogram = np.zeros(hn, dtype=np.uint64)
    if n == 0:
        histogram[0] = 1
    else:
        chosen = np.zeros(n, dtype=np.int64)
        for code0 in range(power(n, n)):
            code = code0
            allowed = True
            for v in range(n):
                c = code % n
                code //= n
                chosen[v] = c
                if ((lists[v] >> c) & 1) == 0:
                    allowed = False
                    break
            if not allowed:
                continue
            q = 0
            k = 0
            for v in range(1, n):
                for u in range(v):
                    if chosen[u] == chosen[v]:
                        q |= 1 << k
                    k += 1
            histogram[q] += 1
    result = np.zeros(hn, dtype=np.uint8)
    all_edges = hn - 1
    for q in range(hn):
        if histogram[q] == 0:
            continue
        available = all_edges ^ q
        h = available
        while True:
            result[h] = 1
            if h == 0:
                break
            h = (h - 1) & available
    return result


@njit(cache=True, parallel=True)
def census_layer(n, gmasks, alpha, connected):
    count = len(gmasks)
    hn = alpha.shape[0]
    vn = alpha.shape[1]
    hall = np.zeros((count, hn), dtype=np.uint8)
    colorable = np.zeros((count, hn), dtype=np.uint8)
    hall_count = np.zeros(count, dtype=np.uint64)
    colorable_count = np.zeros(count, dtype=np.uint64)
    bad_count = np.zeros(count, dtype=np.uint64)
    witness = np.full(count, -1, dtype=np.int64)
    consistency_error = np.zeros(count, dtype=np.uint8)
    for i in prange(count):
        lists = adjacency(n, gmasks[i])
        cstatus = colorable_status(n, lists, hn)
        for h in range(hn):
            colorable[i, h] = cstatus[h]
            good = 1
            for subset in range(1, vn):
                if connected[h, subset] == 0:
                    continue
                rhs = 0
                for c in range(n):
                    rhs += alpha[h, subset & lists[c]]
                if rhs < popcount(subset):
                    good = 0
                    break
            hall[i, h] = good
            hall_count[i] += good
            colorable_count[i] += cstatus[h]
            if cstatus[h] and not good:
                consistency_error[i] = 1
            if good and not cstatus[h]:
                bad_count[i] += 1
                if witness[i] < 0:
                    witness[i] = h
    return (hall, colorable, hall_count, colorable_count, bad_count, witness,
            consistency_error)


def packed_hex(row):
    return np.packbits(row, bitorder="little").tobytes().hex()


def load_reps(path):
    with open(path, newline="", encoding="ascii") as stream:
        return [
            (int(row["n"]), row["graph6"], int(row["edge_mask"]))
            for row in csv.DictReader(stream, delimiter="\t")
        ]


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: census_numba.py representatives.tsv census_exact.tsv")
    reps = load_reps(sys.argv[1])
    output = Path(sys.argv[2])
    with output.open("w", encoding="ascii", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow([
            "n", "graph6", "g_edge_mask", "num_H", "hall_count",
            "colorable_count", "bad_count", "witness_H", "hall_bits_hex",
            "colorable_bits_hex",
        ])
        for n in range(7):
            layer = [(code, mask) for rn, code, mask in reps if rn == n]
            gmasks = np.array([mask for _, mask in layer], dtype=np.int64)
            alpha, connected = h_tables(n)
            results = census_layer(n, gmasks, alpha, connected)
            hall, colorable, hc, cc, bc, witnesses, errors = results
            if np.any(errors):
                raise AssertionError(f"colorability without Hall in layer n={n}")
            for i, (code, mask) in enumerate(layer):
                writer.writerow([
                    n, code, mask, hall.shape[1], int(hc[i]), int(cc[i]),
                    int(bc[i]), int(witnesses[i]), packed_hex(hall[i]),
                    packed_hex(colorable[i]),
                ])
            stream.flush()
            print(
                f"completed n={n} classes={len(layer)} H_per_class={hall.shape[1]}",
                file=sys.stderr,
                flush=True,
            )


if __name__ == "__main__":
    main()
