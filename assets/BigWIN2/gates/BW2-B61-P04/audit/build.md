# Build audit

The manuscript was forcibly rebuilt from generated-file cleanup through a
converged `pdflatex`/BibTeX sequence with:

`latexmk -cd -gg -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`

The command succeeded and produced a three-page PDF.  The final
`manuscript/main.log` contains no LaTeX or package warnings, undefined
citations, undefined cross-references, overfull or underfull boxes, errors,
emergency stops, or fatal diagnostics.  `manuscript/main.blg` contains no
missing database entries, duplicate entries, or BibTeX warnings.

The bibliography consistency checker reports five cited keys, five BibTeX
keys, no missing or unused entries, and exact agreement with all five AUX
`\\bibcite` keys.  `evidence/verify_certificates.py` and the separately
implemented `audit/referee_check.py` both completed successfully.

`pdfinfo` confirms the exact metadata title
`The Least Frobenius Alexander Quandle Isogeny-Detection Prime over F_5` and
author `Xiaojian Zeng`, with three unencrypted letter-size pages.

The rebuilt PDF SHA-256 is
`5f5d18112852285fcefb7a3c1d58bb1336602eba0087651701de5ddfd1bac3c9`.
