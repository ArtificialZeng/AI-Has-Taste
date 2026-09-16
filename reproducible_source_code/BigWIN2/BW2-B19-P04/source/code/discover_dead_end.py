#!/usr/bin/env python3
"""Exact-integer discovery search; output is evidence, never a certificate."""

import argparse
import itertools
import json
import platform
import random
import sys
from pathlib import Path


def facets(n=7, d=3):
    return tuple(tuple(c) for c in itertools.combinations(range(1, n + 1), d + 1))


FACETS = facets()
SETS = tuple(frozenset(f) for f in FACETS)
FULL = (1 << len(FACETS)) - 1


def appendable_ridge(state, j):
    """Ridge-cover characterization of a pure codimension-one intersection."""
    f = SETS[j]
    intersections = [f & SETS[i] for i in range(35) if state >> i & 1]
    ridges = [h for h in intersections if len(h) == 3]
    return bool(ridges) and all(any(h <= r for r in ridges) for h in intersections)


def appendable_direct(state, j):
    """Independent evaluator: inclusion-maximal intersections must all be ridges."""
    f = SETS[j]
    ints = {f & SETS[i] for i in range(35) if state >> i & 1}
    maximal = [h for h in ints if not any(h < k for k in ints)]
    return bool(maximal) and all(len(h) == 3 for h in maximal)


def legal_moves(state):
    return [j for j in range(35) if not (state >> j & 1) and appendable_ridge(state, j)]


def crosscheck(samples, seed):
    rng = random.Random(seed ^ 0x5EEDC0DE)
    for _ in range(samples):
        state = rng.randrange(1, FULL + 1)
        for j in range(35):
            if not (state >> j & 1):
                a = appendable_ridge(state, j)
                b = appendable_direct(state, j)
                if a != b:
                    raise AssertionError((state, j, a, b))


def run(trials, seed):
    rng = random.Random(seed)
    best = None
    hist = {}
    for trial in range(trials):
        state = 1  # fix facet (1,2,3,4) by vertex transitivity
        order = [0]
        while state != FULL:
            moves = legal_moves(state)
            hist[len(moves)] = hist.get(len(moves), 0) + 1
            if not moves:
                return {"dead": True, "trial": trial, "order_indices": order,
                        "order_facets": [FACETS[i] for i in order], "state": state,
                        "histogram": hist}
            # Minimum-onward-degree heuristic with randomized ties.
            scored = []
            for j in moves:
                nxt = state | (1 << j)
                scored.append((len(legal_moves(nxt)), rng.random(), j))
            _, _, chosen = min(scored)
            state |= 1 << chosen
            order.append(chosen)
        if best is None or len(order) < len(best):
            best = order
    return {"dead": False, "trials": trials, "best_length": len(best or []),
            "histogram": hist}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=73003001)
    ap.add_argument("--crosscheck-samples", type=int, default=1000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    crosscheck(args.crosscheck_samples, args.seed)
    result = run(args.trials, args.seed)
    result["discovery_only"] = True
    result["parameters"] = vars(args) | {"output": str(args.output) if args.output else None}
    result["environment"] = {"python": sys.version, "platform": platform.platform()}
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
