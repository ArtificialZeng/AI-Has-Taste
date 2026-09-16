#!/usr/bin/env python3
"""Exact corroboration of proof.md; no finite test is a universal proof.

Run from PROJECT_DIR: python3 evidence/research/verify.py
Only the sibling verify.json is written. No old evidence is overwritten.
The full-board evaluator uses direct Young-diagram cells and bit masks.
The transfer evaluator uses sets. The partition evaluator constructs options.
All three are implemented here without importing the triage computations.
"""
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import platform
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
JOB = "primary-20260913-king-odd-staircase-research-fd17b876b830"
MOVES = ((1, 0), (0, 1), (1, 1))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mex(values):
    z = 0
    while z in values:
        z += 1
    return z


def parameters(r, k):
    assert r >= 1 and r % 2 == 1 and k >= 1
    p = r + 2
    return p - (1 + (k - 1) % p), ((k - 1) // p) % 2


def grid(L, h, i, j):
    m, n = min(i, j), max(i, j)
    if m == n == L:
        return 2
    x, y, a, b = L % 2, 1 - L % 2, 3 - h, 2 + h
    if n < L:
        pattern = ((x, a), (b, y))
    elif m <= L:
        pattern = ((b, y), (x, a))
    else:
        pattern = ((y, b), (a, x))
    return pattern[m % 2][n % 2]


def boundary_formula(r, k):
    # Direct transcription of the triage-frozen W, not grid(0,j).
    t = 1 + (k - 1) % (r + 2)
    h = ((k - 1) // (r + 2)) % 2
    out = []
    for j in range(r):
        if j == 0 and t == r + 2:
            out.append(2)
        elif j < r + 2 - t:
            out.append((t + 1) % 2 if j % 2 == 0 else 3 - h)
        else:
            out.append(2 + h if j % 2 == 0 else t % 2)
    return tuple(out)


def shape(r, k):
    return tuple(width for width in range(r * k, 0, -r) for _ in range(r))


def direct_board(parts):
    result = [[0] * v for v in parts]
    for i in reversed(range(len(parts))):
        for j in reversed(range(parts[i])):
            mask = 0
            for di, dj in MOVES:
                u, v = i + di, j + dj
                if u < len(parts) and v < parts[u]:
                    mask |= 1 << result[u][v]
            result[i][j] = next(z for z in range(4) if (mask & (1 << z)) == 0)
    return result


@lru_cache(None)
def partition_value(parts):
    assert parts
    values = set()
    for di, dj in MOVES:
        dest = tuple(v - dj for v in parts[di:] if v > dj)
        if dest:
            values.add(partition_value(dest))
    return mex(values)


def transfer(r, previous=None, corner=None):
    table = [[None] * (r + 1) for _ in range(r + 1)]
    if previous is not None:
        for j in range(r):
            table[r][j] = table[j][r] = previous[j]
    table[r][r] = corner
    for i in reversed(range(r)):
        for j in reversed(range(r)):
            options = {table[i + di][j + dj] for di, dj in MOVES}
            options.discard(None)
            table[i][j] = mex(options)
    return table


def main():
    started = time.monotonic()
    proof_hash = digest(HERE / "proof.md")
    source_hash = digest(ROOT / "source.md")
    assert source_hash == "e4dc12773dcaea452c4710f74f8cea0715f792af5af8f043d8d73d5b30913ae8"
    counts = {"local_identity_cells": 0, "seam_table_rows": 0,
              "transfer_interior_cells": 0, "boundary_words": 0,
              "direct_boards": 0, "direct_interior_cells": 0,
              "recursive_subpartitions": 0, "huge_k_one_step_cases": 0}

    # Finite representatives checking every row of the written exceptional table.
    seam_records = []
    for h in (0, 1):
        a, b = 3 - h, 2 + h
        for L in (4, 5):
            if L % 2 == 0:
                specs = [(0,L-1,a,(1,b,0)), (1,L-1,1,(a,0,b)),
                         (L-1,L,0,(2,a,1)), (L,L+1,1,(0,b,a)),
                         (L,L+2,b,(a,1,0))]
            else:
                specs = [(0,L-1,1,(b,0,a)), (1,L-1,b,(1,a,0)),
                         (L-1,L,0,(2,b,1)), (L,L+1,1,(0,a,b)),
                         (L,L+2,a,(b,1,0))]
            specs += [(L-1,L-1,1,(0,0,2)), (L,L,2,(1,1,0))]
            for i,j,value,options in specs:
                actual = tuple(grid(L,h,i+di,j+dj) for di,dj in MOVES)
                assert grid(L,h,i,j) == value and actual == options
                assert mex(set(options)) == value
                counts["seam_table_rows"] += 1
                seam_records.append({"L_parity":L%2, "h":h,
                                     "relative_cell":[i-L,j-L],
                                     "value":value, "options":list(options)})

    for L in range(13):
        for h in (0, 1):
            for i in range(18):
                for j in range(18):
                    options = {grid(L,h,i+di,j+dj) for di,dj in MOVES}
                    assert grid(L,h,i,j) == mex(options), (L,h,i,j,options)
                    counts["local_identity_cells"] += 1

    rows = []
    block_sizes = list(range(1,32,2)) + [33,47,65,79,101]
    for r in block_sizes:
        end = 2*(r+2)+3
        roots = []
        previous = None
        for k in range(1,end+1):
            corner = None if k <= 2 else roots[-2]
            table = transfer(r,previous,corner)
            current = tuple(table[0][:r])
            assert current == boundary_formula(r,k), (r,k,"boundary")
            counts["boundary_words"] += 1
            if k >= 2:
                L,h = parameters(r,k)
                for i in range(r):
                    for j in range(r):
                        assert table[i][j] == grid(L,h,i,j), (r,k,i,j)
                        counts["transfer_interior_cells"] += 1
            if r <= 11:
                parts = shape(r,k)
                board = direct_board(parts)
                assert tuple(board[0][:r]) == current
                counts["direct_boards"] += 1
                for i in range(r):
                    for j in range(r):
                        assert board[i][j] == table[i][j], (r,k,i,j,"direct")
                        counts["direct_interior_cells"] += 1
                        if r <= 5 and k <= 6:
                            subparts = tuple(v-j for v in parts[i:] if v > j)
                            assert partition_value(subparts) == table[i][j]
                            counts["recursive_subpartitions"] += 1
            roots.append(current[0])
            previous = current
        rows.append({"r":r,"k_range":[1,end],"mismatches":[],
                     "full_board_checked":r<=11})

    # Isolated one-step tests from the assumed W at huge phase indices.
    # These are NOT direct evaluations of enormously large full boards.
    huge_cases = []
    for r in (1,3,65):
        p = r+2
        for ell in (10**50,10**50+1):
            for t in (1,2,p-1,p):
                k = ell*p+t
                table = transfer(r,boundary_formula(r,k-1),boundary_formula(r,k-2)[0])
                L,h = parameters(r,k)
                for i in range(r):
                    for j in range(r):
                        assert table[i][j] == grid(L,h,i,j)
                counts["huge_k_one_step_cases"] += 1
                huge_cases.append({"r":r,"k":str(k),"t":t,"h":h})

    assert digest(HERE / "proof.md") == proof_hash
    result = {"job_id":JOB,"arithmetic":"exact integers and finite mex; no random tests",
              "python":platform.python_version(),"counts":counts,
              "coverage":rows,"seam_table":seam_records,
              "huge_k_one_step_cases":huge_cases,
              "proof_sha256_fixed_before_tests":proof_hash,
              "script_sha256":digest(Path(__file__).resolve()),
              "source_sha256":source_hash,"source_unchanged":True,
              "elapsed_seconds":time.monotonic()-started,
              "qualification":"Finite corroboration by this proposer job, not fresh referee review. Universal proof is the exhaustive local case argument and induction in proof.md."}
    tmp = HERE / ".verify.json.tmp"
    tmp.write_text(json.dumps(result,indent=2)+"\n")
    tmp.replace(HERE / "verify.json")
    print(json.dumps({"counts":counts,"elapsed_seconds":result["elapsed_seconds"],
                      "mismatches":[],"proof_sha256":proof_hash}))


if __name__ == "__main__":
    main()
