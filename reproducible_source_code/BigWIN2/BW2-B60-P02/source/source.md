# Immutable source: win-00060-p02

## Frozen problem

For each polynomial degree `p in {1,2,3,4,5}`, set the Nitsche parameter `gamma_D=5p(p+1)` and use exactly the two-element cut configuration and bilinear form `a^(2)_{kappa,gamma}` defined in Proposition 4 and Appendix B of arXiv:2609.04067v1. Determine exactly

`gamma_*(p) = sup_{0<kappa<1} inf{gamma : a^(2)_{kappa,gamma} is positive semidefinite}`,

including all limiting or interior `kappa` that attain the supremum. The output must be an exact rational or algebraic value with a verifiable generalized-eigenvalue/resultant/Sturm certificate, not a floating-point plot. In particular, decide whether the paper's `kappa -> 0` necessary threshold `1/(gamma_D-p^2)` is also globally sharp for each of the five degrees.

## Primary source and locator

- Paper: *A Multigrid Method for CutFEM and its Convergence*, arXiv:2609.04067v1.
- Locator: Proposition 4 and Appendix B.
- Local evidence: `batches/inbox/bigWin-60-materials/2609.04067.pdf`.
- PDF SHA-256: `cbe004fd2b861aa6342b9b2d8d2ba065319ae039be5cb2cda4721780e534fac3`.

The full-`kappa` sharpness and exact maximizers are treated as unverified until triage checks the entire paper and neighboring literature.
