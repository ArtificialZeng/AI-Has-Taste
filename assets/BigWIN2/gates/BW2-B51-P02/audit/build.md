# Clean-build release audit

The manuscript was cleaned with `latexmk -C main.tex` and rebuilt in `manuscript/` with

```
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The converged build succeeded and produced a three-page PDF.  The final `manuscript/main.log` SHA-256 is `8ae752e04a82795679d11bae68a0a3bebb3249ad594af3f6a730d65a4cc12646`.  A diagnostic scan of the final `.log` and `.blg` found no undefined citation or reference, missing database entry, repeated BibTeX entry, LaTeX error, fatal error, emergency stop, undefined control sequence, runaway argument, or BibTeX warning.

The bibliography key checker reports four cited keys, four bibliography keys, no missing or unused entries, and exact agreement with the final `.aux`.  `pdfinfo` reports a valid unencrypted PDF 1.5 file with three letter-size pages, title `The Connectivity-Code Number of C3 square C4 Is 16`, and author `Xiaojian Zeng`.  `pdffonts` reports every listed font embedded and subsetted.  Cross-references to Theorem 1 and Table 1 resolve in the rendered PDF.

**Verdict: accept.**
