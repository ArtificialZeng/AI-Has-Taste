# PDF audit

Status: PASS.

The author metadata and journal-neutral format are supplied and audited.  The
final source has 3 citations, 3 bibliography entries, no missing or unused
entries, and a clean LaTeX/BibTeX build with no warnings, undefined
references/citations, overfull/underfull boxes, or errors.

Final artifact:

- Path: `output/pdf/05_almost_golomb_prefix.pdf`.
- PDF metadata title and author agree with the manuscript; the author is
  `Zijian Zeng`.
- Format: PDF 1.5, 5 letter-size pages, 348722 bytes, no encryption, forms,
  or JavaScript.
- All listed fonts are embedded and subsetted.
- SHA-256:
  `2fd8cef7267653c9d22ec53f241ccee30085231fb28472fddeace81d9415df56`.

Full-page visual audit after `pdftoppm -png -r 150`:

- Page 1: title, author, abstract, opening equations, footnote, and margins are
  clear; no clipping, overlap, black block, or placeholder.
- Page 2: definition, displayed formulas, proof text, and QED mark are clear
  and remain inside the text block.
- Page 3: running head, endpoint identities, theorem statement, and proof are
  clear; no collision or truncation.
- Page 4: theorem conclusion, diagnostics, limitations, and disclosure are
  clear; line breaks and page margins are sound.
- Page 5: references, affiliation, and both email addresses are clear; the
  remaining lower-page whitespace is normal and contains no artifact.

The `pdftotext -layout` extraction contains the supplied author, affiliation,
both email addresses, and both cited arXiv version identifiers.  A
case-insensitive scan found no SHA-256/digest wording, hash placeholder,
internal route or role label, completion/confidence score, anonymous-author
placeholder, funding statement, or acknowledgment section in the PDF text.

The companion source archive
`output/latex/05_almost_golomb_prefix_latex.zip` has SHA-256
`df1c4924654b9e5ed348a726aab31040e5e8b94ccb9f9e64f74cd9c19d324d18`
and size 10026 bytes.  Its directory was listed, every member passed
`unzip -t`, and a clean extraction passed the independent finite verifier and
the full LaTeX/BibTeX build, again producing a 5-page PDF without warnings.

Failed attempts retained:

- An initial BibTeX invocation against an absolute temporary path was blocked
  by TeX's `openout_any=p` policy; rerunning from inside the temporary
  directory fixed the environment issue.
- The first full second pass found the scaffold's missing `xcolor` dependency
  for mixed link colors and a long running head; both were repaired before the
  clean final audit.
