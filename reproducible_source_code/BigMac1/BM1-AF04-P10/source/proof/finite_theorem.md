# Certified finite theorem: radius-seven exchange rigidity

## Objects and quantifiers

Let \(V=\mathbb F_2^7\).  Let
\(C_0=(P_0,\ldots,P_{332})\) be the 333 three-dimensional subspaces
reconstructed from Appendix C of Heinlein--Kiermaier--Kurz--Wassermann
(DOI `10.3934/amc.2019029`) using the serialized generators and representatives
in `data/appendix_c_333.json`.  Indices below refer to the verifier's canonical
ordering, by increasing membership fingerprint.

For an ambient subspace \(X\notin C_0\), define its blocker set

\[
B(X)=\{i\in\{0,\ldots,332\}:d_S(X,P_i)<4\}.
\]

For \(r\ge0\), the radius-\(r\) exchange family consists of every code of the
form

\[
(C_0\setminus\{P_i:i\in R\})\cup A,
\]

where \(R\subseteq\{0,\ldots,332\}\), \(|R|\le r\), and \(A\) is an arbitrary
set of subspaces in the full ambient Grassmann lattice outside \(C_0\).  The
only condition on the assembled family is minimum subspace distance at least
four.  Thus additions of every dimension \(0,\ldots,7\) are included.

## Normalization lemma

**Lemma.** If an exchange \((C_0\setminus R)\cup A\) is feasible, then

\[
R'=\bigcup_{X\in A}B(X)\subseteq R
\]

and \((C_0\setminus R')\cup A\) is feasible and has cardinality at least that
of the original exchange.

**Proof.** Feasibility with each retained plane says exactly that
\(B(X)\subseteq R\) for every \(X\in A\), hence \(R'\subseteq R\).  Every plane
restored from \(R\setminus R'\) is at distance at least four from every member
of \(A\); pairwise distances inside \(C_0\) and inside \(A\) were already
valid.  Restoring these planes therefore preserves feasibility and cannot
decrease cardinality. \(\square\)

Consequently, to maximize within radius \(r\), it suffices to enumerate the
sets \(R\) that are unions of blocker sets and satisfy \(|R|\le r\).  A
candidate with \(|B(X)|>r\) cannot occur.  For an enumerated \(R\), let

\[
E_R=\{X\notin C_0:B(X)\subseteq R\}.
\]

If \(G_R\) is the compatibility graph on \(E_R\), the exact optimum associated
with \(R\) is

\[
333-|R|+\omega(G_R).
\]

## Theorem

**Theorem.** Among all radius-seven exchanges around \(C_0\), the maximum
cardinality is 334.  In particular, no code of size 335 can be obtained by
deleting at most seven planes of \(C_0\) and adding arbitrary mutually
compatible subspaces of arbitrary dimensions.

**Exact finite proof.** The independent verifier reconstructs all 333 planes
from the two group generators and 103 Appendix C orbit representatives.  It
then enumerates all 29,212 subspaces of \(V\) in RREF and recomputes distance as

\[
d_S(U,W)=2\operatorname{rank}(U+W)-\dim U-\dim W.
\]

There are 14,146 outside candidates having at most seven blockers and 14,140
distinct blocker sets among them.  An exact closure under union produces all
2,561,563 normalized removal sets of size at most seven.  For every such set,
the eligible graph has at most 15 vertices.  The verifier exhausts every one
of its at most \(2^{15}\) vertex subsets and hence evaluates \(\omega(G_R)\)
without floating point or solver trust.  The maxima for \(|R|=0,\ldots,7\) are

\[
334,333,333,333,334,333,333,333.
\]

Their overall maximum is 334.  It is attained for \(R=\varnothing\) by adding
the full space \(V\).  The normalization lemma transfers the exhaustive result
from normalized removal sets to all removal sets of size at most seven.
\(\square\)

## Scope

This theorem is a complete finite result for one precisely specified exchange
neighborhood.  It is not a global upper bound on \(A_2(7,4)\), does not exclude
a 335-word code elsewhere in the 29,212-vertex compatibility graph, and does
not independently reproduce the published SDP upper bound 388.  The dated
global frontier therefore remains \(334\le A_2(7,4)\le388\).
