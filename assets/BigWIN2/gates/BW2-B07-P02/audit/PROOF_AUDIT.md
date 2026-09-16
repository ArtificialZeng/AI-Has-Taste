# Proof audit

Status: PASS (2026-08-30 UTC).

- Formal statement matches the source endpoint exactly after the reindexing
  \(m=n+1\).
- The coefficient identity and factorization were derived formally and
  cross-checked through degree 80 with exact rationals.
- Boundary evaluations at \(1\) and \(-1\) follow absolute-convergence
  estimates; no illicit termwise boundary manipulation remains.
- The `W` induction covers its initial and empty-sum cases and proves strict
  signs for every relevant coefficient.
- The `J` zeroth moment, first moment, and pointwise tail bounds were checked
  independently from the final convolution arithmetic.
- The near and far convolution ranges include every parity-compatible index,
  including the constant coefficient of `W`.
- The tail estimate is strict from degree 5000.  The exact and interval
  prefix certificates overlap at degree 5000 and cover degrees 31--5000.
- All fatal and major entries in `proof/gap_ledger.md` are resolved.
- Numerical diagnostics were not used as proof.
- No proof assistant was used.
