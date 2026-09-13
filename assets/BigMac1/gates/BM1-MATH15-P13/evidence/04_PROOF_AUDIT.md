# Proof audit

Status: pass for the restricted split-graph theorem; full chordal problem open.

- Builder proof: `proof/builder_notes.md`.
- Counterexample/obstruction review: `proof/breaker_notes.md`.
- Exactification: `proof/certifier_notes.md`.
- Independent definition-level reconstruction: `proof/referee_notes.md`.

The marked-to-unmarked implication, simultaneous three-type homogenization,
nonunique host partitions, missing edge types, and quantifier negation in the
lower bound were checked separately.  No fatal or major gap remains for the
split-graph endpoint.  Gap G01 remains fatal for the full chordal upper bound
and is explicitly outside the claimed theorem.

The exact witness verifier passes and rejects a deliberately corrupted
certificate.  No proof assistant was used.
