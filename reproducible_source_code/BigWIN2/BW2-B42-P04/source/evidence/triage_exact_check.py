#!/usr/bin/env python3
"""Exact discrete-log triage check; uses integer arithmetic only."""


LIMIT = 20_000


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for q in range(2, int((limit - 1) ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q : limit : q] = b"\x00" * (((limit - 1 - q * q) // q) + 1)
    return [q for q in range(limit) if sieve[q]]


def prime_divisors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def primitive_root(p):
    n = p - 1
    factors = prime_divisors(n)
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def log_table(p, g):
    logs = [None] * p
    x = 1
    for j in range(p - 1):
        logs[x] = j
        x = x * g % p
    assert x == 1 and all(logs[x] is not None for x in range(1, p))
    return logs


def witnessed_parameters(p, k):
    """For chi(g)=exp(2*pi*i*k/(p-1)), return exact qualifying a's."""
    n = p - 1
    g = primitive_root(p)
    logs = log_table(p, g)
    plus, minus = n // 6, 5 * n // 6
    assert k * (n // 2) % n == 0  # chi(-1)=1
    return [
        a
        for a in range(2, p)
        if {(k * logs[a]) % n, (k * logs[(1 - a) % p]) % n} == {plus, minus}
    ]


eligible = [p for p in primes_below(LIMIT) if p % 12 == 1]
sextic = [(p, witnessed_parameters(p, (p - 1) // 6)) for p in eligible]
bad = [p for p, values in sextic if not values]

# At p=13, enumerate every even exponent k, i.e. every character with chi(-1)=1.
p = 13
all_p13 = sorted(
    {a for k in range(2, p - 1, 2) for a in witnessed_parameters(p, k)}
)

print(f"range: primes p < {LIMIT} with p == 1 (mod 12)")
print(f"eligible prime count: {len(eligible)}")
print(f"zero sextic-character parameter counts: {bad}")
print(f"p=13 parameters over every allowed character: {all_p13}")
print("first twelve sextic-character results (p, count, first witnesses):")
for p, values in sextic[:12]:
    print(p, len(values), values[:4])
