#!/usr/bin/env python3
"""Independent exact verifier for the k=4 Laurent certificate.

Only the Python standard library is used.  Unlike the discovery program, DAGs
are generated through all topological orders, deduplicated, canonically
unlabelled, and weighted by reciprocal automorphism order.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
from math import comb, factorial
from pathlib import Path


Laurent = dict[int, Fraction]


def clean(poly: Laurent) -> Laurent:
    return {e: c for e, c in poly.items() if c}


def add(left: Laurent, right: Laurent) -> Laurent:
    ans = dict(left)
    for exponent, coefficient in right.items():
        ans[exponent] = ans.get(exponent, Fraction()) + coefficient
    return clean(ans)


def scale(poly: Laurent, scalar: Fraction) -> Laurent:
    return clean({e: c * scalar for e, c in poly.items()})


def multiply(left: Laurent, right: Laurent) -> Laurent:
    ans: Laurent = {}
    for e1, c1 in left.items():
        for e2, c2 in right.items():
            ans[e1 + e2] = ans.get(e1 + e2, Fraction()) + c1 * c2
    return clean(ans)


def dz(poly: Laurent, times: int) -> Laurent:
    for _ in range(times):
        poly = clean({e - 2: -c * e for e, c in poly.items()})
    return poly


def odd_double_factorial(n: int) -> int:
    if n in (-1, 0, 1):
        return 1
    if n < -1:
        raise ValueError(n)
    ans = 1
    for value in range(n, 0, -2):
        ans *= value
    return ans


_m_cache: dict[tuple[int, int], int] = {}


def one_component_count(leaves: int, reticulations: int) -> int:
    if leaves < reticulations or leaves < 0 or reticulations < 0:
        return 0
    key = (leaves, reticulations)
    if key in _m_cache:
        return _m_cache[key]
    if reticulations == 0:
        value = 0 if leaves == 0 else odd_double_factorial(2 * leaves - 3)
    elif reticulations == 1:
        value = (leaves - 1) * odd_double_factorial(2 * leaves - 3)
    else:
        k = reticulations
        value = (leaves + k - 2) * one_component_count(leaves, k - 1)
        value += (k - 1) * one_component_count(leaves, k - 2)
        correction = 0
        for d in range(1, k):
            correction += (
                comb(k - 1, d)
                * odd_double_factorial(2 * d - 1)
                * (
                    one_component_count(leaves - d, k - 1 - d)
                    - one_component_count(leaves + 1 - d, k - 1 - d)
                )
            )
        if correction % 2:
            raise AssertionError("nonintegral recurrence correction")
        value += correction // 2
    _m_cache[key] = value
    return value


def generalized_binomial(alpha: Fraction, j: int) -> Fraction:
    ans = Fraction(1)
    for q in range(j):
        ans *= alpha - q
    return ans / factorial(j)


def numerator_coefficients(k: int) -> list[Fraction]:
    alpha = Fraction(4 * k - 1, 2)
    ans = []
    for r in range(2 * k):
        coefficient = Fraction()
        for j in range(r + 1):
            coefficient += (
                Fraction(one_component_count(k + r - j, k), factorial(r - j))
                * generalized_binomial(alpha, j)
                * (-2) ** j
            )
        ans.append(coefficient)
    return ans


def substitute_z_polynomial(coefficients: list[Fraction], denominator_power: int) -> Laurent:
    """Substitute z=(1-X^2)/2 and divide by X^denominator_power."""
    ans: Laurent = {}
    for r, coefficient in enumerate(coefficients):
        for j in range(r + 1):
            exponent = 2 * j - denominator_power
            ans[exponent] = ans.get(exponent, Fraction()) + (
                coefficient * comb(r, j) * (-1) ** j / (2**r)
            )
    return clean(ans)


def vertex_weights(k: int) -> dict[tuple[int, int], Laurent]:
    fs = {0: {0: Fraction(1), 1: Fraction(-1)}}
    for d in range(1, k + 1):
        fs[d] = substitute_z_polynomial(numerator_coefficients(d), 4 * d - 1)
    weights = {}
    for children in range(k + 1):
        for double_children in range(children + 1):
            if double_children:
                weight = dz(fs[double_children], children - double_children)
            else:
                weight = dz(fs[0], children)
                if children:
                    weight = add(
                        weight,
                        {0: Fraction(-odd_double_factorial(2 * children - 3))},
                    )
            weights[children, double_children] = weight
    return weights


def topological_generation(m: int) -> set[tuple[int, ...]]:
    """Generate labelled DAGs through all topological orders, then deduplicate."""
    matrices: set[tuple[int, ...]] = set()
    for nonroot_order in permutations(range(1, m)):
        order = (0,) + nonroot_order
        choices = [
            list(combinations_with_replacement(order[:position], 2))
            for position in range(1, m)
        ]
        for parent_data in product(*choices):
            adjacency = [0] * (m * m)
            for position, parents in enumerate(parent_data, 1):
                child = order[position]
                for parent in parents:
                    adjacency[parent * m + child] += 1
            matrices.add(tuple(adjacency))
    return matrices


def permute_matrix(matrix: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, ...]:
    m = len(permutation)
    return tuple(
        matrix[permutation[i] * m + permutation[j]]
        for i in range(m)
        for j in range(m)
    )


def canonical_classes(matrices: set[tuple[int, ...]], m: int) -> dict[tuple[int, ...], int]:
    classes: dict[tuple[int, ...], int] = {}
    root_preserving = [(0,) + p for p in permutations(range(1, m))]
    for matrix in matrices:
        canonical = min(permute_matrix(matrix, p) for p in root_preserving)
        classes[canonical] = classes.get(canonical, 0) + 1
    return classes


def component_graph_count_by_rows(m_max: int) -> dict[int, int]:
    """Independently count fully labelled D_m by the sink-row recurrence.

    Remove the current sink row of size s.  If the smaller graph has t sinks,
    inclusion--exclusion forces every one of those t vertices to be used as a
    parent of at least one new sink.  The necessary bound is t <= 2s.
    """
    by_size_and_sinks: dict[tuple[int, int], int] = {(1, 1): 1}
    totals = {1: 1}
    for m in range(2, m_max + 1):
        for s in range(1, m):
            old_size = m - s
            subtotal = 0
            for t in range(1, min(2 * s, old_size) + 1):
                old_count = by_size_and_sinks.get((old_size, t), 0)
                if not old_count:
                    continue
                extensions = sum(
                    (-1) ** omitted
                    * comb(t, omitted)
                    * comb(old_size - omitted + 1, 2) ** s
                    for omitted in range(t + 1)
                )
                subtotal += extensions * old_count
            by_size_and_sinks[m, s] = comb(m, s) * subtotal
        totals[m] = sum(by_size_and_sinks.get((m, s), 0) for s in range(1, m))
    return totals


def graph_weight(matrix: tuple[int, ...], m: int, weights: dict[tuple[int, int], Laurent]) -> Laurent:
    ans: Laurent = {0: Fraction(1)}
    for vertex in range(m):
        children = [child for child in range(m) if matrix[vertex * m + child]]
        vertex_type = (
            len(children),
            sum(matrix[vertex * m + child] == 2 for child in children),
        )
        ans = multiply(ans, weights[vertex_type])
    return ans


def rv_egf_by_unlabelled_classes(k: int) -> tuple[Laurent, int, int, Counter]:
    m = k + 1
    matrices = topological_generation(m)
    classes = canonical_classes(matrices, m)
    weights = vertex_weights(k)
    total: Laurent = {}
    automorphisms = Counter()
    for representative, orbit_size in classes.items():
        automorphism_order = factorial(k) // orbit_size
        automorphisms[automorphism_order] += 1
        total = add(
            total,
            scale(graph_weight(representative, m, weights), Fraction(1, automorphism_order)),
        )
    return total, len(matrices), len(classes), automorphisms


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def coefficient_count(poly: Laurent, n: int) -> int:
    coefficient = Fraction()
    for exponent, scalar in poly.items():
        coefficient += scalar * generalized_binomial(Fraction(exponent, 2), n) * (-2) ** n
    value = coefficient * factorial(n)
    if value.denominator != 1:
        raise AssertionError("EGF coefficient is not integral")
    return value.numerator


def tc4_count(n: int) -> int:
    bracket = (
        odd_double_factorial(2 * n + 5)
        - 4 * (2 ** (n + 2)) * factorial(n + 2)
        + 2 * odd_double_factorial(2 * n + 3)
        + Fraction(17, 2) * (2 ** (n + 1)) * factorial(n + 1)
        - Fraction(283, 63) * odd_double_factorial(2 * n + 1)
    )
    value = comb(n, 4) * bracket
    if value.denominator != 1:
        raise AssertionError("TC4 formula is not integral")
    return value.numerator


def corrected_delta4_count(n: int) -> int:
    """Evaluate the corrected all-ell formula in the exact certificate."""
    a_coefficients = [
        Fraction(309, 16), Fraction(48467, 840), Fraction(-7831, 140),
        Fraction(-1088, 5), Fraction(-34739, 210), Fraction(-1027, 105),
        Fraction(110, 3), Fraction(8),
    ]
    b_coefficients = [
        Fraction(-194), Fraction(-1633, 3), Fraction(-1091, 2),
        Fraction(-985, 6), Fraction(82), Fraction(64),
    ]
    a0 = sum(coefficient * n**degree for degree, coefficient in enumerate(a_coefficients))
    b0 = sum(coefficient * n**degree for degree, coefficient in enumerate(b_coefficients))
    value = (
        a0 * odd_double_factorial(2 * n - 3)
        + Fraction(15, 16) * odd_double_factorial(2 * n - 5)
        - b0 * 2 ** (n - 3) * factorial(n)
    )
    if value.denominator != 1:
        raise AssertionError("corrected Delta4 formula is not integral")
    return value.numerator


def solve_square(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """Fraction-only Gauss--Jordan elimination; fail closed on singular input."""
    n = len(matrix)
    augmented = [row[:] + [value] for row, value in zip(matrix, rhs)]
    for column in range(n):
        pivot = next((row for row in range(column, n) if augmented[row][column]), None)
        if pivot is None:
            raise AssertionError("singular interpolation matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [augmented[row][-1] for row in range(n)]


def load_certificate(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    project = Path(__file__).resolve().parents[1]
    certificate_path = project / "certificates" / "delta4_laurent.json"
    certificate = load_certificate(certificate_path)
    expected = {
        int(exponent): parse_fraction(coefficient)
        for exponent, coefficient in certificate["rv4_laurent_coefficients"].items()
    }
    n4 = numerator_coefficients(4)
    if n4 != [Fraction(value) for value in certificate["N4_coefficients_ascending_z"]]:
        print("FAIL: one-component numerator mismatch", file=sys.stderr)
        return 1
    f4 = substitute_z_polynomial(n4, 15)
    star = scale(
        multiply(f4, {0: Fraction(1), 1: Fraction(-4), 2: Fraction(6),
                      3: Fraction(-4), 4: Fraction(1)}),
        Fraction(1, 24),
    )
    if star.get(3) != Fraction(5, 16):
        print("FAIL: isolated four-sink-star coefficient mismatch", file=sys.stderr)
        return 1
    actual, labelled_count, class_count, automorphisms = rv_egf_by_unlabelled_classes(4)
    if actual != expected:
        print("FAIL: Laurent polynomial mismatch", file=sys.stderr)
        return 1
    if labelled_count != 1587 or class_count != 79:
        print("FAIL: D5 counts mismatch", file=sys.stderr)
        return 1
    row_counts = component_graph_count_by_rows(5)
    if row_counts != {1: 1, 2: 2, 3: 15, 4: 256, 5: 7935}:
        print("FAIL: independent sink-row recurrence mismatch", file=sys.stderr)
        return 1
    if row_counts[5] != 5 * labelled_count:
        print("FAIL: fixed-root and all-root-labelled counts disagree", file=sys.stderr)
        return 1
    if dict(sorted(automorphisms.items())) != {1: 56, 2: 19, 4: 1, 6: 2, 24: 1}:
        print("FAIL: automorphism histogram mismatch", file=sys.stderr)
        return 1
    if actual.get(3) != Fraction(5, 16):
        print("FAIL: decisive X^3 coefficient mismatch", file=sys.stderr)
        return 1

    # Finite exact cross-check of the claimed degree bounds.  Fourteen values
    # determine the 8+6 coefficients of deg(A)<=7 and deg(B)<=5.  The next
    # exact value gives a nonzero integer residual.
    delta = {
        n: coefficient_count(actual, n) - tc4_count(n)
        for n in range(5, 20)
    }
    for n in range(5, 31):
        if corrected_delta4_count(n) != coefficient_count(actual, n) - tc4_count(n):
            print("FAIL: corrected closed form mismatch", file=sys.stderr)
            return 1
    matrix: list[list[Fraction]] = []
    rhs: list[Fraction] = []
    for n in range(5, 19):
        matrix.append(
            [Fraction(n**j * odd_double_factorial(2 * n - 3)) for j in range(8)]
            + [Fraction(-n**j * 2 ** (n - 3) * factorial(n)) for j in range(6)]
        )
        rhs.append(Fraction(delta[n]))
    fitted = solve_square(matrix, rhs)
    n = 19
    predicted = sum(
        fitted[j] * n**j * odd_double_factorial(2 * n - 3)
        for j in range(8)
    ) + sum(
        fitted[8 + j] * (-n**j * 2 ** (n - 3) * factorial(n))
        for j in range(6)
    )
    residual = Fraction(delta[n]) - predicted
    if residual != 98075577600000:
        print("FAIL: finite degree-bound residual mismatch", file=sys.stderr)
        return 1

    # Any polynomial in l multiplying (2l-3)!! is obtained by applying a
    # polynomial in theta=z*d/dz to 1-X.  The theta orbit of 1-X contains
    # only odd X-exponents <=1 (and a constant before the first derivative).
    # A polynomial in l multiplying 2^l l! has only even X-exponents.  Thus
    # neither summand, nor a finite initial correction (a polynomial in z),
    # can produce X^3.
    certificate_hash = hashlib.sha256(certificate_path.read_bytes()).hexdigest()
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "status": "PASS",
                "labelled_D5_root_fixed": labelled_count,
                "unlabelled_D5": class_count,
                "fully_labelled_D5_sink_row_check": row_counts[5],
                "automorphism_histogram": dict(sorted(automorphisms.items())),
                "rv4_X3_coefficient": "5/16",
                "isolated_star_X3_coefficient": str(star[3]),
                "degree_bound_test_range": "fit ell=5..18; test ell=19",
                "degree_bound_residual_at_19": str(residual),
                "corrected_closed_form_check_range": "ell=5..30",
                "obstruction": "nonzero odd exponent 3 is outside both polynomial-basis EGF spans",
                "certificate_sha256": certificate_hash,
                "verifier_sha256": code_hash,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
