# Citation and bibliography audit

## Scope and method

Release job `win-00087-p01-release-38ca90bfe4c5`, citation attempt 1,
launch `485d119b-d989-4aa7-b7b1-aedaf66592ef`.  Verification was performed
on the UTC date 2026-09-11 against the canonical
`manuscript/main.tex` and `manuscript/references.bib`, bound to manuscript
snapshot digest
`aa8bc8a4188203e53f8d6df1ad6e9190eae01dd1b8a32e2919d91fd1171312e9`
and PDF digest
`5db8179a7b52d8e5f1c0c8da7a2eddd42ebcd39aa6a264560e5dd20d44cb14ca`.

The audit used two non-interleaved passes.  Pass 1 froze all citation-bearing
claim units in `audit/citation-claim-ledger.json`; its five-key union is
exactly the ordinary body-flow citation set.  Pass 2 replayed those fixed
claims against primary publisher records and original source text.  For each
academic citation I ran author/year/title, exact-title, author/venue, DOI, and
where applicable arXiv-identifier searches.  Detailed locators and support
decisions are preserved in `audit/citation-source-verification.json`.

## Claim-to-source findings

| Claim | Key | Primary record and inspected location | Decision |
|---|---|---|---|
| C01 | `Erdos1963` | DOI `10.2307/3613396`; original article pp. 220--221, opening formulation and definition of the classical parameter | Verified (paraphrase) |
| C02 | `SzekeresSzekeres1965` | DOI `10.2307/3612854`; Cambridge record/extract for pp. 290--293, cross-checked against Jeffries (2026), Section 1 and Theorem 1.1 | Verified (paraphrase) |
| C03 | `BorowieckiEtAl2003` | DOI `10.1017/S0963548303005674`; publisher abstract, pp. 359--364 | Verified (exact) |
| C04 | `Jeffries2026` | arXiv:2604.08790v1, Definitions 2.1--2.2, PDF p. 4 | Verified (exact) |
| C05 | `Jeffries2026` | Proposition 2.3, Theorem 2.2, Figure 7 and text, and Conclusion, PDF pp. 5, 6, 8, 10 | Verified (exact) |
| C06 | `Zeng2026Tuza` | DOI `10.20944/preprints202608.1304.v1`; v1 Abstract and Section 1 | Verified (exact) |

The Szekeres publisher page exposes the original paper's extract rather than
its full body.  I therefore did not treat a remembered formula as a quotation:
the modest nearby claim that the lower bound was sharpened was cross-checked
against accessible original text in the present problem's primary source,
Jeffries (2026), which states the attribution and formula.  No numerical claim
was rounded or inferred.

## Bibliographic identity audit

All five entries match their authoritative records in author identity, title,
year, venue or repository, pages/version, and DOI where applicable.  No key or
BibTeX correction was necessary.

| Key | Record | Authority | Action |
|---|---|---|---|
| `Erdos1963` | P. Erdős, *On a Problem in Graph Theory*, 1963, pp. 220--223 | Cambridge/DOI `10.2307/3613396` and the Erdős archive scan | Retained |
| `SzekeresSzekeres1965` | E. Szekeres and G. Szekeres, *On a Problem of Schütte and Erdős*, 1965, pp. 290--293 | Cambridge/DOI `10.2307/3612854` | Retained |
| `BorowieckiEtAl2003` | Four authors, *Schütte's Tournament Problem and Intersecting Families of Sets*, CPC 12(4), 359--364 | Cambridge/DOI `10.1017/S0963548303005674` | Retained |
| `Jeffries2026` | Joel Jeffries, *Schütte's Property for Sets of Tournaments and an Application to Dice Games* | arXiv:2604.08790v1 | Retained |
| `Zeng2026Tuza` | Zijian Zeng, *Tuza's Conjecture for Split Graphs with an Eight-Vertex Clique Part and Two Neighborhood Types* | Preprints.org v1/DOI `10.20944/preprints202608.1304.v1` | Retained |

## Coverage and relevance

The bibliography is not library-only.  Four natural non-library sources occur
in ordinary body flow: the classical origin, its closest sharper classical
bound, the intersecting-family bipartite variation, and Jeffries' primary
multi-tournament source.  The one selected user-library record is the only one
of the active 49 first-sheet entries directly concerning both triangle
covering/packing and split graphs; it supports only the explicit comparison
sentence and is not used as evidence for the theorem.  A second library item
would not support an actual claim and would be padding.

The proof itself invokes no external nontrivial theorem: the two-uniform
classification, edge count, and block construction are all proved in full.
Consequently no method citation is missing from the proof.  Every retained
reference has a direct nearby role, and no decorative or uncited BibTeX entry
remains.

## Mechanical consistency

The hook-compatible active-text parser extracts exactly
`BorowieckiEtAl2003`, `Erdos1963`, `Jeffries2026`,
`SzekeresSzekeres1965`, and `Zeng2026Tuza`.  The BibTeX checker reports five
cited keys, five entries, no missing or unused entry, and exact agreement with
the final `.aux`.  The converged `.log` and `.blg` contain no undefined
citation/reference, missing database entry, duplicate entry, BibTeX warning,
LaTeX error, or fatal diagnostic.  The user-library selection passed the
installed hook-compatible validator with the exact attempt and launch
identity.

**Verdict: accept.**  Citation support, bibliographic identity, coverage, and
mechanical consistency all pass at the frozen manuscript/PDF snapshot.
