#!/usr/bin/env python3
"""Exact verifier for the A383733 zero-set certificate.

The verifier parses only integer/sign data, reconstructs graph colourings, checks
the finite templates and the four exhaustive nonexistence cases, and prints
SHA-256 hashes.  It does not import discovery outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path


def fail(message: str) -> None:
    """Terminate verification with a nonzero status in every Python mode."""
    raise SystemExit("FAIL: " + message)


def require(condition: bool, message: str) -> None:
    """Optimization-safe replacement for correctness-critical assertions."""
    if not condition:
        fail(message)


def signs(word: str) -> tuple[int, ...]:
    if not isinstance(word, str) or not word or any(ch not in "+-" for ch in word):
        fail("a sign word must be a nonempty string over '+-'")
    return tuple(1 if ch == "+" else -1 for ch in word)


def edges(n: int) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    offsets = [1, 3] + ([n // 2] if n % 2 == 0 else [])
    for i in range(n):
        for offset in offsets:
            j = (i + offset) % n
            if i != j:
                result.add(tuple(sorted((i, j))))
    return result


def colors_from_d(d: tuple[int, ...]) -> tuple[int, ...]:
    if sum(d) % 3:
        fail("the sign word does not close modulo 3")
    colors = [0]
    for delta in d[:-1]:
        colors.append((colors[-1] + delta) % 3)
    return tuple(colors)


def direct_graph_check(d: tuple[int, ...]) -> None:
    c = colors_from_d(d)
    require(len(c) == len(d), "colour reconstruction changed the word length")
    require(
        all(c[i] != c[j] for i, j in edges(len(d))),
        "reconstructed colours are not proper on the literal graph",
    )


def sign_constraints(d: tuple[int, ...]) -> None:
    n = len(d)
    require(n >= 3, "a cyclic difference word must have length at least three")
    require(sum(d) % 3 == 0, "the difference word does not close modulo three")
    require(
        all(not (d[i] == d[(i + 1) % n] == d[(i + 2) % n]) for i in range(n)),
        "the difference word violates an offset-three edge",
    )
    if n % 2 == 0:
        m = n // 2
        require(
            all(sum(d[(i + j) % n] for j in range(m)) % 3 != 0 for i in range(n)),
            "the difference word violates a diameter edge",
        )


def balanced_word(plus: int, minus: int) -> tuple[int, ...]:
    if plus <= 0 or minus <= 0 or max(plus, minus) > 2 * min(plus, minus):
        fail("counts cannot be distributed into cyclic runs of length at most two")
    if plus >= minus:
        extra = plus - minus
        word = "++-" * extra + "+-" * (minus - extra)
    else:
        extra = minus - plus
        word = "--+" * extra + "-+" * (plus - extra)
    result = signs(word)
    require(sum(x == 1 for x in result) == plus, "balanced word has the wrong plus count")
    require(sum(x == -1 for x in result) == minus, "balanced word has the wrong minus count")
    return result


def odd_witness(n: int) -> tuple[int, ...]:
    if n % 6 == 1 and n >= 13:
        k = (n - 1) // 6
        counts = (3 * k + 2, 3 * k - 1)
    elif n % 6 == 3 and n >= 9:
        k = (n - 3) // 6
        counts = (3 * k, 3 * k + 3)
    elif n % 6 == 5 and n >= 11:
        k = (n - 5) // 6
        counts = (3 * k + 1, 3 * k + 4)
    else:
        fail(f"no odd family covers n={n}")
    d = balanced_word(*counts)
    require(len(d) == n, "odd-family word has the wrong length")
    sign_constraints(d)
    direct_graph_check(d)
    return d


def one_flip(a: tuple[int, ...]) -> tuple[int, ...]:
    b = (-a[0],) + a[1:]
    return a + b


def half_word(data: dict, m: int) -> tuple[int, ...]:
    seeds = data["even_one_flip"]["half_word_seeds"]
    if str(m) in seeds:
        return signs(seeds[str(m)])
    if m < 12:
        fail(f"no one-flip half-word for m={m}")
    r = 12 + ((m - 12) % 9)
    repetitions = (m - r) // 9
    prefix = signs(data["even_one_flip"]["extension_block"]) * repetitions
    return prefix + signs(seeds[str(r)])


def validate_half_template(a: tuple[int, ...]) -> None:
    require(len(a) >= 3, "one-flip half-word is too short")
    require(a[0] == 1, "one-flip half-word must start with plus")
    require(sum(a) % 3 == 1, "one-flip half-word has the wrong residue")
    require(a[1] != a[2], "one-flip half-word violates its initial seam predicate")
    require(a[-2] != a[-1], "one-flip half-word violates its terminal predicate")
    require(a[-1] != a[1], "one-flip half-word violates its cyclic seam predicate")
    require(
        all(not (a[i] == a[i + 1] == a[i + 2]) for i in range(len(a) - 2)),
        "one-flip half-word contains a forbidden linear triple",
    )
    d = one_flip(a)
    sign_constraints(d)
    direct_graph_check(d)


def exhaustive_exception(n: int) -> tuple[int, int]:
    """Enumerate all 2^n adjacent-difference assignments exactly."""
    closing = 0
    locally_valid = 0
    for d in product((-1, 1), repeat=n):
        if sum(d) % 3:
            continue
        closing += 1
        if any(d[i] == d[(i + 1) % n] == d[(i + 2) % n] for i in range(n)):
            continue
        locally_valid += 1
        if n % 2:
            fail(f"found a colouring sign word for claimed zero n={n}: {d}")
        m = n // 2
        if all(sum(d[(i + j) % n] for j in range(m)) % 3 for i in range(n)):
            fail(f"found a colouring sign word for claimed zero n={n}: {d}")
    return closing, locally_valid


def validate_schema(data: object) -> dict:
    """Reject missing, additional, or altered certificate fields exactly."""
    require(isinstance(data, dict), "certificate root must be an object")
    required = {
        "schema_version",
        "definition",
        "sign_encoding",
        "odd_families",
        "even_one_flip",
        "special_difference_words",
        "claimed_zeros",
    }
    require(set(data) == required, "certificate top-level schema mismatch")
    require(data["schema_version"] == 1, "certificate schema version mismatch")
    require(
        data["definition"]
        == {
            "vertex_set": "Z/nZ",
            "cyclic_offsets": [1, 3],
            "diameter_offset_for_even_n": "n/2",
            "colors": [0, 1, 2],
        },
        "graph definition mismatch",
    )
    require(
        data["sign_encoding"]
        == {
            "+": 1,
            "-": -1,
            "color_rule": "c[0]=0; c[i+1]=c[i]+d[i] mod 3",
        },
        "sign encoding mismatch",
    )
    require(
        data["odd_families"]
        == [
            {"n": "6*k+1", "range": "k>=2", "plus_count": "3*k+2", "minus_count": "3*k-1"},
            {"n": "6*k+3", "range": "k>=1", "plus_count": "3*k", "minus_count": "3*k+3"},
            {"n": "6*k+5", "range": "k>=1", "plus_count": "3*k+1", "minus_count": "3*k+4"},
        ],
        "odd-family metadata mismatch",
    )
    even = data["even_one_flip"]
    require(isinstance(even, dict), "even_one_flip must be an object")
    require(
        set(even)
        == {"rule", "extension_block", "extension_length", "half_word_seeds", "large_half_rule"},
        "even_one_flip schema mismatch",
    )
    require(
        even["rule"] == "d=a followed by a copy of a with its first sign flipped",
        "one-flip rule text mismatch",
    )
    require(even["extension_length"] == 9, "extension length mismatch")
    require(
        even["large_half_rule"]
        == "for m>=12, take r in [12,20] congruent to m mod 9 and prefix the r-seed by ((++-) repeated 3*((m-r)/9) times)",
        "large-half rule mismatch",
    )
    seeds = even["half_word_seeds"]
    require(isinstance(seeds, dict), "half_word_seeds must be an object")
    require(
        set(seeds) == {"3", "5", "7", "9", "11", *(str(m) for m in range(12, 21))},
        "half-word seed keys mismatch",
    )
    special = data["special_difference_words"]
    require(isinstance(special, dict) and set(special) == {"20"}, "special-word schema mismatch")
    require(data["claimed_zeros"] == [7, 8, 12, 16], "claimed zero list mismatch")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "certificates" / "zero_set_certificate.json",
    )
    args = parser.parse_args()
    try:
        raw = args.certificate.read_bytes()
    except OSError as exc:
        fail(f"cannot read certificate: {exc}")
    try:
        parsed = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON: {exc}")
    data = validate_schema(parsed)

    # Check every literal one-flip seed and the length-nine neutral extension.
    for key, word in data["even_one_flip"]["half_word_seeds"].items():
        a = signs(word)
        require(len(a) == int(key), f"half-word seed {key} has the wrong length")
        validate_half_template(a)
    extension = signs(data["even_one_flip"]["extension_block"])
    require(len(extension) == data["even_one_flip"]["extension_length"], "extension block length mismatch")
    require(sum(extension) % 3 == 0, "extension block is not residue-neutral")
    require(extension == signs("++-") * 3, "extension block is not the proved neutral prefix")

    # Instantiate every construction in a substantial diagnostic range.  The
    # infinite step itself is the checked template lemma (neutral prefix plus
    # preserved endpoint predicates), documented in the proof.
    for n in range(6, 1001):
        if n in data["claimed_zeros"]:
            continue
        if n % 2:
            odd_witness(n)
        elif n == 20:
            d = signs(data["special_difference_words"]["20"])
            sign_constraints(d)
            direct_graph_check(d)
        else:
            validate_half_template(half_word(data, n // 2))

    exception_counts = {str(n): exhaustive_exception(n) for n in data["claimed_zeros"]}
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "theorem": "three-colourability zero set for n>=6 is {7,8,12,16}",
        "finite_exception_enumeration": exception_counts,
        "diagnostic_witness_range": [6, 1000],
        "certificate_sha256": input_hash,
        "verifier_sha256": code_hash,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
