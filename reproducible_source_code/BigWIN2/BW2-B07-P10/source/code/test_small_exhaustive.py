#!/usr/bin/env python3
"""Small exhaustive attacks on the Burnside and ideal-count lemmas."""

import itertools
import math


P = [1, 1, 3, 19, 219, 4231]


def integer_partitions(n: int, cap: int):
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def labeled_posets(n: int):
    pairs = list(itertools.combinations(range(n), 2))
    for states in itertools.product(range(3), repeat=len(pairs)):
        less = [0] * n
        for (i, j), state in zip(pairs, states):
            if state == 1:
                less[i] |= 1 << j
            elif state == 2:
                less[j] |= 1 << i
        transitive = True
        for i in range(n):
            for j in range(n):
                if less[i] >> j & 1 and less[j] & ~less[i]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            yield tuple(less)


def canonical_permutation(lengths: tuple[int, ...]) -> tuple[int, ...]:
    permutation = []
    start = 0
    for length in lengths:
        cycle = list(range(start, start + length))
        image = {cycle[i]: cycle[(i + 1) % length] for i in range(length)}
        permutation.extend(image[x] for x in cycle)
        start += length
    return tuple(permutation)


def fixed(poset: tuple[int, ...], permutation: tuple[int, ...]) -> bool:
    n = len(poset)
    for i in range(n):
        for j in range(n):
            if ((poset[i] >> j) & 1) != ((poset[permutation[i]] >> permutation[j]) & 1):
                return False
    return True


def path_sum(lengths: tuple[int, ...]) -> int:
    answer = 0
    for order in itertools.permutations(range(len(lengths))):
        product = 1
        for i, j in zip(order, order[1:]):
            product *= 2 ** math.gcd(lengths[i], lengths[j]) - 1
        answer += product
    return answer


def matchings(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first, *tail = vertices
    yield from matchings(tuple(tail))
    for position, second in enumerate(tail):
        rest = tuple(tail[:position] + tail[position + 1 :])
        for matching in matchings(rest):
            yield ((first, second),) + matching


def construction_lower(lengths: tuple[int, ...]) -> int:
    r = len(lengths)
    answer = P[r] + path_sum(lengths) - math.factorial(r)
    if r != 2:
        for matching in matchings(tuple(range(r))):
            if not matching:
                continue
            product = P[r - 2 * len(matching)]
            for i, j in matching:
                product *= 2 * (2 ** math.gcd(lengths[i], lengths[j]) - 2)
            answer += product
    return answer


def number_ideals(poset: tuple[int, ...]) -> int:
    n = len(poset)
    predecessor = [0] * n
    relations = 0
    for i in range(n):
        for j in range(n):
            if poset[i] >> j & 1:
                predecessor[j] |= 1 << i
                relations += 1
    count = 0
    for subset in range(1 << n):
        count += all(not (subset >> j & 1) or predecessor[j] & ~subset == 0 for j in range(n))
    return count, relations


def colex_bound(n: int, relations: int) -> int:
    edges = n * (n - 1) // 2 - relations
    a = max(x for x in range(n + 1) if x * (x - 1) // 2 <= edges)
    if a == n:
        return 1 << n
    b = edges - a * (a - 1) // 2
    return (1 << a) + (1 << b) + n - a - 1


def main() -> None:
    for n in range(1, 6):
        posets = list(labeled_posets(n))
        if len(posets) != P[n]:
            raise SystemExit(f"TEST FAILED: P({n})={len(posets)}")
        for poset in posets:
            ideals, relations = number_ideals(poset)
            if ideals > colex_bound(n, relations):
                raise SystemExit("TEST FAILED: colex ideal bound")
        for cycle_type in integer_partitions(n, n):
            permutation = canonical_permutation(cycle_type)
            exact = sum(fixed(poset, permutation) for poset in posets)
            lower = construction_lower(cycle_type)
            if lower > exact:
                raise SystemExit(
                    f"TEST FAILED: n={n}, type={cycle_type}, lower={lower}, exact={exact}"
                )
    print("TEST PASSED: all labeled posets through n=5 satisfy both structural bounds")


if __name__ == "__main__":
    main()
