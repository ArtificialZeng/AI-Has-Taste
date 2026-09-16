#!/usr/bin/env python3
"""Exact CNF search for a length-L 3-out-of-5 picture-hanging word.

For every retained pair/triple and every half-open interval [i,j), the Boolean
E(i,j) is equivalent to the standard free-reduction grammar: either the first
letter is ignored and the remainder is empty, or it is paired with an inverse
letter after an empty middle and before an empty suffix.  Pair projections are
required empty and triple projections nonempty.  The generated CNF therefore
has no search-depth approximation.

Only complete generator/sign symmetries are broken.  A returned model is
replayed by a separate stack reducer before it is reported.
"""

import argparse
import itertools
import platform
import time

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver

from search_exact_z3 import freely_reduce, project, verify


SIGNED = tuple(range(-5, 0)) + tuple(range(1, 6))


def add_equiv_or(cnf, output, alternatives):
    """Add output <-> OR(alternatives), with alternatives as literals/bools."""
    alternatives = [a for a in alternatives if a is not False]
    if any(a is True for a in alternatives):
        cnf.append([output])
        return
    cnf.append([-output] + alternatives)
    for alternative in alternatives:
        cnf.append([-alternative, output])


def and_lit(cnf, pool, literals, name):
    """Return a literal/bool exactly equivalent to the conjunction."""
    if any(lit is False for lit in literals):
        return False
    literals = [lit for lit in literals if lit is not True]
    if not literals:
        return True
    if len(literals) == 1:
        return literals[0]
    output = pool.id(name)
    for literal in literals:
        cnf.append([-output, literal])
    cnf.append([output] + [-literal for literal in literals])
    return output


