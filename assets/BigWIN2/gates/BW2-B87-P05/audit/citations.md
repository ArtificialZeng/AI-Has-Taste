# Citation and bibliography audit

Release job: `win-00087-p05-release-62ff0861644e`  
Citation attempt: 1  
Launch ID: `f04441b6-0a74-445b-8ac4-7b8858c583df`  
Search and verification date (UTC): 2026-09-11  
Mode: search verification followed by a LaTeX/BibTeX consistency audit

## Two-stage protocol

Pass 1 read the complete canonical manuscript and bibliography and froze the
claim/citation pairs before assigning verification conclusions.  The final
13-claim ledger is `audit/citation-claim-ledger.json`; the union of its six
citation keys is exactly the ordinary body-flow citation set.  Pass 2 checked
those frozen claims sequentially against primary text and authoritative
publication records.  The user expressly prohibited sub-agents, so this worker
performed every per-reference check directly.

## Claim-level findings

| Claims | Citation key | Status | Primary evidence and exact locator |
|---|---|---|---|
| C01--C02 | `GouldenJackson1979` | Verified (exact metadata; specialized support) | Official Wiley record at `https://doi.org/10.1112/jlms/s2-20.3.567` and author-hosted PDF, abstract and Introduction on PDF p. 1: clusters are linearly ordered collections of overlapping distinguished sequences and organize their generating functions. |
| C03--C04 | `ElizaldeNoy2012` | Verified (exact) | Official ScienceDirect record at `https://doi.org/10.1016/j.aam.2012.08.003` and author-hosted article, abstract and Section 2: overlap constraints yield cluster posets whose linear extensions are enumerated. |
| C05--C06 | `MendesRemmel2006` | Verified (exact) | Official ScienceDirect article `https://www.sciencedirect.com/science/article/pii/S019688580600056X`, abstract: symmetric-function combinatorics is used for consecutive-pattern occurrence generating functions in permutations and words. |
| C07--C08 | `SavageWilf2006` | Verified (exact metadata; paraphrase support) | Official arXiv record `https://arxiv.org/abs/math/0504310` and author-hosted PDF, Introduction and main multiset result: fixed three-letter classical-pattern avoidance is symmetric in the multiplicities. |
| C09--C11 | `ChenFangKitaev2026` | Verified (exact) | Official versioned PDF `https://arxiv.org/pdf/2602.13566v2`, definitions on printed pp. 3--5, Proposition 4.12 and Remark 4.13 on p. 12, and Conjecture 6.1 on p. 17.  The v2 title, authors, date, identifier, and DOI match the bibliography. |
| C12--C13 | `Zeng2026Bezout` | Verified (exact metadata; paraphrase support) | Official Preprints.org v1 record `https://doi.org/10.20944/preprints202608.2160.v1`, abstract and Section 5: coefficient recovery is compared with multipoint evaluation, and the root-polynomial coefficients are elementary symmetric functions up to signs.  This also verifies active user-library row 14 and the exact nearby sentence. |

All 13 frozen claims are supported without numerical mismatch, contradictory
hypotheses, or omitted qualification.  No BibTeX entry or citation key required
replacement.

## Coverage and bibliography integrity

The bibliography is not user-library-only.  Five natural non-library primary
sources cover the problem origin and closest verified source, the cluster
method, overlap posets and linear extensions, symmetric-function occurrence
enumeration, and earlier multiset-pattern symmetry.  The one selected library
paper is the only active first-sheet record specifically combining coefficient
recovery with elementary symmetric functions; it supports a narrowly worded
comparison and no theorem from it is imported.  A second library citation would
be padding.

All six retained entries have an ordinary body-flow `\cite{...}` and a supported
nearby claim.  No citation is supplied by `\nocite`, a comment, an inert macro,
verbatim text, or a conditional.  The bibliography checker reports six cited
keys, six BibTeX entries, no missing or unused entry, and exact agreement with
the converged AUX set.  The final log and BLG contain no undefined citation or
reference, missing database entry, repeated entry, BibTeX warning, or TeX fatal
error.  The hook-compatible user-library validator passed after the manuscript's
composite hyperlink colors were replaced with its visibility-safe standard blue;
that release-only edit changed no prose, citation, bibliography, or mathematics.

A fresh broad query found a third-party page alleging a September 2026 Zenodo
work titled *Stable Consecutive Patterns and Chain Clusters*.  The available web
index exposed neither an official Zenodo/DataCite record nor its primary text,
and a local WSL request could not connect, so the lead was not treated as verified
literature or cited.  Before recording that limitation,
`literature/crossref-*.json` and `literature/crossref-*.md` were enumerated; no
captures exist.  Since this manuscript expressly makes no priority claim, the
unverified lead does not supply or defeat a retained claim, but it should be
rechecked before external submission.  Overall citation status: **PASS**
(13/13 frozen claims verified; 0 failed).
