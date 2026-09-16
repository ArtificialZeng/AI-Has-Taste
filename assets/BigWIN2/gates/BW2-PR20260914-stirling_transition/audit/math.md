# Fresh mathematical referee report

**Verdict: ACCEPT the exact frozen candidate.**

- Referee job: `primary-20260914-stirling-transition-referee-e0d57d510f15`.
- Review date: 2026-09-14.
- Snapshot: `b137208424a1f9968874146cbe4d73bed2aeb9258d7ef9df7b155c852e9275ca`.
- Frozen kind: `resolution-paper`; frozen original status: `proved`.
- Original source SHA-256: `4a37fe8a21f41aac0b72c9da83e28e1aff2ce19676fe24c5d93befb9e2d99594`.

The submitted argument proves the original all-k, all-n assertion and the
stronger statement in `claim.json`: for each integer k>=1, the stated finite
threshold N_k>=k+1 has a nonnegative prefix and a strictly negative tail.
The claimed weak second difference of q_k, including its strictness for k>=2,
also follows on the full stated domain. No narrower replacement claim is
being accepted.

This is a fresh model review, not human peer review or a claim of statistical
independence. I read the prescribed instructions, `source.md`, `problem.md`,
`claim.json`, the snapshot and its listed evidence; I inspected the relevant
actual primary statements in the two frozen HTML files and made the public
source checks described below. I did not read checkpoints, scheduling state,
earlier referee reports, job transcripts, or unlisted local research files.
No agents or additional model processes were used. All ten file hashes and
the canonical snapshot digest were independently recomputed successfully.
The frozen files, including `source.md`, were left unchanged.

## Reconstructed mathematical argument

### 1. Preservation of convex coefficient ratios

Write F_t(u,v)=u(1+t v)/(1+t u), with t>0. For 0<=u<=v,
w>=2v-u and h>=2u-v, monotonicity in the first argument of
F_t(w,v) follows from (1+t v)/(1+t w)^2>0. Monotonicity of
F_t(u,h) in h follows from t u/(1+t u)>=0. Thus the relevant
second difference is bounded below by

    F_t(2v-u,v)-2F_t(v,u)+F_t(u,2u-v)
      = 2t^2(v-u)^3 / [(1+t u)(1+t v)(1+t(2v-u))].

I checked this identity by independent exact polynomial expansion after
cross-multiplication. Every denominator here is positive. In particular,
2v-u>=v>=0. A negative comparison value 2u-v affects only a numerator,
so no positivity hypothesis has been silently used there. The limit
F_t(w,v)->v+1/t as w tends to positive infinity is an elementary rational
limit; no exchange of an infinite sum or limit is involved.

For coefficients a_0,...,a_m>0 set R_0=0 and R_j=a_(j-1)/a_j.
After multiplying by 1+t z, the ratios are

    S_j=F_t(R_j,R_(j-1)) (1<=j<=m),
    S_0=0,  S_(m+1)=R_m+1/t.

At center j use (h,u,v,w)=(R_(j-2),R_(j-1),R_j,R_(j+1)).
For interior centers, the hypotheses are precisely monotonicity and convexity
of the old ratios. At j=1 the extension R_(-1)=0 gives h>=-R_1.
At j=m the infinity endpoint gives exactly S_(m+1), not an additional
coefficient needing a positivity assumption. This also works when m=1,
where both endpoint treatments occur together.

The resulting S sequence is convex. Since S_1>0=S_0, all its increments
are strictly positive. This supplies the monotonicity hypothesis at the
next induction step; it is not circular. Starting with one factor proves
that R_j=e_(j-1)/e_j, R_0=0, is strictly increasing and discretely convex
for every finite product of positive factors (1+x_i z).

### 2. The cubic term and its boundary cases

Set A=e_r, B=e_(r-1), C=e_(r-2), E=e_(r-3), for 1<=r<=m,
with e_0=1 and negative-index coefficients zero. A and B are positive.
For H=B^2-A C and U=B^2 C-2A C^2+A B E:

- If r=1, H=1 and U=0.
- If r>=2, strict increase of the adjacent ratios gives H>0.
- If r=2, U=B^2-2A, and convexity at the first ratio center gives U>=0.
- If r>=3, A B C>0 and
  U/(A B C)=R_r-2R_(r-1)+R_(r-2)>=0.

