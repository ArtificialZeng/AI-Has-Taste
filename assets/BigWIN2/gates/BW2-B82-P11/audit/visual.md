# Rendered-page visual audit

Job: `win-00082-p11-release-537ef5a321bf`

`manuscript/main.pdf` was rendered at 150 dpi and every page was actually
viewed at original rendered resolution.  Pages 1 through 5 were reviewed
exactly once after the final source change and build.

| Page | Material inspected | Finding |
|---:|---|---|
| 1 | Title, author block, abstract, introduction, citations, main theorem | Clean; title and equations fit, text and theorem directions are legible, no clipping or overlap. |
| 2 | Profiles, rank-one reduction, tail-sum criterion | Clean; all displayed equations and proof-ending symbols are legible and inside margins. |
| 3 | Finite classification, census formulas, method citation, corollary | Clean; long prose and formulas wrap correctly, citation [3] is visible, no overprint or truncation. |
| 4 | Cluster reduction, core census, sharpness proof | Clean; all inequalities, tuples, and concluding paragraph are legible and within the page. |
| 5 | Data/assistance disclosure and four references | Clean; all four references are readable, with no collision, clipping, or missing glyph. |

No figures or charts are present.  Page numbering, section hierarchy,
mathematical symbols, proof boxes, fonts, and bibliography labels render
consistently.  The white space below the short bibliography on page 5 is a
normal consequence of the manuscript length, not missing content.

Rendered evidence: `audit/rendered-pages/page-1.png` through
`audit/rendered-pages/page-5.png`.
