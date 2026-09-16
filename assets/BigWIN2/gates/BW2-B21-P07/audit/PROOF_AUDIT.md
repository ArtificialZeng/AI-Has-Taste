# Proof audit

- Formal endpoint: the literal last-occurrence conjunction is false once a
  single later hit is certified.
- Exact witness: `audit/breaker_artifacts/witness.json`.
- Feasibility: an independent verifier reconstructs the 78,493,252nd prime
  and all preceding recurrence states; exit status 0 is recorded twice,
  including from the clean extracted release.
- Decisive equality: `567791839 + 1579691809 = 2147483648 = 2^31`, hence the
  largest odd divisor is 1.
- Scope: no assertion that this is the next or last hit.
- Fatal/major proof gaps: none for disproof. No proof assistant was used.

Status: passed root recheck on 2026-09-02. A fresh 100,000,000-term segmented
reconstruction and an independent SymPy prime-iterator reconstruction both
returned the same witness and exited successfully.
