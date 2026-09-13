#!/usr/bin/env python3
"""Independent exact combinatorial model for Lentfer's R_n^(1,2).

This module deliberately does not import any code outside ``independent/``.
It implements

* the Artin presentation of Q[x_1,...,x_n]/(e_1,...,e_n),
* two mutually anticommuting exterior alphabets theta and xi,
* the diagonal S_n action, including exterior signs, and
* Lentfer's Definition 3.1 candidate monomials.

All coefficients produced here are Python integers.  Finite-field reduction is
performed only by callers that use it as a discovery/screening backend.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
from math import comb

Poly = tuple[int, ...]
State = tuple[Poly, int, int]
Sparse = dict[int, int]


def compositions(total: int, length: int):
    """Yield weak compositions of ``total`` into ``length`` parts."""
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def masks_of_size(n: int, size: int):
    for mask in range(1 << n):
        if mask.bit_count() == size:
            yield mask


def artin_polynomials(n: int, degree: int | None = None):
    """Artin monomials x^a with 0 <= a_i < i (one-based i)."""
    for a in product(*(range(i) for i in range(1, n + 1))):
        if degree is None or sum(a) == degree:
            yield a


def block_states(n: int, degree: int, theta_degree: int, xi_degree: int):
    for a in artin_polynomials(n, degree):
        for tmask in masks_of_size(n, theta_degree):
            for smask in masks_of_size(n, xi_degree):
                yield (a, tmask, smask)


def _complete_homogeneous_exponents(count: int, degree: int):
    yield from compositions(degree, count)


@lru_cache(maxsize=None)
def reduce_poly(a: Poly) -> tuple[tuple[Poly, int], ...]:
    """Reduce a monomial modulo (e_1,...,e_n) to the Artin basis.

    We use the reduced Groebner basis

        h_i(x_i,...,x_n),  i=1,...,n,

    whose leading monomials are x_i^i for lex x_1>...>x_n.  The
    result is serialized as a sorted tuple so it can be memoized.
    """
    n = len(a)
    bad = next((i for i, exponent in enumerate(a) if exponent >= i + 1), None)
    if bad is None:
        return ((a, 1),)

    power = bad + 1
    base = list(a)
    base[bad] -= power
    accum: dict[Poly, int] = {}
    # x_i^i = -sum of the other degree-i monomials in x_i,...,x_n.
    excluded = (power,) + (0,) * (n - bad - 1)
    for tail in _complete_homogeneous_exponents(n - bad, power):
        if tail == excluded:
            continue
        child = base.copy()
        for offset, exponent in enumerate(tail):
            child[bad + offset] += exponent
        for reduced, coefficient in reduce_poly(tuple(child)):
            accum[reduced] = accum.get(reduced, 0) - coefficient
    return tuple(sorted((monomial, coefficient) for monomial, coefficient in accum.items() if coefficient))


def inversion_sign(values: list[int]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions & 1 else 1


def permute_mask_sign(mask: int, permutation: tuple[int, ...]) -> tuple[int, int]:
    """Apply old index i -> permutation[i], returning mask and wedge sign."""
    images = [permutation[i] for i in range(len(permutation)) if (mask >> i) & 1]
    out = sum(1 << image for image in images)
    return out, inversion_sign(images)


@lru_cache(maxsize=None)
def cached_permute_mask_sign(mask: int, permutation: tuple[int, ...]) -> tuple[int, int]:
    return permute_mask_sign(mask, permutation)


@lru_cache(maxsize=None)
def permute_poly(a: Poly, permutation: tuple[int, ...]) -> tuple[tuple[Poly, int], ...]:
    n = len(a)
    moved = [0] * n
    for old, new in enumerate(permutation):
        moved[new] = a[old]
    return reduce_poly(tuple(moved))


def permute_state(state: State, permutation: tuple[int, ...]) -> dict[State, int]:
    """Act on one Artin/exterior basis state and reduce polynomially."""
    a, tmask, smask = state
    new_tmask, tsign = cached_permute_mask_sign(tmask, permutation)
    new_smask, ssign = cached_permute_mask_sign(smask, permutation)
    sign = tsign * ssign
    return {(reduced, new_tmask, new_smask): sign * coefficient for reduced, coefficient in permute_poly(a, permutation)}


@lru_cache(maxsize=None)
def all_permutations(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(permutations(range(n)))


def reynolds_state(state: State) -> dict[State, int]:
    """Unnormalized Reynolds sum sum_{sigma in S_n} sigma(state)."""
    accum: dict[State, int] = {}
    for permutation in all_permutations(len(state[0])):
        for target, coefficient in permute_state(state, permutation).items():
            accum[target] = accum.get(target, 0) + coefficient
    return {target: coefficient for target, coefficient in accum.items() if coefficient}


def exterior_product_sign(left_t: int, left_s: int, right_t: int, right_s: int) -> int:
    """Sign for (theta_T xi_S)(theta_U xi_V) in theta-then-xi order."""
    inversions = left_s.bit_count() * right_t.bit_count()
    # In the concatenation T,U, an inversion is a pair t in T, u in U with t>u.
    inversions += sum(1 for t in _bits(left_t) for u in _bits(right_t) if t > u)
    inversions += sum(1 for s in _bits(left_s) for v in _bits(right_s) if s > v)
    return -1 if inversions & 1 else 1


def _bits(mask: int):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def multiply_states(left: State, right: State) -> dict[State, int]:
    """Multiply two states in the Artin/exterior quotient, exactly."""
    la, lt, ls = left
    ra, rt, rs = right
    if (lt & rt) or (ls & rs):
        return {}
    sign = exterior_product_sign(lt, ls, rt, rs)
    raw_poly = tuple(x + y for x, y in zip(la, ra))
    return {(a, lt | rt, ls | rs): sign * coefficient for a, coefficient in reduce_poly(raw_poly)}


def multiply_by_generator(state: State, kind: str, index: int) -> dict[State, int]:
    n = len(state[0])
    zero = (0,) * n
    if kind == "x":
        exponent = list(zero)
        exponent[index] = 1
        generator = (tuple(exponent), 0, 0)
    elif kind == "theta":
        generator = (zero, 1 << index, 0)
    elif kind == "xi":
        generator = (zero, 0, 1 << index)
    else:
        raise ValueError(f"unknown generator kind: {kind!r}")
    return multiply_states(generator, state)


def candidate_states(n: int):
    """Yield exactly the monomials in Lentfer Definition 3.1.

    A pair (T,S) is the weight of a modified Motzkin path iff index 1 is in
    neither set and alpha_i >= 0 for every i.  Here bit 0 represents index 1.
    """
    for tmask in range(1 << n):
        if tmask & 1:
            continue
        for smask in range(1 << n):
            if smask & 1:
                continue
            alpha = [0]
            valid = True
            for i in range(1, n):
                value = alpha[-1] - 1 + (not ((tmask >> i) & 1)) + (not ((smask >> i) & 1))
                alpha.append(int(value))
                if value < 0:
                    valid = False
                    break
            if not valid:
                continue
            for a in product(*(range(bound + 1) for bound in alpha)):
                yield (tuple(a), tmask, smask)


def candidate_by_block(n: int):
    out: dict[tuple[int, int, int], list[State]] = {}
    for state in candidate_states(n):
        a, tmask, smask = state
        key = (sum(a), tmask.bit_count(), smask.bit_count())
        out.setdefault(key, []).append(state)
    return out


def expected_ambient_size(n: int) -> int:
    return 4**n


def sanity_counts(n: int) -> dict[str, int]:
    candidates = list(candidate_states(n))
    return {
        "candidate_count": len(candidates),
        "candidate_expected": (2 ** (n - 1)) * __import__("math").factorial(n),
        "polynomial_artin_count": __import__("math").factorial(n),
        "ambient_total": __import__("math").factorial(n) * 4**n,
        "fermionic_mask_pairs": expected_ambient_size(n),
    }
