# Mathematical triage evidence

Job: `newwin-00001-p16-triage-b3295de4c9e7`, 2026-09-12.
This is a checked research route and an exact finite observation. It is not
a fresh referee report or an accepted resolution-paper claim.

## Universal reduction, checked directly

Let h(m)=sigma(m)/m and suppose an integer in the frozen domain violates the
desired conclusion, so b_i=p_i^(a_i+1) >= 2R for all five i. Put
D=product(p_i-1), H=R/D, and E=R-2D.

1. The multiplicative formula gives h(n)=H product(1-1/b_i)<H. Since
   h(n)>=2, E is a positive odd integer. If p1>=5, monotonicity of
   p/(p-1) would give H <= 85085/46080 < 2 from the five smallest
   allowable primes 5,7,11,13,17. Therefore p1=3.
2. The quotient formula, also valid when a1=1, is

       h(n/3) = (R/D)(1-3/b1) product_{i=2}^5(1-1/b_i).

   For 0<=u_i<=1, product(1-u_i)>=1-sum(u_i). One proof by induction
   uses 1-P(1-u)=(1-P)+Pu <= (1-P)+u for 0<=P<=1.
   The five losses here sum to at most (3+4)/(2R), hence

       h(n/3) >= (R-7/2)/D.

   If E>=5, this is at least 2+3/(2D)>2, contradicting primitivity.
   Thus any counterexample has E=1 or E=3. No bound on exponents or n
   was used. Non-deficiency equality h(n)=2 remains included.

There is also a simple way to remove E=1. Since 3 divides R, either some
other prime is 1 modulo 3, in which case D=0 modulo 3 and E=0 modulo 3,
or all other primes are 2 modulo 3, in which case D=2 modulo 3 and
E=2 modulo 3. Thus E is never 1 modulo 3. The computation below nevertheless
tests both gaps to compare against the supplied intake route.

## Complete finite search design

For a proper prime prefix, write A=product(p), B=product(p-1). If its gap
g=A-2B is positive, adjoining a prime q changes it to qg+2B>3, and further
adjoining primes increases it. Such a prefix cannot lead to final E=1,3.
Zero gap is impossible because A is odd. Therefore every proper prefix of
a potential exceptional radical has A<2B.

For p2>=15,

    H <= (3/2)(15/14)^4 < 2,

as 3*15^4=151875 < 153664=4*14^4. Thus p2 is one of 5,7,11,13.
For fixed p2=p and p3>=t,

    H <= (3p)/(2(p-1)) * (t/(t-1))^3.

The function t/(t-1) decreases for t>1. The first integer cutoffs and
retained p3 values are:

| p2 | p3 excluded at or above | retained p3 with A<2B |
|---|---|---|
| 5 | 47 | 17,19,23,29,31,37,41,43 |
| 7 | 23 | 11,13,17,19 |
| 11 | 17 | 13 |
| 13 | 15 | none |

The excluded p3=7,11,13 in the first row already give a positive prefix
gap. The exact endpoint products are retained in `gap-divisor-check.json`.
There are precisely 13 remaining prefixes; these are derived bounds, not
chosen search cutoffs.

Fix any of these triples, write c=2B-A>0, and denote the last two primes
by x<y. The gap equation is equivalent to

    (c*x-2B)(c*y-2B) = 2*A*B-c*e = N_e,   e in {1,3}.

Indeed expanding the equation gives
Axy-2B(x-1)(y-1)=e. The four-prime prefix must still have negative gap,
so u=c*x-2B>0; also v=c*y-2B>u. Therefore every possible pair is obtained
from a positive divisor u of N_e with u<=sqrt(N_e), v=N_e/u, followed by

    x=(u+2B)/c, y=(v+2B)/c.

The verifier checks integrality, strict ordering beyond p3, and primality
by division through the integer square root. It lists all divisors through
the integer square root of N_e using exact integer arithmetic. Allowing
u=v in the candidate loop is harmless because x<y is tested afterward.
For each of the 26 equations N_e>0. No prime or exponent is omitted by an
arbitrary numerical limit.

## Reproducible observation and limits

Run from the project root:

    python3 evidence/check_gap_divisors.py

Observed with Python 3.10.12: 13 prefixes, 26 gap equations, 147 divisor
pairs, zero solutions. For E=3, the only integral ordered candidates before
primality checking are (257,65533), (259,22015), (265,7509) at prefix
(3,5,17); (97,9215), (107,925) at prefix (3,5,19); and (27,2079) at
prefix (3,7,11). Each has a visibly composite member: respectively
65533=13*71^2, 259=7*37, 265=5*53, 9215 divisible by 5, 925 divisible
by 5, and 27=3^3. All other E=3 rows have no integral ordered candidates.
Exact divisor lists and all rejection inputs are
in `evidence/gap-divisor-check.json`. The implementation is separate from
the supplied recursive prime search and imports none of its code. It gives
the same empty exceptional set. The input PDF, supplied script and supplied
JSON hashes also match the handoff's stated hashes.

As a nonvacuous control, the same last-pair solver at prefix (3,7), gap 3,
recovers (3,7,13,19): 5187-2*2592=3. This also shows why one cannot
silently assert the auxiliary gap exclusion for four prime factors.

The universal reduction plus a fully verified finite exclusion would prove
the frozen five-prime assertion. The purpose of this bounded triage is to
justify advancing that exact target. Human-readable rejection certificates,
focused novelty review, and eventual fresh mathematical review still belong
to the following phases. No assertion is made for six or more primes, for
the stronger R bound, or for nonprimitive abundant numbers.
