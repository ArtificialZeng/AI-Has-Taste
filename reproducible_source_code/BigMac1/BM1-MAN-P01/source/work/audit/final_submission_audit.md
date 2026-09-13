# Final submission audit

## Scope

This audit covers the partial-result paper proving the exact spectrum of the
Bapat--Sunder permanental-minor matrix on regular real projective polygons.
It does not claim an order-at-most-15 real counterexample, a finite-dimensional
exclusion, or the unrestricted real conjecture.

## Mathematical gate

- Analytic proof: PASS.
- Independent definition-level cyclotomic reconstruction for orders 3--8:
  PASS.
- Normal and optimized verifier outputs: byte-identical.
- Wrong-phase, wrong-factor, and wrong-binomial attacks: rejected.
- Referee findings: 0 fatal, 0 major, 0 minor.

## Bibliographic gate

- Four cited records were checked against official journal/DOI records.
- Every cited key is present in `references.bib` and in the generated `.aux`.
- No unresolved or uncited BibTeX entry remains.

## Build and presentation gate

- `latexmk`/BibTeX build: PASS with no undefined citation, undefined
  reference, overflow, or LaTeX error in the final log.
- Final page count: 4.
- All four rendered pages were inspected at 150 dpi: no clipping, overlap,
  broken glyph, or illegible formula was found.
- Author affiliations and email addresses are present; Yonghua Xiong carries
  an asterisk and is explicitly labelled `Corresponding Author`.

## Archive gate

The final ZIP preserves the `paper/` and `literature/` layout required by the
bibliography path and includes the exact proof, independent verifier and JSON
audit, numerical reconnaissance engine and frozen aggregate summary, citation
audit, ledgers, and final PDF.  A clean extraction/build check is recorded in
the final manifest workflow.

## Verdict

PASS: submission-ready for the stated infinite-family partial theorem.
