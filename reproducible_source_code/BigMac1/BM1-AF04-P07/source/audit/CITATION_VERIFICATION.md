## Verification Report

**Mode:** Search verification  
**Document:** `paper/main.tex`  
**Generated:** 2026-08-30 (Asia/Shanghai)

### Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 30 |
| Verified | 30 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall Status:** **PASS: all C01--C30 verified.**

Pass 1 is frozen in `audit/CITATION_CLAIM_EXTRACTION.md`.  Pass 2 used that
list sequentially and did not re-extract or add claims.  External historical
claims were checked against primary, publisher, institutional, or official
records; claims introduced by this work were checked against the serialized
exact artifacts and independent replay logs, not against web summaries.

### Verified claims

| ID | Claim (abbreviated) | Source and exact support | Confidence |
|---|---|---|---|
| C01 | Yuster conjectured the displayed formula. | Yuster author PDF, Conjecture 1.1, lines 29--35 of the parsed primary text. | exact |
| C02 | Verified for every `n<=8`. | Yuster author PDF, lines 35 and 353--356. | exact |
| C03 | The `n=8` case was computational. | Yuster author PDF, line 356. | exact |
| C04 | Kabiya--Yuster proved the `41/300` bound via a fractional relaxation. | University of Haifa CRIS abstract and author PDF abstract, which state the coefficient and fractional/integral connection. | exact |
| C05 | The 2026 note gives `nu_3(9)=9`, `nu_3(10)=12` with exhaustive artifacts. | Kirtchakov public note, lines 203--207 and repository artifact description. | exact |
| C06 | `nu_3(11)=15`. | `certificates/n11_sweeps_match.json` proves the universal lower bound within the declared generator contract; `certificates/minimizer_11.json` plus its independent verifier proves the matching upper bound. | exact |
| C07 | Yuster's `4,4,3` specialization gives upper bound 15. | Yuster author PDF, lines 342--352; local arithmetic `6+6+3=15`. | exact |
| C08 | The 55-bit literal and fifteen triples certify a minimizer. | `certificates/minimizer_11.json`; `MINIMIZER_OK` in `logs/final_replay.log`. | exact |
| C09 | The literal has 117 transitive triples, all hit by 15 within-part pairs. | Independent exhaustive loop in `code/verify_minimizer.py`; serialized output reports `transitive_triples_checked=117`, `within_pairs=15`. | exact |
| C10 | nauty 2.9.3, `gentourng`, 192 residues. | `logs/environment.txt`, both aggregate certificates, and all 192 residue records. | exact |
| C11 | McKay--Piperno describe nauty and canonical-labeling methods. | arXiv:1301.1493 abstract explicitly describes the refinement-individualization framework and nauty implementation. | paraphrase |
| C12 | OEIS A000568 records unlabeled tournament counts. | Official OEIS A000568 title and sequence line. | exact |
| C13 | Davis-formula evaluation gives 903,753,248. | Official OEIS formula lines 83--88; exact `Fraction` replay in `logs/final_replay.log`. | exact |
| C14 | The 192 slice counts sum exactly to 903,753,248. | `verified_total` in both order-11 aggregate JSON certificates. | exact |
| C15 | Builder accepted every class. | `certificates/n11_builder_full_m192.json`: PASS, 192 slices, verified total 903,753,248, no failure slice. | exact |
| C16 | Certifier accepted every class. | `certificates/n11_certifier_full_m192.json`: PASS, 192 slices, verified total 903,753,248, no failure slice. | exact |
| C17 | All 192 counts and input-stream digests match. | `certificates/n11_sweeps_match.json`: PASS and `matching_slices=192`; comparator replay in `logs/final_replay.log`. | exact |
| C18 | Scanner executable hashes differ. | Match certificate records Builder `73da...111a` and Certifier `f7d2...9157`. | exact |
| C19 | Class-count table for orders 3--11. | Official OEIS A000568 sequence; independent exact output in `logs/final_replay.log`. | exact |
| C20 | Both programs reproduce the `n=9,10` baseline. | `certificates/baseline_n9_sweeps_match.json` and `baseline_n10_sweeps_match.json`; final replay. | exact |
| C21 | 32 blow-ups and 100,000 seeded random tournaments were tested. | Strict summaries in `logs/breaker_cyclic_443_{builder,certifier}.log` and `logs/breaker_random100k_{builder,certifier}.log`; equal stream digests in each pair. | exact |
| C22 | Exact maximum on the minimizer is 15. | `certificates/structured/minimizer_11_exact.txt`, value 15 with literal witness. | exact |
| C23 | Twenty-one corruptions were rejected. | Six minimizer, nine scanner/aggregate, and six comparison rejections in `logs/final_replay.log`. | exact |
| C24 | Recorded software/OS environment. | Direct version output serialized in `logs/environment.txt`; compiler-generated hashes match the aggregate certificates. | exact |
| C25 | Per-class witnesses are not stored; independent inputs are regenerated. | Release tree inspection, `code/run_sweep.sh`, separate aggregate indices, and Certifier role record. | exact |
| C26 | One Codex CLI session, no subagents, serial four-role protocol. | User execution contract in `CLI_PROMPT.md` and four role records under `audit/roles/`; no subagent record exists. | exact |
| C27 | No floating point, optimizer, SAT solver, or proof assistant in the decisive lower bound. | Source inspection of both C scanners and Python gates; only integer/bitwise search and hashing occur. | exact |
| C28 | Sole named author and responsibility declaration. | Explicit user authorship contract in `CLI_PROMPT.md`; LaTeX contains no additional author. | exact |
| C29 | Leave graph is `K_4`-free and has `55-3q` edges. | Direct audited proof in `proof/structural_reductions.md` and Section 2 of the manuscript. | exact |
| C30 | One-vertex extension iff the admissible leave graph has a 3-matching. | Direct two-way audited proof in `proof/structural_reductions.md` and Section 2 of the manuscript. | exact |

