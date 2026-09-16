# Precise reading: a proper Euler magic matrix of order seven

## Frozen input and interpretation

The immutable statement is `source.md` (SHA-256
`db3a6a3a46749c29054363b03ef7f9b7acf3eb1989ca3278ee21038f2454a714`,
checked 2026-09-06). Indices below range over \(\{1,\ldots,7\}\).

The question is whether

\[
\exists M=(m_{ij})\in\mathbb Z^{7\times7}\;\exists\gamma\in
\mathbb Z\setminus\{0\}
\]

such that all of the following hold:

1. for every \(i,k\),
   \[
   \sum_{j=1}^7m_{ij}m_{kj}=\gamma\,\delta_{ik};
   \]
2. \(\sum_{i=1}^7m_{ii}^2=\gamma\);
3. \(\sum_{i=1}^7m_{i,8-i}^2=\gamma\); and
4. for every two distinct positions \((i,j)\ne(k,l)\),
   \(|m_{ij}|\ne |m_{kl}|\).

Thus the same \(\gamma\) occurs in the row-orthogonality, main-diagonal,
and anti-diagonal identities. “Proper” means condition 4, equivalently that
the 49 entry-squares are pairwise distinct. The wording permits one zero
entry, but no more than one. There is no requirement that the entries be
positive or consecutive.

An existence resolution must give an explicit integer matrix and verify all
28 upper-triangular entries of \(MM^{\mathsf T}=\gamma I_7\), both diagonal
sums, and all \(\binom{49}{2}=1176\) square inequalities by exact arithmetic.
A nonexistence resolution must exclude every rational solution of the
normalized equations, not merely a search range or a chosen parametrized
family. Near-misses and floating-point matrices do not settle the question.

## Equivalent normalized problem and elementary constraints

Any solution has \(\gamma>0\). Taking determinants gives
\((\det M)^2=\gamma^7\), so every prime valuation of \(\gamma\) is even and
\(\gamma=c^2\) for some \(c\in\mathbb Z_{>0}\). Consequently

\[
Q=M/c\in O(7,\mathbb Q),\qquad D(Q)=A(Q)=1,
\]

where
\(D(Q)=\sum_iq_{ii}^2\) and
\(A(Q)=\sum_iq_{i,8-i}^2\). A row sign change, if needed, puts \(Q\) in
\(SO(7,\mathbb Q)\) without changing the other conditions. Conversely, a
rational orthogonal \(Q\) with \(D(Q)=A(Q)=1\) and 49 distinct absolute
entries yields an integer solution after clearing denominators. Hence the
integer and rational formulations are equivalent.

Since \(M\) is square and invertible, \(M^{\mathsf T}M=\gamma I_7\) follows
from the displayed hypotheses. The entrywise square matrix therefore has all
row sums, column sums, and both main-diagonal sums equal to \(\gamma\), but
the problem is strictly narrower than the general magic-square-of-squares
problem because the signed square roots must be mutually orthogonal.

Distinct nonnegative integer absolute values have total square at least
\(\sum_{r=0}^{48}r^2=38024\). Since the total of all 49 entry-squares is
\(7\gamma\), one has \(\gamma\ge5432\); because \(\gamma=c^2\), necessarily
\(c\ge74\) and \(\gamma\ge5476\). This is only a necessary bound.

## Source status and nearest results

Status: **open-supported as of 2026-09-06**, not independently certified as
open for all possible literature. Exact-title and equivalent-phrase web
searches on that date found no order-seven resolution. The following primary
sources were inspected rather than relying on search snippets:

- Peter Müller, “On Euler's magic matrices of sizes 3 and 8,”
  *Acta Arithmetica* 222 (2026), 71–82; arXiv:2504.16260v2,
  <https://arxiv.org/abs/2504.16260>. Definition 1.1 matches the frozen
  statement. Theorem 4.1 gives an improper permutation-matrix Euler example
  for every order \(n\ge4\), hence in order 7, but its repeated zeros make it
  far from proper. Retrieved 2026-09-06.
- Scott Duke Kominers, “A proper Euler magic matrix of order 5,”
  arXiv:2607.19416v1, <https://arxiv.org/abs/2607.19416>. Definition 1.1 and
  Lemma 2.1 give the definition and odd-order rational normalization above.
  Theorem 3.1/Corollary 3.2 show that left or right Givens rotations on mirror
  pairs preserve \(D+A\); Section 5 explicitly lists the order-seven mirror
  pairs \(\{1,7\},\{2,6\},\{3,5\}\), says a suitable nearly proper seed is
  still needed, and states that proper examples in odd orders beyond 5 remain
  open. Retrieved 2026-09-06.
- Sanjit Singh Mehat, “A proper Euler magic matrix of order 6,”
  arXiv:2608.15318v1, <https://arxiv.org/abs/2608.15318>. The abstract gives
  two exact order-six examples but makes no order-seven claim. Retrieved
  2026-09-06.

No historical-registry artifact was supplied inside the project, so a
registry-level duplicate comparison could not be performed. The mathematical
statement is nevertheless precise and agrees with the cited primary
definition.

## Triage target and first route

Nearest prior result \(X\): Müller supplies an improper order-seven Euler
matrix, while Kominers supplies a mirror-rotation reduction and identifies
the missing ingredient as a suitable order-seven seed. Proposed delta \(Y\):
either an explicit proper order-seven matrix, or a proof excluding all
rational points in the proper locus (the construction direction is the
bounded first priority). Verification route \(Z\): clear denominators and run
a standalone exact-integer checker for orthogonality, both diagonal sums, and
49-way distinctness.

The cheapest seed test already rules out using only the full mirror-rotation
orbit of Müller's order-seven permutation seed. With mirror blocks
\(\{1,7\},\{2,6\},\{3,5\},\{4\}\), a left/right product of such rotations
can occupy at most six \(2\times2\) off-center blocks plus the center, hence
at most 25 positions; at least 24 entries remain zero, contradicting
properness. A richer rational seed or a deformation outside that orbit is
required.

