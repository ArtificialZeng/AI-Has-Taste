#!/usr/bin/env python3
"""Standalone exact verifier for the length-26 3-out-of-5 word."""

from itertools import combinations


WORD = (
    1, 2, 3, 4, -1, -2, -3, -4, 5,
    2, 1, 4, 3, -4, -3, -2, -1,
    3, 4, 1, 2, -4, -3, -2, -1, -5,
)


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def delete(word, removed):
    removed = frozenset(removed)
    return reduce_word(letter for letter in word if abs(letter) not in removed)


assert len(WORD) == 26
assert reduce_word(WORD) == WORD

three_deletions = {
    subset: delete(WORD, subset) for subset in combinations(range(1, 6), 3)
}
two_deletions = {
    subset: delete(WORD, subset) for subset in combinations(range(1, 6), 2)
}

assert len(three_deletions) == 10
assert all(residual == () for residual in three_deletions.values())
assert len(two_deletions) == 10
assert all(residual != () for residual in two_deletions.values())

print("reduced_length =", len(WORD))
for subset, residual in three_deletions.items():
    print("delete", subset, "->", residual)
for subset, residual in two_deletions.items():
    print("delete", subset, "->", residual)
print("VERIFIED: length-26 3-out-of-5 solution")
