# Build audit

Accept. A clean build was produced by first running `latexmk -C main.tex` and
then the canonical command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from
`manuscript/`. After the PDF metadata repair, the same canonical command
converged again.

The result is a valid three-page A4 PDF. Every listed font is embedded and has
Unicode mapping. PDF metadata now contains the article title, author Xiaojian
Zeng, and a subject. `main.log` and `main.blg` contain no unresolved citation or
cross-reference, missing/repeated bibliography entry, warning targeted by the
bibliography audit, LaTeX error, fatal error, emergency stop, undefined control
sequence, or runaway argument. The post-build key checker reports four cited
keys, four database keys, no missing/unused keys, and exact agreement with the
auxiliary file.
