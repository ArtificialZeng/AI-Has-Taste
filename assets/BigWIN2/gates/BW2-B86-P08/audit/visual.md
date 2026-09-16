# Rendered-page visual audit

Release job: `win-00086-p08-release-c24024c4e62f`.

`build/main.pdf` was rendered at 144 dpi to four PNG images.  Every rendered
page was opened and inspected at original image resolution, in order:

1. Page 1: title, author block, abstract, context, theorem statement, displayed
   inequalities, citations, and footer are complete and legible.
2. Page 2: continuation paragraph, oriented-link section, displayed formulas,
   proof-ending symbol, Euler section, equation numbers, and footer are
   complete and legible.
3. Page 3: degree-three and disphenoid proofs, all vector formulas, equation
   number, scope-section heading, and footer are complete and legible.
4. Page 4: verification/scope text, assistance disclosure, all four reference
   entries and DOI/arXiv strings, and footer are complete and legible.

No page has clipping, overlap, missing glyphs, illegible mathematics, bad page
breaks, distorted figures, or text outside the margins.  The article contains
no charts, figures, or tables requiring value-by-value visual-source checking.
All fonts reported by `pdffonts` are embedded and subsetted, and the PDF
metadata matches the manuscript.

Verdict: **accept**.
