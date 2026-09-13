# Citation and bibliography audit

Audit date: 2026-08-29 (Asia/Shanghai)

Mode: search verification with local-certificate verification for claims that
are original to this project.

## Pass 1 — frozen claim extraction

The following list was extracted from `paper/main.tex` before any claim-level
verification. Definitions, displayed recurrences, reproduction commands, and
explicit limitations phrased as nonclaims were excluded under the skill's
claim-extraction rules.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Alavi--Malde--Schwenk--Erdős asked whether every tree (and perhaps forest) has a unimodal vertex-independence sequence. | attribution/existence | lines 49--54 |
| C02 | Erdős Problem 993 remains open without an order bound. | temporal/existence | lines 53--54, 238--239 |
| C03 | Tree log-concavity first fails at order 26. | attribution/statistic | lines 56--57 |
| C04 | Infinite and large searched families of non-log-concave trees are known. | existence/attribution | lines 57--59 |
| C05 | Reynolds reported exhaustive tree unimodality through order 29. | statistic/attribution | lines 59--60 |
| C06 | A later independently reviewed census reached order 30. | temporal/statistic/attribution | lines 60--62 |
| C07 | Every tree on exactly 31 vertices has a weakly unimodal independent-set sequence. | existence/original theorem | lines 114--116 |
| C08 | The order-31 enumeration contains exactly 40,330,829,030 unlabelled trees. | statistic | lines 133--138, 188 |
| C09 | All 120 order-31 residue classes report zero non-unimodal trees. | statistic/original result | lines 124, 138--147, 187--190 |
| C10 | The aggregate sequence and parent fingerprints are respectively `92f46f1b00c219ad` and `d53b120ed8c90b52`. | statistic/original result | lines 143--146, 191--192 |
| C11 | OEIS A000055 gives 40,330,829,030 unlabelled trees on 31 vertices. | statistic/attribution | lines 135--138 |
| C12 | Every tree on at most 31 vertices has a weakly unimodal sequence. | existence/corollary | lines 152--159 |
| C13 | Exactly 159 order-31 trees are non-log-concave, and all 159 are unimodal. | statistic/original result | lines 162--172, 190 |
| C14 | The coefficient and product bounds are exactly 300,540,195 and 90,324,408,810,638,025, both within `uint64_t` as stated. | statistic/derived | lines 97--109 |
| C15 | Direct subset enumeration reproduced every polynomial for all 436 unlabelled trees through order 11. | statistic/original validation | lines 200--203 |
| C16 | The order-23 24-way partition and unsplit run both contain 14,828,074 trees and have matching fingerprints. | statistic/original validation | lines 203--205 |
| C17 | The summed checker CPU time is exactly 56,320.05 seconds. | statistic/original result | line 193 |
| C18 | The three displayed SHA-256 values bind the checker source, checker binary, and nauty archive. | statistic/original integrity claim | lines 210--218 |
| C19 | The bundled `gentreeg` source identifies Li and Ruskey's algorithm and code as the basis of the generator. | attribution | lines 120--124 |
| C20 | McKay and Piperno describe nauty. | attribution | lines 122--123 |
| C21 | Every saved order-31 exceptional polynomial was independently rebuilt with arbitrary-precision integers. | existence/original validation | lines 141--147, 166--172 |
| C22 | The isolated rebuild reproduced the order-23 residue fingerprints and passed the direct subset audit through order 11. | existence/original validation | lines 204--208 |
| C23 | No proof assistant or theorem prover was used. | process/existence | lines 248--250 |
| C24 | OpenAI Codex assisted with the listed research and drafting tasks. | process/existence | lines 252--255 |

Pass 1 is frozen. Pass 2 may verify or correct these claims, but it may not
silently add a newly noticed claim to this list.

## Mechanical key check before Pass 2

`check_bib_keys.py paper/main.tex` reported nine cited keys, nine bibliography
entries, no missing bibliography file, no cited key absent from the `.bib`,
and no unused entry.

## Pass 2 — verification

### Summary

| Metric | Count |
|---|---:|
| Frozen claims | 24 |
| Verified by primary web source | 8 |
| Verified by exact local certificate or direct derivation | 14 |
| Verified process disclosures | 2 |
| Numerical errors | 0 |
| Misquotations or hallucinations | 0 |
| Unverified claims | 0 |

Overall status: **PASS, 24/24**.

### Claim-level results

