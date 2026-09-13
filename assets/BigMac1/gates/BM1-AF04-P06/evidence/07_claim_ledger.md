# Claim ledger

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | Lam--Leung's journal paper has metadata J. Algebra 224(1) (2000), 91--109, DOI 10.1006/jabr.1999.8089. | exact, verified | Elsevier DOI landing page; Crossref | article metadata | high | Supplies the original published structural source. |
| C02 | For primes 3, 5, 7, Lam--Leung construct the asymmetric weight-14 example and prove the corresponding minimum/uniqueness statement. | exact, verified from primary text and source audit | Lam--Leung, arXiv:math/9511209; journal DOI | Example 2.5, Theorem 4.8, Theorem 6.5 | high | Explains the first asymmetric fixed-conductor orbit, but not weight 20. |
| C03 | Christie--Dykema--Klep prove the general type classification only through weight 16. | exact, verified | arXiv:2008.11268v2 | abstract; Theorem 3.3 | high | The formal literature frontier is lower than the prompt's computational frontier. |
| C04 | The current revision's data for weights 17--21 are conjectural and rely on a preliminary implementation with floating-point vanishing tests. | exact, verified | arXiv:2008.11268v2 | Remarks 4.1--4.2, Section 4.2, Appendix A | high | Those tables are cross-checks, not certificates for this task. |
| C05 | arXiv:2008.11268 was submitted 2020-08-25 and last revised as v2 on 2025-12-16; no journal DOI/version of record was located. | exact metadata plus bounded negative search | arXiv/DataCite; Crossref title query; author publication page | submission history and database query dated 2026-08-30 | high for dates; medium for absence | Cite it as a preprint, not a journal theorem. |
| C06 | The authors' public code repository remains at the 2020 code described by the paper and does not implement this fixed-conductor affine enumeration. | verified repository inspection | GitHub `lchristie/Sums-of-Roots-of-Unity` | README and files at public default branch; checked 2026-08-30 | high | Existing code is related prior art, not a weight-20 certificate. |
| C07 | TheoremDB's 2026-07-28 packet records seven affine-Galois orbits through weight 19 for distinct 105th roots, with a deterministic SymPy/Z3 replay. | exact, externally reported and locally to be reproduced | TheoremDB P2744/R526 | computation record and inline source | high after local replay; pending at lock time | This is the true computational baseline in the prompt. |
| C08 | The same TheoremDB packet labels weight 20 as the next experiment and does not report an answer. | exact, verified | TheoremDB P2744/R528 | status `next experiment`, scope weight 20 | high | Confirms the requested endpoint is not already solved in the supplied source. |
| C09 | OpenAlex indexed two works citing arXiv:2008.11268 as of the search date; neither claims a fixed-conductor-105 affine classification through weight 20. | database report plus primary-title/abstract inspection | OpenAlex citing-works query; cited works | API query dated 2026-08-30 | medium-high | No later resolution was found in the indexed citation trail. |
| C10 | Searches for `105th roots`, `conductor 105`, `distinct`, `minimal vanishing`, `weight 20`, and affine/Galois equivalence found no primary paper or public code resolving this exact endpoint. | bounded negative search, not proof of absence | arXiv, Crossref, OpenAlex, zbMATH/MathSciNet web search, GitHub, TheoremDB | queries recorded in `search_log.md` | medium | Novelty wording must remain dated and database-bounded. |
| C11 | Sivek characterizes which cardinalities occur for *some* vanishing subset of distinct \(n\)-th roots; this does not classify inclusion-minimal subsets or affine orbits. | exact, verified | Integers 10 (2010), 365--368; DOI 10.1515/integ.2010.031 | Theorem 2 and publisher metadata | high | Weight 20 existence at conductor 105 is compatible prior art, not the requested minimal-orbit result. |
| C12 | A result-aware second search found neither exact weight-20 representative, no later fixed-conductor-105 classification, and no updated public implementation; TheoremDB still states that weight 20 is open. | bounded negative search, not proof of absence | exact-string web search; arXiv; Crossref; OpenAlex; J-GLOBAL/zbMATH-linked metadata; GitHub API; TheoremDB | queries and API results dated 2026-08-30 | medium-high | Supports the dated novelty claim for the two-orbit certified result. |

## NOVELTY_LOCK (2026-08-30, Asia/Shanghai)

The locked endpoint is the complete affine-Galois classification at *exactly*
weight 20 for distinct 105th roots.  The prompt's `weight <= 19` boundary is a
reproduced TheoremDB computational artifact, not a peer-reviewed theorem.  The
strongest checked primary mathematical source proves general types through
weight 16 and explicitly labels its implemented extension through 21
conjectural.  No checked primary source, later citation, professional metadata
record, or public repository supplies the requested fixed-conductor answer.

This is a dated, finite search conclusion, not a universal proof of novelty.
Gate 1 is locked for discovery; a second pass is mandatory before release.

## RELEASE_NOVELTY_PASS (2026-08-30, after certification)

The second pass used both complete exponent lists as exact-string fingerprints,
repeated the conductor/weight searches, refreshed Crossref and OpenAlex, checked
the current arXiv/preprint metadata, and queried the public repository head.
Neither fingerprint was found. OpenAlex still reports two citing works for the
Christie--Dykema--Klep preprint, neither about this endpoint; Crossref still
returns no journal version; GitHub still reports commit
`b0563b270dc89ed7ca9e195535a107d5a81cc6dc` (2020-07-28) as the repository head;
and TheoremDB still labels weight 20 open. Within those dated searches, the two
certified affine orbits appear new. This remains a bounded novelty statement,
not a logical proof that no unindexed or private work exists.
