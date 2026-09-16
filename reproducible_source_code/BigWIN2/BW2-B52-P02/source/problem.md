# Precise problem reading

## Frozen target

Let \(P_k\) be the simple path with vertex set \(\{0,\ldots,k-1\}\) and edges
\(\{i,i+1\}\).  The Cartesian product

\[
G=P_3\square P_4
\]

has vertex set \(\{0,1,2\}\times\{0,1,2,3\}\), with distinct \((i,j)\)
and \((i',j')\) adjacent exactly when
\(|i-i'|+|j-j'|=1\).  Thus \(|V(G)|=12\), \(|E(G)|=17\), and its degree
sequence is nonconstant.

For a finite abelian group \(\Gamma\), written additively, and a set
\(S\subseteq\Gamma\setminus\{0\}\) with \(S=-S\), the simple undirected Cayley
graph \(\operatorname{Cay}(\Gamma,S)\) has vertex set \(\Gamma\), with distinct
\(x,y\) adjacent exactly when \(y-x\in S\).  An induced Abelian Cayley embedding
of a finite simple graph \(H\) is an injection \(f:V(H)\to\Gamma\) such that,
for every pair of distinct vertices \(u,v\),

\[
uv\in E(H)\quad\Longleftrightarrow\quad f(v)-f(u)\in S.
\]

Define

\[
\eta(H)=\min\{|\Gamma|:\Gamma\text{ is finite abelian and such }S,f
\text{ exist}\}.
\]

The problem is to determine the unique integer \(N=\eta(P_3\square P_4)\).
Equivalently, an exact resolution must supply (a) one finite abelian group of
order \(N\), one symmetric connection set, and one injection satisfying the
displayed biconditional, and (b) a proof that for every integer \(M<N\), every
finite abelian group \(\Gamma\) of order \(M\), every injection
\(f:V(G)\to\Gamma\), and every legitimate \(S\), the biconditional fails.
There is no isometry requirement, and the quantifier over host groups is not
restricted to cyclic groups.

For a fixed injection \(f\), define

\[
D_E=\{\pm(f(v)-f(u)):uv\in E(G)\},\qquad
D_{\bar E}=\{\pm(f(v)-f(u)):u\ne v,\ uv\notin E(G)\}.
\]

The source's Proposition 3 gives the exact finite certificate condition:
some connection set works if and only if \(D_E\cap D_{\bar E}=\varnothing\),
in which case \(S=D_E\) works.

## Established bounds and boundary cases

The injectivity floor gives \(\eta(G)\ge 12\).  Equality at the number of
vertices occurs only when the graph itself is an abelian Cayley graph; since
\(G\) is irregular whereas every Cayley graph is regular, \(\eta(G)>12\).
Hence

\[
13\le \eta(P_3\square P_4)\le 20.
\]

The upper bound has the explicit product certificate
\(\Gamma=\mathbb Z_4\times\mathbb Z_5\),
\(f(i,j)=(i,j)\), and
\(S=\{\pm(1,0),\pm(0,1)\}\).  The selected coordinate ranges do not wrap
around to create an extra edge.  This is the source's verified order-20
construction, not an exact value.

For a complete lower certificate below 20, the unresolved orders reduce to the
following abelian isomorphism types (orders below 13 are already excluded):

- 13: \(\mathbb Z_{13}\); 14: \(\mathbb Z_{14}\); 15: \(\mathbb Z_{15}\);
- 16: \(\mathbb Z_{16}\), \(\mathbb Z_2\times\mathbb Z_8\),
  \(\mathbb Z_4\times\mathbb Z_4\),
  \(\mathbb Z_2^2\times\mathbb Z_4\), and \(\mathbb Z_2^4\);
- 17: \(\mathbb Z_{17}\); 18: \(\mathbb Z_{18}\) and
  \(\mathbb Z_3\times\mathbb Z_6\); 19: \(\mathbb Z_{19}\).

A search may stop at the first host order, but every smaller type must be
exhausted.  Translation permits normalising one chosen grid vertex to zero;
graph and host automorphism reductions require a completeness justification.

## Source status, nearest prior result, and proposed delta

Source status: **new-question**.  The cited paper does not state this individual
cell as an open problem, but its general Problem 2 asks how far the product bound
can be improved.  Its Section 5.1, Theorem 14 and Corollary 15 prove the product
bound; the paragraph following Corollary 15 verifies the order-20 construction
for \(P_3\square P_4\).  Table 1 gives only one exact path-grid value,
\(\eta(P_3\square P_3)=15\), against its product bound 16.  No exact value for
\(P_3\square P_4\) is supplied.

Nearest prior result: the exact adjacent square cell
\(\eta(P_3\square P_3)=15\), plus the target's explicit order-20 host.
Proposed delta: determine the target's exact value over **all** finite abelian
groups.  Verification route: enumerate the finite list above in increasing
order using the exact difference-separation predicate, emit any host labelling
as a directly checkable certificate, and preserve exhaustive no-host counts/logs
for every smaller group type for independent rerun.

Primary source inspected 2026-09-07: R. Fokam Souop and L. Bitjoka,
*Induced Embeddings of Graphs into Abelian Cayley Graphs*,
[arXiv:2609.01486v1](https://arxiv.org/abs/2609.01486v1), especially Definition 1,
Proposition 3, Proposition 5, Theorem 10, Theorem 14, Corollary 15, Table 1, and
Problem 2.  Exact-assertion searches found no separate primary source stating
the target value; this limited search is not evidence of priority or open status.

## Source-record correction (not a change to the frozen problem)

The immutable `source.md` attributes arXiv:2609.01486v1 to J. A. Noel and
J. A. Scott.  The official arXiv v1 record and paper instead name Rigobert Fokam
Souop and Laurent Bitjoka.  The arXiv identifier, title, theorem numbering, grid
construction, Table 1, and Problem 2 otherwise match the mathematical lead, so
the attribution error does not make the target ambiguous.  `source.md` remains
unchanged.
