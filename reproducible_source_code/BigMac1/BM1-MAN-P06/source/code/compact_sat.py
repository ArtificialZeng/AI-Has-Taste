#!/usr/bin/env python3
"""Generate the parity-compressed Erdős--Szekeres refutation CNF.

The formula is a one-sided, sound refutation encoding.  Every realizable
general-position point set with no convex k-subset induces a satisfying
assignment.  Therefore UNSAT proves the corresponding Erdős--Szekeres upper
bound.  SAT alone need not give a realizable order type.
"""

from __future__ import annotations

import argparse
import itertools
import math
from pathlib import Path
from typing import Dict, Iterable, Iterator, Sequence, TextIO, Tuple


Triple = Tuple[int, int, int]
Quad = Tuple[int, int, int, int]


def falling_factorial(n: int, r: int) -> int:
    result = 1
    for value in range(n - r + 1, n + 1):
        result *= value
    return result


def triple_variables(n: int) -> Dict[Triple, int]:
    return {
        triple: index
        for index, triple in enumerate(itertools.combinations(range(n), 3), 1)
    }


def orientation_literal(
    a: int, b: int, c: int, variables: Dict[Triple, int]
) -> int:
    """Literal asserting that the ordered triple (a,b,c) is positive."""
    ordered = tuple(sorted((a, b, c)))
    variable = variables[ordered]
    if (a, b, c) in (
        ordered,
        (ordered[1], ordered[2], ordered[0]),
        (ordered[2], ordered[0], ordered[1]),
    ):
        return variable
    return -variable


def reduced_ax5_clauses(
    n: int, variables: Dict[Triple, int]
) -> Iterator[Tuple[int, ...]]:
    """The reduced five-point implication family used in the 2025 encoding."""
    for p1 in range(n):
        for p2 in range(n):
            if p2 == p1:
                continue
            for p3 in range(n):
                if p3 in (p1, p2):
                    continue
                for p4 in range(p3 + 1, n):
                    if p4 in (p1, p2):
                        continue
                    for p5 in range(p3 + 1, n):
                        if p5 in (p1, p2, p3, p4):
                            continue
                        antecedents = (
                            orientation_literal(p1, p2, p3, variables),
                            orientation_literal(p1, p2, p4, variables),
                            orientation_literal(p1, p2, p5, variables),
                            orientation_literal(p1, p3, p4, variables),
                            orientation_literal(p1, p4, p5, variables),
                        )
                        conclusion = orientation_literal(p1, p3, p5, variables)
                        yield tuple(-literal for literal in antecedents) + (conclusion,)


def full_ax5_clauses(
    n: int, variables: Dict[Triple, int]
) -> Iterator[Tuple[int, ...]]:
    """All ordered instances of the five-point implication."""
    for p1, p2, p3, p4, p5 in itertools.permutations(range(n), 5):
        antecedents = (
            orientation_literal(p1, p2, p3, variables),
            orientation_literal(p1, p2, p4, variables),
            orientation_literal(p1, p2, p5, variables),
            orientation_literal(p1, p3, p4, variables),
            orientation_literal(p1, p4, p5, variables),
        )
        conclusion = orientation_literal(p1, p3, p5, variables)
        yield tuple(-literal for literal in antecedents) + (conclusion,)


