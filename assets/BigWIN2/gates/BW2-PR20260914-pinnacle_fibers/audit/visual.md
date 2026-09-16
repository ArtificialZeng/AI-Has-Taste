# Rendered-page visual audit

**Verdict: accept.** Release job:
`primary-20260914-pinnacle-fibers-release-9c1ceac429e4`.
UTC date: 2026-09-14.

The final PDF is `manuscript/build/main.pdf`, with three pages reported by
`pdfinfo`. I rendered it using `pdftoppm -r 130 -png` and actually opened
each of `release-preview/page-1.png`, `page-2.png` and `page-3.png` with the
image-viewing tool. Each image is 1105×1430 pixels. This assessment uses
those rendered images in addition to the text extraction.

| Page | Actual observations |
| --- | --- |
| 1 | Two-line title, author, affiliation and email are legible. The abstract and first section fit inside the margins. Inversion subscripts, inverse-permutation notation, the middle-order symbol and citations [1]–[4] render correctly. The last paragraph continues normally onto page 2; no text is clipped. |
| 2 | The theorem and complete proof fit. Both tables have clear columns and all nine data rows are readable. I checked the five named permutation rows and the four lower-box rows against the source and exact replay. Equations (1)–(3), meet/join signs, the unequal concluding permutations, and proof-ending square are visible. The last proof line and page number remain separate. No overlap or illegible symbol was observed. |
| 3 | The counts 120, 56 and 25, verifier description, method citation [5], bound-set formulas and scope limits are readable. The assistance disclosure is distinct from the references. All five bibliography entries, including complete wrapped DOI strings and the preprint/version label, stay inside the margins. There is no unresolved citation marker or nearly empty extra page. |

The paper has no plot or externally sourced graphic. Its two mathematical
tables were verified entry by entry; their values are exact and involve no
rounding, axis scaling or visual uncertainty. No clipping, overlap, missing
glyph or substantive presentation defect was found. `visual.json` records
the exact reviewed page list and binds this review to the current PDF and
manuscript snapshot; `release-render-manifest.json` binds the PNG bytes to
the same PDF.
