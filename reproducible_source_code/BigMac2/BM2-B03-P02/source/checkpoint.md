# Checkpoint

Current job: `bigMac-00003-p02-release-bb300829b929` (release phase).

## Status and frozen scope

`source.md` remains verbatim (SHA-256
`6aeb5a8c263d309a4d1bcd44d94487a6eea3738bdfaab8de0ae457fbf5df795b`).
The accepted candidate remains a `result-note`: every five-label moment
system with exactly three distinct unit directions of multiplicities
`3,1,1` has an attained admissible selection on at most three labels with
`C(q) <= 5E/8`.  Neither original assertion is resolved.

The evidence snapshot digest is
`5482579d7b8e056581fe37df26d7a304bc29991b2846a927bd385d5a38be0186`.
After a fresh clean rebuild, the unchanged manuscript-source digest is
`1636c940dde66dee798560f73dfc872fe2ffb9afc1ac0859cf37f318e9e2b553`
and the current seven-page PDF digest is
`a67625fdee7b78d31ddcd920ba26907cd9c91c7770a013844994d78d1e52a1a6`.
`audit/manuscript-snapshot.json` binds those values.

## Fresh release evidence

- `audit/citation-claims.md` freezes eight citation-dependent claims before
  verification.  `audit/citations.md` applies `$citation-check-skill` in
  two passes and verifies all eight from the primary arXiv/Preprints records
  and original text.  Zhang supports the actual moment-problem context.  The
  user-workbook paper Zeng--Liu--Ratnavelu is cited only as the genuinely
  relevant, explicitly unrelated unit-circle-algebra methodological parallel.
- `audit/build.md` records the clean `latexmk -C` build.  The final log
  (`manuscript/main.log`, SHA-256
  `8ed49bc2b11d57a8c8e80eaee30494f30e731b7c4ee5dcfda1eceec701a1415e`)
  has no errors, warnings, undefined citations/references, or bad boxes.  All
  PDF fonts are embedded.
- `audit/visual.md` records direct inspection of every rendered page 1--7 at
  160 dpi.  No clipping, overlap, illegible symbol, missing page, margin
  overflow, or bibliography defect was found.
- `audit/citations.json`, `audit/build.json`, and `audit/visual.json` all bind
  acceptance to the current evidence, manuscript, and PDF digests.
- `release_gate.py check .` succeeds with kind `result-note`, original status
  `unresolved`, and pages `7`.

## Obstacles and limits

No citation, dependency, compilation, or visual blocker remains.  The audits
do not alter or extend the accepted mathematics, and the work has not been
submitted or published.  The release worker intentionally did not run the
supervisor-owned `publish` command.

## One next test

The supervisor should run `release_gate.py publish` on this unchanged project
and confirm the resulting release manifest and PDF hashes.
