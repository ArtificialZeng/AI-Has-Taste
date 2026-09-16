#!/usr/bin/env python3
"""Exact symbolic replay for the three-job matching spectrum.

Only Python's integer/Fraction arithmetic is used.  Affine expressions are
stored as a+b*d.  The program derives fractional intervals and slots from the
instance data, proves that each tested interval contact has a constant truth
value on 0<d<1/6, enumerates all injective job-saturating matchings, and emits
an exact JSON certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys


D_LEFT = Fraction(0)
D_RIGHT = Fraction(1, 6)
JOBS = ("q", "h", "r")
MACHINES = (0, 1, 2)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True, order=True)
class Affine:
    constant: Fraction = Fraction(0)
    slope: Fraction = Fraction(0)

    def __add__(self, other: "Affine") -> "Affine":
        return Affine(self.constant + other.constant, self.slope + other.slope)

    def __sub__(self, other: "Affine") -> "Affine":
        return Affine(self.constant - other.constant, self.slope - other.slope)

    def at(self, d: Fraction) -> Fraction:
        return self.constant + self.slope * d

    def root(self) -> Fraction | None:
        if self.slope == 0:
            return None
        return -self.constant / self.slope

    def sign_on_open_domain(self) -> int | None:
        """Return -1, 0, +1 if the sign is constant; otherwise None."""
        left = self.at(D_LEFT)
        right = self.at(D_RIGHT)
        if left == right == 0:
            return 0
        if left >= 0 and right >= 0:
            return 1
        if left <= 0 and right <= 0:
            return -1
        return None

    def text(self) -> str:
        if self.slope == 0:
            return qstr(self.constant)
        slope_abs = abs(self.slope)
        slope_text = "d" if slope_abs == 1 else f"{qstr(slope_abs)}*d"
        if self.constant == 0:
            return slope_text if self.slope > 0 else f"-{slope_text}"
        op = "+" if self.slope > 0 else "-"
        return f"{qstr(self.constant)}{op}{slope_text}"


ZERO = Affine()
ONE = Affine(Fraction(1))

sizes = {
    "q": ONE,
    "h": Affine(Fraction(1, 2)),
    "r": Affine(Fraction(1, 3), Fraction(-1)),
}

shares = {
    ("q", 0): Affine(Fraction(1, 3), Fraction(1)),
    ("q", 1): Affine(Fraction(2, 3), Fraction(-1)),
    ("h", 0): Affine(Fraction(2, 3)),
    ("h", 2): Affine(Fraction(1, 3)),
    ("r", 0): ONE,
}


def positive_on_domain(value: Affine) -> bool:
    return value.sign_on_open_domain() == 1


def interval_text(interval: tuple[Affine, Affine]) -> str:
    return f"[{interval[0].text()},{interval[1].text()})"


# Derive the nonincreasing-size order at d=1/12 and certify that it stays so.
representative = Fraction(1, 12)
orders: dict[int, list[str]] = {}
order_checks: list[dict[str, str]] = []
for machine in MACHINES:
    eligible = [job for job in JOBS if (job, machine) in shares]
    eligible.sort(key=lambda job: sizes[job].at(representative), reverse=True)
    for first, second in zip(eligible, eligible[1:]):
        difference = sizes[first] - sizes[second]
        assert positive_on_domain(difference)
        order_checks.append({"machine": str(machine), "inequality": f"p_{first}-p_{second}={difference.text()}>0"})
    orders[machine] = eligible


# Build every fractional job interval by concatenating shares in the derived order.
job_intervals: dict[tuple[str, int], tuple[Affine, Affine]] = {}
totals: dict[int, Affine] = {}
for machine in MACHINES:
    cursor = ZERO
    for job in orders[machine]:
        share = shares[(job, machine)]
        assert positive_on_domain(share)
        job_intervals[(job, machine)] = (cursor, cursor + share)
        cursor = cursor + share
    totals[machine] = cursor


# Derive the number of unit slots from the representative, and certify no total
# crosses an integer in the open domain.  The last slot is truncated at M_i.
slots: dict[str, tuple[int, tuple[Affine, Affine]]] = {}
interior_breakpoints: set[Fraction] = set()
for machine in MACHINES:
    total_at_rep = totals[machine].at(representative)
    slot_count = (total_at_rep.numerator + total_at_rep.denominator - 1) // total_at_rep.denominator
    for integer in range(slot_count + 1):
        root = (totals[machine] - Affine(Fraction(integer))).root()
        if root is not None and D_LEFT < root < D_RIGHT:
            interior_breakpoints.add(root)
    assert slot_count - 1 < total_at_rep <= slot_count
    for z in range(1, slot_count + 1):
        lower = Affine(Fraction(z - 1))
        integer_upper = Affine(Fraction(z))
        upper = totals[machine] if totals[machine].at(representative) < z else integer_upper
        label = chr(ord("A") + len(slots))
        slots[label] = (machine, (lower, upper))


# Roots at which a fractional interval endpoint could cross an integer slot
# boundary are precisely the remaining possible adjacency breakpoints.
for interval in job_intervals.values():
    for endpoint in interval:
        for integer in range(4):
            root = (endpoint - Affine(Fraction(integer))).root()
            if root is not None and D_LEFT < root < D_RIGHT:
                interior_breakpoints.add(root)

assert not interior_breakpoints, interior_breakpoints


# Two half-open intervals [a,b), [c,e) overlap iff b-c>0 and e-a>0.
# Certify both affine signs on the whole domain rather than merely sampling.
neighbors: dict[str, list[str]] = {job: [] for job in JOBS}
contact_checks: list[dict[str, str | bool]] = []
for job in JOBS:
    for slot, (machine, slot_interval) in slots.items():
        if (job, machine) not in job_intervals:
            continue
        job_interval = job_intervals[(job, machine)]
        gap_one = job_interval[1] - slot_interval[0]
        gap_two = slot_interval[1] - job_interval[0]
        sign_one = gap_one.sign_on_open_domain()
        sign_two = gap_two.sign_on_open_domain()
        assert sign_one is not None and sign_two is not None
        adjacent = sign_one == 1 and sign_two == 1
        if adjacent:
            neighbors[job].append(slot)
        contact_checks.append(
            {
                "job": job,
                "slot": slot,
                "upper_job_minus_lower_slot": gap_one.text(),
                "upper_slot_minus_lower_job": gap_two.text(),
                "adjacent": adjacent,
            }
        )


# Enumerate the full Cartesian product of neighborhoods and retain exactly the
# injective choices.  This saturates all three jobs and is exhaustive by design.
matchings: list[tuple[str, str, str]] = []
for choice in product(*(neighbors[job] for job in JOBS)):
    if len(set(choice)) == len(choice):
        matchings.append(choice)


def maximum_on_domain(values: list[Affine]) -> Affine:
    # Compare every pair at the representative and prove the winning
    # inequalities have constant sign throughout the domain.
    winner = max(values, key=lambda value: value.at(representative))
    for value in values:
        difference = winner - value
        assert difference.sign_on_open_domain() in (0, 1)
    return winner


matching_records: list[dict[str, object]] = []
makespans: list[Affine] = []
for matching in matchings:
    loads = {machine: ZERO for machine in MACHINES}
    for job, slot in zip(JOBS, matching):
        machine = slots[slot][0]
        loads[machine] = loads[machine] + sizes[job]
    makespan = maximum_on_domain(list(loads.values()))
    makespans.append(makespan)
    matching_records.append(
        {
            "template_q_h_r": "(" + ",".join(matching) + ")",
            "loads_m0_m1_m2": [loads[machine].text() for machine in MACHINES],
            "makespan": makespan.text(),
        }
    )


def affine_key(value: Affine) -> tuple[Fraction, Fraction]:
    return value.constant, value.slope


multiset: dict[str, int] = {}
for value in sorted(makespans, key=affine_key, reverse=True):
    multiset[value.text()] = multiset.get(value.text(), 0) + 1


# Comparison targets are transcribed from problem.md only after all objects above
# have been derived.  A discrepancy aborts rather than emitting a certificate.
expected_matchings = [
    ("A", "B", "C"),
    ("A", "E", "B"),
    ("A", "E", "C"),
    ("D", "A", "B"),
    ("D", "A", "C"),
    ("D", "B", "C"),
    ("D", "E", "B"),
    ("D", "E", "C"),
]
expected_multiset = {"11/6-d": 1, "4/3-d": 2, "1": 5}
assert matchings == expected_matchings
assert multiset == expected_multiset


project_dir = Path(__file__).resolve().parents[1]
source_digest = sha256((project_dir / "source.md").read_bytes()).hexdigest()
assert source_digest == "66bd29461d230e70ebd25d85636d33bb9132c518790efc445618077a3ba1df4b"

certificate = {
    "arithmetic": "exact integers and fractions; affine expressions a+b*d",
    "source_sha256": source_digest,
    "parameter_domain": "0<d<1/6",
    "representative": qstr(representative),
    "interior_breakpoints": [],
    "orders": {str(machine): orders[machine] for machine in MACHINES},
    "order_checks": order_checks,
    "job_intervals": {
        f"{job}@{machine}": interval_text(interval)
        for (job, machine), interval in job_intervals.items()
    },
    "slots": {
        slot: {"machine": machine, "interval": interval_text(interval)}
        for slot, (machine, interval) in slots.items()
    },
    "contact_checks": contact_checks,
    "neighbors": neighbors,
    "enumeration_domain_size": len(neighbors["q"]) * len(neighbors["h"]) * len(neighbors["r"]),
    "valid_matching_count": len(matchings),
    "matchings": matching_records,
    "makespan_multiset": multiset,
    "minimum_makespan": "1",
    "maximum_makespan": "11/6-d",
    "comparison_with_problem_md": "all eight templates and all multiset multiplicities agree",
}

serialized = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
if len(sys.argv) == 3 and sys.argv[1] == "--write":
    output_path = Path(sys.argv[2]).resolve()
    assert output_path.parent == Path(__file__).resolve().parent
    output_path.write_text(serialized, encoding="utf-8")
elif len(sys.argv) != 1:
    raise SystemExit(f"usage: {Path(sys.argv[0]).name} [--write OUTPUT_IN_EVIDENCE_DIR]")
print(serialized, end="")
