# Fresh build audit

The current manuscript was rebuilt from its listed sources with

```text
cd manuscript && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

on 2026-09-08. `latexmk` performed a full cleanup, ran pdfLaTeX, BibTeX, and the
required final pdfLaTeX pass, exited zero, and reported the target up to date.
The authoritative final compiler log is `manuscript/main.log`, SHA-256
`dfc48d559c17b226fd4cd184f4077625dbce0124533c1f4053fe659fde4ca44f`.
It is nonempty and contains no fatal error, undefined citation/reference,
multiply defined label, LaTeX/package warning, overfull box, or underfull box.
`manuscript/main.blg` reports two used entries, no missing fields, and zero
warnings.

The output has a valid PDF header, three A4 pages, nonempty text extraction,
title and author metadata matching `publication.json`, and SHA-256
`6e17f36b687befdf2133bb4e6974434a9b37fdd580ab8c8cc050124b473cb6f8`.
`pdffonts` shows every font subset embedded with Unicode mapping. Cross-
references (Theorem 1, Lemma 2, equations (1)--(2)) and bibliography labels
[1]--[2] resolve in the extracted and rendered output. The build is clean.
