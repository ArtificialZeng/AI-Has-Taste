#!/usr/bin/env python3
"""Independent exact verifier for the order-13 LC-orbit certificate.

This implementation does not call the C++ generator.  It independently
decodes graph6 (also cross-checking NetworkX), verifies every discovery-tree
edge, verifies closure under all 13 local complementations, and tests every
one of the C(13,5)=1287 five-subsets of every serialized orbit member.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys

import networkx as nx
import numpy as np

N = 13
E = N * (N - 1) // 2


def edge_tables() -> tuple[list[tuple[int, int]], list[list[tuple[int, int]]]]:
    endpoints: list[tuple[int, int]] = []
    incident: list[list[tuple[int, int]]] = [[] for _ in range(N)]
    for j in range(1, N):
        for i in range(j):
            p = len(endpoints)
            endpoints.append((i, j))
            incident[i].append((1 << p, 1 << j))
            incident[j].append((1 << p, 1 << i))
    assert len(endpoints) == E
    return endpoints, incident


ENDPOINTS, INCIDENT = edge_tables()


def decode_graph6(text: str) -> int:
    raw = text.encode("ascii")
    if len(raw) != 14 or raw[0] != 63 + N:
        raise ValueError("expected the short graph6 encoding of a 13-vertex graph")
    state = 0
    for p in range(E):
        value = raw[1 + p // 6] - 63
        if not 0 <= value <= 63:
            raise ValueError("invalid graph6 byte")
        if value & (1 << (5 - p % 6)):
            state |= 1 << p
    return state


def rows_from_state(state: int) -> list[int]:
    rows = [0] * N
    x = state
    while x:
        bit = x & -x
        p = bit.bit_length() - 1
        i, j = ENDPOINTS[p]
        rows[i] |= 1 << j
        rows[j] |= 1 << i
        x ^= bit
    return rows


def clique_masks() -> list[int]:
    result = [0] * (1 << N)
    for subset in range(1 << N):
        mask = 0
        for p, (i, j) in enumerate(ENDPOINTS):
            if subset & (1 << i) and subset & (1 << j):
                mask |= 1 << p
        result[subset] = mask
    return result


CLIQUE = clique_masks()


def local_complement_from_incident(state: int, vertex: int) -> int:
    neighbors = 0
    for edge_bit, neighbor_bit in INCIDENT[vertex]:
        if state & edge_bit:
            neighbors |= neighbor_bit
    return state ^ CLIQUE[neighbors]


def edge_mask(vertices: tuple[int, ...]) -> int:
    chosen = set(vertices)
    mask = 0
    for p, (i, j) in enumerate(ENDPOINTS):
        if i in chosen and j in chosen:
            mask |= 1 << p
    return mask


def split_masks(masks: list[int]) -> tuple[np.ndarray, np.ndarray]:
    low = np.array([x & ((1 << 64) - 1) for x in masks], dtype=np.uint64)
    high = np.array([x >> 64 for x in masks], dtype=np.uint16)
    return low, high


def verify(candidate: str, orbit_path: Path) -> dict[str, object]:
    blob = orbit_path.read_bytes()
    if blob[:8] != b"LC13ORB2":
        raise AssertionError("bad orbit-certificate magic")
    count = int.from_bytes(blob[8:16], "little")
    entry_dtype = np.dtype(
        [("lo", "<u8"), ("hi", "<u2"), ("parent", "<u4"), ("move", "u1")]
    )
    expected_size = 16 + count * entry_dtype.itemsize
    if len(blob) != expected_size:
        raise AssertionError(("certificate byte length", len(blob), expected_size))
    nodes = np.frombuffer(blob, dtype=entry_dtype, count=count, offset=16)
    lows = np.ascontiguousarray(nodes["lo"])
    highs = np.ascontiguousarray(nodes["hi"])
    states = [int(lo) | (int(hi) << 64) for lo, hi in zip(lows, highs, strict=True)]
    state_set = set(states)
    if len(state_set) != count:
        raise AssertionError("duplicate full adjacency bitstring in certificate")
    if np.any(highs >= (1 << (E - 64))):
        raise AssertionError("bits above the 78-edge domain are set")

    root = decode_graph6(candidate)
    if states[0] != root:
        raise AssertionError("certificate root differs from graph6 input")

    # Independent graph6 decoder cross-check.
    nx_graph = nx.from_graph6_bytes(candidate.encode("ascii"))
    if nx_graph.number_of_nodes() != N or nx_graph.number_of_edges() != root.bit_count():
        raise AssertionError("NetworkX graph6 decode disagrees")
    nx_edges = {tuple(sorted(e)) for e in nx_graph.edges()}
    own_edges = {ENDPOINTS[p] for p in range(E) if root & (1 << p)}
    if nx_edges != own_edges:
        raise AssertionError("NetworkX edge set disagrees with independent decoder")

    residues = {1, 3, 4, 9, 10, 12}
    paley_edges = {
        (i, j)
        for i in range(N)
        for j in range(i + 1, N)
        if (j - i) % N in residues
    }
    if own_edges != paley_edges:
        raise AssertionError("candidate is not the Paley graph on Z/13Z")

    # Every nonroot record has a certified earlier parent and LC move.  This
    # proves every listed state is reachable from the graph6 root.
    if int(nodes["parent"][0]) != (1 << 32) - 1 or int(nodes["move"][0]) != 255:
        raise AssertionError("bad root sentinel")
    for i in range(1, count):
        parent = int(nodes["parent"][i])
        move = int(nodes["move"][i])
        if parent >= i or move >= N:
            raise AssertionError(("invalid discovery edge", i, parent, move))
        if local_complement_from_incident(states[parent], move) != states[i]:
            raise AssertionError(("false discovery edge", i, parent, move))
        if i % 100_000 == 0:
            print(f"tree_edges_verified={i}", file=sys.stderr, flush=True)

    # Full closure under all 13 generators.  Together with reachability and
    # uniqueness, this proves that the list is exactly the labeled LC orbit.
    closure_moves = 0
    for i, state in enumerate(states):
        rows = rows_from_state(state)
        for vertex in range(N):
            child = state ^ CLIQUE[rows[vertex]]
            if child not in state_set:
                raise AssertionError(("orbit not closed", i, vertex))
            closure_moves += 1
        if (i + 1) % 100_000 == 0:
            print(f"orbit_states_closed={i + 1}", file=sys.stderr, flush=True)

    # Separate exact alpha check: vectorized integer operations exhaust every
    # 5-subset for every orbit member.  No graph-search logic is reused.
    five_sets = list(itertools.combinations(range(N), 5))
    five_masks = [edge_mask(s) for s in five_sets]
    mask_lo, mask_hi = split_masks(five_masks)
    chunk = 2048
    for start in range(0, count, chunk):
        stop = min(start + chunk, count)
        lo_block = lows[start:stop, None]
        hi_block = highs[start:stop, None]
        has_edge = (np.bitwise_and(lo_block, mask_lo[None, :]) != 0)
        has_edge |= np.bitwise_and(hi_block, mask_hi[None, :]) != 0
        bad = np.argwhere(~has_edge)
        if bad.size:
            row, column = map(int, bad[0])
            raise AssertionError(
                ("independent five-set", start + row, five_sets[column])
            )
        if stop % 100_000 < chunk:
            print(f"alpha_states_verified={stop}", file=sys.stderr, flush=True)

    # An exact independent four-set establishes beta=4, not merely beta<=4.
    four_witness = None
    for vertices in itertools.combinations(range(N), 4):
        mask = edge_mask(vertices)
        lo = np.uint64(mask & ((1 << 64) - 1))
        hi = np.uint16(mask >> 64)
        indices = np.flatnonzero(
            (np.bitwise_and(lows, lo) == 0) & (np.bitwise_and(highs, hi) == 0)
        )
        if indices.size:
            four_witness = {"orbit_index": int(indices[0]), "vertices": list(vertices)}
            break
    if four_witness is None:
        raise AssertionError("no independent four-set found")

    return {
        "candidate_graph6": candidate,
        "candidate_description": "Paley graph P(13) on Z/13Z",
        "vertices": N,
        "edges": len(own_edges),
        "graph6_networkx_crosscheck": True,
        "orbit_certificate": orbit_path.as_posix(),
        "orbit_certificate_sha256": hashlib.sha256(blob).hexdigest(),
        "orbit_entry_format": "LC13ORB2: root-first BFS records (uint64 lo, uint16 hi, uint32 parent, uint8 move), little-endian",
        "orbit_size": count,
        "full_adjacency_keys_unique": True,
        "reachable_tree_edges_verified": count - 1,
        "closure_moves_verified": closure_moves,
        "five_subsets_per_state": len(five_sets),
        "state_subset_pairs_verified": count * len(five_sets),
        "independent_five_found": False,
        "independent_four_witness": four_witness,
        "beta": 4,
        "conclusion": "Every member of the complete labeled LC orbit has independence number at most four.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate")
    parser.add_argument("orbit", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    report = verify(args.candidate, args.orbit)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