def build_cnf(length=18, symmetry=True, count_pattern=None):
    cnf = CNF()
    pool = IDPool()
    x = {(i, value): pool.id(f"x_{i}_{value}")
         for i in range(length) for value in SIGNED}

    # Exactly one signed generator at every word position.
    for i in range(length):
        literals = [x[i, value] for value in SIGNED]
        cnf.append(literals)
        for a, b in itertools.combinations(literals, 2):
            cnf.append([-a, -b])

    # The input itself is freely reduced.
    for i in range(length - 1):
        for value in SIGNED:
            cnf.append([-x[i, value], -x[i + 1, -value]])

    if symmetry:
        cnf.append([x[0, 1]])
        # Without a count pattern, label generators by their first occurrence.
        # With a sorted count pattern, only equal-count generators remain
        # interchangeable, and a shortest solution may be taken cyclically
        # reduced and rotated to an occurrence of generator 1.
        ordered = range(2, 6) if count_pattern is None else [
            g for g in range(2, 6) if count_pattern[g - 1] == count_pattern[g - 2]]
        if count_pattern is not None:
            cnf.append([-x[length - 1, -1]])
        for g in ordered:
            for i in range(length):
                earlier = [x[j, g - 1] for j in range(i)] + [x[j, -(g - 1)] for j in range(i)]
                for value in (g, -g):
                    cnf.append([-x[i, value]] + earlier)
        # Independent inversion makes each generator's first occurrence positive.
        for g in range(1, 6):
            for i in range(length):
                earlier = [x[j, g] for j in range(i)] + [x[j, -g] for j in range(i)]
                cnf.append([-x[i, -g]] + earlier)

    # Pair emptiness implies zero exponent sum.  Adding the redundant exact
    # cardinalities greatly strengthens propagation without changing models:
    # #(+g) + #(not -g) = length iff #(+g) = #(-g).
    for g in range(1, 6):
        cnf.append([x[i, g] for i in range(length)])
        cnf.append([x[i, -g] for i in range(length)])
        if count_pattern is None:
            cardinality = CardEnc.equals(
                lits=[x[i, g] for i in range(length)] + [-x[i, -g] for i in range(length)],
                bound=length, vpool=pool, encoding=EncType.cardnetwrk)
            cnf.extend(cardinality.clauses)
        else:
            assert count_pattern[g - 1] % 2 == 0
            half = count_pattern[g - 1] // 2
            for sign in (1, -1):
                cardinality = CardEnc.equals(
                    lits=[x[i, sign * g] for i in range(length)], bound=half,
                    vpool=pool, encoding=EncType.seqcounter)
                cnf.extend(cardinality.clauses)

    for retained in list(itertools.combinations(range(1, 6), 2)) + list(
            itertools.combinations(range(1, 6), 3)):
        tag = "".join(map(str, retained))
        relevant = {}
        for i in range(length):
            r = pool.id(f"r_{tag}_{i}")
            selected = [x[i, value] for g in retained for value in (g, -g)]
            add_equiv_or(cnf, r, selected)
            relevant[i] = r

        inverse_match = {}
        for i in range(length):
            for k in range(i + 1, length):
                match = pool.id(f"m_{tag}_{i}_{k}")
                inverse_match[i, k] = match
                cnf.append([-match, relevant[i]])
                for g in retained:
                    for value in (g, -g):
                        # Exactness in both directions, using one-hot x(i,*).
                        cnf.append([-x[i, value], -x[k, -value], match])
                        cnf.append([-match, -x[i, value], x[k, -value]])

        empty = {(i, i): True for i in range(length + 1)}
        for width in range(1, length + 1):
            for i in range(length - width + 1):
                j = i + width
                alternatives = [and_lit(
                    cnf, pool, [-relevant[i], empty[i + 1, j]],
                    f"skip_{tag}_{i}_{j}")]
                for k in range(i + 1, j):
                    alternatives.append(and_lit(
                        cnf, pool,
                        [inverse_match[i, k], empty[i + 1, k], empty[k + 1, j]],
                        f"pair_{tag}_{i}_{k}_{j}"))
                e = pool.id(f"e_{tag}_{i}_{j}")
                add_equiv_or(cnf, e, alternatives)
                empty[i, j] = e
        cnf.append([empty[0, length] if len(retained) == 2 else -empty[0, length]])

    return cnf, pool, x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=18)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--no-symmetry", action="store_true")
    parser.add_argument("--cnf")
    parser.add_argument("--proof")
    parser.add_argument("--count-pattern",
                        help="sorted unsigned counts, e.g. 2,2,2,4,8")
    args = parser.parse_args()

    started = time.monotonic()
    count_pattern = (tuple(map(int, args.count_pattern.split(",")))
                     if args.count_pattern else None)
    if count_pattern is not None:
        if len(count_pattern) != 5 or sum(count_pattern) != args.length:
            parser.error("count pattern must have five entries summing to length")
        if tuple(sorted(count_pattern)) != count_pattern:
            parser.error("count pattern must be nondecreasing")
    cnf, pool, x = build_cnf(args.length, not args.no_symmetry, count_pattern)
    built = time.monotonic()
    with_proof = bool(args.proof)
    with Solver(name=args.solver, bootstrap_with=cnf.clauses,
                with_proof=with_proof, use_timer=not with_proof) as solver:
        result = solver.solve()
        solved = time.monotonic()
        model = solver.get_model() if result else None
        proof = solver.get_proof() if (not result and with_proof) else None

    if args.cnf:
        cnf.to_file(args.cnf)

    print("python =", platform.python_version())
    print("pysat = 1.8.dev24")
    print("solver =", args.solver)
    print("length =", args.length)
    print("symmetry =", not args.no_symmetry)
    print("count_pattern =", count_pattern)
    print("variables =", pool.top)
    print("clauses =", len(cnf.clauses))
    print("build_seconds =", f"{built - started:.6f}")
    print("solve_seconds =", f"{solved - built:.6f}")
    print("result =", "sat" if result else "unsat")
    if result:
        positive = set(lit for lit in model if lit > 0)
        word = tuple(next(value for value in SIGNED if x[i, value] in positive)
                     for i in range(args.length))
        pairs, triples = verify(word)
        print("word =", word)
        for kept, residual in pairs.items():
            print("retain", kept, "->", residual)
        for kept, residual in triples.items():
            print("retain", kept, "->", residual)
        print("VERIFIED SAT WITNESS")
    elif args.proof:
        with open(args.proof, "w", encoding="ascii") as handle:
            for line in proof:
                handle.write(line)
                handle.write("\n")
        print("proof_lines =", len(proof))


if __name__ == "__main__":
    main()