def parity_guard_clauses(
    q: Quad,
    indicator: int,
    variables: Dict[Triple, int],
    signotope_restricted: bool = False,
    equivalence: bool = False,
    factored_reverse: bool = False,
) -> Iterator[Tuple[int, ...]]:
    """Encode indicator => odd four-orientation parity.

    Odd parity is the non-convex four-point case.  For each even assignment,
    one clause forbids that assignment when ``indicator`` is true.  There are
    eight clauses without a signotope assumption and four after restricting
    to signotope-admissible assignments.  With ``equivalence=True``, the
    reverse implication is encoded by likewise forbidding every admissible
    odd assignment when ``indicator`` is false.
    """
    a, b, c, d = q
    orientations = (
        variables[(a, b, c)],
        variables[(a, b, d)],
        variables[(a, c, d)],
        variables[(b, c, d)],
    )
    if signotope_restricted:
        abc, abd, acd, bcd = orientations
        # Under the one-change rule, odd parity is equivalent to
        # (abc != bcd) and (abd == acd).  This factors the four guards from
        # width five to width three.
        yield (-indicator, abc, bcd)
        yield (-indicator, -abc, -bcd)
        yield (-indicator, -abd, acd)
        yield (-indicator, abd, -acd)
        if equivalence:
            if factored_reverse:
                # Under one-change, even parity is equivalently
                # (abc == abd) and (acd == bcd).  Thus indicator=0 can be
                # guarded by four additional ternary clauses.
                yield (indicator, -acd, bcd)
                yield (indicator, acd, -bcd)
                yield (indicator, -abc, abd)
                yield (indicator, abc, -abd)
                return
            for bits in itertools.product((False, True), repeat=4):
                if sum(bits) % 2 == 0:
                    continue
                sequence = (bits[3], bits[2], bits[1], bits[0])
                changes = sum(
                    left != right for left, right in zip(sequence, sequence[1:])
                )
                if changes > 1:
                    continue
                mismatches = tuple(
                    -var if bit else var for var, bit in zip(orientations, bits)
                )
                yield (indicator,) + mismatches
        return
    for bits in itertools.product((False, True), repeat=4):
        if sum(bits) % 2:
            continue
        mismatches = tuple(-var if bit else var for var, bit in zip(orientations, bits))
        yield (-indicator,) + mismatches
    if equivalence:
        for bits in itertools.product((False, True), repeat=4):
            if sum(bits) % 2 == 0:
                continue
            mismatches = tuple(
                -var if bit else var for var, bit in zip(orientations, bits)
            )
            yield (indicator,) + mismatches


def signotope_clauses(q: Quad, variables: Dict[Triple, int]) -> Iterator[Tuple[int, ...]]:
    """Standard four-clause rank-three signotope encoding.

    For ``a < b < c < d``, the clauses are equivalent to requiring the sign
    sequence ``abc, abd, acd, bcd`` to have at most one change.  This compact
    form is the ordered signotope encoding used by Subercaseaux--Mackey--Qian--
    Heule; ``signotope_direct_clauses`` below retains the direct eight-clause
    forbidden-pattern encoding for controlled propagation benchmarks.
    """
    a, b, c, d = q
    abc = variables[(a, b, c)]
    abd = variables[(a, b, d)]
    acd = variables[(a, c, d)]
    bcd = variables[(b, c, d)]
    yield (-abc, -acd, abd)
    yield (abc, acd, -abd)
    yield (-abc, -bcd, acd)
    yield (abc, bcd, -acd)


def signotope_direct_clauses(
    q: Quad, variables: Dict[Triple, int]
) -> Iterator[Tuple[int, ...]]:
    """Directly forbid all eight patterns with two or three sign changes."""
    a, b, c, d = q
    sequence = (
        variables[(b, c, d)],
        variables[(a, c, d)],
        variables[(a, b, d)],
        variables[(a, b, c)],
    )
    for bits in itertools.product((False, True), repeat=4):
        changes = sum(left != right for left, right in zip(bits, bits[1:]))
        if changes <= 1:
            continue
        yield tuple(-var if bit else var for var, bit in zip(sequence, bits))


def signotope_prime_clauses(
    q: Quad, variables: Dict[Triple, int]
) -> Iterator[Tuple[int, ...]]:
    """All eight ternary prime implicates of the one-change relation."""
    yield from signotope_clauses(q, variables)
    a, b, c, d = q
    abc = variables[(a, b, c)]
    abd = variables[(a, b, d)]
    acd = variables[(a, c, d)]
    bcd = variables[(b, c, d)]
    yield (-abd, acd, -bcd)
    yield (-abc, abd, -bcd)
    yield (abc, -abd, bcd)
    yield (abd, -acd, bcd)


def hull_clauses(
    n: int,
    layers: Sequence[int],
    offsets: Sequence[int],
    variables: Dict[Triple, int],
) -> Iterator[Tuple[int, ...]]:
    """Convex-layer and optional wedge anchors matching the audited generator."""
    current = 0
    previous = 0
    for layer_index, size in enumerate(layers):
        stop = current + size
        for triple in itertools.combinations(range(current, stop), 3):
            yield (orientation_literal(*triple, variables),)
        for left in range(current, stop - 1):
            for point in range(stop, n):
                yield (orientation_literal(left, left + 1, point, variables),)
        if size:
            for point in range(stop, n):
                yield (orientation_literal(stop - 1, current, point, variables),)

        if layer_index and offsets[layer_index]:
            anchor = current + offsets[layer_index]
            for point in range(current + 1, n):
                yield (orientation_literal(previous, current, point, variables),)
            for point in range(current + 1, n):
                if point != anchor:
                    yield (-orientation_literal(previous, anchor, point, variables),)
        previous = current
        current = stop


