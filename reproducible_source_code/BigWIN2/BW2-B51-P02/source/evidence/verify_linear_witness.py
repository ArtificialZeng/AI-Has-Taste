#!/usr/bin/env python3
"""Independent exact replay of the fixed C3 square C4 connectivity code.

This verifier does not import the search program or trust its flow variables.
It reconstructs the graph from coordinates, checks the serialized certificate,
constructs all 16 words from the four 24-bit generators, and runs a fresh BFS
on each of the 120 pairwise symmetric differences.
"""

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path


def make_graph():
    vertices = [(i, j) for i in range(3) for j in range(4)]
    index = {v: k for k, v in enumerate(vertices)}
    edges = []
    for i in range(3):
        for j in range(4):
            edges.append((index[i, j], index[(i + 1) % 3, j]))
    for i in range(3):
        for j in range(4):
            edges.append((index[i, j], index[i, (j + 1) % 4]))
    assert len(edges) == 24
    assert len({tuple(sorted(edge)) for edge in edges}) == 24
    return vertices, edges


def reached_vertices(mask, edges):
    adjacency = [[] for _ in range(12)]
    for e, (u, v) in enumerate(edges):
        if (mask >> e) & 1:
            adjacency[u].append(v)
            adjacency[v].append(u)
    reached = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in reached:
                reached.add(v)
                stack.append(v)
    return reached


def xor_rank(vectors):
    pivots = {}
    for value in vectors:
        x = value
        while x:
            b = x.bit_length() - 1
            if b not in pivots:
                pivots[b] = x
                break
            x ^= pivots[b]
    return len(pivots)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", default="evidence/linear_witness.json")
    parser.add_argument("--trees", default="evidence/spanning_tree_certificate.json")
    args = parser.parse_args()
    path = Path(args.certificate)
    raw = path.read_bytes()
    cert = json.loads(raw)

    vertices, edges = make_graph()
    assert cert["graph"] == "C3 square C4"
    assert cert["vertices"] == [list(v) for v in vertices]
    assert cert["edges"] == [list(e) for e in edges]

    labels = [int(x, 16) for x in cert["edge_labels_hex"]]
    generators = [int(x, 16) for x in cert["generators_24bit_hex"]]
    assert len(labels) == 24 and all(0 <= x < 16 for x in labels)
    assert len(generators) == 4 and all(0 <= x < (1 << 24) for x in generators)
    reconstructed = [sum(((labels[e] >> b) & 1) << e for e in range(24)) for b in range(4)]
    assert reconstructed == generators

    incident = [[] for _ in range(12)]
    for e, (u, v) in enumerate(edges):
        incident[u].append(e)
        incident[v].append(e)
    local_ranks = [xor_rank([labels[e] for e in incident[v]]) for v in range(12)]
    assert local_ranks == [4] * 12

    words = []
    for coefficients in range(16):
        word = 0
        for b in range(4):
            if (coefficients >> b) & 1:
                word ^= generators[b]
        words.append(word)
    assert len(set(words)) == 16

    pair_count = 0
    difference_counts = {a: 0 for a in range(1, 16)}
    for i, j in combinations(range(16), 2):
        difference = words[i] ^ words[j]
        assert difference == words[i ^ j]
        reached = reached_vertices(difference, edges)
        assert reached == set(range(12)), (i, j, sorted(reached))
        pair_count += 1
        difference_counts[i ^ j] += 1
    assert pair_count == 120
    assert set(difference_counts.values()) == {8}

    nonzero_weights = [words[a].bit_count() for a in range(1, 16)]

    tree_cert = json.loads(Path(args.trees).read_text())
    entries = tree_cert["entries"]
    assert [int(entry["a_hex"], 16) for entry in entries] == list(range(1, 16))
    for entry in entries:
        a = int(entry["a_hex"], 16)
        mask = int(entry["mask_hex"], 16)
        tree_edges = entry["tree_edges"]
        assert mask == words[a]
        assert len(tree_edges) == len(set(tree_edges)) == 11
        assert all(0 <= e < 24 and ((mask >> e) & 1) for e in tree_edges)
        tree_mask = sum(1 << e for e in tree_edges)
        assert reached_vertices(tree_mask, edges) == set(range(12))
    print("VERIFIED")
    print("certificate_sha256", hashlib.sha256(raw).hexdigest())
    print("vertices", len(vertices), "edges", len(edges))
    print("generators", " ".join(f"{x:06x}" for x in generators))
    print("distinct_words", len(set(words)))
    print("local_basis_ranks", " ".join(map(str, local_ranks)))
    print("nonzero_word_weights", " ".join(map(str, nonzero_weights)))
    print("connected_nonzero_words", 15)
    print("connected_pairwise_differences", pair_count)
    print("validated_spanning_tree_certificates", len(entries))
    print("multiplicity_per_nonzero_difference", " ".join(str(difference_counts[a]) for a in range(1, 16)))


if __name__ == "__main__":
    main()
