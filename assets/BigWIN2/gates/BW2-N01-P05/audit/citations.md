# Verification report

**Overall status: PASS.** Mode: primary-source search and local accepted-evidence verification.
Job: `newwin-00001-p05-release-df34904a6a33`. Checked: 2026-09-12T10:11:20.355939+00:00. Citation attempt 1; launch `c2ccef94-9c81-44d3-bcc0-0e973282ad7e`.

The final manuscript has 32 extracted claims and five active citation keys. All 32 claims are supported within their stated scope; no numerical error, unsupported strengthening, missing active reference or undefined citation remains. Mathematical theorem checks here trace the frozen acceptance; they do not constitute a new mathematical referee decision.

## Two-stage method and scope

The release worker read the complete manuscript, bibliography and Python companion, froze the claim/citation list, and then checked source existence, bibliographic identity, exact passages, hypotheses and nearby support. After the small citation/layout repairs, the final 32-claim extraction was frozen separately and replayed sequentially. The claim content of the final ledger equals that extraction exactly. Its citation-key union equals the conservative parser's ordinary body-flow key set. Comments, verbatim program text and inert macros contribute no keys.

The explicitly requested `citation-check-skill` and `bib-reference-audit` were used serially because the user forbade agents. No interactive confirmation or pre-publication hook was invoked. All applicable academic search templates were issued for retained citations; noisy unrelated results were discarded. Original primary texts, not search snippets alone, support the citation decisions. Direct web records and requests are saved under `audit/release-sources/`.

The exact final source scope is `manuscript/main.tex`, `manuscript/references.bib`, and `manuscript/verify_base.py`. The code is now printed in standard verbatim blocks and also supplied as a companion file. Its nonblank source and AST match exactly. Generated BibTeX/TeX auxiliaries and installed packages are build dependencies, not additional authored publication sources.

## Bibliography coverage and identity

The printed bibliography contains four natural non-library sources for the problem origin, deterministic map, closest length-layer results and nearby image/preimage work, plus one exact-computation method comparison. No reference quota was used and no theorem is attributed to the library paper. The elementary multinomial counts and literal simulation are explained or implemented in full and need no unrelated algorithm citation.

