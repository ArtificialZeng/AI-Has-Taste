# Build audit

The canonical manuscript was rebuilt from a forced-clean `latexmk -gg` pass
followed by the normal converging command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`.  The final pass completed with no undefined citation or reference,
BibTeX warning, repeated entry, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.

The bibliography checker found one bibliography file, 7 cited keys, 7 BibTeX
keys, no missing or unused keys, and exact agreement with `main.aux`.  The exact
certificate also replayed successfully: modulus 5, level 20, comparison weight
60, index 36, Sturm bound 180, coefficients 0 through 180, empty failure list.

`pdfinfo` reports a valid four-page letter-size PDF with nonempty title, author,
subject, and keyword metadata.  `pdffonts` reports every font embedded and
Unicode-mapped.  The final PDF SHA-256 is
`6b28bde3e718552f47f4245cff4fa4ccb38b2cbf6afe155290150b90073c29dd`.
