#!/usr/bin/env python3
"""Certified Proposition 7.1 ordinate cover for win-00070-p04.

The script uses exact integer endpoint arithmetic for periodic phase windows
and python-flint/Arb balls for all transcendental bounds and for the final
joint-energy exclusions.  It writes a JSON audit report and the surviving
closed ordinate intervals.  The output is a necessary-condition cover only;
it is not a zero count.
"""

from __future__ import annotations

from array import array
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx, fmpq


ctx.prec = 192

T = 8_596_696
GRID = 10**9                    # endpoints are integer nanounits
T_TICK = T * GRID
CONST_DIGITS = 24
CONST_SCALE = 10**CONST_DIGITS
JOINT_MAX_TICKS = 5_000_000     # 0.005-wide terminal boxes
JOINT_N = 30
ALPHA_PARTS = 24                # interval subdivision for the omega arc

# Decimal lower/upper enclosures have common denominator 10^24.  Each upper
# logarithm (and pi) is exactly one unit above the displayed lower endpoint.
PI_LO = int("3" + "141592653589793238462643")
PI_HI = PI_LO + 1
LOG_DATA = {
    2: (0, "693147180559945309417232"),
    3: (1, "098612288668109691395245"),
    5: (1, "609437912434100374600759"),
    13: (2, "564949357461536736053487"),
    21: (3, "044522437723422996500597"),
    34: (3, "526360524616161389666766"),
    55: (4, "007333185232470918662702"),
    89: (4, "488636369732139838317815"),
}

# Certified angular-radius upper bounds, also scaled by 10^24.  The first two
# come from (17); the rest come from (20), in Fibonacci-index order.
DELTA_HI = {
    2: int("512174793486796593149426"),
    3: int("598687998441899467344934"),
    5: int("932674913662750792270648"),
    13: int("1209611441366676873107514"),
    21: int("1405838206058152966984497"),
    34: int("1666472314236621336794858"),
    55: int("2039987021672562880879150"),
    89: int("2810571796660721292073878"),
}

# Simple rational outward bounds used uniformly on 0.73 <= sigma < sigma_F.
H_UP = fmpq(45_602_822, 10**9)
K_UP = fmpq(402_314_890, 10**9)
A_LO = fmpq(594_603_557, 10**9)  # lower bound for 2^(-sigma)
B_LO = fmpq(438_691_337, 10**9)  # lower bound for 3^(-sigma)
R_LO = fmpq(75_746_608, 10**8)   # lower bound for R(sigma)
ETA_HI = fmpq(348_764_756, 10**9)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def decimal_scaled(q: fmpq, digits: int = CONST_DIGITS) -> int:
    """Return q*10^digits when it is an integer, failing otherwise."""
    x = q * 10**digits
    z = x.numerator // x.denominator
    assert fmpq(z) == x
    return int(z)


def log_bounds(base: int) -> tuple[int, int]:
    integer_part, fractional = LOG_DATA[base]
    lo = integer_part * CONST_SCALE + int(fractional)
    return lo, lo + 1


def fibs(nmax: int) -> list[int]:
    f = [0, 1, 1]
    while len(f) <= nmax:
        f.append(f[-1] + f[-2])
    return f


