# Release manifest

Release date: 2026-08-22.  Research status: **partial theorem**.

## Mathematical statement and proof

- `problem/formal_statement.md` — formalized Frankl problem and project scope.
- `paper/main.tex` — submission manuscript source.
- `proof/fc_deletion_lifting.md` — expanded integer deletion and closed-form
  proof.
- `proof/power_chain_weighting_no_go.md` — infinite twin-free obstruction to
  fixed frequency-power templates.
- `proof/gap_ledger.md` — unresolved global and priority gaps.

## Exact computation and replay

- `src/fc_deletion_lift.py` and `src/verify_fc_deletion_lift.py` — recurrence
  certificate generation and independent verification.
- `src/enumerate_small_union_closed.py` and
  `src/verify_small_union_closed.py` — five-point census and independent full
  replay.
- `src/verify_power_chain_no_go.py` — exact construction and union-closure
  checks for finite no-go witnesses.
- `results/fc_deletion_lift_bounds.json` — frozen recurrence data.
- `results/small_family_weighting_audit.json` — complete reported census and
  weighting aggregates.
- `tests/run_all_fast.sh` — fast exact release gate.
- `tests/run_small_family_audit.sh` — full census plus independent
  (4{,}960^2)-pair replay.

The fast gate and the full replay both pass.  The full replay was also checked
by an independent adversarial reviewer after verifier hardening.

## Literature, proof, and rendering audits

- `literature/claim_ledger.md` and `literature/search_log.md` — bounded novelty
  and claim search.
- `audit/CITATION_AUDIT.md` — five-record source audit.
- `audit/PROOF_AUDIT.md` — analytic and computational proof audit.
- `audit/PDF_AUDIT.md` — build, metadata, text, and visual inspection.

## Released PDF

- `output/pdf/integer_floor_lifting_union_closed.pdf`
- Size: 338,837 bytes
- SHA-256:
  `e22bc052d7c361a41acdb9169b64a719f804a3db909262d46ced7813154af67d`

The checksum is release metadata and is not included in the PDF text.
