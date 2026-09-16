# Immutable source — win-00050-p03

## Original lead

Determine the game chromatic number of the next unresolved triangular generalized-Mycielski layer `M_3(C_3)`.

## Precise frozen statement for triage

Use Definition 2.1 of the primary source. In the standard vertex-coloring game on the fixed thirteen-vertex graph `M_3(C_3)`, Alice and Bob alternately give a previously uncolored vertex one of `q` colors while maintaining properness; Alice wins if all vertices are colored, and Bob wins once an uncolored vertex has no legal color. Determine whether Alice wins for `q=4`. Equivalently decide exactly whether `chi_g(M_3(C_3))=4` or `5`.

A computational result must give a complete, independently replayable strategy DAG with legal-move checks, terminal-condition checks, color-renaming canonicalization and graph-automorphism canonicalization. A finite collection of sample plays is not a proof. The claim is only for `k=3`; it may not be generalized to all `k` without a separate proof.

## Primary source and delta

- Yushuang Mou, Qiang Sun and Chao Zhang, *The game chromatic number of generalized Mycielski graphs of paths and cycles*, arXiv:2609.02283v1, Definition 2.1, Theorem 3.1 and Theorem 5.1(1): https://arxiv.org/abs/2609.02283v1
- Local primary PDF: `batches/inbox/bigWin-50-materials/2609.02283.pdf`
- SHA-256: `42a09d9f05b1ab5b3fe51662cab09cb61e3d5e7660703fc9840b4a8e3bc67504`
- Retrieved: 2026-09-07; 16 pages.

The source proves only `4<=chi_g(M_k(C_3))<=5` for `k>=2`. The prior project `win-00046-p02` settled the distinct ten-vertex case `k=2`; its result does not decide `k=3`.

