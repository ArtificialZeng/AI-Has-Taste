# Verification Report

**Mode:** Primary-source search verification, with local accepted-proof and finite-evidence checks.
**Job:** `newwin-00001-p07-release-eea8aff93c71`.
**Generated (UTC):** 2026-09-12T08:35:50.951410+00:00.
**Overall status:** PASS for the exact current manuscript/PDF scope.

| Metric | Count |
|---|---:|
| Frozen claim units | 21 |
| Verified | 21 |
| Citation-bearing claim units | 7 |
| Distinct body citation keys | 4 |
| Non-library primary references | 3 |
| Selected library references | 1 |
| Unverified / numerical errors / misleading / hallucinations | 0 |

The two stages were non-interactive, as instructed. The full manuscript was read and its claim ledger frozen before fresh source verification. A later formatting-only repair moved the Section 6 locator out of the selected citation optional argument; no claim text, key, hypothesis or theorem changed. The final ledger has current canonical source hashes and the current manuscript snapshot digest. This fresh context performed all reference checks itself: agents were explicitly prohibited by the user.

## Claim checks

| ID | Manuscript lines | Result and evidence |
|---|---|
| C01 | 29–38 | Verified: Accepted frozen proof, manuscript Theorem 1/Lemmas 2–4/Corollary 5, and Archer–Bourne Section 5 paragraph 2. The abstract matches the accepted scope. |
| C02 | 51–53 | Verified: BonaSmith2019, Section 1, PDF page 2, lines 33–36. |
| C03 | 53–55 | Verified: ArcherGeary2024, Introduction, PDF pages 1–2; chain definition assigns a pattern to each power. |
| C04 | 55–58 | Verified: ArcherBourne2026, Lemma 3.1, Theorem 3.5 and Section 5 paragraph 2. |
| C05 | 79–90 | Verified: claim.json and evidence/bijection-proof.md Sections 1–3; manuscript proofs preserve both directions, size and empty cases. |
| C06 | 92–93 | Verified: ArcherBourne2026, Lemma 3.1 and following composition-bijection sentence, HTML lines 122–128. |
| C07 | 93–94 | Verified: ArcherGeary2024, Lemma 2.1 and invariant-interval proof, PDF page 2, lines 80–102. |
| C08 | 95–100 | Verified: ArcherGeary2024, Theorem 5.2 and proof, PDF page 16, especially lines 1428–1438. Source k>=2 and its 231/321 input and 132 target are kept distinct from the current result. |
| C09 | 106–109 | Verified: ArcherBourne2026 Lemma 3.1 for positive n; manuscript Lemma 2 proves the empty extension directly. |
| C10 | 112–136 | Verified: Manuscript Lemma 2 proof, compared to frozen evidence Section 1: forced prefix, strictly decreasing remaining size, and both inverse identities. |
| C11 | 139–146 | Verified: Manuscript Lemma 3 proof, frozen evidence Section 2; invariant intervals and exact modular cube formula. |
| C12 | 149–171 | Verified: Exact block cases and two increasing runs in frozen evidence Section 2 agree with manuscript. Successive selected entries have at most one descent. |
| C13 | 174–198 | Verified: Frozen evidence Section 3 and accepted audit/math.md step 4; the internal avoidance hypothesis and empty case remain explicit. |
| C14 | 201–208 | Verified: Theorem 1 proof combines precisely the inversion criterion and unrestricted inverse identities; no square assumption is introduced. |
| C15 | 211–215 | Verified: Directly checked the two three-letter encodings have identity cubes; a single summand equal to 2143 supplies the stated omitted-hypothesis example. |
| C16 | 219–243 | Verified: Frozen evidence Section 4 and manuscript Corollary 5: the exceptional part is unique; A and E are formal series; constant term one. |
| C17 | 246–249 | Verified: audit/referee-check.json full_permutation_rows and formal_series.coefficients_0_to_16; first ten values match exactly. |
| C18 | 250–255 | Verified: Read audit/referee_verify.py full permutation loop, third_power and ranks; audit/referee-check.json records coverage. Sum of factorials 0! through 9! was freshly recomputed as 409114. No release-phase rerun of the full enumeration is claimed. |
| C19 | 255–259 | Verified: Read generic pool/list loop and degree-100 expansion in audit/referee_verify.py and output JSON. Freshly checked 1+32+32^2=1057 and 1!+2!+3!+4!-1=32. |
| C20 | 261–267 | Verified: ZengEtAl2026 Section 6, lines 207–218, and the local separate verifier. The comparison is restricted to exact predicates and separate implementation, not identical algorithms or proof strength. |
| C21 | 270–280 | Verified: Fresh archive byte/syntax inspection in audit/release-supplement-check.json, README run instructions, accepted math report and frozen proof assistance disclosures; literature queries recorded in current source-search evidence. No absolute priority, formal verification or external peer-review claim appears. |

