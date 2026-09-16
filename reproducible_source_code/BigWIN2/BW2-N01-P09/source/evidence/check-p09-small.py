#!/usr/bin/env python3
"""Bounded exact SC229 intake check, not an all-arity proof.

Two exhaustive function evaluators: literal ternary operation through n=5,
and integer truth masks through n=6. All ordered disjoint root splits cover
every permutation/bracketing. Separately compare two proposed species counts.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
from fractions import Fraction

TABLE = ((0, 0, 0), (1, 0, 1), (1, 1, 1))


def ordered_splits(mask):
    left = (mask - 1) & mask
    while left:
        yield left, mask ^ left
        left = (left - 1) & mask


def bitmap(values):
    return sum(1 << i for i, value in enumerate(values) if value == 1)


def mask_functions(n):
    assignments = list(itertools.product(range(3), repeat=n))
    all_bits = (1 << len(assignments)) - 1
    one = [bitmap(a[i] for a in assignments) for i in range(n)]
    two = [bitmap(int(a[i] == 2) for a in assignments) for i in range(n)]
    sets = {1 << i: {one[i]} for i in range(n)}
    evaluations = 0
    for size in range(2, n + 1):
        for mask in range(1, 1 << n):
            if mask.bit_count() != size:
                continue
            found = set()
            for left, right in ordered_splits(mask):
                for f in sets[left]:
                    for g in sets[right]:
                        value = f & (all_bits ^ g)
                        if left.bit_count() == 1:
                            value |= two[left.bit_length() - 1]
                        found.add(value)
                        evaluations += 1
            sets[mask] = found
    return sets, assignments, evaluations


def literal_functions(n, assignments):
    sets = {1 << i: {tuple(a[i] for a in assignments)} for i in range(n)}
    for size in range(2, n + 1):
        for mask in range(1, 1 << n):
            if mask.bit_count() != size:
                continue
            found = set()
            for left, right in ordered_splits(mask):
                for f in sets[left]:
                    for g in sets[right]:
                        found.add(tuple(TABLE[a][b] for a, b in zip(f, g)))
            sets[mask] = found
    return sets


def lagrange_count(n):
    coefficient = sum(
        Fraction(math.comb(n, k) * k ** (n - 1 - k), math.factorial(n - 1 - k))
        for k in range(n)
    )
    value = math.factorial(n - 1) * coefficient
    assert value.denominator == 1
    return int(value)


def species_series_counts(limit):
    # T=x(1+T exp(T)), independently expanded in exact formal series.
    t = [Fraction(0)] * (limit + 1)
    t[1] = Fraction(1)
    for n in range(2, limit + 1):
        exponential = [Fraction(0)] * n
        exponential[0] = Fraction(1)
        for degree in range(1, n):
            exponential[degree] = sum(
                i * t[i] * exponential[degree - i]
                for i in range(1, degree + 1)
            ) / degree
        t[n] = sum(t[i] * exponential[n - 1 - i] for i in range(1, n))
    return [int(t[n] * math.factorial(n)) for n in range(1, limit + 1)]


def main():
    rows = []
    total_literal_assignment_cells = 0
    for n in range(1, 7):
        masks, assignments, evaluations = mask_functions(n)
        if n <= 5:
            literal = literal_functions(n, assignments)
            for support, functions in literal.items():
                normalized = {bitmap(f) for f in functions}
                assert normalized == masks[support], (n, support)
                total_literal_assignment_cells += len(functions) * len(assignments)
        values = masks[(1 << n) - 1]
        count = len(values)
        assert count == lagrange_count(n), (n, count, lagrange_count(n))
        digest = hashlib.sha256(
            ("\n".join(format(v, "x") for v in sorted(values)) + "\n").encode()
        ).hexdigest()
        rows.append({"n": n, "distinct_functions": count,
                     "assignments_per_function": 3 ** n,
                     "mask_compositions": evaluations,
                     "literal_all_supports_agree": True if n <= 5 else None,
                     "truth_set_sha256": digest})
    proposed = species_series_counts(12)
    assert proposed == [lagrange_count(n) for n in range(1, 13)]
    assert proposed[:5] == [1, 2, 12, 108, 1340]
    result = {
        "schema": 1, "python": platform.python_version(), "table": TABLE,
        "randomness": "none", "arithmetic": "integers and exact rational formal series",
        "rows": rows, "literal_assignment_cells_checked": total_literal_assignment_cells,
        "proposed_egf": "T=x*(1+T*exp(T))",
        "proposed_counts_n1_to_12": proposed,
        "scope": "Exhaustive functions n<=6; independent literal-table comparison n<=5. Two formal-series formulas agree through n=12. Neither finite agreement nor a guessed species proves all-n term-function injectivity.",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_name("p09-intake-check.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
