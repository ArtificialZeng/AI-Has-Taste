# Clean-build audit

**Job:** `win-00086-p07-release-355ff84f5321`  
**Mathematical snapshot:** `4cf87cb9ea162f6513208d0fb7f067f9d89b3118d6c8b3fdda7f2377eb1f899f`  
**Manuscript digest:** `c5a200dedb8fc24fbf35915c0407d1b52ee42e0a3dff2d5342a1da0eb5055cdf`  
**PDF digest:** `afb95c1775998b3b1ddbecd831f9ef49129aab0c0a5379309ce951315725dd7f`

The canonical command completed successfully and converged:

```text
cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -g main.tex
```

BibTeX 0.99d and pdfTeX 1.40.22 produced a four-page letter-size PDF. The
converged `main.log` and `main.blg` contain no LaTeX error, fatal error,
emergency stop, undefined control sequence, runaway argument, undefined
citation/reference, missing database entry, repeated entry, BibTeX warning,
overfull box, or underfull box diagnostic.

The read-only bibliography checker reports five cited keys, five bibliography
keys, no missing or unused key, and exact agreement with `main.aux`.
`pdftotext` extracted all four pages. `pdffonts` reports every font embedded.
`pdfinfo` reports the correct title, author Xiaojian Zeng, four pages, letter
size, and an unencrypted PDF. The final build log SHA-256 is
`02043fbe1b7d01e5b6b2a3f29c0785e3d4f39df44cfc5ddbe40bebd50cdce2c2`.

The only source edits in this release pass are scope-preserving parser
compatibility notation (`T^{*}`, `\lnot`, explicit indexed `\vee`/`\wedge`,
and `\mathrel{|=}`) and explicit PDF title/author metadata. They do not alter
the accepted claim, proof, numerical data, citations, or bibliography.

**Verdict:** accept; clean build.

