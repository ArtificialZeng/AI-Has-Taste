#!/usr/bin/env python3
"""Exhaust the corner-normalized order-13 Cayley-host search.

No third-party package is used.  A normalized injection of the 12 grid
vertices into Z/13Z has image Z/13Z minus one nonzero residue.  A symmetric
connection set is specified by a subset of the six sign-paired differences.
Thus the 12 * 64 cases below cover every possible normalized host.
"""

from collections import Counter
import json


MODULUS = 13
ABSOLUTE_DIFFERENCES = tuple(range(1, (MODULUS + 1) // 2))
TARGET_DEGREES = tuple(sorted([2] * 4 + [3] * 6 + [4] * 2))


def absolute_difference(a: int, b: int) -> int:
    d = (b - a) % MODULUS
    return min(d, MODULUS - d)


def main() -> None:
    signature_counts = Counter()
    degree_match_count = 0
    zero_has_corner_degree_count = 0
    structural_formula_checks = 0

    for omitted in range(1, MODULUS):
        image = tuple(x for x in range(MODULUS) if x != omitted)
        assert len(image) == 12 and 0 in image

        for mask in range(1 << len(ABSOLUTE_DIFFERENCES)):
            selected = {
                d for d in ABSOLUTE_DIFFERENCES if mask & (1 << (d - 1))
            }
            degrees = []
            for x in image:
                degree = sum(
                    absolute_difference(x, y) in selected
                    for y in image
                    if y != x
                )
                degrees.append(degree)

                # The full Cayley graph has degree 2|selected|.  Deleting the
                # omitted vertex lowers a surviving degree by zero or one.
                full_degree = 2 * len(selected)
                assert degree in (full_degree - 1, full_degree)
                structural_formula_checks += 1

            signature = tuple(sorted(degrees))
            signature_counts[signature] += 1
            zero_has_corner_degree_count += degrees[image.index(0)] == 2
            degree_match_count += signature == TARGET_DEGREES

    candidate_count = (MODULUS - 1) * (1 << len(ABSOLUTE_DIFFERENCES))
    assert candidate_count == 768
    assert sum(signature_counts.values()) == candidate_count
    assert structural_formula_checks == candidate_count * 12
    assert degree_match_count == 0

    result = {
        "arithmetic": "exact integer enumeration",
        "group": "Z_13",
        "normalization": "a fixed grid corner has label 0",
        "omitted_residues_tested": MODULUS - 1,
        "symmetric_connection_sets_tested_per_omission": 1
        << len(ABSOLUTE_DIFFERENCES),
        "normalized_host_candidates_tested": candidate_count,
        "target_degree_multiset": list(TARGET_DEGREES),
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_with_zero_of_degree_two": zero_has_corner_degree_count,
        "structural_degree_checks": structural_formula_checks,
        "conclusion": "no induced Abelian Cayley embedding in Z_13",
        "degree_signature_histogram": {
            ",".join(map(str, signature)): count
            for signature, count in sorted(signature_counts.items())
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
