# Immutable source — win-00052-p02

## Original lead

Determine the first rectangular path-grid value not evaluated exactly in the source.

## Precise frozen statement for triage

Let `G=P_3 square P_4`, the Cartesian product of paths on three and four vertices. With induced Abelian Cayley embedding and `eta` defined exactly as in `win-00052-p01`, determine `eta(G)`.

The product construction gives `eta(G)<=eta(P_3)eta(P_4)=4*5=20`. A resolution must give an exact host certificate at the claimed order and a complete lower certificate for every smaller finite Abelian group order not already excluded by a theorem. Numerical heuristics or a single cyclic-group search do not settle the statement.

## Primary source and delta

- J. A. Noel and J. A. Scott, *Induced Embeddings of Graphs into Abelian Cayley Graphs*, arXiv:2609.01486v1, Theorem 14, Corollary 15, Table 1, and Problem 2: https://arxiv.org/abs/2609.01486v1
- Local PDF: `batches/inbox/bigWin-52-materials/2609.01486.pdf`
- SHA-256: `225f0354c45ac9babe9f7f2e30134abcc17454fa284f089fd58a182424262844`
- Retrieved 2026-09-07.

The source verifies only its order-20 construction for this graph and reports an exact value only for `P_3 square P_3`. This is a fixed next rectangular cell. If p01 and p02 both succeed by the same machinery, combine their mathematical contribution at writing/release rather than padding two papers.
