# Exact certificate for a prime factor of `a22`

For (a_0=1) and (a_{n+1}=a_n^2+2), set

\[
q=108099707.
\]

## Deterministic primality proof

Use the following standard full-factorization form of Pocklington's theorem. If
(N-1=F), every prime factor of (F) is certified, (F>\sqrt N), and for each
prime (p\mid F) there is an integer (b_p) such that

\[
b_p^{N-1}\equiv1\pmod N,
\qquad
\gcd\left(b_p^{(N-1)/p}-1,N\right)=1,
\]

then (N) is prime.

First,

\[
34361-1=34360=2^3\cdot5\cdot859.
\]

The integer 859 has no prime divisor among
(2,3,5,7,11,13,17,19,23,29), whose residues are respectively
(1,1,4,5,1,1,9,4,8,18); since (29=\lfloor\sqrt{859}\rfloor), 859 is
prime. The other factors 2 and 5 are prime. Exact modular exponentiation gives:

| (p) | (b_p) | (b_p^{34360}\bmod34361) | (b_p^{34360/p}\bmod34361) | gcd with 34361 after subtracting 1 |
|---:|---:|---:|---:|---:|
| 2 | 3 | 1 | 34360 | 1 |
| 5 | 2 | 1 | 15387 | 1 |
| 859 | 2 | 1 | 1951 | 1 |

Thus Pocklington proves that 34361 is prime. Now

\[
q-1=108099706=2\cdot11^2\cdot13\cdot34361.
\]

The factors 2, 11, and 13 are elementary primes, and 34361 was just certified.
Exact modular exponentiation gives:

| (p) | (b_p) | (b_p^{q-1}\bmod q) | (b_p^{(q-1)/p}\bmod q) | gcd with (q) after subtracting 1 |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 108099706 | 1 |
| 11 | 2 | 1 | 54894374 | 1 |
| 13 | 2 | 1 | 39708810 | 1 |
| 34361 | 2 | 1 | 99912603 | 1 |

Therefore Pocklington proves that (q=108099707) is prime.

## Complete exact modular recurrence

Starting with (r_0=1) and computing
(r_{n+1}=(r_n^2+2)\bmod q) gives:

| (n) | (r_n) | (n) | (r_n) |
|---:|---:|---:|---:|
| 0 | 1 | 12 | 13474761 |
| 1 | 3 | 13 | 51643108 |
| 2 | 11 | 14 | 36226811 |
| 3 | 123 | 15 | 44888898 |
| 4 | 15131 | 16 | 33268166 |
| 5 | 12747749 | 17 | 18262376 |
| 6 | 4130680 | 18 | 80442749 |
| 7 | 59509522 | 19 | 68864772 |
| 8 | 53448106 | 20 | 83683223 |
| 9 | 101159942 | 21 | 103702901 |
| 10 | 81091708 | 22 | 0 |
| 11 | 50080613 |  |  |

Hence (a_{22}\equiv r_{22}=0\pmod q).

Finally, exact integer recursion gives (a_5=228947163>108099707=q>1).
All (a_n\ge1), and (a_{n+1}=a_n^2+2>a_n), so (q<a_5<a_{22}).
Thus (q) is a proper prime divisor of (a_{22}), resolving the frozen task.

The standard-library verifier `verify_a22_certificate.py` recomputes every
factorization product, modular power, gcd, auxiliary trial division, recurrence
transition, and the proper-divisor inequality without probable-prime routines.

