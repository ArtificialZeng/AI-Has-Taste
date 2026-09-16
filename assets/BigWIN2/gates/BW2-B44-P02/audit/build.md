# Release build audit

Verdict: accept.

The canonical command `cd manuscript && latexmk -pdf
-interaction=nonstopmode -halt-on-error main.tex` converged successfully after
BibTeX and produced `manuscript/main.pdf` with five letter-size pages. A clean
build was performed after `latexmk -C`; the final incremental rebuild after the
last wording repair also converged in one pass. `manuscript/main.log` is the
audited final log. Pattern scans found no undefined citation or cross-reference,
missing database entry, repeated BibTeX entry, LaTeX error, fatal error,
emergency stop, undefined control sequence, or runaway argument.

The bibliography checker reported six cited keys, six entries, zero missing or
unused keys, and exact agreement with `manuscript/main.aux`. `pdfinfo` reported a
valid unencrypted PDF 1.5 with five pages. `pdffonts` reported all fonts embedded
and subsetted. The PDF has extractable text and internal equation, theorem, and
bibliography references resolve in the converged output.

