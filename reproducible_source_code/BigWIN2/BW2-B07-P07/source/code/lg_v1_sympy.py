#!/usr/bin/env python3
"""Independent exact LG evaluator using the radical-free V1 R-matrix.

This implementation is deliberately separate from ``code/lg_exact.py``.  It
uses SymPy rational functions and the V1 R-matrix in Appendix A of
Garoufalidis et al., *Skein theory for the Links--Gould polynomial* (2026).
"""

from __future__ import annotations

import argparse
import json

import sympy as sp


def matrices():
    t0, t1 = sp.symbols("t0 t1")
    r = sp.MutableSparseMatrix(16, 16, {})

    def add(source, target, coefficient):
        column = 4 * source[0] + source[1]
        row = 4 * target[0] + target[1]
        r[row, column] += coefficient

    add((0, 0), (0, 0), -1)
    add((0, 1), (1, 0), -t0)
    add((0, 2), (2, 0), -t1)
    add((0, 3), (3, 0), -t0 * t1)
    add((1, 0), (0, 1), -1)
    add((1, 0), (1, 0), t0 - 1)
    add((1, 1), (1, 1), t0)
    add((1, 2), (2, 1), -t1)
    add((1, 2), (3, 0), (t0 - 1) * t1)
    add((1, 3), (3, 1), t0 * t1)
    add((2, 0), (0, 2), -1)
    add((2, 0), (2, 0), t1 - 1)
    add((2, 1), (1, 2), -t1 ** -1)
    add((2, 1), (3, 0), 1 - t0)
    add((2, 2), (2, 2), t1)
    add((2, 3), (3, 2), 1)
    add((3, 0), (0, 3), -1)
    add((3, 0), (1, 2), t1 ** -1 - 1)
    add((3, 0), (2, 1), t1 - 1)
    add((3, 0), (3, 0), t0 + t1 - 2)
    add((3, 1), (1, 3), t1 ** -1)
    add((3, 1), (3, 1), t0 - 1)
    add((3, 2), (2, 3), t1)
    add((3, 2), (3, 2), t1 - 1)
    add((3, 3), (3, 3), -1)

    identity = sp.eye(16)
    rinv = ((t0 ** -1 + t1 ** -1) * (identity + r)
            - (t0 * t1) ** -1 * (r + r * r) - identity)
    enhancement = sp.diag(-1, 1, 1, -1)
    return t0, t1, r, rinv, enhancement


def links_gould(word, strands):
    t0, t1, r, rinv, enhancement = matrices()
    if strands < 2:
        raise ValueError("at least two strands are required")
    generators = []
    for position in range(strands - 1):
        left = sp.eye(4 ** position)
        right = sp.eye(4 ** (strands - position - 2))
        generators.append((sp.kronecker_product(left, r, right),
                           sp.kronecker_product(left, rinv, right)))
    value = sp.eye(4 ** strands)
    for letter in word:
        if letter == 0 or abs(letter) >= strands:
            raise ValueError(f"invalid B_{strands} generator: {letter}")
        value = value * generators[abs(letter) - 1][0 if letter > 0 else 1]
    quantum_trace = sp.eye(4)
    for _ in range(strands - 1):
        quantum_trace = sp.kronecker_product(quantum_trace, enhancement)
    value = quantum_trace * value
    open_block = 4 ** (strands - 1)
    return sp.cancel(sum(value[k, k] for k in range(open_block)))


def self_test():
    t0, t1, r, rinv, _ = matrices()
    assert (r * rinv - sp.eye(16)).applyfunc(sp.cancel) == sp.zeros(16)
    assert (rinv * r - sp.eye(16)).applyfunc(sp.cancel) == sp.zeros(16)
    assert sp.cancel(links_gould([1], 2) - 1) == 0
    expected = (2 * t0 * t1 - 3 * t0 - 3 * t1 + t0 / t1 + 7
                + t1 / t0 - 3 / t1 - 3 / t0 + 2 / (t0 * t1))
    assert sp.cancel(links_gould([1, -2, 1, -2], 3) - expected) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs="*", type=int)
    parser.add_argument("--strands", type=int, default=3)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("INDEPENDENT_V1_SELF_TEST_OK")
        return
    if not args.word:
        parser.error("provide a braid word or --self-test")
    result = sp.expand(links_gould(args.word, args.strands))
    print(json.dumps({"word": args.word, "strands": args.strands,
                      "polynomial": str(result)}, sort_keys=True))


if __name__ == "__main__":
    main()
