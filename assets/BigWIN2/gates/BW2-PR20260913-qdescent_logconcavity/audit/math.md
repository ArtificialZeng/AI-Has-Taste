# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Job: `primary-20260913-qdescent-logconcavity-referee-4070c25402ef`.
Snapshot: `9ae9add72fc8f4054cff292c5f61239af227e330f2412ceb2363069cdd3253eb`.
Review completed on 2026-09-14, Asia/Shanghai (2026-09-13 UTC).
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The argument proves the original statement at its full frozen scope, the
explicit additional diagonal inequalities, and the directed kernel inequality
for independently ordered cutoffs. No substantive correction or scope change
is required. This is a fresh mathematical review pass, not a claim of
statistically independent evidence or external journal peer review.

## Inputs and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and each
listed evidence file. The primary HTML was read using its mathematical alt
text; the three frozen primary text excerpts were read completely. The
Krattenthaler, Bencs, and Liang--Sagan excerpts were reread after a combined
tool output was truncated. The selected skill, referee reference, and release
contract were each read in a separate complete tool result. I did not consult
checkpoint/state files, earlier job transcripts, or earlier audit verdicts.
Assertions of confidence in the mandatory frozen inputs played no evidentiary
role. No child agent or additional model process was used.

Independent SHA-256 recomputation matches all 12 files in the snapshot and its
canonical mapping digest, both before and after the fresh computation. The
source remains byte-identical, with SHA-256
`09b28e35bf37a42405472803e963d8cd37dce27edee55c075e7689eab2781fcb`.
No frozen input was edited. The candidate's verification script was inspected
but not executed, since its main function overwrites a frozen evidence file.
The fresh implementation and actual results are `audit/referee-check.py` and
`audit/referee-check.json`.

## Scope checked

For every finite nonempty set S of positive integers, m=max S, and 1<=k<=m,
a_k is precisely the inversion enumerator of permutations of [m+k] with
descent set S and all values m+1,...,m+k in their first m positions.
The zero conventions a_0=a_(m+1)=0 are retained. The accepted conclusion is
that every a_k in this range is nonzero and

    a_i a_j - a_(i-1) a_(j+1) is in Z_>=0[q],  1<=i<=j<=m.

The literal source prints i<j. Its nearby discussion includes diagonal
inequalities. The candidate explicitly separates these readings: it proves
the literal original and also i=j. Acceptance does not reinterpret the
source, and does not depend on a diagonal counterexample or a wording defect.

The further frozen conclusion is also accepted, without symmetrizing or
restricting r,s:

    K(m;i,r) K(m;j,s) - K(m;i-1,r) K(m;j+1,s) >=_q 0

for all m>=1, 1<=i<=j<=m, and every ordered pair 1<=r,s<=m, where

    K(m;k,r) = q^(k^2) ([m choose k]_q - [m-r choose k]_q)

on the stated natural range, and its two boundary values are zero.

## Reconstruction of the decisive proof

For a k-subset U of [m], set w_k(U)=sum(U)-k(k+1)/2. This integer lies
between 0 and k(m-k). The sum H(m;k,r) of q^w_k(U) over subsets with
min U<=r equals

    [m choose k]_q - q^(kr) [m-r choose k]_q.

Indeed the excluded subsets are translations by r of subsets of [m-r].
Reflection of subsets gives Gaussian reciprocity. Substitution gives
q^(mk) H(m;k,r)(q^-1)=K(m;k,r), including cases k>m-r by the zero
convention. The normalization is correct: both resulting terms have the
factor q^(k^2). The subset [k] is the unique term of weight zero, so every
interior H has constant coefficient 1, and every interior K has coefficient
1 in degree mk.

Consider 1<=i<=j<m, delta=j-i+1, |A|=i-1, |B|=j+1. Protect b=min B,
let B0=B\{b}, and shift A by delta. On the integer interval
[delta,m+delta], put

    f(t)=|(A+delta) intersect [t]|-|B0 intersect [t]|.

The critical lower bound is valid even at equality: B0 contains no 1,
so f(delta)>=-(delta-1)>-delta. For every t>=m in this interval, B0 is
fully counted and at most i-1 shifted A elements have been counted; hence
f(t)<=i-1-j=-delta. Consequently the last position L attaining the maximum
M of f satisfies L<m. The next integer e=L+1 lies in (delta,m]. Since
one-step increments of f belong to {-1,0,1}, and f cannot retain its
maximum at e, we have f(e)=M-1 and e in B0\(A+delta).

