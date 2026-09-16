# Formal statement

## Universal conjecture

For every finite, undirected, simple, connected graph (G=(V,E)), let
(L(G)) be its ordinary line graph.  Thus (V(L(G))=E(G)), and two distinct
edges of (G) are adjacent in (L(G)) exactly when they share an endpoint.
For a real symmetric matrix (A), let (n_+(A),n_0(A),n_-(A)) count its
positive, zero and negative eigenvalues, with algebraic multiplicity.  Put

\[
s(L(G))=n_+(A(L(G)))-n_-(A(L(G))),\qquad
c(G)=|E|-|V|+1.
\]

The conjecture is

\[
2s(L(G))\le c(G)+1.
\]

Zero eigenvalues do not contribute.  Equivalently,

\[
s(L(G))\le \left\lfloor\frac{c(G)+1}{2}\right\rfloor.
\]

## Finite theorem sought here

Prove or disprove the same assertion under the additional exact condition
(|V(G)|=9), by traversing exactly one representative of every isomorphism
class.  "Order nine" refers to the order of the root graph (G), not the
order (|E(G)|) of its line graph.  The standard universe has 261,080
connected simple isomorphism classes.

## Exact computational formulation

Let (B) be the unsigned incidence matrix and (Q=BB^{\mathsf T}=D+A).
Since (B^{\mathsf T}B=A(L(G))+2I), exact spectral bookkeeping gives

\[
s(L(G))=\operatorname{sig}(Q-2I)-c(G)+1.
\]

The correction term is mandatory, including for bipartite graphs.  The census
uses exact rational congruence inertia on (Q-2I), with an independent exact
integer-characteristic-polynomial/Sturm verifier.

## Edge cases and scope

The one-vertex connected graph has an empty line graph and signature zero, so
it is harmless in the universal formulation.  Loops, parallel edges, signed
edges, directed graphs and disconnected graphs are outside the quantified
class.  A certified order-nine result is finite and does not prove the
universal conjecture.
