# Build audit

**Verdict:** accept.

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged
successfully under pdfTeX and produced `manuscript/main.pdf` with 4 letter-size
pages.  The final PDF SHA-256 is
`366afa2fdaaa2649d6584093f6c7aa7a338294faf8fa5d6270e84642fe4e9e8e`.
The nonempty final log is `manuscript/main.log`, SHA-256
`48b65b1d0ff2494ef0b4e93b4c953597d1eca86e22d5b5350b1de58dd3d18813`.

Log scans found no undefined citations/references, missing BibTeX entries,
duplicate entries, LaTeX errors, fatal errors, emergency stops, undefined
control sequences, or runaway arguments.  Labels and bibliography references
are resolved.  `pdfinfo` confirms an unencrypted PDF 1.5 file with extractable
text, title “The Smallest Eberlein Eigenvalue of J(4r+2,2r,r): The Sharp
Threshold r0=2,” and author “Xiaojian Zeng.”
