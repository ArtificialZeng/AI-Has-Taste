# Fresh build review — PASS

Job `primary-20260912-ray-west-j-release-868ef104b3ea`; citation attempt 2; launch `ff8a352f-ad4d-4eb8-83f5-ae31f830433d`; UTC 2026-09-12T16:20:40.393944+00:00.
Manuscript digest `88064f2101397ed813a05ddc4ded0858ec9e9f132bb77e394ae666ca61024116`; PDF digest `75f184f2ee498c46b38ff3ae7f05b92076719ba8dcc5034e43f8f20e0031d285`.

Forced a clean build using `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex` from `manuscript`. Exit status 0; BibTeX and pdfLaTeX converged. No manuscript or bibliography edit was needed. The final TeX/BibTeX logs were scanned for undefined citations/references, missing database entries, repeated entries, LaTeX failures and overfull/underfull boxes; none occurred.

The bibliography checker found five citation keys, five BibTeX entries and five auxiliary bibliography keys, with no missing or extra keys. The source has only the canonical bibliography and no external figures or auxiliary authored TeX inputs; the `.fls` dependencies were inspected. Publication source_files contains the complete authored inputs plus companion reproducibility instructions.

`pdfinfo` reports seven A4 pages and correct title, author and subject. All 19 font entries are embedded, subsetted and have Unicode mappings. The PDF contains no JavaScript and is not encrypted. PDF text is nonempty and was compared with the source and rendered pages. The manuscript was refrozen after the clean build; the mathematical snapshot did not change. The build logs and metadata are recorded in `audit/release-build-console.log`, `audit/release-pdfinfo.txt`, `audit/release-fonts.txt`, `audit/release-bib-keys.txt` and `audit/release-pdf-text.txt`.
