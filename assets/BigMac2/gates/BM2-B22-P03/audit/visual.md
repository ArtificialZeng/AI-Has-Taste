# Fresh rendered-page visual audit

`manuscript/main.pdf` was rendered at 180 dpi with Poppler.  Every actual page
was opened and inspected at original rendered resolution.  The page images are
retained in `audit/rendered-pages/page-1.png` through `page-4.png`.

| Page | Material inspected | Observation |
|---|---|---|
| 1 | Title block, abstract, definitions, displayed HC4, opening attribution | Centering and margins are consistent; equations, subscripts, determinant bars, binomial coefficient, citation, and footer are fully visible and legible. |
| 2 | Context, theorem and scope disclaimer, gap formula, symmetry reduction, table caption/header and rows 1--7 | No clipped equations or text.  The longtable begins cleanly, columns align, and the continuation at the page boundary loses no row or rule. |
| 3 | Repeated table header, rows 8--27, census, coefficient formula, proof, verifier command | The repeated header is present; all five columns, en-dash ranges, proof square, equations, and monospace command fit without overlap or crowding. |
| 4 | Reproducibility/limitations, assistance disclosure, and references [1]--[3] | Paragraphs and bibliography are sharp and within margins; the arXiv URL and both DOI strings wrap/read correctly; the final whitespace is harmless. |

There are no figures or charts requiring separate data-point review.  Across
pages 1--4 there is no clipping, overlap, missing glyph, illegible text,
unintended blank page, distorted table, or substantive presentation defect.
All fonts are embedded, and the PDF metadata title/author match the rendered
title page.

**Verdict: ACCEPT.  Pages reviewed: 1, 2, 3, 4.**
