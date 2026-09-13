# Precise problem statement

## Frozen input and bibliographic correction

The immutable statement is `source.md` (SHA-256
`fbffc6b3d9b3b2db7bac8945473758846ca4cf5d4db8d9fb17073f50d47cfe43`).
Its mathematical task is coherent, but its citation metadata is not: arXiv
`2609.03444v1` is Francesco Cordella, *Odd denominators in the Lonely Runner
spectrum for six speeds* (submitted 2026-09-03), not the authors and title
printed in `source.md`. The theorem/table references and the examples with
22 and 33 match Cordella's paper. This correction does not alter the frozen
problem.

## Definitions and quantifiers

Let
\[
  D=\mathbb Z_{>0}\setminus\{1,4,5,6,7\}.
\]
For a real number \(x\), put
\[
  \lVert x\rVert=\min_{k\in\mathbb Z}|x-k|.
\]
This depends only on the class of \(x\) in the circle
\(\mathbb T=\mathbb R/\mathbb Z\). For every \(m\in D\), define
\[
 f_m(t)=\min\{\lVert t\rVert,\lVert4t\rVert,\lVert5t\rVert,
                    \lVert6t\rVert,\lVert7t\rVert,\lVert mt\rVert\},
 \qquad t\in\mathbb T,
\]
\[
 L(m)=\max_{t\in\mathbb T}f_m(t),\qquad
 A(m)=\{t\in\mathbb T:f_m(t)=L(m)\}.
\]
The maximum exists because \(f_m\) is continuous on compact \(\mathbb T\).
All six speeds are positive and pairwise distinct by the definition of \(D\).

The requested determination is:

1. Give an exhaustive, mutually exclusive partition of every \(m\in D\)
   (for example by congruences plus explicitly listed exceptions), and on
   every part give an exact rational expression for \(L(m)\). Every positive
   admissible \(m\), without a finite search cutoff, must be covered.
2. Determine the complete set \(A(m)\) modulo 1 on every part, not merely one
   witnessing time. Fractions denote their classes in \(\mathbb T\); the
   symmetry \(t\mapsto1-t\) may be used to compress the answer.
3. Determine exactly
   \[
     N=\{m\in D:1/7<L(m)<1/6\}.
   \]
   Both inequalities are strict. This parenthetical definition in the
   frozen source is binding; it is narrower than Cordella's convention
   “near-tight” \(ML<1/6\), which does not itself exclude \(ML=1/7\).

“Complete piecewise rational formula” is read as a proved all-\(m\)
classification. A finite exact scan, a fitted periodic pattern, or a list of
candidate cases is evidence only, not a solution.

## Source status and nearest prior result

Status: **source-derived / status-uncertain; original determination problem
unresolved at triage**.

Primary source inspected 2026-09-06:

- Francesco Cordella, *Odd denominators in the Lonely Runner spectrum for six
  speeds*, arXiv:2609.03444v1,
  <https://arxiv.org/abs/2609.03444>. Local copy:
  `literature/Lonely-Runners-2609.03444v1.pdf`, SHA-256
  `28794c2fa76d481e951bfbff96e9d77781e539bae8318081eab5c31e0b09d688`.
- Lemma 2.2 (printed p. 4) gives an exact finite candidate-time algorithm:
  maxima below \(1/2\) occur when two coordinates coincide or are antipodal,
  so times have denominators among pairwise sums and nonzero differences.
- Theorem 6.1 (printed p. 13) treats all but a finite exceptional set of
  near-tight sextuples and reports an exact search through maximum speed 110;
  it does not classify this entire one-parameter family.
- Table 2 (printed p. 14) records
  \(L(22)=2/13\) and \(L(33)=6/37\). The discussion immediately before
  Section 6.2 notes the base quintuple \((1,4,5,6,7)\), of maximum loneliness
  \(2/11\), with 22 or 33 adjoined. Section 6.4 contains broader open
  questions, not an analysis of all \(m\).

## Triage target

Nearest prior result \(X\): the items above. Proposed delta \(Y\): an exact
all-\(m\) formula for \(L(m)\), the full argmax sets \(A(m)\), and the strict
near-tight set \(N\). Verification route \(Z\): specialize Lemma 2.2's
collision/antipode candidates to \((1,4,5,6,7,m)\), prove that the resulting
upper envelope is exhaustive, and independently check all exceptional
parameters in exact rational arithmetic.
