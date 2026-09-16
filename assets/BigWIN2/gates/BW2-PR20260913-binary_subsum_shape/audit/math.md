# Independent mathematical referee report

Job: `primary-20260913-binary-subsum-shape-referee-be5abf08413f`.
Snapshot: `88b4434a3ac9397e2263ead6d4b67c7943824b36cc6ee739d7ca5394a90e2f80`.

**Verdict: accept the exact frozen result-note scope.** The original conjecture
remains unresolved. All three numbered assertions and the supporting kernel
lemma in `claim.json` pass; no assertion has been removed or weakened.

## Scope and integrity

The reviewed assertions are: strict boundary log-concavity uniformly for
`1 <= j <= floor((1-epsilon)*sqrt(log_2(n)/2))` at sufficiently large n for each
fixed epsilon in (0,1); strict inequalities at the first three positions for
every n>=6, with `T_j(N_n)>T_j(A_n)>0` when n is even; the exact finite
sufficient criterion using M_n; and `K3_m(l,t)>=0` for every integer m>=5 and
0<=l<=t<=m, with precisely the submitted formal-weight definition. Reflections
are included throughout where stated. This is the full frozen `result-note`,
with `original_status=unresolved`.

All 22 frozen file hashes and the canonical snapshot digest were independently
recomputed before and after verification, with no discrepancy. The immutable
source hash remains
`13e46a8af8569069d5eeadd7da3bb949452eccaa5e9472a43ebadec7f5231fdb`.
No frozen input was changed. The proposer and referee job IDs differ. This
report is the present fresh-context review, not a claim of statistical
independence or external peer review. No agents or additional model processes
were used. Owner confidence and historical audit conclusions were not used.

## Reconstruction of the growing range and finite criterion

Write b(n) for the number of binary partitions, avoiding confusion with the
recurrence summand B_n. Adding a one proves that b(n) is nondecreasing.
For a uniform binary partition of n, deletion of r parts equal to q gives

    mu_q = sum_(r>=1) b(n-rq)/b(n),   mu = mu_1,

with b(h)=0 for negative h. Grouping the sum for mu into its first q-1 terms
and the blocks rq,...,(r+1)q-1 proves `mu <= q-1+q*mu_q`. Every term in the
initial group is at most 1; every term in a block is at most its first term.
There is no probabilistic independence assumption.

The exact expected-weight identity `sum_(q=2^k) q*mu_q=n`, summed against these
bounds for k=0,...,K, gives

    mu <= (n+2^(K+1)-K-2)/(K+1).

Taking the prescribed minimum proves mu<=M_n. For L=log_2(n) and
K=floor(L-log_2(L)), n>=4 makes K admissible and the denominator positive.
The stated estimate

    M_n/n <= (1+2/L)/(L-log_2(L))

follows by 2^(K+1)<=2n/L and K+1>=L-log_2(L). Thus mu/n has the upper bound
`(1+o(1))/L`; an unproved asymptotic enumeration formula is unnecessary.

For each summand, the factor `(1+x)^(n-m_lambda(1))` supplies a coefficient
lower bound. The union bound for a j-subset of n labels gives

    c_(n,j) >= b(n)*binom(n,j)*(1-j*mu/n).

The union bound for j independent draws, excluding forbidden labels and
collisions, also gives

    c_(n,j) >= b(n)*n^j/j!*(1-delta),
    delta = j*mu/n+j(j-1)/(2n).

These inequalities remain valid when the right side is negative; squaring is
used only after positivity has been established. On the other side, increasing
each nonnegative exponent to n, then multiplying by further nonnegative
factors, proves coefficientwise domination by

    product_(k>=0)(1+x^(2^k))^n = (1-x)^(-n).

The binary-expansion identity is formal: only finitely many factors affect
each coefficient. No analytic product convergence or limit exchange is hidden
here. Consequently

    c_(n,j) <= b(n)*binom(n+j-1,j)
             <= b(n)*n^j/j!*exp(j(j-1)/(2n)).

For n>=2, 1<=j<=n, and an internal j, `j*M_n<n` ensures a positive lower
envelope. Squaring it and bounding the neighboring coefficients above gives
exactly assertion (3), including its strict comparison and binomial indices.

For assertion (1), put alpha=1-epsilon and
J_n=floor(alpha*sqrt(L/2)). Uniformly for 1<=j<=J_n,

    delta=o(1),  j*delta<=alpha^2/2+o(1),
    j*delta^2=o(1),  j*(j^2-j+1)/n=o(1).

