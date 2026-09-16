#!/usr/bin/env python3
"""Dedicated exact attacks on the universal modular-period theorem.

This is supporting falsification evidence for proof/modular_period_theorem.md,
not a proof of that theorem or of the original eight-zero assertion.
"""

import argparse
import json
import platform
import random

from numba import njit


@njit
def period_summary(k: int):
    modulus = 1 << k
    period = 3 * modulus
    x, y = 0, 1
    # Include both initialized indices when they vanish modulo the modulus.
    # The second clause matters only for k=0 (modulus one).
    zeros = [0]
    if 1 % modulus == 0:
        zeros.append(1)
    for n in range(2, period + 2):
        x, y = y, ((y ^ n) - x) % modulus
        if n < period and y == 0:
            zeros.append(n)
    return x, y, zeros


@njit
def all_states_word_cube(k: int):
    modulus = 1 << k
    checked = 0
    for x0 in range(modulus):
        for y0 in range(modulus):
            x, y = x0, y0
            for step in range(3 * modulus):
                j = step % modulus
                x, y = y, ((y ^ j) - x) % modulus
            if x != x0 or y != y0:
                return checked, x0, y0, x, y
            checked += 1
    return checked, -1, -1, -1, -1


@njit
def all_states_all_phases(k: int):
    modulus = 1 << k
    checked = 0
    for phase in range(modulus):
        for x0 in range(modulus):
            for y0 in range(modulus):
                x, y = x0, y0
                for step in range(3 * modulus):
                    j = (phase + step) % modulus
                    x, y = y, ((y ^ j) - x) % modulus
                if x != x0 or y != y0:
                    return checked, phase, x0, y0, x, y
                checked += 1
    return checked, -1, -1, -1, -1, -1


@njit
def exhaustive_lift_identities(max_base_k: int):
    checked = 0
    for base_k in range(max_base_k + 1):
        modulus = 1 << base_k
        lifted = 2 * modulus
        for j in range(modulus):
            for x in range(lifted):
                for y in range(lifted):
                    # T_(j+M) = H_(0,1) T_j.
                    lhs0 = y
                    lhs1 = ((y ^ (j + modulus)) - x) % lifted
                    rhs0 = y
                    rhs1 = (((y ^ j) - x) + modulus) % lifted
                    if lhs0 != rhs0 or lhs1 != rhs1:
                        return checked, base_k, j, x, y, 1
                    checked += 1
                    # T_j H_v = H_(beta,alpha+beta) T_j for all four v.
                    for alpha in range(2):
                        for beta in range(2):
                            in0 = (x + alpha * modulus) % lifted
                            in1 = (y + beta * modulus) % lifted
                            lhs0 = in1
                            lhs1 = ((in1 ^ j) - in0) % lifted
                            out0 = y
                            out1 = ((y ^ j) - x) % lifted
                            rhs0 = (out0 + beta * modulus) % lifted
                            rhs1 = (out1 + ((alpha + beta) % 2) * modulus) % lifted
                            if lhs0 != rhs0 or lhs1 != rhs1:
                                return checked, base_k, j, x, y, 2
                            checked += 1
    return checked, -1, -1, -1, -1, 0


