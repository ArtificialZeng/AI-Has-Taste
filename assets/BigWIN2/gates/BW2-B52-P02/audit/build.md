# Clean build audit

The manuscript was cleaned with `latexmk -C` and rebuilt to convergence with
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  The first
post-clean bootstrap invocation generated the recorder file but returned a
transient latexmk recorder-timing error; the immediate continuation ran
BibTeX and the required TeX passes and converged successfully.  A final
invocation after all repairs returned zero and reported every target current.

The final `manuscript/main.log` and `manuscript/main.blg` contain no undefined
citation or reference, missing database entry, repeated entry, LaTeX error,
fatal error, emergency stop, undefined control sequence, runaway argument, or
BibTeX warning.  The BibTeX key checker reports 3 cited keys, 3 bibliography
keys, and exact TEX/AUX agreement.  PDF metadata contains the title and author;
the final output is a four-page A4 PDF.
