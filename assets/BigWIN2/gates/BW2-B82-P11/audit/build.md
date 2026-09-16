# Clean-build audit

Job: `win-00082-p11-release-537ef5a321bf`

The canonical build was cleaned with `latexmk -C main.tex` and rebuilt in
`manuscript/` using

```
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The converged build succeeds and produces a five-page PDF.  The final
`manuscript/main.log` SHA-256 is
`f6d08d46ba3ac61f1b1b4689940030dcb55d0fb8c50e046d5da4c6b85a94afde`.
Final scans find no undefined citation or cross-reference, missing or repeated
BibTeX entry, LaTeX error, fatal error, emergency stop, undefined control
sequence, runaway argument, or overfull box.  The bibliography checker finds
four cited keys and four entries with exact AUX agreement.  All PDF fonts are
embedded subsets; text extraction works; the document is unencrypted, has no
JavaScript, uses letter-size pages, and reports five pages.  Two harmless
underfull bibliography lines remain visually legible and do not cross a page
boundary.
