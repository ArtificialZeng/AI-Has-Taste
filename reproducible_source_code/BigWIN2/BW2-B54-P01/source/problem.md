# Precise problem statement

## Frozen instance and mathematical reading

Let \(\mathbb N_0=\{0,1,2,\ldots\}\), with its usual addition and
multiplication, and set
\[
A=\begin{pmatrix}1&12\\11&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&132\\1&1\end{pmatrix}.
\]
The question is the truth of the following unbounded existence statement:

> Does there exist an integer \(\ell\geq 1\), positive integers
> \(n_0,\ldots,n_\ell\) with \(n_0=n_\ell=2\), square matrices
> \(M_i\in\mathbb N_0^{n_i\times n_i}\) with \(M_0=A\) and
> \(M_\ell=B\), and, for every \(0\leq i<\ell\), rectangular matrices
> \(R_i\in\mathbb N_0^{n_i\times n_{i+1}}\) and
> \(S_i\in\mathbb N_0^{n_{i+1}\times n_i}\) such that
> \(M_i=R_iS_i\) and \(M_{i+1}=S_iR_i\)?

There is no bound in the problem on \(\ell\), the intermediate dimensions
\(n_i\), or the entries. Zero entries are allowed. An affirmative resolution
requires one finite chain with every displayed factorization checked over
\(\mathbb N_0\). A negative resolution must exclude all such finite chains,
not merely chains below chosen length, dimension, or entry bounds. Any bounded
nonexistence result is only partial and must state its bounds. Shift equivalence,
integer similarity, agreement of spectral invariants, or failure of a particular
search is not a resolution.

This is exactly the \(k=11\) member of Baker's family
\[
A_k=\begin{pmatrix}1&k+1\\k&1\end{pmatrix},\qquad
B_k=\begin{pmatrix}1&k(k+1)\\1&1\end{pmatrix}.
\]
Only this fixed value \(k=11\) is in scope.

## Intake checks and source status

Both matrices are positive (hence primitive), have trace \(2\), determinant
\(-131\), and characteristic polynomial \(t^2-2t-131\). They are integrally
similar: with
\[
P=\begin{pmatrix}1&12\\1&11\end{pmatrix},\qquad \det P=-1,
\]
one has \(AP=PB\). They are also shift equivalent over \(\mathbb N_0\). For
example, at lag \(22\), take \(R=P\) and
\[
S=P^{-1}A^{22}=
\begin{pmatrix}
3639181777320288676873&675432186255210239002500\\
56286015521267519916875&330834707029117152443
\end{pmatrix}.
\]
Exact integer arithmetic gives \(AR=RB\), \(SA=BS\), \(RS=A^{22}\), and
\(SR=B^{22}\). Thus the standard easy necessary tests pass, but none implies
strong shift equivalence. The displayed \(S\) first becomes entrywise
nonnegative at lag 22 for this particular intertwiner \(P\); this is not a
claim that 22 is the minimum lag among all shift equivalences.

Source status: **open-supported**, not proved open in an absolute sense. Jeandel,
*Combinatorial Search for Strong Shift Equivalence*, arXiv:2609.03567v1
(submitted 2026-09-03), Definition 1 and Problem 3, defines the family and the
question. Theorem 2 and Section 2.1 report exact SSE chains for \(k\leq10\) and
\(k=12\), while reporting no chain found for the remaining tested \(k\geq11\),
including \(k=11\); the text explicitly treats search exhaustion as nonproof.
The nearest proved result is therefore the same family at the adjacent values
\(k=10\) and \(k=12\), not the present instance. Inspected at
https://arxiv.org/abs/2609.03567v1 and its 49-page PDF on 2026-09-07, especially
PDF pp. 1--7 (Definition 1, Problem 3, Theorem 2, Sections 2.1 and 3.1).
Exact-assertion and equivalent-language searches on 2026-09-07 retrieved no
primary source resolving \(k=11\) beyond that new preprint; this limited search
does not establish priority or continuing open status.

## Proposed contribution and verification route

Nearest prior result: Jeandel's verified chains for the same family through
\(k=10\) and exceptionally at \(k=12\). Proposed delta: settle the omitted
\(k=11\) instance, preferably by an explicit SSE chain; otherwise obtain a
strictly bounded, reproducibly exhaustive obstruction without representing it
as a resolution. An affirmative certificate is mechanically verifiable by
checking nonnegativity, dimensions, and every identity \(M_i=R_iS_i\),
\(M_{i+1}=S_iR_i\) in exact integer arithmetic.

