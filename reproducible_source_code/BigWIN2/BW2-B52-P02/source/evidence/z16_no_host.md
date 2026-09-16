# Exact exclusion of every order-16 Abelian Cayley host

Let (X=\operatorname{Cay}(\Gamma,S)) have order 16 and degree
(d=|S|), and let (U) be the four vertices outside a putative induced
copy of (P_3\square P_4).  Write (e_X(U)) for the number of host edges
with both ends in (U).  Since deleting (U) removes
(4d-e_X(U)) edges, the 17-edge target would satisfy

\[
  17=\frac{16d}{2}-(4d-e_X(U))=4d+e_X(U).
\]

The target has maximum degree 4, hence (d\geq4).  The displayed equation
then forces (d=4) and (e_X(U)=1).  Thus it suffices to consider symmetric
connection sets of cardinality four and omitted quadruples spanning one edge.

`z16_exact_search.py` performs exactly this enumeration.  Translation sends a
fixed grid corner to the identity, so the omitted quadruple ranges over all
(\binom{15}{4}=1365) subsets of the nonidentity elements.  For each of the
five Abelian group types of order 16, the script constructs all inverse-orbits
and hence every inverse-closed four-element connection set.  Their respective
counts are 21, 33, 33, 125, and 1365 for

\[
 \mathbb Z_{16},\quad \mathbb Z_2\times\mathbb Z_8,\quad
 \mathbb Z_4^2,\quad \mathbb Z_2^2\times\mathbb Z_4,\quad
 \mathbb Z_2^4.
\]

It tests 2,152,605 normalized connection-set/omitted-set pairs.  After the
one-edge filter it compares the exact induced degree multiset with
((2^4,3^6,4^2)), requires the normalized identity to have corner degree two,
and runs a complete backtracking graph-isomorphism test constrained to fix that
corner.  There are respectively 1,184, 2,016, 2,880, 10,752, and 120,960 such
isomorphism checks, and none succeeds.  Full type-by-type counts are in
`z16_exact_search.json`.

The normalization is complete: translating any Cayley labeling by the negative
of the fixed corner label preserves every difference and sends that corner to
the identity.  The inverse-orbit enumeration is complete for every legitimate
undirected Cayley connection set of forced size four.  The backtracking test
assigns every grid vertex bijectively to an image vertex, rejects only on exact
degree or already-assigned adjacency/nonadjacency disagreement, and therefore
cannot reject an isomorphism.  Consequently no order-16 Abelian Cayley host
contains the target as an induced subgraph, and

\[
  \eta(P_3\square P_4)\geq17.
\]
