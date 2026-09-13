# Citation audit

Audit date: **2026-08-30 Asia/Shanghai**.

The project contract requires one CLI executor and serial Builder, Breaker,
Certifier, and Referee roles, so citation verification was performed serially
rather than delegated.  Every retained citation key, bibliographic record, and
the claim attached to each occurrence was checked.

| Key | Occurrences in `paper/main.tex` | Claim checked | Record checked | Result |
|---|---|---|---|---|
| `Honold2016` | line 59 | source for the mixed-dimension definition and bounds context | AIMS publisher and Crossref DOI `10.3934/amc.2016033`: authors, exact title, journal 10(3), 649--682, 2016 | pass |
| `Heinlein2019` | lines 61, 78 | 333 three-dimensional codewords, minimum distance four, and Appendix C generators/representatives | AIMS publisher, arXiv `1708.06224v5`, and Crossref DOI `10.3934/amc.2019029`: authors, Theorem 2, Appendix C, journal 13(3), 457--475, 2019 | pass after title repair |
| `Heinlein2020` | line 63 | published upper bound \(A_2(7,4)\le388\) obtained using SDP | AIMS publisher, arXiv `1809.09352v2`, Theorem 1.1, and Crossref DOI `10.3934/amc.2020034`: journal 14(4), 613--630, 2020 | pass |
| `SubspaceCodesTable` | line 64 | dated specialist table displays 334--388 | Bayreuth binary mixed-dimension table, row \(n=7\), column \(d=4\), accessed in Gate 1; a later command-line retry was unavailable and was not treated as contrary evidence | pass with dated-access qualifier |
| `TheoremDB2026` | line 68 | public replay closes radii through five and lists radius six as the next experiment | TheoremDB P2796, R497, R500, and R504, snapshot reviewed 2026-07-28 and rechecked in both novelty passes | pass |

## Repairs and normalization

- Crossref's 2019 BibTeX export embeds malformed HTML in the mathematical
  title.  The title was normalized from the publisher metadata to
  “A subspace code of size 333 in the setting of a binary \(q\)-analog of the
  Fano plane.”
- An initial manuscript entry incorrectly paraphrased the end of that title as
  “7-dimensional ambient space.”  The audit caught and corrected it before the
  clean build.
- Unicode page-range dashes from Crossref were normalized to BibTeX `--`.
- No author, year, DOI, volume, issue, or page fields were inferred from a
  secondary bibliography.

## Automated checks

After the final build, `check_bib_keys.py` reports five cited keys, five BibTeX
entries, zero missing keys, zero unused entries, and zero missing AUX
bibliography labels.  The final `.bbl` is generated from
`paper/references.bib`; no manual `.bbl` edits were made.
