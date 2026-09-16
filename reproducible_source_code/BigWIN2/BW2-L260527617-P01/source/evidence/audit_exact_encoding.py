#!/usr/bin/env python3
"""Deterministic audit of the finite-case split and stored exact CNFs."""

import gc
import hashlib
import itertools
import platform

import pysat
from pysat.formula import CNF

from search_exact_sat import build_cnf
from search_exact_z3 import freely_reduce


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def patterns(length):
    return [
        entries
        for entries in itertools.combinations_with_replacement(
            range(2, length + 1, 2), 5
        )
        if sum(entries) == length
    ]


def grammar_empty(word, retained):
    """Independent Boolean evaluation of the interval grammar used in CNF."""
    retained = frozenset(retained)
    length = len(word)
    empty = {(i, i): True for i in range(length + 1)}
    for width in range(1, length + 1):
        for i in range(length - width + 1):
            j = i + width
            if abs(word[i]) not in retained:
                value = empty[i + 1, j]
            else:
                value = any(
                    word[k] == -word[i]
                    and empty[i + 1, k]
                    and empty[k + 1, j]
                    for k in range(i + 1, j)
                )
            empty[i, j] = value
    return empty[0, length]


def audit_grammar():
    # Include two retained generators and one ignored generator.  This checks
    # every word through length 7, including cancellation cascades and skips.
    alphabet = (-3, -2, -1, 1, 2, 3)
    checked = 0
    for length in range(8):
        for word in itertools.product(alphabet, repeat=length):
            projected = [letter for letter in word if abs(letter) in (1, 2)]
            expected = not freely_reduce(projected)
            assert grammar_empty(word, (1, 2)) == expected
            checked += 1
    print(f"GRAMMAR_CROSSCHECK words={checked} max_length=7 result=pass")


def main():
    print(f"python={platform.python_version()} pysat={pysat.__version__}")
    all_patterns = {length: patterns(length) for length in range(10, 20, 2)}
    assert [len(all_patterns[length]) for length in range(10, 20, 2)] == [1, 1, 2, 3, 5]
    print("COUNT_PATTERNS", all_patterns)
    for length in range(10, 20, 2):
        for pattern in all_patterns[length]:
            suffix = "".join(map(str, pattern))
            path = f"L{length}_{suffix}.cnf"
            generated, pool, _ = build_cnf(
                length=length, symmetry=True, count_pattern=pattern
            )
            stored = CNF(from_file=path)
            assert pool.top == stored.nv == generated.nv
            assert generated.clauses == stored.clauses
            print(
                "CNF_REGENERATED",
                f"path={path}",
                f"pattern={pattern}",
                f"variables={stored.nv}",
                f"clauses={len(stored.clauses)}",
                f"sha256={sha256(path)}",
                "result=identical",
            )
            del generated, stored
            gc.collect()
    audit_grammar()
    print("AUDIT_EXACT_ENCODING_PASS")


if __name__ == "__main__":
    main()
