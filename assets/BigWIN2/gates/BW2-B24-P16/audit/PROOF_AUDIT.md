# Proof audit

Status: PASS for the disproof endpoint.

- Builder reduced quotient parity to bit k of 3^k and recorded why the
  attempted infinite positivity routes do not close (`audit/builder.md`).
- Breaker independently found the first failure n=331522, S_n=0 with Ruby
  integer arithmetic and a second shift-based evaluator (`audit/breaker.md`).
- Certifier independently found the same first failure, exhaustively checked
  through 1,000,000, and supplied a fail-closed Python verifier with a modular
  exponentiation/direct-quotient prefix cross-check (`audit/certifier.md`).
- Referee reconstructed all definitions and endpoints and caught the unrelated
  off-by-two error in OEIS's odd-count comment (`audit/referee.md`).
- Root rerun of the certifier command passed. Feasibility (integer n>2 and
  exact recurrence) and the decisive comparison S_331522=0 are separate.
- The batch-level root independently reran the Ruby integer implementation to
  the first failure and then reran the fail-closed Python certificate through
  1,000,000 from a clean ZIP extraction. Both returned first failure 331522
  with value zero; the latter also returned S_1000000=580 and minimum -359 at
  371843.
- No fatal or major gap remains for the counterexample. The blocked positive
  proof route is irrelevant once the universal statement is disproved.
- No proof assistant was used.
