# Precise problem reading

## Frozen claim

The immutable original statement is `source.md` (SHA-256
`e0696f682554b3b51d04c3ce8601d9778a1a30a06b2cb7de02681361f21db681`).
Its mathematical claim is read as follows.

For every finite undirected graph \(H=(V,E)\) and every ordered pair
\((s,t)\in V^2\) with \(s\ne t\), if

1. \(H\) is simple and connected;
2. \(|V|=12\);
3. \(\deg_H(s)=\deg_H(t)=2\), while \(\deg_H(v)=3\) for every
   \(v\in V\setminus\{s,t\}\); and
4. \(\operatorname{dist}_H(s,t)\ge 3\), where distance is the number of
   edges in a shortest path,

then \(H\) contains a simple cycle with exactly 4 vertices or a simple cycle
with exactly 8 vertices. A simple \(k\)-cycle is a cyclic sequence of \(k\)
distinct vertices whose consecutive pairs, including the last-first pair, are
edges of \(H\).

The terminals are treated as ordered for rooted-isomorphism reporting:
\((H,s,t)\cong(H',s',t')\) means there is a graph isomorphism sending \(s\)
to \(s'\) and \(t\) to \(t'\). The truth of the cycle claim is invariant under
swapping the terminals, so the finite search may process each undirected edge
once. If counterexamples were found, both orientations would have to be
accounted for when forming ordered-rooted classes. An unordered-terminal
convention would change only that classification convention, not the claim or
the certificate of cycle existence.

## Exact cubic reformulation and coverage

Given an admissible \((H,s,t)\), condition 4 implies \(st\notin E(H)\).
Adding \(st\) therefore produces a connected simple cubic graph \(G\) on 12
vertices. Mark the added edge \(e=\{s,t\}\). Conversely, for a connected
simple cubic graph \(G\) on 12 vertices and an edge \(e=\{s,t\}\), deleting
\(e\) gives the required degree sequence. It is admissible exactly when
\(G-e\) is connected and \(\operatorname{dist}_{G-e}(s,t)\ge3\). These two
operations are inverse on labeled objects and hence also give complete
coverage up to rooted isomorphism. Thus the claim is equivalently:

> For every connected simple cubic \(G\) on 12 vertices and every edge
> \(e=\{s,t\}\) for which \(G-e\) is connected and the endpoints have distance
> at least 3 in \(G-e\), the graph \(G-e\) contains a \(C_4\) or a \(C_8\).

The requested successful output is not merely a count. If the claim is true,
it is a complete replayable certificate that covers every eligible census-edge
pair and supplies a valid cycle in the deletion graph (the source requests the
lexicographically least one). If false, it is a complete list of ordered-rooted
counterexample classes, each with graph6 data and explicit terminal labels.

## Prior result, proposed delta, and status

Nearest prior result: Daniel Garcia, *Small graphs without power-of-two cycles:
a lower bound of 24, a correction to a construction of Exoo, and explicit
bounds for f(k)*, arXiv:2609.04686v1 (submitted 2026-09-04), Proposition
6.2(2), treats two-attachment gadgets of orders 4, 6, and 8 and excludes a
\(C_4/C_8\)-free order-10 gadget whose terminals have distance at least 3.
The paper does not state the order-12 case. Its Definition 3.1 formalizes the
related attachment-gadget framework. The broad theorem in its abstract for
graphs of minimum degree at least 3 does not directly settle this claim because
\(H\) has two degree-2 vertices; after adding \(st\), a guaranteed \(C_4\) or
\(C_8\) in \(G\) might use the added edge and hence cease to be a cycle in
\(H\).

Proposed delta: decide and completely certify the order-12 two-attachment case,
including the source's requested counterexample classification if necessary.
Verification route: use the add/delete-edge bijection, Meringer's complete
census of 85 connected simple cubic graphs on 12 vertices, an exact per-edge
cycle-witness verifier, and preferably an independently constructed SAT/UNSAT
cross-check.

Source status is **new-question / status-uncertain**, not “verified open.” A
targeted search on 2026-09-07 for the exact gadget assertion and the equivalent
cubic edge-deletion formulation found no primary result beyond Garcia's
order-10 statement. This is only a literature screen, not a priority claim.

## Inspected primary and authoritative sources

- Garcia, arXiv:2609.04686v1, especially Definition 3.1 and Proposition
  6.2(2): <https://arxiv.org/abs/2609.04686>. Retrieved 2026-09-07. The local
  PDF SHA-256 is
  `0ab4267dc8b9de8abb3c3868385a2afad9fb8f08614836297581a4ee03ab77f8`,
  matching `source.md`; the official supplement hash also matches the stated
  `5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4`.
- Markus Meringer's official connected-regular-graph registry:
  <https://www.mathe2.uni-bayreuth.de/markus/reggraphs.html> and the order-12
  cubic page <https://mathe2.uni-bayreuth.de/markus/REGGRAPHS/12_3_3.html>.
  Retrieved 2026-09-07. The registry reports 85 connected cubic graphs on 12
  vertices and cites M. Meringer, “Fast Generation of Regular Graphs and
  Construction of Cages,” *Journal of Graph Theory* 30 (1999), 137–146. The
  supplied adjacency census has the stated SHA-256
  `f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7`.
