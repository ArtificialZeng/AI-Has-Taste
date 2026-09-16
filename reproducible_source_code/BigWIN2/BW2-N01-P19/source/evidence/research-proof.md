# A separation certificate for the second remainder set

Research job: `newwin-00001-p19-research-c7978facb398`, 2026-09-12.
This is a complete proposed mathematical argument for fresh referee review,
not an acceptance report or a publication manuscript.

## Exact claim and scope

For every positive integer n, put

    S_0(n) = {1,...,floor(n/2)},
    S_(j+1)(n) = {n mod k : k in S_j(n), k>0},
    s_j(n) = |S_j(n)|.

All braces denote sets. Zero is counted as a value but never used as a
modulus. We prove the frozen original claim: s_2(n)/n has no limit.
The assertion is only for j=2; no conclusion about j>=3 is claimed.

Define

    L_Q = lcm{p*q : 3<=q<=Q, p prime, p<q},
    L = L_10 = 75600,
    M = L_50 = 691374732709966591241323368000,
    alpha = 30093341768093808664597/276977102566985955634500,
    beta  = 1182869/9979200,
    delta = beta-alpha
          = 131410063319607383019139/13294900923215325870456000 > 0.

The stronger proposed certificate, valid for every integer t>=1, is

    s_2(M*t)/(M*t) <= alpha + (M+3)/(M*t),                  (T1)
    s_2(L*t+1)/(L*t+1) >= beta - (L+2)/(L*t+1).            (T2)

These imply the required limsup and liminf bounds along two increasing
sequences tending to infinity. Section 6 also gives separated, fixed finite
bounds for every t>=203.

## 1. An exact positive-remainder identity

For positive integers n and r,

    r in S_2(n)
    iff there exist q>=3 and a prime p<q such that
        (q+1)*r <= n-q and p*q divides (q-1)*n+r.          (1)

To prove the forward implication, take k in S_1(n) with n=q*k+r and
0<r<k. There is an integer h with 1<=h<=floor(n/2) such that
n=a*h+k, 0<=k<h, and a>=2. In fact k>=r+1>0. Hence
n>=2*(k+1)+k=3*k+2, so q=floor(n/k)>=3. Choose a prime
p dividing a. Then

    (n-k)/p >= h > k,
    p < n/k-1 = q-1+r/k < q.

Since q*(n-k)=(q-1)*n+r, the asserted divisibility holds.
Finally k>=r+1 is precisely (q+1)*r<=n-q.

Conversely, suppose the right side of (1) holds. Reducing its divisibility
modulo q gives q|(n-r). Define k=(n-r)/q. The inequality gives
k>=r+1. The identity q*(n-k)=(q-1)*n+r and divisibility by p*q
give p|(n-k), even if p divides q: this is cancellation in an integer
divisibility, not division by a unit modulo p. Put h=(n-k)/p. Because
p<=q-1 and r>0,

    n-k=(q-1)*k+r > p*k,

so h>k. Also p>=2 and k>0 give h<=floor(n/2). Thus
n=p*h+k, 0<=k<h, proves k in S_1(n), and n=q*k+r,
0<r<k, proves r in S_2(n). This proves (1).

Identity (1) concerns positive r only. The difference between |S_2(n)|
and its positive part is either zero or one, without any assumption about
whether zero occurs. For n=1 the sets are empty, consistently with (1).

## 2. Uniform finite cutoff and residue counting

For Q>=3 let U_Q(n) be the set of positive r supplied by (1) with q<=Q,
and write T_Q(n)=|U_Q(n)|. Clearly U_Q(n) is contained in S_2(n).
If a positive element is missing from U_Q(n), choose any witness in (1).
Its q is at least Q+1, and

    r <= (n-q)/(q+1) < n/(q+1) <= n/(Q+2).

There are at most floor(n/(Q+2)) such positive integers. Including zero,

    0 <= s_2(n)-T_Q(n) <= floor(n/(Q+2))+1.              (2)

Fix a residue b modulo L_Q and n congruent to b. For each residue a
modulo L_Q, let w_b(a) be the least q in {3,...,Q} for which

    p*q divides (q-1)*b+a for some prime p<q,             (3)

and put w_b(a)=infinity if there is none. This test is unchanged upon
replacing n by b or r by a, since every p*q divides L_Q.
Let A_q(b) be the number of residues with w_b(a)=q. Set

    H_q(n)=floor((n-q)/(q+1))=floor((n+1)/(q+1))-1,
    C_Q(b)=sum_(q=3)^Q A_q(b)/(L_Q*(q+1)).               (4)

The endpoint H_q(n) is nonincreasing in q. Consequently the entire
contribution of a class with w_b(a)=q is exactly its positive
representatives at most H_q(n); a later witness cannot extend it.