def certify_constants() -> dict[str, str]:
    """Prove every rounded constant used below encloses its target."""
    sigma0 = arb(fmpq(73, 100))
    sigma75 = arb(fmpq(3, 4))
    fs = fibs(100)
    phi = (arb(1) + arb(5).sqrt()) / 2

    n_tail = 90
    z_partial = sum(
        (arb(fs[n]) ** (-sigma0) for n in range(1, n_tail + 1)), arb(0)
    )
    tail_up = phi ** (-(n_tail - 1) * sigma0) / (1 - phi ** (-sigma0))
    h_partial = z_partial - 4 - 2 * arb(144) ** (-sigma0)
    h_enclosure_up = h_partial + tail_up
    assert h_enclosure_up < arb(H_UP)

    k0 = (
        arb(72) ** (-sigma0)
        + arb(18) ** (-sigma0)
        + 4 * arb(48) ** (-sigma0)
    )
    assert k0 < arb(K_UP)
    assert arb(2) ** (-sigma75) > arb(A_LO)
    assert arb(3) ** (-sigma75) > arb(B_LO)

    r75_partial = sum(
        (
            arb(fs[n]) ** (-sigma75)
            for n in range(5, n_tail + 1)
            if n not in (6, 12)
        ),
        arb(0),
    )
    assert r75_partial > arb(R_LO)

    pi = arb.pi()
    assert arb(fmpq(PI_LO, CONST_SCALE)) < pi
    assert pi < arb(fmpq(PI_HI, CONST_SCALE))
    for base in LOG_DATA:
        lo, hi = log_bounds(base)
        target = arb(base).log()
        assert arb(fmpq(lo, CONST_SCALE)) < target
        assert target < arb(fmpq(hi, CONST_SCALE))

    phase_rhs = 2 * arb(H_UP) / (1 - arb(K_UP))
    calculated_deltas: dict[int, arb] = {}
    for base, lower_weight in ((2, A_LO), (3, B_LO)):
        chord = (phase_rhs / arb(lower_weight)).sqrt()
        calculated_deltas[base] = 2 * (chord / 2).asin()

    omega_chord = (2 * arb(H_UP) / arb(R_LO)).sqrt()
    eta = 2 * (omega_chord / 2).asin()
    assert eta < arb(ETA_HI)
    phase_index = {5: 5, 13: 7, 21: 8, 34: 9, 55: 10, 89: 11}
    for base, n in phase_index.items():
        chord = (
            (2 * arb(H_UP) * arb(fs[n]) ** sigma75).sqrt() + omega_chord
        )
        assert chord < 2
        calculated_deltas[base] = 2 * (chord / 2).asin()

    # F_13=233 is already vacuous in (20), and the bound increases with F_n.
    first_vacuous = (
        (2 * arb(H_UP) * arb(fs[13]) ** sigma75).sqrt() + omega_chord
    )
    assert first_vacuous > 2

    for base, delta in calculated_deltas.items():
        assert delta < arb(fmpq(DELTA_HI[base], CONST_SCALE))

    return {
        "H_0.73_upper_expression": h_enclosure_up.str(45, radius=True),
        "H_upper_used": str(H_UP),
        "K_0.73": k0.str(45, radius=True),
        "K_upper_used": str(K_UP),
        "R_0.75_partial_through_F90": r75_partial.str(45, radius=True),
        "R_lower_used": str(R_LO),
        "omega_arc_halfwidth_calculated": eta.str(45, radius=True),
        "omega_arc_halfwidth_upper_used": str(ETA_HI),
        "first_vacuous_20_chord_bound_F233": first_vacuous.str(45, radius=True),
        "arb_precision_bits": str(ctx.prec),
    }


def phase_intervals(base: int):
    """Yield a closed grid cover of the odd-pi phase windows for one base."""
    log_lo, log_hi = log_bounds(base)
    delta_hi = DELTA_HI[base]
    odd = 1
    while True:
        # Exact rational outward rounding.  Scaling by 10^24 cancels.
        lo = ((odd * PI_LO - delta_hi) * GRID) // log_hi
        if lo > T_TICK:
            return
        hi = ceil_div((odd * PI_HI + delta_hi) * GRID, log_lo)
        yield max(0, lo), min(T_TICK, hi)
        odd += 2


def intersect_sorted(left, right) -> tuple[array, array]:
    """Intersect two sorted, internally disjoint closed interval streams."""
    out_lo = array("q")
    out_hi = array("q")
    a_iter, b_iter = iter(left), iter(right)
    try:
        a, b = next(a_iter), next(b_iter)
    except StopIteration:
        return out_lo, out_hi
    while True:
        lo, hi = max(a[0], b[0]), min(a[1], b[1])
        if lo <= hi:
            out_lo.append(lo)
            out_hi.append(hi)
        if a[1] < b[1]:
            try:
                a = next(a_iter)
            except StopIteration:
                break
        else:
            try:
                b = next(b_iter)
            except StopIteration:
                break
    assert all(out_hi[i] < out_lo[i + 1] for i in range(len(out_lo) - 1))
    return out_lo, out_hi


