# Immutable source statement: win-00046-p02

## Title

The four-color game on `M_2(C_3)`

## Statement

Let `M_2(C_3)` be the generalized Mycielski graph with vertex set `V^0 union V^1 union V^2 union {omega}`, three vertices in each layer, base edges forming `C_3`, cross-layer edges as in the source definition, and the root adjacent to every vertex in `V^2`. Alice and Bob alternately color an uncolored vertex from a fixed palette, always maintaining a proper coloring. Alice wins if all ten vertices are colored; Bob wins if an uncolored vertex becomes uncolorable.

Determine whether
\[
\chi_g(M_2(C_3))=4\quad\text{or}\quad\chi_g(M_2(C_3))=5.
\]

## Scope and provenance

- Primary source: Mou–Sun–Zhang, arXiv:2609.02283v1, generalized Mycielski construction and game definitions on pp.2–3; Theorem 5.1(1), p.14 proves `4 <= chi_g(M_k(C_3)) <= 5` for all `k >= 2`.
- Frozen PDF: `batches/inbox/bigWin-46-materials/2609.02283.pdf`, SHA-256 `42a09d9f05b1ab5b3fe51662cab09cb61e3d5e7660703fc9840b4a8e3bc67504`.
- The fixed ten-vertex instance is unresolved within the paper but is not presented there as a numbered open problem; call it a new finite question.

## Accepted contribution boundary

A resolution must give either a complete four-color winning strategy for Alice or a complete four-color winning strategy for Bob. A search result alone is insufficient: the strategy DAG must be independently checkable, cover every legal opponent reply, and preserve whose turn it is. The source's five-color upper bound and chromatic lower bound then turn either certificate into the exact value.

## Cheapest decisive route

Solve only the four-color game after quotienting by graph automorphisms, color permutations and identical-layer symmetries; export a canonical minimax DAG plus a small verifier that replays all legal branches.
