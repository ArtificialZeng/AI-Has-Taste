# Clean build audit

For release job win-00073-p01-release-01fed9f3c856, the unchanged accepted
canonical sources were rebuilt from scratch with
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex. The command
exited 0 and produced a four-page PDF. The final manuscript/main.log and
manuscript/main.blg contain none of the audited undefined-citation or reference,
missing-entry, duplicate-entry, BibTeX warning, LaTeX error, or fatal patterns.

The final PDF has four unrotated letter-size pages, is unencrypted, and was
produced by pdfTeX with hyperref. Its rendered title and author agree with the
manuscript; its optional PDF title and author metadata fields are blank rather
than contradictory. pdffonts reports every listed font embedded and subsetted.
Labels, theorem numbering, mathematical glyphs, bibliography, and URLs all
resolve. The standard-library exact verifier independently reports OK for every
integer from 1 through 30, including N=1 with 1/48. The converged clean build is
accepted.