The last division is not used when C=0. Scaling all four coefficients by a
common positive number preserves both sign conclusions. These observations
justify every use of H and U in the submitted proof, including k=2 and k=3.

### 3. Passage from row coefficients to convexity in n

Insertion of the largest element gives
c(n+1,k)=n c(n,k)+c(n,k-1), and hence the row polynomial is
z(z+1)...(z+n-1). For n>=k>=2, put r=k-1 and use the positive
weights 1,1/2,...,1/(n-1). The four coefficients (A,B,C,E) in
the proof are (n-1)! times those in the previous paragraph. Thus H>0,
U>=0 and B>0 throughout this domain.

Two recurrence steps give the denominators

    Q1=n A+B,
    Q2=n(n+1)A+(2n+1)B+C,

and the respective q numerators B, nB+C, and
n(n+1)B+(2n+1)C+E. Directly forming their second difference over
the positive denominator A Q1 Q2 gives a numerator P satisfying

    B P = B(n A+B)H + 2n H^2 + (B+n A)U.

This is the submitted positive decomposition with its division by B cleared.
The independent polynomial check verifies it identically, with no numerical
substitution. The first term is strictly positive and the others are
nonnegative. Therefore q_k(n)-2q_k(n+1)+q_k(n+2)>0 for every
n>=k>=2. For k=1, c(n,0)=0 and c(n,1)>0 for n>=1, so q_1=0
and the second difference is identically zero. The B=0 case is never
inserted into the divided decomposition.

This step is essential: convexity with respect to coefficient degree in a
fixed row is not simply identified with convexity in n while the weights
change. The recurrence and the positive decomposition supply that passage.

### 4. Finite threshold and signs on the entire domain

For fixed k>=1, put d_j=q_k(j)-q_k(j+1), j>=k. The established
second difference makes d_j nonincreasing. All q_k(j) are finite and
nonnegative. If every d_j were at least 1, telescoping would give
q_k(k+t)<=q_k(k)-t for every nonnegative integer t, a contradiction
for an integer t>q_k(k). Thus the set of integers j>=k with d_j<1
is nonempty and has a least element j_0. This proves the existence required
by the candidate's formula N_k=1+j_0 without an asymptotic assertion.

For n>=k+1 the positive denominator c(n-1,k)c(n,k) permits the exact identity

    D_k(n)/[c(n-1,k)c(n,k)] = d_(n-1)-1.

Minimality gives d_(n-1)>=1 for k+1<=n<N_k. Monotonicity gives
d_(n-1)<=d_(j_0)<1 for n>=N_k. Consequently the prefix is
nonnegative and the whole tail is strictly negative. Possible equalities
before the threshold are allowed; absence of equality in finite tests is
not used. The remaining indices satisfy D_k(n)=0 for 1<=n<k and
D_k(k)=1, while N_k>=k+1.

For k=1 the construction gives N_1=2. Independently,
D_1(n)=-(n-1)!(n-2)!<0 for n>=2, with D_1(1)=1. For the optional
k=0 boundary, D_0(n)=0 for n>=1, including n=1 where c(0,0)=1.
No denominator is used outside its positive support.

## Checks actually performed

The fresh standard-library verifier `audit/referee_verify.py` was written
for this review. It executes no proposer code. In particular, the submitted
verifier was read but not run, since it writes a frozen output and additionally
reads source copies outside the allowed evidence list. The new verifier's
results and input binding are saved in `audit/referee-checks.json`.

The exact checks passed:

- Integer sparse-polynomial verification of the preservation identity and
  the positive decomposition; both residual polynomials are zero.
- 576 rational preservation inputs and 576 infinity endpoint inputs,
  including 216 cases with an actually negative h, flat increments, u=0,
  and large or small positive t.
- All 791 positive-weight multisets of sizes 1 through 7 from
  {1/10000,1/3,1,7,10000}: strict increase and all 3,829 convexity centers.
- Counts from direct row-polynomial multiplication cross-checked against
  the permutation cycle-type formula n!/product(i^m_i m_i!) for every
  n=0,...,22, covering 4,508 cycle types.
- 72,000 exact D tests for 1<=k<=200 and 1<=n<=360, with the ratio identity
  checked on its positive support and all boundary signs checked.
