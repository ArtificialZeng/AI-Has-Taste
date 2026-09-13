# Checkpoint

## Restored state — 2026-09-08

The exact two-weight Z/5Z claim in `claim.json` and its proof and finite
checker are unchanged. The old snapshot was accepted by referee
`bigMac-00007-p02-referee-0d4b575892af`, but that acceptance does not bind
this updated checkpoint. A fresh mathematical referee is required before
writing. No new mathematical acceptance is asserted here.

## Decisive evidence and resolved operational issue

- `source.md` remains unchanged with SHA-256
  `3e5ea16b71c4994ed41da59d6c974640eeb23303558f0df40da7550fab4ba6db`.
- `evidence/proof.md` gives direct-sum translation averaging, the exact
  invariant GL cone, exhaustive cut orbits, and strict/face/tie optimizers.
  `evidence/check_finite.py` is the reproducible finite check. The exact
  objective is `5*min(a+2*b,2*a+b)/(6*(a+b))` for `a,b>=0`, `a+b>0`.
- The old write blocker is now obsolete: the authentic extracted record is
  present at `literature/user_bibliography_check.md`. The user's designated
  Excel DOI/BibTeX metadata controls when an external refresh is unavailable.
  Citation-access issues must not block PDF creation or local release;
  unsupported attribution must instead be narrowed or repaired honestly.
- Before recovery, rehashing the six frozen files found only checkpoint.md
  changed. `claim.json`, source, interpretation, proof, and checker all
  matched the old snapshot. The old checkpoint and snapshot are preserved at
  `evidence/checkpoint-before-recovery-2026-09-08.md` and
  `audit/snapshot-before-recovery-2026-09-08.json` for history.
- No proof route has failed in this restoration. The previous stop was an
  infrastructure/bibliography-policy state, not a mathematical obstruction.

## One next test

Freeze the current stable evidence with release_gate.py and dispatch a new
`gpt-5.6-sol` / `ultra` referee through the sole queue owner, following the
user's latest model-switch instruction. Recheck all
quantifiers, equality cases, exact evidence, and the bounded contribution
against the original source. If accepted, proceed to writing and a separate
fresh release audit. Preserve the research-pass count and session deadline.
