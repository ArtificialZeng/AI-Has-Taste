# Proposer verification record

Job `newwin-00001-p20-research-f42a5d965fef`, 2026-09-12.
This records checks by the proposing worker, not a separate mathematical
audit or an acceptance. No other agents or workers were used.

## Analytic check

The proposed coefficients were fixed by the prior leads. The current
proof supplies the substantive missing uniform estimates, with a new
elementary Wallis-integral bound in place of a cited Stirling remainder.
The following potential errors were specifically checked:

- The reflection endpoint is -d-2, giving S[-d-2]=1-S[d]. Its upper
  branch correction is consequently -hf(y), while the lower branch
  correction is +hf(y).
- Signed summation for negative d excludes both endpoints. Adding the
  two endpoint half-weights gives the same formula as for positive d.
  For d=-1 the sum is empty; for d=0 it contains the central mass.
- Pointwise mass error is relative O(h^2), making accumulated CDF error
  O(h^2). The explicit lower bound p/(hf)>=1/(2e) controls division.
  The inverse error in equation (14) is an exact algebraic identity.
- The rational upper term contributes 2y/h+2-2y^2, with the explicitly
  bounded remainder retained in equation (17).
- F0 is C^2 at zero although H is not differentiable there; V is C^1.
  Thus the Taylor remainder uses a compact-interval bound independent
  of the actual floor offset, including offsets arbitrarily near -1.
- B=A+1 and m>=ceil(max(4,4B^2,K)) ensure all needed indices are valid.
  All final constants depend only on A. Their size is not optimized.

These checks found no mathematical gap in the submitted argument.
They are still a same-context proposer check; fresh review is pending.

## Reproducible computation

Run from the project directory:

```
python3 evidence/research-check.py > evidence/research-check.json
```

The script uses Python integers and Fraction for finite algebra, and
mpmath at 90 decimal digits for analytic-function evaluations. Its
output records the source, proof, and script hashes.

Exact finite checks passed: 2352 source/reflection identities, 1148
signed monomial-quadrature identities, 1176 rational-remainder
identities, 30 reciprocal-remainder identities, and 48 central jumps.
Coverage and parameters are specified exactly in the script and JSON.
Another 577 floor memberships were checked rationally: each sample
is specified by x=(d+theta)/sqrt(m), with exact rational theta.

The numerical tests use previously untested nonsquare capacities
m=17,127,509,2039; A=1/8,1,3,6; selected interior and endpoint cells;
and theta=0, 10^-20, 1/3, 1-10^-20. Of 577 samples, 417 satisfy the
proof's explicit m threshold. Those passed the local, CDF, and final
error-constant comparisons. The other 160 are stress observations
outside that sufficient threshold, not claims of enlarged coverage.
The exact expectations use the original integer numerator and denominator.

No numerical interval arithmetic was used, and real floor cells were
not exhausted. These are finite consistency checks, not certificates
of the universal analytic theorem. That theorem rests on the written
inequalities in `research-proof.md`.

## Original-source integrity and next review test

The source hash remains
`b5dd0cb2ff5644a13c42b0b0e352a6a172be7c766f45a41ad37d89c83c4af495`.
The decisive original primary PDF is preserved under `evidence/external/`.
No manuscript, output PDF, audit acceptance, or release manifest was made.

One next test: a fresh referee should try to invalidate the full frozen
claim by checking equations (7), (10)--(19), especially d=-1, d=0,
the reciprocal remainder, and the C^2 floor Taylor bound, then compare
the claimed application scope with primary Corollary 7.2 and section 8.
