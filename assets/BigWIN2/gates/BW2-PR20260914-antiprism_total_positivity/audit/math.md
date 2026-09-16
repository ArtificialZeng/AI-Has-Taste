# Fresh mathematical referee report

Verdict: **accept the exact frozen result-note scope**.

Job: `primary-20260914-antiprism-total-positivity-referee-2ff96328895d`.
Date: 2026-09-14.
Snapshot: `fd3a6126f1cdaa284e6ddf47330455d28fc2279c1f2dcd4db37729e575ecb89a`.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

The uniform coefficient identity, its negative sign for every integer
k >= 76, the order-22 negative coefficient, and the positive coefficient
for every k >= 1 all pass. This acceptance does not prove or disprove
total nonnegativity of any untested antiprism matrix. It accepts the
specified obstruction to a project-generated coefficient assertion,
without changing the submitted statement or contribution.

## Inputs and review integrity

I read the frozen source, precise interpretation, claim, snapshot, listed
proof and hypothesis files, both listed arithmetic implementations, their
serialized certificates, the relevant passages of the three listed primary
sources, and the listed literature comparison. The large order-five and
order-six JSON tables were parsed in full; their positivity and selected
coefficients were examined computationally, as distinguished below from
independently reconstructing an entire table.

All 15 file hashes and the canonical snapshot digest were recomputed and
matched. The immutable source retains SHA-256
`9e95e6241ffc8f233a1c0b4bf2ac35126b98ace72434474ca22006c35c7f9615`.
No frozen input was edited. No previous audit, owner verdict, checkpoint,
state file, or earlier transcript was used. Assertions of confidence inside
the proof dossier were not treated as evidence. No subagent or additional
model process was used. The supplied research programs were inspected but
not run, since their main functions would overwrite frozen certificates.

The new calculation is `audit/referee_verify.py`, with exact outputs in
`audit/referee-verification.json`. It imports no project implementation.
`audit/referee-integrity.json` records the input-integrity check. These are
verification artifacts of this referee job, not additions to the frozen
claim or replacements for its evidence.

## Reconstruction of the decisive mathematics

### The definition and its connection to the original matrix

There is no change of auxiliary polynomial between the hypothesis and the
submitted theorem. In formal power series, putting E = exp(t(x+y)) gives

    exp(tx)/(1-(E-1)(c-1))
      = exp(-ty)/(1-(1-E^(-1))*c).

Its c^ell coefficient is exactly
`exp(-ty)*(1-exp(-t(x+y)))^ell`. Its t^r coefficient is the dossier's
T_(r,ell), and it vanishes for ell > r. Thus the earlier c-extraction
definition and the submitted T definition agree identically.

The generating identity for H follows directly from its frozen double
sum. Set p = i-s and q = r-i+s, so r = p+q. Summing the three binomial
factors against x^j y^n/(j!n!) gives

    (x^s/s!)*exp(y)*(x+y)^(p+q)/(p!q!).

The factor t^i is t^(p+s). Summing s and then using the two Stirling
exponential generating functions gives

    G = exp(tx+y)/
        (1-(exp(t(x+y))-1)*(exp(x+y)-1)).

Rewriting its denominator yields the finite-in-each-t-degree expansion

    [t^r]G = sum_(ell=0)^r T_(r,ell)(x,y)*exp(ell*x+(ell+1)*y).

For the positive column indices under review the ell = 0 term vanishes.
Extracting x^(j+s)y^(d-j-s) proves the submitted M-to-H identity, including
the factorial normalizations and the increasing column order. The actual
specialization is precisely

    a = j-k, n = d-j, z_1 = 2^n,
    z_ell = ell^a*(ell+1)^n-(ell-1)^a*ell^n  (ell >= 2).

For d >= j >= k these z variables are nonnegative and z_1 is positive.
Their partial sums telescope to ell^a*(ell+1)^n, as required. All series
manipulations are formal and locally finite; no limiting exchange is used.

### Extracting the next power of a at n = 0

Here is a reconstruction confined to n = 0, which suffices for every
coefficient in the frozen claim and avoids specializing inverses at a
possibly singular parameter value.

