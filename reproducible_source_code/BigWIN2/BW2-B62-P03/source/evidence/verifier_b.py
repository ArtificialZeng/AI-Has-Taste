#!/usr/bin/env python3
"""Independent exact verifier for Gamma_n using one-line permutation maps.

Vertices are enumerated as maps p=(p(1),...,p(n)); maps with a single orbit
are retained.  Adjacency is computed literally as composition s_i o p o s_i.
The cycle-word conversion in this file is used only for human-readable output
and for comparison with verifier A, never to construct an edge.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
from collections import Counter
from pathlib import Path


Permutation = tuple[int, ...]  # zero-based images, despite one-based output


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left o right as a one-line map."""
    return tuple(left[right[x]] for x in range(len(left)))


def adjacent_swap(n: int, generator: int) -> Permutation:
    """The map (generator,generator+1), with generator one-based."""
    answer = list(range(n))
    a = generator - 1
    answer[a], answer[a + 1] = answer[a + 1], answer[a]
    return tuple(answer)


def has_one_orbit(p: Permutation) -> bool:
    """Test whether the orbit of 1 has length n."""
    x = 0
    for step in range(1, len(p) + 1):
        x = p[x]
        if x == 0:
            return step == len(p)
    raise AssertionError("a permutation orbit did not close")


def cycle_word(p: Permutation) -> tuple[int, ...]:
    """Serialize a known full cycle by following its map from label 1."""
    word = [1]
    x = p[0]
    while x != 0:
        word.append(x + 1)
        x = p[x]
    assert len(word) == len(p)
    return tuple(word)


def map_from_cycle_text(text: str) -> Permutation:
    """Parse an A-format cycle solely for independent witness replay."""
    labels = tuple(int(part) for part in text.strip()[1:-1].split(","))
    p = [-1] * len(labels)
    for a, b in zip(labels, labels[1:] + labels[:1]):
        p[a - 1] = b - 1
    assert sorted(p) == list(range(len(labels))) and has_one_orbit(tuple(p))
    return tuple(p)


def cycle_text(word: tuple[int, ...]) -> str:
    return "(" + ",".join(str(x) for x in word) + ")"


def map_text(p: Permutation) -> str:
    return "[" + ",".join(str(x + 1) for x in p) + "]"