def hull_clause_count(n: int, layers: Sequence[int], offsets: Sequence[int]) -> int:
    current = 0
    count = 0
    for layer_index, size in enumerate(layers):
        stop = current + size
        count += math.comb(size, 3) + size * (n - stop)
        if layer_index and offsets[layer_index]:
            count += 2 * (n - current - 1) - 1
        current = stop
    return count


def counts(
    n: int,
    k: int,
    layers: Sequence[int] = (),
    offsets: Sequence[int] = (),
    ax5_mode: str = "reduced",
    parity_mode: str = "one-sided",
    fix_reflection: bool = False,
    fix_extreme: bool = False,
) -> dict:
    triples = math.comb(n, 3)
    quads = math.comb(n, 4)
    if ax5_mode == "signotope":
        ax5 = 4 * quads
    elif ax5_mode in ("signotope-direct", "signotope-prime"):
        ax5 = 8 * quads
    elif ax5_mode == "reduced":
        ax5 = falling_factorial(n, 5) // 3
    elif ax5_mode == "full":
        ax5 = falling_factorial(n, 5)
    elif ax5_mode == "none":
        ax5 = 0
    else:
        raise ValueError(f"unknown ax5 mode: {ax5_mode}")
    if parity_mode not in ("one-sided", "equivalence", "equivalence-factored"):
        raise ValueError(f"unknown parity mode: {parity_mode}")
    signotope_mode = ax5_mode in ("signotope", "signotope-direct", "signotope-prime")
    parity_base = 4 if signotope_mode else 8
    is_equivalence = parity_mode != "one-sided"
    parity = parity_base * (2 if is_equivalence else 1) * quads
    if signotope_mode:
        if parity_mode == "equivalence-factored":
            parity_literals_per_quad = 24
        else:
            parity_literals_per_quad = 12 + (20 if is_equivalence else 0)
    else:
        if parity_mode == "equivalence-factored":
            raise ValueError("factored equivalence requires a signotope block")
        parity_literals_per_quad = 40 * (2 if is_equivalence else 1)
    exclusion = math.comb(n, k)
    hull = hull_clause_count(n, layers, offsets) if layers else 0
    if fix_reflection and fix_extreme:
        raise ValueError("choose at most one symmetry normalization")
    symmetry = math.comb(n - 1, 2) if fix_extreme else int(fix_reflection)
    variables = triples + quads
    clauses = ax5 + parity + exclusion + hull + symmetry
    if ax5_mode in ("signotope", "signotope-prime"):
        consistency_width = 3
    elif ax5_mode == "signotope-direct":
        consistency_width = 4
    else:
        consistency_width = 6
    literals = (
        consistency_width * ax5
        + parity_literals_per_quad * quads
        + math.comb(k, 4) * exclusion
        + hull
        + symmetry
    )
    return {
        "variables": variables,
        "clauses": clauses,
        "literal_occurrences": literals,
        "triple_variables": triples,
        "four_set_indicators": quads,
        "consistency_clauses": ax5,
        "parity_clauses": parity,
        "exclusion_clauses": exclusion,
        "hull_clauses": hull,
        "symmetry_clauses": symmetry,
    }


