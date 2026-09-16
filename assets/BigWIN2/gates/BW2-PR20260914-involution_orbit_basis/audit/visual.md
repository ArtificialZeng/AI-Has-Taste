# Rendered-page visual audit

Verdict: **accept**.
Release job: `primary-20260914-involution-orbit-basis-release-0d8839b8ec7d`.
Audit time (UTC): 2026-09-14T11:39:34.022643+00:00.

The final seven-page PDF was freshly rendered using `pdftoppm -png -r 120 build/main.pdf audit/release-render/page`. Each of the resulting seven PNGs was actually opened with the image viewer in this release context. Text extraction was used only as a supplement, not as visual review.

| Page | Image inspected | Observations |
|---|---|---|
| 1 | audit/release-render/page-1.png | Title, author, abstract, original/general scope, quotient displays and four-family exclusion set all fit. The affiliation/email footnote is separate from the last display and is legible. |
| 2 | audit/release-render/page-2.png | Theorem 1, straightening formula, positive weights, Corollary 2 and Hilbert series have readable subscripts, summation limits and equation numbers. The ideal-generator paragraph and citations do not overlap. |
| 3 | audit/release-render/page-3.png | The quotient and incidence formulas, determinant statement, five-cycle and vector relation are clear. Lemma 4 begins cleanly at the bottom; its proof continues normally on page 4. |
| 4 | audit/release-render/page-4.png | All three strict-score cases, odd walks, exact lower bounds and the final initial-ideal argument are readable. Long lines and display numbers remain inside the margins. |
| 5 | audit/release-render/page-5.png | The revised partition wording is clear. Inverse RSK, transposes and the three-row matching/tableau display are legible after removing the strut; the horizontal rule does not overlap its entries. |
| 6 | audit/release-render/page-6.png | The two-pair threshold and proof, complete-family argument, finite ranges and rational-rank formula are readable. The continuation to the page-7 floated table is normal. |
| 7 | audit/release-render/page-7.png | The exact evaluation table and caption are clear, with all values checked against the replay. The library citation, scope limitation and AI disclosure are visible in body flow. All seven numbered references, author names and line-wrapped URLs are resolved, legible and unclipped. |

No substantive clipping, overlap, missing glyph, unreadable equation, distorted figure or unresolved citation was found. Page-7 Table 1 matches every exact source value; the tableau configurations on page 5 match the accepted source construction. There are no data plots needing axis or uncertainty checks. Page size is A4 and the document title/author metadata are correct.

The report covers only the PDF digest in audit/visual.json. Any later source edit or rebuild requires the affected checks again.
