# Claim ledger

Claim list frozen before the substantive finite search. `Exact` means a
statement copied from a primary source; `paraphrase` and `inference` are marked
explicitly. Search cutoff for Gate 1 is 2026-08-29 (Asia/Shanghai).

| ID | Type | Claim | Status | Primary evidence and location | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C01 | exact metadata | The source paper is *K-Knuth Equivalence for Increasing Tableaux* by Christian Gaetz, Michelle Mastrianni, Rebecca Patrias, Hailee Peck, Colleen Robichaux, David Schwein, and Ka Yu Tam. | verified | EJC article page; published PDF title page | 100% | Fixes attribution. |
| C02 | exact metadata | The formal journal record is *Electronic Journal of Combinatorics* 23(1) (2016), P1.40, DOI `10.37236/4805`, published 2016-03-04. | verified | EJC article page and Crossref API record | 100% | Corrects/locks bibliography. |
| C03 | exact | The four word relations are \(xzy\equiv zxy\), \(yxz\equiv yzx\) for \(x<y<z\), \(x\equiv xx\), and \(xyx\equiv yxy\). | verified | Published paper, Section 2.3 | 100% | Defines the computed relation. |
| C04 | exact | Tableau equivalence is equivalence of row words, with rows read left-to-right from bottom to top. | verified | Published paper, Section 2.4 | 100% | Fixes tableau encoding. |
| C05 | exact | Conjecture 7.6 states interval completeness of the shape set of every K-Knuth class of straight tableaux. | verified | Published paper, Section 7.3, Conjecture 7.6 | 100% | Exact target. |
| C06 | exact author report plus reproduction | The authors report that Conjecture 7.6 was verified for K-Knuth classes on \([n]\) for \(n\leq7\); the initial-tableau, class, and URT counts through seven are independently reproduced here. | verified and reproduced | Published paper, sentence immediately after Conjecture 7.6; `results/verification_n0_n8.log` | 100% | Makes \(n=8\) the next finite endpoint in that paper and locks the baseline. |
| C07 | inference | Order-preserving standardization reduces every alphabet of cardinality \(n\) to initial tableaux on \([n]\). | verified | Published paper, Definitions 2.4 and 2.6 plus direct inspection of the relations | 100% | Clarifies “alphabet size 8.” |
| C08 | exact | Algorithm 1 computes all K-Knuth classes in the finite set of tableaux on \([n]\), and Theorem 3.1 proves its correctness. | verified | Published paper, Section 3, Algorithm 1 and Theorem 3.1 | 100% | Supplies the certification algorithm. |
| C09 | exact public-code record | Ka Yu Tam's Python 2 implementation of the classification algorithm is publicly linked by OEIS A261601. | verified | OEIS A261601 supporting file `a261601.py.txt`; local SHA-256 `6446744d803c8e06e7b5a7c0ae63b6e3f942c33a42cb14d0afdd359636e2c4ed` | 100% | Baseline implementation is available but is not trusted as our verifier. |
| C10 | exact arXiv metadata | The latest arXiv record is `1409.6659v2`, submitted 2014-09-23 and last revised 2015-08-23. | verified | arXiv abstract submission history and export API | 100% | A 2026 date rendered by experimental HTML is not a v3 revision. |
| C11 | bounded negative novelty claim | No public proof, counterexample, or \(n=8\) certification of Conjecture 7.6 was found in two recorded search passes or in the searchable full text of 14 arXiv citing works. | not found within recorded scope | Search log; Crossref, OpenAlex, Semantic Scholar; 14 downloaded citing preprints; frozen-result numerical and phrase queries | 90% | Allows release of a bounded novelty claim while forbidding an unbounded “never solved” claim. |
| C12 | exact nearby invariant | Equivalent initial tableaux have the same outer hook; first-row and first-column lengths are therefore fixed within a class. | verified | Published paper, Proposition 2.43 | 100% | Reduces shape variation to the interior. |

## Gate 1 decision: `NOVELTY_LOCK`

**PASS, bounded to the two search passes logged on 2026-08-29.** The source, DOI,
journal publication, exact conjecture, latest arXiv version, known \(n\leq7\)
author report, citation graph, public original code, and frozen-result numerical
fingerprints were checked. The
frontier “\(n=8\) is the first endpoint not verified in the source paper” is
correct. The stronger claim “nobody has solved it since” is intentionally
limited to C11's recorded databases and full-text corpus. The mandatory second
novelty pass found no conflicting result within that scope.
