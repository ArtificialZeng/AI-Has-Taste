#!/usr/bin/env python3
"""Two exact, independently formulated checks of Psi_{P3}.

Route A constructs the finite r=2 multiweighted bond poset, computes every
Möbius value from its lower interval, and sums the resulting monomials.
Route B uses Theorem 5.7(5.3) on bond partitions.  Integer polynomials in two
variables are represented by exponent-pair -> coefficient dictionaries.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import product


VERTICES = (0, 1, 2)
EDGES = {frozenset((0, 1)), frozenset((1, 2))}
R = 2


def set_partitions(items):
    """Generate set partitions once, in restricted-growth order."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in set_partitions(rest):
        yield ((first,),) + partition
        for i in range(len(partition)):
            blocks = list(partition)
            blocks[i] = tuple(sorted((first,) + blocks[i]))
            blocks.sort(key=lambda b: b[0])
            yield tuple(blocks)


def connected(block):
    block = frozenset(block)
    if len(block) <= 1:
        return True
    seen = {next(iter(block))}
    while True:
        grown = seen | {
            v
            for u in seen
            for v in block
            if u != v and frozenset((u, v)) in EDGES
        }
        if grown == seen:
            return grown == block
        seen = grown


def bond_partitions(items):
    return tuple(p for p in set_partitions(items) if all(connected(b) for b in p))


def weak_compositions(total, parts=R):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def add_poly(*polys):
    result = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {e: c for e, c in result.items() if c}


def scale_poly(poly, scalar):
    return {e: scalar * c for e, c in poly.items() if scalar * c}


def mul_poly(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            exponent = tuple(x + y for x, y in zip(a, b))
            result[exponent] = result.get(exponent, 0) + ca * cb
    return {e: c for e, c in result.items() if c}


def h(degree):
    return {composition: 1 for composition in weak_compositions(degree)}


ONE = {(0, 0): 1}


def canonical_element(blocks, weights):
    return tuple(sorted(zip(blocks, weights), key=lambda bw: bw[0][0]))


def direct_elements():
    elements = []
    for partition in bond_partitions(VERTICES):
        choices = [tuple(weak_compositions(len(block) - 1)) for block in partition]
        for weights in product(*choices):
            elements.append(canonical_element(partition, weights))
    return sorted(elements, key=lambda x: (len(VERTICES) - len(x), x))


def leq(lower, upper):
    """The defining order of the r-multiweighted bond poset."""
    for upper_block, upper_weight in upper:
        pieces = [(b, w) for b, w in lower if set(b) <= set(upper_block)]
        if set().union(*(set(b) for b, _ in pieces)) != set(upper_block):
            return False
        weight_sum = tuple(sum(w[j] for _, w in pieces) for j in range(R))
        delta = tuple(upper_weight[j] - weight_sum[j] for j in range(R))
        if any(x < 0 for x in delta) or sum(delta) != len(pieces) - 1:
            return False
    return True


def direct_mobius_psi():
    elements = direct_elements()
    bottom = canonical_element(tuple((v,) for v in VERTICES), ((0, 0),) * 3)
    mobius = {}
    for element in elements:
        if element == bottom:
            mobius[element] = 1
        else:
            mobius[element] = -sum(
                value
                for lower, value in mobius.items()
                if lower != element and leq(lower, element)
            )
    psi = {}
    for element, value in mobius.items():
        total_weight = tuple(sum(w[j] for _, w in element) for j in range(R))
        psi[total_weight] = psi.get(total_weight, 0) + value
    return add_poly(psi), elements, mobius


@lru_cache(maxsize=None)
def mobius_symmetric(block):
    """M of the connected induced subgraph on block, via (5.3)."""
    block = tuple(block)
    if len(block) == 1:
        return ONE
    terms = []
    partitions = bond_partitions(block)
    top = (tuple(block),)
    for partition in partitions:
        if partition == top:
            continue
        term = h(len(partition) - 1)
        for part in partition:
            term = mul_poly(term, mobius_symmetric(tuple(part)))
        terms.append(term)
    return scale_poly(add_poly(*terms), -1)


def recurrence_psi():
    terms = []
    for partition in bond_partitions(VERTICES):
        term = ONE
        for block in partition:
            term = mul_poly(term, mobius_symmetric(tuple(block)))
        terms.append(term)
    return add_poly(*terms)


def homogeneous(poly, degree):
    return {e: c for e, c in poly.items() if sum(e) == degree}


def format_poly(poly):
    return "{" + ", ".join(f"{e}:{poly[e]}" for e in sorted(poly)) + "}"


def main():
    direct, elements, mobius = direct_mobius_psi()
    recurrence = recurrence_psi()
    expected_psi = {
        (0, 0): 1,
        (0, 1): -2,
        (1, 0): -2,
        (0, 2): 1,
        (1, 1): 3,
        (2, 0): 1,
    }
    assert direct == recurrence == expected_psi

    f0, f1, f2 = (homogeneous(direct, d) for d in range(3))
    ell = add_poly(mul_poly(f1, f1), scale_poly(mul_poly(f0, f2), -1))
    assert ell == {(0, 2): 3, (1, 1): 5, (2, 0): 3}

    # In degree two, s_(2)=m_(2)+m_(1,1) and s_(1,1)=m_(1,1).
    monomial_m2 = ell[(2, 0)]
    monomial_m11 = ell[(1, 1)]
    schur_s2 = monomial_m2
    schur_s11 = monomial_m11 - monomial_m2
    assert (schur_s2, schur_s11) == (3, 2)

    ranks = {}
    for element in elements:
        rank = len(VERTICES) - len(element)
        ranks[rank] = ranks.get(rank, 0) + 1
    maximal_values = {
        element[0][1]: mobius[element] for element in elements if len(element) == 1
    }

    print("P3 edges: 01,12; r=2 variables")
    print(f"direct poset element counts by rank: {ranks}")
    print(f"direct maximal Möbius values by weight: {maximal_values}")
    print(f"route A Psi coefficient map: {format_poly(direct)}")
    print(f"route B Psi coefficient map: {format_poly(recurrence)}")
    print("both routes: Psi_P3 = 1 - 2 e_(1) + e_(1,1) + e_(2)")
    print(f"L_(P3,1) coefficient map in x1,x2: {format_poly(ell)}")
    print(f"stable Schur coefficients: s_(2)={schur_s2}, s_(1,1)={schur_s11}")
    print("therefore L_(P3,1) = 3 s_(2) + 2 s_(1,1)")
    print("source Example 7.4 prints 2 s_(2) + 3 s_(1,1); that equality is false")


if __name__ == "__main__":
    main()
