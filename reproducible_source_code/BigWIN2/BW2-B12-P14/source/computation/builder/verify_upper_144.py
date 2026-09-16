#!/usr/bin/env python3
"""Independent exact checker for the arithmetic proof Z(13,23;3,3) <= 144."""
from itertools import product
from math import comb

ROWS, COLS, TARGET = 13, 23, 145
CAPACITY = 2 * comb(ROWS, 3)


def penalty(d: int) -> int:
    return comb(d, 3) - 15 * d + 70


assert CAPACITY == 572
assert all(penalty(d) >= 0 for d in range(ROWS + 1))
assert [d for d in range(ROWS + 1) if penalty(d) == 0] == [6, 7]

# A feasible 145-edge degree histogram has total penalty at most seven.
# Degrees with penalty > 7 cannot occur, so enumerate only degrees 5--8.
profiles = []
for counts in product(range(COLS + 1), repeat=4):
    hist = dict(zip(range(5, 9), counts))
    if sum(counts) != COLS:
        continue
    if sum(d * hist[d] for d in hist) != TARGET:
        continue
    triple_sum = sum(comb(d, 3) * hist[d] for d in hist)
    if triple_sum <= CAPACITY:
        profiles.append((hist, CAPACITY - triple_sum))

expected = [
    ({5: 0, 6: 16, 7: 7, 8: 0}, 7),
    ({5: 0, 6: 17, 7: 5, 8: 1}, 1),
    ({5: 1, 6: 14, 7: 8, 8: 0}, 2),
]
assert profiles == expected, profiles

# Sum of row deficits is three times the global slack.  Every row avoiding
# exceptional degree-5/8 columns has deficit congruent to 132 == 2 (mod 5),
# hence at least two.  Even maximal exceptional coverage yields contradictions.
for hist, slack in profiles:
    exceptional_coverage = 5 * hist[5] + 8 * hist[8]
    clean_rows = max(0, ROWS - exceptional_coverage)
    forced = 2 * clean_rows
    budget = 3 * slack
    assert forced > budget, (hist, forced, budget)

print("PASS: exactly three 145-edge profiles; row-deficit contradictions prove Z<=144")
