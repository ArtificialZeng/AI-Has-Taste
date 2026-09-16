# Immutable source — win-00052-p01

## Original lead

Determine the first unresolved unbalanced complete-multipartite value in the source: `eta(K_{1,1,5})`.

## Precise frozen statement for triage

Let `G=K_{1,1,5}`. For a finite Abelian group `Gamma`, an induced Abelian Cayley embedding is an injection `f:V(G)->Gamma` for which there is a symmetric set `S subset Gamma\{0}` satisfying `uv in E(G)` if and only if `f(v)-f(u) in S`. Let `eta(G)` be the least possible `|Gamma|`. Determine `eta(K_{1,1,5})` exactly.

The source gives the lower floor 10 and a residue-class construction of order 15. A positive upper certificate must list `Gamma`, all seven labels, and `S`, with an exact all-pairs check. A lower certificate must cover every Abelian group type at every order below the claimed optimum; failed search is not a proof unless the exhaustive domain and verifier are frozen.

## Primary source and delta

- J. A. Noel and J. A. Scott, *Induced Embeddings of Graphs into Abelian Cayley Graphs*, arXiv:2609.01486v1, Remark 12 and Definition 1: https://arxiv.org/abs/2609.01486v1
- Local PDF: `batches/inbox/bigWin-52-materials/2609.01486.pdf`
- SHA-256: `225f0354c45ac9babe9f7f2e30134abcc17454fa284f089fd58a182424262844`
- Retrieved 2026-09-07.

The paper says the complete-multipartite construction is not generally tight and singles out `K_{1,1,5}`: the floor is 10, the construction gives 15, and the obvious order-10 refinement fails. The proposed delta is the exact fixed graph, not a universal classification.
