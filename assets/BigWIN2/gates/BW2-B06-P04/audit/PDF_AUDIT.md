# PDF audit

Status: **PASS**

Final artifact: `output/pdf/unique_nac_n11_submission.pdf`

## Mechanical validation

- Six letter-size pages; unencrypted; no form fields or JavaScript.
- PDF title and author metadata match the manuscript and Zijian Zeng.
- All fonts reported by `pdffonts` are embedded.
- Final LaTeX log contains no warning, undefined reference, overfull box,
  underfull box, fatal error, or multiply-defined label.
- Extracted text contains the theorem totals and scope limitation, and contains
  no hash, model/vendor name, internal role/route identifier,
  completion/confidence score, or internal audit phrase.
- Static citation audit remains 8 cited keys, 8 bibliography entries, 0
  missing, and 0 unused.

## Page-by-page visual inspection

All pages were rendered at 150 dpi with Poppler and inspected at original
rendered resolution after the last source change.

1. Title, author, abstract, opening definitions, citations, footer, and subject
   classification are aligned and legible.
2. Main theorem, scope paragraph, Laman definition, NAC definition, displayed
   formula, and connectivity lemma have clean breaks and margins.
3. Open-step lemma, one-open-step proposition, proof symbols, and stable-cut
   equation are complete with no clipping.
4. Family-A formula, four certificate types, and section transition are
   legible; links do not obscure text.
5. Five verifier checks, the four-way count table, theorem proof, and build
   command are aligned with no table or margin overflow.
6. Reproducibility limitations, data statement, all eight references,
   affiliation, and both email addresses are present and readable.

No overlap, clipping, missing glyph, black square, broken table, or defective
page transition was found.

## Archive tests

- `output/latex/unique_nac_n11_latex.zip` contains only `main.tex`,
  `references.bib`, and `BUILD.md`.  It was extracted into a newly created
  empty directory and built with `latexmk`; the independent build produced a
  clean six-page PDF with the same title, author, page size, and file size.
- `output/reproducibility/unique_nac_n11_reproducibility.zip` passed ZIP
  integrity testing.  It was extracted into a separate new directory; its
  build script recompiled the verifier, accepted all 2,039,273 certificate
  rows, and passed all eight adversarial mutations.
