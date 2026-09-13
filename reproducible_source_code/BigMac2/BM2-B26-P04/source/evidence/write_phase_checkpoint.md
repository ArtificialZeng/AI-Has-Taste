# Writing-phase checkpoint

- **Job:** `bigMac-00026-p04-write-d061770d4a3a`.
- **Accepted scope preserved:** `release_gate.py check-math` passed for evidence
  snapshot `413f5c03360234d737d20f93f903d94a9e4c26eeddf3b27781609cb6e3077d6d`.
  The manuscript states exactly the accepted 13-vertex resolution and the
  certified equality \(\beta(P(13))=4\).
- **Draft artifacts:** `manuscript/main.tex` clean-builds with the command in
  `publication.json` to the three-page `manuscript/main.pdf`. The final log has
  no warnings, undefined references, overfull boxes, or underfull boxes.
- **Bibliography:** `literature/user_bibliography_check.md` is absent from this
  project. Consistently with the available dated literature evidence, the PDF
  conservatively cites the directly relevant Bae and Ascoli--Frederickson--
  Frederickson--McFarland--Post arXiv records and makes no priority claim.
- **Freeze evidence:** `release_gate.py freeze-manuscript` passed with manuscript
  digest `2e9c2db43c81ef604db52995d8c5ac90209a5496cfc3f0e013fb46853731df9a`
  and PDF digest
  `660790999231e46001a4fe219f1f44fb8f0c80b0fdbd7bd6ed663e08dab92f3e`.
- **Integrity obstacle:** root `checkpoint.md` is itself hash-bound in the
  accepted mathematical evidence snapshot. Altering it during writing would
  invalidate the fresh referee acceptance, so this phase record is stored as a
  separate evidence checkpoint instead.
- **Next test:** Run a fresh citation, clean-build, and page-by-page visual audit
  against `audit/manuscript-snapshot.json`; repair only manuscript issues and
  refreeze before local release.
