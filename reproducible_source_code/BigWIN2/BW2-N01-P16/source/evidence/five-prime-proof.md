# Five-prime small-component bound: proof submitted for review

Research job: `newwin-00001-p16-research-ba4f5e168b06`, 2026-09-12.
This is research evidence, not referee acceptance or a manuscript.

**Exact claim.** Let sigma denote the sum of positive divisors. If

    n = product_{i=1}^5 p_i^a_i,   3 <= p_1 < ... < p_5,

where the p_i are distinct primes and all a_i are positive integers, and
sigma(n) >= 2n while sigma(d) < 2d for every positive proper divisor d of n,
then min_{1<=i<=5} p_i^(a_i+1) < 2 product_{i=1}^5 p_i.
This is exactly `source.md`, interpreted in `problem.md`. Perfect numbers
are included; no theorem excluding odd perfect numbers is used.

## 1. Reduction independent of exponent size

Put h(m)=sigma(m)/m, R=product p_i, D=product(p_i-1)=phi(R), and E=R-2D.
The geometric-series formula and multiplicativity give

    h(n) = (R/D) product_{i=1}^5 (1-1/p_i^(a_i+1)) < R/D.

Thus h(n)>=2 implies E>0, and E is odd since R is odd. The function
t/(t-1) strictly decreases for t>1. If p_1>=5, comparison with the five
smallest available odd primes yields

    R/D <= (5*7*11*13*17)/(4*6*10*12*16)
         = 85085/46080 < 2,

a contradiction. Hence p_1=3.

Suppose for contradiction that b_i=p_i^(a_i+1)>=2R for every i. Then

    h(n/3) = (R/D) (1-3/b_1) product_{i=2}^5 (1-1/b_i).       (1)

This formula also holds when a_1=1: the factor corresponding to 3 is
(3/2)(1-1/3)=1, correctly removing 3 from the quotient.

For any u_i in [0,1], product(1-u_i)>=1-sum u_i. Indeed, if a product P
of preceding factors lies in [0,1], then
1-P(1-u)=1-P+Pu <= 1-P+u; induction proves the inequality.
The five losses in (1) are 3/b_1,1/b_2,...,1/b_5. They lie in [0,1]
and sum to at most 7/(2R), so

    h(n/3) >= (R-7/2)/D = 2 + (E-7/2)/D.                   (2)

Primitivity requires h(n/3)<2. Hence E<7/2, forcing E=1 or E=3.
The value E=1 is impossible modulo 3: if one of p_2,...,p_5 is 1 modulo 3,
then D and E are 0 modulo 3; otherwise these four primes are all 2 modulo 3,
so D=2 modulo 3 and E=2 modulo 3. It remains to exclude E=3.

## 2. Complete reduction of the radical equation

We prove that no product of five distinct odd primes has R-2phi(R)=3.
Such a product has R/D>2, so the preceding comparison again forces p_1=3.

For an initial prime prefix let A be its product, B the product of its
primes minus one, and g=A-2B. Adjoining a prime q changes the gap to

    Aq-2B(q-1) = qg+2B.                                   (3)

If g>0, this is >3, and subsequent extensions increase a positive gap.
A proper prefix of a final gap-3 radical cannot therefore have g>0.
Equality g=0 is impossible because A is odd. Every proper prefix has A<2B.

If p_2>=15, monotonicity gives R/D<2, since

    R/D <= (3/2)(15/14)^4,
    3*15^4=151875 < 153664=4*14^4.

Thus p_2 is one of 5,7,11,13. For p_2=p and p_3>=t,

    R/D <= [3p/(2(p-1))] [t/(t-1)]^3.

This is at most 2 if 3pt^3<=4(p-1)(t-1)^3. The following explicit
endpoints and prime lists leave exactly 13 triples:

| p_2 | p_3 excluded at or above t | 3pt^3 | 4(p-1)(t-1)^3 | Retained p_3 after A<2B |
|---:|---:|---:|---:|---|
| 5 | 47 | 1557345 | 1557376 | 17,19,23,29,31,37,41,43 |
| 7 | 23 | 255507 | 255552 | 11,13,17,19 |
| 11 | 17 | 162129 | 163840 | 13 |
| 13 | 15 | 131625 | 131712 | none |

For p_2=5, the omitted primes 7,11,13 give positive three-prime gaps
9,5,3, respectively, and (3) excludes them. The lists otherwise contain
every prime strictly between p_2 and t. These are derived cutoffs, not
assumed numerical bounds on the primes, exponents, or n.

## 3. Exact factor certificate for the final two primes

Fix any of the 13 triples, and put c=2B-A>0. Write x=p_4, y=p_5.
The equation Axy-2B(x-1)(y-1)=3 is equivalent, by expansion, to

    (cx-2B)(cy-2B) = 2AB-3c = N.                          (4)

