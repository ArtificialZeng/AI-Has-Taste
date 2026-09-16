# Rendered-page visual audit

Release job `win-00071-p01-release-74f5b2e2a4db`, checked 2026-09-08.

All four pages of the canonical PDF were freshly rendered to PNG at 144 dpi and
each page was viewed at original rendered resolution.  Pages 1--4 have readable
text and mathematics, complete margins, continuous paragraph flow, visible
equation numbers and proof-end marks, and no clipping, overlap, blank page,
missing glyph, illegible item, or broken figure.  The bibliography on page 4
is readable; its long URLs wrap within the text block without clipping.

All 23 fonts reported by `pdffonts` are embedded and subsetted.  `pdfinfo`
reports four unrotated US-letter pages, no encryption, no forms or JavaScript,
and the expected pdfTeX/LaTeX producer data.  The optional title, subject,
keywords, and author metadata fields are blank rather than inaccurate.

No visual issue was found.  The authored theorem scope in the rendered paper
matches the accepted claim: every canonical zero is simple, real and in
`[-3,1]` for every integer `n >= 1`.
