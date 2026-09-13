# Search log

## NOVELTY_LOCK -- first pass (2026-08-29, Asia/Shanghai)

Frozen claims: C01--C08 in `claim_ledger.md`.  The lock concerns the precise
question whether the condition numbers of \(A\) and \(A+uv^T\) alone force
Algorithm 2 to eventually return a backward-stable finite iterate.  It does
not claim novelty for generic SM instability or for conditional iterative-
refinement theorems.

## Primary-source retrieval

- arXiv abstract/metadata: <https://arxiv.org/abs/2510.01696>.  Result: v1 only,
  submitted 2025-10-02; exact conjecture occurs in the abstract.
- arXiv PDF: <https://arxiv.org/pdf/2510.01696>.  Saved as
  `sources/2510.01696.pdf`, SHA-256
  `711c793c7b3ad604e8fb15ba845710b61feb2568142596a51a16c915c7f1723c`.
- arXiv source: <https://export.arxiv.org/e-print/2510.01696>.  Saved as
  `sources/2510.01696.tar`, SHA-256
  `0bf7fa5c4badfdace95e61d18df57e288f510f9b372d0fe177e6de19de04ae37`.
- arXiv DOI: <https://doi.org/10.48550/arXiv.2510.01696>.

## Search queries and bounded outcomes

Search date: 2026-08-29.  Queries were run as exact-title/identifier searches
and as mathematical phrase searches; absence means only absence from these
results on this date.

| Database/site | Query | Outcome relevant to this project |
|---|---|---|
| arXiv | `2510.01696`; exact title | Only v1 found; source conjecture and conditional Theorems 4.6--4.7 verified. |
| General web restricted to arXiv | `Sherman Morrison iterative refinement backward stable conjecture` | Source paper found; no later arXiv resolution found. |
| OUP Academic / IMAJNA | exact title | No publisher article page surfaced in search. |
| Crossref / DOI web search | exact title; author/title | No journal DOI surfaced; only the arXiv-issued DOI was located. |
| DBLP | `2510.01696` | CoRR record only, metadata updated 2025-11-08. |
| zbMATH web search | `Sherman-Morrison iterative refinement` | No resolving work surfaced. |
| OpenAlex and Semantic Scholar | title/arXiv identifier and citing-work lookup | Metadata frozen locally; OpenAlex reported zero citing works and Semantic Scholar reported one applied-paper citation, with no proof or counterexample to the conjecture. |
| Author academic site | exact title | Author reports August 2026 acceptance in an IMAJNA special issue; this is an author report, not a publisher record. |
| General exact phrase | `"SM-IR" "Sherman-Morrison" backward stable`; `"fixed-precision iterative refinement"` | No proof/counterexample to this exact conjecture surfaced. |

## Theorem frontier frozen before exactification

1. Known from the source: plain SM can be unstable; under explicit residual
   hypotheses one SM-IR correction is backward stable (Theorems 4.6--4.7).
2. Open in the source: eventual success based only on numerical
   nonsingularity/condition numbers.
3. Structural vulnerability not excluded in Algorithm 2: scale cancellation
   in the capacitance denominator is not controlled by either condition number.
4. Candidate new endpoint: exact binary64 dimension-one stagnation at a
   finite, non-backward-stable fixed point despite both exact condition numbers
   being one.  Novelty remained bounded by the searches above and was checked
   again after the proof was frozen, as recorded next.

## NOVELTY_LOCK -- second pass (2026-08-29, Asia/Shanghai)

This pass was performed after freezing the exact theorem, the all-precision
family, and the independent referee reconstruction.  The following exact or
near-exact queries were checked on the open web and, where indicated, with an
arXiv domain restriction:

| Query | Outcome |
|---|---|
| `"fixed-point counterexample" "Sherman-Morrison" iterative refinement` | No work resolving the source conjecture surfaced. |
| `"2^p+1" "Sherman-Morrison" iterative refinement` | No matching mathematical result surfaced. |
| `"condition-number-only" "Sherman-Morrison" iterative refinement` | No matching proof, counterexample, or correction surfaced. |
| `site:arxiv.org Sherman Morrison iterative refinement counterexample backward stability` | Returned the source paper and unrelated Sherman--Morrison or refinement papers; no later resolution was found. |
| exact title and `2510.01696` on arXiv/DataCite/Crossref/OpenAlex/Semantic Scholar | arXiv v1 remained the only primary manuscript record located; no journal DOI or resolving follow-up was found. |

The machine-readable responses used in this pass are preserved as
`datacite_2510.01696.json`, `openalex_2510.01696.json`,
`semanticscholar_2510.01696.json`,
`semanticscholar_citations_2510.01696.json`, and
`crossref_title_query.json`.  These bounded negative results support only the
phrase "we found no prior resolution in the named searches"; they are not a
proof of global novelty.  The author's reported August 2026 acceptance was
again treated as an author report because no publisher record was located.

## Release-refresh search after verifier hardening (2026-08-29)

The theorem itself did not change during certificate hardening, but the
novelty lock was refreshed immediately before rebuilding the release. Exact
queries for `"fixed-point counterexample"`, `"2^p+1"`, and
`"condition-number-only"` together with `Sherman-Morrison` and `iterative
refinement` again returned no resolving paper. An arXiv-domain exact-title
search returned arXiv:2510.01696v1 as the primary manuscript. OUP/IMAJNA,
Crossref/DOI, exact-title, and citation/counterexample queries produced the
arXiv/DBLP preprint record and nonauthoritative mirrors or reviews, but no
publisher article, later arXiv version, proof, correction, or counterexample
to the exact conjecture.

This refresh changes no novelty claim: the project states only that no prior
resolution was found in the named searches through the recorded date. It does
not assert exhaustive or absolute novelty.
