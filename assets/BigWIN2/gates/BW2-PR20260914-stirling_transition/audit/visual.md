# Rendered-page visual audit

Verdict: **ACCEPT**. Job: `primary-20260914-stirling-transition-release-4805c41c0f1c`. UTC date: 2026-09-14.

The final rebuilt PDF, digest `22f7c5bfe3776b76e3440bb37b6cc9731b836d1d817a01617f50e97b7978157d`, was rendered with
`pdftoppm -r 130 -png manuscript/build/main.pdf audit/release-pages/page`.
Every final page image was actually opened with the image-viewing tool after the last rebuild. This review uses the rendered pages, not text extraction alone.

| Page | Actual observations |
|---|---|
| 1 | Title, author and affiliation/email footnote are clear. Abstract and all of Theorem 1 fit; the ratio, threshold and strict-tail inequalities are intact. The revised primary-source citation and Conjecture 8.8 locator resolve. |
| 2 | Row/column comparison and abstract-only literature limitation are legible. Long section heading fits. Coefficient-ratio lemma, preservation identity, derivatives and infinite endpoint are unclipped; equation labels align correctly. |
| 3 | Finite-degree endpoint proof continues normally. H,U formulas and boundary cases are readable. The direct library citation [5] appears in ordinary text. The row product fits the line; Proposition 4 ends the page and its proof starts on page 4. |
| 4 | Both q recurrence fractions, the three-line numerator expansion after spacer removal, and the positive decomposition are readable and aligned. The telescoping proof and determinant identity fit. Threshold boundaries and k=0 remark are intact. |
| 5 | Exact-count ranges and the cycle-type sum are readable. AI assistance disclosure is explicit. All five bibliography entries and author accents render, long URLs wrap inside margins, and there are no unresolved citation markers. |

No clipping, overlapping text, unreadable glyph, misplaced formula number or substantive layout defect was found. There are no figures, charts or numerical tables requiring a separate visual data-source comparison. The displayed numerical coverage was checked against exact replay. All five final PNG hashes are recorded in `audit/visual.json`; pages_reviewed is exactly [1,2,3,4,5].
