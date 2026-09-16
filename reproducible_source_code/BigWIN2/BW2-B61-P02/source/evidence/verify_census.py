#!/usr/bin/env python3
"""Independent full verifier for census_exact.tsv.

Differences from the enumerator are intentional:

* graph6 rows are decoded with NetworkX and checked against the stored masks;
* independence numbers are obtained by direct enumeration of independent
  submasks, not by the enumerator's vertex-deletion recurrence;
* Hall inequalities are checked for every nonempty vertex subset, not only
  connected induced subsets;
* colorability is tested against an independently generated list of assignment
  conflict masks for each H, not by marking downward closures.

The verifier recomputes every status bit for every one of the 209 canonical G
and every labelled H, then checks all row and aggregate SHA-256 bindings.
"""

import csv
import hashlib
import itertools
import json
import sys
from pathlib import Path

import networkx as nx
import numpy as np
from numba import njit, prange


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def edge_pairs(n):
    return [(u, v) for v in range(1, n) for u in range(v)]


def unpack(hex_text, number):
    packed = np.frombuffer(bytes.fromhex(hex_text), dtype=np.uint8)
    return np.unpackbits(packed, bitorder="little")[:number].astype(np.uint8)


def packed(row):
    return np.packbits(row, bitorder="little").tobytes()


def status_digest(n, graph6, gmask, num_h, hall, colorable):
    payload = (
        f"{n}\0{graph6}\0{gmask}\0{num_h}\0".encode("ascii")
        + packed(hall) + b"\0" + packed(colorable)
    )
    return hashlib.sha256(payload).hexdigest()


@njit(cache=True)
def bit_count(x):
    total = 0
    while x:
        x &= x - 1
        total += 1
    return total


@njit(cache=True)
def graph_adjacency(n, edge_mask):
    adj = np.zeros(n, dtype=np.int64)
    k = 0
    for v in range(1, n):
        for u in range(v):
            if (edge_mask >> k) & 1:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
            k += 1
    return adj


@njit(cache=True)
def lexicographic_bit_rank(mask, number_of_edges):
    """Rank the graph6 adjacency-bit word (first bit most significant)."""
    rank = 0
    for k in range(number_of_edges):
        rank = (rank << 1) | ((mask >> k) & 1)
    return rank


@njit(cache=True, parallel=True)
def canonical_masks_of_all_labelled_graphs(n, permutation_edge_maps):
    m = n * (n - 1) // 2
    hn = 1 << m
    answer = np.zeros(hn, dtype=np.int64)
    for original in prange(hn):
        best_rank = 1 << m
        best_mask = 0
        for p in range(permutation_edge_maps.shape[0]):
            relabelled = 0
            for new_k in range(m):
                old_k = permutation_edge_maps[p, new_k]
                if (original >> old_k) & 1:
                    relabelled |= 1 << new_k
            rank = lexicographic_bit_rank(relabelled, m)
            if rank < best_rank:
                best_rank = rank
                best_mask = relabelled
        answer[original] = best_mask
    return answer


