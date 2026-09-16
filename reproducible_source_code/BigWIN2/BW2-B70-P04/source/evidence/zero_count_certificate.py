#!/usr/bin/env python3
"""Directed-rounding certificate for the frozen Fibonacci-zeta count.

This script consumes the certified necessary ordinate cover from
``phase_cover_intervals.tsv``.  It proves that every point of the eight closed
rectangles 0.73 <= Re(s) <= 0.75 is either in the frozen disk or in a box on
which Z_F is nonzero.  A separate Rouche calculation proves that the frozen
disk contains exactly one zero, counted with multiplicity.

All transcendental evaluations use python-flint/Arb balls.  Rational box
endpoints, tail bounds, and comparison constants are exact.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx, fmpq


ctx.prec = 256

N = 140
SIGMA_MIN = Fraction(73, 100)
SIGMA_MAX = Fraction(3, 4)
T_MAX = Fraction(8_596_696)

# Exact rational bounds certified below.
TAIL0_UP = Fraction(1, 10**20)
TAIL1_UP = Fraction(1, 10**18)
M1_UP = Fraction(379, 100)
M2_UP = Fraction(16)

DISK_X = Fraction(730_178_633_163, 10**12)
DISK_Y = Fraction(8_596_695_206_382, 10**6)
DISK_R = Fraction(1, 10**6)

SOURCE_SHA256 = "428ca0cb32177fac8b016408059181d851fd2e86db0559ed57263745527dd932"


def aq(x: Fraction | int) -> arb:
    """An Arb ball containing the exact rational x."""
    x = Fraction(x)
    return arb(fmpq(x.numerator, x.denominator))


def qstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fibs(nmax: int) -> list[int]:
    values = [0, 1, 1]
    while len(values) <= nmax:
        values.append(values[-1] + values[-2])
    return values


@dataclass(frozen=True)
class Box:
    sigma_lo: Fraction
    sigma_hi: Fraction
    t_lo: Fraction
    t_hi: Fraction
    interval_index: int
    depth: int

    @property
    def sigma_mid(self) -> Fraction:
        return (self.sigma_lo + self.sigma_hi) / 2

    @property
    def t_mid(self) -> Fraction:
        return (self.t_lo + self.t_hi) / 2

    @property
    def l1_radius(self) -> Fraction:
        # This is at least the Euclidean distance from the centre to any point.
        return (
            self.sigma_hi - self.sigma_lo + self.t_hi - self.t_lo
        ) / 2


def read_phase_intervals(path: Path) -> list[tuple[Fraction, Fraction]]:
    rows = path.read_text().splitlines()
    assert rows[0] == "index\tlower_closed\tupper_closed\twidth"
    answer: list[tuple[Fraction, Fraction]] = []
    for expected_index, row in enumerate(rows[1:], 1):
        index, lower, upper, width = row.split("\t")
        lo, hi = Fraction(lower), Fraction(upper)
        assert int(index) == expected_index
        assert hi - lo == Fraction(width)
        assert 0 < lo <= hi <= T_MAX
        if answer:
            assert answer[-1][1] < lo
        answer.append((lo, hi))
    assert len(answer) == 8
    return answer


def box_inside_disk(box: Box) -> tuple[bool, Fraction]:
    max_squared_distance = max(
        (x - DISK_X) ** 2 + (y - DISK_Y) ** 2
        for x in (box.sigma_lo, box.sigma_hi)
        for y in (box.t_lo, box.t_hi)
    )
    return max_squared_distance <= DISK_R**2, max_squared_distance


def split_box(box: Box) -> tuple[Box, Box]:
    args = dict(interval_index=box.interval_index, depth=box.depth + 1)
    if box.sigma_hi - box.sigma_lo >= box.t_hi - box.t_lo:
        middle = box.sigma_mid
        return (
            Box(box.sigma_lo, middle, box.t_lo, box.t_hi, **args),
            Box(middle, box.sigma_hi, box.t_lo, box.t_hi, **args),
        )
    middle = box.t_mid
    return (
        Box(box.sigma_lo, box.sigma_hi, box.t_lo, middle, **args),
        Box(box.sigma_lo, box.sigma_hi, middle, box.t_hi, **args),
    )


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    evidence_dir = root / "evidence"
    source_path = root / "source.md"
    phase_path = evidence_dir / "phase_cover_intervals.tsv"
    phase_report_path = evidence_dir / "phase_cover_report.json"
    leaf_path = evidence_dir / "zero_count_boxes.tsv"
    report_path = evidence_dir / "zero_count_report.json"

    assert file_sha256(source_path) == SOURCE_SHA256
    phase_sha256 = file_sha256(phase_path)
    phase_report = json.loads(phase_report_path.read_text())
    assert phase_report["cover_sha256"] == phase_sha256
    assert phase_report["status"] == "certified_necessary_condition_cover_not_zero_count"
    intervals = read_phase_intervals(phase_path)

    fs = fibs(N)
    logs = [arb(0)] * (N + 1)
    for n in range(1, N + 1):
        logs[n] = arb(fs[n]).log()

    sigma0 = aq(SIGMA_MIN)
    phi = (arb(1) + arb(5).sqrt()) / 2
    q = phi ** (-sigma0)
    assert 0 < q < 1

    # F_n >= phi^(n-2) and F_n <= phi^(n-1) follow by induction from
    # phi^2=phi+1.  They give the following uniform tails for Re(s)>=0.73.
    first_tail_k = N - 1
    tail0_expression = q**first_tail_k / (1 - q)
    tail1_expression = (
        phi.log()
        * q**first_tail_k
        * ((first_tail_k + 1) - first_tail_k * q)
        / (1 - q) ** 2
    )
    assert tail0_expression < aq(TAIL0_UP)
    assert tail1_expression < aq(TAIL1_UP)

    # Uniform derivative bound.  The finite portion is evaluated directly;
    # the derivative tail is the preceding geometric-series expression.
    m1_finite = sum(
        (logs[n] * arb(fs[n]) ** (-sigma0) for n in range(1, N + 1)),
        arb(0),
    )
    m1_expression = m1_finite + tail1_expression
    assert m1_expression < aq(M1_UP)

    # A coarse but convenient full bound for Z_F'' on Re(s)>=0.73:
    # sum_{k>=1}(k+1)^2 log(phi)^2 q^k.
    m2_expression = (
        phi.log() ** 2 * q * (4 - 3 * q + q**2) / (1 - q) ** 3
    )
    assert m2_expression < aq(M2_UP)

    def partial_value(sigma: Fraction, ordinate: Fraction) -> acb:
        s = acb(aq(sigma), aq(ordinate))
        return sum(
            ((-s * logs[n]).exp() for n in range(1, N + 1)), acb(0)
        )

    # On every excluded box B with centre m, the mean-value integral gives
    # |Z_F(s)-P_N(m)| <= TAIL0_UP + M1_UP*radius(B).  The strict Arb
    # comparison below therefore proves Z_F(s) != 0 throughout B.
    pending = [
        Box(SIGMA_MIN, SIGMA_MAX, lo, hi, index, 0)
        for index, (lo, hi) in enumerate(intervals, 1)
    ]
    leaves: list[dict[str, str | int]] = []
    visited = 0
    maximum_depth = 0
    per_interval = {
        str(i): {"excluded_boxes": 0, "disk_boxes": 0, "maximum_depth": 0}
        for i in range(1, 9)
    }
    while pending:
        box = pending.pop()
        visited += 1
        maximum_depth = max(maximum_depth, box.depth)
        stats = per_interval[str(box.interval_index)]
        stats["maximum_depth"] = max(stats["maximum_depth"], box.depth)

        inside, max_distance_squared = box_inside_disk(box)
        common = {
            "interval_index": box.interval_index,
            "depth": box.depth,
            "sigma_lower": qstr(box.sigma_lo),
            "sigma_upper": qstr(box.sigma_hi),
            "t_lower": qstr(box.t_lo),
            "t_upper": qstr(box.t_hi),
        }
        if inside:
            stats["disk_boxes"] += 1
            leaves.append({
                "kind": "inside_frozen_disk",
                **common,
                "abs_partial_lower": "",
                "error_upper": "",
                "gap_lower": "",
                "max_distance_squared": qstr(max_distance_squared),
            })
            continue

        value = partial_value(box.sigma_mid, box.t_mid)
        error = aq(TAIL0_UP + M1_UP * box.l1_radius)
        modulus = abs(value)
        if modulus.lower() > error:
            gap = modulus - error
            assert gap > 0
            stats["excluded_boxes"] += 1
            leaves.append({
                "kind": "certified_nonzero",
                **common,
                "abs_partial_lower": str(modulus.lower()),
                "error_upper": str(error.upper()),
                "gap_lower": str(gap.lower()),
                "max_distance_squared": qstr(max_distance_squared),
            })
            continue

        assert box.depth < 80
        left, right = split_box(box)
        # LIFO order is fixed so the emitted certificate is deterministic.
        pending.append(right)
        pending.append(left)

    # The disk is wholly in the original counting region and in phase window 8.
    assert DISK_X - DISK_R >= SIGMA_MIN
    assert DISK_Y - DISK_R > 0
    assert DISK_Y + DISK_R <= T_MAX
    assert intervals[7][0] <= DISK_Y - DISK_R
    assert DISK_Y + DISK_R <= intervals[7][1]

    # Rouche certificate on the exact frozen disk.  Put
    # L(s)=P_N(c)+P_N'(c)(s-c).  On the boundary,
    # |L| >= |P_N'(c)|r-|P_N(c)|.  The difference Z_F-L is bounded by the
    # value tail, derivative tail, and the integral Taylor remainder.
    centre = acb(aq(DISK_X), aq(DISK_Y))
    p_centre = sum(
        ((-centre * logs[n]).exp() for n in range(1, N + 1)), acb(0)
    )
    dp_centre = -sum(
        (
            logs[n] * (-centre * logs[n]).exp()
            for n in range(1, N + 1)
        ),
        acb(0),
    )
    p_abs = abs(p_centre)
    dp_abs = abs(dp_centre)
    radius = aq(DISK_R)
    linear_boundary_lower = aq(Fraction(0)) + dp_abs.lower() * radius - p_abs.upper()
    difference_upper = (
        aq(TAIL0_UP)
        + aq(TAIL1_UP) * radius
        + aq(M2_UP) * radius**2 / 2
    )
    assert p_abs.upper() < dp_abs.lower() * radius
    assert linear_boundary_lower > difference_upper
    rouche_gap = linear_boundary_lower - difference_upper
    assert rouche_gap > 0

    columns = [
        "kind",
        "interval_index",
        "depth",
        "sigma_lower",
        "sigma_upper",
        "t_lower",
        "t_upper",
        "abs_partial_lower",
        "error_upper",
        "gap_lower",
        "max_distance_squared",
    ]
    leaf_lines = ["\t".join(columns)]
    for leaf in leaves:
        leaf_lines.append("\t".join(str(leaf[column]) for column in columns))
    leaf_bytes = ("\n".join(leaf_lines) + "\n").encode()
    leaf_path.write_bytes(leaf_bytes)

    excluded_count = sum(
        stats["excluded_boxes"] for stats in per_interval.values()
    )
    disk_count = sum(stats["disk_boxes"] for stats in per_interval.values())
    assert excluded_count + disk_count == len(leaves)
    assert disk_count > 0

    report = {
        "job_id": "win-00070-p04-research-afa9b8e545d5",
        "status": "certified_exact_zero_count",
        "conclusion": {
            "N_0.73_8596696": 1,
            "frozen_closed_disk_zero_count_with_multiplicity": 1,
            "frozen_disk_unique_zero_is_simple": True,
        },
        "domain_reduction": {
            "source_theorem": "Mantovanelli Theorem 1.1: no zeros for Re(s)>=sigma_F and sigma_F<0.75",
            "phase_cover": "Every remaining zero with 0.73<=Re(s)<sigma_F and 0<t<=8596696 has t in one of the eight closed input intervals.",
            "direct_box_domain": "All eight closed products [0.73,0.75] x phase interval",
            "included_boundaries": "The products and all leaf boxes are closed; hence sigma=0.73 and every retained ordinate endpoint are included. The phase cover also covers the possible top boundary t=8596696.",
        },
        "analytic_bounds": {
            "truncation_index": N,
            "arb_precision_bits": ctx.prec,
            "tail_value_expression": tail0_expression.str(50, radius=True),
            "tail_value_upper_used": qstr(TAIL0_UP),
            "tail_derivative_expression": tail1_expression.str(50, radius=True),
            "tail_derivative_upper_used": qstr(TAIL1_UP),
            "first_derivative_bound_expression": m1_expression.str(50, radius=True),
            "first_derivative_upper_used": qstr(M1_UP),
            "second_derivative_bound_expression": m2_expression.str(50, radius=True),
            "second_derivative_upper_used": qstr(M2_UP),
        },
        "box_cover": {
            "visited_boxes": visited,
            "leaf_boxes": len(leaves),
            "certified_nonzero_leaf_boxes": excluded_count,
            "leaf_boxes_inside_frozen_disk": disk_count,
            "maximum_depth": maximum_depth,
            "per_interval": per_interval,
            "leaf_file": "evidence/zero_count_boxes.tsv",
            "leaf_file_sha256": hashlib.sha256(leaf_bytes).hexdigest(),
            "criterion": "At box centre m, |P_N(m)| > TAIL0_UP + M1_UP*((sigma width+t width)/2).",
            "coverage": "Each initial closed rectangle is recursively bisected into two closed children; every final child is either certified nonzero or contained in the frozen disk.",
        },
        "rouche_disk": {
            "centre_exact": "730178633163/1000000000000 + (8596695206382/1000000)i",
            "radius_exact": qstr(DISK_R),
            "partial_value_at_centre": p_centre.str(55, radius=True),
            "partial_derivative_at_centre": dp_centre.str(55, radius=True),
            "partial_value_modulus": p_abs.str(55, radius=True),
            "partial_derivative_modulus": dp_abs.str(55, radius=True),
            "linear_zero_distance_upper": (p_abs / dp_abs).upper().str(55),
            "linear_boundary_lower": linear_boundary_lower.str(55, radius=True),
            "difference_upper": difference_upper.str(55, radius=True),
            "rouche_gap": rouche_gap.str(55, radius=True),
            "argument": "The linear function has one zero inside the disk. On the circle its modulus lower bound exceeds the value-tail + derivative-tail*r + M2*r^2/2 bound for Z_F minus the linear function, so Rouche gives exactly one zero counted with multiplicity and none on the circle.",
        },
        "input_hashes": {
            "source.md": SOURCE_SHA256,
            "evidence/phase_cover_intervals.tsv": phase_sha256,
            "evidence/phase_cover_report.json": file_sha256(phase_report_path),
        },
        "method_notes": [
            "Arb comparisons are strict interval comparisons; an assertion succeeds only when the displayed inequality is certified.",
            "The value and derivative tails use F_n>=phi^(n-2), F_n<=phi^(n-1), and exact geometric-series sums; both Fibonacci inequalities follow by induction from phi^2=phi+1.",
            "The nonzero box criterion follows by integrating Z_F' along the line segment from the box centre and using the uniform derivative bound on Re(s)>=0.73.",
            "Exactly one zero counted with multiplicity implies existence, uniqueness as a distinct zero, and simplicity.",
        ],
    }
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