| ID | Status | Evidence and exact check |
|---|---|---|
| C01 | Verified — paraphrase | The archival 1987 paper states Problem 3 in the tree/forest form: [Alavi--Malde--Schwenk--Erdős, pp. 15--23](https://www.renyi.hu/~p_erdos/1987-33.pdf). |
| C02 | Verified — exact temporal status | The live [SciNet problem record](https://api.scinet.pub/p/8383c81d-e6c5-406d-aa40-43e383f3d57f) is ACTIVE, describes proof/counterexample acceptance, and lists only finite advances. Its latest event remains the order-30 finding. |
| C03 | Verified — exact | The formal [publisher repository record](https://repozitorij.upr.si/IzpisGradiva.php?id=22017&lang=eng) and [DOI](https://doi.org/10.26493/1855-3974.3207.2ad) identify the version of record as *Ars Mathematica Contemporanea* 25(4) (2025), article P4.03; its title states non-log-concavity starting at order 26. |
| C04 | Verified — paraphrase | [Galvin, arXiv:2502.10654](https://arxiv.org/abs/2502.10654) constructs an infinite family; [Ramos--Sun, arXiv:2510.18826](https://arxiv.org/abs/2510.18826) reports tens of thousands of searched examples on 27--101 vertices. |
| C05 | Verified — exact | The [Zenodo 19100781 record](https://zenodo.org/records/19100781) reports all 8,691,747,673 trees through order 29. |
| C06 | Verified — exact | The [SciNet order-30 finding](https://api.scinet.pub/f/b1eaa502-a0b8-4181-a285-2e7fa9cee15d) reports exactly 14,830,871,802 order-30 trees, zero non-unimodal sequences, and an independent review/reproduction. |
| C07 | Verified — exact local theorem | `results/order31_aggregate.json` and the independent aggregate both return PASS with exact complete coverage and zero non-unimodal trees. |
| C08 | Verified — exact | Both local aggregators give 40,330,829,030; [OEIS A000055](https://oeis.org/A000055) gives the identical order-31 count. Deviation: 0. |
| C09 | Verified — exact | There are exactly 120 paired summaries; every chunk has `trees=generated>0`; aggregate `nonunimodal=0`. |
| C10 | Verified — exact | Both aggregators independently sum the exact same two fingerprints: `92f46f1b00c219ad` and `d53b120ed8c90b52`. |
| C11 | Verified — exact | OEIS A000055 defines the sequence as the number of trees with $n$ unlabelled nodes and lists 40,330,829,030 at $n=31$. |
| C12 | Verified — exact derivation | C07 covers order 31; the independently reviewed C06 source covers every order through 30. No unstated induction is used. |
| C13 | Verified — exact | Both local aggregators report 159; the independent verifier rebuilds 159 serialized non-log-concave records and accepts their unimodality. |
| C14 | Verified — exact derivation | Python integer recomputation gives $\binom{31}{15}=300{,}540{,}195$ and square $90{,}324{,}408{,}810{,}638{,}025<2^{64}-1$. Deviation: 0. |
| C15 | Verified — exact local certificate | `experiments/crosscheck_c_checker.py` reports all 436 unlabelled trees through order 11 and reconstructs each polynomial by subsets. |
| C16 | Verified — exact local certificate | `results/partition_test_order23_aggregate.json` reports 24 chunks, 14,828,074 trees, and the same two fingerprints as the unsplit result. |
| C17 | Verified — exact | Both local aggregates independently sum checker CPU time to 56,320.05 seconds. Deviation: 0. |
| C18 | Verified — exact | Fresh SHA-256 recomputation matches all three strings in the manuscript and the preflight. |
| C19 | Verified — exact attribution | The frozen `gentreeg.c` says that the wrapper contains `FreeTrees.c` written by Li and Ruskey, labels them the programmers, and identifies the algorithm as coming from their 1999 paper.  The manuscript makes only this algorithm/code-source attribution; it does not say that the 1999 paper describes the later wrapper.  The [official University of Victoria publication page](https://webhome.cs.uvic.ca/~ruskey/Publications/RootedFreeTree/RootedFreeTree.html) verifies the paper metadata. |
| C20 | Verified — paraphrase | The DOI record and [arXiv:1301.1493](https://arxiv.org/abs/1301.1493) identify McKay--Piperno's paper and state that it brings the description of nauty up to date. |
| C21 | Verified — exact local certificate | `results/order31_independent_aggregate.json` records `rebuilt_serialized_nonlogconcave=159`; its source imports no project module and evaluates with Python integers. |
| C22 | Verified — exact local certificate | `results/order31_rebuild_audit.txt` records the matching order-23 residue fields, all 436 direct-subset checks, and `REBUILD_AUDIT PASS`. |
| C23 | Verified — process disclosure | No Lean, Coq, Isabelle, HOL, SMT proof assistant, or theorem-prover artifact or invocation appears in the project run; the proof is an exact finite computational certificate. |
| C24 | Verified — process disclosure | This project was executed in OpenAI Codex; the listed assistance categories match the recorded work. |

### Bibliography record audit

| Key | Official/primary source | Result |
|---|---|---|
| `AlaviMaldeSchwenkErdos1987` | Erdős archival PDF | Minimal manual entry verified; no official BibTeX export located. |
| `Kadrawi_2025` | DOI content negotiation for 10.26493/1855-3974.3207.2ad | Formal journal block used with two documented BibTeX-safety normalizations: Crossref's non-compiling `pages={#P4.03}` became the publisher-displayed `pages={P4.03}`, and warning-producing `month=July` became the identical literal `month={July}`.  All authors, title, journal, volume, issue, year, DOI, URL, publisher, and ISSN fields are unchanged. |
| `galvin2026treesnonlogconcaveindependent` | arXiv official `/bibtex/2502.10654` | Official block used verbatim; corrected year from 2025 to 2026. |
| `ramos2025aienhancedapproachtree` | arXiv official `/bibtex/2510.18826` | Official block used verbatim; removed unsupported middle initial. |
| `reynolds_2026_19100781` | Zenodo official BibTeX export | Official block used verbatim. |
| `SciNetOrder30` | Live SciNet finding | Entry verified and author corrected from generic SciNet to the displayed Roman Labs attribution. |
| `OEISA000055` | OEIS A000055 | Minimal web-resource entry verified. |
| `LiRuskey1999` | Author's University of Victoria publication page | Minimal proceedings entry verified. |
| `McKay_2014` | DOI content negotiation for 10.1016/j.jsc.2013.09.003 | Official publisher/Crossref block used verbatim. |

Key changes synchronized in `paper/main.tex`:

- `KadrawiLevit2023` → `kadrawi2023independencepolynomialtreeslogconcave` → `Kadrawi_2025`
- `Galvin2025` → `galvin2026treesnonlogconcaveindependent`
- `RamosSun2025` → `ramos2025aienhancedapproachtree`
- `Reynolds2026` → `reynolds_2026_19100781`
- `McKayPiperno2014` → `McKay_2014`

Final mechanical and clean-build check: nine cited keys, nine bibliography
entries, nine auxiliary citations, no missing or unused key, and no LaTeX or
BibTeX warning. There are no unresolved citation blockers.

## Terminal revision: frozen claims C25--C29

This list was frozen before the terminal revision was verified.

| ID | Claim | Type | Location |
|---|---|---|---|
| C25 | Kadrawi--Levit is a formal journal article in *Ars Mathematica Contemporanea* 25(4) (2025), article P4.03, DOI 10.26493/1855-3974.3207.2ad. | attribution/temporal | bibliography and citation C03 |
| C26 | The manuscript attributes only the algorithm/code basis of `gentreeg` to Li--Ruskey, not the later wrapper's description. | attribution | theorem proof, lines 120--124 |
| C27 | Missing residue 119, a residue-000 count mismatch, a changed terminal coefficient, and a changed preflight hash each force nonzero verifier exit. | local exact validation | fail-closed audit |
| C28 | The documented manuscript build changes into `paper/` before invoking LaTeX and BibTeX. | process | release README |
| C29 | The theorem is restricted to exactly 31 vertices; the unrestricted conjecture remains open. | scope/existence | title, abstract, theorem, limitations, final status |

### Terminal revision: Pass 2

| ID | Status | Evidence |
|---|---|---|
| C25 | Verified -- exact | DOI content negotiation and the University of Primorska repository agree on both authors, title, 2025, volume 25, issue 4, and article P4.03. |
| C26 | Verified -- exact | Lines 1--4 and 94--98 of the frozen `gentreeg.c` distinguish the later wrapper from Li--Ruskey's `FreeTrees.c`, algorithm, and code.  The revised sentence preserves that distinction. |
| C27 | Verified -- exact | `results/fail_closed_rejection_tests.json` records nonzero exit code 1 and the expected rejection reason for all four independently materialized corruptions. |
| C28 | Verified -- exact | Both the root `RELEASE_README.md` and the packaged `README.md` use `cd paper` before the four build commands. |
| C29 | Verified -- exact | The theorem says “exactly 31”; the abstract, limitations, `TASK_STATUS.json`, and `FINAL_STATUS.md` explicitly leave arbitrary order open. |

Terminal-revision result: **PASS, 5/5**.  Combined citation/claim result:
**PASS, 29/29**.  No unresolved citation blocker remains.
