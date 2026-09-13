# Real Bapat--Sunder `F_A` project

## Exact target

For a real symmetric positive semidefinite matrix `A` of order `n`, define

`F_A[i,j] = A[i,j] per(A(i,j))`,

where `A(i,j)` deletes row `i` and column `j`.  The disproof target is an
explicit example of order at most 15 and a rational vector `x` for which

`x^T F_A x > per(A) x^T x`.

The final certificate must use integer or rational arithmetic.  A numerical
eigenvalue is discovery evidence only.

## Correct literature baseline

- `literature/drury_2018_FA_counterexample.pdf` gives a complex Hermitian
  rank-two counterexample of order 8 to the `F_A` conjecture and explicitly
  states the real version as a conjecture.
- `literature/drury_2017_real_POT_counterexample.pdf` gives a real rank-three
  order-16 counterexample to a stronger Schur-power/permanental-Oppenheim
  statement.  It does not by itself disprove the `F_A` conjecture.
- `literature/pioge_et_al_2025_implication.pdf` gives an order-16 complex
  Hermitian Gram matrix whose real Rayleigh quotient violates the real-part
  `F_A` inequality, and reports an unsuccessful numerical search at order 15.
  Its matrix is not real symmetric.

Thus the often repeated phrase "known real order-16 `F_A` counterexample" is
not supported by these three primary sources.  This project attacks the
strictly stronger real-matrix target stated above.

## Rigorous outcome

For every `n >= 3`, the real rank-two correlation matrix

`A_n[i,j] = cos(pi(i-j)/n)`

has

`per(A_n) = n!/2^(n-1)`

and complete `F_A` spectrum

`n!/2^n * (binom(n-1,s)^(-1) + binom(n-1,s-1 mod n)^(-1))`.

Thus the constant mode is uniquely maximal and the largest nonconstant
eigenvalue is exactly `n/(2(n-1))` times the permanent.  This is a nontrivial
infinite-family theorem; it is not a proof of the full real conjecture.

The analytic proof is independently reconstructed for orders 3--8 in exact
cyclotomic arithmetic by `src/verify_regular_projective_family.py`.  Its normal
and optimized outputs are byte-identical, and wrong-phase, wrong-scale, and
wrong-binomial attacks are rejected.

## Final deliverables

- `output/pdf/bapat_sunder_regular_projective_family.pdf`
- `output/bapat_sunder_regular_projective_family_latex_and_certificates.zip`

The final PDF is generated once under a stable filename after the exact proof,
independent audit, citation audit, clean build, and visual inspection pass.
