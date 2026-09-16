# Immutable source — win-00052-p04

## Original lead

Determine the exact unbounded-speed robber cop number of the smallest two-dimensional even torus not made exact by the source bounds.

## Precise frozen statement for triage

On the undirected graph `G=C_4 square C_4`, cops move along at most one edge per cop move, while after the cops move a robber may traverse any finite path whose vertices avoid all occupied cop vertices. Capture occurs when a cop occupies the robber vertex. Let `c_{1,infinity}(G)` be the least number of cops having a winning strategy under the source convention. Determine `c_{1,infinity}(C_4 square C_4)` exactly.

A resolution must freeze the move-order convention, give a replayable winning strategy for the upper bound, and an independently checkable robber strategy or solved attractor-state certificate for one fewer cop. State-space enumeration must record graph encoding, legal-state definition, symmetry quotient if any, and a hash/digest.

## Primary source and delta

- Arindam Biswas, *Fast robbers on abelian Cayley graphs and digraphs*, arXiv:2608.30474v1, Section 5.2: https://arxiv.org/abs/2608.30474v1
- Local PDF: `batches/inbox/bigWin-52-materials/2608.30474.pdf`
- SHA-256: `b1009b09b4aefa9d3a1c6278529bc28209b1a4bdd11aa5a71ce2e46c906230b6`
- Retrieved 2026-09-07.

The source quotes product/asymptotic bounds and, for `m>=18`, `2m-24<=c_{1,infinity}(C_m square C_m)<=2m`; it does not state the `m=4` exact value. This is a bounded atlas cell, not evidence for the asymptotic conjectures. Later exact-game literature must be checked before any novelty claim.
