# Fresh rendered-page visual audit

Release job: `bigMac-00029-p13-release-2f9da8670649`  
PDF: `manuscript/main.pdf`  
Actual page count: 5

The final PDF was freshly rendered with Poppler at 144 dpi to `audit/rendered/page-1.png` through `page-5.png`. Every page was opened and inspected at original image resolution, not inferred from text extraction.

| Page | Observations |
|---|---|
| 1 | Title, author block, abstract, first section, displayed products/equations, citation `[1]`, margins, and footer are sharp and fully inside the page. No clipping, overlap, or malformed glyph is visible. |
| 2 | Lemma 1, proof, Remark 34 comparison, the narrowed Zeng title-level comparison and citation `[2]`, theorem statement, equations, proof mark, margins, and footer are legible with consistent spacing. |
| 3 | Generator equation, Lemma 3, prose, profile formula, propositions, proof marks, and footer are legible. No line or equation crosses a margin. |
| 4 | Table 1 has all 24 rows, five aligned columns, intact rules, and readable headings. The local-certificate table, propositions, equations, proof text, proof marks, and footer are unobstructed. |
| 5 | Table 2, theorem conclusion, scope/reproducibility section, verbatim commands, AI-assistance disclosure, both complete bibliography entries, and footer are legible. The page is neither blank nor crowded, and no bibliography line is clipped. |

Across all five pages, text density, font size, equation alignment, table rules, white space, page numbering, and running order are consistent. There are no figures requiring separate legend or data-point checks. All fonts are embedded; the PDF metadata contains the manuscript title and author.

## Verdict

**ACCEPT.** Pages 1--5 were actually seen and have no substantive typography, clipping, overlap, blank-page, or legibility defect.
