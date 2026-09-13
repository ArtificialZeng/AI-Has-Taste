# PDF audit

Status: PASS.  Date: 2026-08-30 CST.

Final file: `output/pdf/A278992_D-finite_recurrence_proof.pdf`

## File and metadata

- Pages: 4.
- Size: 312,538 bytes.
- SHA-256:
  `181de7b00cd7f4dc0806e78866f179d386b671e0fb6e3b70eb7b0f56ecaf0393`.
- Title: `Proof of the Four-Step D-Finite Recurrence for OEIS A278992`.
- Author: `Zijian Zeng`.
- Subject and keywords: present and topic-correct.
- Page size: US Letter, no rotation.
- Fonts: every listed font is embedded; no missing glyph report.
- PDF author metadata, body author, affiliation, and both email addresses match
  the user-supplied values exactly.

## Clean build

A fresh temporary directory containing only `main.tex` and `references.bib`
was built with `latexmk`/BibTeX under TeX Live 2026.  The LaTeX citation audit
reported `cited=2 bib=2 missing=0 unused=0`; the final log contains no warning,
undefined citation/reference, overfull box, or underfull box.  The final PDF is
the clean-build PDF.

## Page-by-page visual inspection

Pages were rendered with Poppler at 150 dpi and inspected at original raster
resolution.

1. **Page 1:** title, sole author, abstract, cited EGF, theorem, recurrence,
   initial values, and foot date are sharp and aligned.  No clipping or
   collision; theorem equation fits the text block.
2. **Page 2:** running header, state-system matrix, piece annihilators, row
   identity, (L_3), proposition, and multiplier are legible.  Fractions and
   matrix delimiters stay inside margins.
3. **Page 3:** Ore identity, coefficient formula, five-row table, exact series,
   and verification section are aligned.  Table rules do not touch text; the
   proof-ending square is intentional.
4. **Page 4:** limitations, AI disclosure, two references, affiliation, and
   both emails are complete.  Remaining bottom whitespace is ordinary final-
   page whitespace and contains no orphaned heading or clipped content.

No overlap, clipping, broken link text, black box, unintended blank page,
missing glyph, raster artifact, or unreadable element was found.  The clean-
build rasters were byte-identical to the inspected page rasters.
