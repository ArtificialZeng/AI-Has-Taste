# V14 builder, reproducibility, and visual audit

Date: 2026-08-25 (Asia/Shanghai)

## Verdict

**PASS as a submission-ready partial-results preprint.**  This verdict is
limited to the five exact positivity families stated in `main.tex`.  It is
not a solution of the unrestricted fixed crossing-lens constant, the full
compact-ball quartic, the general complex common-metric gate, or the
arbitrary-node bridge.

## Exact-certificate replay

The package-local source generators and independent reconstruction programs
were rerun from the packaged files.  They passed the structural counts,
exact rational arithmetic, legality inequalities, Bernstein controls, seam
identities, raw-gate diagnostics, and fail-closed scope checks.

For the new inward-Z frontier cell, the frozen exact objects are:

- source SHA-256 `1a2ef5c669d1602a27641f05ae1d051e7f03d6db99a8280085b3ececd23667a4`;
- independent verifier SHA-256 `9d00fc3b026bd6751831e412205fb2803a9026c6eba38c408f5c861f886b1642`;
- 32 nonzero `(S,X)` coefficients, 1,581 centered monomials, bidegree `(7,4)`;
- 40/40 strict centered Bernstein controls, with exact weakest reserve
  `119539987320009056100108078372012547879/718761099264000000000000000000`;
- 72/72 exact legal raw-gate diagnostics positive;
- exact chart-legality bracket
  `83059/100000 < X_chart < 4153/5000`.

The upper bracket is a chart obstruction only: it is neither a negative value
of the original gate nor a maximality theorem.  Numerical diagnostics are
reported only as falsification checks and are not used as continuum proofs.

One packaging-only failure occurred during the first package-local replay:
the compact-ball reduction audit required by the frontier verifier had not
yet been copied into the candidate directory.  The missing frozen dependency
was added without changing any mathematical source, and the complete replay
then passed.  Its SHA-256 is
`0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20`.

## Bibliography audit

All 5 cited keys occur in `references.bib` and in the generated `main.bbl`.
The independent bibliographic audit verified 5/5 records against official
publisher or bibliographic sources, with no key change, no database repair,
and no unresolved citation.  See `audits/BIB_AUDIT_V14.md`.

## Deterministic clean builds

Two clean copies were built in different random temporary directories using

```sh
SOURCE_DATE_EPOCH=1787625600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both PDFs and the builder copy are byte-identical:

`75ed2727eceb0b0d6aa698c3de98b399dcb98ab31adca6e710983b41ab956203`

Each has 31 Letter pages and a file size of 540,213 bytes.  The final log has
no overfull or underfull boxes, no undefined citations or references, and no
LaTeX/package warnings or fatal errors.

## PDF and visual checks

- PDF version 1.7; no encryption, forms, JavaScript, or suspect objects.
- Every listed font is embedded, subset, and Unicode-mapped.
- All 31 pages were rendered to PNG and inspected in four contact sheets.
- Pages 1, 19, 20, 21, 30, and 31 were additionally inspected at original
  render resolution.
- No clipping, overlap, missing glyph, broken formula, or illegible author
  metadata was found.
- The title page names all five authors and identifies Yonghua Xiong as the
  corresponding author; page 31 contains the supplied affiliations and email
  addresses.

## Builder conclusion

Fatal findings: 0.  Major findings: 0.  Minor findings: 0.

The candidate may be frozen and sent to an independent final referee.  Any
claim that the unrestricted problem has been solved would contradict both the
paper and this audit.
