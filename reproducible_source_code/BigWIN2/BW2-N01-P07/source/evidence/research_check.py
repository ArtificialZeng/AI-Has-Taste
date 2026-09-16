"""Exact finite attacks on the written proof; run from any working directory.

Command: python3 evidence/research_check.py
The structural proof, not these finite checks, establishes the all-n theorem.
Uses only Python's standard library. No prior check implementation is imported.
"""
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOB = "newwin-00001-p07-research-4c610e4f54cc"


def direct_sum(blocks):
    out = []
    offset = 0
    for block in blocks:
        out.extend(offset + value for value in block)
        offset += len(block)
    return tuple(out)


def encode(parts):
    return direct_sum(tuple(range(2, d + 1)) + (1,) for d in parts)


def decode(p):
    parts = []
    while p:
        d = p.index(min(p)) + 1
        assert p[:d] == tuple(range(2, d + 1)) + (1,)
        parts.append(d)
        p = tuple(value - d for value in p[d:])
        assert sorted(p) == list(range(1, len(p) + 1))
    return tuple(parts)


def cube(p):
    # Three literal evaluations. No direct-sum or block-cube shortcut.
    return tuple(p[p[p[i] - 1] - 1] for i in range(len(p)))


def brute_2143(p):
    # Direct rank comparison, independent of the fast inversion-based search.
    for values in combinations(p, 4):
        order = sorted(values)
        if tuple(order.index(v) + 1 for v in values) == (2, 1, 4, 3):
            return True
    return False


def witness_2143(p):
    """Return indices a<b<c<d with p[b]<p[a]<p[d]<p[c], or None.

    Before each c, retain an inversion a<b<c whose upper value p[a] is
    smallest among all earlier inversions. An inversion c<d completes
    2143 exactly if p[d] is above that smallest upper value. This search
    has no knowledge of compositions, cyclic blocks, or direct sums.
    """
    best = None
    for c in range(2, len(p) - 1):
        b = c - 1
        for a in range(b):
            if p[a] > p[b] and (best is None or p[a] < p[best[0]]):
                best = (a, b)
        if best is not None:
            for d in range(c + 1, len(p)):
                if p[best[0]] < p[d] < p[c]:
                    a, b = best
                    assert a < b < c < d
                    assert p[b] < p[a] < p[d] < p[c]
                    return a, b, c, d
    return None


def compositions(n):
    # Every nonempty composition has a unique first positive part.
    if n == 0:
        yield ()
    else:
        for first in range(1, n + 1):
            for tail in compositions(n - first):
                yield (first,) + tail


def test_parts(parts):
    p = encode(parts)
    assert decode(p) == parts
    assert encode(decode(p)) == p
    q = cube(p)
    formula = direct_sum(
        tuple(1 + ((i + 3) % d) for i in range(d)) for d in parts)
    assert q == formula
    result = witness_2143(q) is None
    assert result == (sum(d not in (1, 3) for d in parts) <= 1), parts
    return result


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def formal_counts(limit):
    # First-part recurrence for compositions with zero/exactly one exception.
    ordinary = [1] + [0] * limit
    one_exception = [0] * (limit + 1)
    for n in range(1, limit + 1):
        for d in (1, 3):
            if d <= n:
                ordinary[n] += ordinary[n - d]
                one_exception[n] += one_exception[n - d]
        one_exception[n] += sum(
            ordinary[n - d] for d in range(1, n + 1) if d not in (1, 3))
    dp = [a + e for a, e in zip(ordinary, one_exception)]

    # Common denominator for A + E*A^2, A=1/(1-z-z^3),
    # E=z^2+z^4/(1-z), constructed by exact polynomial arithmetic.
    base = [1, -1, 0, -1]
    denominator = polymul([1, -1], polymul(base, base))
    numerator = polymul([1, -1], base)
    numerator[2] += 1
    numerator[3] -= 1
    numerator[4] += 1
    series = []
    for n in range(limit + 1):
        rhs = numerator[n] if n < len(numerator) else 0
        rhs -= sum(denominator[k] * series[n - k]
                   for k in range(1, min(n + 1, len(denominator))))
        series.append(rhs)
    assert dp == series
    return dp, numerator, denominator


