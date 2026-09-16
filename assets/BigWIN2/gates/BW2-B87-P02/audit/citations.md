# Citation and bibliography audit

Release job: `win-00087-p02-release-03572e9b7dea`  
Citation attempt: 1  
Launch ID: `f5e6cf6e-c141-4ad8-9794-baf600c4170a`  
Search and verification date (UTC): 2026-09-11  
Mode: search verification followed by a LaTeX/BibTeX consistency audit

## Two-stage protocol

Pass 1 read the complete canonical manuscript and bibliography and froze the
claim/citation pairs before assigning verification conclusions.  The final
15-claim ledger is `audit/citation-claim-ledger.json`; the union of its six
citation keys is exactly the ordinary body-flow citation set.  Pass 2 then
checked those frozen claims sequentially against primary text and authoritative
publication records.  The user expressly prohibited sub-agents, so this worker
performed the per-reference checks directly.

## Claim-level findings

| Claims | Citation key | Status | Primary evidence and exact locator |
|---|---|---|---|
| C01--C02 | `DiasDaSilvaHamidoune1994` | Verified (exact metadata; paraphrase support) | Official Wiley record at `https://doi.org/10.1112/blms/26.2.140`, abstract and citation metadata.  The abstract states the prime-field two-subset-sum bound and that it answers the Erdos--Heilbronn conjecture. |
| C03--C05 | `AlonNathansonRuzsa1996` | Verified (exact specialization) | Author-hosted primary PDF `https://web.math.princeton.edu/~nalon/PDFS/anrf3.pdf`, Proposition 1.2 and Theorem 3.2 on PDF pp. 2 and 6--7; the two-set, unequal-size specialization is the displayed bound.  Concluding remarks item 4 on PDF p. 12 poses the inverse equality problem.  The official ScienceDirect record supplies matching metadata and DOI. |
| C06--C07 | `Karolyi2005` | Verified (exact) | Author-hosted primary PDF `https://karolyigy.web.elte.hu/preprints/inverse4.pdf`, Theorem 7 on PDF p. 4, gives precisely the prime-field hypotheses and equality classification used in the manuscript.  The official ScienceDirect metadata match. |
| C08--C09, C13 | `LiuQian2026` | Verified (exact; scope comparison) | Official ScienceDirect article `https://www.sciencedirect.com/science/article/pii/S107157972600078X`, abstract and introduction: the inverse problem is solved when at least one set is an arithmetic progression.  Author, title, volume, article number, year, and DOI match the bibliography. |
| C10--C13 | `LiLiang2026` | Verified (exact; scope comparison) | Official arXiv v1 record `https://arxiv.org/abs/2609.10148`, abstract, Example 2.1 on PDF pp. 2--3, and Theorem 3.1: the counterexample is at the boundary `|A|+|B|=p`, while the refined theorem assumes `|A|+|B|<=p-1`. |
| C14--C15 | `Zeng2026Rainbow` | Verified (exact metadata; paraphrase support) | Official SSRN record and primary PDF at `https://doi.org/10.2139/ssrn.7387259`, abstract on PDF p. 1: pairwise-distinct edge sums on a finite Abelian group and coset/fiber construction principles.  This also verifies active user-library row 36 and the exact nearby comparison. |

All 15 frozen claims are supported without numerical mismatch, contradictory
hypotheses, or omitted qualification.  The scope comparison is deliberately not
a priority claim.  A targeted search for the boundary, two-missing-sum
classification returned the Liu--Qian and Li--Liang records as the closest
results and no exact equivalent; this bounded search is not asserted to prove
novelty.

## Coverage and bibliography integrity

The bibliography is not user-library-only.  Five natural non-library primary
sources cover the symmetric problem, the asymmetric sharp bound and inverse
problem origin, the symmetric inverse theorem, the closest arithmetic-progression
classification, and the boundary counterexample/refined range.  The one selected
library paper is the only one among the 49 first-sheet records naturally adjacent
to sums and structure in finite Abelian groups; it supports a narrowly worded
comparison and no mathematical result is imported from it.  A second library
citation would be padding.

All six retained entries have an ordinary body-flow `\cite{...}` and a supported
nearby claim.  No citation is supplied by `\nocite`, a comment, an inert macro,
verbatim text, or a conditional.  The bibliography checker reports six cited
keys, six BibTeX entries, no missing or unused entry, and exact agreement with
the converged AUX set.  The final log and BLG contain no undefined citation or
reference, missing database entry, repeated entry, BibTeX warning, or TeX fatal
error.  No key or BibTeX replacement was required.

Before treating any live source as unavailable, `literature/crossref-*.json` and
`literature/crossref-*.md` were enumerated; neither the directory nor matching
captures existed.  Fresh primary publisher, author, arXiv, and SSRN records
supplied the evidence.  Overall status: **PASS** (15/15 claims verified; 0
failed).
