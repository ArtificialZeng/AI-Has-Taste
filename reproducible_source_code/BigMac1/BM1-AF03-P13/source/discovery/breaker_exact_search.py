#!/usr/bin/env python3
"""Independent exact breaker search for length-10 generalized snake words.

Discovery arithmetic is integer-only through construction of h* and 24! L(t).
mpmath is used only after exact reduction to locate roots of a quintic.  The
search deliberately visits all 2^10 words; no symmetry is trusted to establish
completeness.

Source conventions used here:
  * word length m is the number of L/R letters (Preliminaries, Definition 2.1);
  * dim O(P(w)) = 2m+4;
  * h* is computed with the corrected final-sub-ladder recurrence in arXiv v2.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
from functools import lru_cache
from math import comb
from pathlib import Path

import mpmath as mp
import networkx as nx


SWAP = str.maketrans("LR", "RL")


def poly_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    c = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        c[i] += value
    for i, value in enumerate(b):
        c[i] += value
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return tuple(c)


def poly_neg(a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-value for value in a)


def poly_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    c = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            c[i + j] += left * right
    return tuple(c)


def poly_shift(a: tuple[int, ...], shift: int) -> tuple[int, ...]:
    """Ascending coefficients of p(x+shift)."""
    out = [0] * len(a)
    for i, coefficient in enumerate(a):
        for j in range(i + 1):
            out[j] += coefficient * comb(i, j) * shift ** (i - j)
    return tuple(out)


def poly_divexact(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    remainder = list(a)
    quotient = [0] * (len(a) - len(b) + 1)
    while remainder and remainder[-1] == 0:
        remainder.pop()
    while len(remainder) >= len(b):
        assert remainder[-1] % b[-1] == 0
        value = remainder[-1] // b[-1]
        offset = len(remainder) - len(b)
        quotient[offset] = value
        for j, coefficient in enumerate(b):
            remainder[offset + j] -= value * coefficient
        while remainder and remainder[-1] == 0:
            remainder.pop()
    if remainder:
        raise ArithmeticError(f"nonzero exact-division remainder: {remainder}")
    return tuple(quotient)


@lru_cache(maxsize=None)
def ladder_hstar(length: int) -> tuple[int, ...]:
    """Narayana polynomial N_{length+2}, ascending coefficients."""
    n = length + 2
    return tuple(comb(n, k + 1) * comb(n, k) // n for k in range(n))


@lru_cache(maxsize=None)
def hstar(word: str) -> tuple[int, ...]:
    """Theorem 4.14 of arXiv v2, using the final maximal sub-ladder."""
    length = len(word)
    if length == 0:
        return (1, 1)
    run = 1
    while run < length and word[-run - 1] == word[-1]:
        run += 1
    if run == length:
        return ladder_hstar(length)
    prefix = word[:-run]
    first = poly_mul(hstar(prefix[:-1]), ladder_hstar(run))
    second = poly_mul(hstar(prefix), ladder_hstar(run - 1))
    overlap = poly_mul((1, 1), poly_mul(hstar(prefix[:-1]), ladder_hstar(run - 1)))
    return poly_add(poly_add(first, second), poly_neg(overlap))


def ehrhart_numerator(word: str) -> tuple[int, ...]:
    """Ascending coefficients of d! L(w;t), where d=2 len(word)+4."""
    dimension = 2 * len(word) + 4
    out = [0] * (dimension + 1)
    for i, h_i in enumerate(hstar(word)):
        term = (1,)
        # d! binom(t+d-i,d) = product_{q=1-i}^{d-i} (t+q).
        for q in range(1 - i, dimension - i + 1):
            term = poly_mul(term, (q, 1))
        for j, coefficient in enumerate(term):
            out[j] += h_i * coefficient
    return tuple(out)


def fixed_y_factor(length: int) -> tuple[int, ...]:
    """At even length, known roots after x=t+(m+4)/2 and y=x^2."""
    if length % 2:
        raise ValueError("this reduction is implemented only for even length")
    radius = (length + 2) // 2
    out = (1,)
    for k in range(radius + 1):
        out = poly_mul(out, (-k * k, 1))
    return out


def reduced_quintic(word: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return G(y), K(y), where d!L(x-center)=G(x^2)=B(y)K(y)."""
    length = len(word)
    center_shift = -(length + 4) // 2  # t=x-(m+4)/2
    shifted = poly_shift(ehrhart_numerator(word), center_shift)
    odd_nonzero = [(i, value) for i, value in enumerate(shifted) if i % 2 and value]
    if odd_nonzero:
        raise ArithmeticError(f"failed exact symmetry for {word}: {odd_nonzero}")
    g_poly = shifted[::2]
    return g_poly, poly_divexact(g_poly, fixed_y_factor(length))


def orbit(word: str) -> tuple[str, ...]:
    complement = word.translate(SWAP)
    return tuple(sorted({word, word[::-1], complement, complement[::-1]}))


