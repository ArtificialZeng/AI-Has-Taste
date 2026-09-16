# PDF audit

Status: **PASS** after the root-level citation correction.

The arbitrary-\(n\) follow-up did not alter or regenerate the finite
manuscript, PDF, or archives. The existing seven-page \(P_{11}\) artifact is
preserved because the full conjecture remains open after search; no new PDF
is represented as a solution of the full problem.

A post-follow-up preservation check matched the prior verified release for
the source statement, formal statement, three certificate files, independent
verifier, manuscript sources, PDF, LaTeX ZIP, and ancillary ZIP byte for byte.

## Build

- Source: `paper/main.tex` with `paper/references.bib`.
- Engine: pdfLaTeX through Latexmk 4.76 and BibTeX.
- Final LaTeX log: no undefined reference/citation, LaTeX/package error,
  overfull box, or underfull box.
- Citation audit: three cited keys, three bibliography entries, no missing or
  unused key.

## Render and visual inspection

- Final PDF: 7 pages, US Letter, 390,965 bytes.
- Every page was rendered at 144 dpi with Poppler and inspected after the
  Raghava citation was added.
- Title/abstract, all displayed formulas, the ten-row rational-mixture table,
  code block, all three references (including the Raghava DOI), running heads,
  page numbers, affiliation, and both email addresses are legible and aligned.
- No clipping, overlap, black box, broken table, missing glyph, or excessive
  intermediate-page whitespace was found. Final-page whitespace is ordinary
  for the short references/author-address page.
- All fonts reported by `pdffonts` are embedded and subsetted.

## Metadata and content policy

- PDF title: “The sharp variation constant for the centered Hardy–Littlewood
  maximal operator on P11”.
- PDF author: Zijian Zeng.
- Extracted-text scan found no SHA-256 value, long hash string, internal
  route/role identifier, completion/confidence field, or assistant product
  name.
- SHA-256 (audit only):
  `8c7a64b99da1a23feb0256ca8117879b171feb4ed55b68c74c602f989bffa590`.

## Archive checks

- The LaTeX ZIP passed `unzip -t`, was extracted into a fresh temporary
  directory, and built independently to a seven-page, 390,965-byte PDF with
  three cited and three defined bibliography keys and no substantive warning.
- The rebuilt LaTeX ZIP is 7,933 bytes and has audit-only SHA-256
  `911048021f206b6f777a3c836fceeecde98527539b4d00ce4e8687e8566584f9`.
- The ancillary ZIP passed `unzip -t`.  Its mathematical inputs are unchanged
  from the prior release, whose fresh-extraction independent exact verifier
  returned `VERIFIED` for all 5,874,849 chambers, 45,011,088 slots, and 10
  rational exceptions.
