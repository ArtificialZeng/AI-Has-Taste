# Exact exclusion of every order-15 host

Let (X) be any (d)-regular graph on 15 vertices.  If deleting three
vertices leaves an induced copy of (P_3\square P_4), then every surviving
degree lies between (d-3) and (d).  Since the grid has minimum degree 2
and maximum degree 4, necessarily

\[
  4\leq d\leq5.
\]

The case (d=5) is impossible by the handshake lemma, because (15d) is
odd.  If (d=4), the full graph has (15d/2=30) edges.  Deleting three
vertices removes at most (3d=12) edges, so the induced subgraph on the
remaining 12 vertices has at least 18 edges.  The grid has only 17 edges,
again a contradiction.

Every Cayley graph is regular.  Consequently no induced embedding exists in
any Cayley graph of order 15, in particular not in the sole abelian group
(\mathbb Z_{15}).  Combining this with the certified exclusions at orders
13 and 14 gives

\[
  \eta(P_3\square P_4)\geq16.
\]

This is a direct proof; it does not rely on an incomplete computational
prefix.
