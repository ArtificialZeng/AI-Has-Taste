# Fresh rendered-page visual audit

Release job: `bigMac-00011-p02-release-8e7a7826a299`  
Bound PDF: SHA-256 `f1561ebd6cb8af5486dd854ca5544d1f49567b0214ba6d35f9a5509f06e9a8d6`

I rendered the current PDF with Poppler at 150 dpi and inspected every page
image at original rendered resolution.  The document contains no figures or
charts; the visual data checks therefore concern the two classification/data
tables, displayed formulas, equation numbers, references, and typography.

| Page | Observation |
|---|---|
| 1 | Title, author block, abstract, section heading, definitions, formulas, and citations are sharp and inside the margins. The two-line title and long admissible-set display are balanced and unclipped. |
| 2 | The complete 16-row classification table is legible, aligned, and contained within the text block. Theorem and Lemma 2 displays have adequate spacing; the proof-ending symbol and equation (1) are intact. |
| 3 | Lemma 3, the small zero-weight table, Proposition 4, and equations (3)-(4) are fully legible. No proof text or right-side equation number collides with a margin. |
| 4 | Both piecewise formulas, regular probe displays, section transitions, and the opening of Section 5 are clear. Braces, exponents, and inequality signs render correctly. |
| 5 | Both starting-level tables and suffix-equivalence displays are aligned and readable. Dense boundary prose remains comfortably within both margins with no crowding or overlap. |
| 6 | The boundary-regime table is aligned and fully visible. Completion text, exact counts, AI disclosure, and all three bibliography entries are readable; the final reference wraps cleanly above the footer. |

Across pages 1--6, page numbers are consistent; margins and hierarchy are
consistent; all mathematical glyphs are readable; there are no clipped or
overlapping elements, broken tables, black boxes, missing glyphs, stray tool
tokens, or visibly unresolved references.  Font embedding was separately
confirmed with `pdffonts`.

**Verdict: accept.**

