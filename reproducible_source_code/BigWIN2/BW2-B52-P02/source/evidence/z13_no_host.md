# Exact exclusion of the order-13 host

Fix a corner (c) of (P_3\square P_4).  If an induced embedding into
(\mathbb Z_{13}) exists, translate it so that (f(c)=0).  Its image has 12
elements, so it is (A=\mathbb Z_{13}\setminus\{r\}) for one
(r\in\{1,\ldots,12\}).

Every symmetric connection set in (\mathbb Z_{13}\setminus\{0\}) is uniquely
specified by a subset of the six sign-pairs
(\{\pm1\},\ldots,\{\pm6\}).  Thus there are exactly
(12\cdot 2^6=768) corner-normalized pairs ((A,S)).  This also covers the
difference-separation formulation: if an injection has
(D_E\cap D_{\bar E}=\varnothing), then (S=D_E) makes its image-induced
Cayley subgraph exactly the grid; conversely such an induced Cayley subgraph
gives the separation.

There is a direct obstruction in every one of the 768 cases.  The full Cayley
graph (\operatorname{Cay}(\mathbb Z_{13},S)) is regular, say of degree (d).
Deleting the sole omitted vertex (r) leaves each surviving vertex with degree
either (d) or (d-1).  Its induced subgraph therefore has at most two degree
values, and their difference is at most one.  But (P_3\square P_4) has degree
multiset

\[
\{2^4,3^6,4^2\},
\]

which has three values and range two.  Hence no induced embedding into
(\mathbb Z_{13}) exists.  Since this is the unique abelian group of order 13,
the certified lower bound improves to
(\eta(P_3\square P_4)\ge 14).

`z13_exact_search.py` independently enumerates all 768 normalized pairs with
exact integer arithmetic, checks the deletion-degree formula at all 9,216
surviving vertices, and finds zero candidates with the target degree multiset.
Its deterministic output is recorded in `z13_exact_search.json`.
