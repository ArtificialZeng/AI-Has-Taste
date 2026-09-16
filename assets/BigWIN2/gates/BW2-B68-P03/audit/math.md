# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the `conjecture-note` claim bound to snapshot
`60a30a9dacd78f550867410e561af6c611168b788fbac99e34fe2f5a8afcaa4c`.
All file digests in `audit/snapshot.json` agree with the current frozen files.
The claim is explicitly an unproved coefficientwise congruence in
`(Z/16Z)[[q]]`; it is not presented as a resolution of the original
problem. My verdict is **accept** for that exact conjectural scope. This
does not certify the proposed identity, either source progression, or any
priority claim as a theorem.

## Reconstruction of the decisive mathematics

Put

\[
 H(q)=\sum_{m\geq 0}c\phi_{18}(6m+1)q^m.
\]

The proposed identity is

\[
 H(q)\equiv 4\frac{f_2f_3^2}{f_1f_6}\pmod {16}.
\]

Every denominator here has constant coefficient one, so the quotient is a
well-defined formal power series. The claimed exact identification of the
right side follows from the Jacobi triple product:

\[
 \sum_{k\in\mathbb Z}q^{k(3k-1)/2}
 =f_3(-q;q^3)_\infty(-q^2;q^3)_\infty.
\]

Using `1+x=(1-x^2)/(1-x)` in the two nonzero residue classes modulo three
turns the product into `f_2 f_3^2/(f_1 f_6)`. This is a formal identity, not
a finite numerical inference.

For `k` modulo five, `k(3k-1)/2` takes residues only in `{0,1,2}`. Hence the
proposed right side has zero coefficients in classes 3 and 4 modulo five.
The substitutions

\[
 6(5n+3)+1=30n+19,\qquad 6(5n+4)+1=30n+25
\]

are correct. Thus the conjectured full 6-section identity would imply both
parts of the frozen source conjecture, including their `n=0` cases. It is
strictly stronger because it predicts every coefficient of the 6-section
modulo 16, not merely two fifths of that section.

## Exact evidence and independent replay

The submitted constant-term generator correctly represents two rows of
equal length: top entries contribute positive weights and bottom entries
contribute nonnegative weights. For degree at most 3025, a common row length
234 has minimum total weight 3042, whereas length 233 has minimum 3017.
Thus the stated Laurent range through absolute `z`-degree 233 is exhaustive.
The use of arithmetic modulo 256 followed by reduction modulo 16 is exact.
The second submitted generator uses a distinct eta/cubic-theta expansion and
reduces every convolution modulo 16; its int64 bound is safe. Both frozen
3026-byte vectors agree.

I also wrote and ran `audit/referee_replay.py`, which imports neither
submitted generator. It starts from the displayed 17-dimensional lattice
formula. If `D_j(s,a)` counts modulo 16 the `j`-tuples having coordinate sum
`s` and sum of squares `a`, the update

\[
 D_{j+1}(s+x,a+x^2)\mathrel{+}=D_j(s,a)
\]

gives the theta coefficient by summing states satisfying
`a+s^2=2N`. Independently, the coefficients `p_18(n)` of `f_1^{-18}` were
computed over the integers from

\[
 n p_{18}(n)=18\sum_{r=1}^n\sigma_1(r)p_{18}(n-r),
\]

with exact integer division. Convolving these two series and only then
reducing modulo 16 reproduced every frozen coefficient for
`0 <= N <= 3025`. Its full-vector SHA-256 is
`25284b4daebdf702db14e284ae6d4d633597f412cec399c409b5cbd70d64745b`.

Direct generalized-pentagonal enumeration then reproduced every proposed
section coefficient for `0 <= m <= 504`. The section digest is
`8f82367d83f74fbeb3f32cf989c7c921f707c583f7c1e90e73a4d518da310db8`.
In particular, this fresh method covers the entire predeclared held-out
range `100 <= m <= 504`, not just the discovery prefix. The command and
digests are recorded in `audit/referee_replay.json`.

The supplied fourteen-summand audit also gives structural evidence rather
than a bare fit: it identifies formal all-orders cancellations for summand
pairs `(4,5)` and `(10,12)`, proves parity support for five individual
summands, and clearly labels the remaining grouped cancellations as finite
observations.

## Contribution and source comparison

The candidate meets the conjecture-note standard:

- It is precise and immediately falsifiable coefficient by coefficient.
- It has a nontrivial use: it would settle both frozen progressions at once
  and predicts the entire `6m+1` section modulo 16.
- The unary-theta form and the partial formal dissection provide structural
  motivation beyond curve fitting.
- The discovery range `0 <= m <= 99` was separated before testing the held-out
  range `100 <= m <= 504`.
- Two submitted left generators, two right descriptions, a summand attack,
  and the fresh lattice replay constitute a serious exact falsification pass.
- The bounded source search is stated with an honest date and expressly does
  not claim priority or exhaustiveness.

The frozen primary-source audit reports that arXiv:2609.05302v1 states only
the two progressions as Conjecture 5.1 and leaves them open. It also correctly
notes that the paper's `6n+5 (mod 8)` theorem does not cover either target,
since 19 and 25 are both 1 modulo 6. Therefore the proposed identity is not a
routine restatement of the recorded nearest theorem.

## Limits and unresolved gaps

No finite prefix proves the all-orders identity. The unproved dissection
groups remain the central mathematical gap, and the original problem remains
unresolved. The primary PDF was not included in the frozen evidence; the
source audit records inspection of the official versioned HTML and failure of
direct PDF retrieval. Consequently I did not independently verify the
term-by-term transcription of formula (3.15) against a primary-source copy.
This does not invalidate the conjecture-note evidence because the direct
constant-term derivation and the fresh lattice replay establish the finite
observations without relying on that attribution, but the attribution should
be checked again during citation review. The bounded search supports only
the stated literature limitation, not novelty or priority.

Within these expressly conjectural limits, no correctness, scope, or
contribution defect requires revision.
