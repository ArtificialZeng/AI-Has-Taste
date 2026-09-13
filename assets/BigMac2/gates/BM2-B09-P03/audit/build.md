# Fresh clean-build audit

Release job: `bigMac-00009-p03-release-5e52c78d86fd`  
Evidence snapshot: `eedc974190423e8943ef82f6b963b7444c569a84a97db0d7dab2272f1b5f3797`  
Manuscript digest: `ffcabe5a81133faecbbd932c487c750bf440cb3db0fa982fefb3e7ac95b80612`  
PDF digest: `ded68a594b2c150cba63f2d28ca7e08b94a0530d6dfd0212164147fb51f4c193`

## Build performed

From `manuscript/` I first ran `latexmk -C main.tex`, then ran the declared
publication command

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

This was a clean build from authored sources.  Latexmk ran pdfLaTeX, BibTeX,
and the required final pdfLaTeX pass, exited successfully, and reported the
target up to date after four pages were produced.  The real final compiler
log is `manuscript/main.log`, 22,971 bytes, with SHA-256
`ed38b5762f84f9d1a6e844a893155455a4f07ec450dd1daea9c541b17327f217`.

## Diagnostics inspected

- The final log contains no fatal/error diagnostic, undefined citation or
  reference, multiply-defined label, overfull box, underfull box, or package
  warning requiring action.
- `manuscript/main.blg` reports `warning$ -- 0`, names
  `references.bib`, and generated a nonempty `main.bbl` containing both cited
  entries.
- `main.aux` contains all three citation calls and resolved `bibcite` entries
  for both keys; all equation, theorem, lemma, and proposition references are
  resolved.
- The recorder exposes no omitted authored TeX, figure, or local style input.
  `main.tex` and `references.bib` are therefore the complete publication
  source list; auxiliary files are build products.
- The PDF begins with `%PDF-`, is unencrypted, has four letter-size pages,
  has nonempty extractable text, and carries the intended title, author,
  subject, and keywords.  All listed fonts are embedded and subsetted.

The clean rebuild changed only the time-dependent PDF bytes, not any authored
source or accepted evidence.  I reran `freeze-manuscript`; the source digest
remained unchanged and the snapshot now binds the PDF digest above.

## Verdict

**Accept.**  The declared sources compile cleanly and reproducibly at the
structural level, the current build log is clean, and references and metadata
are resolved.
