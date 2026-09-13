# Builder record

Date: 2026-08-30 CST.  Role executed serially by the sole Codex CLI.

The Builder began from the published EGF, not from guessed coefficients.  The
key reduction was to use the basis (X=(E,E/s,G)), closed under (d/dt) over
(mathbb Q(t)).  Exact row elimination produced the scalar order-3 operator
(mathcal L_3).  A rational order-2 left multiplier was then solved for so
that (mathcal M\circ\mathcal L_3) has the polynomial order-5 form whose EGF
coefficient equation is the target recurrence.

The human-readable derivation, all operators, the symbolic row identity, the
coefficient table, and the initial-index repair appear in
`proof/main_proof.md`.

Builder conclusion: candidate complete proof; handed to Breaker and Certifier,
not self-certified.
