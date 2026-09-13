# Fresh clean-build audit

## Provenance

Release job `bigMac-00008-p02-release-3defdfe0b6e1` audited the current
evidence/manuscript/PDF bindings:

- evidence snapshot: `cf4597267e383e2f6d584b9ff7d0a39dc9e6aea0ab3436c568fe4ad6aebf1752`;
- manuscript digest: `a5410eeaa54fffd182f197ac68b5f94a0eb68f05b50790ec06872846b789bff5`;
- PDF digest: `f248e5787b17ec5a563a9de3ac25df0612805c5d84dfbdc5f3e3e2b40cf2a621`.

## Clean rebuild

I removed the generated LaTeX state with `latexmk -C main.tex` and then ran the
declared publication command from `manuscript/`:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The rebuild started without an auxiliary file, ran pdfLaTeX, BibTeX, and the
necessary final pdfLaTeX pass, and exited successfully with all targets current.
The actual final compiler transcript is `manuscript/main.log`, is nonempty, and
has SHA-256
`c40b7f2ed98047df801bbad95762b1290f7dc0adab6bed095731642d9311a266`.

## Log, reference, and PDF checks

- The final compiler log has no fatal errors, undefined references/citations,
  multiply defined labels, missing-file diagnostics, overfull boxes, underfull
  boxes, or LaTeX/package warnings. The BibTeX log reports zero warnings.
- `manuscript/main.aux` contains both requested citation keys, both corresponding
  `bibcite` records, and resolved labels for Theorem 1, Lemmas 2--3, and equations
  (1)--(16).
- `pdfinfo` reports a valid unencrypted five-page letter-size PDF, with title,
  author, and subject matching the manuscript. `pdftotext` extraction is nonempty
  and contains both numbered references.
- `pdffonts` reports every used font embedded and subsetted with Unicode mapping.
- The recorder file shows no undeclared authored TeX, bibliography, figure, or
  local-style dependency. Generated `.aux`, `.bbl`, and `.out` files are not
  source inputs.
- Fresh runs of both exact verification programs passed after the build.
- `source.md` remains byte-for-byte unchanged at SHA-256
  `93dae429fcc298c6e538247a4cdaa8e4d6dbaddc20ed8cb4bc7fe60f9cc8d088`.

Transient undefined-reference messages from the deliberately auxiliary-free
first pdfLaTeX pass were resolved by BibTeX and the final pass; they do not occur
in the bound final compiler log or output.

## Verdict

**ACCEPT.** The bound PDF is the result of a clean successful build, and the
current final log is free of unresolved citations/references and substantive
compiler or layout diagnostics.
