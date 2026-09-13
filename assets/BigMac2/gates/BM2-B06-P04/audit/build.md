# Fresh clean-build audit

On 2026-09-07 I reran both declared exact verifier scripts, then built from a
genuinely clean state with:

```text
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both verifiers returned empty mismatch lists. The clean build completed with
pdfTeX/TeX Live 2026 and BibTeX. Expected first-pass undefined messages were
resolved by BibTeX and subsequent LaTeX passes; the final `manuscript/main.log`
contains no fatal error, undefined citation/reference, rerun request, overfull
box, or underfull box, and `main.blg` reports zero warnings.

The resulting `%PDF-` file has six letter-size pages, nonempty extractable text,
embedded Type 1 fonts, and no encryption or JavaScript. Empty title/author PDF
metadata fields are a non-rendering limitation, not a build failure. The final
build-log SHA-256 is
`6162fd4ba01bcc1c0ceeb53b063ff65b31b244f402ccc4ac018d80084714a473`.
After the clean build, `freeze-manuscript` bound manuscript digest
`c23d26d2584719649ee3db4ada9697f708ed078781cb7e5db02f51b184d924f7`
to PDF digest
`b4b04e9f967e139efa2217af474d321fc423d25cd8fa56e827274e34b7444093`.

**Verdict: accept the clean build.**