### Numerical and visual integrity

The manuscript contains one numerical table.  Every value in its orders
3--11 class-count column agrees exactly, digit for digit, with both official
OEIS A000568 and the independent rational-arithmetic output.  The target
column is the exact integer evaluation of Yuster's formula.  The manuscript
contains no chart, plotted axis, photographic claim, or rounded data graphic.

### Sources

| ID | Citation | Type | URL / local artifact | Used for |
|---|---|---|---|---|
| S1 | Yuster (2004), *The number of edge-disjoint transitive triples in a tournament* | primary author PDF / journal DOI | `https://math.haifa.ac.il/raphy/papers/tt3tour.pdf`; DOI `10.1016/j.disc.2004.07.005` | C01--C03, C07 |
| S2 | Kabiya--Yuster (2008), *Packing transitive triples in a tournament* | institutional record / primary author PDF | `https://cris.haifa.ac.il/en/publications/packing-transitive-triples-in-a-tournament/`; DOI `10.1007/s00026-008-0352-3` | C04 |
| S3 | Kirtchakov (2026) certified note | public primary repository | `https://github.com/05oz/certify/blob/main/tt3-paper/note.md` | C05 |
| S4 | McKay--Piperno (2014), *Practical graph isomorphism, II* | primary arXiv / journal DOI | `https://arxiv.org/abs/1301.1493`; DOI `10.1016/j.jsc.2013.09.003` | C11 |
| S5 | OEIS A000568 | official sequence record | `https://oeis.org/A000568` | C12, C13, C19 |
| S6 | Davis (1954), *Structures of dominance relations* | original bibliographic record / DOI | DOI `10.1007/BF02478368`; formula cross-checked in S5 | C13 |
| S7 | Exact local release artifacts | primary computation and replay evidence | `certificates/`, `logs/final_replay.log`, `code/`, `tests/` | C06, C08--C10, C14--C25, C27 |
| S8 | User execution contract and role ledger | primary provenance record | `CLI_PROMPT.md`, `audit/roles/` | C26, C28--C30 |

No numerical errors, citation-not-found cases, hallucinations, misleading
claims, or unresolved items remain.  The Zenodo landing redirect for the 2026
note could not be opened in the web sandbox; the note itself and public GitHub
artifacts were directly inspected, and the DOI is therefore not used as the
sole support for any claim.
