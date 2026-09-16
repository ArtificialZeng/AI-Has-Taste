# Rendered-page visual audit

Verdict: accept. Job `primary-20260914-partition-jumps-release-53b5e2a5c417`. Reviewed 2026-09-14T02:13:11.328575+00:00.

Current manuscript digest `6a77b9ab481ab6d3d7560adb2a14429616d35e351ddc1b733579ad606bd36ea0`; PDF digest `407292477df86d3d20d3536ae5001cbe99c2ba30ebd67f2214dffa3be1a8a451`; research snapshot `fce4053e5a3907860b747c9542daeb32f9d40fbb83dae61c32423ee9941797aa`.

The current seven-page PDF was freshly rendered by `pdftoppm -png -r 130`. Every individual image was actually opened with the image viewer, in order, in this release job. This is a rendered-page inspection, not an inference from pdftotext or file existence.

1. Title, author/affiliation/email and abstract are readable. Graph definition, citations and D_delta cases have intact symbols and margins. Theorem 1 continues naturally on page 2.
2. Theorem 1 continuation and Theorem 2 are complete. Degree and two-capacity dimension formulas, endpoint conventions and the three-case display fit within margins; citation locators and equation numbers are resolved.
3. The staircase and two-birth lemmas, proof endings, signed-jump case split and initial witness family are readable. No clipped formulas, overlapping proof marks or missing symbols.
4. Every cell of the twelve-row four-column table was read and compared with fresh verifier output. Column headings and integer values are clear. The degree-correction inequality, indicator formulas and lower-page equation remain inside the margins.
5. The all-n degree witnesses and support triples are legible. The library citation and exact finite coverage numbers are readable. Residual-scope and computational/AI-assistance paragraphs remain complete.
6. The appendix explanation and framed Python listing are readable, including indentation, comparisons, subset enumeration and expected rows. The listing continues across the page break without clipping.
7. The final two code lines and closing frame are visible. All seven bibliography entries, authors, arXiv version identifiers and the library DOI were read. Wrapped URLs and the DOI remain legible with no margin collision; lower-page whitespace is harmless.

All pages [1,2,3,4,5,6,7] were reviewed. No substantive clipping, overlap, unreadable notation, unresolved reference marker or corrupted font was seen. There are no plots or diagrams. Table 1 is the only data visual; all values match exact fresh output. The code and theorem page continuations preserve their content and were checked across the break.

The PDF metadata and font embedding were checked separately in the build audit. Per-page image paths and hashes are in audit/visual.json. No manuscript/source edits followed rendering or inspection.
