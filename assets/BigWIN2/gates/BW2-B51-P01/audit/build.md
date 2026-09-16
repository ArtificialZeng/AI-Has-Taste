# Clean build audit

**Result:** pass.

From `manuscript/`, `latexmk -C main.tex` removed generated build products and
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` rebuilt the
paper through converged pdfLaTeX/BibTeX runs.  The final output is a three-page
PDF.  The final log scan found none of the configured citation, bibliography,
cross-reference, undefined-control-sequence, runaway-argument, LaTeX, or fatal
error patterns.

The post-build bibliography checker reported 3 cited keys and 3 BibTeX keys,
with no missing bibliography file, missing key, unused key, or AUX mismatch.
`pdfinfo` reports letter pages, no encryption, no forms or JavaScript, and
embedded Type 1 fonts are listed in the build log.

Bound PDF SHA-256:
`e297df007df6d2fa4ed8beed724cba4f7202be32c7cdfa8a938bb482d8743105`.
