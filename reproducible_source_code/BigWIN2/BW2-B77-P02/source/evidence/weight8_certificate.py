#!/usr/bin/env python3
"""Exact/modular certificate search for formal qMZV injectivity through weight 8.

All combinatorial coefficients are computed over Z.  A rank reported modulo a
prime is a rigorous lower bound for the corresponding rank over Q, since the
displayed modular minor lifts to an integer minor not divisible by that prime.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path

import numpy as np
from flint import nmod_mat
from numba import njit


MAX_WEIGHT = 8
PRIME = 1_000_003


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def weight(word: tuple[int, ...]) -> int:
    return sum(max(s, 1) for s in word)


def later_words(total: int) -> list[tuple[int, ...]]:
    """All (possibly empty) tails of exact weight ``total``."""
    if total == 0:
        return [()]
    ans: list[tuple[int, ...]] = []
    for letter_weight in range(1, total + 1):
        letters = (0, 1) if letter_weight == 1 else (letter_weight,)
        for s in letters:
            for tail in later_words(total - letter_weight):
                ans.append((s,) + tail)
    return ans


@lru_cache(maxsize=None)
def exact_words(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    ans: list[tuple[int, ...]] = []
    for first in range(1, total + 1):
        for tail in later_words(total - first):
            ans.append((first,) + tail)
    return tuple(ans)


def all_words(max_weight: int = MAX_WEIGHT) -> list[tuple[int, ...]]:
    return [u for w in range(max_weight + 1) for u in exact_words(w)]


def tau(word: tuple[int, ...]) -> tuple[int, ...]:
    if not word:
        return ()
    bits: list[int] = []
    for s in word:
        bits.extend([1] * s)
        bits.append(0)
    dual_bits = [1 - bit for bit in reversed(bits)]
    ans: list[int] = []
    run = 0
    for bit in dual_bits:
        if bit:
            run += 1
        else:
            ans.append(run)
            run = 0
    assert run == 0 and ans and ans[0] >= 1
    dual = tuple(ans)
    assert weight(dual) == weight(word)
    return dual


@lru_cache(maxsize=None)
def quasi_shuffle(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[tuple[tuple[int, ...], int], ...]:
    """Return the stuffle product as a sorted tuple of (word, coefficient)."""
    if not left:
        return ((right, 1),)
    if not right:
        return ((left, 1),)
    a, u = left[0], left[1:]
    b, v = right[0], right[1:]
    out: Counter[tuple[int, ...]] = Counter()
    for tail, c in quasi_shuffle(u, right):
        out[(a,) + tail] += c
    for tail, c in quasi_shuffle(left, v):
        out[(b,) + tail] += c
    for tail, c in quasi_shuffle(u, v):
        out[(a + b,) + tail] += c
    return tuple(sorted(out.items()))


def ideal_rows(words: list[tuple[int, ...]]) -> list[dict[int, int]]:
    """Rows v*(tau(u)-u), with wt(u)+wt(v)<=8, omitting zero rows."""
    index = {u: i for i, u in enumerate(words)}
    by_weight = {w: list(exact_words(w)) for w in range(MAX_WEIGHT + 1)}
    rows: list[dict[int, int]] = []
    for wu in range(1, MAX_WEIGHT + 1):
        for u in by_weight[wu]:
            tu = tau(u)
            if tu == u:
                continue
            for wv in range(MAX_WEIGHT - wu + 1):
                for v in by_weight[wv]:
                    row: Counter[int] = Counter()
                    for term, c in quasi_shuffle(v, tu):
                        assert weight(term) <= MAX_WEIGHT
                        row[index[term]] += c
                    for term, c in quasi_shuffle(v, u):
                        assert weight(term) <= MAX_WEIGHT
                        row[index[term]] -= c
                    clean = {j: c for j, c in row.items() if c}
                    if clean:
                        rows.append(clean)
    return rows


def modular_matrix(rows: list[dict[int, int]], ncols: int, prime: int) -> nmod_mat:
    mat = nmod_mat(len(rows), ncols, prime)
    for i, row in enumerate(rows):
        for j, value in row.items():
            mat[i, j] = value % prime
    return mat


def relation_report(prime: int) -> dict:
    words = all_words()
    counts = [len(exact_words(w)) for w in range(MAX_WEIGHT + 1)]
    assert counts == [1, 1, 3, 8, 21, 55, 144, 377, 987]
    assert len(words) == 1597 and len(set(words)) == len(words)
    assert all(tau(tau(u)) == u for u in words)
    rows = ideal_rows(words)
    mat = modular_matrix(rows, len(words), prime)
    relation_rref, rank = mat.rref()
    columns = pivot_columns(relation_rref)
    assert len(columns) == rank
    column_submatrix = selected_matrix(
        mat, list(range(len(rows))), columns, prime
    )
    transposed_rref, transpose_rank = column_submatrix.transpose().rref()
    row_indices = pivot_columns(transposed_rref)
    assert transpose_rank == rank and len(row_indices) == rank
    minor = selected_matrix(mat, row_indices, columns, prime)
    determinant = int(minor.det())
    assert determinant != 0
    return {
        "max_weight": MAX_WEIGHT,
        "prime": prime,
        "exact_weight_word_counts_including_empty_at_weight_0": counts,
        "domain_dimension": len(words),
        "number_of_nonzero_ideal_rows": len(rows),
        "ideal_row_rank_mod_prime": rank,
        "nonzero_minor": {
            "ideal_row_indices": row_indices,
            "word_column_indices": columns,
            "determinant_mod_prime": determinant,
        },
        "required_q_coefficient_rank": len(words) - rank,
        "row_family": "v*(tau(u)-u) for basis words u,v with wt(u)+wt(v)<=8",
    }


@njit
def truncated_nested_sums(
    heads: np.ndarray,
    tails: np.ndarray,
    update_order: np.ndarray,
    binomials: np.ndarray,
    max_degree: int,
    prime: int,
    empty_index: int,
) -> np.ndarray:
    """Compute H_w(M) for all suffix words, at M=max_degree, modulo prime.

    At each upper bound M, longer words are updated before their tails, so the
    tail row still equals H_tail(M-1), exactly as required by the strict
    inequalities n_1>...>n_k.
    """
    states = np.zeros((len(heads), max_degree + 1), dtype=np.int64)
    states[empty_index, 0] = 1
    for upper in range(1, max_degree + 1):
        for pos in range(len(update_order)):
            i = update_order[pos]
            s = heads[i]
            tail = tails[i]
            if s == 0:
                for degree in range(max_degree + 1):
                    states[i, degree] = (
                        states[i, degree] + states[tail, degree]
                    ) % prime
            else:
                multiple = s
                while upper * multiple <= max_degree:
                    shift = upper * multiple
                    coeff = binomials[s, multiple]
                    for degree in range(max_degree - shift + 1):
                        states[i, degree + shift] = (
                            states[i, degree + shift]
                            + coeff * states[tail, degree]
                        ) % prime
                    multiple += 1
    return states


def q_coefficient_array(
    words: list[tuple[int, ...]], max_degree: int, prime: int
) -> np.ndarray:
    suffix_set = {u[i:] for u in words for i in range(len(u) + 1)}
    suffixes = sorted(suffix_set, key=lambda u: (len(u), u))
    suffix_index = {u: i for i, u in enumerate(suffixes)}
    heads = np.array([(-1 if not u else u[0]) for u in suffixes], dtype=np.int64)
    tails = np.array(
        [(suffix_index[()] if not u else suffix_index[u[1:]]) for u in suffixes],
        dtype=np.int64,
    )
    update_order = np.array(
        [suffix_index[u] for u in sorted(suffixes[1:], key=lambda u: (-len(u), u))],
        dtype=np.int64,
    )
    binomials = np.zeros((MAX_WEIGHT + 1, max_degree + 1), dtype=np.int64)
    for s in range(1, MAX_WEIGHT + 1):
        for multiple in range(s, max_degree + 1):
            binomials[s, multiple] = math.comb(multiple - 1, s - 1) % prime
    states = truncated_nested_sums(
        heads,
        tails,
        update_order,
        binomials,
        max_degree,
        prime,
        suffix_index[()],
    )
    # Return rows indexed by q-degree and columns indexed by admissible words.
    word_rows = np.array([suffix_index[u] for u in words], dtype=np.int64)
    return states[word_rows, :].T.copy()


def dense_modular_matrix(array: np.ndarray, prime: int) -> nmod_mat:
    nrows, ncols = array.shape
    mat = nmod_mat(nrows, ncols, prime)
    for i in range(nrows):
        for j in range(ncols):
            value = int(array[i, j])
            if value:
                mat[i, j] = value
    return mat


def pivot_columns(rref: nmod_mat) -> list[int]:
    pivots: list[int] = []
    previous = -1
    for i in range(rref.nrows()):
        pivot = None
        for j in range(previous + 1, rref.ncols()):
            if rref[i, j]:
                pivot = j
                break
        if pivot is None:
            break
        pivots.append(pivot)
        previous = pivot
    return pivots


def selected_matrix(
    original: nmod_mat, row_indices: list[int], column_indices: list[int], prime: int
) -> nmod_mat:
    result = nmod_mat(len(row_indices), len(column_indices), prime)
    for i, source_i in enumerate(row_indices):
        for j, source_j in enumerate(column_indices):
            value = original[source_i, source_j]
            if value:
                result[i, j] = value
    return result


def q_report(prime: int, max_degree: int) -> dict:
    words = all_words()
    coefficients = q_coefficient_array(words, max_degree, prime)
    # Direct low-degree checks anchor the coefficient convention.
    word_index = {u: i for i, u in enumerate(words)}
    assert coefficients[0, word_index[()]] == 1
    assert all(coefficients[d, word_index[()]] == 0 for d in range(1, max_degree + 1))
    # Z(z_1) has divisor-count coefficients.
    for degree in range(1, max_degree + 1):
        divisor_count = sum(1 for d in range(1, degree + 1) if degree % d == 0)
        assert coefficients[degree, word_index[(1,)]] == divisor_count % prime
    # The elementary duality Z(z_2)=Z(z_1 z_0) must hold coefficientwise.
    assert np.array_equal(coefficients[:, word_index[(2,)]], coefficients[:, word_index[(1, 0)]])

    qmat = dense_modular_matrix(coefficients, prime)
    q_rref, rank = qmat.rref()
    columns = pivot_columns(q_rref)
    assert len(columns) == rank
    column_submatrix = selected_matrix(
        qmat, list(range(max_degree + 1)), columns, prime
    )
    transposed_rref, transpose_rank = column_submatrix.transpose().rref()
    rows = pivot_columns(transposed_rref)
    assert transpose_rank == rank and len(rows) == rank
    minor = selected_matrix(qmat, rows, columns, prime)
    determinant = int(minor.det())
    assert determinant != 0
    return {
        "prime": prime,
        "max_q_degree": max_degree,
        "number_of_q_coefficient_rows": max_degree + 1,
        "q_coefficient_rank_mod_prime": rank,
        "nonzero_minor": {
            "q_degrees": rows,
            "word_column_indices": columns,
            "words": [list(words[j]) for j in columns],
            "determinant_mod_prime": determinant,
        },
        "coefficient_definition": (
            "exact nested-sum coefficients reduced modulo prime; for s>0, "
            "[q^(n*m)](q^n/(1-q^n))^s=binomial(m-1,s-1), m>=s; "
            "for s=0 the factor is 1"
        ),
    }


def orthogonality_report(prime: int, max_degree: int) -> dict:
    """Check every generated ideal row against every retained q coefficient."""
    words = all_words()
    rows = ideal_rows(words)
    coefficients = q_coefficient_array(words, max_degree, prime)
    failures = 0
    for row in rows:
        image = np.zeros(max_degree + 1, dtype=np.int64)
        for j, value in row.items():
            image = (image + (value % prime) * coefficients[:, j]) % prime
        if np.any(image):
            failures += 1
    assert failures == 0
    return {
        "ideal_rows_checked": len(rows),
        "q_degrees_checked": [0, max_degree],
        "nonzero_images_mod_prime": failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("relations", "q", "full"), default="full")
    parser.add_argument("--prime", type=int, default=PRIME)
    parser.add_argument("--max-q-degree", type=int, default=250)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    assert is_prime(args.prime), f"modulus {args.prime} is not prime"
    if args.stage == "relations":
        report = {"relations": relation_report(args.prime)}
    elif args.stage == "q":
        report = {"q_coefficients": q_report(args.prime, args.max_q_degree)}
    else:
        relation_data = relation_report(args.prime)
        q_data = q_report(args.prime, args.max_q_degree)
        rank_sum = (
            relation_data["ideal_row_rank_mod_prime"]
            + q_data["q_coefficient_rank_mod_prime"]
        )
        report = {
            "relations": relation_data,
            "q_coefficients": q_data,
            "orthogonality_check": orthogonality_report(
                args.prime, args.max_q_degree
            ),
            "rank_sum": rank_sum,
            "rank_sum_equals_domain_dimension": (
                rank_sum == relation_data["domain_dimension"]
            ),
        }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    if not args.quiet:
        print(rendered, end="")


if __name__ == "__main__":
    main()
