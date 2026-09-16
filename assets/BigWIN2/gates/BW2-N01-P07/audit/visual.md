# Rendered-page visual audit

Verdict: accept. Job: `newwin-00001-p07-release-eea8aff93c71`. UTC review: 2026-09-12T08:35:50.951410+00:00.

The freshly built PDF was rendered with `pdftoppm -png -r 140 manuscript/build/main.pdf manuscript/build/release-page`. The reviewer actually opened and viewed each of the four resulting PNG pages with the image-view tool in this release context. This is not a file-existence or pdftotext-only check.

Page 1: `manuscript/build/release-page-1.png`. Title, author/affiliation/email, abstract, contextual citations, class definitions and block notation all fit and are legible. Subscripts, cubes, exceptional-part cardinality and empty-object wording match the TeX. No clipping or overlap.

Page 2: `manuscript/build/release-page-2.png`. Theorem 1 and criterion (1), cited prior-work comparison, both inverse identities and Lemma 3 with equations (2)–(3) are legible. Display spacing, sum notation, indices, page break and proof box have no collisions.

Page 3: `manuscript/build/release-page-3.png`. Continuation of the cube proof, Lemma 4 and its four-entry inequalities, main proof and Corollary 5 are legible. Equation (4) matches A+EA^2; exceptional-part summation and formal-series notation are intact. No clipping or misplaced proof box.

Page 4: `manuscript/build/release-page-4.png`. All ten sequence values and finite counts 409114, 1057, 32, and degree 100 match the recorded evidence. The direct method citation, assistance/scope disclosure and all four references appear in normal flow. Long URL/DOI strings wrap within margins; accents and author names display correctly.

There are no figures, plots or data tables requiring a separate value/axis audit. Every page is readable at the rendered resolution. The theorem/equation sequence, proof continuation, references, margins and footer page numbers were inspected. No visual correction is needed. All pages correspond to the same PDF; no source/PDF edit followed inspection.

Accepted mathematical snapshot: `fe32cd463141d526a90ca7859d55059aa1c6d3392a12234796cdd4a3af87ba8e`.
Manuscript digest: `9b400315173b3f139418af88297c0b16a3cb6a2e7e69400d2159eaef4ce21e18`.
PDF digest: `06151776bf758df940a752315bb7beb008e876a8624db1f50f278b49323ed0b5`.
