# Rendered-page visual audit

**Verdict: accept.** Job `newwin-00001-p13-release-e80ab705955d`; UTC 2026-09-12T10:22:27.030551+00:00.

The current nine-page PDF was rendered using `pdftoppm -r 110 -png`. Every individual page image was actually opened with `view_image` and examined in this worker. No clipping, overlapping content, missing glyph or illegibility was found. There are no plots or external figures. The numerical table and orbit table were also compared directly with accepted raw data by `audit/release_verify_artifacts.py`.

| Page | Observation |
|---:|---|
| 1 | Title, author and affiliation are legible. Abstract, q-hit definition, integral weight and residue display fit within margins; citations [2]-[4] resolve. |
| 2 | Theorem 1 retains the universal square-board statement. Convolution equations and inverse are legible; citation locators and sums do not collide. |
| 3 | Operator lemma and component-defect formula are clearly set. Citations to the diagonal method and small-component polynomiality are visible. No clipped subscripts. |
| 4 | The complete dummy-permutation patch argument and its displayed cardinalities are readable. Proof terminator and the signed orbit example are separated cleanly. |
| 5 | Weight coefficient formulas, differential-operator identity and locality theorem are legible. The universal sum near the page bottom is above the footer with no overlap. |
| 6 | The finite-certificate proof and all four rows of the enumeration table are legible. Counts, minima and maxima match the raw-data transcription check. The main-theorem conclusion is present. |
| 7 | All verification totals are legible, including 83,919, 989,340, 329,780, 2,907, 282,701 and 6,300. Direct library citation [6], preprint scope comparison, reproducibility and assistance disclosure are visible. |
| 8 | All 28 orbit-table rows are visible on one page. Masks, signs, powers and the three rank columns are readable with no overlap. The narrowest final rows still separate the polynomials. |
| 9 | All six bibliography entries are visible and match their keys and verified metadata. Accented names, q notation, page ranges and wrapped URLs are readable; no overflow or missing reference. |

Rendered image paths and hashes are recorded in `audit/visual.json`. These observations apply to PDF digest `03aafbb8438b545795ef0dce60b93227c846381a78d5f070d1a283b09eb6644d` and manuscript digest `69f0c0877e7662597fc452e956d04ade99877f4da48524144a92a7980f33837e`. The PDF and source were not edited after rendering or inspection.