The complete fixed claim text, type, precise source location and direct keys are in `audit/citation-claim-ledger.json`; statuses and confidence classifications are in `audit/citation-claim-verification.json`. Mathematical scope checking uses the accepted claim and original proof, not a bibliography record as evidence of a new theorem. Numerical evidence is reported with exact finite coverage and does not establish the all-n conclusion.

## Bibliographic records and nearby support

### BonaSmith2019
Miklós Bóna; Rebecca Smith. *Pattern avoidance in permutations and their squares*. Discrete Mathematics 342(11), 3194–3200 (2019). DOI `10.1016/j.disc.2019.06.029`.
[Primary record](https://www.sciencedirect.com/science/article/pii/S0012365X19302250); [inspected text](https://arxiv.org/pdf/1901.00026). Section 1, PDF page 2, first paragraph; definition of strong q-avoidance (PDF extracted lines 33–36).
The defining restriction uses the same pattern for a permutation and its square.
Retained existing verified entry; no key change; no reconstructed export was presented as official BibTeX.
Direct publisher open failed; publisher-indexed metadata and accessible author-deposited full PDF supplied the necessary evidence.

### ArcherGeary2024
Kassie Archer; Aaron Geary. *Powers of permutations that avoid chains of patterns*. Discrete Mathematics 347(9), 114040 (2024). DOI `10.1016/j.disc.2024.114040`.
[Primary record](https://www.sciencedirect.com/science/article/abs/pii/S0012365X24001717); [inspected text](https://arxiv.org/pdf/2312.14351). Introduction, PDF pages 1–2; Lemma 2.1 and proof, PDF page 2, lines 80–102; Theorem 5.2 and proof, PDF page 16, lines 1371–1441.
Chains allow power-dependent patterns; invariant direct-sum intervals justify powers; for the stated 231/321 input and 132 output (k>=2), every part after the first divides k.
Retained existing verified entry, including the word that in the title; no key change.
The nearby theorem was checked in the full primary arXiv version, not inferred from publisher metadata. The source uses the inverse orientation of the cyclic block; the manuscript distinguishes its input and target.

### ArcherBourne2026
Kassie Archer; Noel Bourne. *Pattern avoidance in compositions and powers of permutations*. Discrete Mathematics & Theoretical Computer Science 28(1), article 4 (2026). DOI `10.46298/dmtcs.17199`.
[Primary record](https://dmtcs.episciences.org/18231); [inspected text](https://arxiv.org/html/2505.05218v3). Lemma 3.1 and following bijection sentence, HTML lines 122–128; Theorem 3.5, lines 169–175; Section 5 second paragraph, line 368.
Known cyclic-block encoding and square enumeration are attributed. The stated cube conjecture has no square condition and permits an exceptional part at any position. The n=0 extension and both inverse identities are proved in the current manuscript.
Retained existing verified entry; no key change.
Publisher BibTeX export endpoint returned an internal error. The retained entry was checked field by field against the primary record/header; no fabricated official export was substituted.

### ZengEtAl2026
Zijian Zeng; Houde Liu; Kuru Ratnavelu; Ong Seng Huat. *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*. Preprints.org, version 1, posted 24 August 2026; not peer-reviewed (2026). DOI `10.20944/preprints202608.1658.v1`.
[Primary record](https://www.preprints.org/manuscript/202608.1658/v1); [inspected text](https://www.preprints.org/manuscript/202608.1658/v1). Section 6, Certificate Architecture and Reproducibility, primary HTML lines 207–218: reconstruction, separate exact implementation, integer/rational comparisons. DOI/title/authors/date association: official Computational Mathematics subject listing, lines 142–167.
The manuscript makes the limited comparison of exact predicates and separately implemented checking. It borrows no geometric bound, classification, complexity guarantee, or conclusion for arbitrary permutation sizes.
Retained existing verified preprint entry and displayed Ong Seng Huat name; no key change. Section locator moved out of the optional citation argument into ordinary text.
DOI resolver open failed, but the live primary record, full text and official subject listing were available. Registry metadata alone was not used as verification.

## Coverage and relevance

The bibliography is sufficient for the actual external claims: Bóna–Smith supplies the strong-avoidance definition; Archer–Geary supplies chains, the direct-sum lemma and the closest higher-power comparison; Archer–Bourne supplies the exact original conjecture, block encoding and square comparison. These three works are not in the active user library by DOI/title/key identity. The ordinary definition of compositions, the block calculation, the two-inversion argument and the elementary formal enumeration are provided in full; no unmentioned external theorem, analytic transfer theorem, SAT solver or clique algorithm is used in the proof. Adding references to such unused methods would be padding.

All 49 active first-sheet library titles were screened, and the closest permutation and finite-verification entries were inspected as leads. Row 9 is the single selected work because Section 6 documents the exact-predicate and separate-verifier features actually compared in the body. The manuscript labels the work a preprint and imports no geometric result. Rows 40 and 45 concern different permutation questions; rows 49 and 50 do not add a needed technique to this short proof. The selection is a minimum coverage choice, not a cap on references. Its `registry_binding` was generated from the live registry/workbook and its exact one-sentence citation context passed the installed hook-compatible selection validator.

## Dependency and build scope

Reviewed all sorted publication sources: `manuscript/README.md`, `manuscript/main.tex`, `manuscript/references.bib`, `manuscript/supplement.zip`. The canonical TeX contains no included fragments, local styles, figures, hidden conditionals, inert citation macros or nocite-only references. Installed TeX packages and plainurl are standard build dependencies; the generated BBL/auxiliary products were checked. Supplement CRC, file identity, code syntax and stated numerical metadata passed fresh local checks. The final key checker reports four cited keys, four bibliography keys, four auxiliary keys, and zero missing or unused keys. The clean final TeX/BibTeX logs have no unresolved citation/reference warning.

`manuscript/references.bib` required no edit and no key changed. `manuscript/main.tex` lines 263–264 received only the direct-citation formatting repair. Official export access failures are recorded, without substituting invented exports or treating them as failure of available primary evidence. The publisher-indexed records, deposited PDFs/full HTML and official Preprints listing jointly verify all retained bibliographic fields and nearby claims. No source was declared unavailable without enumerating the supplied Crossref-capture patterns (both empty).

## Search and scope limits

Search date is 2026-09-12 UTC. `audit/citation-search-index.json` records every applicable search template and evidence file. Sources were checked at the original lemma, theorem, proof paragraph or method section, not merely at DOI existence. No later equivalent resolution was identified among the inspected sources and targeted results. This is a bounded novelty comparison, not a guarantee of priority, external peer review or public publication.

## Snapshot binding

Accepted mathematical snapshot: `fe32cd463141d526a90ca7859d55059aa1c6d3392a12234796cdd4a3af87ba8e`.
Manuscript: `9b400315173b3f139418af88297c0b16a3cb6a2e7e69400d2159eaef4ce21e18`.
PDF: `06151776bf758df940a752315bb7beb008e876a8624db1f50f278b49323ed0b5`.
