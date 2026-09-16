#!/usr/bin/env python3
"""Independent verifier for rigidity_rank_results.json certificates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def coord(s: int, t: int, trial: int, v: int, j: int) -> int:
    raw = f"win-00065-p04|{s}|{t}|{trial}|{v}|{j}".encode("ascii")
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big") % 2001 - 1000


def graph_edges(s: int, t: int) -> list[tuple[int, int]]:
    n = 3 * s + 4 * t
    deleted: set[tuple[int, int]] = set()
    start = 0
    for length, count in ((3, s), (4, t)):
        for _ in range(count):
            vertices = list(range(start, start + length))
            start += length
            for k in range(length):
                pair = sorted((vertices[k], vertices[(k + 1) % length]))
                deleted.add((pair[0], pair[1]))
    return [(u, v) for u in range(n) for v in range(u + 1, n) if (u, v) not in deleted]


def make_matrix(s: int, t: int, d: int, trial: int) -> tuple[np.ndarray, np.ndarray]:
    n = 3 * s + 4 * t
    points = np.array([[coord(s, t, trial, v, j) for j in range(d)] for v in range(n)], dtype=np.int64)
    matrix = np.zeros((len(graph_edges(s, t)), n * d), dtype=np.int64)
    for row, (u, v) in enumerate(graph_edges(s, t)):
        delta = points[u] - points[v]
        matrix[row, u*d:(u+1)*d] = delta
        matrix[row, v*d:(v+1)*d] = -delta
    return points, matrix


def rank_mod(matrix: np.ndarray, p: int) -> int:
    a = matrix.copy() % p
    rank = 0
    for col in range(a.shape[1]):
        choices = np.flatnonzero(a[rank:, col])
        if not choices.size:
            continue
        pivot = rank + int(choices[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        inv = pow(int(a[rank, col]), p - 2, p)
        a[rank] = a[rank] * inv % p
        for row in range(rank + 1, a.shape[0]):
            factor = int(a[row, col])
            if factor:
                a[row] = (a[row] - factor * a[rank]) % p
        rank += 1
        if rank == a.shape[0]:
            break
    return rank


def det_mod(matrix: np.ndarray, p: int) -> int:
    a = matrix.copy() % p
    det = 1
    for col in range(a.shape[0]):
        choices = np.flatnonzero(a[col:, col])
        if not choices.size:
            return 0
        pivot = col + int(choices[0])
        if pivot != col:
            a[[col, pivot]] = a[[pivot, col]]
            det = -det
        value = int(a[col, col])
        det = det * value % p
        inv = pow(value, p - 2, p)
        for row in range(col + 1, a.shape[0]):
            factor = int(a[row, col]) * inv % p
            if factor:
                a[row, col:] = (a[row, col:] - factor * a[col, col:]) % p
    return det % p


def main() -> None:
    data = json.loads((HERE / "rigidity_rank_results.json").read_text(encoding="utf-8"))
    p = int(data["method"]["prime"])
    checked = 0
    for rec in data["records"]:
        s, t, d, target = (int(rec[k]) for k in ("s", "t", "dimension", "target_rank"))
        cert = rec["maximal_minor_certificate"]
        if cert is None:
            raise AssertionError(f"missing certificate for {(s,t)}")
        points, matrix = make_matrix(s, t, d, int(cert["trial"]))
        affine = np.column_stack((np.ones(points.shape[0], dtype=np.int64), points))
        if rank_mod(affine, p) != d + 1:
            raise AssertionError(f"affine-span failure for {(s,t)}")
        rows = [int(x) for x in cert["row_indices"]]
        cols = [int(x) for x in cert["column_indices"]]
        if len(rows) != target or len(cols) != target:
            raise AssertionError(f"wrong minor size for {(s,t)}")
        residue = det_mod(matrix[np.ix_(rows, cols)], p)
        if residue == 0 or residue != int(cert["determinant_mod_p"]):
            raise AssertionError(f"bad determinant for {(s,t)}: {residue}")
        checked += 1
    print(f"verified {checked} affine-span and nonzero-maximal-minor certificates modulo {p}")


if __name__ == "__main__":
    main()
