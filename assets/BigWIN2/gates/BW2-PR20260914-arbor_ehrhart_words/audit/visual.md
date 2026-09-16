# Rendered-page visual audit

Verdict: ACCEPT. Job: primary-20260914-arbor-ehrhart-words-release-df3b6d5a637c. Date: 2026-09-14 UTC.
PDF: manuscript/build/main.pdf. PDF digest: a0966dd2d7f0ae4465313fac6828dcc584637c136f7f96f29a054eb42a3c2b93.
Manuscript digest: 86d46d2a9bca82f4a491660782aab2fd6bab55254b9b392ef32d82dc8330d322.

The final PDF was rendered with pdftoppm -scale-to 1500 -png. Every final
page image audit/release-pages/page-1.png through page-6.png was actually opened
and visually inspected, after the canonical rebuild and freeze. Earlier images
were also viewed before the wrapper-only edit. Identical image hashes confirm
that the edit preserved every rendered page; actual image review was still
repeated for all six final pages. This is not a pdftotext-only audit.

| Page | Actual observation |
|---|---|
| 1 | Title, author, affiliation, abstract, polytope and content definitions are legible; large braces and all subscripts stay inside margins. |
| 2 | Theorem 1, prior-work paragraph and both lemma statements fit. Equation (7) is complete; the proof continues normally to page 3. |
| 3 | Operator proof, disjoint unions and upper/lower recurrences are legible without overlapping indices or clipped display lines. |
| 4 | Transformation proof, coefficient extraction and the box inverse are complete. The final binomial coefficient at the bottom is not cut off. |
| 5 | Proof completion, scope comparisons, support-counterexample attribution and exact counts are readable. The model-assistance limitations and all cross-references resolve. |
| 6 | All six bibliography entries and URLs are readable and fit. The dated local-author version and lack of SSRN PDF comparison are explicit in reference [6]. |

No clipping, overlaps, unreadable fonts, unresolved references or substantive
layout defects were seen. There are no charts, images or data tables in the
manuscript. Mathematical displays and the textual enumeration counts were
checked in the claim audit. The separate recovered source PDF page 1 was also
opened and shows Zijian Zeng, the exact title and 31 August 2026 date; its body
was read from TeX and PDF text, without asserting hosted-version identity.
