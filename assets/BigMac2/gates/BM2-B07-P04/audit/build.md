# Fresh clean-build audit

**Generated:** 2026-09-07T12:31:08+08:00  
**Verdict:** accept

I removed all generated LaTeX products with `latexmk -C article.tex` and built
from the two declared authored sources with
`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex`. Latexmk ran
pdfLaTeX, BibTeX, and the required converging pdfLaTeX pass and exited
successfully with all targets current.

The final compiler transcript is `manuscript/article.log`, SHA-256
`53667c93dd188a55e94d9b86e418acec8da6fd17e2e0685862b02bde7a056120`.
I inspected that log and `manuscript/article.blg`: there are no LaTeX/package
warnings, overfull or underfull boxes, undefined citations, undefined
cross-references, multiply-defined labels, BibTeX warnings, errors, emergency
stops, or fatal diagnostics. `article.aux` binds both citation keys and all
internal references; `article.bbl` contains both expected entries and the
corrected `arXiv:2608.18584v2` label.

The output begins with a valid PDF header, has four letter-sized pages, is not
encrypted, and yields nonempty text from every page. PDF metadata gives the
intended title, author, and subject. `pdffonts` reports every used font embedded
and subsetted with Unicode mappings. The real recorder trace contains no local
authored dependency beyond `article.tex` and `references.bib`; generated
`article.aux`, `article.bbl`, and `article.out` and system TeX files are not
publication sources. The clean build is accepted.
