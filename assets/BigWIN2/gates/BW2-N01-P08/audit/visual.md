# Rendered-page visual audit

Verdict: accept. Job newwin-00001-p08-release-467bc3c43b74. Reviewed 2026-09-12T09:48:39.283125+00:00.

The final PDF was rendered with `pdftoppm -png -r 130 manuscript/build/main.pdf audit/release-page`. All six full-page images were actually opened with view_image in this release context after the final rebuild and refreeze. This is visual inspection, not a claim based on pdftotext or image-file existence.

- Page 1 (audit/release-page-1.png): Title, author and affiliation, abstract, definition and full Theorem 1 inspected. Formula indices, root multiplicities, citation labels and margins legible.
- Page 2 (audit/release-page-2.png): Ordinary scalar formula, comparison paragraph and unique first-return lemma inspected. Bottom boundary-case table is complete, including all three rows (0,0), (1,0), (1,1), with no collision with the footer.
- Page 3 (audit/release-page-3.png): Generating equation, formal Lagrange extraction, positive coefficients, Vandermonde specialization and ordinary reduction inspected. Aligned equations and citations remain within the text area.
- Page 4 (audit/release-page-4.png): Jacobi normalization, Rodrigues identity, orthogonality, root transform, boundary cases and section transition inspected. Mathematical exponents and limits are clear; the continuation onto page 5 is ordinary pagination.
- Page 5 (audit/release-page-5.png): All parameter pairs, exact counts 49/303/11, the visible selected Zeng citation, Bézout spelling, computation/AI disclosure and first five references inspected. No hidden or clipped citation, unexpanded key or overlapping DOI.
- Page 6 (audit/release-page-6.png): Final four references inspected, including the selected preprint title, version, URL and restored exact DOI. URLs wrap legibly. Remaining whitespace after the bibliography is normal; no content is cut off.

No clipping, overlap, illegible symbols, unresolved citation marker, missing table row or distorted chart was found. The manuscript contains one analytical boundary-case table and no external plots. Its six entries were checked value-by-value against the factor analysis. All six pages are text-bearing and the footer page numbers are correct.

Snapshot 4c76e5c2d8e61b75a85b57cf165889afc1b82282f4c36bfce8d9575114e62dd6; PDF 9e7ebe7f07e45ddd1ff6e9e524e8cd63ce4060627680c871a96a8815807e76ff.
