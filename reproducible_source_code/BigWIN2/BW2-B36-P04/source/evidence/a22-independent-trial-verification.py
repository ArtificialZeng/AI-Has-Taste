#!/usr/bin/env python3
"""Independent elementary verification of the proposed a_22 factor.

This deliberately does not use the Pocklington data in a22-certificate.md.
Primality of q is checked by exhaustive trial division through floor(sqrt(q)).
"""
from math import isqrt


Q = 108_099_707
EXPECTED = [
    1, 3, 11, 123, 15131, 12747749, 4130680, 59509522,
    53448106, 101159942, 81091708, 50080613, 13474761,
    51643108, 36226811, 44888898, 33268166, 18262376,
    80442749, 68864772, 83683223, 103702901, 0,
]


def main() -> None:
    bound = isqrt(Q)
    assert bound == 10397 and bound * bound < Q < (bound + 1) ** 2

    # Every composite positive integer has a prime, hence integer, divisor at
    # most its square root. Checking every integer is redundant but elementary.
    tested = 0
    for divisor in range(2, bound + 1):
        assert Q % divisor != 0
        tested += 1

    residues = [1]
    for _ in range(22):
        residues.append((residues[-1] ** 2 + 2) % Q)
    assert residues == EXPECTED and residues[-1] == 0

    a = 1
    for _ in range(5):
        a = a * a + 2
    assert a == 228_947_163 and 1 < Q < a

    print("PASS")
    print(f"q {Q}")
    print(f"trial_divisors_tested {tested}")
    print(f"largest_trial_divisor {bound}")
    print("recurrence_transitions 22")
    print("a22_mod_q 0")
    print(f"a5 {a}")


if __name__ == "__main__":
    main()
