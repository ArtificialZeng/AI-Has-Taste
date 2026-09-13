#!/usr/bin/env python3
"""Exact branch-and-bound search for a bounded Lehmer-totient counterexample.

The search space is a set of odd primes, not a range of integers.  Every
arithmetic decision used for pruning or accepting a candidate is an integer
comparison or an integer remainder.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
import time
from collections import Counter
from pathlib import Path


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_histogram(counter: Counter[int]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter)}


def run_search(cap: int) -> dict[str, object]:
    if cap < 3:
        raise ValueError("cap must be at least 3")

    primes = [p for p in primes_up_to(cap) if p != 2]
    prime_count = len(primes)
    all_mask = (1 << prime_count) - 1
    record_width = max(1, (prime_count + 7) // 8)

    # For i < j, the edge i--j is present exactly when p_i does not divide
    # p_j-1.  A Lehmer prime set must be a clique in this graph.
    compatible_after: list[int] = []
    incompatible_pairs = 0
    for i, p in enumerate(primes):
        mask = 0
        for j in range(i + 1, prime_count):
            if (primes[j] - 1) % p:
                mask |= 1 << j
            else:
                incompatible_pairs += 1
        compatible_after.append(mask)

    root_upper_n = math.prod(primes)
    root_upper_d = math.prod(p - 1 for p in primes)

    selection_attempts = 0
    upper_bound_prunes = 0
    surviving_nodes = 0
    ratio_eligible = 0
    two_adic_pass = 0
    korselt_lcm_pass = 0
    exact_divisibility_pass = 0
    visited_by_cardinality: Counter[int] = Counter()
    eligible_by_cardinality: Counter[int] = Counter()
    two_adic_by_cardinality: Counter[int] = Counter()
    korselt_by_cardinality: Counter[int] = Counter()
    candidate_digest = hashlib.sha256()
    two_adic_survivors: list[dict[str, object]] = []
    solutions: list[dict[str, object]] = []

    def visit(
        candidate_mask: int,
        selected_mask: int,
        selected_count: int,
        selected_n: int,
        selected_phi: int,
        selected_lcm: int,
        upper_n: int,
        upper_d: int,
    ) -> None:
        nonlocal selection_attempts
        nonlocal upper_bound_prunes
        nonlocal surviving_nodes
        nonlocal ratio_eligible
        nonlocal two_adic_pass
        nonlocal korselt_lcm_pass
        nonlocal exact_divisibility_pass

        # At a sibling step, tail_upper_* is the unreduced product ratio for
        # (selected primes) union (the current and all later candidates).
        tail_mask = candidate_mask
        tail_upper_n = upper_n
        tail_upper_d = upper_d

        while tail_mask:
            bit = tail_mask & -tail_mask
            i = bit.bit_length() - 1
            p = primes[i]
            tail_mask ^= bit
            selection_attempts += 1

            child_candidates = tail_mask & compatible_after[i]
            excluded = tail_mask ^ child_candidates

            child_upper_n = tail_upper_n
            child_upper_d = tail_upper_d
            excluded_work = excluded
            while excluded_work:
                excluded_bit = excluded_work & -excluded_work
                excluded_i = excluded_bit.bit_length() - 1
                child_upper_n //= primes[excluded_i]
                child_upper_d //= primes[excluded_i] - 1
                excluded_work ^= excluded_bit

            # Every factor p/(p-1) is greater than one.  Hence the ratio of
            # every extension is at most child_upper_n/child_upper_d.  A
            # Lehmer number must have n/phi(n)>2, so this prunes a whole
            # canonical subtree with an exact cross multiplication.
            if child_upper_n <= 2 * child_upper_d:
                upper_bound_prunes += 1
            else:
                child_mask = selected_mask | bit
                child_count = selected_count + 1
                child_n = selected_n * p
                child_phi = selected_phi * (p - 1)
                child_lcm = math.lcm(selected_lcm, p - 1)

                surviving_nodes += 1
                visited_by_cardinality[child_count] += 1

                if child_n > 2 * child_phi:
                    ratio_eligible += 1
                    eligible_by_cardinality[child_count] += 1
                    candidate_digest.update(
                        child_mask.to_bytes(record_width, "little")
                    )

                    n_minus_one = child_n - 1
                    two_part = child_phi & -child_phi
                    if n_minus_one % two_part == 0:
                        two_adic_pass += 1
                        two_adic_by_cardinality[child_count] += 1
                        selected_primes = [
                            primes[j]
                            for j in range(prime_count)
                            if child_mask & (1 << j)
                        ]
                        two_adic_survivors.append(
                            {
                                "primes": selected_primes,
                                "n": str(child_n),
                                "phi": str(child_phi),
                                "v2_phi": two_part.bit_length() - 1,
                                "korselt_lcm": str(child_lcm),
                                "korselt_remainder": str(n_minus_one % child_lcm),
                            }
                        )
                        if n_minus_one % child_lcm == 0:
                            korselt_lcm_pass += 1
                            korselt_by_cardinality[child_count] += 1
                            quotient, remainder = divmod(n_minus_one, child_phi)
                            if remainder == 0:
                                exact_divisibility_pass += 1
                                solutions.append(
                                    {
                                        "primes": selected_primes,
                                        "n": str(child_n),
                                        "phi": str(child_phi),
                                        "quotient": str(quotient),
                                    }
                                )

                visit(
                    child_candidates,
                    child_mask,
                    child_count,
                    child_n,
                    child_phi,
                    child_lcm,
                    child_upper_n,
                    child_upper_d,
                )

            # The next sibling excludes p, so remove its unreduced factor.
            tail_upper_n //= p
            tail_upper_d //= p - 1

    started = time.perf_counter()
    if root_upper_n > 2 * root_upper_d:
        visit(
            all_mask,
            0,
            0,
            1,
            1,
            1,
            root_upper_n,
            root_upper_d,
        )
    elapsed = time.perf_counter() - started

    total_pairs = prime_count * (prime_count - 1) // 2
    return {
        "schema": "lehmer-prime-set-search-v1",
        "arithmetic": "exact Python integers; no floating-point search decisions",
        "cap": cap,
        "largest_prime_in_universe": primes[-1] if primes else None,
        "odd_prime_count": prime_count,
        "compatible_pairs": total_pairs - incompatible_pairs,
        "incompatible_pairs": incompatible_pairs,
        "root_ratio_numerator": str(root_upper_n),
        "root_ratio_denominator": str(root_upper_d),
        "selection_attempts": selection_attempts,
        "upper_bound_prunes": upper_bound_prunes,
        "surviving_nodes": surviving_nodes,
        "visited_by_cardinality": stable_histogram(visited_by_cardinality),
        "ratio_eligible_sets": ratio_eligible,
        "ratio_eligible_by_cardinality": stable_histogram(
            eligible_by_cardinality
        ),
        "two_adic_pass": two_adic_pass,
        "two_adic_pass_by_cardinality": stable_histogram(
            two_adic_by_cardinality
        ),
        "two_adic_survivors": two_adic_survivors,
        "korselt_lcm_pass": korselt_lcm_pass,
        "korselt_lcm_pass_by_cardinality": stable_histogram(
            korselt_by_cardinality
        ),
        "exact_divisibility_pass": exact_divisibility_pass,
        "solutions": solutions,
        "candidate_stream_sha256": candidate_digest.hexdigest(),
        "search_code_sha256": file_sha256(Path(__file__).resolve()),
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "elapsed_seconds": round(elapsed, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, default=300)
    parser.add_argument(
        "--compact", action="store_true", help="print compact rather than indented JSON"
    )
    args = parser.parse_args()
    result = run_search(args.cap)
    json.dump(
        result,
        sys.stdout,
        sort_keys=True,
        indent=None if args.compact else 2,
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
