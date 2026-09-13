#!/usr/bin/env python3
"""Generate the Szekeres--Peters direct rank-three signotope CNF for k=6."""

from __future__ import annotations

import argparse
import itertools
import math
from pathlib import Path
from typing import Dict, Iterator, Tuple

from compact_sat import signotope_clauses, signotope_prime_clauses, triple_variables, write_dimacs


Triple = Tuple[int, int, int]
SixSet = Tuple[int, int, int, int, int, int]


def convex_relations(six: SixSet, variables: Dict[Triple, int]) -> tuple[tuple[int, ...], ...]:
    """Return the eight signed four-term relations in Szekeres--Peters (4.1)."""
    a, b, c, d, e, f = six
    x = variables
    return (
        (x[a, b, c], x[b, c, d], x[c, d, e], x[d, e, f]),
        (x[a, b, c], x[b, c, d], x[c, d, f], -x[a, e, f]),
        (x[a, b, c], x[b, c, e], x[c, e, f], -x[a, d, f]),
        (x[a, b, d], x[b, d, e], x[d, e, f], -x[a, c, f]),
        (x[a, c, d], x[c, d, e], x[d, e, f], -x[a, b, f]),
        (x[a, b, c], x[b, c, f], -x[a, d, e], -x[d, e, f]),
        (x[a, b, d], x[b, d, f], -x[a, c, e], -x[c, e, f]),
        (x[a, c, d], x[c, d, f], -x[a, b, e], -x[b, e, f]),
    )


def direct_six_clauses(
    n: int,
    variables: Dict[Triple, int],
    fix_reflection: bool,
    fix_extreme: bool,
    prime_signotope: bool,
) -> Iterator[tuple[int, ...]]:
    for quad in itertools.combinations(range(n), 4):
        if prime_signotope:
            yield from signotope_prime_clauses(quad, variables)
        else:
            yield from signotope_clauses(quad, variables)
    for six in itertools.combinations(range(n), 6):
        for relation in convex_relations(six, variables):
            # A relation holds iff its four signed literals are all true or
            # all false.  These two clauses forbid both cases.
            yield relation
            yield tuple(-literal for literal in relation)
    if fix_reflection:
        yield (variables[0, 1, 2],)
    if fix_extreme:
        for j, k in itertools.combinations(range(1, n), 2):
            yield (variables[0, j, k],)


def counts(
    n: int, fix_reflection: bool, fix_extreme: bool, prime_signotope: bool
) -> dict[str, int]:
    quads = math.comb(n, 4)
    six_sets = math.comb(n, 6)
    if fix_reflection and fix_extreme:
        raise ValueError("choose at most one symmetry normalization")
    symmetry = math.comb(n - 1, 2) if fix_extreme else int(fix_reflection)
    signotope_multiplier = 8 if prime_signotope else 4
    return {
        "variables": math.comb(n, 3),
        "clauses": signotope_multiplier * quads + 16 * six_sets + symmetry,
        "literal_occurrences": 3 * signotope_multiplier * quads + 64 * six_sets + symmetry,
        "signotope_clauses": signotope_multiplier * quads,
        "convex_relation_forbidding_clauses": 16 * six_sets,
        "symmetry_clauses": symmetry,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--fix-reflection", action="store_true")
    parser.add_argument("--fix-extreme", action="store_true")
    parser.add_argument("--prime-signotope", action="store_true")
    parser.add_argument("--count-only", action="store_true")
    args = parser.parse_args()
    if args.n < 6:
        raise SystemExit("require n >= 6")
    if args.fix_reflection and args.fix_extreme:
        raise SystemExit("choose at most one of --fix-reflection and --fix-extreme")
    result = counts(
        args.n, args.fix_reflection, args.fix_extreme, args.prime_signotope
    )
    for key, value in result.items():
        print(f"{key}={value}")
    if args.count_only:
        return
    if args.out is None:
        raise SystemExit("--out is required unless --count-only is used")
    variables = triple_variables(args.n)
    write_dimacs(
        args.out,
        result["variables"],
        result["clauses"],
        direct_six_clauses(
            args.n,
            variables,
            args.fix_reflection,
            args.fix_extreme,
            args.prime_signotope,
        ),
    )
    print(f"wrote={args.out}")


if __name__ == "__main__":
    main()
