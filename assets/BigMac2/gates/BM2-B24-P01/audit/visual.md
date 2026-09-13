# Fresh rendered-page visual audit

Audit date: 2026-09-09.  The frozen PDF was rendered afresh with `pdftoppm` at
150 dpi.  I opened and inspected every page image at original rendered
resolution, not merely extracted text.  The reviewed images are
`audit/rendered/page-1.png` through `audit/rendered/page-5.png`.

| Page | Observation |
|---:|---|
| 1 | Title, author block, abstract, map formula, theorem, and citations are sharp and within margins; no collision or clipped line. |
| 2 | Long exact integers, fractions, equation numbers, and proof text remain legible; all display widths fit the text block. |
| 3 | The page break from Lemma 2 is coherent; both proof-end marks, threshold inequalities, and equation numbers render correctly. |
| 4 | Critical-point list, multiplicity sum, asymptotic formula, and postcritical-set display are clear; the final paragraph continues normally to page 5. |
| 5 | Continued proof, scope/disclosure text, and all five bibliography entries are readable.  DOI and title wrapping is conventional and does not overlap. |

The page size and orientation are consistent throughout.  Margins, baseline
spacing, math fonts, superscripts, hats, calligraphic symbols, en dashes, and
reference numbering are visually sound.  No page has clipping, overlap,
illegible text, missing glyphs, unintended blank regions, malformed equations,
or broken links visible as print artifacts.  There are no figures, charts, or
data tables requiring a separate value-by-value visual check.

Pages reviewed: 1, 2, 3, 4, 5.  Verdict: accept.
