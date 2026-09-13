# Citation audit

Audit date: 2026-08-30. Mode: web-backed verification of literature claims
and definition-level local verification of the new finite claims. Pass 1 was
frozen in `audit/CITATION_CLAIMS.md` before this Pass 2 audit; no claim was
added, removed, or silently weakened during verification.

## Bibliographic record audit

The three journal records were checked by title, authors, year, venue,
pagination, and DOI using DOI/publisher metadata and independent indexes. The
BibTeX records were originally fetched by DOI content negotiation. Only TeX
normalization (math delimiters, page dash, and month syntax) was applied.

| Key | Authoritative/independent evidence | Result | Action |
|---|---|---|---|
| `Chung_1989` | [DOI 10.1109/18.30982](https://doi.org/10.1109/18.30982); [CiNii/Crossref record](https://cir.nii.ac.jp/crid/1360855568745675392); [author publication list](https://cseweb.ucsd.edu/~fan/research/papers/list.pdf) | Verified: Chung, Salehi, Wei; *IEEE Transactions on Information Theory* 35(3), 595--604 (1989). The DOI is `10.1109/18.30982`. | Retained official record. |
| `Bailey_2013` | [DOI 10.1016/j.disc.2011.11.039](https://doi.org/10.1016/j.disc.2011.11.039); [Elsevier version of record](https://www.sciencedirect.com/science/article/pii/S0012365X11005462); [arXiv:1107.4120](https://arxiv.org/abs/1107.4120) | Verified: Bailey and Burgess; *Discrete Mathematics* 313(11), 1167--1190 (2013). | Retained official record. |
| `Baicheva_2013` | [DOI 10.1007/s00200-013-0192-1](https://doi.org/10.1007/s00200-013-0192-1); [indexed author manuscript](https://www.researchgate.net/publication/257340440_Optimal_v521_optical_orthogonal_codes_of_small_v); [author publication list](https://www.moi.math.bas.bg/~tsonka/list_of_publications.htm) | Verified: Baicheva and Topalova; *Applicable Algebra in Engineering, Communication and Computing* 24(3--4), 165--177 (2013). Its notation is explicitly `(v,5,2,1)`. | Normalized malformed MathML in the DOI export to TeX; facts unchanged. |
| `TheoremDB2026` | [TheoremDB problem P2632](https://theoremdb.org/statements/P2632/) and its [canonical statement URL](https://www.theoremdb.org/statements/cyclic-315-packing-31/) | Verified as a dated research-memory web record, not as a peer-reviewed paper. The page states the certified interval 9--13 and remains marked open in the indexed snapshot. | Retained as `@misc`; access scope is explicit. |

All four citation keys used in `paper/main.tex` occur exactly once in
`paper/references.bib`. The auxiliary-file audit reports four cited keys,
four database keys, no missing keys, and no unused keys.

## Pass 2: claim-by-claim verification

`Verified (local exact)` means that the serialized input was reconstructed
without importing discovery output and checked with integer/set arithmetic.
`Verified (bounded search)` is intentionally not a universal priority claim.

| ID | Status | Evidence and audit finding |
|---|---|---|
| C01 | Verified (local exact) | C11 gives \(M\ge12\); C05/C15/C17 give \(M<13\). Together with the elementary \(M\le13\) reduction, the only value is 12. |
| C02 | Verified (local exact) | `code/verify_packing_certificate.py` reconstructs 31 translates of each of 12 blocks and reports 372 distinct blocks and 3,720 distinct triples. |
| C03 | Verified (local exact) | `code/enumerate_instance.py` and the no-import global verifier independently reconstruct 145 resources and 4,761 valid columns. |
| C04 | Verified (local exact) | `code/verify_global_fixed_cover.py` reconstructs the action of all 30 units and obtains 162 disjoint multiplier orbits. |
| C05 | Verified (local exact) | All 162 branch manifests are accepted and jointly cover all 4,761 block variables; every branch status is `UNSAT_BY_COMPLETE_BRANCHING`. |
| C06 | Verified | The correlation interpretation follows directly by translating two weight-five supports: a repeated triple is exactly overlap at least 3, hence both nonzero autocorrelation and cross-correlation are at most 2. Chung--Salehi--Wei is the foundational OOC reference verified above. |
| C07 | Verified | The title and definitions of Baicheva--Topalova use `(v,5,2,1)`, i.e. autocorrelation bound 2 and cross-correlation bound 1. This differs from equal bounds 2. |
| C08 | Verified | The dated TheoremDB record explicitly states the interval \(9\le M\le13\). |
| C09 | Verified (local exact) | Prime orbit-stabilizer counting gives \(\binom{31}{3}/31=145\) and \(\binom{31}{5}/31=5,481\); exhaustive reconstruction agrees. |
| C10 | Verified (local exact) | Definition-level enumeration rejects a block class exactly when two of its ten triples share a translation class, leaving 4,761. |
| C11 | Verified (local exact) | `certificates/packing12.json` is accepted by the positive verifier; deliberate duplicate/collision/schema mutations are rejected by `tests/test_positive_verifier.py`. |
| C12 | Verified (mathematical) | For each distance, a fixed pair has 29 possible third points and each developed block consumes three; thus \(r_d\le\lfloor29/3\rfloor=9\). Summing ten pairs over 15 distances gives \(10M\le135\), hence \(M\le13\). |
| C13 | Verified (mathematical) | At \(M=13\), \(\sum r_d=130\). Writing \(r_d=9-e_d\) gives \(l_d=29-3r_d=2+3e_d\) and \(\sum e_d=135-130=5\). |
| C14 | Verified (local exact) | Independent orbit reconstruction gives 156 orbits of size 30, five of size 15, and one of size 6, totaling 4,761. |
| C15 | Verified (local exact) | Every representative's exact compatibility neighborhood was exhaustively searched for a 12-clique; all 162 searches ended with the locked UNSAT status. |
| C16 | Verified (manifest aggregation) | The global verifier recomputes the sum 68,377,851,660 and the stated minimum/maximum from the 162 branch manifests. |
| C17 | Verified (local exact) | The fail-closed global verifier returns exactly `VERIFIED_GLOBAL_TARGET13_UNSAT`; coverage and corruption tests pass. |
| C18 | Verified (hash audit) | SHA-256 was recomputed for `experiments/instance.json`, the positive certificate, global manifest, `code/exact_clique.cpp`, and `experiments/exact_clique_fixed_fast`; all five match Table 1. |
| C19 | Verified (replay record) | Fresh compilation/replay records for fixed variable 537 (minimum nodes) and 362 (the unique size-six orbit) are recorded in the role and proof audits. |
| C20 | Verified | The positive, fixed-branch, global-cover, encoding, leave, and multiplier tests each include rejecting cases. Both auxiliary LRAT files are accepted by `literature/upstream_drat_trim/lrat-check`; truncation and semantic mutations are rejected. |
| C21 | Verified (process audit) | No Lean, Coq, Isabelle, HOL, or other proof-assistant source or invocation occurs in the project record. The negative checker is conventional C++/Python. |
| C22 | Verified (process audit) | `logs/roles/`, `routes/registry.json`, and the experiment ledger distinguish discovery from proof; UNKNOWN, timeout, floating, and interrupted runs are expressly excluded from the theorem. |
| C23 | Verified (bounded search) | Gate 2 in `literature/NOVELTY_LOCK.md` and `literature/search_log.md` records exact-parameter searches across TheoremDB, arXiv, OpenAlex, Crossref, citation neighbors, and indexed public code. None of those searched records resolved this parameter. This does **not** assert universal priority over unindexed or unpublished work. |

## Verdict

- Verified claims: 22.
- Verified only within an explicitly bounded search scope: 1 (C23).
- Contradicted or unsupported claims: 0.
- Bibliographic key, DOI, or metadata conflicts remaining: 0.

The paper's citations and externally checkable claims pass the two-pass gate.
The novelty sentence remains deliberately qualified by its documented search
scope.
