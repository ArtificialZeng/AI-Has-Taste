# Citation audit

Audit date: 2026-08-29  
Mode: primary-source web verification plus LaTeX/BibTeX consistency audit  
Verdict: **PASS**

The manuscript has one cited work, so the `bib-reference-audit` skill's
few-citation exception was used and no citation subagent was spawned.

| Key | Manuscript uses | Verification source | Result |
|---|---|---|---|
| `Gaetz_2016` | Conjecture 7.6 and the reported (n\le7) computation; Algorithm 1/Theorem 3.1; baseline counts; the multi-box shape-change warning | Official EJC article page and PDF; DOI `10.37236/4805`; arXiv `1409.6659v2` for version history | Authors, title, journal, volume 23, issue 1, article P1.40, year 2016, and every cited mathematical location verified |

The five in-text uses are at `paper/main.tex` lines 55, 137, 170, 207, and
approximately 222 (the last may shift mechanically). All are supported by the
same primary paper and no citation key was renamed.

The BibTeX entry was taken from official DOI metadata and normalized without
changing authorship or title. The article number `P1.40`, present on the EJC
record, was added as the `pages` field and the DOI URL was normalized to HTTPS;
this removed BibTeX's missing-pages warning.

Final automated checks: one cited key, one bibliography key, zero missing keys,
zero unused entries, zero keys missing from `.aux`, zero undefined citations or
references, and zero BibTeX database warnings or duplicates.

The novelty statement is separately bounded by the two-pass search log; this
audit does not turn a negative search into a universal absence claim.
