#!/usr/bin/env python3
"""Exact sparse coefficient audit for the 126 reconstructed TP4 templates.

For each m <= 6 this script computes every grouped polynomial Psi_m(L) in
Z[r_0,...,r_{m-1}].  It uses inclusion--exclusion for the condition that the
selected subsets have union [m], determinant multilinearity, and sparse exact
integer polynomial arithmetic.  No symbolic CAS or floating-point arithmetic
is used.

The output records coefficients by symmetric-monomial orbit.  If
lambda=(lambda_0 >= ... >= lambda_{m-1}) and Orb(lambda) is its set of distinct
coordinate permutations, then ``coefficient`` is the common coefficient of
each labelled monomial in Orb(lambda), not the orbit sum.  The script verifies
the required divisibility of the independently accumulated orbit sum and also
cross-checks each polynomial by exact evaluation against reconstruct_126.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path

import reconstruct_126 as reconstruction


BASE = 5  # every local row is multiaffine, and there are four rows
ALL_COLUMNS = tuple(range(7))
LOCAL_COLUMNS = tuple(combinations(ALL_COLUMNS, 4))


def poly_add_into(target, source, scale=1):
    for monomial, coefficient in source.items():
        value = target.get(monomial, 0) + scale * coefficient
        if value:
            target[monomial] = value
        elif monomial in target:
            del target[monomial]


def poly_mul(left, right):
    if not left or not right:
        return {}
    # Base-5 integer addition is exponent-vector addition here.  Each factor
    # supplied by a row is squarefree, and at most four rows are multiplied,
    # so no base-5 digit can carry.
    if len(left) > len(right):
        left, right = right, left
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            key = a + b
            out[key] = out.get(key, 0) + ca * cb
    return {key: value for key, value in out.items() if value}


def subsets_of(mask):
    sub = mask
    while True:
        yield sub
        if not sub:
            break
        sub = (sub - 1) & mask


def mask_codes(m):
    powers = tuple(BASE**i for i in range(m))
    return tuple(
        sum(powers[i] for i in range(m) if mask & (1 << i))
        for mask in range(1 << m)
    )


def base_row(m, codes):
    """Coefficient polynomials of g_[m]=prod_i(1+r_i x)."""
    row = [{} for _ in ALL_COLUMNS]
    for mask in range(1 << m):
        row[mask.bit_count()][codes[mask]] = 1
    return row


def selected_row(m, vmask, cap, weights, shift, codes):
    """Coefficients of sum_{S subset V, |S|<=cap} w_|S| c_S x^shift g_[m]\S."""
    row = [{} for _ in ALL_COLUMNS]
    universe = (1 << m) - 1
    for selected in subsets_of(vmask):
        size = selected.bit_count()
        if size > cap:
            continue
        weight = weights[size]
        complement = universe ^ selected
        # c_S=prod_{i in S}(1+r_i); choose a monomial T subset S.
        for factor_monomial in subsets_of(selected):
            # [x^q]g_[m]\S is the sum over q-subsets Q of the complement.
            for elementary_monomial in subsets_of(complement):
                degree = shift + elementary_monomial.bit_count()
                if degree not in ALL_COLUMNS:
                    continue
                key = codes[factor_monomial | elementary_monomial]
                row[degree][key] = row[degree].get(key, 0) + weight
    return row


def wedge_determinants(rows):
    """Return det(rows[:,L]) for all four-subsets L, as sparse polynomials."""
    states = {(): {0: 1}}
    for row in rows:
        following = {}
        for selected_columns, old_polynomial in states.items():
            occupied = set(selected_columns)
            for column, entry in enumerate(row):
                if column in occupied or not entry:
                    continue
                inversions = sum(old_column > column for old_column in selected_columns)
                sign = -1 if inversions & 1 else 1
                new_columns = tuple(sorted(selected_columns + (column,)))
                product = poly_mul(old_polynomial, entry)
                poly_add_into(following.setdefault(new_columns, {}), product, sign)
        states = {columns: polynomial for columns, polynomial in following.items() if polynomial}
    return states


TERM_SPECS = (
    ((1, reconstruction.W1, 1), (0, (1,), 1), (2, reconstruction.H2, 2)),
    ((1, reconstruction.W1, 1), (0, (1,), 1), (3, reconstruction.W3, 3)),
    ((1, reconstruction.W1, 1), (2, reconstruction.W2, 2), (2, reconstruction.H2, 2)),
    ((1, reconstruction.W1, 1), (2, reconstruction.W2, 2), (3, reconstruction.W3, 3)),
)


def decode(code, m):
    exponents = []
    for _ in range(m):
        exponents.append(code % BASE)
        code //= BASE
    assert code == 0
    return tuple(exponents)


def orbit_size(partition):
    denominator = 1
    for multiplicity in Counter(partition).values():
        denominator *= math.factorial(multiplicity)
    return math.factorial(len(partition)) // denominator


def template_orbit_sums(m):
    """Accumulate each Psi_m(L), collapsing labelled monomials only after a determinant."""
    codes = mask_codes(m)
    row0 = base_row(m, codes)
    totals = {columns: {} for columns in LOCAL_COLUMNS}
    universe = (1 << m) - 1

    # The union-exact sum is sum_{V subset U}(-1)^(|U|-|V|) times the
    # unrestricted multilinear determinant whose selected sets all lie in V.
    for term in TERM_SPECS:
        for vmask in range(1 << m):
            ie_sign = -1 if (m - vmask.bit_count()) & 1 else 1
            rows = [row0]
            rows.extend(
                selected_row(m, vmask, cap, weights, shift, codes)
                for cap, weights, shift in term
            )
            determinants = wedge_determinants(rows)
            for columns, polynomial in determinants.items():
                collapsed = totals[columns]
                for monomial, coefficient in polynomial.items():
                    partition = tuple(sorted(decode(monomial, m), reverse=True))
                    collapsed[partition] = collapsed.get(partition, 0) + ie_sign * coefficient

    return {
        columns: {partition: value for partition, value in polynomial.items() if value}
        for columns, polynomial in totals.items()
    }


def evaluate_orbits(orbits, roots):
    """Evaluate a symmetric polynomial from common per-labelled-monomial coefficients."""
    from itertools import permutations

    total = 0
    for partition, coefficient in orbits.items():
        for exponents in set(permutations(partition)):
            monomial = 1
            for root, exponent in zip(roots, exponents):
                monomial *= root**exponent
            total += coefficient * monomial
    return total


def audit_m(m, manifest_templates):
    orbit_sums = template_orbit_sums(m)
    template_keys = {(item["m"], tuple(item["L"])) for item in manifest_templates}
    records = []
    survivor_count = 0
    negative_orbits = []
    witness_roots = reconstruction.WITNESS_ROOTS[:m]

    for columns in LOCAL_COLUMNS:
        per_monomial = {}
        for partition, summed_coefficient in sorted(orbit_sums[columns].items(), reverse=True):
            size = orbit_size(partition)
            assert summed_coefficient % size == 0, (m, columns, partition, summed_coefficient, size)
            coefficient = summed_coefficient // size
            if coefficient:
                per_monomial[partition] = coefficient

        expected_value = reconstruction.aggregate_template(m, columns, witness_roots)
        actual_value = evaluate_orbits(per_monomial, witness_roots)
        assert actual_value == expected_value, (m, columns, actual_value, expected_value)

        retained = (m, columns) in template_keys
        assert retained == bool(per_monomial), (m, columns, retained, bool(per_monomial))
        if not retained:
            continue
        survivor_count += 1

        positives = {p: c for p, c in per_monomial.items() if c > 0}
        negatives = {p: c for p, c in per_monomial.items() if c < 0}
        labelled_positive = sum(orbit_size(p) for p in positives)
        labelled_negative = sum(orbit_size(p) for p in negatives)
        labelled_total = BASE**m
        record = {
            "template_id": f"m{m}-L{''.join(map(str, columns))}",
            "m": m,
            "L": list(columns),
            "degree_bound_per_variable": 4,
            "labelled_monomials_total": labelled_total,
            "labelled_positive_coefficients": labelled_positive,
            "labelled_zero_coefficients": labelled_total - labelled_positive - labelled_negative,
            "labelled_negative_coefficients": labelled_negative,
            "nonzero_symmetric_orbits": len(per_monomial),
            "minimum_nonzero_coefficient": str(min(per_monomial.values())),
            "maximum_coefficient": str(max(per_monomial.values())),
            "coefficient_orbits": [
                {"partition": list(partition), "coefficient": str(coefficient)}
                for partition, coefficient in sorted(per_monomial.items(), reverse=True)
            ],
            "crosscheck_roots": list(witness_roots),
            "crosscheck_value": str(actual_value),
        }
        records.append(record)
        for partition, coefficient in negatives.items():
            negative_orbits.append(
                {"template_id": record["template_id"], "partition": list(partition), "coefficient": str(coefficient)}
            )

    return records, survivor_count, negative_orbits


def build_audit():
    manifest_path = Path(__file__).with_name("template_manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    templates = manifest["templates"]
    records = []
    counts = []
    negative_orbits = []
    for m in range(7):
        m_records, count, m_negatives = audit_m(m, templates)
        records.extend(m_records)
        counts.append(count)
        negative_orbits.extend(m_negatives)

    assert counts == manifest["survivor_counts_by_m"]
    assert len(records) == manifest["total_survivors"] == 126
    return {
        "schema_version": 1,
        "scope": "All ordinary monomial coefficients of every one of the 126 reconstructed Psi_m(L), m<=6.",
        "method": (
            "Exact integer sparse polynomials; inclusion-exclusion enforces union U; determinant multilinearity "
            "separates subset sums; labelled monomials are collapsed into permutation orbits only after each "
            "determinant, then divided by the exact orbit size."
        ),
        "coefficient_domain": "Z[r_0,...,r_{m-1}], with exponent 0<=e_i<=4",
        "interpretation": (
            "Each coefficient_orbits entry gives the common ordinary monomial coefficient for every distinct "
            "permutation of its exponent partition; omitted exponent partitions have coefficient zero."
        ),
        "independent_crosscheck": (
            "Every reconstructed polynomial is evaluated at the fixed positive integer witness and compared "
            "exactly with aggregate_template from reconstruct_126.py."
        ),
        "survivor_counts_by_m": counts,
        "templates_audited": len(records),
        "negative_coefficient_orbits": negative_orbits,
        "all_coefficients_nonnegative": not negative_orbits,
        "templates": records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    audit = build_audit()
    encoded = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.output}")
        print(f"sha256 {hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
