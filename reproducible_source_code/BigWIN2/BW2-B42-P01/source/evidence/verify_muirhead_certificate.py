#!/usr/bin/env python3
"""Verify exact Muirhead certificates for the six non-coefficientwise-positive templates."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


# (template_id, positive partition lambda, negative partition mu, amount).
# Amounts are in the normalized monomial-mean basis
# M_lambda=m_lambda/|Orb(lambda)|.  Muirhead gives M_lambda>=M_mu.
TRANSFERS = (
    ("m4-L1234", (2, 1, 1, 0), (1, 1, 1, 1), 984),
    ("m4-L2345", (3, 3, 2, 0), (3, 3, 1, 1), 72),
    ("m4-L2345", (4, 3, 2, 0), (4, 3, 1, 1), 144),
    ("m4-L2345", (4, 4, 2, 0), (4, 4, 1, 1), 72),
    ("m4-L2345", (4, 4, 3, 0), (4, 4, 2, 1), 72),
    ("m4-L2345", (4, 4, 3, 1), (4, 4, 2, 2), 72),
    ("m5-L1234", (2, 1, 1, 0, 0), (1, 1, 1, 1, 0), 1440),
    ("m5-L1234", (2, 1, 1, 1, 0), (1, 1, 1, 1, 1), 1200),
    ("m5-L1235", (2, 1, 1, 1, 0), (1, 1, 1, 1, 1), 720),
    ("m5-L1345", (3, 2, 1, 1, 0), (3, 1, 1, 1, 1), 240),
    ("m5-L1345", (4, 2, 1, 1, 0), (4, 1, 1, 1, 1), 240),
    ("m5-L1345", (4, 3, 2, 2, 1), (4, 2, 2, 2, 2), 240),
    ("m5-L2345", (3, 2, 2, 1, 0), (3, 2, 1, 1, 1), 600),
    ("m5-L2345", (4, 2, 2, 1, 0), (4, 2, 1, 1, 1), 600),
    ("m5-L2345", (3, 3, 2, 1, 0), (3, 3, 1, 1, 1), 600),
    ("m5-L2345", (4, 3, 2, 1, 0), (4, 3, 1, 1, 1), 600),
    ("m5-L2345", (4, 3, 2, 2, 1), (4, 2, 2, 2, 2), 600),
    ("m5-L2345", (4, 3, 3, 2, 1), (4, 3, 2, 2, 2), 600),
)


def orbit_size(partition):
    denominator = math.prod(math.factorial(n) for n in Counter(partition).values())
    return math.factorial(len(partition)) // denominator


def majorizes(lam, mu):
    return sum(lam) == sum(mu) and all(
        sum(lam[:j]) >= sum(mu[:j]) for j in range(1, len(lam) + 1)
    )


def build_certificate():
    coefficient_path = Path(__file__).with_name("template_coefficients.json")
    audit = json.loads(coefficient_path.read_text(encoding="utf-8"))
    templates = {item["template_id"]: item for item in audit["templates"]}
    supplies = {}
    demands = {}
    all_negative_keys = set()
    for template_id, item in templates.items():
        for orbit in item["coefficient_orbits"]:
            partition = tuple(orbit["partition"])
            coefficient = int(orbit["coefficient"])
            normalized_amount = coefficient * orbit_size(partition)
            key = (template_id, partition)
            if coefficient > 0:
                supplies[key] = normalized_amount
            elif coefficient < 0:
                demands[key] = -normalized_amount
                all_negative_keys.add(key)

    used_supply = defaultdict(int)
    covered_demand = defaultdict(int)
    records = []
    for template_id, lam, mu, amount in TRANSFERS:
        assert template_id in templates
        assert majorizes(lam, mu), (template_id, lam, mu)
        source = (template_id, lam)
        target = (template_id, mu)
        assert source in supplies, source
        assert target in demands, target
        used_supply[source] += amount
        covered_demand[target] += amount
        records.append(
            {
                "template_id": template_id,
                "positive_partition": list(lam),
                "negative_partition": list(mu),
                "homogeneous_degree": sum(lam),
                "normalized_amount": str(amount),
                "majorization_partial_sums_positive": [str(sum(lam[:j])) for j in range(1, len(lam) + 1)],
                "majorization_partial_sums_negative": [str(sum(mu[:j])) for j in range(1, len(mu) + 1)],
            }
        )

    assert set(covered_demand) == all_negative_keys
    assert all(covered_demand[key] == demands[key] for key in all_negative_keys)
    assert all(used_supply[key] <= supplies[key] for key in used_supply)

    affected = sorted({template_id for template_id, _, _, _ in TRANSFERS})
    assert len(affected) == 6
    assert sum(bool(item["labelled_negative_coefficients"]) for item in templates.values()) == 6
    assert all(
        not item["labelled_negative_coefficients"] or template_id in affected
        for template_id, item in templates.items()
    )

    return {
        "schema_version": 1,
        "scope": "Universal nonnegativity certificate for all 126 reconstructed coefficient templates Psi_m(L).",
        "basis": (
            "For a partition lambda, m_lambda is the sum of distinct labelled monomials in its orbit and "
            "M_lambda=m_lambda/|Orb(lambda)|.  Each stored ordinary coefficient c contributes "
            "c*|Orb(lambda)| times M_lambda."
        ),
        "inequality": (
            "Muirhead: if lambda majorizes mu and both have the same total degree, then "
            "M_lambda(r)>=M_mu(r) for all nonnegative real r."
        ),
        "coefficientwise_nonnegative_templates": 120,
        "muirhead_certified_templates": affected,
        "negative_orbits_covered": len(all_negative_keys),
        "transfers": records,
        "supply_checks": [
            {
                "template_id": key[0],
                "positive_partition": list(key[1]),
                "available_normalized_amount": str(supplies[key]),
                "used_normalized_amount": str(used),
                "remaining_normalized_amount": str(supplies[key] - used),
            }
            for key, used in sorted(used_supply.items())
        ],
        "all_negative_demands_exactly_covered": True,
        "all_126_templates_nonnegative_on_nonnegative_roots": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    encoded = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.output}")
        print(f"sha256 {hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
