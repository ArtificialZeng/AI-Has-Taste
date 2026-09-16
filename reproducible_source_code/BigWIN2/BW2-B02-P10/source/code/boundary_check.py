#!/usr/bin/env python3
"""Exhaustively attack the boundary-word classification of CRIM positions.

Canonical words are empty or begin with 0 and end with 1.  A move deletes one
letter and then removes leading 1s and trailing 0s.  This checker computes the
P/N recurrence directly and compares it with the proposed end-peeling formula.
It does not import either partition evaluator.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from pathlib import Path
from typing import Iterable, Sequence


def canonicalize(word: str) -> str:
    return word.lstrip("1").rstrip("0")


def followers(word: str) -> set[str]:
    return {canonicalize(word[:i] + word[i + 1 :]) for i in range(len(word))}


def run_pairs(word: str) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    i = 0
    while i < len(word):
        zeros = 0
        while i < len(word) and word[i] == "0":
            zeros += 1
            i += 1
        ones = 0
        while i < len(word) and word[i] == "1":
            ones += 1
            i += 1
        if zeros == 0 or ones == 0:
            raise ValueError("input is not a canonical nonempty word")
        pairs.append((zeros, ones))
    return pairs


def run_pairs_with_positions(
    word: str,
) -> tuple[list[tuple[int, int]], list[tuple[list[int], list[int]]]]:
    pairs: list[tuple[int, int]] = []
    positions: list[tuple[list[int], list[int]]] = []
    i = 0
    while i < len(word):
        zeros: list[int] = []
        while i < len(word) and word[i] == "0":
            zeros.append(i)
            i += 1
        ones: list[int] = []
        while i < len(word) and word[i] == "1":
            ones.append(i)
            i += 1
        pairs.append((len(zeros), len(ones)))
        positions.append((zeros, ones))
    return pairs, positions


def peel_data(word: str) -> tuple[int, int, int, list[tuple[int, int]]]:
    pairs = run_pairs(word)
    left = 0
    while left < len(pairs) and pairs[left][0] == 1 and pairs[left][1] % 2 == 1:
        left += 1
    right = 0
    while (
        right < len(pairs)
        and pairs[-1 - right][0] % 2 == 1
        and pairs[-1 - right][1] == 1
    ):
        right += 1
    return min(len(pairs), left + right), left, right, pairs


def peel_count(word: str) -> int:
    if not word:
        return 0
    return peel_data(word)[0]


def predicted_losing(word: str) -> bool:
    return len(word) % 2 == 0 and peel_count(word) % 2 == 0


def delete_at(word: str, position: int) -> str:
    return canonicalize(word[:position] + word[position + 1 :])


def builder_odd_witness(word: str) -> str:
    """Return the follower selected by the Builder lemma's case split."""
    if len(word) % 2 != 1 or not word:
        raise ValueError("Builder witness requires a nonempty odd canonical word")
    m_value, left, right, pairs = peel_data(word)
    indexed_pairs, positions = run_pairs_with_positions(word)
    if indexed_pairs != pairs:
        raise AssertionError("internal run parser disagreement")
    core_first = left
    core_last = len(pairs) - right - 1
    core_length = core_last - core_first + 1
    if core_length <= 0:
        raise AssertionError("odd word cannot have an empty core")

    def remove(pair_index: int, symbol: int) -> str:
        run = positions[pair_index][symbol]
        if not run:
            raise AssertionError("selected empty run")
        return delete_at(word, run[0])

    if core_length > 1:
        if m_value % 2 == 1:
            if left > 0:
                return remove(left - 1, 1)
            return remove(len(pairs) - right, 0)

        a, b = pairs[core_first]
        if a == 1:  # Necessarily b is even because this is the first core pair.
            candidates = (remove(core_first, 0), remove(core_first, 1))
            for candidate in candidates:
                if predicted_losing(candidate):
                    return candidate
            raise AssertionError("consecutive-M exceptional pair supplied no witness")
        if (a, b) == (2, 1):
            return remove(core_first, 1)
        if a == 2 and b % 2 == 1:
            return remove(core_first, 1)
        return remove(core_first, 0)

    a, b = pairs[core_first]
    if m_value % 2 == 0:
        if a % 2 == 1:  # Includes a=1, b even.
            return remove(core_first, 0)
        return remove(core_first, 1)

    if a == 1:  # Then b is even.
        return remove(core_first, 1)
    if b == 1:  # Then a is even.
        return remove(core_first, 0)
    if a % 2 == 1:  # a>=3 odd and b even.
        if right > 0:
            return remove(core_first + 1, 0)
        return remove(core_first - 1, 1)
    # a even and b>=3 odd.
    if left > 0:
        return remove(core_first - 1, 1)
    return remove(core_first + 1, 0)


