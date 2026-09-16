# Frozen source problem: the order-17 common-neighbor gap

Canonical id: `win-00083-p01`  
Frozen on: 2026-09-09 (Asia/Shanghai)  
Primary source: Ascolese--Negrini--Pagani--Pellegrini,
arXiv:2609.08803v1, Lemma 3.1, Corollary 5.8, Theorem 5.9, and the
conjectural sentence immediately following Corollary 5.8.  
Local source copy: `batches/inbox/bigWin-83-materials/2609.08803.pdf`,
SHA-256 `b38417ec4dcdbc7515207120346edf99e7285c31a49e6c215ed949034e76bbf9`.

## Statement

Prove or disprove the following exact nonexistence assertion.

> There is no finite simple undirected graph `G` with `|V(G)|=17` such that
> for every two distinct vertices `x,y`,
> `|N_G(x) intersect N_G(y)| <= 1`, and
> `sum_{u in V(G)} binom(deg_G(u),2) = 123`.

The pairwise-codegree condition is equivalent to `C4`-freeness. Under that
condition the displayed sum counts precisely the 123 unordered vertex pairs
having one common neighbor; the remaining 13 pairs have none. In the source
notation the assertion is equivalent to non-realizability of
`gamma_123=(1^123,0^13)` by a graph in `Q_17`.

## Scope and contribution boundary

The source proves the nonexistence only for planar graphs. Any arbitrary
counterexample is reduced by Corollary 5.8 to a connected nonplanar graph with
`5 <= Delta(G) <= 9`; the authors conjecture that this case does not occur and
their reported verification stops at order 16. The project must not cite the
planar theorem as resolving the frozen assertion. A complete proof needs a
human-checkable reduction and/or independently checked exact finite certificate;
a bare SAT/ILP solver result is insufficient.

This file is immutable. Any later repaired or restricted claim must be written
separately and must not be presented as solving this source statement.

