# Rendered-page visual audit

Job: `primary-20260913-binary-subsum-shape-release-b63927b8723e`. Verdict: **accept**. Inspected 2026-09-13T00:42:04.160819+00:00.

The final PDF was rendered with `pdftoppm -png -r 120 manuscript/build/main.pdf audit/rendered/page`. Every rendered image was actually opened and viewed using the image tool, in groups 1-3, 4-6 and 7-9. Text extraction was auxiliary, not a substitute for visual inspection. The images are 1020 by 1320 pixels; all nine pages have been seen. No figure uses statistical axes, rounding or uncertainty graphics; the tables are exact symbolic substitutions and integer data.

- **Page 1:** Title, author/affiliation/email and partial-scope abstract readable; definition, corrected n>=6 conjecture and recurrence fit inside margins; citation numbers and optional source locators are visible.
- **Page 2:** All three theorem parts, rational criterion and mean-bound lemma are legible; floors, inequalities, subscripts and equation tags are intact.
- **Page 3:** Mean-bound proof and coefficient envelopes readable; coefficientwise-order symbol preserved after alias expansion; displayed uniform estimates fit above the footer.
- **Page 4:** Ratio argument and initial coefficient identities fit without collisions; prior attributions visible; fractions and equation tags remain clear.
- **Page 5:** First/second-position proof and four-row chamber table readable; all table entries checked against the accepted substitutions; the floating table after the phrase In particular causes no loss of content.
- **Page 6:** Quartic and polarized kernel formulas, lemma, tails and power sums readable; the revised ordinary-math indentation preserves every term and has no clipping.
- **Page 7:** Four-row K3 chamber table, parity threshold, certificate counts and strictness comparison readable; every table entry agrees with the accepted chamber formulas; tags do not overlap text.
- **Page 8:** Both small-n triples and Turan values, all eight dyadic table entries, interpolation/SymPy/library citations and limitations are visible and exact; assistance paragraph continues normally onto page 9.
- **Page 9:** Assistance disclosure continuation, all six appendix arrays and all five bibliography entries readable. Long author list and URLs wrap inside margins. The appendix arrays contain the exact 42 coefficients checked separately.

No clipping, overlap, unreadable glyphs, missing mathematical symbols, broken bibliography text or unresolved cross-reference markers were found. Table and appendix numbers were compared to their exact source/certificate values; see `audit/release-numeric-check.json` and `audit/release-verification.json`. The manuscript preserves the accepted boundary-only scope.

PDF SHA256: `0f292bc7d40735ca4fe719110e0e9a7f613c6095415ccb903f9ec0f7a3de280d`. Manuscript digest: `d06ec580b55b37058246c2ae5e7cbc8175b2b13f0432c84821dfbee48d3510f1`. The final supplement-only comment edit left these rendered PDF bytes unchanged.
