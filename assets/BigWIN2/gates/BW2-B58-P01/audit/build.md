# Fresh clean-build audit

The final source was built from a cleaned auxiliary state with

```text
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

in `manuscript/`.  Latexmk converged after BibTeX and a second pdfLaTeX pass.
The final `main.log` contains no undefined citation/reference, LaTeX error,
fatal error, emergency stop, repeated entry, overfull box or underfull box
diagnostic.  `main.blg` contains no missing database entry or BibTeX warning.

The bibliography checker reports three cited keys, three BibTeX entries, zero
missing files/keys, zero unused entries, and exact agreement with all three
final `aux` bibcite keys.  `pdfinfo` reports a valid unencrypted four-page
letter-size PDF and the intended title, author, subject and keywords.  All 18
fonts reported by `pdffonts` are embedded Type 1 fonts with Unicode mappings.

Final build log SHA-256:
`881351c3a81596e51aa3f266bc75241abdbde3d4d787bbdb451b00e0b6b6c9d5`.
