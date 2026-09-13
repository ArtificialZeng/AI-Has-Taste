# Fresh build audit

The accepted publication sources were rebuilt from a clean generated-file state
on 2026-09-07:

```text
cd manuscript
latexmk -C article.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex
```

`latexmk` completed successfully after the normal BibTeX and rerun cycle and
reported `article.pdf` up to date.  The current final compiler transcript is
`manuscript/article.log`, SHA-256
`4ba33b6165274d2342ad10e9309efad985f194086769a9d166ff83d8ccd3a4ea`.
The final transcript contains no LaTeX/package warnings, undefined citations or
references, multiply defined labels, overfull/underfull boxes, fatal errors, or
emergency stops.  `manuscript/article.blg` reports two entries and zero BibTeX
warnings; `article.aux` contains all fourteen equation/theorem labels and both
`\\bibcite` records.

`pdfinfo` identifies a valid, unencrypted five-page letter-size PDF with the
intended title and author.  `pdftotext` produces nonempty text including both
resolved references.  `pdffonts` reports every font embedded and subsetted.
The PDF SHA-256 is
`686b7969702fea9d9276d391960696a55b698637c9bb60c865b4444ba071fcbb`,
matching `audit/manuscript-snapshot.json`.

**Verdict: accept; clean build.**
