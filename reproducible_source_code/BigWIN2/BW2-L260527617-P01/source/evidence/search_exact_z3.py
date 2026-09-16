#!/usr/bin/env python3
"""Exact bounded search for k-out-of-n picture-hanging words.

The word letters are nonzero integers in [-n,n].  For each retained alphabet,
the encoding simulates ordinary free reduction with an exact LIFO stack.  A
2-letter retained alphabet must finish at depth zero, while a 3-letter retained
alphabet must finish at positive depth.  Thus for n=5 this encodes exactly the
twenty deletion conditions in source.md, in addition to free reduction of the
input word.

The optional symmetry constraints are complete: a generator permutation and
independent sign inversions put the first letter at +1, order generators 2..n
by first occurrence, and make every generator's first occurrence positive.
No cyclic quotient or search-specific pruning is used.
"""

import argparse
import itertools
import platform
import time

import z3


def freely_reduce(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def project(word, retained):
    retained = frozenset(retained)
    return freely_reduce(letter for letter in word if abs(letter) in retained)


def verify(word, n=5):
    assert all(1 <= abs(letter) <= n for letter in word)
    assert freely_reduce(word) == tuple(word)
    pair_residuals = {
        kept: project(word, kept) for kept in itertools.combinations(range(1, n + 1), 2)
    }
    triple_residuals = {
        kept: project(word, kept) for kept in itertools.combinations(range(1, n + 1), 3)
    }
    assert all(not residual for residual in pair_residuals.values())
    assert all(residual for residual in triple_residuals.values())
    return pair_residuals, triple_residuals


def abs_z3(x):
    return z3.If(x > 0, x, -x)


def add_projection_stack(solver, letters, retained, must_be_empty, tag):
    """Simulate free reduction of the retained subword with a persistent array."""
    length = len(letters)
    depth = [z3.Int(f"d_{tag}_{i}") for i in range(length + 1)]
    stack = [z3.Array(f"a_{tag}_{i}", z3.IntSort(), z3.IntSort())
             for i in range(length + 1)]
    solver.add(depth[0] == 0)
    solver.add(stack[0] == z3.K(z3.IntSort(), 0))
    retained_tests = []
    for i, letter in enumerate(letters):
        relevant = z3.Or(*[abs_z3(letter) == g for g in retained])
        pop = z3.And(relevant, depth[i] > 0,
                     z3.Select(stack[i], depth[i] - 1) == -letter)
        push = z3.And(relevant, z3.Not(pop))
        solver.add(depth[i] >= 0, depth[i] <= i)
        solver.add(depth[i + 1] == z3.If(
            z3.Not(relevant), depth[i], z3.If(pop, depth[i] - 1, depth[i] + 1)))
        solver.add(stack[i + 1] == z3.If(
            push, z3.Store(stack[i], depth[i], letter), stack[i]))
        retained_tests.append(relevant)
    solver.add(depth[length] >= 0, depth[length] <= length)
    solver.add(depth[length] == 0 if must_be_empty else depth[length] > 0)
    return depth


def add_projection_grammar(solver, letters, retained, must_be_empty, tag):
    """Encode exact empty reduction by the standard noncrossing-pair grammar.

    Empty[i,j] means that the projection of letters[i:j] freely reduces to the
    identity.  Its defining equivalence either skips an unretained first letter,
    or matches a retained first letter to an inverse at k after an empty middle,
    followed by an empty suffix.  This is an exact characterization, not a
    bounded stack approximation.
    """
    length = len(letters)
    empty = {(i, i): z3.BoolVal(True) for i in range(length + 1)}
    retained = tuple(retained)
    for width in range(1, length + 1):
        for i in range(length - width + 1):
            j = i + width
            variable = z3.Bool(f"e_{tag}_{i}_{j}")
            empty[i, j] = variable
            relevant = z3.Or(*[abs_z3(letters[i]) == g for g in retained])
            alternatives = [z3.And(z3.Not(relevant), empty[i + 1, j])]
            for k in range(i + 1, j):
                alternatives.append(z3.And(
                    relevant, letters[k] == -letters[i],
                    empty[i + 1, k], empty[k + 1, j]))
            solver.add(variable == z3.Or(*alternatives))
    solver.add(empty[0, length] if must_be_empty else z3.Not(empty[0, length]))
    return empty


def build_solver(length=18, n=5, symmetry=True, timeout_ms=0,
                 encoding="grammar"):
    solver = z3.Solver()
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    letters = [z3.Int(f"w_{i}") for i in range(length)]
    domain = tuple(range(-n, 0)) + tuple(range(1, n + 1))
    for letter in letters:
        solver.add(z3.Or(*[letter == value for value in domain]))
    for i in range(length - 1):
        solver.add(letters[i + 1] != -letters[i])

    if symmetry:
        # Relabel and invert the generator of the first letter.
        solver.add(letters[0] == 1)
        # Relabel the other generators in increasing order of first occurrence.
        for g in range(2, n + 1):
            for i, letter in enumerate(letters):
                if i == 0:
                    solver.add(abs_z3(letter) != g)
                else:
                    solver.add(z3.Implies(
                        abs_z3(letter) == g,
                        z3.Or(*[abs_z3(letters[j]) == g - 1 for j in range(i)])))
        # Independently invert each generator so its first occurrence is positive.
        for g in range(1, n + 1):
            for i, letter in enumerate(letters):
                earlier = [abs_z3(letters[j]) == g for j in range(i)]
                solver.add(z3.Implies(
                    letter == -g, z3.Or(*earlier) if earlier else z3.BoolVal(False)))

    for kept in itertools.combinations(range(1, n + 1), 2):
        encoder = add_projection_grammar if encoding == "grammar" else add_projection_stack
        encoder(solver, letters, kept, True, "p" + "".join(map(str, kept)))
    for kept in itertools.combinations(range(1, n + 1), 3):
        encoder = add_projection_grammar if encoding == "grammar" else add_projection_stack
        encoder(solver, letters, kept, False, "t" + "".join(map(str, kept)))
    return solver, letters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=18)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--timeout-ms", type=int, default=0)
    parser.add_argument("--no-symmetry", action="store_true")
    parser.add_argument("--encoding", choices=("grammar", "stack"),
                        default="grammar")
    parser.add_argument("--dump-smt2")
    args = parser.parse_args()

    started = time.monotonic()
    solver, letters = build_solver(args.length, args.n, not args.no_symmetry,
                                   args.timeout_ms, args.encoding)
    built = time.monotonic()
    if args.dump_smt2:
        with open(args.dump_smt2, "w", encoding="utf-8") as handle:
            handle.write(solver.to_smt2())
    result = solver.check()
    finished = time.monotonic()

    print("python =", platform.python_version())
    print("z3 =", z3.get_version_string())
    print("length =", args.length)
    print("symmetry =", not args.no_symmetry)
    print("encoding =", args.encoding)
    print("assertions =", len(solver.assertions()))
    print("build_seconds =", f"{built - started:.6f}")
    print("solve_seconds =", f"{finished - built:.6f}")
    print("result =", result)
    if result == z3.sat:
        model = solver.model()
        word = tuple(model.eval(letter).as_long() for letter in letters)
        pair_residuals, triple_residuals = verify(word, args.n)
        print("word =", word)
        for kept, residual in pair_residuals.items():
            print("retain", kept, "->", residual)
        for kept, residual in triple_residuals.items():
            print("retain", kept, "->", residual)
        print("VERIFIED SAT WITNESS")
    elif result == z3.unknown:
        print("reason_unknown =", solver.reason_unknown())


if __name__ == "__main__":
    main()
