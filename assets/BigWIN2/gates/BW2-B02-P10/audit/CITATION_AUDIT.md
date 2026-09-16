# Citation audit

Status: PASS for the journal-neutral submission manuscript.

Audit date: 2026-08-29 (UTC and Asia/Shanghai calendar dates agree).

## Source identity

- The sole cited work is Ina Bašić, Eric Gottlieb, and Matjaž Krnc,
  *CRIM: A Natural Game on Integer Partitions*, arXiv:2606.16828v1,
  submitted 2026-06-15.
- The arXiv source, abstract record, API metadata, and DataCite metadata were
  cross-checked.  The manuscript calls it a version-one preprint, not a
  journal publication.
- The exact source claims and their locations are recorded in
  `literature/claim_ledger.md`; the bounded novelty search is recorded in
  `literature/search_log.md`.

## Coverage and consistency

- `audit_latex.py` reports `cited=1 bib=1 missing=0 unused=0`.
- Both substantive source-dependent paragraphs cite the source: the game/rank
  attribution and the prior-family/conjecture attribution.
- The bibliography entry includes authors, title, arXiv identifier, subject,
  version, submission date, year, and a visible stable arXiv URL.
- No family already proved in the source is claimed as new.  The novelty claim
  is bounded to the databases and web searches completed through the audit
  date; it is not phrased as proof that no unindexed work exists.

Fatal or major citation defects: none found.

Publication recheck: `audit_latex.py` again reports
`cited=1 bib=1 missing=0 unused=0`.  The bounded novelty conclusion is
unchanged: no prior proof, counterexample, or boundary-word classification was
found in the recorded searches through 2026-08-29.  This is not a claim about
unindexed work.