It follows that C=A union {e-delta}, D=B\{e} are valid subsets of [m]
of sizes i and j. No element of A is removed, the inserted element is new,
and the protected element of B remains. Thus min C<=min A when A is
nonempty, min D=min B, and the combined element sum decreases by delta.
Intersections between A and B, or between C and D, are allowed and cause
no problem; disjointness is never assumed.

The inverse is genuinely determined by the output. From C,D recover
b=min D and form

    g(t)=|(C+delta) intersect [t]|-|(D\{b}) intersect [t]|.

For an image pair, g(t)=f(t)+2*1_(t>=e). Before e, its value is at most
M. At e it equals M+1; thereafter it is at most M+1, because L was the
last maximum of the integer-valued f. Thus e is the first global maximum
of g on the stated interval. Removing e-delta from C and reinserting e
into D recovers A,B. A left inverse on the image suffices: surjectivity
onto the whole target product is neither asserted nor needed.

The difference between input and output normalization constants is exactly
delta. The decrease of the element sum therefore makes this injection
weight preserving for the two H factors. Since the first minimum weakly
decreases and the second is unchanged, the injection restricts to both
cutoffs independently; no assumption r<=s is used. Its image complement
enumerates the coefficients of the directed H difference. For i=1 or j=m,
the subtracted product is zero by convention, so these cases require no
minimum of an empty set. This also treats m=1 and every diagonal.

Coefficient reversal by q^(m(i+j)) sends the H difference to precisely
the directed K difference. Both products have the same reversal bound,
and all H exponents lie below it. No negative exponent or sign change is
introduced. This establishes the complete frozen directed assertion.

For the reduction to the original definition, let T=S\{m}, and let x_r
count permutations sigma of [m] with Des(sigma)=T and sigma_m=r, by
inversions. A counted original permutation has an increasing suffix U of
size k contained in [m]. Its prefix consists of the complement of U in
[m+k], whose standardization is sigma. Exactly min(U)-1 prefix values
are below min(U); hence the final descent is equivalent to r>=min(U).
This proves both directions and uniqueness of the proposed reconstruction.
For U={u_1<...<u_k}, the number of prefix entries exceeding u_t is
m-u_t+t. The cross inversions total

    mk-sum(U)+k(k+1)/2 = mk-w_k(U).

Prefix inversions equal inv(sigma), and suffix inversions vanish. Therefore
a_k=sum_r x_r K(m;k,r). The same identity holds at the two zero boundaries.
Expanding the desired determinant and summing the directed K inequalities
against the nonnegative polynomials x_r x_s is legitimate in Z[q].

Finally, every T subset [m-1] occurs as a descent set: reverse each block
of consecutive positions joined by edges of T, assigning consecutive value
intervals in increasing block order. There are descents exactly at the
edges of T. Some x_r is consequently nonzero; U=[k] is allowed for that
r for every k. This establishes every asserted nonzero a_k, and thus the
no-internal-zero requirement.

The proof uses finite sets and polynomial identities throughout. There is
no division by a potentially zero polynomial, limiting exchange, or hidden
uniformity assumption. No equality classification is part of the frozen
claim; none is inferred from the checks.

## Independent exact checks actually completed

Running `python3 audit/referee-check.py` completed successfully. It imports
no candidate arithmetic or transfer code.

- Exhaustive bit-mask transfer enumeration for all 1<=i<=j<m<=11 checked
  1,444,125 inputs, including 1,097,790 at m=11 beyond the candidate's
  reported transfer range. It checked ground set, sizes, normalization,
  both minima, the left inverse, and absence of collisions.
- Direct subset enumeration checked 1,496 pairs of H/K identities and
  support assertions for all 1<=k,r<=m<=16. For each of H and K it checked
  112,676 strict and 18,496 diagonal directed inequalities, including every
  ordered pair of cutoffs and both zero boundaries.
- These larger polynomial checks use exact base packing, not a sign test
  at one positive value of q. Each factor counts at most 2^m subsets, so
  every product coefficient is at most 4^m. Base 2^(2m+4) with half-base
  guard digits prevents every carry and borrow in the signed difference;
  the guard bits test each coefficient separately. Ordinary coefficient
  convolution independently crosschecked all 2,730 H inequalities through
  m=7. Explicit negative-polynomial control cases were also checked.
- Direct enumeration of 4,084,856 permutations, without presupposing an
  increasing suffix in the enumeration, verified all 129 coefficient
  identities for every nonempty S with max S<=5 and every k in range.
  The cross-inversion kernel was computed by counting actual cross pairs.
  The original polynomials independently passed 222 strict and 129
  diagonal inequalities and all nonzero assertions in this range.

