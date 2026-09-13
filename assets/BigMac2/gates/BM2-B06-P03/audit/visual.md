# Fresh rendered-page visual audit

Job: `bigMac-00006-p03-release-45c673bd9503`. Date: 2026-09-08.
Verdict: **accept**. PDF: `manuscript/main.pdf`. Pages reviewed: **1, 2, 3**.

I freshly rendered the unchanged current PDF with
`pdftoppm -png -r 120 manuscript/main.pdf evidence/release-render/page` and
opened each of the three PNGs as images. This review is based on actual page
images, supplemented by text extraction and fonts inspection. The images and
their hashes are retained in the release evidence.

| Page | Image | Direct observations |
|---|---|---|
| 1 | `evidence/release-render/page-1.png` | The complete title and its b-bar superscript/subscripts fit within the page. Author, affiliation, email, abstract, and heading are legible. Infinite products, exponents, fractions, equation numbers (1)--(3), and formal-series notation have intact glyphs. The source's k=4 caveat is visible at the bottom with safe separation from page number 1. No clipping, collisions, or unresolved citation markers. |
| 2 | `evidence/release-render/page-2.png` | Theorem 1, proof, divisor-sum cases, recurrence, coefficient vectors, final integer calculation, and proof square are clear. Equation labels (4)--(5) align without collision. Both literature-comparison paragraphs fit above the footer, including the methods-only workbook citation [2]. Dense content remains legible, with no overlapping baselines, broken mathematical glyphs, or clipped right margins. |
| 3 | `evidence/release-render/page-3.png` | The computational/AI disclosure and both full bibliography entries are complete and readable. Names, title, arXiv version, date, and supplied DOI/URL render clearly. Line breaks stay within the margins. The page is intentionally less full, with no orphaned content or missing continuation. Footer 3 is unobstructed. |

The page count is independently three according to `pdfinfo`. There are no
charts, graphs, figures, numerical tables, or diagrams requiring separate
visual-data provenance checks. The displayed exact numbers agree with the
accepted proof and the fresh recurrence calculation. All page images were
viewed; no contact-sheet-only or text-only substitute was used.

The relevant workbook record and methods-only use were inspected in
`literature/user_bibliography_check.md`; the source bibliography and PDF were
preserved unchanged. This visual acceptance applies only to the current
PDF digest recorded in `audit/visual.json`.
