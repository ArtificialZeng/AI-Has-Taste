# Independent mathematical referee report

**Verdict: accept the exact frozen conjecture-note scope.**

Job: `primary-20260913-subsum-denominator-referee-681ef09731fa`.
Reviewed on 2026-09-13 UTC. Snapshot:
`c33bf573f4ff5837fe88c72e3f97531b9de48fe90675139f240935896a34a200`.
The frozen workflow fields remain `kind = conjecture-note` and
`original_status = unresolved`.

K_sharp_v1 is accepted for presentation as an explicitly unproved conjecture
with the submitted supporting results. Neither K_sharp_v1 nor the original
all-n, all-index log-concavity conjecture has been proved in this review.
The accepted fixed-edge theorem retains its submitted cutoff 96. Further
referee tests below are falsification evidence, not a revision of that scope.

## Inputs and independence

I read the original statement, its precise interpretation, the claim, the
snapshot and its listed decisive arguments, programs, serialized certificates
and primary-source passages. I did not read checkpoint.md, state.json,
earlier job transcripts or an earlier audit verdict. Assertions of success
inside the supplied evidence were not treated as certification. All 23 frozen
file hashes and the canonical snapshot digest were checked before and after
the fresh computation. No frozen input was changed.

The new verifier imports no research program. It is an independently written
implementation in this fresh referee job, not statistically independent
evidence or a formal proof-assistant check. The review used exact integer
arithmetic throughout. Reproduction, from the project directory:

```
python3 audit/referee_exact.py
python3 audit/referee_supplement.py
```

These commands read the frozen inputs and write only referee artifacts under
audit/. Results are in `audit/referee_exact.json` and
`audit/referee_supplement.json`. The first run completed in 64.691 seconds.

## Reconstruction of the reduction

For an actual recurrence stage at n, write n=s*2^t. The factors preceding
1+x^s are precisely those of degrees s/2, s/4, ..., s/2^{v_2(s)}.
Consequently the submitted a_{s,t} includes every preceding dyadic factor,
and every actual ascending stage occurs in this parametrization.

Writing E_i(n)=#{q>=0:2^q i<n}, splitting off q=0 gives

\[
E_i(2n)-E_i(n)=\mathbf1_{i<2n}.
\]

At the specified least start tau, m=j+1<2s*2^tau. Thus every exponent
needed for the coefficient triple grows by exactly one at every subsequent
doubling. The earlier-stage factors do not depend on t. With
A=a_{s,tau} and P_m=product_{i=1}^m(1+x^i), this proves

\[
a_{s,\tau+u}\equiv A P_m^u\pmod{x^{m+1}},\qquad u\ge0.
\]

The coefficient at degree r is a polynomial in u of degree at most r.
Every nonzero product in F has total coefficient index at most 2j; negative
indices contribute zero. Hence deg F(tau+u)<=2j. Newton interpolation is
therefore an exact identity with coefficients Delta^h F(tau), not an
assumption inferred from fitting a finite grid. Tau exists for every allowed
(s,j), and j=0 gives the constant F=1.

Expanding twice the new bivariate product minus the old product and its
shift gives the multiplier

\[
2(1+x^s)(1+y^s)-1-(xy)^s
=1+2x^s+2y^s+(xy)^s.
\]

With L_j(W)=[x^jy^j]W-[x^{j-1}y^{j+1}]W, this proves the submitted
identity

\[
\Delta^h F(\tau)=L_j\bigl(A(x)A(y)
(1+2x^s+2y^s+(xy)^s)(P_m(x)P_m(y)-1)^h\bigr).
\]

The minus sign in L_j prevents an inference from coefficient positivity
alone. In particular, the supplied generic example A=1,s=3,j=2 has values
-3 and -1 at h=1,2 by direct homogeneous expansion. It does not have the
actual-stage hypothesis. This also confirms why a general positivity slogan
would not establish the submitted conjecture.

## Exact certificate and fixed-edge theorem

The fresh coefficient construction used a different product representation.
For N=s*2^t-1 and o the odd part of s, dyadic telescoping gives

\[
a_{s,t}(x)=\frac{1-x^s}{1-x^o}
\prod_{\substack{d\le N\\d\text{ odd}}}(1-x^d)^{-e_{N,d}}
\prod_{\substack{d\le2N\\d\text{ even}}}(1-x^d),
\quad e_{N,d}=\#\{q\ge0:2^qd\le N\}.
\]