Define constant lower triangular matrices

    A_(r,ell) = [x^r]T_(r,ell)/ell^r,
    E_(r,ell) = r*A_(r,ell)
                - [x^(r-1)y]T_(r,ell)/(ell^(r-1)*(ell+1)),

and put F = A^(-1)E. The diagonal of A is ell^(-ell), so it is invertible
for every positive integer k. Set B = diag(ell^k*w_ell),
V_(ell,s) = (ell/(ell+1))^s, S = diag(1-k,...,0), and
D_(r,r) = kr-r(r-1)/2. Here w_ell = z_1+...+z_ell.

At n = 0 the coefficient of a^r in row r of M is the corresponding row
of U = ABV. Its coefficient of a^(r-1) is the row of

    N = DABV + EBVS.

Indeed, the q = 0 term uses the next coefficient of (a+k+s)_r,
namely r(k+s)-r(r-1)/2, and the q = 1 term uses (n-s)_1 = -s.
Terms with q >= 2 have a-degree at most r-2. Consequently no omitted
term can contribute to a^(K-1), where K = k(k+1)/2.

V is invertible because its nodes ell/(ell+1) are distinct. A Vandermonde
calculation, with exactly the submitted row and column orders, gives

    det V = prod_(p<q)(q-p) / prod_(ell=1)^k ell^(k-1),
    det U = lambda_k * prod_(ell=1)^k w_ell,
    lambda_k = prod_(r=1)^k r! / prod_(ell=1)^k ell^ell > 0.

By determinant multilinearity the desired next coefficient is
`det(U)*tr(U^(-1)N)`. Work first over the field of rational functions in
z. If W = V S V^(-1), the trace expression is

    sum_r (kr-r(r-1)/2)
      + sum_(ell<=i) F_(i,ell)*W_(ell,i)*(ell/i)^k*w_ell/w_i.

Multiplication by prod w clears every displayed denominator. This is a
polynomial identity, valid also when some w variables specialize to zero.
Lower triangularity of F is essential and is satisfied.

For completeness, rational interpolation in the basis q^(1-k),...,1
gives the cardinal functions (q_i/q)^(k-1)*L_i(q), where L_i is the
ordinary polynomial Lagrange basis at q_ell = ell/(ell+1).
Applying q*d/dq gives

    W_(ell,ell) = (ell+1)*
      (ell*(H_(ell-1)-H_(k-ell))-(k-1)),

    (ell/i)^k W_(ell,i) =
      (-1)^(i-ell+1)*ell*(ell+1)/(i-ell)
      *binom(k-ell,i-ell)/binom(i,i-ell)  (ell < i).

The latter follows by inserting
`q_ell-q_h=(ell-h)/((ell+1)*(h+1))` in L_i'(q_ell).
This checks the orientation and sign rather than presuming positivity of
an interpolation matrix. Also F_(ell,ell) = ell/(ell+1).
The diagonal part of the trace therefore reduces to

    sum_ell (ell*(3-ell)/2
             +ell^2*(H_(ell-1)-H_(k-ell)))
      = k(k+1)(2k+1)/6.

To check the last equality, the harmonic contribution is
`sum_(p<q)(q^2-p^2)/(q-p) = sum_(p<q)(p+q)`.

### The selected z monomials and the uniform formula

Write Z_(k,m) = z_1^m*z_(m+1)*...*z_k, with 1 <= m <= k.
Its coefficient in prod w is 1. Its coefficient in
`(prod w)*w_ell/w_i`, for ell < i, is 1 when i <= m and 0 otherwise.
To verify this, assign z_k to its only possible factor w_k, then z_(k-1)
to w_(k-1), and continue down to m+1. A missing w_i in this range makes
the assignment impossible. When no such factor is missing, all remaining
factors must supply z_1. There is no extra factorial or multiplicity.

It follows for every integer 1 <= m <= k that

    [a^(K-1) n^0 Z_(k,m)]R_k / lambda_k
      = k(k+1)(2k+1)/6
        + sum_(1<=ell<i<=m)
          (-1)^(i-ell+1)*ell*(ell+1)/(i-ell)
          *binom(k-ell,i-ell)/binom(i,i-ell)*F_(i,ell).

