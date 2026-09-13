# Fresh clean-build audit

**Verdict:** ACCEPT

The manuscript directory was first cleaned with `latexmk -C main.tex`, then
built from the two sources declared in `publication.json` using

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build completed successfully after BibTeX and the required LaTeX reruns.
The current final transcript is `manuscript/main.log`, SHA-256
`d19ef1cbd9740a7d099c7648985a578fd36181da62f61ed5ebb689f5d32c9b36`.
The final log and `main.blg` contain no errors, undefined citations or
references, multiply-defined labels, LaTeX/package warnings, overfull boxes,
or underfull boxes.  All six citation occurrences resolve to the three
expected bibliography entries, and all theorem/equation cross-references are
present in `main.aux`.

The output is a valid, nonempty four-page PDF (SHA-256
`c48cda58c31b61f1df7183905c97bd3978ef96eba6a129238c4a90efedec2941`).
`pdfinfo` reports the intended title, author, subject, and keywords.  `pdffonts`
reports every font embedded, subsetted, and Unicode-mapped.  Text extraction
is nonempty.  The final authored statement is exactly the accepted
resolution-paper scope; the release edit only repaired citation metadata and
added PDF metadata, without altering the mathematics.
