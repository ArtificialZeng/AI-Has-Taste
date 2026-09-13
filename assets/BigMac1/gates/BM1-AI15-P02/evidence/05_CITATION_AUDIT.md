# Verification Report

**Mode:** Search verification for external claims; exact-artifact verification
for the manuscript's new mathematics  
**Document:** `paper/main.tex`  
**Generated:** 2026-08-29 (Asia/Shanghai)  
**Frozen extraction:** `audit/CITATION_CLAIMS.md`

## Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 20 |
| Verified | 20 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status: PASS.** Pass 2 did not add, remove, or reinterpret claims
from the frozen Pass 1 list.

## Verified external claims

| ID | Claim result | Source and exact support | Confidence |
|---|---|---|---|
| CC01 | Verified | OEIS A321614 states the `4 x 2n`, `2n`-king, rectangle-symmetry orbit definition; the manuscript separately and correctly makes the four-operation `n=2` convention explicit. | paraphrase |
| CC02 | Verified | OEIS A321614 labels both the displayed g.f. and recurrence “Conjectures from Colin Barker, Dec 22 2018.” | exact |
| CC03 | Verified | The OEIS entry and b-file list indices `0..21`, exactly 22 values. | exact |
| CC04 | Verified | Wilf's publisher page and article abstract state the `2m x 2n` maximum `mn`, the `2 x 2` cell reason, and the general fixed-`m` asymptotic theorem. | paraphrase |
| CC05 | Verified | OEIS A061593 defines exactly the labeled number of ways to place `2n` nonattacking kings on `4 x 2n` and gives the same identity-branch terms/g.f. | exact |
| CC06 | Verified | The SciNet finding states reproduction of all 22 terms, exact verification through `n=5000`, exact BM order ten on that range, and explicitly says this is not an all-`n` proof. | paraphrase |

## Verified new mathematical and reproducibility claims

| ID | Claim result | Exact primary evidence | Confidence |
|---|---|---|---|
| CC07 | Verified | The disjoint `2 x 2` clique bound and explicit placement in `problem/formal_statement.md`; independently reconstructed by builder and referee. | exact |
| CC08 | Verified | Both 12-state encodings are exhaustively regenerated; referee Section 8 gives the explicit isomorphism and confirms all 144 transfer entries. | exact |
| CC09 | Verified | Builder and root verifiers reconstruct the three involutions, check involution/permutation properties and all transfer invariances. | exact |
| CC10 | Verified | The two horizontal states and induced `2 x 2` matrix are reconstructed; the resulting branch is `1,2,3,...`. | exact |
| CC11 | Verified | Middle-edge and center-state vectors are rebuilt from the involutions; their sums and both parity formulas are checked independently. | exact |
| CC12 | Verified | `agents/builder/verify_certificate.py` checks every integer coefficient of `Z(y)(I-yT)=D0(y)1^T` after reconstructing `T`. | exact |
| CC13 | Verified | Builder verifier derives all four rational functions from the resolvent identity; root verifier generates the same branches from a separate 68-dimensional representation. | exact |
| CC14 | Verified | Both verifiers cross-multiply the Burnside average and Barker numerator/denominator over the integers. | exact |
| CC15 | Verified | The manuscript remainders were recomputed independently; builder runs exact Euclid, while the root certificate checks the serialized rational Bezout identity. | exact |
| CC16 | Verified | Coefficient expansion gives the ten coefficients; root verifier checks 68 observable annihilation moments, and Cayley–Hamilton proves all later moments. Coprimality gives minimality. | exact |
| CC17 | Verified | Builder and breaker independently enumerate all `C(16,4)=1820` four-square subsets, obtaining the eight fixed counts and orbit totals 23/14. | exact |
| CC18 | Verified | With delta `-9` at index 2, exact coefficient propagation gives recurrence residuals `-1080,1134,-243` (equivalently RHS-minus-actual `1080,-1134,243`) at indices 10–12. | exact |
| CC19 | Verified | Both exact verifiers were executed successfully; their compact PASS records and SHA-256 hashes are recorded in `audit/PROOF_AUDIT.md`. | exact |
| CC20 | Verified | Source inspection shows standard-library imports only, `random_seed: null`, no floating decisive path, and no theorem-prover files or claims. Builder, breaker, and referee reports are present and independent. | exact |

## Mandatory search record

Academic-citation templates were all run for Wilf: author/year/title prefix;
full title on arXiv/Semantic Scholar; author/year/journal; and DOI. The
authoritative publisher record was found and preferred. Direct record and
exact-title searches were run for both OEIS entries and the SciNet finding.
The Gate 6 novelty queries (`A321614 proof recurrence`, `A321614 order-10
proof`, exact expanded denominator, and arXiv exact-topic search) found no
prior all-`n` proof.

## Sources

| ID | Citation | Type | URL | Used for |
|---|---|---|---|---|
| S1 | OEIS A321614 | official database entry/data | https://oeis.org/A321614 | CC01–CC03 |
| S2 | OEIS A061593 | official database entry/data | https://oeis.org/A061593 | CC05 |
| S3 | Herbert S. Wilf, *The Problem of the Kings*, EJC 2 (1995), R3, DOI 10.37236/1197 | original peer-reviewed paper/publisher record | https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r3 | CC04, CC07 |
| S4 | SciNet finding 4d13cbaa | original computational report/artifact record | https://api.scinet.pub/f/4d13cbaa-b64a-4167-b7c4-8e435279c9d0 | CC06 |
| S5 | Builder/root/breaker serialized certificates and independent verifiers | exact project primary artifacts | local paths listed in `proof/proof_dag.md` | CC07–CC20 |

No citation was found that contradicts a manuscript claim. The novelty
conclusion remains bounded: “no all-`n` proof found in the recorded searches
through 2026-08-29,” not an absolute claim of historical priority.
