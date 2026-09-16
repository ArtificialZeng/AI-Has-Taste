# Mathematical referee report

## Frozen scope and verdict

I reviewed the frozen `resolution-paper` claim that, for the definition in
`problem.md`,

\[
\eta(P_3\square P_4)=19,
\]

with the displayed embedding in \(\mathbb Z_{19}\) and nonexistence in every
finite Abelian group of order at most 18.  All files named by
`audit/snapshot.json` have the recorded SHA-256 digests.  The candidate proves
the exact frozen statement, and my verdict is **accept**.

## Reconstruction of the upper certificate

Let

\[
f(i,j)=-i-4j\pmod {19},\qquad S=\{1,4,15,18\}=\{\pm1,\pm4\}.
\]

The twelve integer expressions \(-i-4j\), with \(0\leq i\leq2\) and
\(0\leq j\leq3\), are distinct modulo 19: the difference of two such
expressions has absolute value at most 14, and an equality
\(\Delta i+4\Delta j=0\) forces first \(\Delta j=0\) and then
\(\Delta i=0\).  A grid edge changing the first coordinate has difference
\(\pm1\), and one changing the second coordinate has difference \(\pm4\).
Conversely, within the same bounded difference range, a residue in
\(\{\pm1,\pm4\}\) has integer representative \(\pm1\) or \(\pm4\).
Checking \(|\Delta i|\leq2\), \(|\Delta j|\leq3\) shows that these values occur
only for \((|\Delta i|,|\Delta j|)=(1,0)\) or \((0,1)\).  Thus no nonedge is
a Cayley edge.

As a separate exact check, I reran `order19_certificate.py`.  It verified all
66 unordered pairs, comprising 17 edges and 49 nonedges, and returned signed
edge differences \(\{1,4,15,18\}\) disjoint from the signed nonedge
differences.  This proves the upper bound 19 without relying on the exhaustive
search that originally found the labelling.

## Reconstruction of the lower bound

Orders below 12 are excluded by injectivity.  At order 12 an injection is a
bijection onto the Cayley host, but every Cayley graph is regular whereas the
grid has degree multiset

\[
(2^4,3^6,4^2).
\]

The direct deletion arguments for the next three orders are sound.  Deleting
one vertex from a regular order-13 graph leaves degrees in two consecutive
values, so it cannot yield the three grid degrees 2, 3, and 4.  At order 14,
deleting two vertices from a \(d\)-regular graph and observing degrees 2 and 4
forces \(d=4\); the 28-edge host then retains at least 20 edges, not 17.  At
order 15, the same degree range forces \(d\in\{4,5\}\).  The handshake lemma
excludes \(d=5\), while deleting three vertices from a 4-regular 30-edge host
leaves at least 18 edges.  These arguments cover arbitrary regular graphs and
hence all Cayley hosts at those orders.

For orders 16--18, let \(d=|S|\), let \(U\) be the omitted set of
\(k=n-12\) vertices, and let \(e(U)\) count its internal host edges.  The
retained edge count is

\[
17=\frac{nd}{2}-kd+e(U).
\]

Since deletion cannot increase degree and the target has maximum degree 4,
\(d\geq4\).  At order 16 the equation is \(17=4d+e(U)\), forcing
\((d,e(U))=(4,1)\).  At order 17 it is
\(17=7d/2+e(U)\); because an inverse-closed subset of a group of odd order is
a union of two-element inverse orbits, \(d\) is even, forcing \((4,3)\).  At
order 18 it is \(17=3d+e(U)\), forcing \((4,5)\) or \((5,2)\).  Thus the
enumerators omit no possible host degree.

The finite Abelian group lists are complete: the five order-16 types are
\(\mathbb Z_{16}\), \(\mathbb Z_2\times\mathbb Z_8\),
\(\mathbb Z_4^2\), \(\mathbb Z_2^2\times\mathbb Z_4\), and
\(\mathbb Z_2^4\); order 17 has only \(\mathbb Z_{17}\); and the two
order-18 types are \(\mathbb Z_{18}\) and
\(\mathbb Z_3\times\mathbb Z_6\).

The computational normalization is also complete.  Translating the label of
the fixed grid corner to the identity preserves every difference.  The scripts
therefore enumerate every omitted subset avoiding the identity and every
inverse-closed connection set of the forced size by taking unions of all
negation orbits.  For each surviving image, the final backtracking maps every
grid vertex bijectively to an image vertex, fixes the chosen corner at the
identity, and rejects a branch only on a degree mismatch or an exact
adjacency/nonadjacency mismatch against an assigned vertex.  Hence a genuine
rooted isomorphism cannot be pruned.

I reran the supplied exact searches.  Their numerical records reproduced; the
only byte-level differences from the frozen JSON files were JSON whitespace.
The order-16 run tested 2,152,605 normalized pairs and performed rooted
isomorphism checks in counts 1,184, 2,016, 2,880, 10,752, and 120,960 for the
five group types.  The order-17 run performed 3,552 such checks.  The two
order-18 types performed 5,172 and 5,856 checks.  All returned zero
isomorphisms.

To audit the most decisive routine by a different implementation, I replaced
the supplied backtracker during fresh reruns with NetworkX 3.4.2's rooted
`GraphMatcher`, marking the grid corner and group identity as the unique root.
Using the same fully enumerated candidate sets, this independent isomorphism
test again returned zero in every one of the five order-16 types, the
order-17 type, and both order-18 types, with the same numbers of terminal
checks.  This cross-check addresses the principal risk of a false negative in
the custom isomorphism search.

## Source comparison and contribution

The snapshotted arXiv PDF gives the induced-embedding definition and the exact
difference-separation criterion used here.  Its Theorem 14 and Corollary 15
give the product construction, and the paragraph following Corollary 15 says
that the order-20 construction for \(P_3\square P_4\) was verified.  The same
passage and Table 1 state the adjacent exact value
\(\eta(P_3\square P_3)=15\), but do not state an exact value for the present
rectangle.  Therefore the order-19 construction plus the complete lower
certificate is the precise delta claimed in `claim.json`, and it resolves the
original frozen task over all finite Abelian groups rather than only cyclic
ones.  The author-attribution correction recorded in `problem.md` agrees with
the PDF and does not affect the mathematics.

No mathematical gap remains in the frozen scope.  This review does not assert
priority beyond the bounded source comparison, consistently with the claim's
own limitation.
