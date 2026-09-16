# PDF audit

Audit date: 2026-08-31 (Asia/Shanghai)  
Status: **pass**

Final file: `output/pdf/Zeng_Prime_Cube_Prime_Square_Minimum_49600.pdf`

## Build

- Clean `latexmk` build succeeded after three required LaTeX/BibTeX passes.
- Final log has no warnings, undefined references/citations, overfull boxes,
  underfull boxes, or errors.
- The LaTeX ZIP passed `unzip -t` and built cleanly after extraction.
- The ancillary downloader verified both author-hosted source PDFs, and the
  independent checker ran successfully from the extracted ZIP.

## Metadata and file facts

- Title: *The Prime-Cube/Prime-Square Minimum Below One Trillion Is 49,600*
- Author: Zijian Zeng
- Pages: 4
- Page size: US letter, 612 by 792 points
- File size: 330,478 bytes
- SHA-256:
  `166a665a180ea98e80b0559a69cc80615c16a3085b020df6ab8e9a9cf51e0718`

## Page-by-page visual inspection

Every page was rendered at 160 dpi with Poppler and inspected at original
resolution.

- Page 1: title, author, abstract, opening equations, theorem, foot matter,
  and page number are aligned and legible.
- Page 2: section transition, reduction proof, and four-row exact-filter
  table are complete; no row or rule is clipped at the page boundary.
- Page 3: continuation proof, Pocklington table, large integer identities,
  square-root formula, and main proof are clear and within margins.
- Page 4: reproducibility/limitations, data availability, four references,
  affiliation, two emails, header, and page number are clear; final-page
  whitespace is balanced for a short article.

No clipping, overlap, missing glyph, black box, broken table, or unreadable
link was observed.  Extracted final text contains none of the prohibited
digests, internal identifiers, completion/confidence metrics, or internal
audit wording.  After the final author-address and disclosure-policy edit,
the root audit repeated the clean build, ZIP rebuild, exact verifier, text
screen, metadata check, and inspection of all four re-rendered pages.
