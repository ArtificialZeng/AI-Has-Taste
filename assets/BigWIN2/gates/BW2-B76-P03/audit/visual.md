# Rendered-page visual audit

For release job `win-00076-p03-release-f17ba9de4d6f`, the final frozen PDF was
rendered with `pdftoppm` to 1360 by 1760 pixel PNGs at 160 dpi.  Every page was
then actually viewed at original rendered resolution after the clean rebuild.

- Page 1: title, author and affiliation, abstract, contextual citations,
  projected-trace definitions, balance equations, theorem statement, and the
  closing source-question citation are all legible.  No text, display, or page
  number is clipped or overlapped.
- Page 2: the complete proof, graph-complement parametrization, vertical trace,
  matrix, horizontal trace, contradiction, and end-of-proof mark are legible.
  Equation numbers and mathematical symbols align correctly and remain inside
  the margins.
- Page 3: exact-verification and scope paragraphs, assistance disclosure, and
  all five bibliography entries are legible.  Long author and URL lines wrap
  cleanly; the corrected Štěpán Roučka name renders correctly.  The lower-page
  whitespace is normal end-matter whitespace.

No chart, graph, table, figure, raster image, or visually encoded quantitative
claim occurs.  Pages 1--3 have consistent orientation, margins, fonts, section
hierarchy, and page numbering.  All fonts are embedded and subset.  PDF title
and author metadata are present.  Visual verdict: accept.
