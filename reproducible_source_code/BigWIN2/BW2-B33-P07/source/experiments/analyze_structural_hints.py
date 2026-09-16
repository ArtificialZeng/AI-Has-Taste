#!/usr/bin/env python3
"""Exact owner-side tests of the unreviewed block-3 structural handoff.

The computations here are finite falsification tests.  The accompanying
Markdown proof, not this program, establishes the universal identities.
"""

import argparse
import json
import platform


KNOWN_ZEROS = [0, 6, 11, 23, 36, 42, 48, 54]


def recurrence(limit):
    values = [0, 1]
    for n in range(2, limit + 1):
        values.append((values[-1] ^ n) - values[-2])
    return values


def residues_mod(modulus, stop):
    values = [0, 1 % modulus]
    for n in range(2, stop):
        values.append(((values[-1] ^ n) - values[-2]) % modulus)
    return values


def epsilon_signature(k):
    modulus = 1 << k
    period = 3 * modulus
    values = residues_mod(2 * modulus, period + 3)
    return [((values[period + c] - values[c]) // modulus) % 2 for c in range(3)]


def check_child_table(k):
    modulus = 1 << k
    period = 3 * modulus
    values = residues_mod(2 * modulus, 2 * period)
    signature = [((values[period + c] - values[c]) // modulus) % 2 for c in range(3)]
    pattern_counts = {f"h{h}e{e}": 0 for h in range(2) for e in range(2)}
    outcome_counts = {"dead": 0, "lower-only": 0, "upper-only": 0, "both": 0}
    parents = []
    children = []
    for r in range(period):
        if values[r] % modulus:
            continue
        parents.append(r)
        h = (values[r] // modulus) % 2
        e = signature[r % 3]
        lower = values[r] == 0
        upper = values[r + period] == 0
        assert lower == (h == 0)
        assert upper == (h == e)
        pattern_counts[f"h{h}e{e}"] += 1
        outcome = ("both" if lower and upper else "lower-only" if lower else
                   "upper-only" if upper else "dead")
        outcome_counts[outcome] += 1
        if lower:
            children.append(r)
        if upper:
            children.append(r + period)
    direct_children = [n for n in range(2 * period) if values[n] == 0]
    children.sort()
    assert children == direct_children
    return {
        "k": k,
        "epsilon_signature": signature,
        "parent_count": len(parents),
        "child_count": len(children),
        "pattern_counts": pattern_counts,
        "outcome_counts": outcome_counts,
        "parents": parents if k == 2 else None,
        "children": children if k == 2 else None,
    }


def xor_low_mask_tests(max_mask_bits):
    cases = 0
    for j in range(max_mask_bits + 1):
        power = 1 << j
        mask = power - 1
        for q in range(-8, 9):
            for r in range(power):
                x = power * q + r
                assert (x ^ mask) == power * q + mask - r
                assert (x ^ mask) - x == mask - 2 * r
                cases += 1
    return cases


def twelve_step_map(state):
    x, y = state
    for j in range(12):
        x, y = y, ((y ^ j) - x) % 8
    return [x, y]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct-limit", type=int, default=1_000_000)
    parser.add_argument("--max-signature-k", type=int, default=22)
    parser.add_argument("--max-child-k", type=int, default=18)
    parser.add_argument("--max-mask-bits", type=int, default=12)
    parser.add_argument("--output")
    args = parser.parse_args()
    assert args.direct_limit >= 49_151
    assert args.max_signature_k >= 2 and args.max_child_k >= 2

    values = recurrence(args.direct_limit)
    zeros = [n for n, value in enumerate(values) if value == 0]
    assert zeros == KNOWN_ZEROS

    backward_cases = 0
    for n in range(3, args.direct_limit + 1):
        mask = (n - 1) ^ n
        rhs = (values[n - 1] ^ mask) - values[n - 1]
        assert (values[n] == 0) == (values[n - 3] == rhs)
        backward_cases += 1
    forward_cases = 0
    for n in range(args.direct_limit - 2):
        mask = (n + 2) ^ (n + 3)
        rhs = (values[n + 1] ^ mask) - values[n + 1]
        assert (values[n] == 0) == (values[n + 3] == rhs)
        forward_cases += 1

    parity = [0, 1, 1, 1, 0, 0]
    bit_strip_cases = 0
    for n in range(2, args.direct_limit + 1):
        h_n = (values[n] - parity[n % 6]) // 2
        h_prev = (values[n - 1] - parity[(n - 1) % 6]) // 2
        h_prevprev = (values[n - 2] - parity[(n - 2) % 6]) // 2
        rhs = (h_prev ^ (n // 2)) - h_prevprev - int(n % 6 == 3)
        assert h_n == rhs
        bit_strip_cases += 1
    pair_map_cases = 0
    for m in range(1, args.direct_limit // 2):
        x = (values[2 * m - 2] - parity[(2 * m - 2) % 6]) // 2
        y = (values[2 * m - 1] - parity[(2 * m - 1) % 6]) // 2
        z = (y ^ m) - x
        w = (z ^ m) - y - int(m % 3 == 1)
        actual_z = (values[2 * m] - parity[(2 * m) % 6]) // 2
        actual_w = (values[2 * m + 1] - parity[(2 * m + 1) % 6]) // 2
        assert (z, w) == (actual_z, actual_w)
        pair_map_cases += 1

    signatures = []
    for k in range(args.max_signature_k + 1):
        sig = epsilon_signature(k)
        assert sig in ([0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1])
        for c in range(3):
            assert sig[(c + 2) % 3] == (sig[(c + 1) % 3] + sig[c] + 1) % 2
        signatures.append({"k": k, "signature": sig})
    child_tables = [check_child_table(k) for k in range(args.max_child_k + 1)]
    assert child_tables[2]["epsilon_signature"] == [0, 1, 0]
    assert child_tables[2]["parents"] == [0, 4, 6, 10, 11]
    assert child_tables[2]["children"] == [0, 4, 6, 11, 12, 18, 22, 23]

    minus_one_class_3 = [
        (n - 3) // 6 for n in range(3, args.direct_limit + 1, 6) if values[n] == -1
    ]
    plus_one_class_1 = [
        (n - 1) // 6 for n in range(1, args.direct_limit + 1, 6) if values[n] == 1
    ]
    plus_one_class_2 = [
        (n - 2) // 6 for n in range(2, args.direct_limit + 1, 6) if values[n] == 1
    ]
    assert minus_one_class_3 == [0, 1, 6, 7, 8, 9]
    assert plus_one_class_1 == [0]
    assert plus_one_class_2 == [1, 3]

    record = {
        "schema_version": 1,
        "purpose": "independent exact falsification of handoff parts A-C",
        "handoff_status": "unreviewed external material; only rederived claims are adopted",
        "semantics": "Python arbitrary-precision infinite-width signed XOR",
        "parameters": vars(args) | {"output": None},
        "dyadic_shift": {
            "signatures": signatures,
            "child_tables": child_tables,
            "k2_expected_sets_reproduced": True,
            "twelve_step_mod8_maps": {
                "[0,0]": twelve_step_map((0, 0)),
                "[1,0]": twelve_step_map((1, 0)),
            },
            "long_lower_run_values": {
                "a_49139": values[49_139],
                "a_49151": values[49_151],
                "expected_power": 1 << 25,
            },
        },
        "three_step_reduction": {
            "low_mask_identity_cases": xor_low_mask_tests(args.max_mask_bits),
            "backward_equivalence_cases": backward_cases,
            "forward_equivalence_cases": forward_cases,
            "zeros_through_limit": zeros,
            "unit_hits_through_limit": {
                "a_6q_plus_3_equals_minus_1": minus_one_class_3,
                "a_6q_plus_1_equals_1": plus_one_class_1,
                "a_6q_plus_2_equals_1": plus_one_class_2,
            },
        },
        "bit_stripping": {
            "scalar_identity_cases": bit_strip_cases,
            "pair_map_cases": pair_map_cases,
        },
        "limitations": [
            "Finite unit-hit lists do not prove the three universal classifications.",
            "Finite signature and child-table tests do not classify infinite lift paths.",
            "The twelve-step example refutes only a quotient retaining the two state high bits and discarding the lower residue.",
        ],
        "python": platform.python_version(),
    }
    assert record["dyadic_shift"]["twelve_step_mod8_maps"] == {
        "[0,0]": [4, 0], "[1,0]": [5, 4]
    }
    assert values[49_139] == values[49_151] == 1 << 25
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