For n>=Q all these endpoints are nonnegative. Represent each class by
c in {1,...,L_Q}, taking c=L_Q for the zero class. The exact count up to
an integer H>=0 is floor((H+L_Q-c)/L_Q), which differs from H/L_Q
by at most 1. Also |H_q(n)-n/(q+1)|<2. For each eligible class the
error relative to n/(L_Q*(q+1)) is therefore at most 1+2/L_Q.
There are at most L_Q such classes, proving

    |T_Q(n)-n*C_Q(b)| <= L_Q+2                           (5)

for every n>=Q in the fixed progression. In particular the bound is
uniform as n tends to infinity within that progression. Combining (2)
and (5) yields

    C_Q(b)-(L_Q+2)/n <= s_2(n)/n
        <= C_Q(b)+1/(Q+2)+(L_Q+3)/n.                    (6)

The upper error includes both the floor allowance and the possible zero.

## 3. Exact coefficient for n congruent to 1 modulo L_10

Condition (3) is the union of residue classes

    a congruent to -(q-1) modulo p*q.

The following is the complete first-witness count at Q=10:

| q | A_q(1) |
|---|--------|
| 3 | 12600 |
| 4 | 12600 |
| 5 | 6930 |
| 6 | 7770 |
| 7 | 4110 |
| 8 | 3540 |
| 9 | 165 |
| 10 | 1128 |

Here the finite domain is exactly {0,...,75599}; no symmetry reduction,
random sampling, or prefix extrapolation is involved. One complete
integer-arithmetic enumeration proving the table is:

```python
L = 75600
first = [0] * L
counts = [0] * 11
primes = [2, 3, 5, 7]
for q in range(3, 11):
    for p in primes:
        if p >= q:
            continue
        modulus = p*q
        for a in range((1-q) % modulus, L, modulus):
            if first[a] == 0:
                first[a] = q
                counts[q] += 1
```

Every congruence in (3) is enumerated once for each allowed (q,p), and
the first assignment is its least q. Thus this is exhaustive. The supplied
research verifier also derives the table by generalized CRT intersections
and exact inclusion-exclusion, without scanning these residues. Its recurrence
uses 1_(E union F)=1_E+1_F-1_(E intersection F). An intersection of two
classes modulo m,d is empty unless their residues agree modulo gcd(m,d);
otherwise it is one class modulo lcm(m,d). Its size in a period L is
L/lcm(m,d). This gives a separate finite arithmetic check of the table.

Substitution into (4) gives the exact equality

    C_10(1) = (1/75600)*(12600/4+12600/5+6930/6+7770/7
                          +4110/8+3540/9+165/10+1128/11)
            = 1182869/9979200 = beta.                    (7)

## 4. Exact coefficient for n congruent to zero

For b=0, condition (3) reduces to p*q|r. The least eligible q for a
positive r is the minimum of the following candidates:

* the second smallest distinct prime divisor of r, if it exists;
* p^2 for every prime p with p^3|r.

Candidates larger than Q are ignored for w_0. To prove this classification,
consider any witness (q,p). If q is prime, r has two distinct prime
divisors whose second smallest is at most q. If q is composite and has
a prime divisor ell different from p, then

    q'=max(p,ell), p'=min(p,ell)

is a witness with 3<=q'<q. If no such ell exists, q is a power p^a
with a>=2; then p^3|r, and q'=p^2<=q is a witness. Conversely each
listed candidate gives a witness directly. This proves the classification
and shows that first witnesses are primes or prime squares.

All densities below mean proportions of residues modulo L_Q, not a
heuristic probability model for n. Every prime a<=Q divides L_Q, and
p^3 divides L_Q whenever p^2<=Q. The latter follows by using the
pair (q,p)=(p^2,p) in its definition. Thus CRT makes the indicated
divisibility/valuation conditions independent over the relevant prime
powers. Extra powers in L_Q only repeat the same residue proportions.
The zero residue can be represented by the positive integer L_Q; the
classification uses only prime powers dividing L_Q and remains valid.

Write P_x=product_(a<x, a prime)(1-1/a). For a prime ell>=3, having
first witness ell requires ell|r and exactly one smaller prime p|r.
If p^2<ell, also require p^3 not to divide r, since otherwise p^2
would be an earlier witness. If p^2>ell there is no such restriction.
There is no equality case because ell is prime. All other primes below
ell must be absent. The corresponding densities, for the different p,
are disjoint. The factors for p are respectively

    1/p-1/p^3  or  1/p.

