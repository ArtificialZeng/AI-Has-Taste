# Fresh build audit

## Bound artifacts

- Publication PDF: `manuscript/main.pdf`, SHA-256
  `35665e8331dce8129d62ea8b66c88da8669115f5e094b2613c38294004b646df`.
- Existing compiler log: `manuscript/main.log`, 25,531 bytes, SHA-256
  `9a02788ea72711b912d9a9dde76ae1af964e5314f6debff2aaaa8ef91c0be428`.
- Build command checked: `cd manuscript && latexmk -pdf
  -interaction=nonstopmode -halt-on-error main.tex`.

The command completed successfully and reported that the frozen PDF was
up-to-date; its digest was unchanged before and after the check.  The bound
log records a successful pdfTeX build of four pages.  I inspected the entire
log and BibTeX log: there is no fatal error, undefined citation or reference,
multiply defined label, LaTeX/package warning, overfull/underfull box, or
rerun request.  The BibTeX log reports zero warnings.  Every internal
equation/theorem reference and both bibliography citations resolve in the
extracted PDF.

`pdfinfo` reports an unencrypted, non-suspect four-page letter-size PDF 1.7
with the intended title and author.  `pdftotext` extracted 8,444 nonempty
bytes.  `pdffonts` lists only embedded subset fonts, all with Unicode maps.
The two publication sources have the hashes recorded in the current
manuscript snapshot, and no authored local dependency is omitted from
`publication.json`.

**Verdict: accept.**  The existing build log is current, nonempty, clean, and
cryptographically bound to this audit; the compiled PDF matches the frozen
manuscript snapshot.