def main():
    source_hash = sha256((ROOT / "source.md").read_bytes()).hexdigest()
    assert source_hash == "f55a25a1a14dbeef692d590d1d55513ad3e234065d61da1ae130416417c7a59e"
    rows = []
    detector_tests = 0
    for n in range(8):
        for p in permutations(range(1, n + 1)):
            assert (witness_2143(p) is not None) == brute_2143(p), p
            detector_tests += 1
    assert detector_tests == 5914

    coefficients, numerator, denominator = formal_counts(100)
    for n in range(13, 17):
        checked = accepted = 0
        for parts in compositions(n):
            accepted += test_parts(parts)
            checked += 1
        assert checked == 2 ** (n - 1)
        assert accepted == coefficients[n]
        rows.append({"n": n, "compositions": checked, "cube_avoiders": accepted})
    assert sum(row["compositions"] for row in rows) == 61440

    alphabet = (1, 2, 3, 4, 5, 7, 16, 31)
    bounded_lists = 0
    for length in range(5):
        for parts in product(alphabet, repeat=length):
            test_parts(parts)
            bounded_lists += 1
    assert bounded_lists == 4681

    # Attack the direct-sum lemma on blocks that need not be cyclic or cubed.
    blocks = [p for n in range(1, 5) for p in permutations(range(1, n + 1))
              if not brute_2143(p)]
    assert len(blocks) == 32
    generic_tests = 0
    for length in range(4):
        for summands in product(blocks, repeat=length):
            q = direct_sum(summands)
            inversion_blocks = sum(list(p) != sorted(p) for p in summands)
            assert (witness_2143(q) is None) == (inversion_blocks <= 1), summands
            generic_tests += 1
    assert generic_tests == 33825

    large_cases = [(d,) for d in range(41, 257)] + [
        (1000,), (4096,), (3,) * 100,
        (3,) * 100 + (2,) + (3,) * 100,
        (4,) + (1,) * 80 + (2,),
        (2,) + (3,) * 80 + (2,),
        (31, 1, 3, 31),
    ]
    for parts in large_cases:
        test_parts(parts)

    # Explicit boundaries and pitfalls: the cube cannot be inverted on its own.
    boundaries = [(), (1,), (3,), (1, 1, 1), (2,), (2, 2), (3, 3), (2, 3, 2)]
    boundary_rows = []
    for parts in boundaries:
        avoids = test_parts(parts)
        p = encode(parts)
        q = cube(p)
        boundary_rows.append({"parts": parts, "permutation": p, "cube": q,
                              "avoids_2143": avoids, "witness": witness_2143(q)})
    assert cube(encode((3,))) == cube(encode((1, 1, 1)))
    assert encode((3,)) != encode((1, 1, 1))
    # Without the single-summand avoidance hypothesis, the generic lemma fails.
    assert witness_2143((2, 1, 4, 3)) == (0, 1, 2, 3)

    result = {
        "job_id": JOB,
        "kind": "exact_finite_observation",
        "source_sha256": source_hash,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_sha256": sha256((ROOT / "evidence/bijection-proof.md").read_bytes()).hexdigest(),
        "detector_validation": {"all_permutations_n": [0, 7], "tested": detector_tests,
                                "reference": "all four-entry subsets ranked directly"},
        "held_out_composition_rows": rows,
        "held_out_compositions_total": 61440,
        "bounded_lists": {"parts_alphabet": alphabet, "list_lengths": [0, 4],
                          "tested": bounded_lists},
        "generic_direct_sum_lemma": {"block_pool": "all nonempty 2143-avoiders of sizes 1..4",
                                    "pool_size": 32, "list_lengths": [0, 3],
                                    "tested": generic_tests},
        "large_cases": {"single_block_interval": [41, 256],
                        "additional_single_block_sizes": [1000, 4096],
                        "structured_cases": "identity cube of length 300; one or two exceptional blocks with long ordinary separators",
                        "tested": len(large_cases), "max_n": max(map(sum, large_cases))},
        "boundary_examples": boundary_rows,
        "generating_function": {"coefficient_range": [0, 100],
                                "numerator_low_to_high": numerator,
                                "denominator_low_to_high": denominator,
                                "initial_values_n_0_to_16": coefficients[:17]},
        "counterexamples_found": 0,
        "limitations": "Finite attacks in the proposer context, not an all-n proof or fresh referee. Earlier size-0..12 composition enumeration is not rerun. No random or floating-point tests."
    }
    out = ROOT / "evidence/research_check.json"
    tmp = out.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result, indent=2) + "\n")
    tmp.replace(out)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