Dividing these by the missing factor 1-1/p in P_ell gives respectively
1/p+1/p^2 or 1/(p-1). Hence

    d_ell = A_ell(0)/L_Q
           = (P_ell/ell)*sum_(p<ell, p prime) h(p,ell),
    h(p,ell) = 1/p+1/p^2 if p^2<ell, and 1/(p-1) otherwise. (8)

For first witness p^2, precisely p^3|r and absence of every other prime
below p^2 are required. Any such other prime would create an earlier
prime-pair witness, and with all of them absent no earlier witness exists.
Therefore

    d_(p^2) = A_(p^2)(0)/L_Q
            = (1/p^3)*P_(p^2)/(1-1/p)
            = P_(p^2)/(p^2*(p-1)).                       (9)

For other q the density is zero. Formulas (8)-(9) are valid whenever the
displayed witness is <=Q, independently of any larger cutoff.

## 5. Rational evaluation and subsequence limits

At Q=50, formulas (8)-(9) give the following nonzero d_q:

| q | d_q |
|---|-----|
| 3 | 1/6 |
| 4 | 1/12 |
| 5 | 1/12 |
| 7 | 2/35 |
| 9 | 4/315 |
| 11 | 116/3465 |
| 13 | 16/585 |
| 17 | 304/15015 |
| 19 | 12224/692835 |
| 23 | 31104/2187185 |
| 25 | 27648/16900975 |
| 29 | 59242752/5391411025 |
| 31 | 1689209856/167133741775 |
| 37 | 31905792/3829070245 |
| 41 | 28931530752/3900644404195 |
| 43 | 160298237952/22952212862579 |
| 47 | 18484212400128/2928046583754721 |
| 49 | 38220595200/81013146586099 |

Consequently, in exact rational arithmetic,

    C_50(0) = sum_(q=3)^50 d_q/(q+1)
             = 6191714756605250456368/69244275641746488908625,
    C_50(0)+1/52 = alpha,
    C_10(1)-alpha = delta > 0.                            (10)

The verifier recomputes every entry from (8)-(9). It also constructs the
divisibility-indicator inclusion-exclusion expressions for the first-witness
events, checks their densities by summing signed 1/d factors, and computes
exact finite truncated counts on the proposed progressions. It never scans
the whole period L_50 or computes literal S_2(M*t).

Applying (6) with (Q,b,n)=(50,0,M*t) proves (T1), and applying its
lower bound with (Q,b,n)=(10,1,L*t+1) proves (T2), for all t>=1.
Taking limsup and liminf, respectively, gives

    limsup_(t->infinity) s_2(M*t)/(M*t) <= alpha
        < beta <= liminf_(t->infinity) s_2(L*t+1)/(L*t+1).

If s_2(n)/n had a limit, both subsequences would have that limit,
contradicting this strict separation. This completes the proposed proof
of the frozen original statement.

## 6. A common finite threshold, with every error retained

Set

    A=(M+3)/M,
    B=(L+2)/L=37801/37800.

Since (L+2)/(L*t+1)<=B/t, (T1)-(T2) give, for t>=203,

    s_2(M*t)/(M*t) <= alpha+A/203 =: alpha_*,
    s_2(L*t+1)/(L*t+1) >= beta-B/203 =: beta_*.

The exact remaining gap is

    beta_*-alpha_* = delta-(A+B)/203
      = 559612671694976819161613011/
        17543633842515402252748580463000 > 0.             (11)

Thus 203 is an explicit common integer threshold. In fact it equals
floor((A+B)/delta)+1; at 202 the corresponding coarse error allowance
does not separate. No minimality for the actual remainder counts is claimed.

## Dependencies, evidence limits, and gap list

The mathematical dependencies are Euclidean division, existence of a prime
divisor of every integer >=2, elementary finite set counting, the Chinese
remainder theorem, and the explicitly specified exact finite arithmetic.
No asymptotic theorem from the source paper is used in the proof itself.

The source comparison is with Baraskar and Vukusic, *Bounds for Sets of
Remainders*, JIS 29 (2026), Article 26.1.4, Theorem 3 (p.4) and Problem 2
(p.16). The latter asks the all-j>=2 question; only its j=2 specialization
is resolved by this proposed argument. The full primary PDF and its supplied
text are preserved in `evidence/external/`. The live source and a bounded
current-literature search are documented in `literature/research-literature.md`.
No equivalent result was found there on 2026-09-12; priority is not certified.

`evidence/research_verify.py` and `evidence/research-verification.json` record
reproducible arithmetic and targeted adversarial tests. Their finite tests do
not establish the universally quantified lemmas: Sections 1-4 supply those
arguments. The proposer did not use an independent model context or external
mathematical referee during this pass. Fresh review remains required.

Known mathematical gaps: none identified by this research pass.
Pending process: a fresh referee must attack the membership identity, the
first-witness density classification, the counting error, and the exact gap.
