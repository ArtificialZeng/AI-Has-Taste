#!/usr/bin/env python3
"""Exact modular rigidity-rank scan for complements of s C3 union t C4.

Every matrix entry comes from an integer placement.  A rank r calculation over
F_p proves that the same integer matrix has rational rank at least r.  When the
placement affinely spans Q^d, the usual trivial-motion kernel gives rational
rank at most r = dn-binomial(d+1,2), so a modular rank of r is an exact rank
certificate over Q.  For the first placement of each graph this program stores
an r by r minor with nonzero determinant modulo p.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

PRIME = 65521
TRIALS = 3
MAX_N = 28


def maxwell_dimension(n: int) -> tuple[int, int]:
    a = 0
    while a * (a + 1) < 2 * n:
        a += 1
    return n - 1 - a, a


def component_cycles(s: int, t: int) -> list[list[int]]:
    cycles: list[list[int]] = []
    v = 0
    for _ in range(s):
        cycles.append(list(range(v, v + 3)))
        v += 3
    for _ in range(t):
        cycles.append(list(range(v, v + 4)))
        v += 4
    return cycles


def complement_edges(s: int, t: int) -> list[tuple[int, int]]:
    n = 3 * s + 4 * t
    forbidden: set[tuple[int, int]] = set()
    for cyc in component_cycles(s, t):
        for i, u in enumerate(cyc):
            v = cyc[(i + 1) % len(cyc)]
            forbidden.add((min(u, v), max(u, v)))
    return [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if (u, v) not in forbidden
    ]


def coordinate(s: int, t: int, trial: int, v: int, j: int) -> int:
    # This precisely specified SHA-256 map avoids implementation-dependent RNGs.
    msg = f"win-00065-p04|{s}|{t}|{trial}|{v}|{j}".encode("ascii")
    z = int.from_bytes(hashlib.sha256(msg).digest()[:8], "big")
    return z % 2001 - 1000


def placement(s: int, t: int, d: int, trial: int) -> np.ndarray:
    n = 3 * s + 4 * t
    return np.array(
        [[coordinate(s, t, trial, v, j) for j in range(d)] for v in range(n)],
        dtype=np.int64,
    )


def rigidity_matrix(s: int, t: int, pmat: np.ndarray) -> np.ndarray:
    n, d = pmat.shape
    edges = complement_edges(s, t)
    mat = np.zeros((len(edges), n * d), dtype=np.int64)
    for k, (u, v) in enumerate(edges):
        delta = pmat[u] - pmat[v]
        mat[k, u * d : (u + 1) * d] = delta
        mat[k, v * d : (v + 1) * d] = -delta
    return mat


def modular_pivots(mat: np.ndarray, prime: int) -> tuple[int, list[int], list[int]]:
    a = np.remainder(mat, prime).astype(np.int64, copy=True)
    m, n = a.shape
    row_ids = list(range(m))
    pivot_rows: list[int] = []
    pivot_cols: list[int] = []
    rank = 0
    for col in range(n):
        nz = np.flatnonzero(a[rank:, col])
        if nz.size == 0:
            continue
        pivot = rank + int(nz[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
            row_ids[rank], row_ids[pivot] = row_ids[pivot], row_ids[rank]
        inv = pow(int(a[rank, col]), -1, prime)
        a[rank, col:] = a[rank, col:] * inv % prime
        if rank + 1 < m:
            factors = a[rank + 1 :, col].copy()
            active = np.flatnonzero(factors)
            if active.size:
                rows = rank + 1 + active
                a[rows, col:] = (
                    a[rows, col:] - factors[active, None] * a[rank, col:]
                ) % prime
        pivot_rows.append(row_ids[rank])
        pivot_cols.append(col)
        rank += 1
        if rank == m:
            break
    return rank, pivot_rows, pivot_cols


def determinant_mod(mat: np.ndarray, prime: int) -> int:
    a = np.remainder(mat, prime).astype(np.int64, copy=True)
    n, m = a.shape
    if n != m:
        raise ValueError("determinant requires a square matrix")
    det = 1
    for col in range(n):
        nz = np.flatnonzero(a[col:, col])
        if nz.size == 0:
            return 0
        pivot = col + int(nz[0])
        if pivot != col:
            a[[col, pivot]] = a[[pivot, col]]
            det = -det
        pv = int(a[col, col])
        det = det * pv % prime
        if col + 1 < n:
            factors = a[col + 1 :, col] * pow(pv, -1, prime) % prime
            active = np.flatnonzero(factors)
            if active.size:
                rows = col + 1 + active
                a[rows, col:] = (
                    a[rows, col:] - factors[active, None] * a[col, col:]
                ) % prime
    return det % prime


def affine_rank(pmat: np.ndarray, prime: int) -> int:
    aug = np.column_stack((np.ones(pmat.shape[0], dtype=np.int64), pmat))
    return modular_pivots(aug, prime)[0]


def main() -> None:
    cases = [
        (s, t)
        for s in range(MAX_N // 3 + 1)
        for t in range(MAX_N // 4 + 1)
        if 4 <= 3 * s + 4 * t <= MAX_N
    ]
    cases.sort(key=lambda st: (3 * st[0] + 4 * st[1], st[0], st[1]))
    records = []
    all_full = True
    for s, t in cases:
        n = 3 * s + 4 * t
        d, a = maxwell_dimension(n)
        edge_count = n * (n - 3) // 2
        target = d * n - d * (d + 1) // 2
        trial_records = []
        certificate = None
        for trial in range(TRIALS):
            pmat = placement(s, t, d, trial)
            affrank = affine_rank(pmat, PRIME) if d else 1
            rmat = rigidity_matrix(s, t, pmat)
            rank, rows, cols = modular_pivots(rmat, PRIME)
            exact_full_rank = affrank == d + 1 and rank == target
            all_full &= exact_full_rank
            trial_records.append(
                {
                    "trial": trial,
                    "affine_rank_mod_p": affrank,
                    "rigidity_rank_mod_p": rank,
                    "target_rank": target,
                    "exact_rational_rank_if_full": target if exact_full_rank else None,
                }
            )
            if trial == 0:
                if target == 0:
                    certificate = {
                        "trial": 0,
                        "row_indices": [],
                        "column_indices": [],
                        "determinant_mod_p": 1,
                    }
                elif exact_full_rank:
                    rows = rows[:target]
                    cols = cols[:target]
                    minor = rmat[np.ix_(rows, cols)]
                    det = determinant_mod(minor, PRIME)
                    if det == 0:
                        raise AssertionError("pivot minor unexpectedly singular")
                    certificate = {
                        "trial": 0,
                        "row_indices": rows,
                        "column_indices": cols,
                        "determinant_mod_p": det,
                    }
        records.append(
            {
                "s": s,
                "t": t,
                "n": n,
                "a_n": a,
                "dimension": d,
                "edge_count": edge_count,
                "target_rank": target,
                "trials": trial_records,
                "maximal_minor_certificate": certificate,
            }
        )
        print(f"(s,t)=({s},{t}) n={n} d={d} ranks={[x['rigidity_rank_mod_p'] for x in trial_records]}/{target}")
    output = {
        "scope": {
            "family": "G = complement of s C3 disjoint-union t C4",
            "conditions": "s,t nonnegative integers; 4 <= 3s+4t <= 28",
            "case_count": len(cases),
            "placements_per_case": TRIALS,
        },
        "method": {
            "coordinate_formula": "SHA256('win-00065-p04|s|t|trial|v|j') first 8 bytes big-endian, reduced modulo 2001, then minus 1000",
            "vertex_order": "all C3 components first, then C4 components; consecutive vertices; cyclic forbidden edges",
            "edge_order": "lexicographic pairs (u,v), u<v, excluding cycle edges",
            "prime": PRIME,
            "interpretation": "full affine rank mod p and rigidity rank r mod p certify affine spanning and exact rational rigidity rank r for the integer placement; a nonzero stored determinant mod p certifies a nonzero integer maximal minor",
        },
        "all_trials_full": all_full,
        "records": records,
    }
    out = Path(__file__).with_name("rigidity_rank_results.json")
    out.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}; all_trials_full={all_full}")


if __name__ == "__main__":
    main()
