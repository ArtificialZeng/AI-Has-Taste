# Fresh rendered-page visual audit

## Binding and rendering

- Release job: `bigMac-00013-p03-release-4189b067aff7`.
- Evidence snapshot: `393c635435e81b9dc70256f6851164d5d45067c12ff2d04143ac46090b6303c6`.
- Manuscript snapshot: `8487aa4f23241b4179277a1ce3bdde7e416eebd1cfe23df81005e94282a62ca3`.
- PDF SHA-256: `0bef46e936a25d8d0af1f3ea63a3cf60c8b5c982e46281d50a845a7ea5f88909`.
- `pdfinfo` page count: 3.

I rendered the current PDF at 180 dpi with `pdftoppm` to
`audit/rendered/page-1.png`, `page-2.png`, and `page-3.png`, then opened and
inspected each full-page raster at original resolution. This audit is based on
the visible pages, not text extraction alone.

## Page-by-page observations

1. **Page 1:** The two-line title is centered and fully inside the margins.
   Author, affiliation, email, date, abstract, definitions, context paragraph,
   theorem statement, accents in “Gwóźdź” and “Möbius,” mathematical symbols,
   and the maximizer set are sharp and legible. There is no clipping, overlap,
   collision, broken glyph, or excessive line spill. The page break occurs
   cleanly after the first part of the theorem.
2. **Page 2:** The asymptotic display and equations (1)--(6) have intact
   delimiters, bars, superscripts, subscripts, and equation numbers. Paragraphs
   and displays have consistent spacing and alignment. The final sentence
   continues naturally onto page 3; no text or equation is clipped or crowded.
3. **Page 3:** The sign argument, Mills-ratio displays, conclusion, boundary
   remark, assistance disclosure, and both references are fully visible. The
   arXiv URL and DOI wrap within the text block without crossing the margin.
   Names and diacritics render correctly. No overlap, truncation, illegibility,
   orphaned equation number, or footer collision is visible.

All pages use consistent typography and generous margins. There are no figures,
charts, tables, or raster data whose values require a separate visual-data
comparison. The PDF metadata title/author agree with the visible title page,
and all fonts reported by `pdffonts` are embedded.

## Verdict

**Accept.** Pages 1, 2, and 3 were each directly reviewed and are readable and
submission-ready, with no substantive visual defect.
