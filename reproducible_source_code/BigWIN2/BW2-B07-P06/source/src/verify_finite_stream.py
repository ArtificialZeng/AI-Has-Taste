#!/usr/bin/env python3
"""Independent finite-stream verifier using NetworkX and matrix traces.

This intentionally does not import the discovery parser or evaluator.
For a cycle with rooted-tree color weights w_i, it computes

    trace(D_0 B D_1 B ... D_{c-1} B),

where D_i=diag(w_i) and B=J-I.  This is a second aggregation of the
proper-coloring definition, independent of the start-color recurrence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass

import networkx as nx


PRIMARY = (
    (998_244_353, (1, 4, 17, 64)),
    (1_000_000_007, (3, 8, 29, 101)),
    (1_000_000_009, (5, 13, 47, 173)),
)
REFINE_MODULUS = 1_000_000_000_000_000_003


@dataclass
class Representative:
    graph6: str
    data: tuple[tuple[int, ...], int, int]
    refined: int | None = None


def parse(line: bytes) -> nx.Graph:
    raw = line.strip()
    if raw.startswith(b">>graph6<<"):
        raw = raw[len(b">>graph6<<") :]
    graph = nx.from_graph6_bytes(raw)
    if not nx.is_connected(graph) or graph.number_of_edges() != graph.number_of_nodes():
        raise ValueError("input is not connected unicyclic")
    return graph


def cyclic_order(graph: nx.Graph) -> list[int]:
    cycles = nx.cycle_basis(graph)
    if len(cycles) != 1 or len(cycles[0]) < 3:
        raise ValueError("input does not have a unique cycle")
    cycle_set = set(cycles[0])
    first = min(cycle_set)
    cycle = [first]
    previous = None
    current = first
    while True:
        neighbors = [w for w in graph[current] if w in cycle_set and w != previous]
        if not neighbors:
            raise ValueError("invalid cycle")
        nxt = neighbors[0]
        if nxt == first:
            break
        if nxt in cycle:
            raise ValueError("premature cycle closure")
        cycle.append(nxt)
        previous, current = current, nxt
    if len(cycle) != len(cycle_set):
        raise ValueError("cycle traversal failed")
    return cycle


def rooted_message(
    graph: nx.Graph,
    vertex: int,
    parent: int | None,
    cycle_set: set[int],
    values: tuple[int, ...],
    modulus: int,
) -> list[int]:
    children = [
        w
        for w in graph[vertex]
        if w != parent and not (vertex in cycle_set and w in cycle_set)
    ]
    child_messages = [
        rooted_message(graph, child, vertex, cycle_set, values, modulus)
        for child in children
    ]
    answer = []
    for color, value in enumerate(values):
        product = value % modulus
        for message in child_messages:
            product = product * ((sum(message) - message[color]) % modulus) % modulus
        answer.append(product)
    return answer


def right_multiply_B(matrix: list[list[int]], modulus: int) -> list[list[int]]:
    # B=J-I, hence every output entry is its row sum minus one entry.
    return [[(sum(row) - entry) % modulus for entry in row] for row in matrix]


def evaluation(graph: nx.Graph, cycle: list[int], values: tuple[int, ...], modulus: int) -> int:
    cycle_set = set(cycle)
    weights = [
        rooted_message(graph, root, None, cycle_set, values, modulus)
        for root in cycle
    ]
    q = len(values)
    matrix = [[weights[0][i] if i == j else 0 for j in range(q)] for i in range(q)]
    for i in range(1, len(cycle)):
        matrix = right_multiply_B(matrix, modulus)
        diagonal = weights[i]
        matrix = [
            [row[column] * diagonal[column] % modulus for column in range(q)]
            for row in matrix
        ]
    matrix = right_multiply_B(matrix, modulus)
    return sum(matrix[i][i] for i in range(q)) % modulus


def data(graph: nx.Graph, cycle: list[int]) -> tuple[tuple[int, ...], int, int]:
    degrees = tuple(sorted((degree for _, degree in graph.degree()), reverse=True))
    r = sum(graph.degree(v) >= 3 for v in cycle)
    k = sum(
        graph.degree(u) >= 2 and graph.degree(v) >= 2
        for u, v in graph.edges()
    )
    return degrees, r, k


def refine_values(n: int) -> tuple[int, ...]:
    return tuple(
        (pow(53, i + 1, REFINE_MODULUS) + 130363 * (i + 1)) % REFINE_MODULUS
        for i in range(n)
    )


def analyze(line: bytes):
    graph = parse(line)
    cycle = cyclic_order(graph)
    signature = tuple(evaluation(graph, cycle, values, modulus) for modulus, values in PRIMARY)
    return graph, cycle, data(graph, cycle), signature


def refine(graph: nx.Graph, cycle: list[int]) -> int:
    return evaluation(graph, cycle, refine_values(graph.number_of_nodes()), REFINE_MODULUS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress-every", type=int, default=100_000)
    parser.add_argument("--output", required=True)
    parser.add_argument("--target-only", action="store_true")
    args = parser.parse_args()
    buckets: dict[tuple[int, tuple[int, ...]], list[Representative]] = {}
    candidates = []
    primary_collision_count = 0
    refined_separation_count = 0
    refined_match_count = 0
    separation_samples = []
    processed = 0
    included = 0
    included_by_cycle: dict[int, int] = {}
    input_digest = hashlib.sha256()
    separation_digest = hashlib.sha256()
    start = time.monotonic()
    for line in sys.stdin.buffer:
        if not line.strip() or line.startswith(b">>"):
            continue
        input_digest.update(line.strip() + b"\n")
        graph, cycle, structural, signature = analyze(line)
        processed += 1
        if args.target_only and len(cycle) == 3 and graph.number_of_nodes() % 2 == 0:
            continue
        included += 1
        included_by_cycle[len(cycle)] = included_by_cycle.get(len(cycle), 0) + 1
        encoded = line.strip().decode("ascii")
        separation_digest.update(
            (
                encoded
                + "|"
                + str(len(cycle))
                + "|"
                + repr(structural)
                + "|"
                + repr(signature)
                + "\n"
            ).encode("ascii")
        )
        key = (len(cycle), signature)
        reps = buckets.get(key)
        if reps is None:
            buckets[key] = [Representative(encoded, structural)]
        else:
            primary_collision_count += 1
            current_refined = refine(graph, cycle)
            match = None
            for rep in reps:
                if rep.refined is None:
                    old_graph, old_cycle, _old_data, _old_sig = analyze(rep.graph6.encode())
                    rep.refined = refine(old_graph, old_cycle)
                if rep.refined == current_refined:
                    match = rep
                    break
            if match is None:
                refined_separation_count += 1
                if len(separation_samples) < 10:
                    separation_samples.append(
                        {
                            "graph6_a": reps[0].graph6,
                            "graph6_b": encoded,
                            "cycle_length": len(cycle),
                            "data_a": reps[0].data,
                            "data_b": structural,
                            "refined_a": reps[0].refined,
                            "refined_b": current_refined,
                        }
                    )
                reps.append(Representative(encoded, structural, current_refined))
            else:
                refined_match_count += 1
                if match.data != structural:
                    candidates.append(
                        {
                            "graph6_a": match.graph6,
                            "graph6_b": encoded,
                            "cycle_length": len(cycle),
                            "data_a": match.data,
                            "data_b": structural,
                            "warning": "evaluation collision; exactify before treating as equal CSF",
                        }
                    )
        if args.progress_every and processed % args.progress_every == 0:
            print(
                f"processed={processed} included={included} buckets={len(buckets)} candidates={len(candidates)} elapsed_s={time.monotonic()-start:.1f}",
                file=sys.stderr,
                flush=True,
            )
    result = {
        "processed": processed,
        "included": included,
        "included_by_cycle": included_by_cycle,
        "buckets": len(buckets),
        "primary_collision_count": primary_collision_count,
        "refined_separation_count": refined_separation_count,
        "refined_match_count": refined_match_count,
        "candidate_count": len(candidates),
        "elapsed_seconds": round(time.monotonic() - start, 3),
        "primary": PRIMARY,
        "refine_modulus": REFINE_MODULUS,
        "input_graph6_sha256": input_digest.hexdigest(),
        "separation_records_sha256": separation_digest.hexdigest(),
        "refined_separation_samples": separation_samples,
        "candidates": candidates,
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print("SUMMARY " + json.dumps(result, separators=(",", ":")), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
