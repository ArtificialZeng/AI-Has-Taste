# Formal statement

## Objects and quantifiers

Let \(X=\{0,1,\ldots,14\}\).  A labelled Steiner triple system of order
15 is a set \(B\subseteq\binom X3\) such that

\[
  \forall p\in\binom X2\quad
  \bigl|\{A\in B:p\subseteq A\}\bigr|=1.
\]

It follows (and is also checked in every certificate) that \(|B|=35\).
Two labelled systems \(B,B'\) are isomorphic when some permutation
\(\pi\in S_{15}\) satisfies \(B'=\{\pi(A):A\in B\}\).  Write \([B]\) for
the isomorphism class of \(B\), and let \(\mathcal S_{15}\) be the set of
all such classes.

Six symbols \(a,b,c,d,e,f\) used below are always required to be pairwise
distinct.  A Pasch configuration in \(B\) is the unordered four-block set

\[
 P=\{abc,ade,fbd,fce\}\subseteq B.
\]

Its mate is

\[
 P'=\{abd,ace,fbc,fde\},
\]

and the switch is \(B^P=(B\setminus P)\cup P'\).  The definition is
independent of the displayed parametrization of the same four-block
configuration.  The pair coverage of \(P\) and \(P'\) is identical, so
\(B^P\) is again an STS(15).

## Quotient graph

Define the finite undirected simple graph \(G=(V,E)\) by

\[
 V=\mathcal S_{15},\qquad
 \{[B],[C]\}\in E
 \iff [B]\ne[C]\text{ and }[C]=[B^P]
\]

for at least one Pasch configuration \(P\) in one (equivalently every)
representative \(B\) of the first class.  Isomorphic switches, loops, and
parallel occurrences are discarded when forming \(E\).

The diameter of a connected graph \(H\) is
\(\max_{u,v\in V(H)}d_H(u,v)\).  A one-vertex component has diameter zero.
No distance is assigned between vertices in different components.

## Canonical representatives used in the certificate

For a labelled system, form its bipartite incidence graph with 15 point
vertices (degree 7) and 35 block vertices (degree 3).  Its nauty canonical
graph (`labelg`, nauty 2.9.3) is an isomorphism invariant.  Order the 15
degree-7 vertices by their labels in that canonical graph, rename them
\(0,\ldots,14\), extract and sort the 35 incident triples, and call the
result the project canonical representative.  The released vertices are
sorted lexicographically by these 35-tuples and numbered `V000` through
`V079`.  Canonicalization is used only to construct identifiers; the
independent verifier proves validity, pairwise nonisomorphism, switch-edge
completeness, components, and distances without invoking nauty or trusting
canonical labels.

## Exact endpoint to determine

Determine \(|V|\), all connected components, every component diameter, and
in particular the exact diameter \(D\) of the nontrivial component.  A full
certificate must contain:

1. 80 explicit 35-block representatives;
2. the complete simple quotient edge list;
3. an eccentric pair \(u,v\) with a path of length \(D\);
4. a complete BFS distance row proving \(d(u,v)\ge D\), and all-pairs BFS
   proving no pair is farther apart;
5. a fail-closed verifier which reconstructs every switch adjacency from
   the representatives and rejects malformed or corrupted input.

## Degenerate and endpoint conventions

- Every Pasch uses exactly six distinct points and four distinct blocks.
- A switch whose output is isomorphic to its input contributes no simple
  edge, though its occurrence remains part of the completeness audit.
- Multiple configurations producing the same pair of isomorphism classes
  contribute one simple edge.
- The anti-Pasch condition means that the set of Pasch configurations is
  empty; it therefore forces isolation in \(G\).
- Completeness of the 80-vertex universe is a classification input that is
  separately cross-checked against the DesignTheory.org complete catalogue
  and the classical enumeration literature.