The overlapping checks agree with the candidate's finite observations.
The larger ranges are additional finite corroboration only. Acceptance
rests on the uniform argument reconstructed above, not on these counts.

## Source comparison and contribution

[Gaetz--Gao, v2](https://arxiv.org/html/1912.04933v2), Sections 1.2 and 2,
was compared directly with the immutable HTML, including Theorems 5 and 6,
Conjecture 7, and the following Remark. The definition in Theorem 5 matches
the frozen original. Their proved b-coefficient result is distinct from
the conjectured a-coefficient result. The Remark's arbitrary-b
counterexample remains prior work; the candidate does not claim a general
arbitrary-b preservation theorem. The current indexed publisher excerpt
also retains Conjecture 7. This observation does not establish present
global openness.

The nearest method is [Krattenthaler (1989), Section 2](https://www.mat.univie.ac.at/~kratt/artikel/q-log.pdf):
the shifted-set transfer, last maximum in the forward map, and first
maximum in its inverse are prior work. The frozen seven-page primary text
was inspected, with its disclosed OCR limitations. The substantive
modification is to remove and protect the larger subset's minimum before
computing prefix differences. In the displayed test A={2}, B={2,3,4},
m=4, i=j=2, the classical map gives C={1,2}, D={3,4} and loses a cutoff
at 2. The protected map gives C=D={2,3}, as independently checked from
the prefix counts. Thus preservation of the minimum is an actual additional
property, not an attribution of the classical construction as new.

[Bencs, Proposition 4.3 and Corollary 4.4](https://arxiv.org/html/1806.00689v2)
were inspected in the frozen primary excerpt. They supply the ordinary
coefficient log-concavity result at q=1 and the translated-polynomial
identity used there. This prior theorem is properly attributed. It is not
a proof of the coefficientwise q inequalities submitted here.

For [Liang--Sagan (2026)](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf),
I inspected the frozen q-order-ideal excerpt and the live statements and
proof of Theorem 6.6, with the adjacent peak evaluation theorem. The latter
results concern sequences indexed by permutation length, whereas this
candidate concerns expansion coefficients indexed by k. Lemma 8.10 is a
potential broader method, but neither the frozen argument nor this review
identifies the present cutoff families with its hypotheses. No general
inapplicability conclusion is justified.

I also checked the displayed Theorem A, Corollaries A.1/A.2, and the
ordinary-q versus quantum comparison in
[Gutierrez--Krattenthaler](https://www.mat.univie.ac.at/~kratt/artikel/GK.pdf).
These statements concern Schur and quantum-binomial sequences; I did not
establish a specialization giving the submitted directed cutoff result.
This was a statement comparison, not a full review of that paper's proof.

The [Liu--Xiao publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X2600107X)
was searched again. Its indexed section snippets do mention strong
q-log-concavity. Direct full-text access failed, so the relevance of its
uninspected lemmas remains undetermined. Its numerical abstract is not
evidence that its full results are inapplicable.

Fresh bounded queries included the original title with "proof" and
"Conjecture", "Gaetz" "Gao" "Conjecture 7" log concavity proof, and
the Liu--Xiao title with "strong". No exact prior resolution was identified
in the primary statements actually inspected. This is bounded comparison,
not a priority certificate; unavailable later sources remain an explicit
limit of the accepted contribution language.

The contribution passes at its frozen scope: a self-contained proof of the
source-defined conjecture, with a directed refinement that works for arbitrary
nonnegative polynomial mixtures of the cutoff kernels. The modification
over the classical injection has a precise, useful payoff: it preserves
the two independent cutoff conditions needed for that refinement and the
original permutation problem. This is neither a toy restriction nor a
repackaging of the known arbitrary-b counterexample. Global priority and
the claim to be a first proof are not accepted or asserted.

## Disposition

There is no unresolved mathematical gap in the submitted scope. Accept
the frozen `resolution-paper` / `proved` candidate in full. The accepted
scope includes all diagonal and directed inequalities; no weaker substitute
was reviewed in their place.

Next step: the runner may perform its mathematical integrity gate and
dispatch writing of the accepted scope. Subsequent writing must retain the
source-index discrepancy, explicit classical attribution, and bounded
later-literature language. Citation, build, visual, and publication checks
remain separate later phases. This referee job created no manuscript or PDF
and performed no publication action.