The first m rows of F are independent of k once k >= m, because the
matrices defining it are lower triangular. The m = 1 sum is empty, proving
the positive-coefficient assertion for every k >= 1. In particular k = 1
gives R_1 = z_1*(a+1+n/2), which verifies the boundary case directly.

Direct binomial exponential expansion gives

    [x^p y^(r-p)]T_(r,ell)
      = (-1)^r/(p!*(r-p)!)
        *sum_(h=0)^ell (-1)^h*binom(ell,h)*h^p*(h+1)^(r-p).

Using these entries and exact matrix inversion, the fresh verifier
reconstructed all 15 entries in the dossier's five-row F table. They
agree. Substituting this table into the preceding expression with m = 5
and expanding the binomial polynomials proves the entire identity

    [a^(K-1) n^0 Z_(k,5)]R_k
      = -lambda_k*(125k^4-9555k^3+17736k^2-346478k+858264)/20736

for all integer k >= 5. This is a symbolic polynomial identity, not a
fit to a finite range. Independently, its degree is at most four: the
diagonal part is cubic and every off-diagonal binomial has degree
i-ell <= 4. Five direct determinant evaluations determine that polynomial
and gave the same result, with k = 10 reserved for an extra check.

For Q(k) equal to the displayed quartic numerator, exact expansion gives

    Q(76+t) = 125t^4+28445t^3+2171196t^2+56268354t+52825392.

Every coefficient, including the constant term, is positive. Hence Q(k)
is positive for every real k >= 76. Since lambda_k > 0, the claimed
coefficient is negative for every integer k >= 76. At k = 5 the final
z product is empty; no exceptional interpretation is needed.

## Fresh arithmetic verification of the finite witness

For Z_(k,m), row support ell <= r forces row k to supply z_k, row k-1
to supply z_(k-1), and so on through row m+1. In those rows only ell = r
is retained; the first m rows retain all ell <= r and supply z_1. Taking
the determinant of these row coefficient vectors is exactly the selected
z coefficient of R_k. This argument holds term by term in the determinant
and does not assume its sign.

The fresh verifier derives the leading and next row coefficients from
the binomial formula for T above, then eliminates the resulting matrix
over Q[epsilon]/(epsilon^2). It computes det(L+epsilon*N) in one elimination.
This is separate from both the producer's trace-family calculation and
the submitted verifier's sum of integer Bareiss row replacements. All
pivots and divisions are exact rationals; the leading matrix is checked
to be nonsingular and its determinant is checked against lambda_k.

For k = 22, m = 9, it obtains exactly

    [a^252 n^0 z_1^9 z_10*...*z_22]R_22 / lambda_22
      = -4429926944297146258237/14051921264640000000 < 0.

The full rational coefficient and its leading normalization are serialized
in `audit/referee-verification.json`. The executable input is the defining
matrix formula together with the recorded exact integers k and m; no
floating-point data or external numerical service is involved. This
establishes the finite witness at its precise stated monomial.

Other checks actually performed were:

- 827 exact M-to-H entry comparisons: 1 <= d <= 8,
  1 <= k <= min(d,5), every k <= j <= d, every required row and column.
- Direct Vandermonde differentiation matrices through k = 8, checking
  all diagonal entries and 84 off-diagonal entries against the formulas.
- Complete selected-z determinant polynomials in a at n = 0 for every
  1 <= m <= k <= 4, checked against the two-coefficient calculation.
- Direct dual-number calculations for (k,m) = (5,5), (6,5), (7,5),
  (8,5), (9,5), (10,5), (6,3), (6,6), (22,9), (25,7), and (22,1).
  The last case gives the positive normalized value 3795.
- The three named order-five/six coefficients match both supplied JSON
  tables and the new direct calculation. All 5,712 and 33,396 listed
  coefficients in those two files are positive; I did not independently
  reconstruct their entire multivariate determinant expansions. Those
  prior full expansions are not a premise of the accepted all-k proof.
- The five submitted Bareiss certificates are internally arithmetically
  consistent: their row-replacement numerators sum to the reported
  rational coefficients after division by their common denominators.

These finite checks support, and do not replace, the all-k derivation.
They make no assertion that order 22 is the first negative order among
all coefficients. The order-25 example is an additional consistency check,
not an enlargement of the frozen claim.

