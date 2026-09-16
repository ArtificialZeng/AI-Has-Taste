# Precise problem and triage scope

Frozen input: `source.md`, SHA-256
`599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8`.
The original file is retained verbatim; the reading below does not replace it.

For every integer n >= 1 and real parameter t, define a_j=(j+t)^n for integers
j >= 0 and a_j=0 for j<0. Let T=(a_(j-i))_(i,j>=0). Here TP means that for every
integer r>=1, every increasing nonnegative row tuple i_1<...<i_r and column
tuple j_1<...<j_r, det(a_(j_v-i_u))_(u,v=1,...,r) >= 0. It is total
nonnegativity, with zero minors allowed. Set M_n={t in R:T is TP}.

The target is the single conjunction: there exists a sequence of real numbers
(c_(2k))_(k>=1) such that for every positive integer k,
M_(2k)=[-c_(2k),1+c_(2k)], 0<c_(2k)<2, and c_(2k)<=c_(2k+2).
Every interval is closed. Thus connectedness, absence of other components,
endpoint membership, and nesting are all required. A possible limit is contextual
and is not part of the frozen target. The all-a Pochhammer variant and its
multiplication problem are distinct. A finite-degree classification cannot
settle the target without a counterexample to one of its quantified assertions.

Let L(binomial(x,j))=z^j and
Q_(n,t)(z)=sum_(j=0)^n z^j sum_(l=0)^j (-1)^l binomial(j,l)(j-l+t)^n.
Its degree is exactly n and leading coefficient is n!. For these monic input
polynomials, t in M_n iff all n zeros of Q_(n,t), with multiplicity, belong to
[-1,0]. The generating numerator is
S_(n,t)(x)=(1-x)^n Q_(n,t)(x/(1-x)); this is the Euler--Frobenius polynomial
P_(n,rho)(x) in Janson's notation with rho=t. A zero of Q at -1 corresponds
to a drop in the numerator's degree, not a finite numerator zero.

## Source status and nearest results

Status: open-supported in the inspected primary sources, without a global
novelty or priority claim. Vishnyakova, arXiv:2607.06207v1, Example 5.7 and
Conjecture 5.8, states this exact even-degree question. Its current arXiv record
lists only v1 (checked 2026-09-14 Asia/Shanghai). Formulae (3)--(8) give the
transform; Statement 2.1 gives reflection t -> 1-t. Example 5.3 already gives
M_2=[(1-sqrt(2))/2,(1+sqrt(2))/2]. Theorem C (Wagner) gives polynomial
multiplication closure, hence M_2 subset M_(2k); this corollary is not new.
Janson, arXiv:1305.3512, (1.1)--(1.2), identifies the Euler--Frobenius coordinates;
its standard parameter range must not be silently extended beyond [0,1].
URLs and inspected positions are recorded in `literature/triage-screen.md`.

## Proposed contribution and verification route

Nearest prior result: known [0,1] real-rootedness, reflection and multiplication
closure. Proposed delta: a uniform mechanism excluding additional admissible
components or proving successive even-degree nesting for exterior shifts.
Verification route: exact discriminant/Sturm calibration in degree four,
followed by the parameter and degree recurrences at a possible double root.
A routine quartic formula alone has insufficient demonstrated novelty/value for
a manuscript. No candidate or mathematical acceptance is asserted at triage.

## Research pass 1: explicit auxiliary target

The frozen conjunction above is unchanged. The sextic collision test is now
complete: `evidence/sextic-collision.md` and its exact Python/JSON certificate
prove M6=[alpha,1-alpha], -0.255<alpha<-0.254, with one exterior double
collision and strictly positive splitting coefficient.

The next auxiliary hypothesis O states: for every odd m>=1 and -b<t<0,
b=1-1/sqrt(2), Q_(m,t) has m-1 simple zeros in (-1,0) and one simple
positive zero. This is not TP for odd degrees. The argument in
`evidence/odd-strip-reduction.md` proves that O in degree n-1 implies
one-direction, nondegenerate admissible collisions in even degree n and
the interval shape of M_n. It does not establish successive nesting and
is not claimed equivalent to the original conjecture. O itself is unproved
in all degrees; the entire strip is verified only for m=1,3,5, with limited
additional exact points recorded in `evidence/odd-strip.json`.

The current primary-source comparison and direct-substitution obstacles are
in `literature/research-pass-1.md`. No novelty claim or candidate is asserted.

## Research pass 2: a stronger induction hypothesis

The original conjunction is unchanged. `evidence/two-step-pass-2.md` proves
that, for all odd m and -1<t<0, Q_(m,t) has positive nonconstant coefficients,
one simple positive root, and no real root at or below -1. Thus O reduces to
simple real-rootedness in its stated strip. Exact discriminant/Sturm certificates
now establish O throughout [-1/3,0) in degrees 7,9,11,13 as well as the earlier
degrees 1,3,5. The conditional collision lemma therefore gives interval shape
also for M8, M10, M12, M14, without a new successive-nesting assertion.

Configuration alone does not support a two-step induction: exact cubic and
degree-seven inputs with the mixed root configuration lose a real pair under
T_t^2 at t=-29/100. Neither input is a shifted-power polynomial. A second
implementation using only rational coefficient arithmetic and Euclidean Sturm
sequences confirms these counterexamples.

The revised sufficient target L adds a coefficient condition. For -b<t<0,
let h have even degree d>=2, positive leading coefficient, and d simple roots
in (-1,0). Put S=h'(0)/h(0), delta=(1+2t)/(1+t)^2. If
0<lambda<=1/(S+delta), does T_t^2[(z-lambda)h] have d+2 simple roots in
(-1,0) and one simple positive root? The added inequality is exactly
[z]T_t^2[(z-lambda)h]>=0 and holds strictly for the actual shifted powers.
The saved argument proves L would imply O by induction from degree three.
L is unproved: 639 exact tests pass, while its extension to -1/3<t<0 is
exactly false at t=-333/1000. Neither this extension nor L is identified with
the frozen original claim. The original and L remain unresolved; no candidate
or publication-value claim is asserted. See `literature/research-pass-2.md`.

## Research pass 3: partial theorem submitted for review

This paragraph supersedes the pass-2 status of L and O; the original frozen
conjunction and its quantifiers above are unchanged. The proof in
`evidence/lemma-l-proof.md` establishes L, including lambda=1/(S+delta),
throughout the larger interval -3/10<=t<0. Its new ingredient is the uniform
strict sign q(-1/[2(S+delta)])>0, derived using weighted Cauchy--Schwarz and
an explicit full-interval Bernstein certificate. Interlacing supplies the
remaining roots. This gives O in all odd degrees on the same interval.

Combining this with the collision argument gives, for every even n>=2,
M_n=[-c_n,1+c_n] with (sqrt(2)-1)/2<=c_n<1-1/sqrt(2). Each exterior
endpoint has a unique double root and all other roots simple, with the
nondegenerate inward splitting described in the proof. The all-degree
successive-nesting assertion c_n<=c_(n+2) remains unresolved. Thus the
candidate kind is result-note, not a resolution of the frozen conjunction.

The proposer has no known gap in this partial theorem; it is awaiting a
fresh mathematical referee, not accepted. `evidence/lemma-l-check.py` and
its JSON certify the algebra and 72 finite regression cases (36 at equality).
The full decisive primary-source text is already inside
`evidence/external/2607.06207v1.html` and is bound into the candidate.
Current comparison and its limitations are in `literature/research-pass-3.md`.