For a product of (1-x^d)^{-g_d}, its logarithmic-derivative coefficients
are beta_r=sum_{d|r}d*g_d. The recursion
r*a_r=sum_{k=1}^r beta_k*a_{r-k} reconstructs the coefficients; every
division was checked exact. This representation was additionally compared
against full direct products at all 48 stages for 9<=n<=32.

Every margin used for the dense verification was reconstructed at its actual
n=s*2^t, without assuming the affine reduction. The fresh program matched
all 4,753 frozen pairs, all 613,137 Newton coefficients, and all 3,126
earlier admissible triples below tau. It checked the exact pair/triple
domains and least-start conditions, not just reported totals. All dense
Newton coefficients are strictly positive. A difference-table computation
was cross-checked with signed binomial sums at up to five orders per pair;
both highest Catalan formulas were checked at every applicable pair.

The finite bases D_1,D_2,D_4,D_8 were rebuilt with full coefficient
sequences and passed. D_3,D_5,D_6,D_7 had negative internal minors, as
expected from the known exceptions.

For an affected shift s<=j+1 and j<=96, nonnegative Newton coefficients
give F>=0 for every t>=tau, and the earlier triples give all remaining
n>=9. If s>=j+2, the coefficient triple is unchanged, T_{j-s}=0, and
F=T_j(old). Starting with D_8, induction over every ascending stage
therefore simultaneously proves the old minors nonnegative and supplies
this unaffected-shift case. H then implies the next minor is nonnegative
because both old indices j and j-s lie within the already controlled
left edge, or are negative zero indices. This induction is not circular.

For old degree L, palindromicity gives F_j=F_{L+s-j}; the two old minors
are interchanged under this reflection. It follows that the right-edge
statement and the submitted bound min(j,deg D_n-j)<=96 hold exactly as
claimed. This is an infinite-n conclusion from a proved polynomial
reduction and exact finite certificates, not from a finite-n prefix test.

## Supporting uniform band and boundary obstruction

For the smoothing lemma, a symmetric degree-d monomial pair reduces the
functional after multiplication by (x+y)^N to

\[
2\binom Nq-\binom N{q-1}-\binom N{q+1}
=\binom Nq\frac{N+2-(N-2q)^2}{(q+1)(N-q+1)}.
\]

Under N+d=2j and N+2>=d^2, the relevant q lies in [0,N] and
|N-2q|<=d. The denominator is positive. The d=0 case is immediate;
for d=1, parity ensures N>=1. Thus the edge and zero-degree cases of
this argument are covered.

Writing R=(x+y)+S and h=2j-k, only residual homogeneous degrees d=k+r
with r<=k can contribute. Thus d<=2k and N=2j-d. The bound
j>=2k^2+k-1 ensures N+2>=d^2 term by term. Nonnegative symmetric
homogeneous components then prove the generic band. Only finitely many
components enter, so no convergence or limiting exchange is involved.

The top two formulas follow from the constant and linear terms of B and
the degree-two term of R, which is (x+y)^2-xy. They yield exactly the
two Catalan expressions in the claim; the second is restricted to j>=1.
The band does not control the low or middle orders in general.

For the boundary lemma set j=2n-1 and m=2n. The polynomial tail, extended
back to u=0, replaces A by A/(1+x^{2n}). Only a_{j+1} changes in the
coefficient range used by F, decreasing by one. In the expanded margin

\[
F=T_j(a)+T_{j-s}(a)+4a_ja_{j-s}
-2a_{j-1}a_{j-s+1}-2a_{j+1}a_{j-s-1},
\]

the coefficient of a_{j+1} is -a_{j-1}-2a_{j-s-1}. This proves the
stated discrepancy. The distinct-part factor product_{i=1}^{n-1}(1+x^i)
has every coefficient positive throughout its support, and 2n-2 is
inside that support for n>=9. Hence the discrepancy is strictly negative.

The tail polynomial has degree at most 4n-2. For h>4n-2 its h-th
difference vanishes; the sole discrepancy at u=0 contributes (-1)^h
times its value. This proves every claimed negative even difference of
order at least 4n. These orders and this start lie outside K_sharp's
assertion. No negativity of the actual H margin follows from this lemma.