Reproduction from the project root:

    python3 audit/referee_verify.py

This writes only its own audit verification JSON. It requires Python and
SymPy; this run used SymPy 1.14.0. No proof-assistant formalization was used.

## Primary-source comparison and contribution assessment

The nearest published mathematical input is the antiprism transformation,
not a conjecture about these independent slack coefficients.

I inspected [Liu--Mao, arXiv:2607.01577v1](https://arxiv.org/pdf/2607.01577v1),
printed page 19, Remark 5.8, in the frozen PDF. Its formula matches the
source matrix. The paper raises the antiprism question and proves TN for
other subdivision families; its general interlacing criterion yields only
order-two nonnegativity. The [current arXiv record](https://arxiv.org/abs/2607.01577)
lists v1, July 2, 2026. None of these results is contradicted here.

I inspected [Athanasiadis--Brunink--Juhnke-Kubitzke,
arXiv:2006.10789v2](https://arxiv.org/pdf/2006.10789v2), printed pages 19--23,
especially Proposition 5.7(b), equations (19)--(21), and Propositions
5.11--5.12. These provide the stated Stirling and transformation
normalizations. The [current arXiv record](https://arxiv.org/abs/2006.10789)
lists v2, September 5, 2021. Its established antiprism results do not
include the auxiliary coefficient formula under review.

The frozen [Mu--Welker HTML](https://arxiv.org/html/2404.03500v2), in the
paragraph before Section 3, describes small-dimensional antiprism TN as
experimental evidence. It does not assert the all-dimensional conclusion.
The [current arXiv record](https://arxiv.org/abs/2404.03500) lists v2,
November 4, 2024. The note does not claim those earlier positive experiments
as new or attribute its internal hypothesis to these authors.

On the review date I also made bounded live searches for:

- `"antiprism" "coefficient positivity" determinant`
- `"antiprism" "total nonnegativity"`
- `"antiprism" "total positivity" "flag"`
- `"antiprism" "total positivity"` restricted to arxiv.org
- `"antiprism" "coefficient" "determinant"` restricted to arxiv.org
- `"antiprism" "Neville"`
- `"125" "9555" "346478"`

No equivalent primary coefficient theorem was identified in these searches
or the inspected primary passages. Searches also returned mirrors,
generated summaries, and irrelevant geometric and chemical uses of
antiprism; none was used as authority. This is a bounded comparison,
not an exhaustive priority certificate or a worldwide open-status claim.
Terminology-equivalent constructions could escape these searches.

The precise delta is a uniform sign obstruction in the next-highest
component of a fixed determinant directly specializing to antiprism
initial flags, together with a separately verified finite witness.
It is not a routine restatement of the known transformation or a new
positive finite table. The proof requires the row-degree extraction,
interpolation weights, selected-monomial analysis, and a nontrivial exact
cancellation giving the quartic. Nor is the restricted family an arbitrary
toy problem: a, n, and the partial-sum variables arise from the actual flag
parameters, and the all-coefficient assertion is the explicitly frozen
certificate strategy being tested.

A credible use is to rule out an all-order proof consisting of certifying
nonnegative monomial coefficients of this unchanged R_k. Any continuation
of that approach must use relations present at the actual parameter
specialization or change the certificate. This is a modest but substantive
result-note contribution under the supplied standard. It should remain
one coherent note; the uniform formula and order-22 witness should not be
split into separate contributions.

## Gaps, limits, and decision

No mathematical gap requiring revision was found in the frozen subsidiary
theorem. The accepted scope includes all its stated quantifiers and both
sign conclusions. Negative formal coefficients do not give negative
values at the actual specialization and do not refute TN of H_d. No claim
about all alternative parametrizations, planar networks, general Neville
methods, or a minimal negative order is accepted or made by this report.
The original all-minors, all-dimensions matrix question remains unresolved.

Correctness, scope, and the limited contribution all pass. The decision is
**accept**, with `kind = result-note` and `original_status = unresolved`
unchanged. No substantive claim revision or new snapshot is needed.
The next workflow test is the runner's provenance/integrity gate before
writing a manuscript confined to this scope. This report is a fresh model
review pass, not external peer review or a promise of journal acceptance.
