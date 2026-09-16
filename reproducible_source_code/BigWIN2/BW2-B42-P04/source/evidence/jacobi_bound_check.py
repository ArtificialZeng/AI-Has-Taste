#!/usr/bin/env python3
"""Exact audit of the sextic Jacobi bound and its finite remainder.

Only integer arithmetic is used.  The coefficient c_d is
zeta_6^d + zeta_6^{-d}, represented by its exact integer value.
"""


C = (2, 1, -1, -2, -1, 1)
ANALYTIC_CUTOFF = 194


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True


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
    factors = prime_divisors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("primitive root not found")


def sextic_witnesses(p):
    """Return a with chi(a),chi(1-a) having exponents {1,5} mod 6."""
    g = primitive_root(p)
    logs_mod_6 = [None] * p
    x = 1
    for exponent in range(p - 1):
        logs_mod_6[x] = exponent % 6
        x = x * g % p
    assert x == 1 and all(v is not None for v in logs_mod_6[1:])
    return [
        a
        for a in range(2, p)
        if {logs_mod_6[a], logs_mod_6[(1 - a) % p]} == {1, 5}
    ]


def witness_certificate(p, a):
    """Return (primitive root, log_g(a) mod 6, log_g(1-a) mod 6)."""
    g = primitive_root(p)
    logs_mod_6 = [None] * p
    x = 1
    for exponent in range(p - 1):
        logs_mod_6[x] = exponent % 6
        x = x * g % p
    return g, logs_mod_6[a], logs_mod_6[(1 - a) % p]


def all_allowed_character_witnesses(p):
    """Union of witnesses over every character satisfying chi(-1)=1."""
    g = primitive_root(p)
    n = p - 1
    logs = [None] * p
    x = 1
    for exponent in range(n):
        logs[x] = exponent
        x = x * g % p
    target = {n // 6, 5 * n // 6}
    result = set()
    for k in range(1, n):
        if k * (n // 2) % n != 0:
            continue
        for a in range(2, p):
            if {
                k * logs[a] % n,
                k * logs[(1 - a) % p] % n,
            } == target:
                result.add(a)
    return sorted(result)


# Jacobi expansion audit.  Generic pairs have r,s,r+s all nonzero mod 6.
inverse_pairs = [(r, s) for r in range(1, 6) for s in range(1, 6)
                 if (r + s) % 6 == 0]
generic_pairs = [(r, s) for r in range(1, 6) for s in range(1, 6)
                 if (r + s) % 6 != 0]
principal_axis_coefficient_sum = sum(C[r] for r in range(1, 6))
inverse_coefficient_sum = sum(C[(r - s) % 6] for r, s in inverse_pairs)
generic_absolute_mass = sum(abs(C[(r - s) % 6]) for r, s in generic_pairs)

assert len(inverse_pairs) == 5
assert len(generic_pairs) == 20
assert principal_axis_coefficient_sum == -2
assert inverse_coefficient_sum == -2
assert generic_absolute_mass == 28

# p+1 > 14*sqrt(p) is equivalent to (p+1)^2 > 196p.
assert (ANALYTIC_CUTOFF + 1) ** 2 > 196 * ANALYTIC_CUTOFF
assert ANALYTIC_CUTOFF ** 2 <= 196 * (ANALYTIC_CUTOFF - 1)
# For f(n)=(n+1)^2-196n, f(n+1)-f(n)=2n-193>0 for n>=194.
assert 2 * ANALYTIC_CUTOFF - 193 > 0

eligible = [p for p in range(2, ANALYTIC_CUTOFF) if is_prime(p) and p % 12 == 1]
finite_results = [(p, sextic_witnesses(p)) for p in eligible]

assert all(values for p, values in finite_results if p >= 37)
assert all_allowed_character_witnesses(13) == []

print("coefficient audit:")
print("  principal-axis coefficient sum (each axis):", principal_axis_coefficient_sum)
print("  inverse-pair coefficient sum:", inverse_coefficient_sum)
print("  generic pair count:", len(generic_pairs))
print("  generic absolute coefficient mass:", generic_absolute_mass)
print("analytic bound: S_p >= (p + 1 - 14*sqrt(p))/18")
print("analytic positivity for every integer p >=", ANALYTIC_CUTOFF)
print("finite eligible primes p < 194 and sextic witnesses:")
for p, values in finite_results:
    print(" ", p, "count", len(values), "witnesses", values)
print("one certificate (p, primitive root, a, log(a) mod 6, log(1-a) mod 6):")
for p, values in finite_results:
    if p >= 37:
        g, log_a, log_one_minus_a = witness_certificate(p, values[0])
        print(" ", p, g, values[0], log_a, log_one_minus_a)
print("p=13 witnesses over all allowed nontrivial characters:",
      all_allowed_character_witnesses(13))
