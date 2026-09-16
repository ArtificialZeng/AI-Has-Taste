# Citation and bibliography verification report

**Mode:** Search verification with local-primary-document replay  
**Release job:** `win-00070-p03-release-f068e3c4ff94`  
**Attempt / launch:** `2` / `b28c4bc0-33c6-4524-b952-68ebb591185b`  
**Verification date:** 2026-09-08  
**Result:** PASS

## Frozen extraction (pass 1)

The complete ordinary body-flow citation extraction was frozen before source
verification in `audit/citation-claim-ledger.json`.  It contains six distinct
claim/citation pairs at exact `manuscript/main.tex` line locations.  Their key
union is exactly

`hatcher2002, kozlov2023, kozlov2024, mamun2026, zeng2026whiskered`.

The same five keys are the complete set reported by the LaTeX source, BibTeX
database, and converged `.aux`.  There are no cite-like custom macros, hidden
conditionals, `\\nocite` uses, comment-only citations, or verbatim citations.

## Independent claim verification (pass 2)

| ID | Nearby claim and exact source locator | Status | Confidence |
|---|---|---|---|
| C01 | The anchored-space definition and collision convention match Mamun--Nalikka--Ramos, Definition 4.13 and Remark 4.14, local official arXiv PDF p. 26; they also match Kozlov, *Stirling complexes*, Definition 2.4. | Verified | exact/paraphrase |
| C02 | Kozlov's publisher record for *Stirling complexes*, Theorems 2.1 and 2.5, determines the tree homotopy type.  The 2024 publisher abstract and §§1, 3--4 of *Homology and Euler characteristic...* explicitly calculate generalized anchored homology on circle graphs. | Verified | paraphrase |
| C03 | Mamun--Nalikka--Ramos, Corollary 4.18(1)--(2), local official arXiv PDF pp. 27--28, gives finite generation and a uniform torsion-exponent divisor.  The following paragraph on p. 28 says the existence of integral torsion in anchored spaces was not known. | Verified | exact/paraphrase |
| C04 | Kozlov, Definition 2.4 makes the anchor set an arbitrary vertex subset, and Theorem 2.5 states a wedge of spheres of dimension `n-|S|`; Springer HTML lines 212--229 and the open article text were checked. | Verified | exact |
| C05 | Hatcher, *Algebraic Topology*, Theorem 3B.6 gives the split Kunneth short exact sequence for CW complexes over a PID.  With free factor homology the Tor terms vanish, exactly supporting the nearby use. | Verified | interpretation |
| C06 | The SSRN primary abstract for DOI `10.2139/ssrn.7385138` says there are 6,021 isomorphism classes and that exhaustive canonical enumeration and exact integer arithmetic produce certificates checked by a verifier reconstructing matrices from graph6 representatives. | Verified | paraphrase |

No numerical value is imported from an external citation into the main proof.
The finite counts 167 and 241 and the two Betti triples are internal exact-check
claims; they trace to the accepted mathematical dossier and the two publication
scripts rather than to bibliography entries.  In this release context the
independent checker again returned 167 and 241 cases with no failures, and the
two exact Smith runs again returned Betti triples $(1,9,27)$ and $(1,12,121)$
with every nonzero invariant factor equal to one.  The qualified literature sentence
at line 155 is consistent with the fresh primary-source searches and explicitly
disclaims exhaustive priority.

## Bibliographic-record audit

| Key | Current record checked against | Metadata result | Action |
|---|---|---|---|
| `hatcher2002` | Allen Hatcher's official Cornell book page and PDF | Author, title, publisher, year, and URL agree | retained |
| `kozlov2023` | Springer version of record, DOI `10.1007/s41468-022-00096-4` | Author, title, journal, volume, pages, year, DOI agree | retained |
| `kozlov2024` | Springer version of record, DOI `10.1007/s41468-024-00167-8` | Author, title, journal, volume, pages, year, DOI agree | retained |
| `mamun2026` | arXiv `2609.04554v1` record and frozen official PDF | Authors, title, date/year, identifier, version agree | retained |
| `zeng2026whiskered` | SSRN primary record and DOI `10.2139/ssrn.7385138` | Author, title, year, venue description, DOI agree | retained; final key intentionally differs from registry key |

There were no BibTeX replacements and no cite-key changes in this release pass.
The only manuscript-source repair was the scope-neutral replacement of two
unsupported LaTeX accent commands by the plain-text spelling `Cech`; it did not
change a claim, citation, source locator, or line number.
All five records are used, none is duplicated, and no official-verification
blocker remains.  The mandated audit ran locally because this release job
explicitly prohibited subagents.

## Coverage and necessity

The bibliography is not user-library-only.  Four natural non-library sources
occur in ordinary body flow: Mamun--Nalikka--Ramos supplies the problem origin
and closest cograph result; the two Kozlov papers supply the decisive tree
theorem and closest circle computation; Hatcher supplies the product-homology
method.  The one selected active-library record supplies a narrowly identified
exact-enumeration methodology comparison.  Each retained source has a direct
nearby use; no decorative citation was retained.

## Primary sources consulted

- <https://arxiv.org/abs/2609.04554v1> and the frozen official PDF
  `evidence/external/2609.04554.pdf`, pp. 26--28.
- <https://link.springer.com/article/10.1007/s41468-022-00096-4>, especially
  Definition 2.4 and Theorem 2.5.
- <https://link.springer.com/article/10.1007/s41468-024-00167-8>, abstract,
  Definition 1.1, and §§3--4.
- <https://pi.math.cornell.edu/~hatcher/AT/AT.pdf>, Theorem 3B.6.
- <https://doi.org/10.2139/ssrn.7385138>, SSRN abstract and suggested citation.

The academic-citation search templates (author/year/title, full title on primary
repositories, author/year/venue, and DOI or arXiv identifier) were replayed for
each record.  Only the primary records above were used for pass/fail decisions.
