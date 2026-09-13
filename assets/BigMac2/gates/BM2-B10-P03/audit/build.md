# Fresh build audit

The existing compiler log `manuscript/article.log` is nonempty and records a
successful pdfTeX build of `manuscript/article.pdf`: four pages, 351,678 bytes.
Its SHA-256 digest is
`f3ef43482972abd5d5fc613ce8b6d11a788ac4dfb805026200e4d7a3000be613`.

The complete log, BibTeX log, `.bbl`, recorder file, `pdfinfo` output, and
`pdftotext -layout` extraction were inspected. There are no compiler failures,
undefined citations or cross-references, rerun requests, BibTeX warnings,
overfull/underfull boxes, missing files, or other layout warnings. BibTeX used
all four cited database entries. The log terminates with a normal four-page PDF
write. PDF metadata contains the manuscript title and author, text extraction is
nonempty, and all 18 listed Latin Modern font subsets are embedded.

The recorder confirms that the only authored compilation inputs are
`article.tex` and `references.bib`; other local inputs are generated build
products. `evidence/check_curvature.py`, also declared in `publication.json`, is
the reproducibility companion rather than an imported TeX file. A fresh run of
that companion succeeded with its exact expected counts.

**Verdict: clean build; accept.**
