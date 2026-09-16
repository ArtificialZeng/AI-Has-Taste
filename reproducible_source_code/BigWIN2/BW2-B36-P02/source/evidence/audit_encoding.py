#!/usr/bin/env python3
"""Regenerate the k=17 DIMACS instance and compare it byte-for-byte."""

from hashlib import sha256
from itertools import combinations
from math import gcd

from pysat.card import CardEnc, EncType
from pysat.formula import CNF

N = 127
K = 17
EXPECTED_SHA256 = "8b79ee1c4a921f27dfdb7d4c6d9581ff98860b85d1caf903b5a500de6763a8c2"

triples = []
for a, b, c in combinations(range(1, N + 1), 3):
    g = gcd(a, b)
    if gcd(a, c) == g and gcd(b, c) == g:
        triples.append((a, b, c))

cnf = CNF()
cnf.extend([[-a, -b, -c] for a, b, c in triples])
card = CardEnc.atleast(
    lits=list(range(1, N + 1)),
    bound=K,
    top_id=N,
    encoding=EncType.totalizer,
)
cnf.extend(card.clauses)

artifact = CNF(from_file="evidence/k17.cnf")
assert len(triples) == 119176
assert len(card.clauses) == 8890
assert cnf.nv == artifact.nv == 1015
assert len(cnf.clauses) == len(artifact.clauses) == 128066
assert cnf.clauses == artifact.clauses
with open("evidence/k17.cnf", "rb") as f:
    digest = sha256(f.read()).hexdigest()
assert digest == EXPECTED_SHA256
print("ENCODING VERIFIED")
print(f"forbidden_triples={len(triples)} totalizer_clauses={len(card.clauses)}")
print(f"variables={cnf.nv} clauses={len(cnf.clauses)} sha256={digest}")
