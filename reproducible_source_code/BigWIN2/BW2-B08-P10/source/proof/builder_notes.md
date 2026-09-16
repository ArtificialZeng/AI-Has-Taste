# Builder branch: exact spectral reductions and unconditional subclasses

## Scope and conventions

Throughout this note, `graph` means a finite undirected simple graph.  Write
\(n=|V(G)|\), \(m=|E(G)|\), and, for connected \(G\),
\(c=m-n+1\).  For a real symmetric matrix \(M\), let
\(n_+(M),n_0(M),n_-(M)\) be its inertia and use the convention
\[
  s(M)=n_+(M)-n_-(M).
\]
Thus \(s(L(G))\) below means the signature of the adjacency matrix of the
line graph.  This convention must be checked against the source note; changing
the sign convention changes the problem.

No census result is assumed anywhere below.

## 1. Exact incidence/signless-Laplacian reduction

Let \(B\in\{0,1\}^{n\times m}\) be the (unsigned) vertex-edge incidence
matrix, and put \(Q=D+A=BB^{\mathsf T}\).  Direct entrywise multiplication
gives
\[
 B^{\mathsf T}B=2I_m+A(L(G)).                                      \tag{1}
\]
The nonzero eigenvalues of \(B^{\mathsf T}B\) and \(BB^{\mathsf T}\),
with multiplicity, coincide (e.g. by singular-value decomposition).  If
\(r=\operatorname{rank}B\), it follows that the spectrum of \(A(L(G))\)
consists of
\[
 \{q-2:q\in\operatorname{Spec}(Q),\ q>0\}
 \quad\text{and}\quad -2\text{ with multiplicity }m-r.             \tag{2}
\]
For a connected graph,
\[
 r=\begin{cases}n-1,&G\text{ bipartite},\\ n,&G\text{ nonbipartite},\end{cases} \tag{3}
\]
provided \(m>0\).  Indeed, \(x^{\mathsf T}B=0\) says \(x_u+x_v=0\)
on every edge; connectedness leaves a one-dimensional solution precisely
when the graph is bipartite.  The isolated one-vertex graph is harmless and
can be checked separately.

Define the threshold counts among *all* eigenvalues of \(Q\)
\[
 a=\#\{q:q>2\},\qquad z=\#\{q:q=2\},\qquad
 b=\#\{q:0<q<2\}.
\]
Then (2) yields
\[
 n_+(A(L(G)))=a,\quad n_0(A(L(G)))=z,\quad
 n_-(A(L(G)))=b+m-r.
\]
Since \(a+b+z=r\), cancellation gives the particularly useful exact identity
\[
 \boxed{s(L(G))=2a+z-m.}                                           \tag{4}
\]
Consequently the target inequality is *equivalent* to
\[
 \boxed{4a+2z\le 3m-n+2.}                                         \tag{5}
\]
This is an exact integer threshold-count formulation, not a numerical test.
It also handles an eigenvalue exactly equal to 2 correctly; discarding \(z\)
is an unsafe shortcut.

## 2. An unconditional dense-graph theorem

**Theorem.** If \(G\) is connected and
\[
                  3m\ge 5n-2,                                     \tag{6}
\]
then \(2s(L(G))\le c(G)+1\).

**Proof.** Trivially \(a+z\le n\), hence
\(2a+z\le2(a+z)\le2n\).  By (4), \(s(L(G))\le2n-m\). Therefore
\[
2s(L(G))\le4n-2m\le m-n+2=c(G)+1,
\]
where the middle inequality is exactly (6). \(\square\)

The same argument gives the slightly sharper graph-specific sufficient
condition \(4a+2z\le3m-n+2\), but that is merely the equivalent criterion
(5), not an a priori structural theorem.  Replacing \(n\) by the incidence
rank does not automatically improve the displayed theorem uniformly because
the coefficient of \(z\) must be retained; one does have
\(2a+z\le2r-z\).

For order 9, (6) proves the conjecture without computation whenever
\(m\ge15\).  Thus an exact order-9 search need only treat connected graphs
with \(8\le m\le14\) (plus the trivial one-vertex case), if its only purpose
is detecting a counterexample.  This is a mathematically proved pruning rule.

## 3. Exact benchmark families

These are useful both as independently checkable subclasses and as unit tests
for any census implementation.

### Stars and paths

For \(G=K_{1,t}\), \(L(G)=K_t\), whose spectrum is
\(t-1,-1^{(t-1)}\) for \(t\ge2\).  Hence \(s=2-t\), while \(c=0\), so the
inequality holds.  The cases \(t=0,1\) are immediate.  For a path \(P_n\),
\(L(P_n)=P_{n-1}\).  The eigenvalues of \(P_k\) are
\(2\cos(j\pi/(k+1))\), \(1\le j\le k\); pairing \(j\) with \(k+1-j\)
shows equal positive and negative counts.  Thus \(s=0\), and equality in the
integer-strengthened assertion \(s\le0\) holds for every path.

