# Build audit

The canonical sources were rebuilt from a cleaned auxiliary state with

```text
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final converged run succeeded and produced a four-page PDF.  The final
`manuscript/main.log` has SHA-256
`15cd7be707bae423c7492553fbbbcec9defc5f9250a2b3506f8922668b8534cf`.
A scan of the final `.log` and `.blg` found no undefined citation or reference,
missing database entry, BibTeX warning, repeated entry, LaTeX error, fatal error,
emergency stop, undefined control sequence, or runaway argument.  The bibliography
checker reports three cited keys, three available entries, zero missing/unused
entries, and exact `.aux` agreement.

`pdfinfo` reports four letter-size pages, no encryption, and valid metadata:
title *Rigidity at the Ideal Endpoint for Equiangular Hyperbolic 4-Cubes*, author
Xiaojian Zeng, and subject *Hyperbolic 4-polytope rigidity at the ideal endpoint*.
`pdffonts` reports that every font is embedded.  The PDF SHA-256 is
`e81fb2000a28b9979af53203dbcaed986aaac0e1cce7502021de82baced0cec7`.
