# Proof audit

Status: PASS (2026-09-03).

- Formal endpoint matches `problem/formal_statement.md`.
- Explicit generators cover unequal degrees outside `(4,3)`, equal degrees
  at least five, and `(2,2)`.
- Common-quotient/automorphism-graph obstructions are fully classified.
- `S_2,S_3,S_4,S_6` special behavior is explicitly audited.
- Three exceptional lower bounds have both human proofs and two independent
  complete exact enumerations; the upper bound is source-verified.
- All fatal and major entries in `proof/gap_ledger.md` are closed.
- Builder, breaker, certifier, and referee records are separate.
- No proof assistant was used.
- Independent root review rechecked the common-quotient classification, the
  equal-degree automorphism obstruction, and all three exceptional cases.
