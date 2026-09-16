# Proof audit

Status: **PASS** on 2026-08-29.

The locked theorem is proved in `proof/tree_conjugacy_proof.md`.  Its terminal
line-by-line reconstruction is `audit/FINAL_PROOF_AUDIT.md`.  Builder,
Breaker, Certifier, and Referee records agree on the endpoint

\[
P(2i+1)=2^{4i+6}-1=4^{2i+3}-1\qquad(i\ge0),
\]

where `P` is the least positive full two-layer return on the infinite lattice.

All fatal and major entries in `proof/gap_ledger.md` are closed.  In
particular, the proof covers the exceptional left boundary, proves the
phase-tagged physical encoding injective, and derives a single contour cycle,
so it excludes every smaller positive return.  Exact computations are
explicitly labelled as audits rather than all-parameter evidence.

Clean executable results:

- unit tests: all 43 passed, including the C checker via the verified Zig 0.13
  `zig cc` wrapper documented in `audit/COMPILER_ENV_NOTE.md`;
- exact certificate verifier: PASS;
- primary tree audit: all vertices/phases through `N=12`;
- independent tree audit: all vertices/phases through `N=14`, one cycle on
  65,535 phase states at the maximal depth;
- normalized local rule: all 192 inputs, zero failures;
- malformed certificate: rejected with exit code 1.

No proof assistant was used.
