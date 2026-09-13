# Precise problem statement

## Frozen reading

Throughout, a graph is finite, simple, undirected, and not necessarily
connected.  Graphs are identified up to graph isomorphism.  The frozen target
concerns graphs on exactly eight vertices; no assertion is made here about the
nonregular order-eight example mentioned in the source.

Let \(G=(V,E)\), with \(|V|=8\), and let \(N_G(v)\) be the open neighborhood of
\(v\).  The graph is **regular ordinary distance-magic** if there are an integer
\(k\), a bijection
\[
  \ell:V\longrightarrow\{1,2,\ldots,8\},
\]
and an integer \(c\) such that every vertex has degree \(k\) and
\[
  \sum_{u\in N_G(v)}\ell(u)=c\qquad(\forall v\in V).
\]
The frozen wording permits \(k=0\) and \(c=0\); it imposes neither
connectedness nor positive degree.  Double-counting gives
\(8c=k(1+\cdots+8)=36k\), hence \(c=9k/2\).  Consequently only
\(k\in\{0,2,4,6\}\) can occur (a regular ordinary distance-magic graph cannot
have odd degree).

Fix
\[
  \Gamma=(\mathbb Z/2\mathbb Z)^3=\mathbb F_2^3.
\]
A **generating \(\Gamma\)-magic map** on \(G\) is a function
\(f:V\to\Gamma\) for which there is a \(\gamma\in\Gamma\) satisfying
\[
  \sum_{u\in N_G(v)}f(u)=\gamma\qquad(\forall v\in V)
\]
and
\[
  \langle f(v):v\in V\rangle=\Gamma.
\]
Here sums are in \(\Gamma\), and generation is equivalently linear spanning
over \(\mathbb F_2\).  The map \(f\) need not be injective or bijective, its
image need not have eight elements, and affine generation by label differences
is not required.

## Quantified assertion and requested classification

Let \(\mathcal C\) be the set of isomorphism classes of regular ordinary
distance-magic graphs on eight vertices.  For \([G]\in\mathcal C\), set
\(P(G)\) to mean that \(G\) has a generating \(\Gamma\)-magic map as defined
above.  The exact universal assertion under test is
\[
  \boxed{\quad \forall [G]\in\mathcal C,\;P(G).\quad}
\]
Equivalently, the requested classification partitions
\(\mathcal C=\mathcal C_+\sqcup\mathcal C_-\), where \(P(G)\) holds precisely
on \(\mathcal C_+\).  Under the completion rule frozen in `source.md`, a
positive resolution must enumerate all of \(\mathcal C\), exhibit and verify
an ordinary distance-magic labeling for every listed class, certify unlabeled
isomorphism coverage, and prove \(P(G)\) for every class.  A negative resolution
of the universal assertion may instead consist of one \(G\in\mathcal C_-\), an
ordinary distance-magic labeling of it, and an exact certificate that \(P(G)\)
fails.  Finding one negative graph resolves the universal assertion but is not,
by itself, a full listing of every member of both parts of the partition.

## Exact modular reformulation

Let \(A\) be the adjacency operator on \(\mathbb F_2^V\), let \({\bf 1}\) be
the all-one vector, and put
\[
  Q_G=\mathbb F_2^V/\langle{\bf 1}\rangle.
\]
Regularity makes \(\langle{\bf 1}\rangle\) invariant under \(A\), so \(A\)
induces the reduced adjacency operator
\[
  \overline A_2:Q_G\longrightarrow Q_G,\qquad [x]\longmapsto[Ax].
\]
For \(\Gamma\cong(\mathbb Z/2\mathbb Z)^3\), the group \(B_\Gamma\) in
Theorem 1.2 of the cited paper is \((\mathbb Z/2\mathbb Z)^2\).  Therefore
\[
  P(G)
  \iff \mathbb F_2^2\hookrightarrow\ker\overline A_2
  \iff \dim_{\mathbb F_2}\ker\overline A_2\ge 2.
\]
All rank and nullity claims in a resolution are thus exact finite-field claims,
not floating-point computations.  Since \(\dim Q_G=7\), failure means reduced
nullity at most one (equivalently reduced rank at least six).

## Source boundary and triage status

The mathematical source is arXiv:2609.05934v1, retrieved 2026-09-09.  Its
Theorem 1.2 supplies the modular equivalence above; Conjecture 4.4 is the
general generating-group assertion; Theorem 4.6 covers regular distance-magic
graphs only when the labeling group has at most two generators; and Corollary
4.7 covers cube-free graph order.  Neither latter result covers
\(|V|=8\) with \(\Gamma=\mathbb F_2^3\).

There is a bibliographic error in the immutable source statement, not a change
to its mathematics: both the local PDF with the recorded SHA-256 and the arXiv
record identify the paper as Ahmet Batal, *Algebraic characterizations of
generating and affinely generating \(\Gamma\)-magic maps and \(\Gamma\)-distance
magic labelings on regular graphs*, rather than the author and title written in
`source.md`.  The numbered results and quoted criterion agree with the actual
paper.  A limited exact-phrase/order-eight search found no primary source giving
the requested eight-vertex classification; this leaves prior-result and novelty
status uncertain rather than establishing openness or priority.

The target is suitable for bounded exact research.  The installed `geng`
generator reports 1, 3, 6, and 1 unlabeled regular graphs of order eight in
degrees 0, 2, 4, and 6 respectively.  Thus only eleven degree-feasible
isomorphism classes require screening, and each can be checked by exhaustive
enumeration of the \(8!\) ordinary labelings followed by exact row reduction of
\(\overline A_2\).
