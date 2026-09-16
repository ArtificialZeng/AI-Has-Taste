# Rendered-page visual audit

Release job: `primary-20260914-antiprism-total-positivity-release-0c9af236c4d2`. Date: 2026-09-14 UTC.

Verdict: **accept**. Every page of the current six-page `build/main.pdf` was freshly rendered with:

```sh
pdftoppm -r 120 -png build/main.pdf audit/release-pages/page
```

The image-viewing tool was used to inspect each of pages **1, 2, 3, 4, 5 and 6**, not merely their text extraction. The page images and hashes are listed in `audit/visual.json`, bound to the current PDF digest.

| Page | Actual observations |
|---|---|
| 1 | Title, author, affiliation, email, abstract and matrix formula are readable. The origin/context citations resolve. The final definition stays within the margins. |
| 2 | The quartic, order-22 rational coefficient and positive coefficient are clear, with their signs and exponents visible. The generating series and specialization fit. The closing reference to equation (9) wraps to a short separate line; it is readable and does not collide with the footer. |
| 3 | Leading-row and trace equations, harmonic formula and signed interpolation formula are readable. The corrected library citation renders as Lemma 2.1 of Zeng [6]; the standard interpolation source renders as [3]. |
| 4 | Lemma 2, its proof, both Stirling formulas and the complete five-row matrix fit. All rational entries and equation numbers are separated clearly. |
| 5 | The positive shifted quartic, forward recurrence, all eight fractions in Table 1 and their negative sum are readable and match the exact output. The power-sum equation at the bottom is not clipped. |
| 6 | Method attribution, finite-search limits and assistance disclosure are readable. All six bibliography entries, DOI strings, authors, years and version labels are visible and inside the margins. No unresolved citation markers occur. |

No clipped text, overlapping equations, illegible data, lost minus signs or substantive typographic defects were observed. The manuscript has one numeric table and one displayed rational matrix, both compared value by value with the exact companion output. It contains no charts or external figures requiring separate visual-data attribution. The accepted limited result-note scope is retained in title, abstract, theorem, limitations and disclosure.
