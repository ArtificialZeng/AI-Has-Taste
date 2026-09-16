# Precise original and proposed resolution

Immutable original: source.md. Research job:
primary-20260913-qdescent-logconcavity-research-8293ab93d85b.
Proposed outcome: resolution-paper candidate, original proved at the proposed
scope, awaiting a fresh referee. No mathematical acceptance or release exists.
Source/literature status remains uncertain; no priority/current-open claim.

## Frozen definitions and scope

Let q be an indeterminate. For every finite nonempty subset S of the positive
integers put m=max S. For a permutation pi of [n], define

    Des(pi)={h:1<=h<n and pi_h>pi_(h+1)},
    inv(pi)=#{(h,l):1<=h<l<=n and pi_h>pi_l}.

For 1<=k<=m, a_k(S;q) is the sum of q^inv(pi) over pi in Sym(m+k)
with Des(pi)=S and {m+1,...,m+k} contained in {pi_1,...,pi_m}.
Set a_0=a_(m+1)=0. Write f>=_q g if f-g has nonnegative coefficients.
The literal frozen original requires no internal zero polynomials and

    a_i(S;q)a_j(S;q)>=_q a_(i-1)(S;q)a_(j+1)(S;q)

for every such S and all 1<=i<j<=m. No internal zeros means that if
r<s<t and a_r,a_t are nonzero then a_s is nonzero. The boundary pairs
have zero right-hand side. The literal source prints i<j, while its nearby
discussion includes diagonal i=j cases. That discrepancy remains explicit.
A diagonal-only failure would not disprove this literal original.

The proposed proof establishes every a_k nonzero and all 1<=i<=j<=m.
Thus it includes the original plus a separately disclosed diagonal
strengthening; it neither corrects nor weakens source.md. S empty is excluded.

## Stronger intermediate statement and exact payoff

Let G(n,k)=[n choose k]_q, zero unless 0<=k<=n, and define

    K(m;k,r)=q^(k^2)(G(m,k)-G(m-r,k)),   1<=k,r<=m,
    K(m;0,r)=K(m;m+1,r)=0.

The candidate proves, for all integers m>=1, 1<=i<=j<=m, and independently
1<=r,s<=m, the directed inequality

    K(m;i,r)K(m;j,s)-K(m;i-1,r)K(m;j+1,s)>=_q 0.       (D)

This strengthens the single and symmetrized mixed inequalities in the
unchanged frozen Target K, evidence/intake/triage-kernel-reduction.md.
For T=S without m, let x_r be the inversion enumerator of sigma in Sym(m)
with Des(sigma)=T and sigma_m=r. The candidate directly reconstructs each
original pi from its standardized prefix sigma and increasing final subset U
of [m]. The final descent is exactly min U<=r, and its cross inversions are
mk-sum(U)+k(k+1)/2. Therefore a_k=sum_r K(m;k,r)x_r. Summing (D) against
the nonnegative x_r*x_s proves the original and diagonal statements.

The proof reverses K to

    H(m;k,r)=G(m,k)-q^(kr)G(m-r,k)
            =sum_(U subset [m], |U|=k, min U<=r) q^(sum(U)-k(k+1)/2).

A transfer from subset sizes (i-1,j+1) to (i,j), with delta=j-i+1, reduces
the total element sum by delta, weakly decreases the first minimum, and
preserves the second minimum. Protecting min B before a shifted-set
last-maximum construction makes the cutoffs survive. A first-maximum rule
recovers the input exactly. This is a complete written argument, with no
known mathematical gap in this research pass, submitted for fresh review.

Decisive argument: evidence/research/protected-minimum-proof.md.
Exact reproducible checks: evidence/research/protected-minimum-check.py and
.json. They cover 346,335 transfers through m=10, 650 kernel identities and
27,313 strict plus 6,084 diagonal directed inequalities through m=12, and
49 original a-definition cases for all max S<=4. Computation is finite
verification, not the proof or an independent mathematical audit.

## Primary comparison and limitations

Gaetz--Gao v2, Sections 1.2/2, Theorems 5/6 and Conjecture 7, defines the
original a coefficients and proves the related b statement. Its arbitrary-b
counterexample is prior work and is not a candidate contribution. The full
local primary input is evidence/external/gaetz-gao-1912.04933v2.html.
Bencs's ordinary q=1 result is known (Proposition 4.3 and Corollary 4.4 of
arXiv:1806.00689v2); the inspected primary excerpt is preserved in
 evidence/external/bencs-1806.00689v2-section4.web.txt.

The closest method is Krattenthaler's shifted-set injection, Section 2 of
On the q-log-concavity of Gaussian binomial coefficients (1989). Its primary
PDF text is saved without transcription as
 evidence/external/krattenthaler-q-log-1989.web.txt. The candidate explicitly
attributes this method and proves the protected-minimum modification.
This tool-extracted text has OCR limitations and is not a PDF byte copy.

The bounded current comparison is in literature/research-pass-1-screen.md.
Liu--Xiao full-text access remains incomplete; its indexed section snippets
mention strong q-log-concavity, so no inapplicability or priority conclusion
is drawn from its numerical abstract. General Liang--Sagan and
Gutierrez--Krattenthaler methods were inspected only at the stated passages.
No equivalent was found in those inspected statements; this is not global
novelty certification. Outer registry/Excel payloads and full conversation
history remain unavailable for independent deduplication.

One next test: a fresh referee should verify (D) by checking the protected
minimum, last/first-maximum inverse and reversal, then independently verify
the suffix reconstruction and original quantifiers. Only the runner may
freeze and schedule that review; this candidate creates no manuscript.
