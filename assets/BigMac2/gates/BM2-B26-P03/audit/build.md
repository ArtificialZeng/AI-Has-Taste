# Fresh clean-build audit

Audit date: 2026-09-09. Release job:
`bigMac-00026-p03-release-22e156271e42`.

The manuscript was rebuilt from no generated auxiliaries by running
`latexmk -C main.tex` followed by the publication command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`. The complete pipeline ran pdfLaTeX, BibTeX, and the required
reruns to convergence and produced a four-page PDF.

The current nonempty compiler transcript is `manuscript/main.log`, SHA-256
`2a9295108efd93e736adb3e88a89418705a1b43a0cfb65471c6ee0d80f521b2f`.
The final log has no fatal error, undefined citation/reference, multiply
defined label, overfull/underfull box, or rerun warning. `manuscript/main.blg`
reports zero BibTeX warnings; all four citation keys appear in `main.aux` and
all four resolved entries appear in `main.bbl` and extracted PDF text.

`pdfinfo` reports an unencrypted PDF 1.7 file with four US-letter pages, and
`pdftotext` extracts 9,757 nonempty bytes. Fonts and mathematical glyphs are
embedded/rendered legibly. The visible title and author are correct; the
optional PDF document-info title/author fields are blank and do not affect the
rendered or submission-ready content.

**Verdict: accept; clean build.**
