# bigMac-00011-p01 — Minimum dimension for a restart-4 conjugate-gradient counterexample

## Immutable source statement

Let `n_min(4)` be the least dimension `n` for which there exist a diagonal
positive-definite matrix `A in R^{n x n}` and a nonzero initial residual
`r_0` such that exact-arithmetic restarted conjugate gradients with restart
length `s=4` never terminates and the normalized even residual directions

`r_{2j}/||r_{2j}||`

do not converge.  Determine `n_min(4)` and give a fully exact certificate in
the minimum dimension.

## Primary boundary

Colbrook, Stepaniants, and Townsend, *A Complete Resolution of Forsythe's
Conjecture for Restarted Conjugate Gradients*, arXiv:2609.04659v1, Theorem 1.1
and Appendix B.4.  The source constructs a counterexample in dimension
`s+4=8`; finite Krylov termination gives the elementary lower bound
`n_min(4)>=5`.  The source does not claim that dimension eight is minimal.

Primary PDF: `batches/literature/bigMac-11/2609.04659v1.pdf`  
PDF SHA-256: `a8eddb4d369949f3410bc711f657c06725fcbd4e6d8b20ff93a8ddced99244ee`

## Permitted contribution boundary

An exact exclusion of dimensions five through seven together with the known
dimension-eight construction, or a smaller exact counterexample with a
certified nonconvergent orbit.  Floating recurrence plots or long numerical
orbits are discovery evidence, not nontermination or nonconvergence proofs.

