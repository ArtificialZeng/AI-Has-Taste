# Fresh rendered-page audit

Release job `primary-20260914-knill-dirac-domination-release-2935067edeff`.
Date: 2026-09-14 UTC. Verdict: **accept** for the current PDF snapshot.

The rebuilt five-page PDF was rendered using
`pdftoppm -r 125 -png build/main.pdf audit/release-pages/page`.
This release context actually viewed **each page 1, 2, 3, 4 and 5** using the
image-viewing tool. Earlier writing-stage images were not substituted for this
inspection. The current images and their SHA-256 values are recorded in
`audit/visual.json`.

| Page | Actual inspection |
|---|---|
| 1 | Two-line title, author/affiliation/email and abstract are legible. The general definitions and citation locators render correctly. The complete main theorem, graph-only hypotheses and sharpness statement fit within the page. |
| 2 | The closest-prior-work paragraph and unsigned absolute-value notation are readable. Incidence blocks, spectral transform, aligned sums and lemma proof fit. The proof-end box and footer are separate; no clipping at the bottom. |
| 3 | Degree majorization, variational formula and the multiline bridge inequality are aligned and legible. Odd-cycle and bipartite cases have clear labels; all radicals, inequality directions and equation numbers remain visible. |
| 4 | Endpoint, trace/rank tail and one-edge spectra are complete. The repaired QED box renders normally. Graph-screen counts, software citations and the rational certificate inequality are readable with no overlaps. |
| 5 | Exact finite counts, rational minimum and higher-dimensional limitation are visible. The library comparison and assistance disclosure are readable. All seven bibliography entries and their DOI/arXiv/web locators fit within the margins; none is unresolved or cropped. |

No figures, data charts or tables occur in the paper. Displayed equations and
numerical claims were compared with the accepted proof and frozen data in the
citation audit. All pages use consistent legible fonts, spacing and margins;
no overlap, clipped formula, missing glyph, unreadable reference or other
substantive presentation defect was observed. PDF title and author metadata
were checked separately in the build audit. All observations bind to the PDF
digest in `audit/manuscript-snapshot.json`.