In particular the lower envelope is positive, and the coefficient ratio is
bounded below by

    R_(n,j) = (j+1)/j * (1-delta)^2 * exp(-(j^2-j+1)/n).

The submitted elementary logarithm inequalities imply
`j*log(R_(n,j)) >= 1-1/(2j)-alpha^2-o(1)` with a uniform remainder. Choose
one fixed J with 1/(2J)<(1-alpha^2)/2. This proves positivity simultaneously
for J<=j<=J_n at sufficiently large n. The finitely many j<J are handled by
R_(n,j)->(j+1)/j>1. This is a uniform-in-j argument; it does not interchange
pointwise thresholds with a growing range. Since d(n)>=n-1, all these indices
are internal once n is large. Every summand is palindromic of the same degree,
so the reflected inequalities follow.

## Reconstruction of the first three positions

The recurrence separates partitions of 2m with no ones (halve their parts)
from partitions with at least two ones (delete two). Its carry factor has
x^2 coefficient 1, x^4 coefficient equal to the indicator that m is even,
and zero odd coefficients. Extracting coefficients and telescoping proves
equations (1) and (9) of `research-boundary-proof.md`, including the cubic and
quartic functionals. The identity
`[x]N_k = k*b(k)-sum_(h<k)b(h)` follows directly by deleting ones.
The constant, linear, and quadratic identities are correctly attributed to
prior work.

For j=1, expanding the Turan determinants gives equation (4). Chebyshev's
sum inequality gives 2R_1>=(m-1)R_0, while R_2<=(m-1)R_1. The remaining
quadratic expression is therefore nonnegative. The increasing polynomial
g_m(k) has average (4m^2-9m-4)/3, positive for every m>=3. With w>0 and
R_0>0 this proves strict compensation. The displayed positive formula for
T_1(A) then proves the full first-position assertion.

For j=2, decompose the nondecreasing weights as
`w_k=sum_(l<=k)e_l`, with e_0=1 and e_l=w_l-w_(l-1)>=0. Polarizing the
quadratic expression gives the exact kernel in equation (6), and hence (7).
The four submitted regions exhaust 0<=l<=t<=m. The certificate expansions
are nonnegative and K_m(0,0)>0 for m>=1. Together with equation (3), this
proves the second-position assertion, including its strictness.

For j=3, the same tail decomposition gives exactly the submitted equation
(10), with compensation `sum_(l,t)e_l*e_t*K3_m(l,t)`. The closed tail formulas
were reconstructed from the literal functionals: the quartic terms reverse
to sums of binom(2k,4)+z*binom(2k,2), 2h^2(m-2h+1), and 2h^2(m-h).
The even-index remainder is

    E_z = (q-(z-epsilon)/2)*(q-(z-epsilon)/2+1-epsilon),

where q=floor(m/2) and epsilon=z mod 2. This includes z=0 and z=m.
The halfway sums vanish on their inactive branch. Thus the submitted tail
expressions agree with the exact formal-weight definition; the certificate
has not silently replaced the intended kernel.

The LL, HH, LH1, and LH2 chamber inverses were checked algebraically. They
cover all integer 0<=l<=t<=m. In the mixed case the split at
t=q+l+delta gives the two indicated gap parameterizations. For delta=0,
the split u>=1 versus u=0,c>=1 covers the strict halfway condition.
After shifts and parity splitting there are 68 roots. The m>=5 constraint
becomes a sum threshold at most 2. Each leaf offset is at most 2, so clipping
coordinates at any integer at least 3 preserves membership in every leaf and
the sum constraint. This proves why a finite coverage check controls the
entire infinite integer domain.

The 144 verified identities therefore prove K3>=0 everywhere claimed.
The positive expansions of K3_m(0,0) for m=2z+5 and m=2z+6 give strict
compensation through e_0^2=1. The separate comparison term is also necessary:
with L=m*w-R_0>=0 and Q<=q2*w, expanding T_3(A) gives the lower bound

    alpha*w^2 + beta*w*L + (2m^2+m)*L^2.

The positive expansions of 9*alpha and 3*beta for m=2z+4 and m=2z+5
prove T_3(A)>0 for m>=4. The directly checked cases n=6 and n=8 give
1000>720>0 and 30520>21900>0, respectively. Thus every even n>=6 is covered.
Both A_(2m) and N_(2m) are palindromic of degree 2m+2d(m)=d(2m), giving the
reflected compensation inequalities. The prior equality N_(2m+1)=N_(2m)
then gives the claimed strict inequalities for odd n as well.

## Fresh exact verification and its logical scope

