# Exact exclusion of every order-14 host

Let (X) be any regular graph on 14 vertices, of degree (d), and suppose
that deleting two vertices leaves an induced copy of
(P_3\square P_4).  Every surviving vertex loses between zero and two
neighbors.  Hence every degree in the induced subgraph lies between (d-2)
and (d).  The grid has minimum degree 2 and maximum degree 4, so its maximum
degree gives (d\geq4), while its minimum degree gives (d\leq4).  Thus
(d=4).

The full graph (X) then has (14d/2=28) edges.  Deleting two vertices
removes at most (2d=8) edges (in fact only 7 if the deleted vertices are
adjacent).  The surviving induced subgraph therefore has at least 20 edges.
But (P_3\square P_4) has exactly 17 edges, a contradiction.

Every Cayley graph is regular.  An induced embedding of the 12-vertex grid in
an order-14 Cayley graph would have an image obtained by deleting two host
vertices, so the obstruction applies to every group and every connection set.
In particular, it excludes the only abelian group of order 14,
(\mathbb Z_{14}).  Together with the previously certified order-13
exclusion, this proves

\[
  \eta(P_3\square P_4)\geq15.
\]

As a reproducible check, `z14_exact_search.py` translates a fixed grid corner
to 0 and enumerates all \(\binom{13}{2}=78\) possible omitted pairs and all
\(2^7=128\) symmetric connection sets in \(\mathbb Z_{14}\), exactly 9,984
normalized candidates.  Exact integer degree filtering rejects all of them;
therefore no fixed-corner isomorphism backtracking is reached.  The output is
stored in `z14_exact_search.json`.
