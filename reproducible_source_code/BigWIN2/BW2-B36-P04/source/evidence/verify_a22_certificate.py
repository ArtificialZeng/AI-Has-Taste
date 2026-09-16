#!/usr/bin/env python3
"""Standard-library-only deterministic verification of the a_22 certificate."""
from math import gcd, isqrt

Q = 108_099_707
RESIDUES = [
    1, 3, 11, 123, 15131, 12747749, 4130680, 59509522,
    53448106, 101159942, 81091708, 50080613, 13474761,
    51643108, 36226811, 44888898, 33268166, 18262376,
    80442749, 68864772, 83683223, 103702901, 0,
]


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def verify_pocklington(n: int, factors: dict[int, int], rows: dict[int, tuple[int, int]]) -> None:
    """Check a full-factorization instance of Pocklington's theorem."""
    f = 1
    for p, exponent in factors.items():
        assert trial_prime(p) or p == 34361
        f *= p**exponent
    assert f == n - 1 and f > isqrt(n)
    assert set(rows) == set(factors)
    for p, (base, expected_x) in rows.items():
        assert pow(base, n - 1, n) == 1
        x = pow(base, (n - 1) // p, n)
        assert x == expected_x
        assert gcd(x - 1, n) == 1


def main() -> None:
    # The only non-small auxiliary prime is first certified.  Here 859 is
    # proved prime by exhaustive trial division through floor(sqrt(859))=29.
    assert all(trial_prime(p) for p in (2, 5, 11, 13, 859))
    verify_pocklington(
        34361,
        {2: 3, 5: 1, 859: 1},
        {2: (3, 34360), 5: (2, 15387), 859: (2, 1951)},
    )
    # With 34361 now prime, this full factorization and the four witness rows
    # certify Q by Pocklington's theorem.
    verify_pocklington(
        Q,
        {2: 1, 11: 2, 13: 1, 34361: 1},
        {
            2: (2, 108099706),
            11: (2, 54894374),
            13: (2, 39708810),
            34361: (2, 99912603),
        },
    )

    r = 1
    computed = [r]
    for _ in range(22):
        r = (r * r + 2) % Q
        computed.append(r)
    assert computed == RESIDUES and computed[-1] == 0

    a = 1
    for _ in range(5):
        a = a * a + 2
    assert a == 228947163 and 1 < Q < a
    print("PASS")
    print(f"certified_prime {Q}")
    print("a5 228947163")
    print("a22_mod_q 0")
    print("residue_count 23")


if __name__ == "__main__":
    main()
