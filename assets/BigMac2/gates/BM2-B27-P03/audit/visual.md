# Fresh rendered-page visual audit

## Method and binding

The current `manuscript/main.pdf`, SHA-256
`ff88f4f1cd608d26134d5ed87844085916170e844a65e79d7fa88364cf8396f9`,
contains four pages according to `pdfinfo`.  I rendered the current PDF at 160
dpi with Poppler to `audit/render/page-1.png` through
`audit/render/page-4.png` and visually inspected every rendered page at original
image resolution.  I also compared the visual content with the layout-preserving
text extraction and checked the font inventory.

## Page-by-page observations

| Page | Material inspected | Observation |
|---|---|---|
| 1 | Two-line title, author block, abstract, definitions, contextual citations, morphism display, and Theorem 1 | All text and symbols are sharp; title and author block are centered; abstract and theorem fit within margins; citations [1]--[3], subscripts, inequalities, and the displayed morphism are legible.  No clipping, overlap, stray marker, or orphaned heading. |
| 2 | Equivariance equation, Lemmas 2--3 and proofs, four representative pairs, start of finite-certificate section | Equation number (1), proof boxes, exponents, modulo notation, and all four pair labels are aligned and readable.  Paragraphs and display equations have adequate spacing and remain inside the text block. |
| 3 | Exhaustive-sweep formulas and counts, citation [4], theorem proof, scope/reproducibility text, and command block | The summation and fraction are unambiguous; the integer 737,875,320 is not clipped; citation [4] resolves visually; code lines are fully visible with no right-margin overflow; section transition and proof box are clean. |
| 4 | Closing computational/AI disclosure and four bibliography entries | Heading hierarchy and paragraph spacing are consistent.  All authors, titles, mathematical `N^16`, DOI/arXiv strings, and wrapped URLs are legible and remain inside the margins.  Reference [4] and its DOI are complete. |

The paper contains no charts, figures, tables, color-dependent elements, or
raster scientific data requiring value-by-value visual verification.  All
fonts are embedded and subsetted.  Page numbers are present and ordered 1--4.
Whitespace is balanced, hyperlinks do not obscure text, and there are no
clipped equations, overlapping objects, missing glyphs, unreadable lines, or
substantive typography defects.

## Verdict

**Accept.** Pages 1, 2, 3, and 4 of the current bound PDF were actually rendered
and inspected, and all are submission-ready.
