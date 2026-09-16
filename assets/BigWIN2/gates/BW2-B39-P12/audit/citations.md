# Citation and bibliography audit

Verdict: **accept**. The audit was performed serially because this release job
explicitly prohibited sub-agents. The six-claim extraction ledger was fixed
before verification. All six claims pass; no numerical error, contradiction,
misleading attribution, or unsupported strengthening was found.

| Key | Current / official title | Primary source and claim location | Action |
|---|---|---|---|
| `Muller2026` | *On Euler's magic matrices of sizes 3 and 8* | arXiv:2504.16260v2, Definition 1.1, Lemma 2.1, Proposition 2.2, Theorem 4.1; IMPAN record for *Acta Arith.* 222 (2026), 71--82 and DOI 10.4064/aa250422-2-8 | verified; retained |
| `Kominers2026` | *A proper Euler magic matrix of order 5* | arXiv:2607.19416v1, Definition 1.1, Lemma 2.1, Theorem 3.1, Corollary 3.2, Section 5 | verified; retained |
| `Mehat2026` | *A proper Euler magic matrix of order 6* | arXiv:2608.15318v1, abstract and Theorem 1.2 | verified; retained |
| `LiebeckOsborne1991` | *The generation of all rational orthogonal matrices* | *American Mathematical Monthly* 98 (1991), 131--133, construction on pp. 131--132; DOI 10.2307/2323943 | verified; retained |
| `Zeng2026Zenodo22242517` | *A Rational Rank-(2, 2) Hadamard Factorization of a Proposed 4 x 4 Real Counterexample* | DataCite HTTP-200 capture for DOI 10.5281/zenodo.22242517; checksum-bound primary PDF, Theorem 2.1 and Section 4, p. 3 | verified; retained |

The five entries form a normal claim-driven bibliography. The first four are
needed for the definition, closest constructions/open-status comparison and
Cayley method. The fifth is the only supervisor-library item and supports only
the explicitly qualified exact-certificate/deterministic-verifier comparison;
the manuscript expressly disclaims relevance to the Euler theorem itself.
There is no citation padding. No key changed and no BibTeX entry required a
metadata correction.

The mechanical checker found five cited keys and five canonical BibTeX
entries, no missing or unused keys, and exact agreement with `main.aux`.
The final log scan found no undefined citation/reference, missing database
entry, repeated entry, BibTeX warning, or LaTeX error.
