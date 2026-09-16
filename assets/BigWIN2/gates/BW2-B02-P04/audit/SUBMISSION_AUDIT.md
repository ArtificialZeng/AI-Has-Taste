# Submission-readiness audit

Overall status: **PASS for a journal-neutral preprint/submission package**, 2026-08-29.

This status means that the manuscript package passes the project's mathematical,
source, metadata, and rendering gates. It does not imply peer review, journal
acceptance, or an unbounded novelty claim.

## Mathematical gate: PASS

- The locked theorem matches the requested \(n=7\), \(1<r<2\) endpoint.
- All 64 canonical cuts, all 189 directed comparisons, and all equality cases
  are covered by exact arithmetic.
- Fatal and major proof gaps: zero.
- The certificate has an independent standard-library verifier, and mutation
  tests reject altered or incomplete records.
- Numerical exploration is identified as discovery evidence only, never as the
  theorem's proof.

## Originality, novelty, and citation gate: PASS with bounded wording

- Mari\'c's prior public result is accurately credited for the isolated-cut
  phase diagram and for Conjecture 5.1.
- The present result is distinguished as the global continuous \(n=7\) proof
  over all 64 cuts, with the complete tie classification.
- Recorded searches through 2026-08-29 found no prior exact continuous proof of
  that endpoint. The manuscript expressly limits this statement to those
  searches and does not claim knowledge of unpublished or unindexed work.
- The sole bibliography entry supports every nearby attribution; the citation
  audit reports `cited=1 bib=1 missing=0 unused=0`.
- The source is described as arXiv v1, not as a peer-reviewed publication.

## Author and manuscript gate: PASS

- Author: Zijian Zeng.
- Affiliation: Institute of Computer Science and Digital Innovation, UCSI
  University, Kuala Lumpur 56000, Malaysia.
- Emails: `zijianzeng@foxmail.com` and
  `1002266693@ucsiuniversity.edu.my`.
- The source uses the requested journal-neutral `amsart` format.
- No target journal was assumed. No funding statement or acknowledgments were
  invented or printed.
- No placeholder author, affiliation, or email remains.
- ChkTeX, citation audit, BibTeX, and the final three-pass LaTeX build are clean.

## Reproducibility and package gate: PASS

- The ZIP contains `main.tex`, `references.bib`, `README.md`, the locked formal
  statement, the exact certificate, and the independent verifier.
- A fresh extraction passed the exact verifier and rebuilt the five-page PDF
  with BibTeX and three LaTeX passes without warnings.
- No proof assistant was used.

## PDF gate: PASS

- All five rendered pages were visually inspected.
- PDF metadata identifies Zijian Zeng and the correct title.
- Extracted-text scans found no forbidden internal identifiers, hashes,
  placeholders, fabricated metadata, or internal AI-audit language.
- Full findings are recorded in `audit/PDF_AUDIT.md`.