Run `python3 audit/referee_verify.py`. The script imports no submitted Python
module and writes only its audit report. Its completed output is
`audit/referee-verification.json`.

The certificate verification uses a different method from the submitted
SymPy/Fraction expansions. On each fixed parity/halfway chamber, the literal
tail expressions have total degrees at most 3,4,5 for p_2,p_3,p_4 and at most
2,3,4 for a_2,a_3,a_4. This follows from the reversed sums and the elementary
power-sum formulas, including the inactive-branch convention. Hence K3 has
total degree at most 8 after any affine leaf substitution. The verifier checks
that the proposed expansion has this degree bound too and compares it with
the literal defining sums at every nonnegative integer simplex point of total
degree at most 8 in the free variables.

This grid is unisolvent, so these are identity checks, not empirical positivity
tests. Indeed, for a degree-D polynomial, every multivariate finite difference
Delta^a P(0), |a|<=D, depends only on values at b<=a on this grid. Agreement
on the grid makes all coefficients in the product-binomial polynomial basis
agree. Fixed axes are removed from the grid. The same argument with degree 6
checks K2, and ordinary univariate interpolation checks the strictness arrays.

Actual completed checks:

- All 144 K3 identities, 12,325 nonnegative monomials, and 12,720 exact
  unisolvent evaluations; all leaf domain and parity constraints checked.
- All 68 parity roots covered, using 8,059 valid clipped vectors at height 4
  (a different clipping height from the submitted verifier).
- All four K2 identities, 105 nonnegative monomials, and 126 unisolvent
  evaluations.
- Six strictness/comparison polynomial identities and 42 univariate
  evaluations, with every displayed coefficient strictly positive.
- Mean bounds for 2<=n<=4096 and 45,069 grouped occupation inequalities,
  including the exact expected total weight.
- Direct summation over 8,348 binary partitions for every 2<=n<=48,
  independently matching coefficients through degree 13.
- A separately implemented truncated recurrence through n=256, matching
  the coefficient functionals and all three strict boundary comparisons;
  3,005 coefficient-envelope checks and 197 successful criterion applications.
- The eight serialized large-parameter criterion outputs were reproduced
  exactly, through n=2^1024. No coefficients of those huge polynomials were
  computed or inferred from a floating-point fit.

The low-n and truncated recurrence checks are calibration, not proofs of
infinite coefficient inequalities. Likewise, the retained full-coefficient
research run through n=512 is contextual finite evidence; this acceptance
does not promote its surviving all-index invariant to a theorem. The n=4,5
failure and the n=6 central equality are consistent with the frozen scope.

## Source comparison, contribution, and limitations

Primary sources were checked live across 2026-09-12–13 UTC (2026-09-13
Asia/Shanghai) and against the frozen PDFs. Fresh `pdftotext -layout`
extraction of both PDFs matched the
corresponding frozen text files byte for byte. The comparison details and
bounded search queries are in `audit/referee-sources.md`.

The nearest prior result is BBFM's structural analysis in Section 4: the
normalization, symmetry, degree and initial coefficient identities, followed
by the even-index recurrence. Those facts are dependencies here and must retain
their attribution. The accessed Chen–Ono–Zhang v2 confirms the corrected
remaining question and treats different, primarily algebraic assertions.

The precise additional result is an unbounded, explicitly quantified uniform
range of strict coefficient log-concavity, a count-free finite sufficient test,
and a uniform three-position comparison for every admissible n. The growing
range is not a direct restatement of finitely many prior coefficient formulas:
it needs control of the mean occupation and coefficient errors uniformly while
j grows. It addresses the original polynomial family without an arbitrary
restriction on the partition set. Its concrete use is to certify boundary
inequalities at parameters too large for coefficient enumeration and to
exclude those positions from any counterexample to the remaining conjecture.
The first-three-position result complements the asymptotic statement at small
n. These form one coherent partial note; the elementary mean lemma and the
individual boundary positions should not be split into separate contributions.

No equivalent was found in the accessed primary sources and bounded searches.
This is not an exhaustive priority certificate, nor is separate originality
claimed for general union bounds, power-sum identities, or elementary
occupation estimates. Within these explicit literature limits, the combined
scope passes the result-note contribution requirement.

No mathematical gap remains in the exact submitted scope. The central
coefficient range, optimal boundary constant, optimal finite threshold, and
the full original log-concavity conjecture remain unresolved here. Acceptance
does not certify a future manuscript, its citations, build, or presentation.
The next workflow step is one manuscript preserving this exact partial scope,
the prior attributions, and the distinction between finite calibration and
all-parameter certificates.