def hash_lines(lines) -> str:
    digest = hashlib.sha256()
    for line in lines:
        digest.update(line.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def scan_distances(graph: list[list[int]], start: int) -> list[int]:
    """A list-queue BFS returning all exact unweighted distances."""
    size = len(graph)
    distance = [-1] * size
    queue = [0] * size
    distance[start] = 0
    queue[0] = start
    head = 0
    tail = 1
    while head < tail:
        u = queue[head]
        head += 1
        next_distance = distance[u] + 1
        for v in graph[u]:
            if distance[v] < 0:
                distance[v] = next_distance
                queue[tail] = v
                tail += 1
    assert tail == size
    return distance


def scan_tree(graph: list[list[int]], start: int):
    """A second BFS variant retaining parent and generator labels."""
    size = len(graph)
    distance = [-1] * size
    parent = [-1] * size
    parent_generator = [-1] * size
    queue = [start]
    distance[start] = 0
    cursor = 0
    while cursor < len(queue):
        u = queue[cursor]
        cursor += 1
        for generator, v in enumerate(graph[u], start=1):
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                parent[v] = u
                parent_generator[v] = generator
                queue.append(v)
    assert len(queue) == size
    return distance, parent, parent_generator


def make_path(
    maps: list[Permutation], parent: list[int], parent_generator: list[int], target: int
) -> dict[str, object]:
    vertices = [target]
    generators: list[int] = []
    while parent[vertices[-1]] != -1:
        generators.append(parent_generator[vertices[-1]])
        vertices.append(parent[vertices[-1]])
    vertices.reverse()
    generators.reverse()
    return {
        "length": len(generators),
        "generators": generators,
        "vertices_as_cycle_words": [cycle_text(cycle_word(maps[v])) for v in vertices],
        "vertices_as_one_line_maps": [map_text(maps[v]) for v in vertices],
    }


def histogram(counter: Counter[int]) -> dict[str, int]:
    return {str(k): counter[k] for k in sorted(counter)}


def replay_a_path(
    record: dict[str, object],
    map_index: dict[Permutation, int],
    graph: list[list[int]],
) -> dict[str, object]:
    texts = record["vertices"]
    generators = record["generators"]
    assert isinstance(texts, list) and isinstance(generators, list)
    vertices = [map_index[map_from_cycle_text(text)] for text in texts]
    transitions_valid = len(vertices) == len(generators) + 1
    if transitions_valid:
        transitions_valid = all(
            graph[u][generator - 1] == v
            for u, generator, v in zip(vertices, generators, vertices[1:])
        )
    independent_distances = scan_distances(graph, vertices[0])
    actual_distance = independent_distances[vertices[-1]]
    return {
        "reported_length": record["length"],
        "independent_endpoint_distance": actual_distance,
        "transitions_valid_by_direct_composition": transitions_valid,
        "is_shortest": transitions_valid
        and len(generators) == actual_distance == record["length"],
    }


def verify(n: int, a_file: Path | None) -> dict[str, object]:
    maps = [
        p
        for p in itertools.permutations(range(n))
        if has_one_orbit(p)
    ]
    map_index = {p: i for i, p in enumerate(maps)}
    assert len(maps) == len(map_index)

    swaps = [adjacent_swap(n, generator) for generator in range(1, n)]
    graph: list[list[int]] = []
    for p in maps:
        neighbor_row = []
        for swap in swaps:
            conjugate = compose(swap, compose(p, swap))
            neighbor_row.append(map_index[conjugate])
        assert len(set(neighbor_row)) == n - 1
        graph.append(neighbor_row)

    for u, row in enumerate(graph):
        assert u not in row
        for generator, v in enumerate(row):
            assert graph[v][generator] == u

    edge_set = {
        (min(u, v), max(u, v))
        for u, row in enumerate(graph)
        for v in row
    }
    assert len(edge_set) * 2 == len(maps) * (n - 1)

    words = [cycle_word(p) for p in maps]
    word_order = sorted(range(len(maps)), key=lambda v: words[v])
    word_rank = {v: rank for rank, v in enumerate(word_order)}

    root_map = tuple(range(1, n)) + (0,)
    root = map_index[root_map]
    root_distance, root_parent, root_parent_generator = scan_tree(graph, root)
    root_histogram = Counter(root_distance)
    sorting_time = max(root_distance)
    sorting_target = min(
        (v for v, d in enumerate(root_distance) if d == sorting_time),
        key=lambda v: words[v],
    )

    all_histogram: Counter[int] = Counter()
    distance_digest = hashlib.sha256()
    diameter = -1
    diameter_pair: tuple[int, int] | None = None
    for source in word_order:
        distances = scan_distances(graph, source)
        all_histogram.update(distances)
        row = ",".join(str(distances[v]) for v in word_order) + "\n"
        distance_digest.update(row.encode("ascii"))
        eccentricity = max(distances)
        farthest = min(
            (v for v, d in enumerate(distances) if d == eccentricity),
            key=lambda v: words[v],
        )
        candidate = (source, farthest)
        if eccentricity > diameter or (
            eccentricity == diameter
            and diameter_pair is not None
            and (words[candidate[0]], words[candidate[1]])
            < (words[diameter_pair[0]], words[diameter_pair[1]])
        ):
            diameter = eccentricity
            diameter_pair = candidate

    assert diameter_pair is not None
    assert sum(all_histogram.values()) == len(maps) ** 2
    diameter_distance, diameter_parent, diameter_parent_generator = scan_tree(
        graph, diameter_pair[0]
    )
    assert diameter_distance[diameter_pair[1]] == diameter

    edges_in_word_order = sorted(
        (min(word_rank[u], word_rank[v]), max(word_rank[u], word_rank[v]))
        for u, v in edge_set
    )
    comparable_vertex_hash = hash_lines(cycle_text(words[v]) for v in word_order)
    comparable_edge_hash = hash_lines(
        f"{cycle_text(words[word_order[u]])}--{cycle_text(words[word_order[v]])}"
        for u, v in edges_in_word_order
    )

    result: dict[str, object] = {
        "schema": "gamma-permutation-map-verifier-b-v1",
        "n": n,
        "internal_representation": "zero-based one-line permutation image tuple; output displayed one-based",
        "vertex_filter": "retain exactly maps whose orbit of label 1 first returns after n steps",
        "adjacency": "construct s_i as a one-line map and compute compose(s_i,compose(p,s_i)); no cycle-word edge construction",
        "ordering": "vertices lexicographic by one-line map; generator rows ordered i=1,...,n-1",
        "counts": {
            "vertices": len(maps),
            "degree": n - 1,
            "undirected_edges": len(edge_set),
            "connected": -1 not in root_distance,
        },
        "root": cycle_text(words[root]),
        "rooted_distance_histogram": histogram(root_histogram),
        "all_ordered_pairs_distance_histogram": histogram(all_histogram),
        "sorting_time": sorting_time,
        "sorting_farthest_cycle": cycle_text(words[sorting_target]),
        "sorting_shortest_path": make_path(
            maps, root_parent, root_parent_generator, sorting_target
        ),
        "diameter": diameter,
        "diameter_farthest_ordered_pair": [
            cycle_text(words[diameter_pair[0]]),
            cycle_text(words[diameter_pair[1]]),
        ],
        "diameter_shortest_path": make_path(
            maps, diameter_parent, diameter_parent_generator, diameter_pair[1]
        ),
        "sha256": {
            "one_line_vertex_stream": hash_lines(map_text(p) for p in maps),
            "cycle_word_vertex_stream_for_cross_check": comparable_vertex_hash,
            "cycle_word_edge_stream_for_cross_check": comparable_edge_hash,
            "cycle_word_ordered_distance_rows_for_cross_check": distance_digest.hexdigest(),
        },
        "software": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "libraries": "Python standard library only",
        },
        "replay": f"python3 evidence/verifier_b.py --n {n} --compare-a evidence/verifier_a_n{n}.json --output evidence/verifier_b_n{n}.json",
    }

    if a_file is not None:
        a = json.loads(a_file.read_text(encoding="utf-8"))
        a_sort_replay = replay_a_path(a["sorting_shortest_path"], map_index, graph)
        a_diameter_replay = replay_a_path(a["diameter_shortest_path"], map_index, graph)
        comparisons = {
            "counts_equal": result["counts"] == a["counts"],
            "rooted_histogram_equal": result["rooted_distance_histogram"]
            == a["rooted_distance_histogram"],
            "all_ordered_pairs_histogram_equal": result[
                "all_ordered_pairs_distance_histogram"
            ]
            == a["all_ordered_pairs_distance_histogram"],
            "sorting_time_equal": sorting_time == a["sorting_time"],
            "diameter_equal": diameter == a["diameter"],
            "selected_sorting_witness_equal": result["sorting_farthest_cycle"]
            == a["sorting_farthest_cycle"],
            "selected_diameter_pair_equal": result["diameter_farthest_ordered_pair"]
            == a["diameter_farthest_ordered_pair"],
            "vertex_stream_hash_equal": comparable_vertex_hash
            == a["sha256"]["vertex_stream"],
            "edge_stream_hash_equal": comparable_edge_hash
            == a["sha256"]["undirected_edge_stream"],
            "ordered_distance_rows_hash_equal": distance_digest.hexdigest()
            == a["sha256"]["ordered_distance_rows"],
            "verifier_a_sorting_path_replay": a_sort_replay,
            "verifier_a_diameter_path_replay": a_diameter_replay,
        }
        comparisons["all_checks_passed"] = all(
            value is True for value in comparisons.values() if isinstance(value, bool)
        ) and a_sort_replay["is_shortest"] and a_diameter_replay["is_shortest"]
        result["verifier_a_comparison"] = comparisons

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--compare-a", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.n < 2:
        parser.error("--n must be at least 2")
    output = json.dumps(verify(args.n, args.compare_a), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        sys.stdout.write(output)
    else:
        args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
