# Immutable source — win-00051-p02

## Original lead

Determine the exact connectivity-code number of the smallest natural non-diagonal product of cycles.

## Precise frozen statement for triage

Let `H=C_3 square C_4` be the Cartesian product on `Z_3 x Z_4`: two vertices are adjacent exactly when one coordinate agrees and the other coordinates are adjacent in the corresponding cycle. A family `C subseteq 2^{E(H)}` is a connectivity code if `A triangle B` is a connected spanning subgraph of `H` for all distinct `A,B in C`. Determine `m(H)=max |C|`.

Since `H` is four-regular, the cut bound gives `m(H)<=16`. A 16-word family, together with exact pairwise connectivity replay, proves equality. If the optimum is smaller, a complete maximum-clique/SAT certificate must prove the upper bound. Heuristic clique failure is not a negative result.

## Primary source and delta

- Chenxiao Tian, *Maximal Connectivity Graph-Codes in Every Degree at Least Four*, arXiv:2609.02953v1, Introduction and §6(d), PDF pp. 1 and 8: https://arxiv.org/abs/2609.02953v1
- Local PDF: `batches/inbox/bigWin-51-materials/2609.02953.pdf`
- SHA-256: `332cefb446276afb3892abe4ae8155e971aacbb77f8d2ff69aa1395178c10429`
- Retrieved 2026-09-07; 10 pages.

The source records `m(C_3 square C_3)=m(C_4 square C_4)=16` and explicitly leaves products of cycles open. The present problem fixes only `C_3 square C_4`.
