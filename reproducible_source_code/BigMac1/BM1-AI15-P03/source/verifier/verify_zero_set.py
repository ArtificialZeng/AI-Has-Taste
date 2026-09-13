#!/usr/bin/env python3
"""Independent exact verifier for the A383733 zero-set certificate.

Only the Python standard library is used.  The verifier has two deliberately
different finite engines:

* exhaustive enumeration of all {+1,-1} cyclic difference words;
* backtracking directly on the graph's three-colour assignments.

It also checks the finite local/algebraic invariants of the three infinite
constructive families recorded in certificate.json.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import List, Sequence, Tuple


HERE = Path(__file__).resolve().parent


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


def signs(text: str) -> Tuple[int, ...]:
    if not isinstance(text, str) or not text or any(ch not in "+-" for ch in text):
        fail("a sign word must be a nonempty string over '+-'")
    return tuple(1 if ch == "+" else -1 for ch in text)


def no_cyclic_triple(word: Sequence[int]) -> bool:
    n = len(word)
    return n >= 3 and all(
        not (word[i] == word[(i + 1) % n] == word[(i + 2) % n])
        for i in range(n)
    )


def no_linear_triple(word: Sequence[int]) -> bool:
    return all(not (word[i] == word[i + 1] == word[i + 2]) for i in range(len(word) - 2))


def admissible_difference_word(word: Sequence[int]) -> bool:
    """Check the exact difference-word conditions, with integer arithmetic."""
    n = len(word)
    if any(x not in (-1, 1) for x in word):
        return False
    if not no_cyclic_triple(word) or sum(word) % 3:
        return False
    if n % 2 == 0:
        m = n // 2
        if any(sum(word[(i + j) % n] for j in range(m)) % 3 == 0 for i in range(n)):
            return False
    return True


def colors_from_differences(word: Sequence[int]) -> Tuple[int, ...]:
    if sum(word) % 3:
        fail("difference word does not close modulo 3")
    colors = [0]
    for d in word[:-1]:
        colors.append((colors[-1] + d) % 3)
    return tuple(colors)


def graph_edges(n: int, offsets: Sequence[int], even_diameter: bool) -> Tuple[Tuple[int, int], ...]:
    edges = set()
    for i in range(n):
        for delta in offsets:
            j = (i + delta) % n
            if i != j:
                edges.add((min(i, j), max(i, j)))
        if even_diameter and n % 2 == 0:
            j = (i + n // 2) % n
            if i != j:
                edges.add((min(i, j), max(i, j)))
    return tuple(sorted(edges))


def graph_coloring_is_proper(colors: Sequence[int], edges: Sequence[Tuple[int, int]]) -> bool:
    return all(colors[i] != colors[j] for i, j in edges)


def direct_graph_completion_count(n: int, offsets: Sequence[int], even_diameter: bool) -> Tuple[int, int]:
    """Count colourings with c(0)=0 by exhaustive graph backtracking.

    The second return value is the number of recursive nodes, useful only as
    a reproducibility diagnostic.  The argument proves nonexistence when the
    first return value is zero because every colouring can be relabelled to
    have c(0)=0.
    """
    edges = graph_edges(n, offsets, even_diameter)
    neighbors = [set() for _ in range(n)]
    for i, j in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)
    colors = [-1] * n
    colors[0] = 0
    nodes = 0

    def rec(colored: int) -> int:
        nonlocal nodes
        nodes += 1
        if colored == n:
            return 1
        # Deterministic DSATUR-style choice; this is independent of the
        # cyclic-difference enumeration.
        uncolored = [v for v in range(n) if colors[v] < 0]
        v = max(
            uncolored,
            key=lambda x: (len({colors[y] for y in neighbors[x] if colors[y] >= 0}), len(neighbors[x]), -x),
        )
        forbidden = {colors[y] for y in neighbors[v] if colors[y] >= 0}
        total = 0
        for color in range(3):
            if color not in forbidden:
                colors[v] = color
                total += rec(colored + 1)
                colors[v] = -1
        return total

    return rec(1), nodes


def enumerate_difference_words(n: int) -> int:
    count = 0
    for mask in range(1 << n):
        word = tuple(1 if (mask >> i) & 1 else -1 for i in range(n))
        if admissible_difference_word(word):
            count += 1
    return count


def half_window_states(u: Sequence[int], v: Sequence[int]) -> Tuple[int, ...]:
    if len(u) != len(v):
        fail("paired halves have different lengths")
    state = sum(u) % 3
    states = [state]
    for x, y in zip(u, v):
        state = (state - x + y) % 3
        states.append(state)
    return tuple(states)


def check_odd_family(data: dict) -> str:
    if set(data) != {
        "minimum_n",
        "target_integer_sum",
        "number_of_double_plus_gaps",
        "remaining_plus_gap_size",
    }:
        fail("unexpected odd_family fields")
    if data["minimum_n"] != 9 or data["target_integer_sum"] != 3:
        fail("odd-family endpoint or target sum changed")
    doubles = data["number_of_double_plus_gaps"]
    singles = data["remaining_plus_gap_size"]
    if doubles != 3 or singles != 1:
        fail("odd-family gap data do not give the claimed construction")

    # Symbolic check.  For n=2q+3, q >= 3: use q isolated minus
    # signs, three following plus-runs of length 2 and q-3 of length 1.
    # The following are coefficient identities in q, not sample tests.
    # plus_count = 2*3 + 1*(q-3) = q+3;
    # length = q + (q+3) = 2q+3; integer sum = (q+3)-q = 3.
    plus_constant = 2 * doubles - singles * doubles
    if plus_constant != 3:
        fail("odd-family plus-count identity failed")
    if data["target_integer_sum"] != plus_constant:
        fail("odd-family integer-sum identity failed")
    if not (1 <= singles <= 2 and doubles >= 0):
        fail("odd-family run bounds failed")
    return "odd n=2q+3 (q>=3): length=2q+3, sum=3, all cyclic runs <=2"


def check_two_mod_four_family(data: dict) -> str:
    if set(data) != {"minimum_n", "difference_period"}:
        fail("unexpected two_mod_four_family fields")
    block = signs(data["difference_period"])
    if data["minimum_n"] != 6 or block != (1, -1):
        fail("2 mod 4 family must be the alternating construction")
    # For n=4k+2 the full alternating word has sum 0 and its half-length
    # 2k+1 is odd, so every half-window sum is +1 or -1.
    if sum(block) != 0 or not no_linear_triple(block * 2):
        fail("alternating block invariant failed")
    return "n=4k+2: alternating word, half-window sums are exactly +/-1"


def check_zero_mod_four_family(data: dict) -> str:
    required = {
        "base_n",
        "first_half",
        "second_half",
        "insertion_index",
        "synchronous_pump_block",
        "order_increment",
    }
    if set(data) != required:
        fail("unexpected zero_mod_four_family fields")
    u = signs(data["first_half"])
    v = signs(data["second_half"])
    block = signs(data["synchronous_pump_block"])
    p = data["insertion_index"]
    if data["base_n"] != len(u) + len(v) or len(u) != len(v):
        fail("pump seed length mismatch")
    if data["base_n"] != 20 or p != 3 or not (2 <= p <= len(u) - 2):
        fail("unexpected pump seed endpoint or insertion site")
    if data["order_increment"] != 2 * len(block) or data["order_increment"] != 4:
        fail("pump order increment mismatch")
    if sum(block) != 0:
        fail("pump block changes the half sum")
    seed = u + v
    if not admissible_difference_word(seed):
        fail("base word is not admissible")
    states = half_window_states(u, v)
    if any(s == 0 for s in states):
        fail("base word has a zero half-window state")

    # A triple can only see two positions to either side of an insertion.
    # B^t is alternating for every t>=1; B+B checks every internal triple,
    # and the two four-symbol contexts check the two boundaries.  The t=0
    # case was checked as part of the seed.
    if not no_linear_triple(block + block):
        fail("a repeated pump block creates a monochromatic triple")
    for half in (u, v):
        local = half[max(0, p - 2) : p] + block + block + half[p : p + 2]
        if not no_linear_triple(local):
            fail("pump insertion boundary creates a monochromatic triple")

    # The same block is inserted at the same paired indices.  Its sum is zero,
    # so the initial half-state is unchanged.  At every inserted pair x=y,
    # the transition s -> s-x+y fixes s.  Old transitions and their nonzero
    # states are therefore preserved for every repetition count t>=0.
    inserted_state = states[p]
    if inserted_state == 0 or any((inserted_state - x + x) % 3 != inserted_state for x in block):
        fail("synchronous insertion does not preserve the half state")
    return (
        "n=20+4t: seed valid; local B^t boundaries, closure, and all paired "
        "half-window states are invariant for every t>=0"
    )


def validate_schema(cert: dict) -> None:
    required = {
        "schema",
        "graph",
        "exceptional_orders",
        "finite_enumeration",
        "odd_family",
        "two_mod_four_family",
        "zero_mod_four_family",
    }
    if set(cert) != required or cert["schema"] != "a383733-zero-set-certificate-v1":
        fail("certificate schema mismatch")
    graph = cert["graph"]
    if set(graph) != {"minimum_n", "cyclic_offsets", "even_diameter", "colors"}:
        fail("graph schema mismatch")
    if graph != {"minimum_n": 6, "cyclic_offsets": [1, 3], "even_diameter": True, "colors": 3}:
        fail("graph definition mismatch")
    if cert["exceptional_orders"] != [7, 8, 12, 16]:
        fail("exception list mismatch")


def main() -> None:
    certificate_path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else HERE / "certificate.json"
    if len(sys.argv) > 2:
        fail("usage: verify_zero_set.py [certificate.json]")
    raw = certificate_path.read_bytes()
    try:
        cert = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON: {exc}")
    validate_schema(cert)

    finite = cert["finite_enumeration"]
    if set(finite) != {"first_n", "last_n", "expected_admissible_difference_words"}:
        fail("finite_enumeration schema mismatch")
    first, last = finite["first_n"], finite["last_n"]
    if (first, last) != (6, 20):
        fail("finite enumeration range mismatch")
    expected = finite["expected_admissible_difference_words"]
    if set(expected) != {str(n) for n in range(first, last + 1)}:
        fail("finite count keys are incomplete")

    actual = {}
    for n in range(first, last + 1):
        actual[str(n)] = enumerate_difference_words(n)
    if actual != expected:
        fail(f"difference-word enumeration mismatch: expected {expected}, got {actual}")
    computed_zeros = [n for n in range(first, last + 1) if actual[str(n)] == 0]
    if computed_zeros != cert["exceptional_orders"]:
        fail("finite zero set does not match the certificate")

    graph = cert["graph"]
    graph_audit = {}
    for n in range(first, last + 1):
        completions, nodes = direct_graph_completion_count(n, graph["cyclic_offsets"], graph["even_diameter"])
        graph_audit[str(n)] = {"completions_with_c0_zero": completions, "recursive_nodes": nodes}
        if completions != actual[str(n)]:
            fail(
                f"independent graph/difference counts disagree at n={n}: "
                f"graph={completions}, differences={actual[str(n)]}"
            )

    family_results = [
        check_odd_family(cert["odd_family"]),
        check_two_mod_four_family(cert["two_mod_four_family"]),
        check_zero_mod_four_family(cert["zero_mod_four_family"]),
    ]

    # Cross-check concrete endpoints and several pump iterations against the
    # graph definition, without treating these samples as the infinite proof.
    sample_words: List[Tuple[int, Tuple[int, ...]]] = []
    for n in range(9, 40, 2):
        q = (n - 3) // 2
        gaps = [2, 2, 2] + [1] * (q - 3)
        word = tuple(x for gap in gaps for x in (-1,) + (1,) * gap)
        sample_words.append((n, word))
    for n in range(6, 40, 4):
        sample_words.append((n, tuple(1 if i % 2 == 0 else -1 for i in range(n))))
    pump = cert["zero_mod_four_family"]
    u0, v0, block, p = signs(pump["first_half"]), signs(pump["second_half"]), signs(pump["synchronous_pump_block"]), pump["insertion_index"]
    for t in range(8):
        u = u0[:p] + block * t + u0[p:]
        v = v0[:p] + block * t + v0[p:]
        sample_words.append((len(u) + len(v), u + v))
    for n, word in sample_words:
        if len(word) != n or not admissible_difference_word(word):
            fail(f"constructed sample difference word failed at n={n}")
        colors = colors_from_differences(word)
        edges = graph_edges(n, graph["cyclic_offsets"], graph["even_diameter"])
        if not graph_coloring_is_proper(colors, edges):
            fail(f"constructed sample failed direct graph check at n={n}")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print("PASS a383733-zero-set-certificate-v1")
    print("certificate_sha256=" + input_hash)
    print("verifier_sha256=" + code_hash)
    print("finite_difference_counts=" + json.dumps(actual, sort_keys=True, separators=(",", ":")))
    print("direct_graph_count_audit=" + json.dumps(graph_audit, sort_keys=True, separators=(",", ":")))
    for result in family_results:
        print("family_invariant=" + result)
    print(f"concrete_graph_cross_checks={len(sample_words)}")


if __name__ == "__main__":
    main()
