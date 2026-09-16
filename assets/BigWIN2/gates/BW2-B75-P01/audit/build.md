# Build audit

**Verdict:** accept  
**Release job:** `win-00075-p01-release-2a110e7491e7`

The current manuscript PDF is the output of a completed clean `latexmk` build using:

```text
cd manuscript && latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The active citation validator exposed a deterministic parser incompatibility with an invoked one-argument cardinality macro and with the prior font package. The macro was expanded at its five uses, the font setup was changed to the validator-supported Latin Modern plus `amssymb`, and the accented word “Bézout” was encoded directly in UTF-8. These are scope-preserving source/typesetting changes: the theorem, equations, proof, citations, and bibliography are unchanged. The manuscript was then cleanly rebuilt and refrozen before the build and visual audits.

Checks performed on the live files:

- `main.log` is nonempty and has SHA-256 `2afcbf7fbf06c9ad3a1bacfdd762653d8a3bc00b3fc0b301a606b1b6a55ade6b`.
- No TeX fatal error, emergency stop, undefined citation, undefined reference, BibTeX database error, duplicate-entry warning, or rerun-required diagnostic remains.
- The AUX/BibTeX citation set equals the five ordinary body-flow citation keys.
- `pdfinfo` recognizes a five-page, unencrypted A4 PDF with extractable content and no JavaScript.
- `pdffonts` reports every listed Type 1 font as embedded; all listed fonts have Unicode mapping.
- The PDF SHA-256 is `25315f0c1a05367617ffb20dd69dc960657592d5e1e5b9619fa915926a71bae3`.

The compilation audit therefore accepts the frozen five-page PDF.
