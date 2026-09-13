# Fresh clean-build audit

The accepted mathematics gate passed immediately before building.  From
`manuscript/`, I ran

```text
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error article.tex
```

The `-gg` run performed a full cleanup and rebuilt the document, bibliography,
cross-references, and PDF.  Latexmk completed successfully after the expected
initial-pass citation/reference resolution and reported all targets up to date.
The retained final compiler transcript is `manuscript/article.log`, SHA-256
`4a7657dbcf1f511d4427bd18b7f40e7b62ae4b26851b8d36d83a84bb2233e29e`.

The final log reports `Output written on article.pdf (5 pages, 317372 bytes)`.
It contains no LaTeX or package warning, undefined citation/reference,
multiply-defined label, overfull/underfull box, fatal error, or emergency stop.
The BibTeX transcript uses all three database entries and has `warning$ -- 0`;
its `missing$ -- 2` line is the standard BibTeX function-call counter, not a
missing-field diagnostic.  The extracted PDF text is nonempty, all three
references are resolved, and `pdfinfo` reports the intended title, author, A4
page size, and five pages.  `pdffonts` reports every font embedded and subsetted.

After this clean build, `freeze-manuscript` bound the unchanged manuscript
digest `8726002cf99990b0538a7b3cc103b078be1fb51180d4d326b035c7056f1a3f9c`
to the fresh PDF digest
`dc0e7cdad08b8ab44088b5088619856056551f5360bb75b42e564881efc0eee7`.

**Verdict: ACCEPT.**  The current PDF is the product of a clean, warning-free
build and its retained log is digest-bound below.
