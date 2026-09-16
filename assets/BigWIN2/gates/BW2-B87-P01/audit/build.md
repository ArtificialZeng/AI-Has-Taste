# Clean-build audit

Release job `win-00087-p01-release-38ca90bfe4c5` was checked against
snapshot digest
`aa8bc8a4188203e53f8d6df1ad6e9190eae01dd1b8a32e2919d91fd1171312e9`
and PDF digest
`5db8179a7b52d8e5f1c0c8da7a2eddd42ebcd39aa6a264560e5dd20d44cb14ca`.

I removed generated LaTeX products with `latexmk -C main.tex`, then ran the
declared build command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from
`manuscript/`.  Latexmk ran pdfLaTeX, BibTeX, and a converging pdfLaTeX pass;
the final target is a three-page PDF.

The final `manuscript/main.log` has SHA-256
`85c1ad96a464f506b252cdfdf07492d850a74907cd97035bfe6e5a78fcb0f270`.
Scanning it and `manuscript/main.blg` found no undefined citation or reference,
missing database entry, duplicate entry, BibTeX warning, LaTeX error,
emergency stop, fatal error, undefined control sequence, or runaway argument.
The bibliography checker reports five cited keys, five BibTeX entries, no
missing or unused key, and exact `.aux` agreement.  `pdfinfo` reports a valid,
unencrypted, three-page letter-size PDF, and `pdffonts` reports every font as
embedded with Unicode mapping.

**Verdict: accept.**
