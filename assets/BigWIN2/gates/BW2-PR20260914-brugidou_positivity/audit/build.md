# Clean-build audit

Verdict: accept. Job: primary-20260914-brugidou-positivity-release-ee08f920b725. Checked 2026-09-13T19:11:53.621208+00:00.

Ran `latexmk -C -outdir=build main.tex` and then
`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex`
from manuscript/. Both exited zero. The process log is
audit/release-build-process.log. This removed the previous generated PDF and
auxiliary state before rebuilding; final BibTeX and LaTeX passes converged.

The final main.log and main.blg contain no undefined citation/reference,
missing database entry, duplicate entry, BibTeX warning, fatal error,
missing glyph, overfull box or underfull box diagnostic. The canonical
bibliography check reports five cited keys, five BibTeX entries, and five
matching auxiliary bibliography keys, with no missing or unused entry.
The current main.bbl was read and all five rendered records were inspected.

pdfinfo confirms five A4 pages, correct title, author Xiaojian Zeng and
subject, no encryption and no JavaScript. All 23 listed fonts are embedded,
subsetted and have Unicode mappings. Font and metadata receipts are in
audit/pdffonts.txt and audit/pdfinfo.txt. There are no figures or external
authored TeX dependencies. The publisher-source and arXiv URLs remain legible.

Mathematical snapshot: a7e3cb1a0da871d53fdebc1638fdbbcc611f8739bce3289b362822cd5d358427.
Manuscript digest: 06882b81d33e7d8fbc23865c86b5df51927549014b55348e0eed9c14726e8940.
PDF digest: 0af683a236a0798007148e4fc2d3bb5d2027c23200211301f1717d6d0065d0a4.
Final log digest: 3c8bb3265d58b91b24a143c3aa42e8f6885f25d4029f357f8ec7b9c800533bdc.
