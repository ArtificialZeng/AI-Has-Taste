#!/usr/bin/env python3
"""Exact SAT search for pairwise-GCD-sunflower-free subsets of [N].

The Boolean variable x_i says that i is selected.  For every triple whose
three pairwise gcds are equal, the CNF contains (-x_a or -x_b or -x_c).
PySAT supplies a cardinality encoding for sum(x_i) >= k.  A returned model is
checked again directly from the definition, without using the generated CNF.
"""

from argparse import ArgumentParser
from itertools import combinations
from math import gcd
import json

from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver


def forbidden_triples(n):
    for a, b, c in combinations(range(1, n + 1), 3):
        g = gcd(a, b)
        if gcd(a, c) == g and gcd(b, c) == g:
            yield (a, b, c)


def verify(values, n, k):
    assert values == sorted(set(values))
    assert len(values) >= k
    assert all(1 <= x <= n for x in values)
    bad = []
    for a, b, c in combinations(values, 3):
        g = gcd(a, b)
        if gcd(a, c) == g and gcd(b, c) == g:
            bad.append((a, b, c, g))
    return bad


def main():
    ap = ArgumentParser()
    ap.add_argument("--n", type=int, default=127)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--solver", default="cadical195")
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--proof-file")
    ap.add_argument("--cnf-file")
    args = ap.parse_args()

    cnf = CNF()
    triples = list(forbidden_triples(args.n))
    cnf.extend([[-a, -b, -c] for a, b, c in triples])
    at_least = CardEnc.atleast(
        lits=list(range(1, args.n + 1)),
        bound=args.k,
        top_id=args.n,
        encoding=EncType.totalizer,
    )
    cnf.extend(at_least.clauses)
    if args.cnf_file:
        cnf.to_file(args.cnf_file)

    with Solver(name=args.solver, bootstrap_with=cnf, with_proof=args.proof) as s:
        sat = s.solve()
        result = {
            "n": args.n,
            "k": args.k,
            "solver": args.solver,
            "variables": cnf.nv,
            "clauses": len(cnf.clauses),
            "forbidden_triples": len(triples),
            "status": "SAT" if sat else "UNSAT",
            "accum_stats": s.accum_stats(),
        }
        if sat:
            positive = {lit for lit in s.get_model() if lit > 0}
            chosen = [i for i in range(1, args.n + 1) if i in positive]
            bad = verify(chosen, args.n, args.k)
            result["chosen"] = chosen
            result["chosen_size"] = len(chosen)
            result["direct_verification"] = {
                "triples_checked": len(chosen) * (len(chosen) - 1) * (len(chosen) - 2) // 6,
                "bad_triples": bad,
                "passed": not bad,
            }
        elif args.proof:
            proof = s.get_proof()
            result["proof_lines"] = len(proof) if proof is not None else None
            if args.proof_file and proof is not None:
                with open(args.proof_file, "w", encoding="ascii") as f:
                    f.write("\n".join(proof) + "\n")
                result["proof_file"] = args.proof_file
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
