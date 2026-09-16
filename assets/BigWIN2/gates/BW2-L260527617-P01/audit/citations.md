# Citation and bibliography audit

## Binding and result

- Release job: `lit-260527617-p01-release-4b162acd588d`
- Citation attempt: `3`
- Launch UUID: `a5edb3f5-fd71-4072-b5f9-3cc4b24f51f3`
- Frozen mathematical snapshot: `95cd9fcb261ad6fe4df05945af76955e312cda7ba75fce350ac973bbca29f6cf`
- Manuscript digest: `9a63259426e3187bf462df2c2662be51389cb663c1ee497f22834586b3fec9b5`
- PDF digest: `b1523fd8749b16a0c9b2baee2c29b7251c8f6f9887af37614338aa38a6843646`
- Verification date: 2026-09-10 UTC

**Verdict: accept.** The frozen extraction contains eleven citation claims and
eight ordinary body-flow keys. Every source exists, retained bibliography
metadata agrees with a primary or authoritative publication record, and each
source passage supports its nearby claim at the stated scope. There are no
undefined citations, unused entries, decorative references, or unsupported
claims of global novelty.

## Two-pass method

Pass 1 read the canonical manuscript, extracted every ordinary body-flow
citation, and froze the eleven claim/citation pairs in
`audit/citation-claim-ledger.json` before source checking. Its key union is
exactly `DemaineEtAl2014`, `EenSorensson2003`, `IgnatievEtAl2018`, `Sinz2005`,
`Verhoeff2026`, `Wastlund2021`, `WetzlerHeuleHunt2014`, and `Zeng2026GCD`,
which is also the exact body-flow key set.

Pass 2 checked those fixed claims sequentially against original papers,
authoritative records, the checksum-bound local Verhoeff PDF, and frozen local
software and certificate records where a source identifies a tool but the
claim concerns this computation. The standard title/author/year/venue and DOI
or arXiv search variants were run for every key. Exact locators are in
`audit/source-locations.json`; decisions are in
`audit/citation-verification.json`. No subagent was used because this release
job expressly prohibited spawning agents.

## Claim-to-source findings

| Claim | Key | Support checked | Decision |
|---|---|---|---|
| CIT-01 | `DemaineEtAl2014` | Section 3.2 defines the free-group word model and deletion of generators | Verified, paraphrase |
| CIT-02 | `Wastlund2021` | Abstract and constructions give later simplified/improved picture-hanging bounds | Verified, paraphrase |
| CIT-03 | `Verhoeff2026` | Abstract/Section 6 give minimum 16; Section 8 identifies 3-out-of-5 and the about-16 search frontier | Verified, paraphrase |
| CIT-04 | `Zeng2026GCD` | SSRN abstract states exact cardinality circuit, Boolean UNSAT, checkable DRAT, and finite scope | Verified, paraphrase |
| CIT-05 | `Verhoeff2026` | Proposition 15 supplies the construction; direct accepted comparison supplies four cancellations | Verified, source plus exact local check |
| CIT-06 | `Sinz2005` | Section 2 and Theorem 1 give the sequential-counter cardinality encoding | Verified, paraphrase |
| CIT-07 | `IgnatievEtAl2018` | PySAT paper lists Glucose3; frozen reproduction audit gives exact versions and byte identity | Verified, source plus local record |
| CIT-08 | `WetzlerHeuleHunt2014` | Paper describes DRAT-trim; frozen audit/log give twelve zero exits and verification markers | Verified, source plus local record |
| CIT-09 | `EenSorensson2003` | MiniSat source and PySAT source identify MiniSat 2.2; replay log bounds its propagation-only role | Verified, source plus local record |
| CIT-10 | `WetzlerHeuleHunt2014` | Sections 2--3 define RUP and its place in clausal proof checking | Verified, paraphrase |
| CIT-11 | `Verhoeff2026` | Inspected v1 stops near length 16; accepted certificates cover length 18 | Verified, expressly bounded comparison |

The cited numerical values were checked exactly. No rounding, truncation, unit
mismatch, or contradictory value was found.

## Bibliographic coverage and consistency

All eight BibTeX entries were checked for authors, title, year, venue or
repository, pages where applicable, and DOI/arXiv identifier. No repair or key
change was needed. The bibliography naturally covers problem origin, closest
prior result, construction context, cardinality encoding, PySAT, MiniSat, and
clausal proof checking. It is not user-library-only.

Active-library row 49 (`Zeng2026GCD`) is directly cited once for the narrow SAT
proof-carrying comparison its SSRN abstract supports. None of the other 48
first-sheet entries naturally supports another existing claim without padding.
The selection is bound to registry SHA-256
`67477dfa5d2f3dfcb5a9123fd79975af80968b43058ff32c774143c2f26112d4`
and workbook SHA-256
`93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427`.
The installed hook-compatible selection validator passed with the exact
problem, attempt, and runner-issued launch UUID.

The bibliography checker found eight cited keys, eight entries, zero missing
or unused entries, and exact agreement with `main.aux`. Final LaTeX and BibTeX
logs contain no undefined citation/reference, missing database entry, repeated
entry, BibTeX warning, TeX error, or fatal diagnostic. This audit makes no
claim of worldwide priority or peer review of the note.
