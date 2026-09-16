# Proof audit

- Lower endpoint: the literal 140-edge matrix passed the project checkers by
  row triples, column triples, and all 506,506 candidate submatrices. A
  separate PowerShell implementation written during the root audit again
  checked all 506,506 candidate submatrices and counted exactly 140 edges.
- Upper endpoint: builder and referee separately reconstructed the three
  degree profiles and row-deficit contradictions; an exact enumerator agrees.
- Fixed-core classification: 8,278,833 candidate supports were tested before
  the first feasible maximum-weight support; optimum added weight is six.
- Breaker searches for 141 and 144 returned only `UNKNOWN` and are not used.
- No floating point, heuristic failure, or unchecked UNSAT enters a theorem.
- The exact-value gap 140--144 remains explicitly open.
- The proof is human-readable and does not rely on a proof assistant.

Status: PASS for the stated partial theorem
`140 <= z(13,23;3,3) <= 144`. The exact value is not claimed.
