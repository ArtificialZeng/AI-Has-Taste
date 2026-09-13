# Proof audit

Date: 2026-08-29.  Status: **PASS for the certified real `n=3` endpoint**.
No verdict is issued for `n=4` or general `n`.

Post-timeout recovery note: all five decisive exact commands and the
standalone breaker verifier were rerun on 2026-08-29 and again exited zero.

## Audited statement

For every real `3 x 3` matrix `T` of rank at most two,

\[
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
\le 20\operatorname{per}(T)^2.
\]

Equality holds exactly when `rank(T) <= 1`, or `T` has a zero row or column,
or a rank-two `T` can be row/column permuted to contain a `2 x 2` all-zero
submatrix.

## Independent checks

- The primary proof in `proof/n3_proof.md` treats rank zero/one, zero
  rows/columns, both rank-two projective row multiplicity strata, points at
  infinity, `per(T)=0`, and the equality zero set.
- `audit/agents/builder.md` independently derives the binary-form contraction
  and proves the split-cubic inequality by an exact discriminant calculation.
- `audit/agents/referee.md` reconstructs the result from the permanent
  definition, explicitly attacks non-split, zero-scale, zero-permanent, and
  affine-boundary failure modes, and reaches the same equality classification.
- `audit/agents/referee_pgl2_equality.md` independently rebuilds the rank-two
  factor maps and the PGL2 plus nonzero row-scaling reduction.  It covers the
  distinct, repeated, and triple row-line strata, keeps homogeneous column
  coordinates (including points at infinity), and derives the equality iff
  classification directly from the two SOS zero sets.  It also records the
  necessary logical precaution that rank at most one must be split off before
  using a minimal rank-two factorization.
- The counterexample hunter in `audit/agents/breaker.md` used independent
  exact evaluators and adversarial floating search.  It found no exact
  counterexample in its recorded scope.  This is diagnostic evidence only.

## Exact certificate rerun

On 2026-08-29 all commands exited zero:

```text
python certificates/verify_n3_sos_stdlib.py
  PASS; certificate b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0
  both exact remainder-monomial counts: 0
python certificates/verify_n3_sos.py
  PASS; exact integer-coefficient expansion
python certificates/builder_verify_n3_equality.py
  ALL EQUALITY CROSS-CHECKS PASSED
python experiments/builder_verify_n3.py
  ALL EXACT CHECKS PASSED
python experiments/referee_verify_n3.py
  PASS: exact symbolic identities and independent direct evaluators
python experiments/referee_verify_pgl2_equality.py
  PASS: both homogeneous SOS identities and both equality families
python certificates/test_fail_closed.py
  PASS: badhash/extra/drop/tamper rejected by both verifiers
```

The standalone breaker verifier also reconstructed all eight retained
integer records from their serialized matrices and verified rank,
`per(T)`, and the duplicated-block permanent.

## Disposition and limitations

The proof is exact and human-readable; the verifiers check polynomial
identities rather than supplying positivity by sampling.  Both certificate
readers bind the canonical SHA-256 and exact nested schema and reject malformed
or mutated inputs.  The full suite also passed in a fresh hash-locked CPython
3.13.5/SymPy 1.13.3 environment.  The source-backed
ordered conjecture is real.  An arbitrary-complex `<=` formulation is not
well-defined and is not silently replaced by an absolute-value conjecture.
For `n=4`, a genuine projective cross-ratio remains, so G04 stays open.

No Lean, Coq, Isabelle, HOL, or other proof assistant was used.  No
SAT/SMT/CAD oracle was used for the final theorem.
