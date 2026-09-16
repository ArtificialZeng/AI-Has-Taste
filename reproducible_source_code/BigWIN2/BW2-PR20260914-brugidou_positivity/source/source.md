# Coefficient positivity in Brugidou's q-exponential monomial specialization

Source: Vincent Brugidou, On a particular specialization of monomial symmetric functions,
arXiv:2306.15300v7 (2025-06-04), Corollary3.5 and Conjecture4.1.
https://arxiv.org/html/2306.15300v7
Captured and selected 2026-09-14 Asia/Shanghai through authorized primary-literature fallback.
This is not a generated browser batch and consumes no 大WIN batch number.

Original Conjecture4.1, with mathematical notation transcribed:
"For any partition λ the coefficients of J_λ are strictly positive."

The following definitions identify the polynomial in that original statement.
Let Λ over Q be the ring of symmetric functions. The specialization φ_q:Λ→Q[q]
is uniquely specified on the algebraically independent elementary generators by
φ_q(e_j)=q^(j(j−1)/2)/j! for j≥1, and φ_q(1)=1.
For a nonempty partition λ=(λ_1≥...≥λ_r≥1) of n, let
ν(λ)=Σ_(i=1)^r(i−1)λ_i, and a_j(λ)=#{i:λ_i=j}.
The monomial symmetric function m_λ is the sum over distinct monomials whose
nonzero exponent multiset is λ. The source defines J_λ by the identity
φ_q(m_λ)=(1−q)^(n−r) q^ν(λ) J_λ(q)/((n−1)! ∏_(j≥1)a_j(λ)!).
By Corollary3.5, J_λ is an integer polynomial, has nonzero constant term,
and has degree d=binom(n−1,2)+r−1−ν(λ).
The original target is: for every n≥1 and every λ⊢n, writing
J_λ(q)=Σ_(k=0)^d c_(λ,k)q^k, every c_(λ,k)>0.
The identity defines a polynomial in the indeterminate q; division at q=0 or1
is not the definition by pointwise evaluation. Constants and one-part/one-column
partitions remain included. There is no bound on n, r, or the largest part.

Conjecture4.2 in the same source asks a separate coefficient log-concavity question.
It is related context, not a silent replacement for the frozen positivity target.
A proof on hooks or another proper subclass is a partial result only.
