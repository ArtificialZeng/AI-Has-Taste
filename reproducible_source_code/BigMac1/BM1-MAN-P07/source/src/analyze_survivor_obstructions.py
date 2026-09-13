#!/usr/bin/env python3
"""Exact obstruction analysis for 2-adic Lehmer prime-set survivors.

All certification decisions use Python integers.  The optional adversarial
search exhausts compatible prime subsets under a small prime cap and is used
only to refute overgeneralized pattern lemmas.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from collections import Counter
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parent.parent


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


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


def factor_integer(value: int) -> dict[int, int]:
    if value < 1:
        raise ValueError("factorization requires a positive integer")
    factors: dict[int, int] = {}
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def factorization_text(factors: dict[int, int]) -> str:
    pieces = []
    for prime, exponent in sorted(factors.items()):
        pieces.append(str(prime) if exponent == 1 else f"{prime}^{exponent}")
    return " * ".join(pieces) if pieces else "1"


def check_compatibility(primes: list[int]) -> bool:
    return all((q - 1) % p != 0 for i, p in enumerate(primes) for q in primes[i + 1 :])


def analyze_prime_set(primes: list[int]) -> dict[str, Any]:
    if primes != sorted(set(primes)):
        raise ValueError("prime set must be strictly increasing")
    if any(p == 2 for p in primes):
        raise ValueError("the survivor representation expects odd primes")

    n_value = math.prod(primes)
    phi_value = math.prod(p - 1 for p in primes)
    lcm_value = math.lcm(*(p - 1 for p in primes))
    n_minus_one = n_value - 1
    factors = factor_integer(lcm_value)
    two_exponent = factors.get(2, 0)
    two_power = 2**two_exponent
    odd_radical = math.prod(q for q in factors if q != 2)

    failures: list[dict[str, Any]] = []
    primary_components: list[dict[str, Any]] = []
    for prime, required_exponent in sorted(factors.items()):
        actual_exponent = valuation(n_minus_one, prime)
        full_prime_power = prime**required_exponent
        first_failing_power = (
            prime ** (actual_exponent + 1)
            if actual_exponent < required_exponent
            else None
        )
        activators = [
            p
            for p in primes
            if valuation(p - 1, prime) >= required_exponent
        ]
        component = {
            "prime": prime,
            "required_exponent_in_L": required_exponent,
            "valuation_in_n_minus_1": actual_exponent,
            "full_prime_power": str(full_prime_power),
            "remainder_mod_full_prime_power": str(
                n_minus_one % full_prime_power
            ),
            "activating_selected_primes": activators,
        }
        primary_components.append(component)
        if first_failing_power is not None:
            nonactivators = [
                p for p in primes if (p - 1) % first_failing_power != 0
            ]
            failure = {
                **component,
                "first_failing_power": str(first_failing_power),
                "remainder_mod_first_failing_power": str(
                    n_minus_one % first_failing_power
                ),
                "nonactivator_product_mod_first_failing_power": str(
                    math.prod(nonactivators) % first_failing_power
                ),
                "nonactivating_selected_primes": nonactivators,
            }
            failures.append(failure)

    odd_failures = [entry for entry in failures if entry["prime"] != 2]
    minimum_witness = (
        min(
            odd_failures,
            key=lambda entry: (
                int(entry["first_failing_power"]),
                entry["prime"],
            ),
        )
        if odd_failures
        else None
    )
    odd_primes = [prime for prime in factors if prime != 2]

    return {
        "primes": primes,
        "cardinality": len(primes),
        "n": str(n_value),
        "phi": str(phi_value),
        "n_minus_one": str(n_minus_one),
        "ratio_feasible_n_gt_2phi": n_value > 2 * phi_value,
        "compatible": check_compatibility(primes),
        "L": str(lcm_value),
        "L_factorization": {
            str(prime): exponent for prime, exponent in sorted(factors.items())
        },
        "L_factorization_text": factorization_text(factors),
        "two_adic_exponent_in_L": two_exponent,
        "two_adic_component_passes": n_minus_one % two_power == 0,
        "odd_radical_of_L": str(odd_radical),
        "odd_radical_divides_n_minus_one": n_minus_one % odd_radical == 0,
        "smallest_odd_prime_divisor_of_L": min(odd_primes),
        "smallest_odd_prime_divisor_passes": (
            n_minus_one % min(odd_primes) == 0
        ),
        "primary_components": primary_components,
        "failing_primary_components": failures,
        "failing_odd_prime_powers": odd_failures,
        "minimum_odd_prime_power_witness": minimum_witness,
        "L_divides_n_minus_one": n_minus_one % lcm_value == 0,
        "L_remainder": str(n_minus_one % lcm_value),
    }


def validate_against_source(
    source: dict[str, Any], source_entry: dict[str, Any], analyzed: dict[str, Any]
) -> None:
    checks = {
        "n": analyzed["n"],
        "phi": analyzed["phi"],
        "korselt_lcm": analyzed["L"],
        "korselt_remainder": analyzed["L_remainder"],
    }
    for key, recomputed in checks.items():
        if str(source_entry[key]) != recomputed:
            raise ValueError(
                f"source mismatch for {source_entry['primes']}: "
                f"{key}={source_entry[key]!r}, recomputed={recomputed!r}"
            )
    expected_v2_phi = valuation(int(analyzed["phi"]), 2)
    if int(source_entry["v2_phi"]) != expected_v2_phi:
        raise ValueError("source v2(phi) does not match recomputation")
    if source.get("two_adic_pass") != len(source["two_adic_survivors"]):
        raise ValueError("source two_adic_pass count is inconsistent")
    if not analyzed["compatible"]:
        raise ValueError("source contains an incompatible prime set")
    if not analyzed["two_adic_component_passes"]:
        raise ValueError("source survivor fails its declared 2-adic filter")
    if not analyzed["ratio_feasible_n_gt_2phi"]:
        raise ValueError("source survivor fails the n/phi > 2 filter")
    if analyzed["L_divides_n_minus_one"]:
        raise ValueError("source survivor unexpectedly passes the Korselt lcm")


def brief_counterexample(primes: tuple[int, ...]) -> dict[str, Any]:
    analyzed = analyze_prime_set(list(primes))
    witness = analyzed["minimum_odd_prime_power_witness"]
    return {
        "primes": list(primes),
        "n": analyzed["n"],
        "phi": analyzed["phi"],
        "L": analyzed["L"],
        "L_factorization_text": analyzed["L_factorization_text"],
        "ratio_feasible_n_gt_2phi": analyzed["ratio_feasible_n_gt_2phi"],
        "odd_radical_divides_n_minus_one": analyzed[
            "odd_radical_divides_n_minus_one"
        ],
        "L_divides_n_minus_one": analyzed["L_divides_n_minus_one"],
        "minimum_odd_prime_power_witness": witness,
    }


def adversarial_small_cap_search(cap: int) -> dict[str, Any]:
    odd_primes = tuple(p for p in primes_up_to(cap) if p != 2)
    compatible_sets = 0
    two_adic_admissible = 0
    ratio_feasible_two_adic = 0
    lcm_pass = 0
    lift_only_failure = 0
    examples: dict[str, tuple[int, tuple[int, ...]]] = {}

    def retain(label: str, chosen: tuple[int, ...], n_value: int) -> None:
        candidate = (n_value, chosen)
        if label not in examples or candidate < examples[label]:
            examples[label] = candidate

    def visit(
        chosen: tuple[int, ...],
        candidates: tuple[int, ...],
        n_value: int,
        phi_value: int,
        lcm_value: int,
    ) -> None:
        nonlocal compatible_sets
        nonlocal two_adic_admissible
        nonlocal ratio_feasible_two_adic
        nonlocal lcm_pass
        nonlocal lift_only_failure

        for position, prime in enumerate(candidates):
            child = chosen + (prime,)
            child_n = n_value * prime
            child_phi = phi_value * (prime - 1)
            child_lcm = math.lcm(lcm_value, prime - 1)
            later = candidates[position + 1 :]
            child_candidates = tuple(
                q for q in later if (q - 1) % prime != 0
            )

            if len(child) >= 2:
                compatible_sets += 1
                two_part = child_phi & -child_phi
                if (child_n - 1) % two_part == 0:
                    two_adic_admissible += 1
                    ratio_feasible = child_n > 2 * child_phi
                    if ratio_feasible:
                        ratio_feasible_two_adic += 1

                    if not ({3, 5} <= set(child)):
                        retain("contains_3_and_5", child, child_n)

                    if (child_n - 1) % child_lcm == 0:
                        lcm_pass += 1
                        retain("all_admissible_sets_fail_L", child, child_n)
                    else:
                        factors = factor_integer(child_lcm)
                        odd_radical = math.prod(
                            q for q in factors if q != 2
                        )
                        if (child_n - 1) % odd_radical == 0:
                            lift_only_failure += 1
                            retain("odd_radical_always_fails", child, child_n)

                        failures = []
                        for q, exponent in factors.items():
                            if q == 2:
                                continue
                            actual = valuation(child_n - 1, q)
                            if actual < exponent:
                                failures.append((q ** (actual + 1), q))
                        if failures:
                            first_power, first_prime = min(failures)
                            if first_power != first_prime:
                                retain(
                                    "minimum_witness_is_always_prime",
                                    child,
                                    child_n,
                                )
                            if first_prime not in (7, 11):
                                retain(
                                    "minimum_witness_is_always_7_or_11",
                                    child,
                                    child_n,
                                )

            visit(
                child,
                child_candidates,
                child_n,
                child_phi,
                child_lcm,
            )

    visit((), odd_primes, 1, 1, 1)

    serialized_examples = {
        label: brief_counterexample(chosen)
        for label, (_, chosen) in sorted(examples.items())
    }
    return {
        "cap": cap,
        "odd_prime_count": len(odd_primes),
        "canonical_compatible_composite_sets": compatible_sets,
        "two_adic_admissible_sets": two_adic_admissible,
        "ratio_feasible_two_adic_sets": ratio_feasible_two_adic,
        "sets_passing_full_L": lcm_pass,
        "L_failing_sets_passing_odd_radical": lift_only_failure,
        "minimal_counterexamples_by_n": serialized_examples,
    }


def counter_to_json(counter: Counter[Any]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter)}


def build_report(source_path: Path, counterexample_cap: int) -> dict[str, Any]:
    source = json.loads(source_path.read_text(encoding="utf-8"))
    survivors = source.get("two_adic_survivors")
    if not isinstance(survivors, list) or not survivors:
        raise ValueError("source contains no two_adic_survivors")

    records = []
    minimum_witness_values: Counter[int] = Counter()
    minimum_witness_bases: Counter[int] = Counter()
    all_failing_bases: Counter[int] = Counter()
    failing_component_counts: Counter[int] = Counter()
    prefix_counts: Counter[tuple[int, ...]] = Counter()

    for index, source_entry in enumerate(survivors, start=1):
        analyzed = analyze_prime_set(list(source_entry["primes"]))
        validate_against_source(source, source_entry, analyzed)
        analyzed["source_index"] = index
        witness = analyzed["minimum_odd_prime_power_witness"]
        minimum_witness_values[int(witness["first_failing_power"])] += 1
        minimum_witness_bases[int(witness["prime"])] += 1
        for failure in analyzed["failing_odd_prime_powers"]:
            all_failing_bases[int(failure["prime"])] += 1
        failing_component_counts[len(analyzed["failing_odd_prime_powers"])] += 1
        prefix_counts[tuple(analyzed["primes"][:3])] += 1
        records.append(analyzed)

    radical_reject_count = sum(
        not record["odd_radical_divides_n_minus_one"] for record in records
    )
    smallest_odd_prime_reject_count = sum(
        not record["smallest_odd_prime_divisor_passes"] for record in records
    )
    minimum_witness_prime_count = sum(
        int(record["minimum_odd_prime_power_witness"]["first_failing_power"])
        == int(record["minimum_odd_prime_power_witness"]["prime"])
        for record in records
    )
    odd_nonsquarefree_L_count = sum(
        any(
            int(prime) != 2 and exponent > 1
            for prime, exponent in record["L_factorization"].items()
        )
        for record in records
    )

    adversarial = adversarial_small_cap_search(counterexample_cap)

    return {
        "schema": "lehmer-survivor-obstruction-analysis-v1",
        "arithmetic": "exact Python integers; no floating-point decisions",
        "source": {
            "path": str(source_path),
            "sha256": sha256_file(source_path),
            "cap": source["cap"],
            "two_adic_survivor_count": len(survivors),
        },
        "definitions": {
            "L": "lcm(p-1 : p in S)",
            "minimum_witness": (
                "minimum numerical odd prime power q^(v_q(n-1)+1) "
                "with v_q(n-1) < v_q(L)"
            ),
            "odd_radical": "product of distinct odd prime divisors of L",
        },
        "summary": {
            "records_certified": len(records),
            "odd_radical_reject_count": radical_reject_count,
            "lift_only_reject_count": len(records) - radical_reject_count,
            "minimum_witness_is_prime_count": minimum_witness_prime_count,
            "smallest_odd_prime_divisor_reject_count": (
                smallest_odd_prime_reject_count
            ),
            "all_contain_3_and_5_count": sum(
                {3, 5} <= set(record["primes"]) for record in records
            ),
            "odd_nonsquarefree_L_count": odd_nonsquarefree_L_count,
            "minimum_witness_value_frequency": counter_to_json(
                minimum_witness_values
            ),
            "minimum_witness_base_frequency": counter_to_json(
                minimum_witness_bases
            ),
            "all_failing_base_frequency": counter_to_json(all_failing_bases),
            "failing_odd_component_count_frequency": counter_to_json(
                failing_component_counts
            ),
            "first_three_prime_prefix_frequency": {
                ",".join(map(str, key)): prefix_counts[key]
                for key in sorted(prefix_counts)
            },
        },
        "exact_modular_obstruction": {
            "statement": (
                "For q^a exactly dividing L, let A={p in S: "
                "p congruent to 1 mod q^a}. Then L divides n-1 only if "
                "the product over S minus A is 1 mod q^a. Requiring this "
                "for every primary component of L is also sufficient by CRT."
            ),
            "search_use": (
                "At a partial node, compute subset-product residues reachable "
                "from compatible extensions. If the inverse current residue "
                "is absent for one active primary modulus, the node is "
                "exactly impossible. Ignoring conflicts among future primes "
                "gives a safe over-approximation for pruning."
            ),
            "novelty_status": (
                "elementary reformulation and proposed pruning rule; "
                "no novelty claim"
            ),
        },
        "adversarial_small_cap_search": adversarial,
        "records": records,
        "script": {
            "path": str(SCRIPT_PATH),
            "sha256": sha256_file(SCRIPT_PATH),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        },
    }


def markdown_table_row(values: list[Any]) -> str:
    return "| " + " | ".join(str(value) for value in values) + " |"


def render_markdown(report: dict[str, Any]) -> str:
    source = report["source"]
    summary = report["summary"]
    adversarial = report["adversarial_small_cap_search"]
    lines = [
        "# Exact odd-prime-power obstructions for the cap-347 survivors",
        "",
        "## Certified finite result",
        "",
        f"All {summary['records_certified']} 2-adic survivors in "
        f"**{source['path']}** were recomputed from their prime sets. "
        "Every stored value of n, phi, L, the 2-adic exponent, and the "
        "Korselt remainder agrees with the independent factorization below.",
        "",
        f"All {summary['odd_radical_reject_count']} sets already fail modulo "
        "an odd prime dividing L. None requires only a higher odd-prime-power "
        "lifting obstruction. This is a certified statement about these "
        "records, not a theorem for arbitrary compatible prime sets.",
        "",
        "Minimum witness means the least numerical odd prime power "
        "q^(v_q(n-1)+1) whose required exponent occurs in L.",
        "",
        "## Aggregate counts",
        "",
        markdown_table_row(["Quantity", "Count"]),
        markdown_table_row(["---", "---:"]),
        markdown_table_row(
            ["Odd-radical rejections", summary["odd_radical_reject_count"]]
        ),
        markdown_table_row(
            [
                "Minimum witness already prime",
                summary["minimum_witness_is_prime_count"],
            ]
        ),
        markdown_table_row(
            [
                "Smallest odd divisor of L already rejects",
                summary["smallest_odd_prime_divisor_reject_count"],
            ]
        ),
        markdown_table_row(
            ["Sets containing both 3 and 5", summary["all_contain_3_and_5_count"]]
        ),
        markdown_table_row(
            [
                "Sets with a repeated odd prime in L",
                summary["odd_nonsquarefree_L_count"],
            ]
        ),
        "",
        "Minimum-witness frequency:",
        "",
        markdown_table_row(["Witness", "Frequency"]),
        markdown_table_row(["---:", "---:"]),
    ]
    for witness, count in summary["minimum_witness_value_frequency"].items():
        lines.append(markdown_table_row([witness, count]))

    lines.extend(
        [
            "",
            "## Per-set exact certificates",
            "",
            markdown_table_row(
                [
                    "ID",
                    "Prime set",
                    "Factorization of L",
                    "Minimum witness",
                    "v_q(n-1) / v_q(L)",
                    "(n-1) mod witness",
                    "All failing odd bases",
                ]
            ),
            markdown_table_row(
                ["---:", "---", "---", "---:", "---", "---:", "---"]
            ),
        ]
    )
    for record in report["records"]:
        witness = record["minimum_odd_prime_power_witness"]
        failing_bases = ",".join(
            str(entry["prime"])
            for entry in record["failing_odd_prime_powers"]
        )
        lines.append(
            markdown_table_row(
                [
                    record["source_index"],
                    "{" + ",".join(map(str, record["primes"])) + "}",
                    record["L_factorization_text"],
                    witness["first_failing_power"],
                    (
                        f"{witness['valuation_in_n_minus_1']} / "
                        f"{witness['required_exponent_in_L']}"
                    ),
                    witness["remainder_mod_first_failing_power"],
                    failing_bases,
                ]
            )
        )

    examples = adversarial["minimal_counterexamples_by_n"]
    lines.extend(
        [
            "",
            "## Adversarial attacks on tempting uniform lemmas",
            "",
            f"The script exhaustively enumerated all "
            f"{adversarial['canonical_compatible_composite_sets']:,} "
            f"compatible composite prime sets with primes at most "
            f"{adversarial['cap']}. Exactly "
            f"{adversarial['two_adic_admissible_sets']:,} pass their "
            "2-adic component; this small-cap search does not impose the "
            "ratio n/phi>2 unless explicitly stated.",
            "",
            markdown_table_row(["Tempting lemma", "Status", "Exact breaker"]),
            markdown_table_row(["---", "---", "---"]),
            markdown_table_row(
                [
                    "Compatibility plus 2-adic admissibility forces L to fail",
                    "Refuted",
                    str(examples["all_admissible_sets_fail_L"]["primes"])
                    + " (n="
                    + examples["all_admissible_sets_fail_L"]["n"]
                    + " passes L)",
                ]
            ),
            markdown_table_row(
                [
                    "If L fails, the odd radical of L must already fail",
                    "Refuted",
                    str(examples["odd_radical_always_fails"]["primes"])
                    + " (first failure 9)",
                ]
            ),
            markdown_table_row(
                [
                    "The minimum odd witness is always prime",
                    "Refuted",
                    str(examples["minimum_witness_is_always_prime"]["primes"])
                    + " (minimum witness 9)",
                ]
            ),
            markdown_table_row(
                [
                    "Every admissible set contains both 3 and 5",
                    "Refuted",
                    str(examples["contains_3_and_5"]["primes"]),
                ]
            ),
            markdown_table_row(
                [
                    "For ratio-feasible cap-347 survivors the witness is 7 or 11",
                    "Refuted inside source",
                    "{3,5,17,53,227} has witness 13",
                ]
            ),
            markdown_table_row(
                [
                    "The smallest odd prime divisor of L always rejects",
                    "Refuted inside source",
                    "record 12 passes modulo 7 and first fails modulo 11",
                ]
            ),
            "",
            "The observations that all 38 source sets contain 3 and 5 and "
            "all 38 fail the odd radical remain finite patterns only.",
            "",
            "## Reusable modular obstruction",
            "",
            "For q^a exactly dividing L, let",
            "",
            r"\[A_{q^a}=\{p\in S:p\equiv1\pmod{q^a}\}.\]",
            "",
            "Every activated prime contributes 1 to the product modulo q^a, "
            "so the primary Korselt condition is exactly",
            "",
            r"\[\prod_{p\in S\setminus A_{q^a}}p\equiv1\pmod{q^a}.\]",
            "",
            "At a partial search node, a safe exact pruning test is therefore "
            "to compute the subset-product residues reachable from compatible "
            "extensions. If the inverse of the current residue is absent for "
            "one active q^a, no extension can satisfy L | n-1. Ignoring "
            "mutual conflicts among future primes only enlarges the reachable "
            "set, so non-reachability remains a valid certificate. This is an "
            "elementary reformulation and proposed exact pruning rule, not a "
            "novelty claim or a global solution.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "results/agent_hunter_cap347.json",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=PROJECT_ROOT / "results/survivor_obstructions_cap347.json",
    )
    parser.add_argument(
        "--markdown-output",
        type=Path,
        default=PROJECT_ROOT / "results/survivor_obstructions_cap347.md",
    )
    parser.add_argument("--counterexample-cap", type=int, default=120)
    args = parser.parse_args()

    report = build_report(args.input.resolve(), args.counterexample_cap)
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    args.markdown_output.write_text(
        render_markdown(report),
        encoding="utf-8",
    )
    print("SURVIVOR OBSTRUCTION ANALYSIS: PASS")
    print("records_certified:", report["summary"]["records_certified"])
    print(
        "odd_radical_reject_count:",
        report["summary"]["odd_radical_reject_count"],
    )
    print(
        "minimum_witness_value_frequency:",
        json.dumps(
            report["summary"]["minimum_witness_value_frequency"],
            sort_keys=True,
        ),
    )
    print(
        "adversarial_compatible_sets:",
        report["adversarial_small_cap_search"][
            "canonical_compatible_composite_sets"
        ],
    )
    print(
        "adversarial_two_adic_sets:",
        report["adversarial_small_cap_search"]["two_adic_admissible_sets"],
    )


if __name__ == "__main__":
    main()
