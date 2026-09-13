# Fresh clean-build audit

This audit is bound to manuscript snapshot
`dc1b753854a1dbcfc26cbe1a8276cdacc299b48dbd367fec0babd75df0fe61e3`
and PDF SHA-256
`97e311fe3a312ace39568a515041bbdeba0d754cefa64d3f96270c5724c53880`.

I removed generated LaTeX products with `latexmk -C main.tex`, then ran
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from
`manuscript/`. Latexmk ran pdfLaTeX, BibTeX, and the required converging
pdfLaTeX pass and produced a three-page PDF. The final compiler transcript is
`manuscript/main.log`, SHA-256
`d743dfe51579c94f31ea5754ac0302998138178806031ec5aa758525fd5f7d26`.

The final log contains no LaTeX/package warning, undefined citation,
undefined reference, multiply-defined label, overfull or underfull box,
compiler error, or fatal diagnostic. `manuscript/main.blg` reports three used
entries and zero BibTeX warnings. The citation-key set in `main.tex`, the
entry-key set in `references.bib`, and the resolved `main.aux` key set are all
exactly `{benevides2024,bushawclifton2026,flocchini2004}`.

`pdfinfo` reports a valid unencrypted three-page PDF with the intended title,
author, subject, and keywords. `pdftotext` yields 6,979 nonempty bytes. All 16
listed Type 1 fonts are embedded and subsetted. No figures or external local
styles are required.

**Verdict: Accept.** The build is clean and its final log and output are
bound to the current manuscript state.
