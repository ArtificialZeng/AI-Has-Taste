# Fresh clean-build audit

## Binding

- Release job: `bigMac-00020-p03-release-c9a19d6ffd27`
- Evidence snapshot: `ba716a810c205d214da52cc5b993cc6650f9d7be715542223f01b7730d054ed1`
- Manuscript snapshot: `bd015dc13f52987325070cf4e693b435b741af53cfb4ca39b5833614c783acac`
- PDF SHA-256: `26b9137506abf8974f01d8805d27f89cd4d89d54d67312fbb31aabe629b8257c`
- Build log: `manuscript/main.log`
- Build-log SHA-256: `f5adace40bf4471053d4baa26a83761778bf1f5bddc162717badfdf2fd0a6846`

## Clean build and inspection

I removed the generated LaTeX outputs with
`latexmk -cd -C manuscript/main.tex`, then ran the declared command
`latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`
from the project root. The build began without an auxiliary file, ran
pdfLaTeX, BibTeX, and the required final pass, and exited successfully.

- The current nonempty final compiler log contains no LaTeX/package warning,
  fatal error, unresolved citation/reference, rerun request, overfull box, or
  underfull box. `main.blg` reports zero warnings and resolves
  `JonesKinnersley2026` from `references.bib`.
- The recorder shows `main.tex` plus generated bibliography products; BibTeX
  records `references.bib`. There is no undeclared local authored TeX import,
  custom style, figure, or bibliography database.
- `pdfinfo` reports a valid, unencrypted, three-page letter-size PDF with title
  *Three Probes Suffice for Directional Localization on the Three-Cube* and
  author Xiaojian Zeng. `pdftotext` extraction is nonempty.
- `pdffonts` reports every font embedded and subsetted with Unicode mappings.
- The immutable `source.md` retains SHA-256
  `a5f6ee89bf21df93a868c15c50725b26f03e8d259a210c27788063657b7da7a5`.

## Verdict

**ACCEPT.** The declared authored sources cleanly produce the bound PDF, and
the current build log is free of unresolved or substantive diagnostics.
