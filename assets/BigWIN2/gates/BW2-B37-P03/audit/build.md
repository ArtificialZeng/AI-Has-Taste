# Build audit

Audit date: 2026-09-06. Release job:
`win-00037-p03-release-aa71e4f3e69c`.

- A clean `latexmk -C main.tex` followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged
  successfully from `manuscript/` and produced a three-page PDF.
- The bibliography checker reports five cited keys, five BibTeX entries, and
  five AUX bibliography keys, with zero missing, unused, or unresolved keys.
- The converged `main.log` and `main.blg` contain no LaTeX/BibTeX error,
  undefined citation/reference, repeated entry, package warning, or fatal
  diagnostic.
- `pdfinfo` reports the correct title and author, letter-size pages, embedded
  PDF metadata, no encryption, and PDF 1.5.
- `python3 evidence/verify_mod32_obstruction.py` reports seven distinct
  coordinate contributions, exactly 520 compressed states after 18
  coordinates, and none of the three targets reachable.
- Immutable `source.md` remains SHA-256
  `1a82944067ef730d97a127bb6727cf78951aa8e5e875521b03a2d9ba06777180`.

Result: accept. PDF SHA-256 is
`a97076fe7d1959fc9d769b91ded4f2080ece5f7103e1940749f286ffd11928da`;
converged build-log SHA-256 is
`2a06759faeff22bffe008c9ea510124d7db7bab8eed74c71693af31e8391724b`.
