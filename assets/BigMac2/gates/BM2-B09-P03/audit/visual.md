# Fresh rendered-page visual audit

Release job: `bigMac-00009-p03-release-5e52c78d86fd`  
PDF: `manuscript/main.pdf`  
PDF digest: `ded68a594b2c150cba63f2d28ca7e08b94a0530d6dfd0212164147fb51f4c193`

## Rendering and page coverage

I rendered the current PDF with Poppler at 170 dpi to four PNGs of
1445-by-1870 pixels and visually inspected each image at original detail:

| Page | Render | Observations |
|---:|---|---|
| 1 | `audit/rendered-pages/page-1.png` | Title, author block, abstract, section heading, definitions, displayed equations, and footer are sharp, aligned, and fully inside the margins. |
| 2 | `audit/rendered-pages/page-2.png` | The context paragraph, theorem, support encoding, and both lemma proofs are legible; equation symbols and intentional proof-end squares render correctly; no collision or clipping occurs. |
| 3 | `audit/rendered-pages/page-3.png` | The numbered list, recurrence, proof, full 12-column frontier table, and methodological citation are readable.  The table fits the text width and every entry is distinct. |
| 4 | `audit/rendered-pages/page-4.png` | The 11-row witness table, final-product argument, limitations, disclosure, and both bibliography entries are complete and legible; the DOI and arXiv URL are not clipped. |

The page sequence is exactly 1, 2, 3, 4.  There are no figures or charts.
For the two data tables, I additionally read every displayed value: the p. 3
frontier row matches the accepted sequence for depths 0 through 11, and the
p. 4 witness factors, admitted levels, and cumulative products match the
accepted claim and certificate report.  Neither table uses visual
distortion, truncated axes, color coding, or unreadable scaling.

Across all pages I found no overlap, cutoff, missing glyph, broken formula,
black replacement box, orphan heading, illegible text, malformed link,
unexpected blank page, or inconsistent page number.  Margins, typography,
spacing, and section hierarchy are consistent.  Text extraction independently
returned nonempty content for the full document, and all PDF fonts are
embedded.

## Verdict

**Accept.**  Every page of the current four-page PDF was rendered and actually
seen, with no substantive presentation defect.
