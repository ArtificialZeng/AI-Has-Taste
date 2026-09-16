# Immutable source — win-00051-p01

## Original lead

Decide the first cubic higher-rank cell of the monomial Lie-additive diameter problem.

## Precise frozen statement for triage

Let `V=Sym^3(C^4)` and `U=Sym^3(span(e_1,e_2,e_3))`. Let `rho:sl_4(C)->End(V)` be the derived natural representation and let `mon(rho(sl_4(C)))` contain the identity and every finite product `rho(X_1)...rho(X_r)`. Prove that there exist `m_1,m_2` in this monoid such that `m_1 U + m_2 U = V`, or prove that no such pair exists. Equivalently, decide whether the monomial Lie-additive diameter in Question 8.5 equals `ceil((4+3-1)/(4-1))=2` for `(n,k)=(4,3)`.

A positive certificate must list the traceless matrices and multiplication order and exhibit a nonzero exact determinant for the resulting `20 x 20` spanning matrix. Random numerical full rank is not a proof. A negative answer requires a universal rank obstruction, not a failed bounded search.

## Primary source and delta

- Urban Jezernik and Špela Špenko, *Additive diameters and covering complexity of irreducible representations*, arXiv:2609.03882v1, Question 8.5, PDF pp. 32–33: https://arxiv.org/abs/2609.03882v1
- Local PDF: `batches/inbox/bigWin-51-materials/2609.03882.pdf`
- SHA-256: `e8c327173640c56f21510418e4cfc329b138ba83b82d9e666361f082377ed849`
- Retrieved 2026-09-07; 33 pages.

Theorem 8.1 handles only `n=3`. This is one fixed `n=4` cell, not the universal question. `win-00043-p11` concerns a different `SL_3` translate-covering problem.
