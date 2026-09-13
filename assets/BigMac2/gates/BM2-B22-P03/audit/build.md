# Fresh clean-build audit

The manuscript was rebuilt from the declared sources on 2026-09-09 with

```text
cd manuscript
latexmk -pdf -gg -interaction=nonstopmode -halt-on-error main.tex
```

The command exited successfully after the required LaTeX/BibTeX reruns and
produced `manuscript/main.pdf` with four A4 pages and 236,186 bytes.  The final
compiler transcript is `manuscript/main.log`, SHA-256
`bf61186bc860d81b863fce890226a653ffaa24dca317a670628bf24831641342`.
The intermediate first-pass undefined references were resolved by latexmk;
the final log has no fatal error, undefined citation/reference, multiply
defined label, overfull/underfull box, LaTeX/package warning, or rerun request.
BibTeX used exactly three entries and reports zero warnings.

TeX emitted the informational pagination diagnostic “Infinite glue shrinkage
found in box being split” while splitting the `longtable`; it explicitly
records that the condition was ignored.  This is not an unresolved reference
or build failure.  The affected page break and repeated table header were
inspected in the rendered pages: all rows, rules, headings, and surrounding
text are intact, aligned, and legible.

`pdfinfo` confirms the intended title and author metadata, A4 geometry, no
encryption, four pages, and PDF 1.7.  `pdffonts` shows every listed Type 1 font
embedded with Unicode mapping.  `pdftotext` returns nonempty text including
the theorem, limitations, and all three references.  The resulting PDF digest
is `dbb918ed658ee709bf1cb4f431f80e5cf699aafe2619a8a2b113aee247f80fe5`.

**Verdict: ACCEPT; clean build.**
