#!/usr/bin/env python3
"""Broad semantic differential test for ``systematic_sat_search.py``.

For each deterministic normalized 6 x 5 matrix A, this script computes every
projective word of the kernel of (I_6 | A), derives the exact maximum number
of pairwise-disjoint target-avoiding recovery supports, and compares that
answer with the SAT encoding for each of the eleven individual targets.

The kernel/support oracle and packing dynamic program below do not reuse the
encoding's arithmetic gates, recovery variables, or model decoder.  The only
import from the encoder under test is ``build_encoding`` itself.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from itertools import product
from pathlib import Path

from pysat.solvers import Solver

from systematic_sat_search import build_encoding

P = 3
K = 6
N = 11


def projective_representatives(length: int) -> list[tuple[int, ...]]:
    return [
        x
        for x in product(range(P), repeat=length)
        if any(x) and next(value for value in x if value) == 1
    ]


def recovery_masks(a: list[list[int]], target: int) -> set[int]:
    """All target-avoiding supports recovering column ``target``."""
    masks: set[int] = set()
    for x in projective_representatives(5):
        # Every kernel direction of (I|A) occurs exactly once as (-Ax,x),
        # up to a nonzero scalar.  A direction involving the target gives a
        # recovery after moving that target term to the other side.
        word = [
            -sum(a[row][col] * x[col] for col in range(5)) % P
            for row in range(K)
        ] + list(x)
        if word[target]:
            mask = sum((value != 0) << col for col, value in enumerate(word))
            masks.add(mask & ~(1 << target))
    return masks


def packing_number(masks: set[int]) -> int:
    """Exact maximum disjoint packing after removing nonminimal supports."""
    minimal: list[int] = []
    for mask in sorted(masks, key=lambda item: (item.bit_count(), item)):
        if not any(previous & mask == previous for previous in minimal):
            minimal.append(mask)
    states = {0: 0}
    for mask in minimal:
        updates: dict[int, int] = {}
        for used, count in states.items():
            if not used & mask:
                union = used | mask
                updates[union] = max(updates.get(union, 0), count + 1)
        for union, count in updates.items():
            states[union] = max(states.get(union, 0), count)
    return max(states.values(), default=0)


def normalized_projective_columns() -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    reps = projective_representatives(K)
    leading = [v for v in reps if v[0] == 1]
    trailing = [v for v in reps if v[0] == 0]
    return leading, trailing


def transpose(columns: list[tuple[int, ...]]) -> list[list[int]]:
    return [[columns[col][row] for col in range(5)] for row in range(K)]


def cases(count: int, seed: int) -> list[tuple[str, list[list[int]]]]:
    # Five boundary/structured cases followed by held deterministic random
    # cases.  Every case obeys the encoder's justified convention: at least
    # three row-0-nonzero columns, followed by all row-0-zero columns.
    e = [tuple(1 if row == col else 0 for row in range(K)) for col in range(K)]
    one = (1,) * K
    structured = [
        ("source_G_prime", [
            [1, 1, 1, 0, 0], [1, 0, 1, 1, 0], [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0], [0, 1, 1, 0, 1], [0, 0, 1, 1, 1],
        ]),
        ("five_parallel_e1", transpose([e[0]] * 5)),
        ("three_e1_two_lower_basis", transpose([e[0], e[0], e[0], e[1], e[2]])),
        ("five_parallel_dense", transpose([one] * 5)),
        ("systematic_parallel_mix", transpose([e[0], e[0], one, e[3], e[5]])),
    ]
    if count < len(structured):
        raise ValueError(f"count must be at least {len(structured)}")
    rng = random.Random(seed)
    leading, trailing = normalized_projective_columns()
    output = list(structured)
    for index in range(count - len(structured)):
        number_leading = rng.randint(3, 5)
        columns = [rng.choice(leading) for _ in range(number_leading)]
        columns += [rng.choice(trailing) for _ in range(5 - number_leading)]
        output.append((f"random_{index:02d}_leading_{number_leading}", transpose(columns)))
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=20260910)
    parser.add_argument("--solvers", nargs="+", default=["minisat22", "cadical195"])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    details = []
    mismatches = []
    for name, a in cases(args.count, args.seed):
        packings = [packing_number(recovery_masks(a, target)) for target in range(N)]
        expected = [packing >= 3 for packing in packings]
        statuses: dict[str, list[bool]] = {}
        for solver_name in args.solvers:
            observed = []
            for target in range(N):
                enc, _, _ = build_encoding(active_targets=(target,), fixed_a=a)
                with Solver(name=solver_name, bootstrap_with=enc.cnf.clauses) as solver:
                    observed.append(solver.solve())
            statuses[solver_name] = observed
            if observed != expected:
                mismatches.append({
                    "case": name,
                    "solver": solver_name,
                    "expected_sat": expected,
                    "observed_sat": observed,
                })
        encoded = json.dumps(a, separators=(",", ":")).encode("ascii")
        details.append({
            "name": name,
            "a_sha256": hashlib.sha256(encoded).hexdigest(),
            "a_rows_mod_3": a,
            "oracle_max_target_avoiding_packings": packings,
            "expected_single_target_sat": expected,
            "observed_single_target_sat": statuses,
        })

    report = {
        "provenance": "win-00084-p06-research-fa957a0a5bec",
        "method": (
            "independent exhaustive projective-kernel support enumeration and "
            "exact disjoint-packing DP, differentially compared with fixed-A CNFs"
        ),
        "field": "F_3",
        "seed": args.seed,
        "matrix_cases": args.count,
        "targets_per_case": N,
        "solver_backends": args.solvers,
        "single_target_solver_checks": args.count * N * len(args.solvers),
        "mismatches": mismatches,
        "accepted": not mismatches,
        "cases": details,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    raise SystemExit(0 if report["accepted"] else 1)


if __name__ == "__main__":
    main()
