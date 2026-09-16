#!/usr/bin/env python3
"""Exact SAT search for a systematic ternary 4-all-symbol PIR matrix.

The unknown matrix is G=(I_6|A), with five nonzero projectively normalized
columns in A.  For each target i the singleton {i} is one recovery set, so
the CNF asks for three further pairwise-disjoint recovery coefficient vectors
avoiding i.  Field multiplication and addition are encoded by their complete
three-valued truth tables; a SAT model is checked again by direct arithmetic.

UNSAT from this script is not by itself a nonexistence proof: the emitted CNF
and a separately replayed proof certificate would be required for that use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


P = 3
K = 6
N = 11
R = 3  # nontrivial recoveries; {i} supplies the fourth


class Encoding:
    def __init__(self) -> None:
        self.pool = IDPool()
        self.cnf = CNF()
        self.trits: dict[str, tuple[int, int, int]] = {}

    def trit(self, name: str) -> tuple[int, int, int]:
        if name in self.trits:
            return self.trits[name]
        lits = tuple(self.pool.id(f"{name}={v}") for v in range(P))
        self.trits[name] = lits
        self.cnf.append(list(lits))
        for u in range(P):
            for v in range(u + 1, P):
                self.cnf.append([-lits[u], -lits[v]])
        return lits

    def fix(self, x: tuple[int, int, int], value: int) -> None:
        self.cnf.append([x[value]])

    def product(
        self,
        name: str,
        x: tuple[int, int, int],
        y: tuple[int, int, int],
    ) -> tuple[int, int, int]:
        z = self.trit(name)
        for xv in range(P):
            for yv in range(P):
                self.cnf.append([-x[xv], -y[yv], z[(xv * yv) % P]])
        return z

    def add(
        self,
        name: str,
        x: tuple[int, int, int],
        y: tuple[int, int, int],
    ) -> tuple[int, int, int]:
        z = self.trit(name)
        for xv in range(P):
            for yv in range(P):
                self.cnf.append([-x[xv], -y[yv], z[(xv + yv) % P]])
        return z

    def equal(
        self, x: tuple[int, int, int], y: tuple[int, int, int]
    ) -> None:
        for value in range(P):
            self.cnf.append([-x[value], y[value]])
            self.cnf.append([-y[value], x[value]])


def build_encoding(
    active_targets: tuple[int, ...] = tuple(range(N)),
    fixed_a: list[list[int]] | None = None,
) -> tuple[
    Encoding,
    list[list[tuple[int, int, int]]],
    list[list[list[tuple[int, int, int]]]],
]:
    enc = Encoding()
    a = [[enc.trit(f"a_{row}_{col}") for col in range(5)] for row in range(K)]
    if fixed_a is not None:
        if len(fixed_a) != K or any(len(row) != 5 for row in fixed_a):
            raise ValueError("fixed_a must have shape 6 x 5")
        for row in range(K):
            for col in range(5):
                enc.fix(a[row][col], fixed_a[row][col] % P)

    # Nonzero projective columns, normalized so their first nonzero entry is 1.
    for col in range(5):
        enc.cnf.append([a[row][col][value] for row in range(K) for value in (1, 2)])
        for row in range(K):
            # If all earlier entries vanish, this entry cannot be 2.
            enc.cnf.append(
                [a[earlier][col][value] for earlier in range(row) for value in (1, 2)]
                + [-a[row][col][2]]
            )

    # For e_1, three disjoint nontrivial recoveries require three distinct A
    # columns nonzero in row 1.  Permute A columns so those occur first, then
    # put all remaining row-1-nonzero columns before the zero ones.
    for col in range(3):
        enc.fix(a[0][col], 1)
    for col in range(4):
        enc.cnf.append([-a[0][col][0], -a[0][col + 1][1]])

    coeff = [
        [
            [enc.trit(f"c_{target}_{rec}_{col}") for col in range(N)]
            for rec in range(R)
        ]
        for target in range(N)
    ]

    for target in active_targets:
        for rec in range(R):
            enc.fix(coeff[target][rec][target], 0)

        # A coordinate may occur in at most one of the three recoveries.
        for col in range(N):
            for first in range(R):
                for second in range(first + 1, R):
                    for fv in (1, 2):
                        for sv in (1, 2):
                            enc.cnf.append(
                                [
                                    -coeff[target][first][col][fv],
                                    -coeff[target][second][col][sv],
                                ]
                            )

        # Break the S_3 symmetry by increasing least-used coordinates.
        minima: list[list[int]] = []
        for rec in range(R):
            choices = [enc.pool.id(f"minimum_{target}_{rec}={col}") for col in range(N)]
            minima.append(choices)
            enc.cnf.append(choices)
            for first in range(N):
                for second in range(first + 1, N):
                    enc.cnf.append([-choices[first], -choices[second]])
            for col, choice in enumerate(choices):
                enc.cnf.append(
                    [-choice, coeff[target][rec][col][1], coeff[target][rec][col][2]]
                )
                for earlier in range(col):
                    enc.cnf.append([-choice, coeff[target][rec][earlier][0]])
        for rec in range(R - 1):
            for first in range(N):
                for second in range(first + 1):
                    enc.cnf.append([-minima[rec][first], -minima[rec + 1][second]])

        # Exact equations sum_j c_j g_j = g_target in F_3.
        for rec in range(R):
            for row in range(K):
                terms: list[tuple[int, int, int]] = []
                if row != target:  # systematic contribution c_row e_row
                    terms.append(coeff[target][rec][row])
                for parity in range(5):
                    terms.append(
                        enc.product(
                            f"mul_{target}_{rec}_{row}_{parity}",
                            coeff[target][rec][K + parity],
                            a[row][parity],
                        )
                    )
                total = terms[0]
                for pos, term in enumerate(terms[1:], start=1):
                    total = enc.add(f"sum_{target}_{rec}_{row}_{pos}", total, term)
                if target < K:
                    enc.fix(total, 1 if row == target else 0)
                else:
                    enc.equal(total, a[row][target - K])

    return enc, a, coeff


def decode_trit(model_set: set[int], trit: tuple[int, int, int]) -> int:
    values = [value for value, lit in enumerate(trit) if lit in model_set]
    if len(values) != 1:
        raise RuntimeError(f"invalid one-hot model values {values}")
    return values[0]


def verify_model(
    matrix: list[list[int]], coefficients: list[list[list[int]]]
) -> dict[str, object]:
    assert len(matrix) == K and all(len(row) == N for row in matrix)
    targets = []
    for target in range(N):
        recoveries = []
        used: set[int] = set()
        for rec in range(R):
            vector = coefficients[target][rec]
            support = {col for col, value in enumerate(vector) if value % P}
            assert target not in support
            assert not (used & support)
            used |= support
            lhs = [
                sum(vector[col] * matrix[row][col] for col in range(N)) % P
                for row in range(K)
            ]
            rhs = [matrix[row][target] % P for row in range(K)]
            assert lhs == rhs
            recoveries.append(
                {
                    "indices_1_based": [col + 1 for col in sorted(support)],
                    "coefficients_mod_3": [vector[col] for col in sorted(support)],
                }
            )
        targets.append(
            {
                "target_index_1_based": target + 1,
                "recovery_sets_excluding_singleton": recoveries,
            }
        )
    return {
        "rank_mod_3": K,
        "all_equations_verified_mod_3": True,
        "all_recovery_supports_pairwise_disjoint_per_target": True,
        "targets": targets,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--cnf", type=Path)
    parser.add_argument("--proof", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    enc, a, coeff = build_encoding()
    if args.cnf:
        enc.cnf.to_file(args.cnf)
        cnf_text = args.cnf.read_bytes()
    else:
        cnf_text = enc.cnf.to_dimacs().encode("ascii")
    report: dict[str, object] = {
        "provenance": "win-00084-p06-research-3dd502da7309",
        "encoding": "one-hot ternary truth tables and modulo-3 addition automata",
        "variables": enc.pool.top,
        "clauses": len(enc.cnf.clauses),
        "cnf_sha256": hashlib.sha256(cnf_text).hexdigest(),
        "solver": args.solver,
    }
    with Solver(
        name=args.solver,
        bootstrap_with=enc.cnf.clauses,
        with_proof=bool(args.proof),
    ) as solver:
        is_sat = solver.solve()
        report["status"] = "SAT" if is_sat else "UNSAT"
        if is_sat:
            model_set = {lit for lit in solver.get_model() if lit > 0}
            aa = [[decode_trit(model_set, a[row][col]) for col in range(5)] for row in range(K)]
            matrix = [
                [1 if row == col else 0 for col in range(K)] + aa[row]
                for row in range(K)
            ]
            cc = [
                [
                    [decode_trit(model_set, coeff[target][rec][col]) for col in range(N)]
                    for rec in range(R)
                ]
                for target in range(N)
            ]
            report["matrix_rows_mod_3"] = matrix
            report["verification"] = verify_model(matrix, cc)
        else:
            report["warning"] = (
                "UNSAT has no mathematical force until a proof certificate for the emitted "
                "CNF is generated and independently replayed."
            )
            if args.proof:
                proof = solver.get_proof()
                if proof is None:
                    raise RuntimeError(f"solver {args.solver} did not return a proof")
                proof_text = "\n".join(proof) + "\n"
                args.proof.write_text(proof_text, encoding="ascii")
                report["proof_file"] = str(args.proof)
                report["proof_lines"] = len(proof)
                report["proof_sha256"] = hashlib.sha256(
                    proof_text.encode("ascii")
                ).hexdigest()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
