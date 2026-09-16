# Verification Report

**Mode:** Search verification  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Generated:** 2026-09-09 (UTC)

| Metric | Count |
|---|---:|
| Total frozen citation claims | 6 |
| Verified | 6 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall Status:** PASS: all six frozen citation claims are verified.

## Release binding

Release job `win-00077-p01-release-1b135af2eacf`, citation attempt 1, launch
`af1e8df0-ec4b-44ea-80b3-4135d38265c2`; checked 2026-09-09 UTC.

## Two-stage procedure

Pass 1 read the complete canonical manuscript and froze its six substantive
claim/citation pairs in `audit/citation-claim-ledger.json` before source
verification (ledger SHA-256
`03ee5d322d44af0fc1edde5ab8dce90764a0d6c32db454442800b2e017d707d8`).
The union of ledger keys is exactly the ordinary body-flow citation set:
`AxenovichEtAl2019`, `BaldacchinoCaroMifsud2026`, and
`Zeng2026SmallRamsey`.

Pass 2 independently ran the applicable author/year/title, exact-title,
venue, DOI, and arXiv-identifier searches for each frozen source, then
inspected the primary publication record and exact supporting passage. The
user prohibited agent delegation for this bounded worker, so the per-key
checks were performed serially in this fresh release context. Machine-readable
locators and decisions are recorded in
`audit/citation-source-verification.json`.

## Claim verification

| Claim | Key | Primary passage | Result |
|---|---|---|---|
| CIT-01 | `AxenovichEtAl2019` | Official Electronic Journal of Combinatorics article page, abstract: planar unavoidable means that some planar graph is a Ramsey graph for the target. | Verified exactly. |
| CIT-02 | `BaldacchinoCaroMifsud2026` | arXiv v1, Definition 1 (PDF p. 2) and the maximal-planar specialization at the start of Section 4 (p. 12): one threshold must work for every sufficiently large class member. | Verified exactly. |
| CIT-03 | `Zeng2026SmallRamsey` | Official Preprints.org v1, abstract and Theorem 1.1; Section 2 states that embeddings are induced and order preserving. | Verified exactly. |
| CIT-04 | `BaldacchinoCaroMifsud2026` | arXiv v1, Theorem 12 (PDF pp. 17--20): the diagonal fork pair is unavoidable in maximal planar graphs and its value is 9. | Verified exactly, including the number. |
| CIT-05 | `BaldacchinoCaroMifsud2026` | arXiv v1, Problem 2 (PDF p. 21): determine the disconnected diagonal unavoidable graphs in the maximal-planar class. | Verified exactly. |
| CIT-06 | `BaldacchinoCaroMifsud2026` | Complete v1 full text, especially notation (p. 4), Theorem 12, and Problem 2: the fork-plus-one-disjoint-edge target is not separately stated. | Verified within the manuscript's explicit version-bounded scope. |

All three cited works exist. Authors, titles, year/version, venue, DOI/arXiv
identifier, and nearby-claim support agree with `manuscript/references.bib`.
No BibTeX replacement or citation-key change was needed, and no retained
source is unverified. The Zeng item is explicitly a non-peer-reviewed preprint
and is used only for a precise distinction between Ramsey notions.

## Coverage, relevance, and consistency

The bibliography is not user-library-only. Axenovich et al. is the natural
primary source for planar Ramsey unavoidability. Baldacchino--Caro--Mifsud is
the problem-origin source, defines the stronger eventual notion, supplies the
closest connected-fork theorem, and states the broader disconnected problem.
Zeng is the sole genuinely relevant active-library item: it supports the
narrow warning that small Ramsey degree for induced order-preserving
embeddings is not the ordinary subgraph-host parameter used in this paper.
The other 48 active-library records concern different problems and would be
decorative.

The selected library item is cited directly in ordinary body flow at
`manuscript/main.tex` lines 44--46. Its selection is bound to the active
49-record registry and this exact attempt and launch in
`audit/user-bibliography-selection.json`; the hook-compatible selection
validator passed. Two natural non-library sources also occur in ordinary body
flow. The planar edge bound used in the proof is a standard elementary fact,
and the paper gives the complete argument needed from it; the labelled checks
are project-specific sanity checks, not an imported computational theorem.

The read-only BibTeX checker found three cited keys, three bibliography
entries, no missing or unused entry, and exact agreement with the final AUX.
The converged `main.log` and `main.blg` contain no undefined citation or
reference, missing database entry, repeated entry, BibTeX warning, LaTeX
error, or fatal diagnostic. The authored scope matches the accepted
mathematical audit: it resolves only the stated fork-plus-edge target and
makes no exhaustive priority claim.

## Primary records inspected

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i4p9>
- <https://arxiv.org/abs/2609.05268v1> and the locally hash-bound v1 PDF
  `evidence/external/2609.05268.pdf`
- <https://doi.org/10.20944/preprints202608.2162.v1> and
  <https://www.preprints.org/manuscript/202608.2162>

Verdict: **accept**. All frozen citation claims are supported, all retained
citations are needed for nearby claims, and bibliography coverage is complete
for the manuscript's actual external dependencies.
