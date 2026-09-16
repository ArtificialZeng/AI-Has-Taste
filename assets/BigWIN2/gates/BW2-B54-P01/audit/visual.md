# Rendered-page visual audit

## Result

**PASS.**  `manuscript/main.pdf` was rendered at 150 dpi with `pdftoppm`, and
each of its four pages was inspected at original rendered resolution.  The
review was visual, not inferred from `pdftotext`.

| Page | Material inspected | Findings |
|---|---|---|
| 1 | title block, author/address, abstract, context, displayed matrices and equation (1) | Clean margins and line breaks; title and affiliation are legible; no overlap or clipping; citations render as numeric links. |
| 2 | Theorem 1, scalar reduction, equations (2)--(6), start of unit-orbit section | Theorem statement is complete; matrices, radicals, subscripts and equation numbers are legible and aligned; no orphaned heading or collision. |
| 3 | unit parametrization, equations (7)--(8), enumeration, very large lag-22 entries | Long integers and the wide witness matrix remain inside the text block and are readable; no margin clipping, overlap, or glyph substitution. |
| 4 | end of proof, reproducibility/AI disclosure, complete bibliography | Scope disclaimer and assistance disclosure are clearly visible; all eight references render completely; long DOI/URL text wraps within the page; no clipped footer. |

Global checks: all pages use consistent margins, running text size, heading
hierarchy, equation numbering, and page numbering.  There are no charts,
figures, tables with numerical graphics, colored elements, truncated axes, or
external raster images requiring a separate data-integrity review.  The rendered
mathematical statement does not strengthen the accepted scope: unrestricted SSE
remains expressly unresolved on pages 1 and 4.  All fonts are embedded and all
visible symbols inspected correctly.

Reviewed renderings:

- `audit/rendered-pages/page-1.png`
- `audit/rendered-pages/page-2.png`
- `audit/rendered-pages/page-3.png`
- `audit/rendered-pages/page-4.png`