| Key | Primary identity and location | Natural role | Action |
| --- | --- | --- | --- |
| `DefantKravitz2024` | Colin Defant; Noah Kravitz, *Foot-Sorting for Socks*, Electronic Journal of Combinatorics 31(3), P3.5. [Primary source](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i3p5); Journal record lines 18-35: author/title/DOI, abstract, publication date and citation | Problem origin: introduction of foot-sorting for set partitions | Verified and retained; no key change |
| `Xia2024` | Janabel Xia, *Deterministic Stack-Sorting for Set Partitions*, Enumerative Combinatorics and Applications 4(3), S2R23. [Primary source](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A23.pdf); Journal p.1 metadata; p.4 Definition 2.5; p.5 Lemma 3.1 and Theorem 3.1 with proof; p.9 Question 6.1 | Exact map, sharp alphabet bound, clump growth, first-letter formula and maximal-time problem | Verified journal numbering and retained; no key change |
| `ChoiGanLiZhu2025` | Yunseo Choi; Katelyn Gan; Andrew Li; Tiffany Zhu, *Set Partitions that Require a Maximum Number of Sorts Through the aba-avoiding Stack*, Enumerative Combinatorics and Applications 5(1), S2R1. [Primary source](https://ecajournal.haifa.ac.il/Volume2025/ECA2025_S2A1.pdf); Journal p.1 metadata; p.2 Theorems 1.1-1.2; p.3 Corollaries 2.1-2.2 and Proposition 3.1; pp.4-5 Lemma 3.5 | Closest prior length-layer results, known first-letter-four subclass, maximal clump counts and truncation | Retained 2025 volume year; distinguished from online publication on 6 September 2024 |
| `GaneshXiaYing2024` | Samanyu Ganesh; Lanxuan Xia; Bole Ying, *More results on stack-sorting for set partitions*, arXiv:2408.05377v1, 9 August 2024. [Primary source](https://arxiv.org/html/2408.05377v1); Abstract record and primary HTML introduction lines 49-51; Sections 3 and 4 | Nearby image-membership and preimage/fertility results distinguished from insertion theorem | Verified explicitly versioned preprint and retained; Lanxuan Xia is distinct from Janabel Xia |
| `Zeng2026MultiplicityArxiv` | Zijian Zeng, *Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees*, arXiv:2608.18179v1, 18 August 2026. [Primary source](https://arxiv.org/html/2608.18179v1); Section 4 final paragraph, primary HTML lines 131-134; data/code paragraph line 149. Primary abstract record lines 8-27 verifies metadata and DOI. | Specific combinatorial comparison of independent exact implementations, explicitly small-order and diagnostic | Added unchanged active-library row-17 BibTeX after every field was verified from arXiv; no invented export or identifier |

The active registry and manifest identify all 49 entries of first sheet `数学主表`; the dynamic selection binding validates the registry against its workbook. Row 17 is the single gate-bound selection. Its precise Section 4 passage supports the smallest citation-bearing sentence at manuscript lines 256-259, and arXiv directly displays its DOI, title, author, date and version. The following sentence explicitly preserves the source's diagnostic limitation. No tree-reconstruction theorem is used as a stack-sorting premise.

The original geometric comparison (`ZengEtAl2026`, row 9) had valid primary-text support, but its DOI could not be independently retrieved. It was replaced in body flow by the verified combinatorial comparison; its existing uncited BibTeX entry was preserved and is not printed. This is a change of compared work, not a key alias. Its missing DOI was not invented. No official BibTeX export request succeeded; existing verified entries were left intact, and the new row-17 entry was copied verbatim from the supplied library only after all fields were independently confirmed by the primary arXiv record. It is not represented as a fetched official export.

No bibliography-revision, handoff or Crossref-capture files were present at the required enumerations. Shell requests were denied by the environment. Those transport failures did not negate the accessible primary texts or become mathematical findings. Bibliographic export transport remains a documented access limitation, not an unresolved printed identifier.

## Fixed claims and exact support

Every entry below was checked against the frozen extraction. Complete text, line interval, direct keys, source locators and support are in `audit/citation-verification.json`; the table gives the individual verdicts.

| ID | Manuscript lines | Direct keys | Source location and support | Verdict |
| --- | --- | --- | --- | --- |
| C01 | 50-51 | DefantKravitz2024 | Journal abstract, lines 24-25. The primary abstract explicitly introduces foot-sorting as a stack-sorting analogue for set partitions. | Verified |
| C02 | 51-59 | Xia2024 | Definition 2.5, printed p.4. Subsequence avoidance, greedy push/pop retry and final output convention agree. | Verified |
| C03 | 68-70 | Xia2024 | Theorem 3.1 and proof p.5; Question 6.1 p.9. All alphabet sizes have the stated upper bound; sharpness is explicitly restricted to r>=3 in the final manuscript. | Verified |
| C04 | 72-78 | ChoiGanLiZhu2025 | Theorems 1.1-1.2, p.2. The r>=3 hypothesis, equivalence under renaming, unique shortest representative and exact next-layer formula agree. | Verified |
| C05 | 78-80 | ChoiGanLiZhu2025 | Lemma 3.5, pp.4-5. Its general first-letter-multiplicity count includes multiplicity four, length 2r+2 and all other letters twice. | Verified |
| C06 | 80-82 | GaneshXiaYing2024 | Introduction lines 49-51; Sections 3-4. The cited topics are image membership and preimages/fertility; no insertion theorem is attributed to this source. | Verified |
| C07 | 120-138 | Xia2024 | Lemma 3.1, p.5. The journal groups first-letter runs. Expanding them into individual occurrences introduces empty segments and gives exactly the manuscript form. | Verified |
| C08 | 140-149 | Xia2024, ChoiGanLiZhu2025 | Proof of Theorem 3.1 p.5; Choi et al. Corollary 2.1 p.3. Clump persistence and the first-unclumped-letter argument give the stated bound; both direct citation keys were checked. | Verified |
| C09 | 256-262 | Zeng2026MultiplicityArxiv | Section 4 final paragraph; primary HTML lines 131-134. Integer dynamic programming is checked by direct edge-subset enumeration at small orders; the text expressly says diagnostic, not used in the proof. | Verified |
| C10 | 329-334 | ChoiGanLiZhu2025 | Corollary 2.2, p.3. The source gives C(phi^i(p))=i along a maximal-time trajectory, including i=0,1. | Verified |
| C11 | 346-357 | ChoiGanLiZhu2025 | Proposition 3.1, p.3. The exact truncated-output identity is stated. Equality of sorting times is the manuscript's explicit elementary consequence. | Verified |
| M01 | 30-42 | Local result/scope | claim.json; audit/math.md, Scope and integrity. All arbitrary-marker quantifiers, two repeated profiles, lower alphabet bound and computer-assisted base match accepted scope. | Verified |
| M02 | 89-101 | Local result/scope | claim.json; evidence/clumped-marker-theorem.md, Exact statement. Adjacent old repetitions and empty insertion set are expressly accepted. | Verified |
| M03 | 103-109 | Local result/scope | evidence/clumped-marker-theorem.md, Scope; audit/math.md. Only maximal-time equality is asserted, consistent with accepted boundary examples. | Verified |
| M04 | 110-112 | Local result/scope | source.md; claim.json; audit/math.md. The original classification and count are not supplied; unresolved status is maintained. | Verified |
| M05 | 54-68 | Local result/scope | manuscript/main.tex definition; audit/math.md, stack map reconstruction. A stack pass reverses sorted blocks; aba is palindromic. These immediate consequences do not use external statistics. | Verified |
| M06 | 152-171 | Local result/scope | evidence/clumped-marker-theorem.md, Elementary dependencies item 3. The manuscript repeats the accepted induction proving clumped deletion commutation and its iterates. | Verified |
| M07 | 173-178 | Local result/scope | evidence/clumped-marker-theorem.md, Elementary dependencies items 2-3. Deletion monotonicity and the number of potentially unclumped old letters give both inequalities. | Verified |
| M08 | 185-216 | Local result/scope | evidence/clumped-marker-theorem.md, item 4; audit/math.md, marker reduction. Arbitrarily many marker blocks are reduced to occupied gaps by the accepted stack argument, not inferred from finite tests. | Verified |
| M09 | 220-227 | Local result/scope | evidence/clumped-marker-base.json; audit/release-verification.json. Both multinomial quotient counts agree with all 120 recomputed representatives. | Verified |
| M10 | 228-245 | Local result/scope | audit/release-base-output.json; audit/release-verification.json. All six data columns in both table rows and the zero-failure claim match the exact rerun and accepted certificate. | Verified |
| M11 | 247-254 | Local result/scope | manuscript/verify_base.py; audit/release-verification.json. The complete executed verifier uses literal forbidden triples and interval sortedness; all two-pass marked cases are checked. | Verified |
| M12 | 264-270 | Local result/scope | evidence/clumped-marker-base.json, methods; audit/referee-checks.json. The original record lists three implementations. The accepted referee used a distinct labelled-word generator. No statistical independence or human review is claimed. | Verified |
| M13 | 275-298 | Local result/scope | evidence/clumped-marker-theorem.md, Induction; audit/math.md. The manuscript preserves the old-letter multiplicities and applies induction only from r>=4 to r-1>=3. | Verified |
| M14 | 305-316 | Local result/scope | claim.json; evidence/clumped-marker-theorem.md, Corollary B. The terminal-marker corollary has the exact accepted profile and r>=3 hypotheses. | Verified |
| M15 | 318-366 | Local result/scope | claim.json; evidence/clumped-marker-theorem.md, application; audit/math.md. The application remains restricted to k>=4 and concludes only the accepted deletion reduction. | Verified |
| M16 | 336-344 | Local result/scope | evidence/clumped-marker-theorem.md, application paragraph. The same first-letter recursion argument establishes an adjacent equal pair whenever a repetition exists. | Verified |
| M17 | 368-371 | Local result/scope | source.md; claim.json; manuscript proposition. No inverse-image enumeration or M_k formula is supplied or claimed. | Verified |
| M18 | 375-388 | Local result/scope | audit/release-verification.json, boundaries_recomputed. All six sorting times were freshly recomputed and match the displayed table exactly. | Verified |
| M19 | 390-395 | Local result/scope | evidence/clumped-marker-heldout.json; audit/referee-checks.json; audit/release-verification.json. The held-out counts sum exactly to 58905; the referee record has 480 expanded-marker inputs. The release does not claim to have rerun those larger corroboration suites. | Verified |
| M20 | 413-422 | Local result/scope | manuscript/verify_base.py; audit/release-verification.json. The generator uses labelled ternary words of lengths 6 and 7 and produces 120 representatives. Exception checks remain enabled under optimization; the printed code matches the companion program. | Verified |
| L01 | 103-109 | Local result/scope | audit/release-sources/final-primary-replay.json; audit/math.md, Primary-source comparison. Fresh targeted queries and the compared primary texts yielded no equivalent theorem in this bounded screen. This is explicitly not a priority or universal open-status assertion. | Verified |

## Exact computation, visual values and limitations

The printed verifier was executed and reproduced all 28,800 inputs and 120 representatives, matching every case in the accepted base and referee certificates. The table's rows are exactly `(15,128,1920,1,128)` and `(105,256,26880,12,3072)`. All six boundary sorting times were recomputed. The held-out sum 58,905 and the separate count 480 were checked against their original records; their complete suites were not reexecuted in release and remain corroboration rather than proof premises.

The manuscript still states the accepted arbitrary-clumped-insertion theorem for r>=3, exactly two copies of each old letter with at most one third copy, including adjacent old repetitions, an empty marker set, arbitrary finitely many new letters and arbitrary positive block multiplicities. Its application remains k>=4. It does not claim equality of submaximal times, an all-k inverse-fiber classification, or a formula for M_k. The literature statement is a bounded comparison, with no priority claim.

All seven rendered pages were actually viewed; the finite-base table on page 4 and boundary table on page 5 agree with their exact evidence. The final text-only clarification changed only page 4, which was viewed again; all other final page images are byte-identical to the images already inspected. Code, equations, citations, reference list and fonts are legible, with no clipping or overlap.

## Mechanical outcomes

The final clean latexmk build succeeded. Final TeX/BibTeX logs contain no undefined citations, undefined cross-references, duplicate entries, warnings, overfull or underfull boxes. The bibliography checker reports five cited keys, five matching auxiliary keys, zero missing keys and one deliberately preserved uncited entry. The hook-compatible `validate_selection` function passed against the exact runner-issued identity. The runner-owned pre-publication hook was not invoked.
