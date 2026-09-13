"""Exact finite triage scan; observations printed here are not an all-m proof."""

from fractions import Fraction

BASE = (1, 4, 5, 6, 7)


def norm(x: Fraction) -> Fraction:
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def ml_and_times(m: int):
    speeds = BASE + (m,)
    candidates = set()
    for i in range(6):
        for j in range(i + 1, 6):
            for denominator in (speeds[i] + speeds[j], abs(speeds[i] - speeds[j])):
                if denominator:
                    candidates.update(Fraction(a, denominator) for a in range(denominator))
    scored = [(min(norm(t * v) for v in speeds), t) for t in candidates]
    value = max(score for score, _ in scored)
    times = tuple(sorted(t for score, t in scored if score == value))
    return value, times


if __name__ == "__main__":
    for m in range(1, 121):
        if m in BASE:
            continue
        value, times = ml_and_times(m)
        print(m, value, ",".join(map(str, times)))

    print("multiples of 11")
    for n in range(1, 81):
        m = 11 * n
        value, times = ml_and_times(m)
        print(n, m, value, ",".join(map(str, times)))
