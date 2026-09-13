# Fresh rendered-page visual audit

Release job: `bigMac-00007-p02-release-e3e9934bb4ec`  
PDF: `manuscript/main.pdf`  
PDF SHA-256:
`e8e4681269c10271d5d861b1a4cd311df05506a161abd8767b18c6e2c7fc393c`

All four pages were freshly rendered at 144 dpi to
`audit/rendered/page-1.png` through `audit/rendered/page-4.png` and inspected
as images, not merely through text extraction.

| Page | Material inspected | Observation |
|---|---|---|
| 1 | title block, abstract, setup, probability definitions, first displayed SDP | Balanced margins and spacing; title, author, email, prose, subscripts, expectation symbols, and display denominators are sharp and fully visible. |
| 2 | theorem, three-case list, source comparison, cut formulas, three-row table | The theorem and citations are legible; bullets, equation tags, table rules, and all rows fit within the text block; no clipping or overlap. |
| 3 | translation-averaging lemma and proof, Fourier/CND cone derivation | Long formulas, summation limits, superscripts, proof marker, and numbered displays are clear; line breaks are natural and nothing crosses the margins. |
| 4 | cone optimization, exact-check scope, assistance disclosure, bibliography | Equations and prose are clear; both references are resolved; the DOI/URL wraps within the text block and the corrected arXiv class `math.CO` is legible. |

There are no figures, charts, or raster data visuals requiring value-by-value
source comparison.  Font inspection shows every PDF font embedded.  Page
numbers are present, there are no blank or duplicated pages, and no equation,
heading, bibliography item, or hyperlink text is clipped, overlapped, or
illegible.

**Pages reviewed: 1, 2, 3, 4. Verdict: accept.**