The fresh program checked tail extrapolation and the full signed difference
of order 4n at all 112 stages for 9<=n<=64, including 64 stages beyond
the frozen n<=32 checks. For n=s=9,j=17 it recovered F=19668,
tail extrapolation 20795, and difference -1127.

## Independent falsification and computational limits

I chose complete coverage of the next contiguous degree block 97<=j<=128,
including every 1<=s<=j+1 and every 0<=h<=2j. This attacks missing shifts
as well as the transition at a dyadic start. The separate Euler-product
calculation found all 826,288 coefficients in 3,632 templates strictly
positive.

This domain overlaps 24 templates and 6,120 coefficients in the frozen
sparse test. Consequently only 3,608 templates and 820,168 coefficients
are newly tested relative to all listed frozen Newton certificates.
The overlap is explicitly recorded in `audit/referee_supplement.json`;
the full block is not described as wholly held out.

I inspected the supplied sparse producer and verifier, and freshly checked
the serialized domain, starts, lengths and signs of all 69,632 coefficients
at its 128 listed pairs through j=513. I did not independently rederive
every middle coefficient in that larger sparse domain. Its stated
second-implementation coverage of five low orders, two top formulas and
outside-grid values remains an appropriately limited claim. The exact
supporting fixed-edge theorem does not depend on that sparse extension.

No counterexample was found. This is finite falsification evidence;
arbitrary j and the untested low/middle orders remain unresolved.

## Source comparison and contribution assessment

The cached primary PDFs were hash-verified. I read BBFM pp. 11, 12 and 18
and Chen--Ono--Zhang pp. 4 and 6, and compared the decisive statements
against live primary HTML on 2026-09-13 UTC.

BBFM Proposition 3.8 gives the denominator product, Proposition 3.9 gives
symmetry and unimodality, and Proposition 3.10 gives every dyadic
recurrence factor. Conjecture 4 is the exact original log-concavity
question. These results do not state the proposed higher dyadic-difference
inequalities. [Ballantine--Beck--Feigon--Maurischat, journal article](https://link.springer.com/article/10.1007/s11139-026-01419-0).

Chen--Ono--Zhang Conjecture 4 and Table 1 still list the ordinary-denominator
question as open; their binary-numerator correction concerns another
polynomial. [Chen--Ono--Zhang, v2](https://arxiv.org/html/2605.21718v2).

Fresh bounded searches included `"subsum" "Newton" "log-concavity"`,
`"Reciprocals of subsum polynomials" log-concavity denominator`,
`"log-concavity" "Newton coefficients" partitions`,
`"log-concavity" "subsum" denominator`, and
`"distinct partitions" polynomial "log-concavity" binomial`.
No equivalent kernel or resolution was identified in the primary sources
inspected. Other search hits about descent polynomials, different partition
statistics and generic Newton bases were not used as theorems. This is
bounded comparison, not exhaustive priority clearance. No claim of novelty
for Newton interpolation or generic binomial smoothing is accepted.

The conjecture meets the substantive screen: it has exact integer
quantifiers and a reproducible falsifier; its start is motivated by a
proved exponent identity and boundary obstruction; the supporting claims
have arguments and exact certificates; the frozen design/held-out split is
clear; independent falsification has extended the tests without changing
the statement; and its relation to the nearest prior results, plausible
use and unresolved parts are explicit.

The precise delta is a conjectured simultaneous sign structure for all
Newton coefficients of actual stage-minor margins. Its credible use is a
uniform certificate for affected stages in the affine region and a
systematic finite-certificate reduction for fixed edges. The high-order
band narrows the remaining search, while the boundary lemma explains a
real limitation of this method. This coherent combination warrants a
conjecture note; the arbitrary cutoff 96 alone is not the contribution.
K_sharp by itself is not a complete induction on a moving linear edge,
and it leaves the unbounded interior of the original problem untouched.

## Final disposition

All four submitted supporting claims pass at their frozen scope. I found
no substantive mathematical gap requiring a changed claim or new snapshot.
Acceptance authorizes the next workflow phase to present this conjecture
and its supporting mathematics with the above limitations. It does not
certify priority, journal acceptance, a proof of K_sharp_v1, or a resolution
of the original problem. The next phase should prepare only the frozen
conjecture-note scope; further research can test the larger-degree tuples
already specified in the dossier.
