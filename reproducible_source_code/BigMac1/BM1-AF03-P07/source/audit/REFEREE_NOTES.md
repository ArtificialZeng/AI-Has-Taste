# Clean-room referee notes

The referee reconstruction began from `problem/formal_statement.md`, the
published four relations, and Algorithm 1, without using discovery component
or interval files. The proof was rebuilt in the order recorded in
`audit/PROOF_AUDIT.md`.

## Attempts to break the endpoint

- Checked empty, singleton, repeated-endpoint, and incomparable-shape cases.
- Verified that standardization preserves equality/order patterns and the
  distinct-letter set.
- Audited the shape-first recursion for omissions and duplicate paths.
- Confirmed that hash-table hashing cannot identify unequal full codes.
- Confirmed all four relation families and
  (n+\binom n2+2\binom n3=148) at (n=8).
- Reproved why queueing only successful unions gives the least right-stable
  congruence.
- Reproved the upward/downward-closure characterization of order-convexity.
- Confirmed that initial filtering selects full components.
- Ran malformed and tampered certificates and required explicit rejection.
- Compared independent totals with discovery and the published (n\le7)
  baseline.

No finite counterexample or endpoint gap survived. The correct verdict is
`CERTIFIED_FINITE_RESULT`, not `PROVED`, because no all-(n) cover-filling
argument was obtained.

