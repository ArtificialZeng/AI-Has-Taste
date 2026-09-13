# Rendered-page visual audit

**Verdict:** accept  
**Checked:** 2026-09-07 (Asia/Shanghai)  
**PDF:** `manuscript/main.pdf` (3 pages, A4)

Every page was rendered at 160 dpi with Poppler and inspected at original
render resolution. The review images are `audit/rendered/page-1.png`,
`audit/rendered/page-2.png`, and `audit/rendered/page-3.png`.

| Page | Material reviewed | Observation |
|---|---|---|
| 1 | Title/author block, abstract, context, Theorem 1, both in-text citations | All text and displayed mathematics are inside the page bounds; spacing is consistent; blue citation links are legible; no clipping, collision, or missing glyph appears. |
| 2 | Cross-product linearization, Proposition 2 and proof, start of rank computation | Equations, subscripts, wedges, arrows, and matrix-unit notation render clearly. The hollow square at the end of the proposition proof is the intended QED symbol. No overlap, truncation, or margin overflow appears. |
| 3 | End of rank proof, scope/disclosure, full bibliography | The final equations, section heading, prose, reference labels, en dash, multiplication signs, and DOI hyperlink are readable and within the margins. No orphaned or clipped content appears. |

There are no figures, tables, charts, or raster data visuals requiring
value-by-value source comparison. Page numbering is complete and ordered
1--3. Font embedding and text extraction were also checked in the build
audit. The theorem wording visible on pages 1 and 3 preserves the accepted
field-uniform nonexistence result and does not add an ideal-theoretic claim.

