# Fresh build audit

Release job: `bigMac-00014-p01-release-bc265e3b209b`

I removed the prior LaTeX products with `latexmk -C manuscript.tex` and rebuilt
from `manuscript/manuscript.tex` using
`latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex` in the
`manuscript` directory. PdfLaTeX ran twice as expected on a clean tree and
produced a five-page A4 PDF.

The final nonempty compiler transcript is `manuscript/manuscript.log`, SHA-256
`a8b91de76e32ce641ea9d33c3d1df41b223c49ea699734ec20f2d4fd58a75c9c`.
It contains no LaTeX/package warning, undefined citation or reference,
multiply-defined label, overfull/underfull box, emergency stop, or fatal error.
The recorder shows no authored dependency beyond the listed TeX source;
auxiliary `.aux` and `.out` files are generated, and all other inputs are
system TeX resources.

`pdfinfo` reports the intended title and author, A4 dimensions, no encryption,
PDF 1.7, and five pages. `pdftotext -layout` yields nonempty text containing the
complete theorem and bibliography. `pdffonts` reports every font embedded,
subset, and Unicode-mapped. The build is clean.