def width_ticks(lo: array | list[int], hi: array | list[int]) -> int:
    return sum(b - a for a, b in zip(lo, hi))


def t_ball(lo_tick: int, hi_tick: int) -> arb:
    # Arb's radius is rounded outward, so this encloses the exact grid box.
    return arb(
        f"{lo_tick + hi_tick}/{2 * GRID}",
        f"{hi_tick - lo_tick}/{2 * GRID}",
    )


def joint_cover(lo: array, hi: array) -> tuple[list[int], list[int], dict[str, int]]:
    """Prune with finite consequences of (18), then (18)+(19)."""
    fs = fibs(JOINT_N)
    sigma75 = arb(fmpq(3, 4))
    terms: list[tuple[arb, arb]] = []
    weight_sum = arb(0)
    for n in range(5, JOINT_N + 1):
        if n in (6, 12):
            continue
        weight = arb(fs[n]) ** (-sigma75)
        terms.append((weight, arb(fs[n]).log()))
        weight_sum += weight

    h_up = arb(H_UP)
    eta_up = arb(ETA_HI)
    # Fixed alpha boxes cover [-eta_up,eta_up].
    alpha_boxes = []
    eta_num, eta_den = int(ETA_HI.numerator), int(ETA_HI.denominator)
    for j in range(ALPHA_PARTS):
        # endpoints eta*(-1+2j/P) and eta*(-1+2(j+1)/P)
        a_num = eta_num * (-ALPHA_PARTS + 2 * j)
        b_num = eta_num * (-ALPHA_PARTS + 2 * (j + 1))
        den = eta_den * ALPHA_PARTS
        alpha_boxes.append(
            arb(f"{a_num + b_num}/{2 * den}", f"{b_num - a_num}/{2 * den}")
        )

    tests = 0
    excluded_by_unrestricted = 0
    excluded_by_arc = 0

    def exclusion_reason(a: int, b: int) -> int:
        """Return 1 or 2 for certified exclusion, or 0 if inconclusive."""
        nonlocal tests
        tests += 1
        tb = t_ball(a, b)
        re_s, im_s = arb(0), arb(0)
        for weight, log_f in terms:
            sine, cosine = (tb * log_f).sin_cos()
            re_s += weight * cosine
            im_s -= weight * sine
        modulus = abs(acb(re_s, im_s))
        # From (18), minimizing over all unit omega gives W-|S(t)| <= H_UP.
        if weight_sum - modulus > h_up:
            return 1

        # From (19), omega=-exp(i alpha), |alpha|<=ETA_HI.  The maximum
        # possible Re(conj(omega)S) is enclosed by subdividing that alpha arc.
        max_projection_upper = None
        for alpha in alpha_boxes:
            sine, cosine = alpha.sin_cos()
            projection = -cosine * re_s - sine * im_s
            upper = projection.upper()
            if max_projection_upper is None or upper > max_projection_upper:
                max_projection_upper = upper
        assert max_projection_upper is not None
        if weight_sum - max_projection_upper > h_up:
            return 2
        return 0

    kept_lo: list[int] = []
    kept_hi: list[int] = []
    for initial_lo, initial_hi in zip(lo, hi):
        stack = [(initial_lo, initial_hi)]
        while stack:
            a, b = stack.pop()
            reason = exclusion_reason(a, b)
            if reason == 1:
                excluded_by_unrestricted += 1
                continue
            if reason == 2:
                excluded_by_arc += 1
                continue
            if b - a <= JOINT_MAX_TICKS:
                if kept_hi and a <= kept_hi[-1]:
                    if b > kept_hi[-1]:
                        kept_hi[-1] = b
                else:
                    kept_lo.append(a)
                    kept_hi.append(b)
                continue
            middle = (a + b) // 2
            # Push right first so the left child is processed first.
            stack.append((middle, b))
            stack.append((a, middle))

    assert all(kept_hi[i] < kept_lo[i + 1] for i in range(len(kept_lo) - 1))
    return kept_lo, kept_hi, {
        "arb_interval_tests": tests,
        "boxes_excluded_by_18_alone": excluded_by_unrestricted,
        "additional_boxes_excluded_using_19": excluded_by_arc,
        "terminal_box_max_ticks": JOINT_MAX_TICKS,
        "joint_free_indices_through": JOINT_N,
        "omega_arc_subintervals": ALPHA_PARTS,
    }


