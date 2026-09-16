#!/usr/bin/env python3
"""Exact, checkpointed census for independence-polynomial stability of trees.

The free-tree stream is the WROM/Beyer--Hedetniemi level-sequence algorithm
used by NetworkX 3.4.2.  All polynomial and Routh operations are integer
operations.  Run from the project root, for example

    python3 evidence/census21.py --order 21 --output evidence/census21

The binary ``canonical.u64`` file contains one collision-free AHU balanced-
parenthesis encoding per generated free tree.  ``chunks.jsonl`` commits each
completed chunk, and ``state.json`` permits resumption at chunk boundaries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import struct
import time
from pathlib import Path


def next_rooted_tree(predecessor: list[int], p: int | None = None):
    """One Beyer--Hedetniemi iteration (returns a fresh list or None)."""
    if p is None:
        p = len(predecessor) - 1
        while predecessor[p] == 1:
            p -= 1
    if p == 0:
        return None
    q = p - 1
    while predecessor[q] != predecessor[p] - 1:
        q -= 1
    result = list(predecessor)
    for i in range(p, len(result)):
        result[i] = result[i - p + q]
    return result


def split_tree(layout: list[int]):
    one_found = False
    m = None
    for i, value in enumerate(layout):
        if value == 1:
            if one_found:
                m = i
                break
            one_found = True
    if m is None:
        m = len(layout)
    return [x - 1 for x in layout[1:m]], [0] + layout[m:]


def next_free_tree(candidate: list[int]):
    """WROM jump from a rooted candidate to the next valid free tree."""
    left, rest = split_tree(candidate)
    lh, rh = max(left), max(rest)
    valid = rh >= lh
    if valid and rh == lh:
        if len(left) > len(rest) or (len(left) == len(rest) and left > rest):
            valid = False
    if valid:
        return candidate
    p = len(left)
    result = next_rooted_tree(candidate, p)
    if candidate[p] > 2:
        new_left, _ = split_tree(result)
        suffix = list(range(1, max(new_left) + 2))
        result[-len(suffix) :] = suffix
    return result


def initial_layout(order: int):
    return list(range(order // 2 + 1)) + list(range(1, (order + 1) // 2))


def adjacency_and_parent(layout: list[int]):
    n = len(layout)
    adjacency = [[] for _ in range(n)]
    parent = [-1] * n
    stack: list[int] = []
    for i, level in enumerate(layout):
        while stack and layout[stack[-1]] >= level:
            stack.pop()
        if stack:
            p = stack[-1]
            parent[i] = p
            adjacency[i].append(p)
            adjacency[p].append(i)
        stack.append(i)
    return adjacency, parent


def convolution(a: list[int], b: list[int]):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a: list[int], b: list[int]):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def independence_polynomial(layout: list[int], parent: list[int]):
    """Return ascending exact coefficients using include/exclude tree DP."""
    n = len(layout)
    excluded: list[list[int] | None] = [None] * n
    included: list[list[int] | None] = [None] * n
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    for v in range(n - 1, -1, -1):
        a = [1]
        b = [0, 1]
        for child in children[v]:
            a = convolution(a, poly_add(excluded[child], included[child]))
            b = convolution(b, excluded[child])
        excluded[v], included[v] = a, b
    return poly_add(excluded[0], included[0])


def centers(adjacency: list[list[int]]):
    n = len(adjacency)
    if n <= 2:
        return list(range(n))
    degree = [len(x) for x in adjacency]
    leaves = [i for i, d in enumerate(degree) if d <= 1]
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for neighbor in adjacency[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        leaves = new_leaves
    return leaves


def rooted_bp(adjacency: list[list[int]], vertex: int, parent: int):
    """Return (subtree order, canonical balanced-parenthesis integer)."""
    child_codes = [rooted_bp(adjacency, w, vertex) for w in adjacency[vertex] if w != parent]
    child_codes.sort()
    size = 1
    bits = 1
    for child_size, child_bits in child_codes:
        bits = (bits << (2 * child_size)) | child_bits
        size += child_size
    return size, bits << 1


def canonical_code(adjacency: list[list[int]]):
    """Collision-free unrooted AHU code, fitting in 2(n+1) bits here."""
    cs = centers(adjacency)
    if len(cs) == 1:
        return rooted_bp(adjacency, cs[0], -1)[1]
    # A virtual root makes the bicentered encoding invariant under swapping.
    pieces = [rooted_bp(adjacency, cs[0], cs[1]), rooted_bp(adjacency, cs[1], cs[0])]
    pieces.sort()
    size, bits = 1, 1
    for child_size, child_bits in pieces:
        bits = (bits << (2 * child_size)) | child_bits
        size += child_size
    assert size == len(adjacency) + 1
    return bits << 1


def routh_first_column(coefficients: list[int]):
    """Exact Routh first column up to positive row scaling.

    Input coefficients are ascending.  The return status is ``regular`` only
    if no pivot or all-zero row occurs.  For a regular table, sign variations
    equal the number of open-right-half-plane roots.
    """
    desc = list(reversed(coefficients))
    width = (len(desc) + 1) // 2
    upper = desc[0::2] + [0] * (width - len(desc[0::2]))
    lower = desc[1::2] + [0] * (width - len(desc[1::2]))
    column = [upper[0]]
    if len(desc) == 1:
        return "regular", column
    column.append(lower[0])
    for _ in range(2, len(desc)):
        pivot = lower[0]
        if pivot == 0:
            return "zero-pivot", column
        sign = 1 if pivot > 0 else -1
        row = [sign * (pivot * upper[j + 1] - upper[0] * lower[j + 1]) for j in range(width - 1)] + [0]
        if not any(row):
            return "zero-row", column
        divisor = 0
        for value in row:
            divisor = math.gcd(divisor, abs(value))
        if divisor > 1:
            row = [value // divisor for value in row]
        upper, lower = lower, row
        column.append(lower[0])
    return "regular", column


def signs(values: list[int]):
    return [1 if x > 0 else -1 if x < 0 else 0 for x in values]


def sign_variations(values: list[int]):
    s = [x for x in signs(values) if x]
    return sum(a != b for a, b in zip(s, s[1:]))


def encode_record(code: int, coefficients: list[int], status: str, column: list[int]):
    # Unambiguous audit digest encoding, independent of Python repr details.
    fields = [format(code, "x"), ",".join(map(str, coefficients)), status, ",".join(map(str, signs(column)))]
    return ("|".join(fields) + "\n").encode("ascii")


def atomic_json(path: Path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=21)
    parser.add_argument("--output", type=Path, default=Path("evidence/census21"))
    parser.add_argument("--chunk-size", type=int, default=50_000)
    parser.add_argument("--limit", type=int, default=0, help="stop cleanly after this many total trees (benchmarking)")
    args = parser.parse_args()
    if not 2 <= args.order <= 31:  # uint64 BP encoding includes a virtual root
        raise SystemExit("this implementation supports orders 2 through 31")
    args.output.mkdir(parents=True, exist_ok=True)
    state_path = args.output / "state.json"
    chunks_path = args.output / "chunks.jsonl"
    codes_path = args.output / "canonical.u64"
    suspect_path = args.output / "suspects.jsonl"

    if state_path.exists():
        state = json.loads(state_path.read_text())
        if state["order"] != args.order or state["chunk_size"] != args.chunk_size:
            raise SystemExit("existing state has incompatible order/chunk size")
        candidate = state["next_layout"]
        total = state["count"]
        chunk_index = state["chunks"]
        if codes_path.stat().st_size != total * 8:
            raise SystemExit("canonical.u64 size disagrees with committed state")
    else:
        candidate = initial_layout(args.order)
        total = 0
        chunk_index = 0
        atomic_json(state_path, {"order": args.order, "chunk_size": args.chunk_size, "count": 0, "chunks": 0, "next_layout": candidate, "complete": False})

    started = time.monotonic()
    while candidate is not None and (not args.limit or total < args.limit):
        codes: list[int] = []
        digest = hashlib.sha256()
        stable = regular_unstable = singular = 0
        chunk_suspects = []
        first_index = total + 1
        while candidate is not None and len(codes) < args.chunk_size and (not args.limit or total + len(codes) < args.limit):
            layout = next_free_tree(candidate)
            if layout is None:
                candidate = None
                break
            adjacency, parent = adjacency_and_parent(layout)
            code = canonical_code(adjacency)
            coefficients = independence_polynomial(layout, parent)
            status, column = routh_first_column(coefficients)
            variation_count = sign_variations(column) if status == "regular" else None
            if status == "regular" and variation_count == 0 and all(x > 0 for x in column):
                stable += 1
            else:
                if status == "regular":
                    regular_unstable += 1
                else:
                    singular += 1
                chunk_suspects.append({
                    "index": total + len(codes) + 1,
                    "layout": layout,
                    "canonical_hex": format(code, "x"),
                    "coefficients_ascending": coefficients,
                    "routh_status": status,
                    "routh_first_column": column,
                    "sign_variations": variation_count,
                })
            codes.append(code)
            digest.update(encode_record(code, coefficients, status, column))
            candidate = next_rooted_tree(layout)

        if not codes:
            break
        with codes_path.open("ab") as handle:
            handle.write(struct.pack("<" + "Q" * len(codes), *codes))
            handle.flush()
            os.fsync(handle.fileno())
        if chunk_suspects:
            with suspect_path.open("a") as handle:
                for item in chunk_suspects:
                    handle.write(json.dumps(item, separators=(",", ":")) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
        total += len(codes)
        elapsed = time.monotonic() - started
        chunk_record = {
            "chunk": chunk_index,
            "first_index": first_index,
            "last_index": total,
            "count": len(codes),
            "record_sha256": digest.hexdigest(),
            "strict_stable": stable,
            "regular_unstable": regular_unstable,
            "singular": singular,
            "last_layout": layout,
            "elapsed_seconds_this_run": elapsed,
        }
        with chunks_path.open("a") as handle:
            handle.write(json.dumps(chunk_record, separators=(",", ":")) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        chunk_index += 1
        atomic_json(state_path, {
            "order": args.order,
            "chunk_size": args.chunk_size,
            "count": total,
            "chunks": chunk_index,
            "next_layout": candidate,
            "complete": candidate is None,
            "elapsed_seconds_latest_run": elapsed,
        })
        print(json.dumps(chunk_record), flush=True)

    if candidate is None:
        atomic_json(state_path, {
            "order": args.order,
            "chunk_size": args.chunk_size,
            "count": total,
            "chunks": chunk_index,
            "next_layout": None,
            "complete": True,
            "elapsed_seconds_latest_run": time.monotonic() - started,
        })


if __name__ == "__main__":
    main()
