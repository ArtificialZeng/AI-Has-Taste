#!/usr/bin/env python3
"""Independent formula checker for modular-theorem falsification evidence."""

import json
import random
import sys

from numba import njit


@njit
def sequence_via_and(k: int):
    modulus = 1 << k
    period = 3 * modulus
    x, y = 0, 1
    zeros = [0]
    if 1 % modulus == 0:
        zeros.append(1)
    for n in range(2, period + 2):
        # For nonnegative residues, y xor n = y+n-2*(y&n), also after
        # reduction modulo a power of two.
        x, y = y, (y + n - 2 * (y & n) - x) % modulus
        if n < period and y == 0:
            zeros.append(n)
    return x, y, zeros


@njit
def all_states_via_and(k: int, phases: bool):
    modulus = 1 << k
    phase_stop = modulus if phases else 1
    checked = 0
    for phase in range(phase_stop):
        for x0 in range(modulus):
            for y0 in range(modulus):
                x, y = x0, y0
                for step in range(3 * modulus):
                    j = (phase + step) % modulus
                    x, y = y, (y + j - 2 * (y & j) - x) % modulus
                assert x == x0 and y == y0
                checked += 1
    return checked


@njit
def exhaustive_lifts_via_and(max_base_k: int):
    """Recompute both lift identities without using direct XOR."""
    checked = 0
    for base_k in range(max_base_k + 1):
        modulus = 1 << base_k
        lifted = 2 * modulus
        for j in range(modulus):
            for x in range(lifted):
                for y in range(lifted):
                    upper_xor = y + j + modulus - 2 * (y & (j + modulus))
                    lower_xor = y + j - 2 * (y & j)
                    lhs0 = y
                    lhs1 = (upper_xor - x) % lifted
                    rhs0 = y
                    rhs1 = (lower_xor - x + modulus) % lifted
                    assert lhs0 == rhs0 and lhs1 == rhs1
                    checked += 1
                    for alpha in range(2):
                        for beta in range(2):
                            in0 = (x + alpha * modulus) % lifted
                            in1 = (y + beta * modulus) % lifted
                            in1_xor_j = in1 + j - 2 * (in1 & j)
                            lhs0 = in1
                            lhs1 = (in1_xor_j - in0) % lifted
                            out0 = y
                            out1 = (lower_xor - x) % lifted
                            rhs0 = (out0 + beta * modulus) % lifted
                            rhs1 = (
                                out1 + ((alpha + beta) % 2) * modulus
                            ) % lifted
                            assert lhs0 == rhs0 and lhs1 == rhs1
                            checked += 1
    return checked


def randomized_lifts_via_and(seed: int, trials: int):
    """Replay the seeded high-bit attack with the AND identity."""
    rng = random.Random(seed)
    for _ in range(trials):
        base_k = rng.randrange(0, 62)
        modulus = 1 << base_k
        lifted = 2 * modulus
        j = rng.randrange(modulus)
        x = rng.randrange(lifted)
        y = rng.randrange(lifted)
        alpha = rng.randrange(2)
        beta = rng.randrange(2)

        upper_xor = y + j + modulus - 2 * (y & (j + modulus))
        lower_xor = y + j - 2 * (y & j)
        upper = (y, (upper_xor - x) % lifted)
        translated = (y, (lower_xor - x + modulus) % lifted)
        assert upper == translated

        in0 = (x + alpha * modulus) % lifted
        in1 = (y + beta * modulus) % lifted
        in1_xor_j = in1 + j - 2 * (in1 & j)
        lhs = (in1, (in1_xor_j - in0) % lifted)
        plain = (y, (lower_xor - x) % lifted)
        rhs = (
            (plain[0] + beta * modulus) % lifted,
            (plain[1] + ((alpha + beta) % 2) * modulus) % lifted,
        )
        assert lhs == rhs


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/modular-falsification-evidence.json"
with open(path, encoding="utf-8") as handle:
    claimed = json.load(handle)
assert claimed["schema_version"] == 1

for item in claimed["sequence_period_tests"]:
    x, y, zeros = sequence_via_and(item["k"])
    assert [x, y] == item["end_state"]
    assert list(zeros) == item["zero_residues"]
    assert len(zeros) == item["zero_residue_count"]
    assert item["passed"] is True

for item in claimed["all_initial_state_tests"]:
    assert all_states_via_and(item["k"], False) == item["states_checked"] == item["expected_states"]
    assert item["passed"] is True and item["counterexample"] is None

for item in claimed["all_phase_tests"]:
    assert all_states_via_and(item["k"], True) == item["state_phase_cases_checked"] == item["expected_cases"]
    assert item["passed"] is True and item["counterexample"] is None

lift_claim = claimed["exhaustive_lift_identity_test"]
assert lift_claim["passed"] is True and lift_claim["counterexample"] is None
assert exhaustive_lifts_via_and(lift_claim["max_base_k"]) == lift_claim["cases_checked"]

random_claim = claimed["randomized_high_bit_lift_test"]
assert random_claim["passed"] is True
randomized_lifts_via_and(random_claim["seed"], random_claim["trials"])

known = set(claimed["known_integer_zero_branches_checked"])
for item in claimed["sequence_period_tests"]:
    if item["period"] > max(known):
        assert known.issubset(set(item["zero_residues"]))

print(json.dumps({
    "status": "PASS",
    "sequence_max_k": claimed["sequence_period_tests"][-1]["k"],
    "all_state_max_k": claimed["all_initial_state_tests"][-1]["k"],
    "all_phase_max_k": claimed["all_phase_tests"][-1]["k"],
    "lift_cases_recomputed": lift_claim["cases_checked"],
    "random_lift_trials_recomputed": random_claim["trials"],
}, separators=(",", ":")))