def exact_decimal(ticks: int) -> str:
    return f"{ticks // GRID}.{ticks % GRID:09d}"


def main() -> None:
    constants = certify_constants()
    stages = []

    lo, hi = intersect_sorted(phase_intervals(2), phase_intervals(3))
    stages.append({
        "constraints": "(17): bases 2 and 3",
        "interval_count": len(lo),
        "total_width_ticks": width_ticks(lo, hi),
    })
    for base in (5, 13, 21, 34, 55, 89):
        lo, hi = intersect_sorted(zip(lo, hi), phase_intervals(base))
        stages.append({
            "constraints": f"previous plus (20): base {base}",
            "interval_count": len(lo),
            "total_width_ticks": width_ticks(lo, hi),
        })

    kept_lo, kept_hi, joint_stats = joint_cover(lo, hi)
    stages.append({
        "constraints": "previous plus joint finite (18)-(19), free indices 5..30",
        "interval_count": len(kept_lo),
        "total_width_ticks": width_ticks(kept_lo, kept_hi),
    })

    evidence_dir = Path(__file__).resolve().parent
    cover_path = evidence_dir / "phase_cover_intervals.tsv"
    lines = ["index\tlower_closed\tupper_closed\twidth"]
    for i, (a, b) in enumerate(zip(kept_lo, kept_hi), 1):
        lines.append(
            f"{i}\t{exact_decimal(a)}\t{exact_decimal(b)}\t{exact_decimal(b-a)}"
        )
    cover_bytes = ("\n".join(lines) + "\n").encode()
    cover_path.write_bytes(cover_bytes)

    for stage in stages:
        stage["total_width"] = exact_decimal(stage["total_width_ticks"])

    report = {
        "job_id": "win-00070-p04-research-3248e212eada",
        "status": "certified_necessary_condition_cover_not_zero_count",
        "ordinate_domain": "0 < t <= 8596696",
        "sigma_domain": "0.73 <= sigma < sigma_F < 0.75",
        "grid": "1e-9; every periodic and terminal endpoint rounded outward",
        "proposition_source": "https://arxiv.org/html/2609.04993v1#S7.Thmtheorem1",
        "derivation": [
            "Lemma 2.1 makes H decreasing; K is decreasing; Theorem 1.1 gives sigma_F<0.75.",
            "Equation (17) gives odd-pi windows for bases 2 and 3 using lower phase weights.",
            "Equations (19)-(20) give every nonvacuous individual free-phase window: F=5,13,21,34,55,89; the bound is vacuous from F_13=233 onward.",
            "For w_n=F_n^(-3/4), (18) implies for n=5..30 (excluding 6,12) that W-|sum w_n F_n^(-it)| <= H_UP.",
            "Equation (19) additionally confines omega to omega=-exp(i alpha), |alpha|<=ETA_HI; Arb interval maxima over 24 alpha subarcs certify further exclusions.",
            "Surviving terminal boxes are retained whole, so the TSV is a superset of all possible zero ordinates in the stated sigma strip.",
        ],
        "constants": constants,
        "stages": stages,
        "joint_pruning": joint_stats,
        "cover_file": "evidence/phase_cover_intervals.tsv",
        "cover_sha256": hashlib.sha256(cover_bytes).hexdigest(),
        "limitations": [
            "The cover is only a necessary-condition cover and proves neither existence nor absence of a zero in any surviving interval.",
            "It does not certify the requested zero count, disk uniqueness, or simplicity.",
            "All zero isolation, tail control on complex boxes, and included-boundary handling remain to be done.",
        ],
    }
    report_path = evidence_dir / "phase_cover_report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
