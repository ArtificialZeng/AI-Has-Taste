#!/usr/bin/env python3
"""Fresh D4 check using signed permutations, independent of the candidate matrices."""

from collections import deque
from itertools import permutations, product


# A signed permutation w=(w_1,...,w_4) means w(e_i)=sgn(w_i)e_|w_i|.
IDENTITY = (1, 2, 3, 4)
GENERATORS = {
    "b": (2, 1, 3, 4),
    "c": (1, 3, 2, 4),
    "d": (1, 2, 4, 3),
    "a": (1, 2, -4, -3),
}


def compose(left, right):
    """Return left after right."""
    answer = []
    for value in right:
        image = left[abs(value) - 1]
        answer.append(image if value > 0 else -image)
    return tuple(answer)


def inverse(w):
    answer = [0] * 4
    for i, value in enumerate(w, 1):
        answer[abs(value) - 1] = i if value > 0 else -i
    return tuple(answer)


def evaluate(word):
    w = IDENTITY
    for letter in word:
        w = compose(w, GENERATORS[letter])
    return w


def act(w, root):
    result = [0] * 4
    for i, coefficient in enumerate(root):
        if coefficient:
            image = w[i]
            result[abs(image) - 1] += coefficient * (1 if image > 0 else -1)
    return tuple(result)


POSITIVE_ROOTS = []
for i in range(4):
    for j in range(i + 1, 4):
        for sign in (-1, 1):
            root = [0] * 4
            root[i], root[j] = 1, sign
            POSITIVE_ROOTS.append(tuple(root))


def is_negative(root):
    first = next(entry for entry in root if entry)
    return first < 0


def length(w):
    return sum(is_negative(act(w, root)) for root in POSITIVE_ROOTS)


def subgroup(letters):
    found = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        w = queue.popleft()
        for letter in letters:
            candidate = compose(w, GENERATORS[letter])
            if candidate not in found:
                found.add(candidate)
                queue.append(candidate)
    return found


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


whole_group = {
    tuple(signs[i] * permutation[i] for i in range(4))
    for permutation in permutations((1, 2, 3, 4))
    for signs in product((-1, 1), repeat=4)
    if signs.count(-1) % 2 == 0
}
assert_true(len(whole_group) == 192, "direct W(D4) enumeration has wrong order")
assert_true(subgroup("abcd") == whole_group, "simple reflections do not generate W(D4)")

source = "bacbacdcbacd"
factorized = "dbcabcdcbaca"
w0 = (-1, -2, -3, -4)
assert_true(evaluate(source) == w0 == evaluate(factorized), "the two Delta words differ")
assert_true([length(evaluate(source[:i])) for i in range(13)] == list(range(13)),
            "source Delta word is not reduced")
assert_true([length(evaluate(factorized[:i])) for i in range(13)] == list(range(13)),
            "factorized Delta word is not reduced")
assert_true(max(map(length, whole_group)) == 12 and length(w0) == 12,
            "the common element is not longest")

rows = (
    ("ac", "dbcabcdcbaca", "dbcabcdcb", "aca"),
    ("bcd", "dbcabcdcb", "dbca", "bcdcb"),
    ("ac", "dbca", "db", "ca"),
    ("bcd", "db", "", "db"),
)
suffix_counts = []
for index, (letters, before_word, residual_word, tail_word) in enumerate(rows, 1):
    before, residual, tail = map(evaluate, (before_word, residual_word, tail_word))
    assert_true(compose(residual, tail) == before, f"factorization fails at row {index}")
    assert_true(length(residual) + length(tail) == length(before),
                f"non-reduced factorization at row {index}")
    parabolic = subgroup(letters)
    suffixes = {
        x for x in parabolic
        if length(compose(before, inverse(x))) + length(x) == length(before)
    }
    assert_true(tail in suffixes, f"tail is not a suffix at row {index}")
    for x in suffixes:
        quotient = compose(tail, inverse(x))
        assert_true(quotient in parabolic, f"parabolic containment fails at row {index}")
        assert_true(length(quotient) + length(x) == length(tail),
                    f"tail is not greatest at row {index}")
    suffix_counts.append(len(suffixes))

leftmost = evaluate("db")
left_descents = sorted(
    letter for letter, generator in GENERATORS.items()
    if length(compose(generator, leftmost)) < length(leftmost)
)
assert_true(left_descents == ["b", "d"], "wrong left descent set")

for generator in GENERATORS.values():
    assert_true(compose(w0, generator) == compose(generator, w0), "w0 is not central")

commutes_with_ac = sorted(
    x for x, gx in GENERATORS.items()
    if all(compose(gx, GENERATORS[y]) == compose(GENERATORS[y], gx) for y in "ac")
)
assert_true(commutes_with_ac == [], "S1-perp is not empty")

print({
    "group_order": len(whole_group),
    "longest_length": length(w0),
    "tail_suffix_counts": suffix_counts,
    "alternating_factors": ["db", "ca", "bcdcb", "aca"],
    "left_descents": left_descents,
    "S1_perp": commutes_with_ac,
})
print("PASS: independent signed-permutation reconstruction")