### Cycles

For \(G=C_n\), also \(L(G)=C_n\), with eigenvalues
\(2\cos(2\pi j/n)\), \(0\le j<n\).  Counting the indices in the two open
semicircles (and the possible two zero endpoints when \(4\mid n\)) gives
\(s(C_n)\in\{-1,0,1\}\).  Since \(c=1\), the required assertion is
\(s\le1\), and hence holds.  This count is exact and includes zero
eigenvalues.

### Complete bipartite graphs

For \(G=K_{u,v}\), the line graph (the rook graph) has spectrum
\[
u+v-2\ (1),\quad u-2\ (v-1),\quad v-2\ (u-1),\quad
-2\ ((u-1)(v-1)).                                                   \tag{7}
\]
The formula follows directly by decomposing functions on
\([u]\times[v]\) into constants, row-zero, column-zero, and doubly-zero
subspaces.  Separating the endpoint cases \(u=1\), \(v=1\), \(u=2\), or
\(v=2\), (7) gives the target inequality by elementary substitution.  In
particular, for \(u,v\ge3\),
\[
s=u+v-1-(u-1)(v-1),\qquad c=(u-1)(v-1),
\]
and the inequality is immediate (its left side rapidly becomes negative).

### Complete graphs

For \(G=K_n\), the triangular graph \(L(K_n)\) has spectrum
\[
2(n-2)\ (1),\quad n-4\ (n-1),\quad -2\ (n(n-3)/2),                 \tag{8}
\]
with the small cases \(n\le3\) read directly.  Formula (8), obtained as well
from the spectrum of \(Q(K_n)=(n-2)I+J\) and (2), verifies the inequality.
For \(n\ge4\) it is also covered by the dense theorem except for irrelevant
small endpoints.

## 4. Potential proof routes and exact gaps

1. **Threshold-count route.** A full proof is reduced by (5) to bounding the
   number of signless-Laplacian eigenvalues above 2, with half weight for
   those equal to 2.  Trace alone is inadequate: eigenvalues just above 2 can
   consume arbitrarily little excess, while small eigenvalues can compensate.
   A successful argument needs graph structure (blocks, degree sequence, or a
   variational injection), not merely \(\operatorname{tr}Q=2m\).

2. **Tree bottleneck.** For a tree, bipartiteness makes \(Q\) similar to the
   ordinary Laplacian and (5) becomes
   \[
       2a+z\le n-1.                                                  \tag{9}
   \]
   Equivalently, the number above 2 must not exceed the number strictly
   between 0 and 2.  Paths and stars satisfy this, but no proof of (9) for all
   trees is supplied here.  Any attempted induction by deleting a leaf must
   control crossings through the exact threshold 2; ordinary Cauchy
   interlacing alone loses precisely the information represented by \(z\).

3. **Pendant-edge/Schur route.** Adding a pendant edge to \(G\) adds one
   vertex to \(L(G)\), adjacent to the clique of old edges incident with the
   attachment vertex.  The adjacency matrix has block form
   \(\begin{psmallmatrix}A&x\\x^{\mathsf T}&0\end{psmallmatrix}\).
   A scalar Schur complement would be attractive, but it requires invertible
   \(A\); singular line-graph adjacency matrices occur abundantly (e.g. odd
   paths).  A valid proof needs a generalized-inverse/nullspace case split.

4. **Block decomposition route.** At a cut vertex of \(G\), the corresponding
   line graph pieces are coupled through a clique, not by a one-vertex sum.
   Therefore adjacency signature is not simply additive over blocks.  Any
   claimed block induction must explicitly calculate this clique coupling.

5. **Disproof pressure test.** Identity (4) says a counterexample must have an
   unusually large population of \(Q\)-eigenvalues above/equal to 2 relative
   to its edge count.  At order 9 it must have at most 14 edges by the theorem.
   This does not rule one out.  In particular, absence in random floating
   point screening would give no control over the equality count \(z\) and is
   not a proof.

## 5. Claims safe to export

The incidence identity (1), spectral transfer (2), signature formula (4),
equivalent criterion (5), dense theorem (6), and benchmark-family
calculations are proved from definitions in this note.  They require no
external citation for correctness, though a manuscript should check whether
the threshold formulation or dense corollary already appears in the line
graph/signless-Laplacian literature before making a novelty claim.

The general conjecture is **not proved** here.  The sharp unresolved core is
the sparse range, already including the all-tree assertion (9).
