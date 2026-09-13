# Fresh clean-build audit

I performed a from-scratch build on 8 September 2026 by running

```text
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

in `manuscript/`. The build completed with exit status zero after the expected
cross-reference rerun. The final compiler transcript is
`manuscript/main.log`, SHA-256
`4db038ae6223d81bde5534bda71c0d35dc9a296c945bb17bebaa1f4c65b9f166`.

The final log contains no LaTeX/package warnings, errors, fatal diagnostics,
undefined citations, undefined references, rerun request, overfull box, or
underfull box. It contains one harmless `microtype` informational message
about ignoring protrusion for a missing small-caps character; the rendered
text is intact. The auxiliary file binds both citation keys and every
cross-reference used by the manuscript.

`pdfinfo` identifies a five-page, unencrypted letter-size PDF with the intended
title, author, subject, and keywords. `pdffonts` reports every font embedded
and Unicode-mapped. `pdftotext` extracts nonempty text from every page (page
character counts 1786, 1787, 2831, 2083, and 2265). The `%PDF-` output is
nonempty and has SHA-256
`19888698d7f2d0de11384534df76a0dec749a4340a3f9c1231e6478013fb08c4`.

The recorder file shows no unlisted authored dependency: apart from TeX system
packages and generated `main.aux`/`main.out`, the sole local source input is
`main.tex`, agreeing with `publication.json`.

**Verdict: accept; clean build.**
