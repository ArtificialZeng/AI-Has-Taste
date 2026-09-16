# Fresh mathematical audit

## Binding and verdict

This report reviews the exact `resolution-paper` claim frozen by snapshot
`c23de72807980bc65d10c3c5ee03746d1f1b64e0c846a0eccfa70336b4e8d4fc`.
All hashes in `audit/snapshot.json` were recomputed and agree with the listed
files, and the snapshot digest agrees with the canonical digest of its file
mapping. The mathematical verdict is **accept**: the cited results cover the
infinite parameter range, the remaining finite cases have valid exact upper
and lower certificates, and the claimed unique pair is established at the
full frozen scope.

## Reconstructed universal reduction

Write (r=12) and (s=n-12). I checked the statements and hypotheses of
Theorem 1.1, Proposition 1.3, Theorem 1.6, Theorem 1.8(i), Table 1, and Lemma
2.2 in the frozen copy of Zhang's arXiv:2608.13599v1.

For (13\le n\le24), the hypothesis (2r>n-1) holds. Proposition 1.3
therefore forces (12\mid w), say (w=12m). Theorem 1.1 then says that
tightness is equivalent (the exceptional cases in that theorem do not apply)
to

\[
  \gcd(12,b)>1\quad\text{for every }s\le b\le ms-1.
\]

Since (w>n-1), (m\ge2). At (n=13), the interval contains (1). At
(n=14,m=2), it is exactly \(\{2,3\}\), so the criterion holds; for
(n=14,m\ge3), it contains (5). For (n=15,\ldots,24), already at
(m=2) the interval contains, respectively,
(5,5,5,7,7,11,11,11,11,13). Each displayed obstruction is coprime to
12 and remains in the interval for larger (m). Hence this range contributes
exactly ((14,24)), and Theorem 1.1 itself supplies equality there.

For (n\ge25), the hypothesis (2r\le n-1) holds. Theorem 1.6 gives
(n\le6r=72) and

\[
  w\le B(n)=\frac{48I(n,12)}{2(n-12)-I(n,12)}.
\]

From equations (2)--(3) of the paper, the units modulo 12 give

\[
 I(n,12)=\min\{F(1),F(5),F(7),F(11)\},
 \qquad F(u)=\max\{i\le n-1:i\equiv u\pmod {12}\}.
\]

I independently evaluated these four residue maxima with integers for every
(25\le n\le72). For (25\le n\le45), the largest value of
(\lfloor B(n)\rfloor) is 74, so every possible (w) satisfies
(n\le w\le74<10n). Theorem 1.8(i) and Table 1 are therefore applicable;
their exhaustive list contains no deleted-speed-12 case in this range.

For (46\le n\le72), intersecting (w\ge n) with the exact bound leaves
exactly

\[
\begin{aligned}
 &(46,46),(46,47),(46,48),(46,49),(46,50),\\
 &(47,47),(47,48),\\
 &(48,48),(48,49),(48,50),\\
 &(50,50),(50,51),(50,52),(50,53),(50,54),(50,55),(50,56),\\
 &(51,51),(51,52),(51,53).
\end{aligned}
\]

This independently reproduces the 20-pair list in the frozen evidence. Values
(n>72) are excluded directly by Theorem 1.6. Thus no admissible parameter
range is left untreated.

## Exact finite certification

I inspected both implementations and the complete serialized certificate
data. The breakpoint implementation constructs precisely the three families
in Lemma 2.2: individual peaks ((2a+1)/(2v)), pairwise sum crossings
(b/(v+w)), and pairwise difference crossings (b/(w-v)), with the stated
complete ranges of the integer indices. All evaluations use exact rational
arithmetic.

I then performed a fresh exact recomputation from those displayed families,
without invoking either evidence program. For all 21 cases (the positive
control and 20 residual pairs), the recomputed number of distinct
breakpoints, maximum value, and least attaining time agree with
`lr_breakpoints_results.json`.

The interval-cover evidence also gives a proof independent of the breakpoint
lemma. For a speed (v) and (0\le q\le1/2),

\[
 \{t\in[0,1]:\|vt\|\le q\}
 =\bigcup_{k=0}^{v}
 \left[\frac{k-q}{v},\frac{k+q}{v}\right]\cap[0,1].
\]

I independently parsed and checked every saved cover record against this
formula: 6,305 labeled rational intervals in total. In each of the 21 cases,
the first interval begins at 0, consecutive intervals overlap at the current
frontier, and the last reaches 1. This proves (LR(V)\le q). I also
recomputed all 964 saved speed distances at the asserted rational times;
each list contains exactly the relevant speed set and has minimum exactly
(q), proving (LR(V)\ge q).

The resulting exact values are:

- (LR(V_{14,24})=1/14);
- (2/59) for ((46,46),(46,48),(46,49),(46,50),(47,48));
- (2/61) for ((46,47),(47,47),(48,48),(48,50));
- (2/65) for ((48,49),(50,50),(50,51),(50,52),(50,54),
  (50,55),(50,56),(51,51),(51,52));
- (2/67) for ((50,53),(51,53)).

Each residual value is strictly greater than the corresponding (1/n), so
none of the residual pairs is tight.

## Source comparison and contribution

The frozen primary source proves the large-deletion criterion and the
middle-range effective bound, but its exact census stops at (n=45), and its
Question 5.1 explicitly leaves the middle-range classification open. The
present claim uses those published results and adds a complete exact treatment
of the 20 cases remaining for (r=12). It is therefore a full solution of the
frozen specialization, not a toy restriction or a finite check presented as a
universal argument. The literature statement is appropriately bounded: the
evidence records a same-date screen of the current arXiv record and exact
topic, while making no unconditional priority claim.

## Gaps and final decision

I found no mathematical or scope gap. The computations are exact, their
certificate logic was independently checked, the known positive pair is
proved rather than merely reproduced numerically, and the theorem-based
exhaustion covers every admissible integer pair. This acceptance certifies the
frozen mathematical claim only; it does not by itself certify publication
formatting, broader literature priority, or journal acceptance.

