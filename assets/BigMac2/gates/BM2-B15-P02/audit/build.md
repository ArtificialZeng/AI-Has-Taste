# Fresh clean-build audit

Release job: `bigMac-00015-p02-release-5446c3c97a60`.

I removed the prior LaTeX auxiliary/output state with `latexmk -C main.tex`
and ran the declared command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

from `manuscript/`.  The build ran pdfLaTeX, BibTeX, and the required rerun,
then reported the target up to date.  The final compiler transcript is the
nonempty `manuscript/main.log`, SHA-256
`ebcc545df3a4c8269e1058730bde4bac7e72c8bf98c2d6af80cc3b614b340746`.
It ends with `Output written on main.pdf (5 pages, 296048 bytes)`.

The final transcript has no fatal error, emergency stop, undefined citation or
reference, LaTeX/package warning, rerun request, overfull box, or underfull box.
`manuscript/main.blg` reports three used entries and `warning$ -- 0`.  The PDF
has a valid `%PDF-` header, five A4 pages, extractable text, title
`Critical First Sign Failure of Even Cumulants for the Blume--Capel Single-Site
Law`, and author `Xiaojian Zeng`.

The fresh build was frozen in `audit/manuscript-snapshot.json`; its manuscript
and PDF digests match this audit.  Verdict: **accept** (`clean_build=true`).

