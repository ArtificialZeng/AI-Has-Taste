# Clean build audit

## Verdict

Accept. In release job `win-00042-p04-release-9bc7d7004a0e`, from
`manuscript/`, `latexmk -C main.tex` was followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. Latexmk ran
BibTeX and converged after the required LaTeX passes. The final PDF has four
pages.

The bibliography checker reports four cited keys, four BibTeX keys, no missing
or unused keys, and exact agreement with `main.aux`. A diagnostic scan of the
final `main.log` and `main.blg` found no undefined citation/reference, missing
database entry, repeated entry, BibTeX warning, LaTeX error, fatal error,
emergency stop, undefined control sequence, or runaway argument.

The exact integer checker was also replayed successfully: 20 generic pairs,
absolute coefficient mass 28, analytic positivity from 194, all eight finite
witnesses, and no allowed witness at 13.

`pdfinfo` reports the intended title, author, subject, and keywords. All PDF
fonts reported by `pdffonts` are embedded and subsetted.
