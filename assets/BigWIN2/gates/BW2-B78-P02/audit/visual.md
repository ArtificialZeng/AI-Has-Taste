# Rendered-page visual audit

Release job: `win-00078-p02-release-382a564d0f4a`.

`manuscript/main.pdf` was rendered at 144 dpi to five PNG images. Every page
was opened at original image resolution and inspected in order:

1. Page 1: title, author block, abstract, context, citations, finite-scope
   qualification, complex list, ordering convention, and footer are complete
   and legible.
2. Page 2: matrix definitions, filters, normalization, theorem statement,
   witness matrices, displayed formulas, equation numbers, and footer are
   complete and legible.
3. Page 3: exact cofactor calculation, steady-state identity, determinant,
   minimal-pair discussion, enumeration setup, lemma, proof text, and footer
   are complete and legible.
4. Page 4: lemma conclusion, all seven audit-table rows, minimality argument,
   scope and reproducibility discussion, code-style text, and footer are
   complete and legible.
5. Page 5: assistance disclosure, all four reference entries, DOI/arXiv text,
   and footer are complete and legible.

No page has clipping, overlap, missing glyphs, illegible mathematics, a bad
page break, distorted graphics, or content outside the margins. The sole table
uses an honest linear layout with no graphical encoding; its seven values agree
exactly with `evidence/census-summary.json` and the accepted mathematical audit.
The article contains no charts or figures requiring value-by-value visual-source
comparison. All fonts reported by `pdffonts` are embedded and subsetted, and
the PDF metadata agrees with the manuscript.

Verdict: **accept**.
