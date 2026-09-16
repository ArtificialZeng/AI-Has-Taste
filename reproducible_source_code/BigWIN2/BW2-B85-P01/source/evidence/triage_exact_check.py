#!/usr/bin/env python3
"""Exact, dependency-free triage checks for the four displayed stabilizers.

This is discovery/triage evidence, not an independent referee certificate.
Paulis are represented exactly as i^p X^x Z^z, with p modulo 4.
"""

from collections import Counter
from itertools import permutations


CASES = {
    "S_A": ("ZZZZI", "XXIIX", "IIXXX"),
    "S_B": ("ZZIZX", "XIZXI", "IXXYI"),
    "S_+": ("XXIIXX", "IIXXXX", "ZZZZIX"),
    "S_-": ("XXZXII", "ZZXYII", "IZZZXX"),
}
PAULI = {
    "I": (0, 0, 0),
    "X": (1, 0, 0),
    "Z": (0, 1, 0),
    "Y": (1, 1, 1),  # Y = i X Z
}
LETTER = {(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}


def parse(word):
    x = z = phase = 0
    for j, letter in enumerate(word):
        xb, zb, pb = PAULI[letter]
        x |= xb << j
        z |= zb << j
        phase += pb
    return x, z, phase % 4


def multiply(left, right):
    """Multiply exact Paulis in the i^p X^x Z^z convention."""
    x, z, p = left
    u, v, q = right
    return x ^ u, z ^ v, (p + q + 2 * ((z & u).bit_count())) % 4


def symplectic(left, right):
    x, z, _ = left
    u, v, _ = right
    return ((x & v).bit_count() + (z & u).bit_count()) % 2


def binary_rank(rows):
    rows = list(rows)
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        rank += 1
        bit = 1 << (pivot.bit_length() - 1)
        rows = [row ^ pivot if row & bit else row for row in rows if row != pivot]
    return rank


def subgroup(words):
    generators = tuple(parse(word) for word in words)
    elements = []
    for selector in range(1 << len(generators)):
        value = (0, 0, 0)
        for j, generator in enumerate(generators):
            if selector >> j & 1:
                value = multiply(value, generator)
        elements.append((selector, value))
    return generators, elements


def display_pauli(value, n):
    x, z, phase = value
    word = "".join(LETTER[(x >> j & 1, z >> j & 1)] for j in range(n))
    relative_phase = (phase - word.count("Y")) % 4
    assert relative_phase in (0, 2)
    return ("+" if relative_phase == 0 else "-") + word


def support(value):
    return value[0] | value[1]


def subset(mask, n):
    return "{" + ",".join(str(j + 1) for j in range(n) if mask >> j & 1) + "}"


def support_dimension_profile(elements, n):
    """Return d(A)=dim_F2{g in S: supp(g) subset A} for every A."""
    supports = [support(value) for _, value in elements]
    profile = {}
    for mask in range(1 << n):
        count = sum((item & ~mask) == 0 for item in supports)
        assert count > 0 and count & (count - 1) == 0
        profile[mask] = count.bit_length() - 1
    return profile


def permute_mask(mask, permutation):
    return sum(((mask >> j) & 1) << permutation[j] for j in range(len(permutation)))


def coordinating_permutations(left, right, n):
    return [
        permutation
        for permutation in permutations(range(n))
        if all(left[mask] == right[permute_mask(mask, permutation)] for mask in left)
    ]


def main():
    data = {}
    for name, words in CASES.items():
        n = len(words[0])
        generators, elements = subgroup(words)
        commute = all(symplectic(a, b) == 0 for a in generators for b in generators)
        rank = binary_rank(x | (z << n) for x, z, _ in generators)
        distinct = len({(x, z, p) for _, (x, z, p) in elements})
        assert commute and rank == 3 and distinct == 8
        profile = support_dimension_profile(elements, n)
        data[name] = (n, elements, profile)
        print(f"[{name}] commute={commute} binary_rank={rank} group_size={distinct}")
        for selector, value in elements:
            print(
                f"  {selector:03b} {display_pauli(value, n)} "
                f"support={subset(support(value), n)}"
            )

    for left_name, right_name in (("S_A", "S_B"), ("S_+", "S_-")):
        n, _, left = data[left_name]
        _, _, right = data[right_name]
        print(f"[{left_name} versus {right_name}]")
        for size in range(n + 1):
            left_hist = Counter(left[m] for m in left if m.bit_count() == size)
            right_hist = Counter(right[m] for m in right if m.bit_count() == size)
            print(
                f"  |A|={size}: left={dict(sorted(left_hist.items()))} "
                f"right={dict(sorted(right_hist.items()))}"
            )
        matches = coordinating_permutations(left, right, n)
        print(f"  coordinating_permutations={len(matches)}")
        assert not matches

    n, _, left5 = data["S_A"]
    _, _, right5 = data["S_B"]
    exceptional_left = [m for m, d in left5.items() if m.bit_count() == 3 and d == 1]
    exceptional_right = [m for m, d in right5.items() if m.bit_count() == 3 and d == 1]
    assert len(exceptional_left) == len(exceptional_right) == 2
    left_intersection = (exceptional_left[0] & exceptional_left[1]).bit_count()
    right_intersection = (exceptional_right[0] & exceptional_right[1]).bit_count()
    assert (left_intersection, right_intersection) == (1, 2)
    print(
        "[five-qubit certificate] d(A)=1 exceptional triples: "
        f"left={[subset(m, n) for m in exceptional_left]}, "
        f"intersection={left_intersection}; "
        f"right={[subset(m, n) for m in exceptional_right]}, "
        f"intersection={right_intersection}"
    )

    n, _, left6 = data["S_+"]
    _, _, right6 = data["S_-"]
    left_hist4 = Counter(left6[m] for m in left6 if m.bit_count() == 4)
    right_hist4 = Counter(right6[m] for m in right6 if m.bit_count() == 4)
    assert left_hist4 == Counter({0: 12, 1: 3})
    assert right_hist4 == Counter({0: 14, 2: 1})
    print(
        "[six-qubit certificate] |A|=4 d-histograms: "
        f"left={dict(sorted(left_hist4.items()))}; "
        f"right={dict(sorted(right_hist4.items()))}"
    )


if __name__ == "__main__":
    main()
