# PDF audit

Audit date: 2026-08-29 (Asia/Shanghai). Final source audited:
`paper/main.tex`; rendered artifact: `paper/main.pdf`.

## Build and metadata

A clean temporary-directory build from only `main.tex` and `references.bib`
completed under pdfTeX 1.40.29 / TeX Live 2026 using
`latexmk -pdf -interaction=nonstopmode -halt-on-error`. The converged log
contains no undefined citation/reference, overfull or underfull box, or
package/LaTeX warning.

| Field | Audited value |
|---|---|
| Title | The n=5 case of Lentfer's (1,2)-bosonic-fermionic coinvariant basis conjecture |
| Author | Zijian Zeng |
| Pages | 5 |
| Page size | 612 x 792 pt (US Letter) |
| Local PDF bytes | 356399 |
| Local PDF SHA-256 | `371018beb64598ae541912982284da690d461287e8cac30108cf5ed2f6575e0a` |
| PDF version | 1.7 |

The clean-build PDF has the same content and metadata but a different
timestamp-dependent digest,
`d62878cd4b163acf310318a50d97f41c47ae734d97c484c7714b793fe00ef8a2`.

## Page-by-page visual inspection

Every page was rasterized with Poppler at 150 dpi and inspected at original
render resolution.

- Page 1: title, author, abstract, citation, theorem statement, running text,
  margins, and footer are intact; no clipping or overlap.
- Page 2: definitions, odd-variable order, Motzkin/alpha formula, canonical
  sign note, and generator proposition render correctly. An earlier visual
  pass exposed a literal `qquad` typo in the alpha formula; the missing
  backslash was repaired, the PDF was rebuilt, and the corrected spacing was
  rechecked.
- Page 3: orbit-sum proof, displayed kernel-partition identity, Newton
  recurrence, result table, and theorem proof are aligned and legible.
- Page 4: verifier checklist, independent Artin--exterior/FLINT audit, SHA-256
  digest, and reproduction command have no overflow or broken glyphs.
- Page 5: limitations, AI/computational disclosure, proof-assistant statement,
  reference, affiliation, and both email addresses are complete and legible;
  final-page whitespace is balanced and contains no orphaned element.

## Verdict

PASS. No clipping, overlap, missing glyph, black box, broken reference, or
metadata/authorship discrepancy remains in the inspected final PDF.
