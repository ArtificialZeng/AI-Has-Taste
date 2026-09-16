#!/usr/bin/env python3
"""Exact, reproducible triage enumeration for the frozen (m,n)=(4,2) cell.

This is a lead for independent proof/audit, not itself mathematical review.
Requires SymPy.
"""

import itertools
import sympy as sp


M = 4
N = 2
GENERATORS = [(i, eps) for i in range(1, N + 1) for eps in (-1, 1)]


def full_adjacency():
    # Each state is a tuple ((label,color),...) in position order.
    states = [
        tuple(zip(perm, colors))
        for perm in itertools.permutations(range(1, N + 1))
        for colors in itertools.product(range(M), repeat=N)
    ]
    index = {state: j for j, state in enumerate(states)}
    adjacency = sp.zeros(len(states))
    for row, state in enumerate(states):
        for length, eps in GENERATORS:
            image = list(state)
            image[:length] = reversed(image[:length])
            image = [
                (label, (color + eps) % M) if pos < length else (label, color)
                for pos, (label, color) in enumerate(image)
            ]
            adjacency[row, index[tuple(image)]] += 1
    return states, adjacency


def schreier_adjacency():
    # Color-major order: (0,1),(0,2),(1,1),(1,2),...,(3,2).
    states = [(color, pos) for color in range(M) for pos in range(1, N + 1)]
    index = {state: j for j, state in enumerate(states)}
    adjacency = sp.zeros(len(states))
    for row, (color, pos) in enumerate(states):
        for length, eps in GENERATORS:
            if pos <= length:
                image = ((color + eps) % M, length + 1 - pos)
            else:
                image = (color, pos)
            adjacency[row, index[image]] += 1
    return states, adjacency


def main():
    x = sp.symbols("x")
    full_states, full = full_adjacency()
    sch_states, sch = schreier_adjacency()

    expected_full = x**10 * (x - 4) * (x - 2)**8 * (x + 2)**8 * (x + 4) * (x**2 - 8)**2
    expected_sch = x**3 * (x - 4) * (x - 2)**2 * (x**2 - 8)

    assert len(full_states) == 32 and len(set(full_states)) == 32
    assert len(sch_states) == 8 and len(set(sch_states)) == 8
    assert full == full.T and sch == sch.T
    assert all(sum(full.row(i)) == 4 for i in range(full.rows))
    assert all(sum(sch.row(i)) == 4 for i in range(sch.rows))
    assert sp.expand(full.charpoly(x).as_expr() - expected_full) == 0
    assert sp.expand(sch.charpoly(x).as_expr() - expected_sch) == 0

    print("full_state_order =", full_states)
    print("A_Cay =")
    print(full)
    print("charpoly(A_Cay) =", sp.factor(full.charpoly(x).as_expr()))
    print("schreier_state_order =", sch_states)
    print("A_Sch =")
    print(sch)
    print("charpoly(A_Sch) =", sp.factor(sch.charpoly(x).as_expr()))
    print("second eigenvalue in both cases = 2*sqrt(2)")
    print("both unnormalized gaps = 4 - 2*sqrt(2)")


if __name__ == "__main__":
    main()