def cover_graph(word: str) -> nx.DiGraph:
    """Directed Hasse graph from the source recursive definition."""
    graph = nx.DiGraph()
    graph.add_nodes_from(range(2 * len(word) + 4))
    graph.add_edges_from([(3, 1), (3, 2), (1, 0), (2, 0)])
    for n, letter in enumerate(word, start=1):
        graph.add_edges_from([(2 * n + 3, 2 * n + 1), (2 * n + 3, 2 * n + 2)])
        switch = n >= 2 and word[n - 2] != letter
        target = 2 * n - 1 if (n == 1 and letter == "L") or switch else 2 * n
        graph.add_edge(2 * n + 2, target)
    return graph


def sha256_coefficients(coefficients: tuple[int, ...]) -> str:
    payload = json.dumps(coefficients, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def locate_maximum_modulus(k_poly: tuple[int, ...], dps: int) -> tuple[mp.mpf, list[mp.mpc]]:
    mp.mp.dps = dps
    roots = mp.polyroots([mp.mpf(value) for value in reversed(k_poly)], maxsteps=1000)
    return max(abs(root) for root in roots), roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=10)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/breaker_length10_exact.jsonl"),
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("experiments/breaker_length10_summary.json"),
    )
    args = parser.parse_args()
    if args.length != 10:
        raise SystemExit("this breaker endpoint is intentionally pinned to length 10")

    words = ["".join(bits) for bits in itertools.product("LR", repeat=args.length)]
    exact_hstar = {word: hstar(word) for word in words}
    complement_equal = all(exact_hstar[word] == exact_hstar[word.translate(SWAP)] for word in words)
    reversal_equal = all(exact_hstar[word] == exact_hstar[word[::-1]] for word in words)
    complement_isomorphic = []
    reversal_isomorphic = []
    for word in words:
        graph = cover_graph(word)
        complement_isomorphic.append(nx.is_isomorphic(graph, cover_graph(word.translate(SWAP))))
        reversal_isomorphic.append(nx.is_isomorphic(graph, cover_graph(word[::-1])))

    rows = []
    violating_words = []
    maximum = None
    for word in words:
        numerator = ehrhart_numerator(word)
        g_poly, k_poly = reduced_quintic(word)
        max_y_modulus, roots = locate_maximum_modulus(k_poly, args.dps)
        x_excess = mp.sqrt(max_y_modulus) - 6
        if max_y_modulus > 36:
            violating_words.append(word)
        if maximum is None or max_y_modulus > maximum[0]:
            maximum = (max_y_modulus, word, k_poly, roots)
        rows.append(
            {
                "word": word,
                "canonical_orbit_representative": min(orbit(word)),
                "orbit": orbit(word),
                "hstar_coefficients_ascending": exact_hstar[word],
                "ehrhart_numerator_coefficients_ascending": numerator,
                "ehrhart_numerator_sha256": sha256_coefficients(numerator),
                "shifted_y_coefficients_ascending": g_poly,
                "residual_quintic_coefficients_ascending": k_poly,
                "numeric_max_y_modulus": mp.nstr(max_y_modulus, args.dps - 10),
                "numeric_x_radius_excess": mp.nstr(x_excess, args.dps - 10),
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")

    assert maximum is not None
    orbit_map = {min(orbit(word)): orbit(word) for word in words}
    bad_orbits = sorted({min(orbit(word)) for word in violating_words})
    summary = {
        "endpoint": "all generalized snake words with exactly 10 L/R letters",
        "word_count": len(words),
        "dimension": 24,
        "corrected_center": -7,
        "corrected_radius": 6,
        "orbit_count_under_complement_and_reversal": len(orbit_map),
        "distinct_exact_hstar_count": len(set(exact_hstar.values())),
        "orbit_size_counts": {
            str(size): sum(len(members) == size for members in orbit_map.values())
            for size in sorted({len(members) for members in orbit_map.values()})
        },
        "exact_hstar_complement_equal_all_words": complement_equal,
        "exact_hstar_reversal_equal_all_words": reversal_equal,
        "directed_cover_graph_complement_isomorphic_word_count": sum(complement_isomorphic),
        "directed_cover_graph_reversal_isomorphic_word_count": sum(reversal_isomorphic),
        "directed_cover_graph_first_reversal_nonisomorphic_word": next(
            (word for word, valid in zip(words, reversal_isomorphic) if not valid), None
        ),
        "numeric_violating_word_count": len(violating_words),
        "numeric_violating_words": violating_words,
        "numeric_violating_orbit_representatives": bad_orbits,
        "worst_word": maximum[1],
        "worst_residual_quintic_coefficients_ascending": maximum[2],
        "worst_numeric_max_y_modulus": mp.nstr(maximum[0], args.dps - 10),
        "worst_numeric_x_radius_excess": mp.nstr(mp.sqrt(maximum[0]) - 6, args.dps - 10),
        "fixed_boundary_y_roots": [k * k for k in range(7)],
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "mpmath": mp.__version__,
            "networkx": nx.__version__,
            "command": "python discovery/breaker_exact_search.py --length 10 --dps 80",
        },
        "notes": [
            "All 1024 words were visited; symmetries were not used to establish completeness.",
            "All polynomial fields are exact integers. Fields prefixed numeric_ are localization only.",
            "Complement is a poset isomorphism in all 1024 directed-cover-graph checks.",
            "Reversal preserves h* in all 1024 exact checks but is not generally a poset isomorphism; completeness did not use it.",
            "The exact counterexample certificate is verified separately by breaker_verify_counterexample.py.",
        ],
    }
    args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
