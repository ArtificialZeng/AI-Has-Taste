# Checkpoint

Job: `bigMac-00005-p04-write-40ccd003c631` (writing phase,
2026-09-06).

## Accepted mathematical scope

- `claim.json` states a `resolution-paper`: for every field, every
  `n >= 6`, and every `r >= 0`, the quotient in `source.md` is
  Cohen--Macaulay exactly when
  `r >= floor((n-4)/2)` and `r != n-4`.
- `audit/math.json` records an `accept` verdict for snapshot digest
  `1c3def76c9bea4f8fcdebbb7978cdbcca0e51d890fcb8cff6b02400019d677fd`.
- The unchanged decisive proof is `evidence/facet-classification.md`; its
  SHA-256 still matches `audit/snapshot.json` at
  `c942a1cadbff1668bd658e148b0c60820077aacbee9aafc652503563591db8e3`.
- `source.md`, `problem.md`, and `claim.json` also still match their accepted
  snapshot hashes. In particular, immutable `source.md` remains
  `22a14216f9374c837488416f68108a80987295e36c90137e98e25ff0619a2105`.

## Writing obstacle

The mandatory initial command `release_gate.py check-math` failed with
`Evidence changed; freeze and obtain a fresh referee audit`. The sole mismatch
found among the five files listed in `audit/snapshot.json` was `checkpoint.md`:
the accepted hash is
`e638fc0068819a5e03f1080bd922a00f65ba87d1db97db31465c03bcc20f1a5a`,
whereas the checkpoint present at the start of this job hashed to
`b44c8ddf1940435ad8dfe78db0b732016ac75fd215d4d8554f90da9b8f559c2a`.
The writing instructions prohibit starting a manuscript after this failure.
Accordingly, no manuscript, PDF, or `publication.json` was created, and
`freeze-manuscript` was not run.

The earlier bibliography obstacle is no longer present:
`literature/user_bibliography_check.md` now exists and identifies the narrowly
relevant Zeng (2026) paper. This does not cure the failed mathematical gate.

## One next test

Freeze the current decisive evidence state and obtain a fresh mathematical
referee audit bound to that snapshot; then rerun `release_gate.py check-math`.
Only if it passes should the resolution manuscript be drafted and compiled.
