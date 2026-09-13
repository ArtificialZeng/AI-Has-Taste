#!/usr/bin/env python3
"""Second exact replay through the independently emitted incidence instance.

Unlike check_exact_weight_certificate.py, this program does not decode graph6.
It checks that certificate rows agree with the canonical census at their stated
indices, then recomputes the weighted contradiction from the direct CSP rows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("census", type=Path)
    parser.add_argument("instance", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    certificate: dict[int, tuple[int, list[int]]] = {}
    for line in args.certificate.read_text(encoding="ascii").splitlines():
        if line.startswith("#"):
            continue
        fields = [int(part) for part in line.split()]
        index, weight, length = fields[:3]
        cycle = fields[3:]
        if index in certificate or weight <= 0 or len(cycle) != length:
            raise ValueError(f"bad certificate record at index {index}")
        certificate[index] = (weight, [length, *cycle])

    census = [[int(part) for part in line.split()] for line in args.census.read_text().splitlines()]
    instance_lines = args.instance.read_text().splitlines()
    vertices, constraints = map(int, instance_lines[0].split())
    instance = [[int(part) for part in line.split()] for line in instance_lines[1:]]
    if vertices != 812 or constraints != 7308 or len(census) != constraints or len(instance) != constraints:
        raise ValueError("unexpected direct-instance dimensions")

    scores = [[0, 0, 0] for _ in range(vertices)]
    weighted_requirement = 0
    support_by_length = {14: 0, 15: 0, 16: 0}
    for index, (weight, certified_cycle) in certificate.items():
        if index < 0 or index >= constraints or census[index] != certified_cycle:
            raise ValueError(f"certificate/census mismatch at index {index}")
        row = instance[index]
        requirement, length = row[:2]
        pairs = list(zip(row[2::2], row[3::2]))
        if length != certified_cycle[0] or requirement != 33 - 2 * length or len(pairs) != length:
            raise ValueError(f"bad direct CSP row at index {index}")
        for vertex, choice_type in pairs:
            if not (0 <= vertex < vertices and 0 <= choice_type < 3):
                raise ValueError(f"bad choice coordinate at index {index}")
            scores[vertex][choice_type] += weight
        weighted_requirement += weight * requirement
        support_by_length[length] += 1

    assignment_upper_bound = sum(max(row) for row in scores)
    gap = weighted_requirement - assignment_upper_bound
    if gap <= 0:
        raise ValueError("direct-instance replay found no contradiction")
    report = {
        "schema": "exact-cycle-weight-incidence-replay-v1",
        "status": "verified_unsat",
        "arithmetic": "exact integers",
        "certificate_sha256": digest(args.certificate),
        "census_sha256": digest(args.census),
        "instance_sha256": digest(args.instance),
        "vertices": vertices,
        "constraints": constraints,
        "certificate_support": len(certificate),
        "support_by_length": {str(k): support_by_length[k] for k in (14, 15, 16)},
        "weighted_cycle_lower_bound": weighted_requirement,
        "assignment_upper_bound": assignment_upper_bound,
        "strict_gap": gap,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
