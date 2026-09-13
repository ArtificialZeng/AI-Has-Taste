# Fresh build audit

I confirmed the accepted mathematical snapshot with `check-math`, removed
generated LaTeX products with `latexmk -C`, and ran the publication command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from
`manuscript/`. pdfLaTeX, Biber 2.21, and the required pdfLaTeX reruns completed
successfully. Biber found all three citekeys and the final log reports a
four-page PDF. Inspection of the final compiler and Biber logs found no fatal
error, emergency stop, undefined citation, undefined reference, rerun request,
overfull box, or underfull box.

`pdfinfo` reports an unencrypted four-page letter-size PDF with the intended
title, author, subject, and keywords. `pdftotext` extracts nonempty text,
including all numbered equations, theorem text, disclosure, data statement,
and three resolved bibliography entries. The bound build log is
`manuscript/main.log`, SHA-256
`c1c456acdd1fb42b7d0028b52d206e574ab4c44459a27475c97fa3f6d5478ba0`.

**Verdict: ACCEPT.** This is a clean reproducible build of the frozen authored
sources.
