# Fresh clean-build audit

## Build performed

On 2026-09-09 I removed the prior generated LaTeX products with
`latexmk -C main.tex` and ran the recorded publication command from the
`manuscript` directory:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The command exited 0 after the required pdfLaTeX/Biber passes and reported all
targets up to date.  Biber found exactly five citekeys in
`manuscript/references.bib` and emitted no warnings or errors.

## Log and output checks

- Bound build log: `manuscript/main.log`, SHA-256
  `6839897ee66bdcdb2cb876061e709397af1c5b6974a1f22afd6852f8d585f0a1`.
- The stabilized log contains no LaTeX or package warning, fatal error,
  undefined reference/citation, multiply-defined label, overfull box, or
  underfull box.  Normal informational package text is not a warning.
- `main.fls` identifies `main.tex` plus system packages and generated
  intermediates; Biber identifies `references.bib`.  This agrees with the two
  source files declared in `publication.json`; there is no authored figure,
  imported TeX file, or custom local style.
- `pdfinfo` reports a nonencrypted three-page letter-size PDF with title
  *Entropy Concavity for All Three-Bit Overlap Bernoulli Distributions* and
  author Xiaojian Zeng.  SHA-256 is
  `86903f0d656433a09cdef9027eb093300e73a6fbadad0b50d95fd2eaea0ce4a0`.
- `pdftotext` produced complete nonempty text, including all theorem and
  equation references and all five bibliography entries.  No unresolved `?`
  marker appears.
- `pdffonts` reports every font embedded and subsetted with Unicode mapping.

## Verdict

**Accept.**  This is a clean, reproducible, warning-free build bound to the
current manuscript and PDF snapshots.