@njit(cache=True)
def brute_alpha_tables(n):
    hn = 1 << (n * (n - 1) // 2)
    vn = 1 << n
    table = np.zeros((hn, vn), dtype=np.uint8)
    for h in range(hn):
        independent = np.ones(vn, dtype=np.uint8)
        independent[0] = 1
        for vertices in range(1, vn):
            k = 0
            ok = 1
            for v in range(1, n):
                for u in range(v):
                    if ((h >> k) & 1) and ((vertices >> u) & 1) and ((vertices >> v) & 1):
                        ok = 0
                    k += 1
            independent[vertices] = ok
        for subset in range(vn):
            best = 0
            candidate = subset
            while True:
                if independent[candidate]:
                    size = bit_count(candidate)
                    if size > best:
                        best = size
                if candidate == 0:
                    break
                candidate = (candidate - 1) & subset
            table[h, subset] = best
    return table


@njit(cache=True)
def int_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


@njit(cache=True)
def conflict_masks(n, lists, hn):
    seen = np.zeros(hn, dtype=np.uint8)
    masks = np.zeros(hn, dtype=np.int64)
    count = 0
    if n == 0:
        masks[0] = 0
        return masks, 1
    colors = np.zeros(n, dtype=np.int64)
    for original in range(int_power(n, n)):
        code = original
        admissible = 1
        for v in range(n):
            colors[v] = code % n
            code //= n
            if ((lists[v] >> colors[v]) & 1) == 0:
                admissible = 0
                break
        if not admissible:
            continue
        conflict = 0
        k = 0
        for v in range(1, n):
            for u in range(v):
                if colors[u] == colors[v]:
                    conflict |= 1 << k
                k += 1
        if seen[conflict] == 0:
            seen[conflict] = 1
            masks[count] = conflict
            count += 1
    return masks, count


@njit(cache=True, parallel=True)
def independently_recompute_layer(n, gmasks, alpha):
    count = len(gmasks)
    hn = alpha.shape[0]
    vn = alpha.shape[1]
    hall = np.zeros((count, hn), dtype=np.uint8)
    colorable = np.zeros((count, hn), dtype=np.uint8)
    for i in prange(count):
        lists = graph_adjacency(n, gmasks[i])
        conflicts, conflict_count = conflict_masks(n, lists, hn)
        for h in range(hn):
            # Direct test against every distinct conflict mask generated by an
            # admissible assignment.
            for j in range(conflict_count):
                if (h & conflicts[j]) == 0:
                    colorable[i, h] = 1
                    break
            # Check all nonempty subsets, a strictly redundant version of Hall.
            good = 1
            for subset in range(1, vn):
                right = 0
                for c in range(n):
                    right += alpha[h, subset & lists[c]]
                if right < bit_count(subset):
                    good = 0
                    break
            hall[i, h] = good
    return hall, colorable


def permutation_edge_maps(n):
    pair_list = edge_pairs(n)
    index = {frozenset(edge): k for k, edge in enumerate(pair_list)}
    maps = []
    for order in itertools.permutations(range(n)):
        maps.append([index[frozenset((order[u], order[v]))] for u, v in pair_list])
    return np.array(maps, dtype=np.int64)


def validate_representatives(reps):
    keys = [(int(r["n"]), r["graph6"]) for r in reps]
    if keys != sorted(keys) or len(keys) != len(set(keys)):
        raise AssertionError("representatives are not unique and sorted")
    for row in reps:
        n = int(row["n"])
        expected_edges = {
            edge for k, edge in enumerate(edge_pairs(n))
            if (int(row["edge_mask"]) >> k) & 1
        }
        decoded = nx.from_graph6_bytes(row["graph6"].encode("ascii"))
        if len(decoded) != n or set(decoded.edges()) != expected_edges:
            raise AssertionError(f"graph6/mask mismatch: {row}")
    # Establish domain completeness without using the atlas or a tabulated
    # unlabeled-graph count: enumerate every labelled G, canonicalize it under
    # every vertex permutation, and compare the resulting orbit representatives.
    exhaustive_counts = []
    for n in range(7):
        canonical = canonical_masks_of_all_labelled_graphs(n, permutation_edge_maps(n))
        exhaustive = set(map(int, canonical))
        recorded = {int(r["edge_mask"]) for r in reps if int(r["n"]) == n}
        if exhaustive != recorded:
            raise AssertionError(f"incomplete canonical G domain at n={n}")
        exhaustive_counts.append(len(exhaustive))
    return exhaustive_counts


def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: verify_census.py census.tsv manifest.json representatives.tsv")
    census_path, manifest_path, reps_path = map(Path, sys.argv[1:])
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if sha256(census_path) != manifest["census_sha256"]:
        raise AssertionError("census file hash mismatch")
    if sha256(reps_path) != manifest["representatives_sha256"]:
        raise AssertionError("representatives file hash mismatch")
    with reps_path.open(newline="", encoding="ascii") as stream:
        reps = list(csv.DictReader(stream, delimiter="\t"))
    exhaustive_counts = validate_representatives(reps)
    if exhaustive_counts != [1, 1, 2, 4, 11, 34, 156]:
        raise AssertionError(f"unexpected derived orbit counts: {exhaustive_counts}")
    with census_path.open(newline="", encoding="ascii") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != len(reps):
        raise AssertionError("row-count mismatch")
    bindings = {(int(r["n"]), r["graph6"]): r for r in manifest["rows"]}
    recomputed_digests = []
    layer_results = []
    for n in range(7):
        layer = [r for r in census if int(r["n"]) == n]
        gmasks = np.array([int(r["g_edge_mask"]) for r in layer], dtype=np.int64)
        alpha = brute_alpha_tables(n)
        hall, colorable = independently_recompute_layer(n, gmasks, alpha)
        for i, row in enumerate(layer):
            num_h = int(row["num_H"])
            recorded_hall = unpack(row["hall_bits_hex"], num_h)
            recorded_colorable = unpack(row["colorable_bits_hex"], num_h)
            if not np.array_equal(hall[i], recorded_hall):
                differences = np.flatnonzero(hall[i] != recorded_hall)
                raise AssertionError(f"Hall mismatch {row['graph6']} H={int(differences[0])}")
            if not np.array_equal(colorable[i], recorded_colorable):
                differences = np.flatnonzero(colorable[i] != recorded_colorable)
                raise AssertionError(f"colorability mismatch {row['graph6']} H={int(differences[0])}")
            digest = status_digest(n, row["graph6"], int(row["g_edge_mask"]), num_h,
                                   hall[i], colorable[i])
            binding = bindings[(n, row["graph6"])]
            if digest != binding["status_sha256"]:
                raise AssertionError(f"row status hash mismatch {row['graph6']}")
            recomputed_digests.append(digest)
        layer_results.append({
            "n": n,
            "classes": len(layer),
            "labelled_H_per_class": int(layer[0]["num_H"]),
            "exact_status_arrays_match": True,
        })
        print(f"independently verified n={n}", file=sys.stderr, flush=True)
    aggregate = hashlib.sha256(b"".join(bytes.fromhex(d) for d in recomputed_digests)).hexdigest()
    if aggregate != manifest["aggregate_status_sha256"]:
        raise AssertionError("aggregate status hash mismatch")
    result = {
        "verifier": "direct-independent-submasks/all-U/conflict-list-v1",
        "all_209_canonical_classes_verified": True,
        "all_labelled_H_status_bits_match": True,
        "all_classes_hall_universal": all(int(r["bad_count"]) == 0 for r in census),
        "canonical_layer_counts_derived_by_full_labelled_G_orbit_enumeration": exhaustive_counts,
        "aggregate_status_sha256": aggregate,
        "census_sha256": manifest["census_sha256"],
        "layers": layer_results,
    }
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    print()


if __name__ == "__main__":
    main()
