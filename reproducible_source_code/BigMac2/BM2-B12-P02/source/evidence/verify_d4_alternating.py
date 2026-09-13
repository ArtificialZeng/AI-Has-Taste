#!/usr/bin/env python3
"""Exact certificate for the D4 alternating normal form of Delta.

Only integer 4-by-4 matrices and exhaustive finite Coxeter-group enumeration
are used. Letter convention:
    a = sigma'_0, b = sigma_0, c = sigma_1, d = sigma_2.
"""

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


N = 4
IDENTITY = tuple(tuple(int(i == j) for j in range(N)) for i in range(N))
MINUS_IDENTITY = tuple(
    tuple(-int(i == j) for j in range(N)) for i in range(N)
)

# A D4 simple-root system whose central root is c and whose leaves are a,b,d.
SIMPLE_ROOT = {
    "b": (1, -1, 0, 0),       # e1-e2
    "c": (0, 1, -1, 0),       # e2-e3
    "d": (0, 0, 1, -1),       # e3-e4
    "a": (0, 0, 1, 1),        # e3+e4
}


def matrix_product(left, right):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(N))
            for j in range(N)
        )
        for i in range(N)
    )


def matrix_vector(matrix, vector):
    return tuple(
        sum(matrix[i][k] * vector[k] for k in range(N))
        for i in range(N)
    )


def inverse(matrix):
    # All matrices below are orthogonal signed-permutation matrices.
    return tuple(tuple(matrix[j][i] for j in range(N)) for i in range(N))


def reflection(alpha):
    # Every D4 root has squared norm 2, so s_alpha(v)=v-(v.alpha)alpha.
    return tuple(
        tuple(int(i == j) - alpha[i] * alpha[j] for j in range(N))
        for i in range(N)
    )


GENERATOR = {letter: reflection(root) for letter, root in SIMPLE_ROOT.items()}

POSITIVE_ROOTS = []
for i in range(N):
    for j in range(i + 1, N):
        for second_sign in (1, -1):
            root = [0] * N
            root[i] = 1
            root[j] = second_sign
            POSITIVE_ROOTS.append(tuple(root))
POSITIVE_ROOT_SET = set(POSITIVE_ROOTS)
require(len(POSITIVE_ROOT_SET) == 12, "D4 must have twelve positive roots")


def root_sign(root):
    if root in POSITIVE_ROOT_SET:
        return 1
    if tuple(-entry for entry in root) in POSITIVE_ROOT_SET:
        return -1
    raise AssertionError(f"not a D4 root: {root}")


def coxeter_length(element):
    return sum(
        root_sign(matrix_vector(element, root)) < 0
        for root in POSITIVE_ROOTS
    )


def evaluate(word):
    element = IDENTITY
    for letter in word:
        require(letter in GENERATOR, f"unknown letter {letter!r}")
        element = matrix_product(element, GENERATOR[letter])
    return element


def enumerate_subgroup(letters):
    """Return element -> a shortest word, by breadth-first search."""
    words = {IDENTITY: ""}
    queue = deque([IDENTITY])
    while queue:
        element = queue.popleft()
        for letter in letters:
            product = matrix_product(element, GENERATOR[letter])
            if product not in words:
                words[product] = words[element] + letter
                queue.append(product)
    for element, word in words.items():
        require(coxeter_length(element) == len(word), "BFS word is not reduced")
    return words


# Verify the chosen representation has precisely the required Coxeter graph.
for letter in "abcd":
    require(
        matrix_product(GENERATOR[letter], GENERATOR[letter]) == IDENTITY,
        f"{letter} is not an involution",
    )
for leaf in "abd":
    left = evaluate(leaf + "c" + leaf)
    right = evaluate("c" + leaf + "c")
    require(left == right, f"missing length-three braid for {leaf},c")
for first, second in (("a", "b"), ("a", "d"), ("b", "d")):
    require(evaluate(first + second) == evaluate(second + first), "leaves do not commute")

whole_group = enumerate_subgroup("abcd")
require(len(whole_group) == 192, "generated group does not have order |W(D4)|=192")
longest_elements = [w for w in whole_group if coxeter_length(w) == 12]
require(longest_elements == [MINUS_IDENTITY], "-I is not the unique length-12 element")

SOURCE_WORD = "bacbacdcbacd"
TARGET_WORD = "dbcabcdcbaca"
source_element = evaluate(SOURCE_WORD)
target_element = evaluate(TARGET_WORD)
require(source_element == MINUS_IDENTITY, "source representative is not w0=-I")
require(target_element == source_element, "factorized representative is unequal to source")
for word_name, word in (("source", SOURCE_WORD), ("target", TARGET_WORD)):
    prefix_lengths = [coxeter_length(evaluate(word[:i])) for i in range(1, 13)]
    require(prefix_lengths == list(range(1, 13)), f"{word_name} word is not reduced")

