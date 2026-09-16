# Rendered-page visual audit

Verdict: accept. Job `newwin-00001-p19-release-825c1e67cb4c`, 2026-09-12 UTC.

Rendered the final six-page PDF at 130 dpi with `pdftoppm -r 130 -png manuscript/build/main.pdf audit/release-render/page`. Actually opened and inspected each individual image with `view_image`; pages 1, 2, 3, 4, 5 and 6 were all seen. Text extraction was supplementary only. Rendered image hashes and their binding to the final PDF appear in `audit/release-render-manifest.json`.

| Page | Content inspected | Finding |
|---|---|---|
| 1 | Two-line title, author, abstract, definitions, original-paper citations, periods and rational constants, affiliation/email footnote | Readable. The lower fraction and footnote are distinct; no overlap or clipping. Scope is explicitly j=2. |
| 2 | Main theorem, separated subsequences, CRT citation, positive-membership proof and cutoff | Formulas, delimiters and equation numbers are readable and within margins. No undefined reference markers. |
| 3 | Counting lemma/proof, full residue-count table and complete enumeration code, exact beta sum | All eight table counts and all code lines are visible; no truncated code, equation or table. |
| 4 | Prime/prime-square classification, CRT proportions, both density formulas, exact C0 and final theorem proof | All cases, exponents and fractions are readable. Heading/proof flow is intact. |
| 5 | All 18 density fractions, caption, finite corollary and gap, computation scope, method citations, AI disclosure | Long rational values remain in the table. Sufficient threshold and higher-iterate limitations are explicit. All text is legible. |
| 6 | Three complete reference entries, journal article number, second edition/year, preprint version/date, URL and DOI | Natural line wrapping, full metadata visible, no clipping. The mostly unused lower page is normal bibliography pagination. |

There are no plotted figures or charts. The two tables contain only exact values; every value was checked against the arithmetic evidence. All fonts are embedded, and PDF metadata has the correct title and author. No clipping, overlapping text, missing symbols, illegible type or unresolved citation markers were found.

`audit/visual.json` records exactly pages [1,2,3,4,5,6] and the final manuscript/PDF snapshot. PDF digest: 65180f3d38bed38a49108150ab3c8efe277ebc78f4ec7d5b1ffbe5c901766bb3.
