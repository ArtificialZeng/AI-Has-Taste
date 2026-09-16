# Fresh rendered-page visual audit

Verdict: **accept**. Job: `primary-20260914-grid-narayana-release-a978c20a048a`.
UTC date: 2026-09-13. Reviewed PDF: `build/main.pdf`.

The release worker rendered the final clean-built PDF with
`pdftoppm -r 125 -png build/main.pdf audit/release-page` and actually viewed each of the six resulting images using the image-view tool. This review does not reuse the writer's page observations. The PDF was not rebuilt or edited afterward.

| Page | Image | Actual observations |
|---|---|---|
| 1 | `audit/release-page-1.png` | Title, author, affiliation, and abstract are readable. The two polytope/enumerator definitions, Narayana normalizations, and Theorem 1 fit the page. The origin/statistic and separate-factor citations show resolved labels and source locators. No clipping or overlap. |
| 2 | `audit/release-page-2.png` | Prefix inequalities, slack updates, half-step sums, and transformed operators are legible. Equation numbers (3)-(8) remain clear. The final unnumbered display is fully inside the bottom margin; the sentence continues naturally on page 3. |
| 3 | `audit/release-page-3.png` | Moment and commutator notation, finite trace, Lemma 2, boundary indices/signs, and derivative display are readable. Both cutoff paragraphs and the proof-ending square fit without collisions. |
| 4 | `audit/release-page-4.png` | Motzkin and inversion citations resolve to the correct entries. The logarithmic series, aligned integration-by-parts identity, Lagrange coefficients, residue, and final coefficient sum are readable. No missing symbols or clipped subscripts. |
| 5 | `audit/release-page-5.png` | The telescoping equality remains clearly aligned after removal of manual spacing. Final binomial factors and exceptional-case statements are readable. The selected library citation is visible in ordinary prose; all six counts and seven parameter pairs are legible. The computational disclosure fits above the footer. |
| 6 | `audit/release-page-6.png` | All five bibliography entries are visible, with resolved numbering, readable author/title/year information and intact links. Natural line breaks in long titles/URLs do not clip or overlap. The lower page is blank after the bibliography. |

There are no charts, figures, or data tables requiring an additional visual data audit. Mathematical displays and finite numerical statements were compared with the accepted proof and saved exact-check output in the claim audit. Across pages 1-6, no illegible font, clipping, overlap, unresolved reference marker, or substantive presentation defect was found.

`audit/visual.json` binds pages `[1,2,3,4,5,6]` and their image hashes to the current manuscript, PDF, and accepted mathematical snapshot. Viewing the PDF is a presentation check, not external peer review.
