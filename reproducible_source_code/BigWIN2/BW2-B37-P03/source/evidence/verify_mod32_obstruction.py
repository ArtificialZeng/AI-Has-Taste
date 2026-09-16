#!/usr/bin/env python3
"""Exhaustively verify the residue obstruction used in the proof.

Dynamic programming compresses all 32^18 residue vectors to their three
power sums modulo 32 and whether at least one coordinate is odd.  A primitive
cleared-denominator solution must lie in the latter class.
"""

MODULUS = 32
NUMBER_OF_COORDINATES = 18

contributions = {
    (pow(a, 2, MODULUS), pow(a, 4, MODULUS), pow(a, 6, MODULUS), a % 2)
    for a in range(MODULUS)
}

states = {(0, 0, 0, 0)}
for _ in range(NUMBER_OF_COORDINATES):
    states = {
        (
            (s2 + t2) % MODULUS,
            (s4 + t4) % MODULUS,
            (s6 + t6) % MODULUS,
            has_odd | is_odd,
        )
        for s2, s4, s6, has_odd in states
        for t2, t4, t6, is_odd in contributions
    }

# D=2d with d odd gives (4,12,8); D=4d gives (16,0,0);
# and v_2(D)>=3 gives (0,0,0), all modulo 32.
targets = {
    "v2(D)=1": (4, 12, 8, 1),
    "v2(D)=2": (16, 0, 0, 1),
    "v2(D)>=3": (0, 0, 0, 1),
}

for label, target in targets.items():
    assert target not in states, (label, target)

print(f"distinct single-coordinate contributions: {len(contributions)}")
print(f"reachable compressed states after 18 coordinates: {len(states)}")
print("none of the three denominator-valuation targets is reachable")
