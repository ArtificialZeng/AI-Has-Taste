# LaTeX audit

Audit date: 2026-08-29 (Asia/Shanghai)

## Verdict

**PASS.**  The manuscript was built from a clean auxiliary directory with
TeX Live 2026, pdfTeX 1.40.29, BibTeX 0.99e, and latexmk 4.88.  The final
converged log contains no undefined citations or references, BibTeX database
warnings, overfull/underfull boxes, package warnings, or LaTeX errors.

The first temporary build exposed an undeclared `xcolor` requirement and two
small overfull boxes.  `xcolor` is now explicitly loaded, and the two
paragraphs were reflowed.  A visual pass also found literal `qquad` text in
several displayed formulas; every occurrence was repaired to `\qquad` before
the final clean build.  These transient defects are not present in the
retained source or PDF.

## Clean build

~~~bash
cd paper
latexmk -C -outdir=../tmp/pdfs/build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../tmp/pdfs/build main.tex
~~~

The converged artifact has eight US-letter pages.  `pdftotext -layout`
contains no placeholder, TODO, undefined marker, or leaked tool token.

## Final log scan

~~~bash
rg -n "Citation .* undefined|There were undefined|I didn't find a database entry|Warning--|Repeated entry|LaTeX Warning|Package .* Warning|LaTeX Error|Fatal error|Emergency stop|Undefined control sequence|Runaway argument|Overfull|Underfull" \
  tmp/pdfs/build/main.log tmp/pdfs/build/main.blg
~~~

Result: no matches.
