#!/usr/bin/env python3
"""Small exhaustive tests for the Lehmer prime-set search."""

from __future__ import annotations

import itertools
import math
import unittest

from agent_hunter_search import primes_up_to, run_search
from agent_hunter_verify import independent_replay, is_prime_trial


DETERMINISTIC_KEYS = (
    "selection_attempts",
    "upper_bound_prunes",
    "surviving_nodes",
    "visited_by_cardinality",
    "ratio_eligible_sets",
    "ratio_eligible_by_cardinality",
    "two_adic_pass",
    "two_adic_pass_by_cardinality",
    "two_adic_survivors",
    "korselt_lcm_pass",
    "korselt_lcm_pass_by_cardinality",
    "exact_divisibility_pass",
    "solutions",
    "candidate_stream_sha256",
)


def brute_force_solutions(cap: int) -> list[dict[str, object]]:
    primes = [p for p in primes_up_to(cap) if p != 2]
    answers: list[dict[str, object]] = []
    for cardinality in range(2, len(primes) + 1):
        for chosen in itertools.combinations(primes, cardinality):
            n_value = math.prod(chosen)
            phi_value = math.prod(p - 1 for p in chosen)
            quotient, remainder = divmod(n_value - 1, phi_value)
            if remainder == 0:
                answers.append(
                    {
                        "primes": list(chosen),
                        "n": str(n_value),
                        "phi": str(phi_value),
                        "quotient": str(quotient),
                    }
                )
    return answers


class HunterTests(unittest.TestCase):
    def test_prime_generators_agree(self) -> None:
        sieve_primes = primes_up_to(347)
        trial_primes = [p for p in range(2, 348) if is_prime_trial(p)]
        self.assertEqual(sieve_primes, trial_primes)

    def test_search_matches_unpruned_power_set(self) -> None:
        result = run_search(30)
        self.assertEqual(result["solutions"], brute_force_solutions(30))
        self.assertEqual(result["exact_divisibility_pass"], 0)

    def test_independent_replay_matches_search(self) -> None:
        result = run_search(50)
        replay = independent_replay(50)
        for key in DETERMINISTIC_KEYS:
            self.assertEqual(result[key], replay[key], key)


if __name__ == "__main__":
    unittest.main(verbosity=2)
