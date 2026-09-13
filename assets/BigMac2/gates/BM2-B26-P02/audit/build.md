# Fresh clean-build audit

The existing auxiliary state was removed with `latexmk -C main.tex`, followed
by the exact clean command recorded in `publication.json`:

```text
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode \
  -halt-on-error -file-line-error main.tex
```

The build ran in `manuscript/` with latexmk 4.88, pdfTeX 1.40.29, and Biber
2.21.  It performed one Biber run and three pdfLaTeX passes.  First-pass
cross-reference and bibliography rerun notices disappeared after convergence;
latexmk reported `All targets (main.pdf) are up-to-date`.

The final compiler transcript is the nonempty file `manuscript/main.log`,
SHA-256
`1e8e875eee7ef16c124e5222efb29f07e6092e7c1a3da8217911051177d2ff6f`.
The final log and `main.blg` contain no LaTeX/package warnings, unresolved
citations or references, overfull/underfull boxes, errors, emergency stops, or
fatal diagnostics.  Biber found all seven cited keys in `references.bib`.

The output is a valid, unencrypted PDF 1.7 of 244,610 bytes and five letter-size
pages.  `pdftotext` extraction is nonempty.  PDF metadata gives the intended
title and author, and `pdffonts` reports every used font embedded and subset.
After this clean build, `freeze-manuscript` bound PDF SHA-256
`94a4ec58d8f02cf5890a7d395d83580460494266512ad076a5199b5ae4d8a6da`
to unchanged manuscript digest
`a3dcc5c255b51d98765bd7c59f9d82e4ade371ff02af82501fb43f5100116920`.

**Verdict: accept; clean build.**
