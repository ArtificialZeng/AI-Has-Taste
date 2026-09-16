#!/usr/bin/env python3
"""Discovery search for equal-CSF unicyclic graphs with different data.

The hash values are exact modular evaluations of the proper-coloring
definition, computed by tree/cycle dynamic programming.  They are filters,
not certificates.  Candidate pairs must be checked by both exact programs.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass

from graph6_utils import parse_graph6, structural_data, unicyclic_decomposition


PRIMARY_POINTS = (
    (1_000_000_007, (1, 2, 5)),
    (1_000_000_007, (2, 7, 19)),
    (1_000_000_009, (3, 11, 41)),
)
REFINE_PRIME = 2_305_843_009_213_693_951  # 2^61 - 1


@dataclass
class Record:
    graph6: str
    data: tuple[tuple[int, ...], int, int]
    refine: int | None


def coloring_evaluation(
    adj: list[list[int]],
    cycle: list[int],
    cycle_set: set[int],
    parent: list[int],
    order: list[int],
    values: tuple[int, ...],
    modulus: int,
) -> int:
    """Evaluate X_G(values) modulo modulus using the unicyclic decomposition."""
    q = len(values)
    messages = [[0] * q for _ in adj]
    for v in reversed(order):
        row = messages[v]
        for color, x in enumerate(values):
            product = x % modulus
            for w in adj[v]:
                if parent[w] == v:
                    child = messages[w]
                    product = product * ((sum(child) - child[color]) % modulus) % modulus
            row[color] = product

    weights = [messages[v] for v in cycle]
    answer = 0
    for start in range(q):
        dp = [0] * q
        dp[start] = weights[0][start]
        for root_index in range(1, len(cycle)):
            total = sum(dp) % modulus
            current_weight = weights[root_index]
            dp = [
                current_weight[color] * ((total - dp[color]) % modulus) % modulus
                for color in range(q)
            ]
        answer = (answer + sum(dp[color] for color in range(q) if color != start)) % modulus
    return answer


def point_values(n: int) -> tuple[int, ...]:
    # Fixed, reproducible, pairwise distinct values.  q=n makes restriction to
    # q variables injective for homogeneous symmetric functions of degree n;
    # one evaluation is still only a probabilistic polynomial identity filter.
    return tuple((pow(37, i + 1, REFINE_PRIME) + 104729 * (i + 1)) % REFINE_PRIME for i in range(n))


def parse_record(line: bytes):
    n, adj, edges = parse_graph6(line)
    if len(edges) != n:
        raise ValueError("expected a connected n-vertex, n-edge graph")
    cycle, cycle_set, parent, order = unicyclic_decomposition(adj)
    return n, adj, cycle, cycle_set, parent, order


def evaluate_record(line: bytes):
    n, adj, cycle, cycle_set, parent, order = parse_record(line)
    data = structural_data(adj, cycle)
    primary = tuple(
        coloring_evaluation(adj, cycle, cycle_set, parent, order, values, prime)
        for prime, values in PRIMARY_POINTS
    )
    return n, adj, cycle, cycle_set, parent, order, data, primary


def refinement(evaluated) -> int:
    n, adj, cycle, cycle_set, parent, order, _data, _primary = evaluated
    return coloring_evaluation(
        adj,
        cycle,
        cycle_set,
        parent,
        order,
        point_values(n),
        REFINE_PRIME,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress-every", type=int, default=100_000)
    parser.add_argument("--candidate-file")
    parser.add_argument(
        "--target-only",
        action="store_true",
        help="skip the excluded class c=3 with even order",
    )
    parser.add_argument("--cycle-length", type=int)
    args = parser.parse_args()

    buckets: dict[tuple[int, tuple[int, ...]], list[Record]] = {}
    candidates: list[dict] = []
    seen = 0
    included = 0
    start_time = time.monotonic()

    for raw in sys.stdin.buffer:
        if not raw.strip() or raw.startswith(b">>"):
            continue
        parsed = parse_record(raw)
        n, adj, cycle, cycle_set, parent, order = parsed
        if args.target_only and len(cycle) == 3 and n % 2 == 0:
            seen += 1
            continue
        if args.cycle_length is not None and len(cycle) != args.cycle_length:
            seen += 1
            continue
        included += 1
        data = structural_data(adj, cycle)
        primary = tuple(
            coloring_evaluation(adj, cycle, cycle_set, parent, order, values, prime)
            for prime, values in PRIMARY_POINTS
        )
        evaluated = (n, adj, cycle, cycle_set, parent, order, data, primary)
        # Cycle length is already an exact CSF invariant, and including it
        # sharply reduces irrelevant specialization collisions.
        key = (len(cycle), primary)
        g6 = raw.strip().decode("ascii")
        representatives = buckets.get(key)
        if representatives is None:
            buckets[key] = [Record(g6, data, None)]
        else:
            current_refine = refinement(evaluated)
            matching = None
            for rep in representatives:
                if rep.refine is None:
                    rep_eval = evaluate_record(rep.graph6.encode("ascii"))
                    rep.refine = refinement(rep_eval)
                if rep.refine == current_refine:
                    matching = rep
                    break
            if matching is None:
                representatives.append(Record(g6, data, current_refine))
            elif matching.data != data:
                candidate = {
                    "n": n,
                    "cycle_length": len(cycle),
                    "graph6_a": matching.graph6,
                    "graph6_b": g6,
                    "data_a": {
                        "degree_sequence": matching.data[0],
                        "rooted_tree_count": matching.data[1],
                        "internal_edge_count": matching.data[2],
                    },
                    "data_b": {
                        "degree_sequence": data[0],
                        "rooted_tree_count": data[1],
                        "internal_edge_count": data[2],
                    },
                    "primary_evaluations": primary,
                    "refinement_evaluation": current_refine,
                    "warning": "modular-evaluation collision only; exact CSF equality not yet certified",
                }
                candidates.append(candidate)
                print(json.dumps(candidate, separators=(",", ":")), flush=True)

        seen += 1
        if args.progress_every and seen % args.progress_every == 0:
            elapsed = time.monotonic() - start_time
            print(
                f"processed={seen} primary_buckets={len(buckets)} candidates={len(candidates)} elapsed_s={elapsed:.1f}",
                file=sys.stderr,
                flush=True,
            )

    summary = {
        "processed": seen,
        "included": included,
        "primary_buckets": len(buckets),
        "candidate_count": len(candidates),
        "elapsed_seconds": round(time.monotonic() - start_time, 3),
        "primary_points": PRIMARY_POINTS,
        "refine_prime": REFINE_PRIME,
    }
    print("SUMMARY " + json.dumps(summary, separators=(",", ":")), file=sys.stderr)
    if args.candidate_file:
        with open(args.candidate_file, "w", encoding="utf-8") as handle:
            json.dump({"summary": summary, "candidates": candidates}, handle, indent=2)
            handle.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
