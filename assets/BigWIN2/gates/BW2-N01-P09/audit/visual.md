# Rendered-page visual audit

Verdict: accept. Job: `newwin-00001-p09-release-9807a7157078`. Reviewed 2026-09-12T10:20:03.678817+00:00.

Rendered the final PDF with `pdftoppm -png -r 130 manuscript/build/main.pdf audit/release-pages/page`. All six PNGs were actually displayed through the image viewer and inspected in this release context; extracted text was only supplemental.

Page 1: Title/author/affiliation/email and abstract are legible. The operation table has exactly rows 000/101/111, and the identity and leftmost decomposition fit their display widths. Both origin citations resolve.

Page 2: The theorem finite sum and EGF render correctly. Prior-work and library citations show the intended locators. Indicators, the evaluation product and the essentiality lemma are legible.

Page 3: The essentiality proof, Cartesian projection formula and AND-prime lemma fit without overlap. Factorization citation resolves; the recognition proof continues normally across the page boundary.

Page 4: The recognition continuation, reconstruction slice formula, normal forms, and both integer recurrences are legible. No clipped subscripts or overlap; page-number margin is clear.

Page 5: Formal coefficient extraction displays are intact. The six-row count table matches the actual exact census entry by entry. Decoder/census/formula scope and the bounded-search limitation are legible.

Page 6: AI/computation disclosure is legible and all five bibliography entries are present. Author names, years, article/page fields, DOI and URL text match the audited source records. Long URLs wrap inside the text area.

No clipping, overlapping text, missing glyphs, illegible equations, broken citation markers, or visually distorted data were observed. There are no plots or external figures. The operation table was compared to the original primary table; every census-table number was compared with the fresh exact output. No rounding is involved. Proof continuations at page boundaries are readable.

Mathematical snapshot: `18815edf6e7f240c1b5c28e90cced864fbed61ffa4fc3c27160e18c4b9bfea38`.
Manuscript digest: `8cb6c3e3d2db41fb4bc023cd68b3ce2ff4d3d04e9f4d543a53b00a298d8effc9`.
PDF digest: `cf142e53197b0ce22401ec43cca40de534ebd52252a00477e83b63d4b14db7fd`.
