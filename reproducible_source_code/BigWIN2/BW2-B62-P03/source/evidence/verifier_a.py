#!/usr/bin/env python3
"""Exact canonical-cycle-word verifier for the graph Gamma_n.

Uses only the Python standard library.  A vertex is the unique rotation of an
n-cycle word whose first entry is 1.  Generator i swaps labels i and i+1 and
then canonicalizes.  All-source BFS computes the ordered-pair distance data.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
from collections import Counter, deque
from pathlib import Path


Word = tuple[int, ...]


def canonicalize(word: Word) -> Word:
    """Rotate a cycle word so that its unique entry 1 comes first."""
    j = word.index(1)
    return word[j:] + word[:j]


def conjugate(word: Word, generator: int) -> Word:
    """Return s_i c s_i in cycle-word form for i=generator."""
    i = generator
    swapped = tuple(i + 1 if x == i else i if x == i + 1 else x for x in word)
    return canonicalize(swapped)


def word_text(word: Word) -> str:
    return "(" + ",".join(map(str, word)) + ")"


def sha256_lines(lines: list[str]) -> str:
    data = "".join(line + "\n" for line in lines).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def bfs(adjacency: list[list[tuple[int, int]]], source: int):
    """BFS with deterministic first parents; returns distances and parents."""
    distances = [-1] * len(adjacency)
    parents: list[tuple[int, int] | None] = [None] * len(adjacency)
    distances[source] = 0
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        for neighbor, generator in adjacency[vertex]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[vertex] + 1
                parents[neighbor] = (vertex, generator)
                queue.append(neighbor)
    return distances, parents


def reconstruct(
    words: list[Word], parents: list[tuple[int, int] | None], target: int
) -> dict[str, object]:
    vertices = [target]
    generators: list[int] = []
    current = target
    while parents[current] is not None:
        previous, generator = parents[current]
        vertices.append(previous)
        generators.append(generator)
        current = previous
    vertices.reverse()
    generators.reverse()
    word_path = [word_text(words[v]) for v in vertices]
    assert len(generators) + 1 == len(word_path)
    for word_a, generator, word_b in zip(vertices, generators, vertices[1:]):
        assert conjugate(words[word_a], generator) == words[word_b]
    return {
        "length": len(generators),
        "generators": generators,
        "vertices": word_path,
    }


def histogram_dict(counter: Counter[int]) -> dict[str, int]:
    return {str(distance): counter[distance] for distance in sorted(counter)}


def verify(n: int) -> dict[str, object]:
    words = [(1,) + tail for tail in itertools.permutations(range(2, n + 1))]
    word_to_index = {word: i for i, word in enumerate(words)}
    assert len(words) == len(word_to_index)

    adjacency: list[list[tuple[int, int]]] = []
    for word in words:
        labeled_neighbors = [
            (word_to_index[conjugate(word, generator)], generator)
            for generator in range(1, n)
        ]
        # Sort by the canonical neighbor word, then generator, fixing BFS order.
        labeled_neighbors.sort(key=lambda item: (words[item[0]], item[1]))
        assert all(neighbor != word_to_index[word] for neighbor, _ in labeled_neighbors)
        assert len({neighbor for neighbor, _ in labeled_neighbors}) == n - 1
        adjacency.append(labeled_neighbors)

    for vertex, neighbors in enumerate(adjacency):
        for neighbor, generator in neighbors:
            assert (vertex, generator) in adjacency[neighbor]

    undirected_edges = sorted(
        (min(vertex, neighbor), max(vertex, neighbor))
        for vertex, neighbors in enumerate(adjacency)
        for neighbor, _ in neighbors
        if vertex < neighbor
    )
    assert len(undirected_edges) == len(set(undirected_edges))

    root_word = tuple(range(1, n + 1))
    root = word_to_index[root_word]
    root_distances, root_parents = bfs(adjacency, root)
    assert -1 not in root_distances
    root_histogram = Counter(root_distances)
    sorting_time = max(root_distances)
    sorting_target = min(
        (i for i, distance in enumerate(root_distances) if distance == sorting_time),
        key=lambda i: words[i],
    )

    all_histogram: Counter[int] = Counter()
    distance_lines: list[str] = []
    diameter = -1
    diameter_pair: tuple[int, int] | None = None
    diameter_parents: list[tuple[int, int] | None] | None = None
    for source in range(len(words)):
        distances, parents = bfs(adjacency, source)
        assert -1 not in distances
        all_histogram.update(distances)
        distance_lines.append(",".join(map(str, distances)))
        eccentricity = max(distances)
        target = min(
            (i for i, distance in enumerate(distances) if distance == eccentricity),
            key=lambda i: words[i],
        )
        pair = (source, target)
        if eccentricity > diameter or (
            eccentricity == diameter
            and diameter_pair is not None
            and (words[pair[0]], words[pair[1]])
            < (words[diameter_pair[0]], words[diameter_pair[1]])
        ):
            diameter = eccentricity
            diameter_pair = pair
            diameter_parents = parents

    assert diameter_pair is not None and diameter_parents is not None
    assert sum(all_histogram.values()) == len(words) ** 2

    vertex_lines = [word_text(word) for word in words]
    edge_lines = [f"{word_text(words[u])}--{word_text(words[v])}" for u, v in undirected_edges]
    result: dict[str, object] = {
        "schema": "gamma-cycle-verifier-a-v1",
        "n": n,
        "canonical_representation": "unique cycle-word rotation (1,a2,...,an); reversal distinct",
        "adjacency": "for i=1,...,n-1 swap labels i and i+1, then rotate to start with 1; simple undirected graph",
        "ordering": "vertices lexicographic; BFS neighbors ordered by (neighbor word,generator)",
        "counts": {
            "vertices": len(words),
            "degree": n - 1,
            "undirected_edges": len(undirected_edges),
            "connected": True,
        },
        "root": word_text(root_word),
        "rooted_distance_histogram": histogram_dict(root_histogram),
        "all_ordered_pairs_distance_histogram": histogram_dict(all_histogram),
        "sorting_time": sorting_time,
        "sorting_farthest_cycle": word_text(words[sorting_target]),
        "sorting_shortest_path": reconstruct(words, root_parents, sorting_target),
        "diameter": diameter,
        "diameter_farthest_ordered_pair": [
            word_text(words[diameter_pair[0]]),
            word_text(words[diameter_pair[1]]),
        ],
        "diameter_shortest_path": reconstruct(
            words, diameter_parents, diameter_pair[1]
        ),
        "sha256": {
            "vertex_stream": sha256_lines(vertex_lines),
            "undirected_edge_stream": sha256_lines(edge_lines),
            "ordered_distance_rows": sha256_lines(distance_lines),
        },
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "libraries": "Python standard library only",
        },
        "replay": f"python3 evidence/verifier_a.py --n {n} --output evidence/verifier_a_n{n}.json",
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.n < 2:
        parser.error("--n must be at least 2")
    result = verify(args.n)
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
