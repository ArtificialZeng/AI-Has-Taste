# Rendered-page visual audit

PASS. Job primary-20260913-chen-ulc-failure-release-6faab700d5ab; checked 2026-09-12T22:57:21.251568+00:00.

I actually viewed all five newly rendered page images, individually displayed by view_image in this release context. pdftotext was only an auxiliary check. Rendering used pdftoppm at 140 dpi from the current built PDF. No page was inferred from its existence or from an earlier visual verdict.

- Page 1: Title, abstract, family definitions, normalization, Theorem 1 and affiliation footnote are legible; the full theorem fits without overlap.
- Page 2: Versioned prior-work qualification, Wang–Zhu citation, Lemma 2, reflection, auxiliary determinant, base and moment step are clear; equation (9) remains inside the bottom margin.
- Page 3: Induction identity and coefficient proof are legible; wide geometric sums and top coefficients fit; equation (17) does not overlap the footer.
- Page 4: Coefficient-integral reduction, parameter range, boundary example, exact-check counts and library citation are clear; equations (18)–(21) fit without clipping.
- Page 5: AI/computational disclosure and all six bibliography entries are legible. Accented names and complete long author list render correctly; URLs wrap inside the margins.

No clipping, overlapping content or illegible symbols were found. There are no charts, data tables or diagrams requiring additional value-by-value visual-source comparison. Displayed numerical examples and finite counts match the accepted dossier and fresh exact replay. The report covers pages 1–5 exactly once. No source or PDF changes occurred after rendering and viewing.

Mathematical snapshot: 4556257bb02194676513831cafeed05699982a8fd956a67820a92eda025f8ae5.
Manuscript digest: 3ceea70d8cc6150305a1e7803d7c68e99dca884218ce450049e222720edc65fc.
PDF digest: 5a8c9b3de7676d91dac6e3836d8d4b43d2fe8301c99567a45480fbc9af995028.
Image paths and hashes are recorded in audit/visual.json.
