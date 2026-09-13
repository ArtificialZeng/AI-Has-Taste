#!/usr/bin/env python3
"""Independent exact replay of the bounded Lehmer prime-set search.

This verifier intentionally uses trial-division prime generation and tuple
candidate lists, rather than the search program's sieve and bitset graph.
"""

from __future__ import annotations

import argparse
import fractions
import hashlib
import json
import math
import platform
import sys
from collections import Counter
from pathlib import Path


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def stable(counter: Counter[int]) -> dict[str, int]:
    return {str(k): counter[k] for k in sorted(counter)}


def independent_replay(cap: int) -> dict[str, object]:
    primes = tuple(p for p in range(3, cap + 1, 2) if is_prime_trial(p))
    index = {p: i for i, p in enumerate(primes)}
    width = max(1, (len(primes) + 7) // 8)

    selected_attempts = 0
    prunes = 0
    survivors = 0
    eligible = 0
    pass_two = 0
    pass_lcm = 0
    pass_full = 0
    visit_hist: Counter[int] = Counter()
    eligible_hist: Counter[int] = Counter()
    two_hist: Counter[int] = Counter()
    lcm_hist: Counter[int] = Counter()
    stream = hashlib.sha256()
    two_survivors: list[dict[str, object]] = []
    witnesses: list[dict[str, object]] = []

    def replay(
        chosen: tuple[int, ...],
        candidates: tuple[int, ...],
        n_value: int,
        phi_value: int,
        korselt_modulus: int,
        upper_num: int,
        upper_den: int,
    ) -> None:
        nonlocal selected_attempts, prunes, survivors, eligible
        nonlocal pass_two, pass_lcm, pass_full

        tail_upper_num = upper_num
        tail_upper_den = upper_den
        for position, p in enumerate(candidates):
            selected_attempts += 1
            later = candidates[position + 1 :]
            child_candidates = tuple(q for q in later if (q - 1) % p != 0)

            child_upper_num = tail_upper_num
            child_upper_den = tail_upper_den
            compatible_set = set(child_candidates)
            for q in later:
                if q not in compatible_set:
                    child_upper_num //= q
                    child_upper_den //= q - 1

            if child_upper_num <= 2 * child_upper_den:
                prunes += 1
            else:
                child_chosen = chosen + (p,)
                child_n = n_value * p
                child_phi = phi_value * (p - 1)
                child_lcm = math.lcm(korselt_modulus, p - 1)
                card = len(child_chosen)
                survivors += 1
                visit_hist[card] += 1

                if child_n > 2 * child_phi:
                    eligible += 1
                    eligible_hist[card] += 1
                    mask = sum(1 << index[q] for q in child_chosen)
                    stream.update(mask.to_bytes(width, "little"))
                    difference = child_n - 1
                    two_part = child_phi & -child_phi
                    if difference % two_part == 0:
                        pass_two += 1
                        two_hist[card] += 1
                        two_survivors.append(
                            {
                                "primes": list(child_chosen),
                                "n": str(child_n),
                                "phi": str(child_phi),
                                "v2_phi": two_part.bit_length() - 1,
                                "korselt_lcm": str(child_lcm),
                                "korselt_remainder": str(difference % child_lcm),
                            }
                        )
                        if difference % child_lcm == 0:
                            pass_lcm += 1
                            lcm_hist[card] += 1
                            quotient, remainder = divmod(difference, child_phi)
                            if remainder == 0:
                                # Independent evaluation of the same condition:
                                # prod p/(p-1)-1/phi must be an integer.
                                rational_value = fractions.Fraction(1, 1)
                                for q in child_chosen:
                                    rational_value *= fractions.Fraction(q, q - 1)
                                rational_value -= fractions.Fraction(1, child_phi)
                                if rational_value.denominator != 1:
                                    raise AssertionError("two exact evaluators disagree")
                                if rational_value.numerator != quotient:
                                    raise AssertionError("quotient evaluators disagree")
                                pass_full += 1
                                witnesses.append(
                                    {
                                        "primes": list(child_chosen),
                                        "n": str(child_n),
                                        "phi": str(child_phi),
                                        "quotient": str(quotient),
                                    }
                                )

                replay(
                    child_chosen,
                    child_candidates,
                    child_n,
                    child_phi,
                    child_lcm,
                    child_upper_num,
                    child_upper_den,
                )

            tail_upper_num //= p
            tail_upper_den //= p - 1

    root_num = math.prod(primes)
    root_den = math.prod(p - 1 for p in primes)
    if root_num > 2 * root_den:
        replay((), primes, 1, 1, 1, root_num, root_den)

    return {
        "selection_attempts": selected_attempts,
        "upper_bound_prunes": prunes,
        "surviving_nodes": survivors,
        "visited_by_cardinality": stable(visit_hist),
        "ratio_eligible_sets": eligible,
        "ratio_eligible_by_cardinality": stable(eligible_hist),
        "two_adic_pass": pass_two,
        "two_adic_pass_by_cardinality": stable(two_hist),
        "two_adic_survivors": two_survivors,
        "korselt_lcm_pass": pass_lcm,
        "korselt_lcm_pass_by_cardinality": stable(lcm_hist),
        "exact_divisibility_pass": pass_full,
        "solutions": witnesses,
        "candidate_stream_sha256": stream.hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    expected = json.loads(args.result.read_text(encoding="utf-8"))
    actual = independent_replay(int(expected["cap"]))

    mismatches = {
        key: {"expected": expected.get(key), "actual": actual[key]}
        for key in actual
        if expected.get(key) != actual[key]
    }
    if mismatches:
        json.dump({"status": "FAIL", "mismatches": mismatches}, sys.stdout, indent=2)
        sys.stdout.write("\n")
        raise SystemExit(1)

    report = {
        "status": "PASS",
        "cap": expected["cap"],
        "exact_divisibility_pass": actual["exact_divisibility_pass"],
        "candidate_stream_sha256": actual["candidate_stream_sha256"],
        "result_file_sha256": file_sha256(args.result),
        "verifier_code_sha256": file_sha256(Path(__file__).resolve()),
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        },
    }
    json.dump(report, sys.stdout, sort_keys=True, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
