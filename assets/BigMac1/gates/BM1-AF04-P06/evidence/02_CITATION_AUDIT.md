# Citation audit

Audit date: 2026-08-30.  Four citation keys were extracted from
`paper/main.tex` and checked serially.  Parallel citation agents were not used
because the user required the current Codex CLI to be the sole executor.

| Key | Cited claim and location | Official record | BibTeX action | Key change | Uncertainty |
|---|---|---|---|---|---|
| `Lam_2000` | Group-ring methods, weight restrictions, and smallest asymmetric examples; Introduction | DOI/Crossref and publisher: https://doi.org/10.1006/jabr.1999.8089 | Used DOI content-negotiation export unchanged | none | none |
| `Sivek_2010` | Cardinalities of vanishing subsets of distinct roots, not minimal-orbit classification; Introduction | Publisher and primary PDF: https://doi.org/10.1515/integ.2010.031 | Used DOI export; supplemented pages 365--368 from the publisher record because the export omitted them | none | none |
| `christie2025classifyingminimalvanishingsums` | Proved type classification through 16 and current conjectural computer extension through 21; Introduction | arXiv v2: https://arxiv.org/abs/2008.11268 | Used official arXiv BibTeX export; added the visible v2 identifier and URL to `note` for `amsplain` | none | none |
| `TheoremDB105` | Seven fixed-conductor affine orbits through 19 and weight 20 left open; Introduction | TheoremDB P2744 snapshot: https://theoremdb.org/statements/minimal-vanishing-105th-root-sums | Transcribed the page's displayed “How to cite” record into `@misc`; added visible access URL | none | No native BibTeX export was provided; the entry is a faithful format conversion of the official citation text. |

The citation context was checked against the primary text, not merely against
metadata.  In particular, Sivek's theorem concerns existence by cardinality and
does not settle minimality, while the current Christie--Dykema--Klep revision
separates its proof through weight 16 from the conjectural implemented range.

Mechanical checks:

```text
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  main.tex --aux main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  main.tex references.bib
```

Results: 4 cited keys, 4 bibliography keys, 0 missing, 0 unused, and 4 matching
`.aux` entries.  Final `main.log` and `main.blg` contain no undefined citation,
missing database entry, repeated entry, BibTeX warning, LaTeX error, overfull
box, or underfull box.  No citation key changed and no citation remains blocked.
