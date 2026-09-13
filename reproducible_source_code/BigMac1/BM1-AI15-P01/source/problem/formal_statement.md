# Formal statement

Let

\[
M=\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix}\in\mathbb Q^{4\times4}\subset\mathbb R^{4\times4}.
\]

For matrices of the same size, \((A\circ B)_{ij}=A_{ij}B_{ij}\).

## Matrix-specific assertion to decide

The boxed assertion adopted from the source prompt is

\[
(C_M)\qquad
\nexists A,B\in\mathbb R^{4\times4}:\quad
A\circ B=M,\quad \operatorname{rank}_{\mathbb R}A\le2,\quad
\operatorname{rank}_{\mathbb R}B\le2.
\]

The task is complete if either \((C_M)\) is proved by a complete real
infeasibility certificate or it is disproved by one exact feasible pair.
This is exactly the disjunctive success condition in the source task: the
first branch would certify the proposed counterexample, while the second
branch “overturns the candidate” by exhibiting explicit rational, algebraic,
or real factors and checking both the Hadamard identity and rank bounds.

The project reaches the second branch.  Its terminal assertion is therefore
the negation of \((C_M)\), namely

\[
(E_M)\qquad
\exists A,B\in\mathbb Q^{4\times4}\subset\mathbb R^{4\times4}:\quad
A\circ B=M,\quad \operatorname{rank}_{\mathbb Q}A=
\operatorname{rank}_{\mathbb Q}B=2.
\]

An exact rational witness for \((E_M)\) disproves \((C_M)\) and satisfies the
source task even though it does not decide the universal statement below.

## Broader question (explicitly separated)

The universal statement

\[
(U)\qquad \forall N\in\mathrm{GL}_4(\mathbb R)\ \exists A,B\in
\mathbb R^{4\times4}:\ N=A\circ B,\quad
\operatorname{rank}A,\operatorname{rank}B\le2
\]

is background motivation.  Disproving \((C_M)\) does not decide \((U)\).

## Quantifiers and field conventions

- All ranks in \((C_M)\) and \((U)\) are ordinary ranks over \(\mathbb R\).
- A rational witness is also a real witness via \(\mathbb Q\subset\mathbb R\).
- The factors may contain zeros at zero entries of \(M\); both factors are
  allowed to vanish at the same location.
- There are no sign, nonnegativity, integrality, symmetry, or normalization
  constraints on the factors.

## Normalizations

No normalization is needed to verify an explicit witness.  In structural
searches one may multiply one factor entrywise by a nonzero rank-one matrix
and the other by its entrywise reciprocal; any division must be restricted
to entries known to be nonzero.

## Edge cases

Since \(\det M=1\), any feasible factorization has both factor ranks exactly
two: the standard inequality
\(\operatorname{rank}(A\circ B)\le
\operatorname{rank}(A)\operatorname{rank}(B)\) gives
\(4\le\operatorname{rank}(A)\operatorname{rank}(B)\le4\).
The exact witness will nevertheless verify rank two directly, without using
this observation as a hidden boundary assumption.