# Each row says BEFORE = AFTER * TAIL. The alternating subsets are applied
# from right to left in the order J1,J2,J1,J2.
TAIL_ROWS = (
    ("ac", "dbcabcdcbaca", "dbcabcdcb", "aca"),
    ("bcd", "dbcabcdcb", "dbca", "bcdcb"),
    ("ac", "dbca", "db", "ca"),
    ("bcd", "db", "", "db"),
)

tail_report = []
for step, (letters, before_word, after_word, tail_word) in enumerate(TAIL_ROWS, 1):
    before = evaluate(before_word)
    after = evaluate(after_word)
    tail = evaluate(tail_word)
    require(
        matrix_product(after, tail) == before,
        f"factor equality fails at tail step {step}",
    )
    require(
        coxeter_length(after) + coxeter_length(tail) == coxeter_length(before),
        f"length additivity fails at tail step {step}",
    )
    require(coxeter_length(tail) == len(tail_word), f"tail {step} is not reduced")

    residual_images = {
        letter: matrix_vector(after, SIMPLE_ROOT[letter]) for letter in letters
    }
    require(
        all(root_sign(image) > 0 for image in residual_images.values()),
        f"residual has a right descent in J at step {step}",
    )

    parabolic = enumerate_subgroup(letters)
    right_suffixes = {}
    for suffix, suffix_word in parabolic.items():
        quotient = matrix_product(before, inverse(suffix))
        if (
            coxeter_length(quotient) + coxeter_length(suffix)
            == coxeter_length(before)
        ):
            right_suffixes[suffix] = suffix_word
    require(tail in right_suffixes, f"proposed tail is not a right suffix at step {step}")

    # Exhaustively certify greatestness: every parabolic reduced suffix x of
    # BEFORE is itself a reduced right suffix of TAIL.
    for suffix in right_suffixes:
        quotient = matrix_product(tail, inverse(suffix))
        require(quotient in parabolic, "tail quotient left the parabolic subgroup")
        require(
            coxeter_length(quotient) + coxeter_length(suffix)
            == coxeter_length(tail),
            f"a competing suffix does not right-divide tail at step {step}",
        )

    greatest = []
    for candidate in right_suffixes:
        if all(
            coxeter_length(matrix_product(candidate, inverse(suffix)))
            + coxeter_length(suffix)
            == coxeter_length(candidate)
            for suffix in right_suffixes
        ):
            greatest.append(candidate)
    require(greatest == [tail], f"tail step {step} lacks a unique greatest suffix")

    histogram = Counter(coxeter_length(suffix) for suffix in right_suffixes)
    tail_report.append(
        {
            "step": step,
            "J": letters,
            "before_length": coxeter_length(before),
            "tail_word": tail_word,
            "tail_length": coxeter_length(tail),
            "after_word": after_word or "1",
            "after_length": coxeter_length(after),
            "residual_simple_root_images": residual_images,
            "parabolic_order": len(parabolic),
            "right_suffix_count": len(right_suffixes),
            "right_suffix_length_histogram": dict(sorted(histogram.items())),
        }
    )

LEFTMOST_WORD = "db"
leftmost = evaluate(LEFTMOST_WORD)
left_descents = [
    letter
    for letter in "abcd"
    if coxeter_length(matrix_product(GENERATOR[letter], leftmost))
    < coxeter_length(leftmost)
]
require(left_descents == ["b", "d"], "leftmost factor has incorrect left descents")

project_dir = Path(__file__).resolve().parents[1]
source_hash = sha256((project_dir / "source.md").read_bytes()).hexdigest()
EXPECTED_SOURCE_HASH = "68c77ce76e18be01e19e9c878d344f7d933fcdb187acd250853f21610efae2ff"
require(source_hash == EXPECTED_SOURCE_HASH, "immutable source.md changed")

report = {
    "arithmetic": "exact integer root matrices; exhaustive finite enumeration",
    "source_md_sha256": source_hash,
    "coxeter_group_order": len(whole_group),
    "positive_root_count": len(POSITIVE_ROOTS),
    "source_word": SOURCE_WORD,
    "factorized_word": TARGET_WORD,
    "longest_element_matrix": MINUS_IDENTITY,
    "tails": tail_report,
    "alternating_factors_left_to_right": ["db", "ca", "bcdcb", "aca"],
    "left_descents_of_leftmost_factor": left_descents,
}
print(json.dumps(report, indent=2, sort_keys=True))
print("PASS: exact D4 alternating-tail and left-divisor certificate")
