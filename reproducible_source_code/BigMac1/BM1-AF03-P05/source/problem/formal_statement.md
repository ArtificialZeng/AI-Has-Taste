# Formal statement

## Objects and conventions

All graphs are finite, undirected, loopless simple graphs.  Let
\(G=(V,E)\) have \(V=\{1,\ldots,n\}\), and let \(\overline G\) denote its
simple complement on the same vertex set.  Isomorphic labelled graphs are
regarded as the same case only for enumeration; the theorem quantifies over
every labelled graph.

Define
\[
 S(G)=\left\{A=(a_{ij})\in\mathbb R^{n\times n}:
 A=A^\top,\quad
 (i\ne j\Longrightarrow [a_{ij}\ne0\iff \{i,j\}\in E])\right\}.
\]
The diagonal entries are unrestricted.  Thus the off-diagonal support is
required to be *exactly* \(E(G)\), rather than merely contained in it.  For a
real symmetric matrix \(A\), let \(q(A)\) be the number of distinct real
eigenvalues of \(A\), without multiplicity, and set
\[
q(G)=\min_{A\in S(G)}q(A).
\]
The minimum exists because \(q(A)\) is an integer in the nonempty finite set
\(\{1,\ldots,n\}\) of possible values and \(S(G)\ne\varnothing\).

## Exact endpoint to decide

Prove or disprove the finite statement
\[
\tag{N9}
\forall G\text{ simple on nine vertices},\qquad
 |E(\overline G)|\le6\ \Longrightarrow\ q(G)=2.
\]
No connectivity, minimum-degree, or absence-of-isolates hypothesis is imposed
on \(\overline G\).  Both bipartite and non-bipartite complements belong to
the formal endpoint, although a verified published theorem may discharge the
bipartite cases.  Edge counts \(0,1,\ldots,6\) and disconnected/degenerate
complements are included.

## Orthogonal normalization

For every nonempty graph \(G\), the following are equivalent:

1. \(q(G)=2\);
2. there is a real symmetric \(Q\in S(G)\) with \(Q^2=I_n\) and both
   eigenvalues \(+1,-1\) present.

Indeed, if \(A\in S(G)\) has exactly the two eigenvalues \(\lambda\ne\mu\),
then
\[
Q=\frac{2A-(\lambda+\mu)I}{\lambda-\mu}
\]
has the same off-diagonal zero/nonzero pattern, is symmetric, and satisfies
\(Q^2=I\).  Conversely, an involution in \(S(G)\) has at most two distinct
eigenvalues.  If \(G\) is nonempty it cannot be \(\pm I\), so it has exactly
two.  Every graph in (N9) is nonempty because it has at least
\(\binom92-6=30\) edges.  Hence an exact symmetric orthogonal realization is
both sufficient and necessary for (N9), with no lost endpoint.

Equivalently, writing \(Q=I-2P\), it is enough and necessary to construct a
nontrivial real orthogonal projection \(P=P^\top=P^2\) such that, for
\(i\ne j\),
\[
 P_{ij}=0\iff \{i,j\}\in E(\overline G).
\]

## Baseline and novelty assertions kept separate

The claims that the implication is already known for bipartite complements,
that orders \(7\) and \(8\) were previously verified, and that order \(9\) is
the first unresolved order are literature assertions, not assumptions in
(N9).  Gate 1 verified these assertions with a provenance refinement: the
conjecture was first published by Fallat--Mojallal (2023), explicitly from a
2022 communication by the six authors who restated it in 2026.  Gate 1 also
showed that the literature-only unresolved frontier can be narrowed from
non-bipartite complements with at most six edges to those with exactly six
edges.  The certified enumeration below nevertheless retains every edge
count \(0,\ldots,6\), so the formal endpoint is not weakened by that reduction.
