# Submission-readiness audit

Audit date: 2026-08-30. Status: passed for a general mathematics submission;
no journal-specific formatting claim is made because no target journal was
specified.

## Mathematical gate

- [x] Formal theorem matches the source problem and proves the full finite
  endpoint `L_8=94`.
- [x] Alphabet, order, rotations, linear factors, quantifiers, and endpoint
  conventions are explicit.
- [x] Occurrence gaps, repeated available occurrences, first-position offset,
  and incidental factors are covered by the occurrence-order lemma.
- [x] Exact certificate is independently reproducible.
- [x] Every fatal/major gap in the ledger is resolved.
- [x] Floating/MILP output is labeled discovery-only.

## Novelty and citation gate

- [x] TheoremDB P2600 and its prior interval are cited.
- [x] Fredricksen--Maiorana and Mucha primary metadata were checked against
  publisher/DOI records; the Mucha arXiv manuscript was also checked.
- [x] Pre- and post-result exact searches are recorded and novelty wording is
  explicitly bounded by the searched public sources and date.
- [x] LaTeX audit reports `cited=3 bib=3 missing=0 unused=0`.
- [x] Each citation supports only its nearby statement.

## Reproducibility gate

- [x] Stable commands and paths appear in `README.md` and the paper.
- [x] Primary certificate check passed: 30 targets, 94-bit word, path overlap
  146, 930 dual inequalities, lower bound 94.
- [x] Independent check passed: orbit target generation, rolling windows, and
  integer Hungarian assignment optimum 146.
- [x] Fail-closed and regression suite passed seven mutation expectations and
  72 brute-force Hungarian comparisons with seed 20260830.
- [x] The source ZIP was extracted into a new empty temporary directory; all
  three exact checks and a clean LaTeX build passed there.
- [x] Extracted text of the clean-built PDF matched the delivered PDF exactly.
- [x] A release manifest is created and verified after all final edits.

## Manuscript gate

- [x] Title and abstract state the exact result.
- [x] Prior work, new result, limitations, and exact proof are separated.
- [x] Witness, all target occurrence positions, and complete dual potentials
  appear in the paper.
- [x] Author, Institute of Computer Science and Digital Innovation at UCSI
  University, Kuala Lumpur 56000, Malaysia, and both supplied emails appear.
- [x] No acknowledgments or funding claim is made.
- [x] The `amsart`/`amsplain` combination is internally consistent; a target
  venue was not specified.
- [x] Source builds with no substantive warnings.

## PDF and handoff gate

- [x] All five rendered pages passed visual inspection after the final edit.
- [x] PDF metadata, page count, file size, and audit-only digest are recorded
  in `audit/PDF_AUDIT.md`.
- [x] Final status is Certified finite result.
- [x] No proof assistant was used.
- [x] PDF and LaTeX/source ZIP are present and the ZIP passes `unzip -t`.

Source ZIP SHA-256 (audit only):
`97e644996cac9a09247029f3478ebc3e4c3d17a51d7fec9045861ebe3e07ffa4`.