def clause_stream(
    n: int,
    k: int,
    layers: Sequence[int],
    offsets: Sequence[int],
    variables: Dict[Triple, int],
    ax5_mode: str,
    parity_mode: str = "one-sided",
    fix_reflection: bool = False,
    fix_extreme: bool = False,
) -> Iterator[Tuple[int, ...]]:
    triple_count = math.comb(n, 3)
    quads = list(itertools.combinations(range(n), 4))
    indicators = {quad: triple_count + index for index, quad in enumerate(quads, 1)}

    if ax5_mode == "signotope":
        for quad in quads:
            yield from signotope_clauses(quad, variables)
    elif ax5_mode == "signotope-prime":
        for quad in quads:
            yield from signotope_prime_clauses(quad, variables)
    elif ax5_mode == "signotope-direct":
        for quad in quads:
            yield from signotope_direct_clauses(quad, variables)
    elif ax5_mode == "reduced":
        yield from reduced_ax5_clauses(n, variables)
    elif ax5_mode == "full":
        yield from full_ax5_clauses(n, variables)
    elif ax5_mode != "none":
        raise ValueError(f"unknown ax5 mode: {ax5_mode}")
    for quad in quads:
        yield from parity_guard_clauses(
            quad,
            indicators[quad],
            variables,
            signotope_restricted=ax5_mode in (
                "signotope", "signotope-direct", "signotope-prime"
            ),
            equivalence=parity_mode != "one-sided",
            factored_reverse=parity_mode == "equivalence-factored",
        )
    for subset in itertools.combinations(range(n), k):
        yield tuple(indicators[quad] for quad in itertools.combinations(subset, 4))
    if layers:
        yield from hull_clauses(n, layers, offsets, variables)
    if fix_reflection:
        yield (variables[(0, 1, 2)],)
    if fix_extreme:
        for j, k in itertools.combinations(range(1, n), 2):
            yield (variables[(0, j, k)],)


def write_dimacs(path: Path, nvars: int, nclauses: int, clauses: Iterable[Tuple[int, ...]]) -> None:
    written = 0
    with path.open("w", encoding="ascii", buffering=1 << 20) as stream:
        stream.write("c parity-compressed Erdos-Szekeres refutation encoding\n")
        stream.write(f"p cnf {nvars} {nclauses}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)))
            stream.write(" 0\n")
            written += 1
    if written != nclauses:
        raise RuntimeError(f"header has {nclauses} clauses but wrote {written}")


def parse_list(value: str) -> Tuple[int, ...]:
    if not value.strip():
        return ()
    return tuple(int(item.strip()) for item in value.split(",") if item.strip())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--layers", default="")
    parser.add_argument("--offsets", default="")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--count-only", action="store_true")
    parser.add_argument(
        "--ax5-mode",
        choices=(
            "signotope",
            "signotope-prime",
            "signotope-direct",
            "reduced",
            "full",
            "none",
        ),
        default="signotope",
        help="orientation-consistency family; signotope is the recommended planar encoding",
    )
    parser.add_argument(
        "--fix-reflection",
        action="store_true",
        help="break global orientation reversal by requiring x_(0,1,2) to be true",
    )
    parser.add_argument(
        "--fix-extreme",
        action="store_true",
        help="normalize an extreme element 0 and its radial order by x_(0,j,k)=true",
    )
    parser.add_argument(
        "--parity-mode",
        choices=("one-sided", "equivalence", "equivalence-factored"),
        default="one-sided",
        help="one-sided guard, direct full equivalence, or ternary factored full equivalence",
    )
    args = parser.parse_args()

    if args.fix_reflection and args.fix_extreme:
        raise SystemExit("choose at most one of --fix-reflection and --fix-extreme")

    if not (4 <= args.k <= args.n):
        raise SystemExit("require 4 <= k <= n")
    layers = parse_list(args.layers)
    offsets = parse_list(args.offsets) if args.offsets else (0,) * len(layers)
    if len(layers) != len(offsets):
        raise SystemExit("layers and offsets must have equal length")
    if layers and (any(size < 3 for size in layers) or sum(layers) > args.n):
        raise SystemExit("layer sizes must be at least 3 and sum to at most n")
    for index, (size, offset) in enumerate(zip(layers, offsets)):
        if index and offset and not (1 <= offset < size):
            raise SystemExit("each nonzero inner-layer offset must lie inside its layer")

    result = counts(
        args.n,
        args.k,
        layers,
        offsets,
        args.ax5_mode,
        args.parity_mode,
        args.fix_reflection,
        args.fix_extreme,
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
        clause_stream(
            args.n,
            args.k,
            layers,
            offsets,
            variables,
            args.ax5_mode,
            args.parity_mode,
            args.fix_reflection,
            args.fix_extreme,
        ),
    )
    print(f"wrote={args.out}")


if __name__ == "__main__":
    main()
