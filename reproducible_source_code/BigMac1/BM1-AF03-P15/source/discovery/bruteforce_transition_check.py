#!/usr/bin/env python3
"""Independent small-n check of the signed-cycle orbit model.

This program deliberately does not import ``orbit_lp``.  It enumerates every
even signed permutation, every D_n reflection, and every upward absolute cover,
then compares the observed orbit sizes and transition support with the closed
signed-cycle formulas used by the quotient construction.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import Counter, defaultdict
from typing import Iterable, Tuple


CycleType = Tuple[Tuple[int, ...], Tuple[int, ...]]


def signed_permutations(n: int) -> Iterable[Tuple[int, ...]]:
    for permutation in itertools.permutations(range(1, n + 1)):
        for negative_positions in itertools.product((1, -1), repeat=n - 1):
            final_sign = math.prod(negative_positions)
            signs = negative_positions + (final_sign,)
            yield tuple(signs[i] * permutation[i] for i in range(n))


def reflections(n: int) -> Iterable[Tuple[int, ...]]:
    identity = list(range(1, n + 1))
    for i in range(n):
        for j in range(i + 1, n):
            for sign in (1, -1):
                reflection = identity.copy()
                reflection[i] = sign * (j + 1)
                reflection[j] = sign * (i + 1)
                yield tuple(reflection)


def apply(element: Tuple[int, ...], signed_index: int) -> int:
    value = element[abs(signed_index) - 1]
    return value if signed_index > 0 else -value


def compose(left: Tuple[int, ...], right: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(apply(left, value) for value in right)


def cycle_type(element: Tuple[int, ...]) -> CycleType:
    n = len(element)
    seen = [False] * n
    positive = []
    negative = []
    for start in range(n):
        if seen[start]:
            continue
        current = start
        length = 0
        sign_product = 1
        while not seen[current]:
            seen[current] = True
            image = element[current]
            sign_product *= 1 if image > 0 else -1
            current = abs(image) - 1
            length += 1
        (positive if sign_product == 1 else negative).append(length)
    return tuple(sorted(positive, reverse=True)), tuple(sorted(negative, reverse=True))


def reflection_length(element: Tuple[int, ...]) -> int:
    positive, negative = cycle_type(element)
    return len(element) - len(positive)


def z(partition: Tuple[int, ...]) -> int:
    multiplicities = Counter(partition)
    value = 1
    for part, multiplicity in multiplicities.items():
        value *= part**multiplicity * math.factorial(multiplicity)
    return value


def predicted_size(n: int, value: CycleType) -> int:
    positive, negative = value
    return (
        2**n
        * math.factorial(n)
        // (2 ** (len(positive) + len(negative)) * z(positive) * z(negative))
    )


def predicted_upper_counts(value: CycleType) -> dict[CycleType, int]:
    positive, negative = value
    positive_multiplicities = Counter(positive)
    negative_multiplicities = Counter(negative)
    ans: dict[CycleType, int] = defaultdict(int)

    positive_lengths = sorted(positive_multiplicities)
    for position, left in enumerate(positive_lengths):
        for right in positive_lengths[position:]:
            if left == right and positive_multiplicities[left] < 2:
                continue
            p = list(positive)
            p.remove(left)
            p.remove(right)
            p.append(left + right)
            target = tuple(sorted(p, reverse=True)), negative
            if left == right:
                degree = left * left * positive_multiplicities[left] * (
                    positive_multiplicities[left] - 1
                )
            else:
                degree = (
                    2
                    * left
                    * right
                    * positive_multiplicities[left]
                    * positive_multiplicities[right]
                )
            ans[target] += degree

    for left, left_multiplicity in positive_multiplicities.items():
        for right, right_multiplicity in negative_multiplicities.items():
            p = list(positive)
            q = list(negative)
            p.remove(left)
            q.remove(right)
            q.append(left + right)
            target = tuple(sorted(p, reverse=True)), tuple(sorted(q, reverse=True))
            ans[target] += 2 * left * right * left_multiplicity * right_multiplicity

    for total, multiplicity in positive_multiplicities.items():
        for left in range(1, total // 2 + 1):
            right = total - left
            p = list(positive)
            p.remove(total)
            q = list(negative) + [left, right]
            target = tuple(sorted(p, reverse=True)), tuple(sorted(q, reverse=True))
            cuts_per_cycle = total if left < right else left
            ans[target] += cuts_per_cycle * multiplicity
    return dict(ans)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?", default=5)
    args = parser.parse_args()
    if not 2 <= args.n <= 7:
        parser.error("this brute-force check is intended for 2 <= n <= 7")

    observed_sizes: Counter[CycleType] = Counter()
    observed_upper: dict[CycleType, set[CycleType]] = defaultdict(set)
    observed_edge_counts: Counter[Tuple[CycleType, CycleType]] = Counter()
    reflection_list = list(reflections(args.n))
    element_count = 0
    upward_edge_count = 0
    for element in signed_permutations(args.n):
        element_count += 1
        source_type = cycle_type(element)
        observed_sizes[source_type] += 1
        source_rank = reflection_length(element)
        for reflection in reflection_list:
            target = compose(element, reflection)
            if reflection_length(target) == source_rank + 1:
                upward_edge_count += 1
                target_type = cycle_type(target)
                observed_upper[source_type].add(target_type)
                observed_edge_counts[(source_type, target_type)] += 1

    assert element_count == 2 ** (args.n - 1) * math.factorial(args.n)
    for value, size in observed_sizes.items():
        assert len(value[1]) % 2 == 0
        assert size == predicted_size(args.n, value), (value, size, predicted_size(args.n, value))
        predicted_counts = predicted_upper_counts(value)
        assert observed_upper[value] == set(predicted_counts), (
            value,
            observed_upper[value] - set(predicted_counts),
            set(predicted_counts) - observed_upper[value],
        )
        for target, source_degree in predicted_counts.items():
            assert observed_edge_counts[(value, target)] == size * source_degree, (
                value,
                target,
                observed_edge_counts[(value, target)],
                size * source_degree,
            )
    print(
        {
            "n": args.n,
            "elements": element_count,
            "reflections": len(reflection_list),
            "upward_directed_edges": upward_edge_count,
            "orbit_types": len(observed_sizes),
            "transition_support_verified": True,
            "transition_multiplicities_verified": True,
            "class_sizes_verified": True,
        }
    )


if __name__ == "__main__":
    main()
