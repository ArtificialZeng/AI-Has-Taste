# Clean build audit

Release job: `bigMac-00003-p01-release-288b9c70330b`.  Audit date:
2026-09-06.  This report is bound to evidence digest
`f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`,
manuscript digest
`2a1f336f0088850ae32cc1ad1db6bd35b78664b26af3a499ddce46fdfbc35320`,
and PDF digest
`3cfe689095e44a9b1e0d5193fbedc15b900446887c5d524b4ff9553126952b0a`.

The explicit target `manuscript/main.tex` was cleaned with `latexmk -C` and
then built with the command recorded in `publication.json`:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=manuscript manuscript/main.tex
```

`latexmk` 4.88 and pdfTeX 1.40.29 completed two `pdflatex` passes and reported
all targets up to date.  The current nonempty build log is
`manuscript/main.log`, SHA-256
`c4c32330c79675a883f1855e039aadf6ee319cffd97a06de0d5109e96beba5f1`.
The final log has no warning,
undefined citation/reference, multiply-defined label, overfull/underfull box,
error, or fatal diagnostic.  Extracted cross-references display as (1)--(4),
and citations display as [1] and [2].

The resulting PDF has three unrotated US-letter pages, is unencrypted, and has
19 embedded subset fonts; `pdffonts` reports every font embedded with Unicode
mapping.  `pdftotext` extracts 5,573 bytes.  `pdfinfo` confirms nonempty title,
author, subject, and keyword metadata.  The final title is
`A Fixed-Periodic Bound for Signed Affine Copies of {0,1,3}` and the author is
`Xiaojian Zeng`.

The build neither reads nor changes the immutable `source.md`; its SHA-256
remains `8bd964b5b75c92eacd0c227be016ba78920c6b599f27b2331de2cdea771f4e98`.
The accepted mathematical evidence snapshot remains
`f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`.
