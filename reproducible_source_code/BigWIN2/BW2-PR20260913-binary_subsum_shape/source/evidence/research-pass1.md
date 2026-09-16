# Research pass 1: finite compensation test and induction work

Job: `primary-20260913-binary-subsum-shape-research-f5d9991a30d8`.
Original target and normalization are unchanged; see `source.md`, `problem.md`.

## Completed exact test

`python3 evidence/research_recurrence.py` writes
`evidence/research_recurrence.json`. It reconstructs all even N_n for 2<=n<=512,
then tests every internal coefficient. The newly assigned range, even
130<=n<=512, comprises 192 polynomials and 441984 internal indices.
At every one of these indices, T_j(N_n)>=T_j(A_n)>=0. There is no original
counterexample. The first-failure fields in the JSON are therefore null.
Across the whole constructed range, the only non-log-concave N_n is N4.
The only negative compensation values occur at n=2,4,6,8.

All decisions use arbitrary-precision integers. For A_n, the implementation
uses exact integer-packed convolution with the binomial coefficients. The
packing base exceeds the sum of all convolution coefficients, precluding carry
between coefficient positions. Separate repeated Pascal multiplication agrees
for even n=2,...,32 and n=130,256,512. Direct partition enumeration agrees for
n=0,...,16. Each polynomial has a reproducible coefficient hash in the JSON.
These cross-checks are different algorithms in this worker, not a fresh referee.

This is a finite observation, not a proof, novelty claim, or candidate.
As required by the prior next test, the next work is a uniform induction attempt;
no further finite-range extension is justified merely by this survival.

## Induction work and changed evidence

The carry multiplier has the exact form

    F_r(x) = product_(i=1)^r (1+x^(2^i))
           = sum_(t=0)^(2^r-1) x^(2t),  r=v2(n).

Thus B_n is an even-spaced moving sum of N_(n-2). Ordinary convolution
preservation for log-concave sequences cannot directly be applied: F_r has
internal zero coefficients. The missing step is a sufficient quantitative
shape condition that this particular recurrence preserves, including the
interaction of A_n and B_n.

The carry-one subclass reduces to A_new=(1+x)^2 A and
N_new=A_new+(1+x^2)N. Positive palindromic inputs satisfying the *strict*
compensation invariant at every internal index do not suffice to preserve
it. An exact degree-eight input has output T_1(N_new)=-304. This is a proved
obstruction to that abstract hypothesis class, not a counterexample involving
the actual binary numerator sequence. Complete input/output coefficients are
in `evidence/research_boundary.json`.

There is also a uniform boundary proof. For every even n>=6,
T_j(N_n)>T_j(A_n)>0 at j=1,2,d(n)-2,d(n)-1. The j=2 assertion already holds
for even n>=4. A cubic coefficient identity reduces the proof to increasing
binary partition counts and a symmetric quadratic kernel. Four explicit
polynomial expansions certify the kernel's nonnegativity. The complete
argument, exact scope and limitations are in `evidence/research-boundary-proof.md`;
`evidence/research_boundary.py` reproduces the symbolic certificates, 454
literal kernel checks and recurrence calibration through even n=128.

No candidate is proposed: the boundary result is narrow, its value as a route
to the remaining coefficients is unestablished, and independent review and
novelty screening of that precise result have not occurred. It is retained as
a proved local research lemma rather than packaged as a small paper.

One next test: decide the explicit third-position kernel K3_m(l,t)>=0 for
all integers m>=5 and 0<=l<=t<=m by a piecewise polynomial certificate or an
exact negative kernel entry. The proof dossier defines K3 from the quartic
coefficient formula. An exact screen of all 6510 pairs for 5<=m<=32 found
no negative entry. This is a new algebraic target, not another extension of
the original polynomial prefix. Failure of this kernel would concern the
specified monotone-weight proof route only.
