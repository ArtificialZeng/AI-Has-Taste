# Precise reading

## Frozen target

The immutable source statement is `source.md`.  The graph in question is

\[
H=K_{1,3}\sqcup K_2,
\]

on six distinct vertices.  Label the claw centre (a), its leaves (b,c,d),
and the separate edge endpoints (e,f); thus
(E(H)=\{ab,ac,ad,ef\}).

Let \(\mathcal K_{\mathrm{MP}}\) be the family used in Definition 1 of
arXiv:2609.05268v1: finite simple maximal planar graphs.  Here “maximal
planar” is read as edge-maximal among simple planar graphs (equivalently, for
orders at least three, a plane triangulation after choosing an embedding).
For (G\in\mathcal K_{\mathrm{MP}}), a red-blue edge-colouring is a map
(\chi:E(G)\to\{R,B\}).

A monochromatic copy of (H) means an ordinary, not necessarily induced,
subgraph copy: there are a colour (q\in\{R,B\}) and an injection
(\phi:V(H)\to V(G)) such that every image of an edge of (H) is an edge of
(G) coloured (q).  Extra host edges, of either colour, among the six image
vertices do not invalidate the copy.  In particular, “disjoint union” requires
the claw and the extra edge to be vertex-disjoint; it does not require them to
be anticomplete in the host.

For an integer (N), define (P(N)) to be the assertion

\[
\begin{split}
&\text{for every integer }n\ge N,\text{ every }G\in\mathcal K_{\mathrm{MP}}
\text{ with }|V(G)|=n,\\
&\text{and every }\chi:E(G)\to\{R,B\},\text{ there is a monochromatic
subgraph copy of }H.
\end{split}
\]

The question is whether \(\{N\in\mathbb Z:P(N)\}\) is nonempty.  If it is,

\[
r_{\mathrm{MP}}(H,H)=\min\{N:P(N)\},
\]

and a solution must prove (P(r_{\mathrm{MP}}(H,H))), hence cover every
larger order.  Necessarily any such threshold is at least 6.  If the set is
empty, a disproof must give an explicit, mechanically verifiable sequence
((G_t,\chi_t)) with each (G_t\in\mathcal K_{\mathrm{MP}}),
(|V(G_t)|\to\infty), and neither colour graph containing (H).  One finite
avoiding colouring is only a lower bound.

## Required structural reduction

For any finite simple graph (F), the following criterion is exact:

> (F) is (H)-free if and only if either (\Delta(F)\le2), or, for every
> chosen subgraph claw (C\cong K_{1,3}) in (F), the four vertices (V(C))
> form a vertex cover of (F).

Indeed, if (F) is (H)-free and (C) is a claw, an edge disjoint from
(V(C)) would combine with (C) to form (H).  Conversely, a copy of (H)
is exactly a claw together with an edge disjoint from its four vertices.  A
vertex of degree at least three supplies a (not necessarily induced) claw by
choosing any three neighbours.

Consequently, in an avoiding colouring each colour graph has one of two
types:

- type L: maximum degree at most 2;
- type C: maximum degree at least 3, and the vertices of any chosen claw form
  a four-vertex cover of all edges of that colour.

This gives the four cases LL, LC, CL, and CC (with LC and CL equivalent after
swapping colours).  The LL case is impossible for every maximal planar graph
of order (n\ge7): each type-L colour graph has at most (n) edges, whereas
a simple maximal planar graph has (3n-6>2n) edges.  Thus research need only
attack the mixed case and the CC case (plus order (n=6) when determining an
exact finite threshold).

## Scope and prior-result boundary

The cited paper is Adriana Baldacchino, Yair Caro, and Xandru Mifsud,
“Ramsey properties of maximal (outer)planar graphs,” arXiv:2609.05268v1
(2026).  Its publicly indexed abstract, inspected 2026-09-07, states a
classification only for **connected** graphs in the diagonal maximal-planar
case.  Since (H=K_{1,3}\sqcup K_2) is disconnected, that advertised theorem
does not settle this target.  The exact singleton is treated here only as a
source-grounded refinement of the paper's broader Problem 2, not as a problem
that the authors explicitly declared open.

The source-designated PDF has now been verified against the requested SHA-256
and copied to `evidence/external/2609.05268.pdf`.  Definition 1 confirms the
at-least-\(N\) convention.  Corollary 2 settles \(K_{1,3}\) alone, not the
disjoint union here.  Proposition 4 supplies necessary forest/component/
diameter conditions which this \(H\) passes.  Theorem 11 and Remark 5 settle
subgraphs of \(P_5\sqcup tK_2\), a class not containing this degree-three
\(H\).  Section 5, Problem 2 asks for the complete disconnected diagonal MP
classification but does not single out this graph.  The source status remains
**new-question** and the exact external resolution status remains
**status-uncertain**; no priority claim is made.

## Triage target

Nearest verified prior boundary: the cited paper's full connected diagonal
classification and its broader disconnected Problem 2.  Both explicit
infinite MP colourings in Section 4.1 fail for the present \(H\); exact
witnesses are recorded in `evidence/upper-bound.md`.  The LC/CC reduction now
also proves \(r_{\mathrm{MP}}(H,H)\le21\), but the least threshold remains to
be determined.