The four-prime prefix has negative gap, so Ax-2B(x-1)=2B-cx<0.
Therefore u=cx-2B>0 and v=cy-2B>u. Every possible solution comes from
a positive divisor u of N with u^2<N, followed by

    v=N/u,  x=(u+2B)/c,  y=(v+2B)/c.                      (5)

Conversely, any such divisor pair making (5) integral with p_3<x<y and
x,y prime yields a gap-3 radical by expansion. This proves both directions
of the reduction, including exclusion of zero and negative factor branches.

The complete factor table is below. All factorizations are into primes.
`gap3-factor-certificate.md` additionally displays every divisor u<=sqrt(N);
`gap3-factor-certificate.json` records both integrality remainders for each
divisor. Formula (5) yields exactly the ordered integral pairs shown.

| Prefix | B | c | N, factored into primes | All integral pairs with p_3<x<y |
|---|---:|---:|---|---|
| 3,5,17 | 128 | 1 | 65277 = 3^2 * 7253 | (257,65533); (259,22015); (265,7509) |
| 3,5,19 | 144 | 3 | 82071 = 3^2 * 11 * 829 | (97,9215); (107,925) |
| 3,5,23 | 176 | 7 | 121419 = 3^4 * 1499 | none |
| 3,5,29 | 224 | 13 | 194841 = 3^2 * 21649 | none |
| 3,5,31 | 240 | 15 | 223155 = 3^4 * 5 * 19 * 29 | none |
| 3,5,37 | 288 | 21 | 319617 = 3^2 * 17 * 2089 | none |
| 3,5,41 | 320 | 25 | 393525 = 3^3 * 5^2 * 11 * 53 | none |
| 3,5,43 | 336 | 27 | 433359 = 3^2 * 179 * 269 | none |
| 3,7,11 | 120 | 9 | 55413 = 3^2 * 47 * 131 | (27,2079) |
| 3,7,13 | 144 | 15 | 78579 = 3^2 * 8731 | none |
| 3,7,17 | 192 | 27 | 137007 = 3^2 * 13 * 1171 | none |
| 3,7,19 | 216 | 33 | 172269 = 3^2 * 19141 | none |
| 3,11,13 | 240 | 51 | 205767 = 3^3 * 7621 | none |

The six ordered pairs fail primality, respectively, because

    65533=13*5041,  259=7*37,  265=5*53,
    9215=5*1843,    925=5*185, 27=3*9.

The only additional integral pair is (25,5375) at prefix (3,5,43); it fails
x>43. Allowing u^2=N in the loop is harmless because x<y is tested.

The finite arithmetic is fully reproducible: trial division proves every
displayed prime factor prime; multiplication verifies N; expanding prime
powers through their multiplicities generates all divisors. Filtering by
u^2<=N leaves 95 divisor pairs in the 13 rows. Testing u+2B and N/u+2B
modulo c gives the displayed pairs. The largest displayed prime factor is
21649, so its primality test needs no trial divisor above 147. The script
`reconstruct_gap3.py` executes these steps with exact integers and compares
every divisor and both congruence remainders with the earlier direct-divisor
calculation. The written completeness reduction covers all prime sizes.

This excludes E=3 and proves the radical lemma. Section 1 now has no
possible E, a contradiction. Thus the simultaneous inequalities b_i>=2R
cannot hold, proving the strict bound in the original scope.

## Dependencies, falsification, and review

The proof uses only the divisor-sum formula, monotonicity, the proved
product inequality, congruences, and the finite table. No classification
of primitive non-deficient numbers or unproved external theorem is used.

The earlier `check_gap_divisors.py` enumerated divisors directly. The new
`reconstruct_gap3.py` rebuilds prime factorizations and divisors without
importing the earlier code. All 13 rows agree. Both recover the control
3*7*13*19=5187, with phi(5187)=2592 and gap 3. Thus the radical exclusion
is not asserted for four primes. The proof does not address six or more
primes or the stronger R bound. It uses no exponent truncation or floats.

A further exact attack avoids factoring N altogether. Solving the original
gap equation for y gives y=[2B(x-1)-3]/(cx-2B), with positive denominator.
Since y>x, one has cx^2<4Bx-2B-3<4Bx and therefore x<4B/c. The new script
enumerates every integer p_3<x<4B/c, testing the quotient for integrality
and y>x. Across the 13 triples this checks 937 values and recovers exactly
the same six ordered pairs. This bound follows from the equation and
ordering, and is not an independently chosen numerical cutoff.

Known mathematical gaps: none identified in this proposer pass. Fresh
referee review is required. Agreement of programs is not acceptance.
The decisive audit target is completeness of the prefix signs and (4),
independent recomputation of all 13 rows, and verification of (1)-(2),
including a_1=1 and h(n)=2.

The nearest primary source and the limited novelty comparison are recorded
in `literature/research-screen.md`. No global priority guarantee is made.
