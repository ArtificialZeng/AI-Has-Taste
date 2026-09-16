# Immutable source — win-00052-p03

## Original lead

Settle the first small cell of the generalized-pancake spectral-gap equality conjecture that the source does not explicitly evaluate.

## Precise frozen statement for triage

Let `S(4,2)=Z_4 wr S_2` and let `R(4,2)` be the four generalized prefix reversals `r_i^epsilon=(c_i^epsilon,r_i)` for `i=1,2` and `epsilon in {-,+}` from Definition 2 of the source. Let `P(4,2)=Cay(S(4,2),R(4,2))`. Let `psi_{4,2}` be its unnormalized adjacency spectral gap. Let `beta_{4,2}` be the unnormalized spectral gap of the color-position Schreier graph for the action on `Z_4 times [2]`. Compute both numbers exactly and prove or disprove `psi_{4,2}=beta_{4,2}`.

The Cayley graph has 32 vertices and the Schreier graph has 8. A certificate must specify the exact adjacency matrices (or representation blocks), their characteristic/minimal factors around the second eigenvalue, and an exact eigenvalue ordering argument. Floating-point eigenvalues alone are not a proof.

## Primary source and delta

- Arindam Biswas, *On the Laplacian spectral gap of generalized pancake graphs*, arXiv:2608.15398v1, Definition 2, Section 5, Conjecture 5.1: https://arxiv.org/abs/2608.15398v1
- Local PDF: `batches/inbox/bigWin-52-materials/2608.15398.pdf`
- SHA-256: `49cf3770084b724debc4cf4cb29403ed23f14fb9b102a10344e7a48bc0fcdb79`
- Retrieved 2026-09-07.

Conjecture 5.1 predicts equality for `2<=m<=5`, `n>=2`; the paper explicitly treats `(3,2)` and the strict counterexample `(6,2)`, but not this 32-vertex cell. Triage must still check for an exact value in cited or later literature.
