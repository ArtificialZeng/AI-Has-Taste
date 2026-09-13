"""Exact finite cross-check of the proved all-parameter formula.

The infinite conclusion rests on family_resolution.md, not on this bounded
test.  This program uses only Fraction arithmetic and the exhaustive
collision/antipode candidate set of Lemma 2.2 in the cited source.
"""

from fractions import Fraction
import json


BASE = (1, 4, 5, 6, 7)
HALF = Fraction(1, 2)


def norm(x: Fraction) -> Fraction:
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def ml_and_times(m: int):
    speeds = BASE + (m,)
    candidates = set()
    for i, u in enumerate(speeds):
        for v in speeds[i + 1 :]:
            for denominator in (u + v, abs(u - v)):
                if denominator:
                    candidates.update(
                        Fraction(a, denominator) for a in range(denominator)
                    )
    scored = [(min(norm(t * v) for v in speeds), t) for t in candidates]
    value = max(score for score, _ in scored)
    times = tuple(sorted(t for score, t in scored if score == value))
    return value, times


def expected(m: int):
    if m % 11:
        r = m % 11
        if r in (2, 9):
            times = (Fraction(4, 11), Fraction(7, 11))
        elif r in (3, 8):
            times = (Fraction(5, 11), Fraction(6, 11))
        else:
            times = tuple(Fraction(k, 11) for k in (4, 5, 6, 7))
        return Fraction(2, 11), times
    n = m // 11
    if n == 1:
        return Fraction(2, 13), (Fraction(4, 13), Fraction(9, 13))
    if n == 2:
        return Fraction(2, 13), tuple(Fraction(k, 13) for k in (4, 6, 7, 9))
    q = 11 * n + 4
    return Fraction(2 * n, q), (
        Fraction(5 * n + 2, q),
        Fraction(6 * n + 2, q),
    )


def intersect_unions(left, right):
    pieces = []
    for a, b in left:
        for c, d in right:
            lo, hi = max(a, c), min(b, d)
            if lo <= hi:
                pieces.append((lo, hi))
    pieces.sort()
    merged = []
    for lo, hi in pieces:
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def base_superlevel(delta: Fraction):
    feasible = [(Fraction(0), HALF)]
    for v in BASE:
        allowed = []
        for k in range(v + 1):
            lo = Fraction(k, v) + delta / v
            hi = Fraction(k + 1, v) - delta / v
            lo, hi = max(lo, Fraction(0)), min(hi, HALF)
            if lo <= hi:
                allowed.append((lo, hi))
        feasible = intersect_unions(feasible, allowed)
    return feasible


def main():
    expected_superlevel = [
        (Fraction(4, 13), Fraction(4, 13)),
        (Fraction(14, 39), Fraction(24, 65)),
        (Fraction(41, 91), Fraction(6, 13)),
    ]
    assert base_superlevel(Fraction(2, 13)) == expected_superlevel

    tested = set(m for m in range(2, 181) if m not in BASE)
    tested.update(11 * n for n in range(1, 101))
    tested.update((11 * 127, 11 * 251))
    for m in sorted(tested):
        actual = ml_and_times(m)
        target = expected(m)
        assert actual == target, (m, actual, target)

    print(
        json.dumps(
            {
                "arithmetic": "exact Fraction",
                "base_superlevel_at_2_over_13": [
                    [str(a), str(b)] for a, b in expected_superlevel
                ],
                "parameters_checked": len(tested),
                "all_admissible_m_through": 180,
                "multipliers_n_through": 100,
                "additional_multipliers": [127, 251],
                "status": "pass",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

