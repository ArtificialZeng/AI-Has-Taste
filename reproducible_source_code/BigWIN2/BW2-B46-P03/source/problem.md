# Precise reading

## Frozen claim to classify

For integers \(n\ge 13\) and \(w>n-1\), let
\[
[n-1]=\{1,2,\ldots,n-1\},\qquad
V_{n,w}=([n-1]\setminus\{12\})\cup\{w\}.
\]
For a real number \(x\), write
\[
\|x\|=\min_{k\in\mathbb Z}|x-k|
\]
for its distance to the nearest integer, and for a finite set of positive
integer speeds \(V\), define
\[
LR(V)=\max_{0\le t<1}\min_{v\in V}\|vt\|.
\]
(The maximum exists: the inner minimum is a continuous, one-periodic
function.)  Determine exactly the set
\[
\mathcal T_{12}=\{(n,w)\in\mathbb Z^2:n\ge13,\ w>n-1,
\ LR(V_{n,w})=1/n\}.
\]
The proposed classification to test is
\[
\mathcal T_{12}=\{(14,24)\}.
\]
This last display is a conjectural candidate, not an assumed fact.

## Quantifiers, normalization, and boundary cases

- Both parameters are integers. Since \(w>n-1\), equivalently \(w\ge n\),
  the inserted speed is positive and is not already in \([n-1]\); hence
  \(V_{n,w}\) has exactly \(n-1\) distinct positive speeds.
- The lower boundary \(n=13\) is included. It is the first admissible value
  for which the deleted speed \(12\) belongs to \([n-1]\).
- Equality is literal equality of real numbers, not a numerical tolerance.
  A classification proof must establish both inclusions: verify
  \(LR(V_{14,24})=1/14\), and rule out equality for every other admissible
  integer pair. Values greater than or less than \(1/n\) both rule out a pair,
  but neither may be inferred from floating-point evidence alone.
- Multiplying all speeds by a common factor is not part of the parameter
  space: the fixed baseline speeds \(1,\ldots,n-1\) make every \(V_{n,w}\)
  primitive (it contains speed \(1\)).

## Scope and nearest prior results

The frozen primary source is Yuhan Zhang, *Single-speed modifications of the
tight Lonely Runner instance: an effective bound and the complete
classification for r = 2*, arXiv:2608.13599v1.  Its notation
\([n-1]_{r\mapsto w}\) agrees with the set above when \(r=12\).

- Proposition 1.3 and Theorem 1.1 cover \(2r>n-1\), hence \(13\le n\le24\)
  here. Tightness then forces \(12\mid w\), and Theorem 1.1 supplies an exact
  gcd criterion.
- For \(n\ge25\), Theorem 1.6 says any tight pair must satisfy \(n\le72\) and
  \(w\le 48I(n,12)/(2(n-12)-I(n,12))\), with \(I\) defined in equations
  (2)--(3) of that paper.
- Theorem 1.8(i) and Table 1 certify a census only for \(5\le n\le45\) and
  \(n\le w\le10n\); they include \((14,24)\) and contain no other entry with
  deleted speed \(12\). Question 5.1 asks for the broader middle-range
  classification. Thus the fixed-\(r=12\) statement is an open-supported
  specialization/finite follow-up, not a theorem asserted in the cited paper.

The intended full-resolution route is therefore: derive all remaining pairs
from these theorems, compute \(LR\) at the complete rational breakpoint set of
Lemma 2.2 for each remaining pair, retain exact maximizing witnesses, and
cross-check with an independently implemented exact method. The source PDF
inspected for this reading has SHA-256
`c661b2edcda1b6d11225c5c94e8a4289ed223da6cba82702336910c38bd73d44`.