- 52,100 exact q second differences for 1<=k<=200 and k<=n<=360.
  All 360 k=1 cases are equalities; every k>=2 case is strictly positive.
- The candidate threshold formula agrees with the first negative D for
  all 200 tested columns. The optional k=0 boundary was checked through 360.

These are reproducible error-detection checks, not the infinite proof. The
mathematical acceptance rests on the reconstructed argument above. The larger
triage counts mentioned in the frozen reduction were not independently
reproduced and are not needed for acceptance. All frozen hashes were checked
again after computation.

## Primary-source comparison and contribution

The frozen Liang--Sagan HTML contains Conjecture 8.9 with the same fixed-k
transition and the same permutation interpretation. Its Theorem 7.2 instead
concerns fixed columns of the second-kind numbers S(n,k). The live
[author-hosted published paper](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf),
printed p.31, labels the transition Conjecture 8.8. The current
[arXiv record](https://arxiv.org/abs/2408.02782), inspected on 2026-09-14,
lists v1 dated 5 August 2024. The different conjecture numbers are therefore
consistent and do not signify different mathematical targets.

I extracted the actual Theorems 1.4 and 1.5 from the frozen
[Salas primary text](https://arxiv.org/html/2607.04217v1). The first fixes n
and compares coefficient indices k and ell. The second compares products
of entire row-generating polynomials. Extracting coefficient x^(2k) from
such a product difference gives a sum over pairs i,2k-i. The term with i=k
is only one summand and does not isolate D_k(n). Thus these displayed
results do not give the submitted transition by direct specialization or
coefficient extraction. I do not assert that every possible indirect
deduction from that paper has been excluded.

The publisher-indexed primary abstract and section descriptions of
[Fan and Wang, Advances in Applied Mathematics 178 (2026), 103092](https://www.sciencedirect.com/science/article/pii/S0196885826000643)
report related elementary-symmetric ratio convexity and a proof of Briggs'
conjecture. Direct opening failed, and a bounded search did not yield an
accessible full text. The extracted publisher mathematics was incomplete.
I therefore do not claim to have checked their exact theorem or ruled out
a Stirling application in that paper. This is a literature-access limit,
not mathematical evidence for or against the candidate. The frozen candidate
explicitly disclaims novelty for the general ratio property, and none of
its proof steps relies on this inaccessible theorem.

The contribution under review is the complete fixed-column transition,
obtained by the row-to-column positive decomposition and finite-threshold
argument. Relative to the inspected Liang--Sagan source, this resolves the
stated all-k conjecture rather than just providing eventual convexity or a
finite table. It provides an exact criterion for the transition and rules
out every later contrary sign reversal. This is a coherent full-resolution
contribution, not an arbitrary small-parameter restriction.

Fresh public searches included the following queries and the close paper's
full title, with and without `filetype:pdf`:

- `"Stirling" "Liang" "Sagan" "conjecture" proof log-convexity`
- `"Stirling" "Conjecture 8.8" proof`
- `"Stirling" "Conjecture 8.9" log convex`
- `"Stirling numbers" "log-concave" "log-convex" "transition" proof`
- `"signless Stirling" "Liang" "proof"`
- `"Stirling" "Fan" "Wang" "convexity" 2026`
- `"Jia-Tao Fan" "symmetric" arxiv`

No equivalent fixed-column resolution was found in the primary sources
inspected during this bounded review. That observation supports the
candidate's deliberately bounded contribution description; it is not a
global priority certificate. In particular, the uninspected Fan--Wang full
text must not be described as having been ruled out. Its accessible synopsis
does not establish duplication, and the limitation does not invalidate the
self-contained full-scope proof or require a narrower mathematical claim.

## Decision and next action

There is no identified substantive mathematical gap and no required claim
revision. Scope, correctness, and the bounded contribution assessment pass.
**The exact frozen `resolution-paper` candidate is accepted with
`original_status=proved`.** This is not conditional acceptance of a weaker
statement. It neither certifies worldwide novelty nor authorizes release
of an unaudited manuscript.

The next action is the runner's structural `check-math` gate against this
unchanged snapshot, followed by manuscript preparation at the accepted scope.
The manuscript should retain the explicit attribution and literature limits
above, and must undergo the separate citation, build and visual release
checks. No manuscript, PDF, release manifest, provenance role file or
scheduling state was created or modified in this referee job.
