#!/usr/bin/env python3
"""Exact exhaustive triage check for the frozen 21435 statement.

For each integer partition of N <= 9, this enumerates every distinct ordering
of its positive parts and, whenever five distinct ranks are available, every
multiset permutation for that content.  The remaining cases are settled by the
strict-inequality observation.  It compares the full occurrence-distribution
polynomials within each coordinate orbit.  No random or floating-point
computation is used.
"""

from collections import Counter
from math import factorial


def integer_partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    if ceiling is None or ceiling > n:
        ceiling = n
    for first in range(ceiling, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def distinct_coordinate_orders(parts):
    counts = Counter(parts)
    out = [0] * len(parts)

    def visit(pos):
        if pos == len(out):
            yield tuple(out)
            return
        for value in sorted(counts):
            if counts[value]:
                counts[value] -= 1
                out[pos] = value
                yield from visit(pos + 1)
                counts[value] += 1

    yield from visit(0)


def distribution(alpha):
    """Return (coefficient tuple, number of generated words)."""
    remaining = list(alpha)
    word = []
    coeff = Counter()
    generated = 0

    def visit(occurrences):
        nonlocal generated
        if len(word) == sum(alpha):
            coeff[occurrences] += 1
            generated += 1
            return
        for letter, left in enumerate(remaining, start=1):
            if not left:
                continue
            remaining[letter - 1] -= 1
            word.append(letter)
            added = 0
            if len(word) >= 5:
                a, b, c, d, e = word[-5:]
                added = int(b < a < d < c < e)
            visit(occurrences + added)
            word.pop()
            remaining[letter - 1] += 1

    visit(0)
    expected = factorial(sum(alpha))
    for part in alpha:
        expected //= factorial(part)
    assert generated == expected
    degree = max(coeff, default=0)
    return tuple(coeff[i] for i in range(degree + 1)), generated


def main():
    summary = {}
    unstable = []
    rank_polynomials = {}
    for n in range(1, 10):
        types = assignments = words = 0
        for parts in integer_partitions(n):
            types += 1
            distributions = {}
            for alpha in distinct_coordinate_orders(parts):
                assignments += 1
                # With fewer than five letter values, strict 21435 occurrences
                # are impossible, so the distribution is known without listing
                # every word.  Its constant coefficient is the multinomial.
                if len(alpha) < 5 or n < 5:
                    total = factorial(n)
                    for part in alpha:
                        total //= factorial(part)
                    poly, generated = (total,), 0
                else:
                    poly, generated = distribution(alpha)
                words += generated
                distributions.setdefault(poly, []).append(alpha)
                if n == 9 and sorted(alpha, reverse=True) == [2] + [1] * 7:
                    repeated_rank = alpha.index(2) + 1
                    rank_polynomials[repeated_rank] = poly
            if len(distributions) > 1:
                unstable.append({
                    "N": n,
                    "type": parts,
                    "classes": distributions,
                })
        summary[n] = {
            "unordered_types": types,
            "ordered_contents": assignments,
            "explicit_words": words,
        }

    print("coverage", summary)
    print("unstable_types", [(x["N"], x["type"]) for x in unstable])
    print("rank_polynomials", dict(sorted(rank_polynomials.items())))
    for item in unstable:
        print("unstable_detail", item)


if __name__ == "__main__":
    main()
