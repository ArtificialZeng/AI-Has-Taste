# Rendered-page visual audit

Verdict: **accept**. Job:
`primary-20260914-q-product-unimodality-release-a0a2d6a0e9ce`.
The final four-page PDF was rendered after the clean build using
`pdftoppm -scale-to 1800 -png manuscript/build/main.pdf manuscript/build/release-page`.
Every resulting page was actually opened with the image-view tool in this
release context. Text extraction was used additionally, not as visual review.

| Page | Image inspected | Observations |
|---|---|---|
| 1 | `manuscript/build/release-page-1.png` | Title, author, date, abstract, parent conjecture, and complete main theorem are legible. Floor brackets and divisibility symbols render correctly. The affiliation footnote fits below the body without overlap. Citations and equation numbers resolve. |
| 2 | `manuscript/build/release-page-2.png` | The context paragraph continues naturally from page 1. Centered-interval expansion, divisibility factorization, midpoint comparison, count identity, and residue parameters fit the margins. Subscripts, superscripts, summation limits, and equation numbers remain distinct. |
| 3 | `manuscript/build/release-page-3.png` | Both proof directions, clipped maximum, floor estimates, residue indicators, witness difference, endpoint bound, proof box, and factor-1 discussion are visible. No equation is clipped or collides with its number or surrounding prose. |
| 4 | `manuscript/build/release-page-4.png` | All example coefficients, exact computational ranges and counts, methodological citation, scope, assistance disclosure, and three references are readable. The wrapped arXiv URL and both DOI identifiers are complete. Bibliography text fits above the footer without overlap. |

All pages have clear margins, legible mathematical fonts, resolved citations,
and ordinary pagination. No figures, charts, or data tables occur in the paper;
the displayed coefficient sequence was checked value-by-value against exact
arithmetic in `audit/release-verification.json`. The PDF metadata, extracted
references, and font embedding were also checked by the build audit.

`audit/visual.json` binds pages `[1,2,3,4]`, the current manuscript/PDF/evidence
digests, and the hashes of the actual images inspected. No source or PDF edit
was made after rendering and inspecting these pages.