def words_of_length(length: int) -> Iterable[str]:
    if length < 2:
        return
    for middle in itertools.product("01", repeat=length - 2):
        yield "0" + "".join(middle) + "1"


def update_hash(hasher: "hashlib._Hash", word: str) -> None:
    hasher.update((word + "\n").encode("ascii"))


def run(max_length: int) -> dict:
    start = time.time()
    exact_p = {""}
    exact_digest = hashlib.sha256()
    predicted_digest = hashlib.sha256()
    update_hash(exact_digest, "")
    update_hash(predicted_digest, "")
    mismatches: list[dict] = []
    odd_domination_failures: list[str] = []
    builder_witness_failures: list[dict] = []
    rows = []
    total = 1

    for length in range(2, max_length + 1):
        count = 0
        exact_count = 0
        predicted_count = 0
        for word in words_of_length(length):
            count += 1
            is_p = all(child not in exact_p for child in followers(word))
            formula = predicted_losing(word)
            if is_p:
                exact_p.add(word)
                exact_count += 1
                update_hash(exact_digest, word)
            if formula:
                predicted_count += 1
                update_hash(predicted_digest, word)
            if is_p != formula and len(mismatches) < 20:
                mismatches.append(
                    {"word": word, "exact_losing": is_p, "formula_losing": formula}
                )
            if length % 2 == 1 and not any(
                predicted_losing(child) for child in followers(word)
            ):
                if len(odd_domination_failures) < 20:
                    odd_domination_failures.append(word)
            if length % 2 == 1:
                witness = builder_odd_witness(word)
                if witness not in followers(word) or not predicted_losing(witness):
                    if len(builder_witness_failures) < 20:
                        builder_witness_failures.append(
                            {
                                "word": word,
                                "witness": witness,
                                "is_follower": witness in followers(word),
                                "witness_length": len(witness),
                                "witness_M": peel_count(witness),
                            }
                        )
        total += count
        rows.append(
            {
                "length": length,
                "canonical_words": count,
                "exact_losing": exact_count,
                "formula_losing": predicted_count,
            }
        )

    return {
        "schema_version": 1,
        "engine": "boundary_word_exhaustive_recurrence",
        "max_length": max_length,
        "canonical_word_count_including_empty": total,
        "mismatch_count_retained": len(mismatches),
        "mismatches": mismatches,
        "odd_domination_failure_count_retained": len(odd_domination_failures),
        "odd_domination_failures": odd_domination_failures,
        "builder_witness_failure_count_retained": len(builder_witness_failures),
        "builder_witness_failures": builder_witness_failures,
        "exact_losing_sha256": exact_digest.hexdigest(),
        "formula_losing_sha256": predicted_digest.hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "elapsed_seconds": round(time.time() - start, 6),
        "by_length": rows,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.max_length < 2:
        parser.error("--max-length must be at least 2")
    result = run(args.max_length)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return (
        0
        if not result["mismatches"]
        and not result["odd_domination_failures"]
        and not result["builder_witness_failures"]
        else 2
    )


if __name__ == "__main__":
    raise SystemExit(main())
