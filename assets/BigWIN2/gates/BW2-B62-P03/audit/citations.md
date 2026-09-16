# Citation and bibliography audit

## Scope and method

Search-mode verification was performed on 2026-09-07 using the required two-stage protocol. Stage 1 extracted ten manuscript claim clusters, citation keys, and source locations without assigning verdicts; that frozen ledger is `audit/citation-claim-ledger.json` (SHA-256 `38499efb9fca4c79831812856fca45bb0585f85282e7fc3801001e07770fe97b`). Stage 2 then checked the two cited works against their primary online records and exact nearby passages, and checked the computational claims against the accepted frozen mathematical record. No subagents were used because this bounded job expressly prohibited agents and parallel Codex workers.

The cited-key surface is complete: `AdinBagnoRoichman2026` occurs at manuscript lines 59 and 215, and `ZengEtAl2026FiniteCertificates` at line 82. Both entries exist uniquely in `manuscript/references.bib`, both occur in the converged `.aux` and `.bbl`, and there are no uncited bibliography entries. No citation key changed and the bibliography required no correction.

## Primary-source verification

### `AdinBagnoRoichman2026`

- Record: Ron M. Adin, Eli Bagno, and Yuval Roichman, *Conjugating full cycles by adjacent transpositions: diameter and sorting time*, arXiv:2601.12597v2 (2026), arXiv-issued DOI `10.48550/arXiv.2601.12597`.
- Authority and metadata: the official arXiv record at <https://arxiv.org/abs/2601.12597> gives the exact title and authors, initial submission 18 January 2026, revision 3 September 2026, classification `math.CO`, DOI, and the comment “to appear in Electron. J. Comb.” The local primary PDF has SHA-256 `de5de1f1ddaec97f2f0bc784107c8f9fb27787242e459cd5b3387b34dfc3aa9b`, matching the immutable problem statement.
- C02: verified exactly/paraphrase. Definitions 1.1 and 1.3 (paper pp. 1--2) define the graph diameter and Coxeter cyclic sorting time used by the manuscript.
- C03: verified exactly/paraphrase. Remark 3.1 (p. 2) identifies the graph with the stated Schreier graph; Theorem 1.5 (p. 2) and Sections 4--6 give general upper and lower bounds.
- C04: verified exactly. The introduction (p. 2) states `Diameter(Gamma_5)=5>4=Sort_5`. Section 7, equation (7.1) and the sentence immediately following it (p. 10), state the proposed sorting formula and that it was verified for every `n<=12`; the accepted referee audit independently evaluates the paper's displayed construction at `n=6,7,8` as `6,10,13`.
- C09: verified exactly/paraphrase. Section 7 labels Conjecture 7.1 as asymptotic and Conjecture 7.2 as unimodality, so the manuscript's explicit non-implication and reproduction statements are correctly limited.

Mandatory academic search variants were run for author/year/title words, full title restricted to arXiv/Semantic Scholar, author/year/venue, DOI, and arXiv identifier. The arXiv record and its original full text were used for the verdict; secondary hits were not used as evidence.

### `ZengEtAl2026FiniteCertificates`

- Record: Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org version 1 (posted 24 August 2026), DOI `10.20944/preprints202608.1658.v1`.
- Authority and metadata: the official full record at <https://www.preprints.org/manuscript/202608.1658> gives the exact title, four authors, submission and posting dates, version, preprint status, and full text.
- C05: verified as a close methodological paraphrase. Section 3 states that a standard-library verifier independently re-enumerates the maximal cliques, reconstructs the full group action, and checks the stored certificate. Section 4 states that a separate list-based exact maximum-clique implementation reconstructs the graph independently. Section 6 identifies the separate verifier files, exact reconstruction tasks, integer/rational arithmetic, hashes, software, and replay information; Section 7 limits the conclusions to the finite libraries. The citing manuscript explicitly says the mathematical problems are unrelated.

Mandatory academic search variants were run for author/year/title words, the full title on primary/academic domains, author/year/venue, and the DOI. The official Preprints.org full text was used for the verdict. The registry supplied only the candidate lead; its title, authors, DOI, version, and relevant passages were independently checked before retention.

## Frozen-claim verification results

| ID | Evidence used | Verdict | Confidence |
|---|---|---|---|
| C01 | accepted `audit/math.md`; frozen dual-verifier records | Verified | exact |
| C02 | Adin--Bagno--Roichman, Definitions 1.1 and 1.3 | Verified | paraphrase |
| C03 | Adin--Bagno--Roichman, Remark 3.1 and Theorem 1.5 | Verified | paraphrase |
| C04 | Adin--Bagno--Roichman, introduction and Section 7; accepted referee evaluation | Verified | exact |
| C05 | Zeng et al., Sections 3--7, especially Section 6 | Verified | paraphrase |
| C06 | `evidence/computation_certificate.md`; `audit/referee_check.json` | Verified | exact |
| C07 | same frozen records; every displayed integer matches | Verified | exact |
| C08 | same frozen records and snapshot hashes | Verified | exact |
| C09 | Adin--Bagno--Roichman, Section 7 | Verified | paraphrase |
| C10 | accepted referee replay of every submitted path | Verified | exact |

Totals: 10 extracted claim clusters; 10 verified; 0 numerical errors; 0 unverified claims; 0 hallucinations; 0 misleading claims. The manuscript does not strengthen the accepted mathematical scope.

## Coverage and necessity

The bibliography is not user-library-only. The arXiv primary paper is necessary for the problem origin, exact definitions, closest prior finite computation, general bounds, and conjecture scope. The selected user-library paper is necessary only for the narrowly worded methodological analogy. The manuscript's BFS, conjugation lemma, exhaustive coverage, histograms, hashes, and path checks are proved or documented directly and do not naturally depend on additional literature. A second library citation would support no new nearby claim and was therefore rejected as padding. Both retained citations have ordinary body-flow `\cite{FinalKey}` use through the canonical `manuscript/references.bib`.

## Mechanical audit

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reports two cited keys, two bibliography keys, no missing bibliography files, no missing cited keys, no uncited entries, and exact `.aux` agreement. The clean BibTeX build converged with no undefined citations, undefined references, missing database entries, duplicate entries, BibTeX warnings, or LaTeX errors. The generated `.bbl` contains both verified entries.

Overall citation status: **accept**.