def randomized_lift_attacks(seed: int, trials: int):
    rng = random.Random(seed)
    for trial in range(trials):
        base_k = rng.randrange(0, 62)
        modulus = 1 << base_k
        lifted = 2 * modulus
        j = rng.randrange(modulus)
        x = rng.randrange(lifted)
        y = rng.randrange(lifted)
        alpha = rng.randrange(2)
        beta = rng.randrange(2)
        upper = (y, ((y ^ (j + modulus)) - x) % lifted)
        translated = (y, (((y ^ j) - x) + modulus) % lifted)
        if upper != translated:
            return {"passed": False, "trial": trial, "kind": "upper-word", "k": base_k}
        lhs = (
            (y + beta * modulus) % lifted,
            ((((y + beta * modulus) % lifted) ^ j)
             - ((x + alpha * modulus) % lifted)) % lifted,
        )
        plain = (y, ((y ^ j) - x) % lifted)
        rhs = (
            (plain[0] + beta * modulus) % lifted,
            (plain[1] + ((alpha + beta) % 2) * modulus) % lifted,
        )
        if lhs != rhs:
            return {"passed": False, "trial": trial, "kind": "translation", "k": base_k}
    return {"passed": True, "seed": seed, "trials": trials, "base_k_range": [0, 61]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-sequence-k", type=int, default=25)
    parser.add_argument("--max-all-state-k", type=int, default=8)
    parser.add_argument("--max-all-phase-k", type=int, default=5)
    parser.add_argument("--max-lift-k", type=int, default=5)
    parser.add_argument("--seed", type=int, default=3307001)
    parser.add_argument("--random-trials", type=int, default=100000)
    parser.add_argument("--output")
    args = parser.parse_args()

    sequence = []
    for k in range(args.max_sequence_k + 1):
        x, y, zeros = period_summary(k)
        sequence.append({
            "k": k,
            "modulus": 1 << k,
            "period": 3 << k,
            "end_state": [x, y],
            "passed": [x, y] == [0, 1 % (1 << k)],
            "zero_residue_count": len(zeros),
            "zero_residues": list(zeros),
        })

    all_states = []
    for k in range(args.max_all_state_k + 1):
        result = all_states_word_cube(k)
        all_states.append({
            "k": k,
            "states_checked": result[0],
            "expected_states": (1 << k) ** 2,
            "passed": result[1] == -1,
            "counterexample": None if result[1] == -1 else list(result[1:]),
        })

    all_phases = []
    for k in range(args.max_all_phase_k + 1):
        result = all_states_all_phases(k)
        all_phases.append({
            "k": k,
            "state_phase_cases_checked": result[0],
            "expected_cases": (1 << k) ** 3,
            "passed": result[1] == -1,
            "counterexample": None if result[1] == -1 else list(result[1:]),
        })

    lift = exhaustive_lift_identities(args.max_lift_k)
    random_result = randomized_lift_attacks(args.seed, args.random_trials)
    record = {
        "schema_version": 1,
        "purpose": "falsification of the proved modular theorem and its lift identities",
        "sequence_period_tests": sequence,
        "all_initial_state_tests": all_states,
        "all_phase_tests": all_phases,
        "exhaustive_lift_identity_test": {
            "max_base_k": args.max_lift_k,
            "cases_checked": lift[0],
            "passed": lift[1] == -1,
            "counterexample": None if lift[1] == -1 else list(lift[1:]),
        },
        "randomized_high_bit_lift_test": random_result,
        "known_integer_zero_branches_checked": [0, 6, 11, 23, 36, 42, 48, 54],
        "boundary_inventory": [
            "modulus 1 (k=0)",
            "every initial state through the declared all-state frontier",
            "every time phase through the declared all-phase frontier",
            "both high-bit values in both state coordinates",
            "the seam between the lower and upper time words",
            "negative representatives are covered by residue-class invariance",
            "degeneracy/extremizer categories are inapplicable because this is a finite-state identity, not an optimization statement",
        ],
        "unsearched_scope": [
            f"sequence periods k>{args.max_sequence_k}",
            f"all initial states k>{args.max_all_state_k}",
            f"all phases k>{args.max_all_phase_k}",
            "the original integer zero assertion beyond the separate direct-search frontier",
        ],
        "python": platform.python_version(),
        "numba": __import__("numba").__version__,
    }
    assert all(item["passed"] for item in sequence)
    assert all(item["passed"] for item in all_states)
    assert all(item["passed"] for item in all_phases)
    assert record["exhaustive_lift_identity_test"]["passed"]
    assert random_result["passed"]
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
