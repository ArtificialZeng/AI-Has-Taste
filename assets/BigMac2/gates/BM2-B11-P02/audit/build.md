# Fresh clean-build audit

Release job: `bigMac-00011-p02-release-8e7a7826a299`  
Bound PDF: SHA-256 `f1561ebd6cb8af5486dd854ca5544d1f49567b0214ba6d35f9a5509f06e9a8d6`  
Build log: `manuscript/main.log`  
Build-log SHA-256: `7dfd5cacae8007aa0de5eba1d26ded6e46e197e3979413c65d5b246d2ecefedb`

I removed generated TeX intermediates with `latexmk -C main.tex` and then ran
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from the
`manuscript` directory.  Latexmk ran the necessary initial LaTeX pass,
BibTeX, and resolving LaTeX pass and exited zero.  The initial-pass undefined
messages were resolved by that normal multi-pass sequence; the bound final
`main.log` has no LaTeX warnings, undefined citations or references,
overfull/underfull boxes, multiply-defined labels, fatal diagnostics, or
rerun request.  `main.blg` reports three used entries and zero warnings.

`pdfinfo` identifies a six-page, unencrypted PDF 1.7 file with the intended
title and author.  `pdftotext` produces 14,130 nonempty bytes and shows the
three resolved references.  `pdffonts` reports every listed font embedded and
subsetted.  The PDF header, page count, and extractability are also checked by
the release gate.

**Verdict: accept.**  This is a clean, reproducible final build with a clean
bound compiler log.

