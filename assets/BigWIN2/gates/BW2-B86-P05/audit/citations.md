# Citation verification report

Release job: `win-00086-p05-release-d366fb9aae22`  
Citation attempt: 2  
Launch: `0da254d5-6c1c-41d0-ab9d-c149077d9629`  
Verification date: 2026-09-10 UTC  
Mode: primary-source search verification plus fresh local exact replay

## Stage 1: frozen extraction

The citation-bearing claims were extracted from the complete canonical manuscript before support decisions were recorded. The frozen extraction is `audit/citation-claim-ledger.json`. Its three unique claims cover exactly the four ordinary body-flow keys parsed from `manuscript/main.tex`: `Gordon2023`, `HeRepository2026`, `HeWu2026`, and `ZengEtAl2026Certificates`. Comments, bibliography commands, cross-references, and inert text supplied no keys.

## Stage 2: claim-level primary-source verification

| Claim | Status | Primary source and exact locator | Support decision |
|---|---|---|---|
| CIT-01 | Verified (paraphrase) | Gordon, *Signed difference sets*, Springer publisher page, abstract and “About this article”; <https://link.springer.com/article/10.1007/s10623-022-01171-8> | The publisher record identifies Gordon's article and defines a signed difference set by adding signs to the ordinary group-ring difference-set equation, explicitly describing a generalization. The manuscript's “introduced ... as a signed extension” wording preserves that scope. |
| CIT-02 | Verified (exact/paraphrase) | He--Wu, arXiv:2608.22936v1, equations (2.3)--(2.4), Lemma 2.1, Theorem 4.4, and bibliography item [7]; <https://arxiv.org/html/2608.22936v1>. Official repository README; <https://github.com/zhiwenhe94/sds-open-case-verification> | The paper states the principal and nonprincipal character equations and the near-full-support residues. Direct substitution of `v=9`, `lambda=1`, `h=q=3` gives `10 = 2 (mod 8)`, equal to the allowed residue `q-1`. The paper identifies the accompanying repository, and the live repository documents the fixed snapshot, status semantics, and reproducibility program. The manuscript does not claim that the live database row remains open. |
| CIT-03 | Verified (paraphrase) | Zeng--Liu--Ratnavelu--Ong, Preprints.org version 1, abstract, Section 3 certificate proof, and Section 6; <https://www.preprints.org/manuscript/202608.1658/v1> | The source uses exact integer predicates, exhaustive symmetry/orbit reconstruction, a standard-library verifier, and a separate independent exact implementation. The manuscript expressly limits the comparison to certificate methodology and says the geometric models are unrelated to signed difference sets. |

The applicable author/year/title, full-title, venue, DOI, and arXiv-identifier searches were all run. Support decisions use the Springer publisher record, arXiv full text, Preprints.org full text, and the live official repository, not secondary snippets. The large `sds.json` body itself was not needed because the manuscript makes no live-row-status claim; the repository README directly supports the retained fixed-snapshot and status-semantics wording. The project contains no `literature/crossref-*` supervisor capture.

## Bibliographic identity and coverage

| Key | Identity check | Why retained |
|---|---|---|
| `Gordon2023` | Publisher title, author, journal, volume 91, issue 5, pages 2107--2115, 2023 date, and DOI `10.1007/s10623-022-01171-8` agree with the canonical BibTeX entry. | Foundational primary source for the signed-difference-set definition and attribution; natural non-library source. |
| `HeWu2026` | arXiv title, authors Zhiwen He and Jiayan Wu, submission date, math.CO class, identifier 2608.22936v1, and arXiv DOI agree with the entry. | Closest primary work for the character equations and near-full-support obstruction used in the comparison. |
| `HeRepository2026` | The public repository title, owner, four-commit history, files, fixed-snapshot purpose, status semantics, and counting-code description were checked on GitHub; the immutable mathematical-source binding supplies the exact cited commit `de57332884c7bf417544285dee9a2cbb015a5fae`. | Primary reproducibility source for the database snapshot and status semantics. |
| `ZengEtAl2026Certificates` | Preprints.org confirms the full title, four authors, version 1, 2026 date, venue, DOI `10.20944/preprints202608.1658.v1`, and cited method passages. | Directly supports the one nearby exact-certificate methodology comparison; selected active user-library source. |

This is a claim-driven scholarly bibliography, not a user-library-only bibliography: three ordinary body-flow keys are natural non-library problem-origin, closest-method, and reproducibility sources. Every retained entry supports a nearby sentence; no decorative reference was found. The active 49-entry registry was inspected, and row 9 is the only selected library work because it directly supports an existing method comparison. The canonical source key `202608.1658` and final key `ZengEtAl2026Certificates` identify the same DOI-bound record.

The four cited keys occur exactly once in `manuscript/references.bib`, occur in the final AUX/BBL, and have no undefined or unused entries. No BibTeX block or citation key required replacement. Per-reference verification was performed serially in this fresh release context because the bounded job expressly prohibited spawning agents or other workers.

The live installed hook-compatible selection validator accepted registry row 9 with the exact runner-issued problem, publication-kind, citation-attempt, and launch bindings; it also confirmed the literal body-flow citation context and canonical `manuscript/references.bib` DOI binding.

## Other factual and numerical assertions

The theorem and proof are bound to the accepted mathematical audit rather than external citations. The finite-accounting assertions were freshly replayed with all three supplied exact programs. They again reported 2,304 raw assignments, 504 principal-eligible assignments, 28 normalized pairs, 48 matrices in `GL(2,3)`, orbit sizes 4 and 24, selected norms 25 and 13, and zero solutions. These values match the manuscript exactly. Definitions, proof steps, disclosures, and methodology descriptions were excluded from the citation-claim extraction under the citation-check rules.

## Verdict

Accept. All retained citation-bearing claims are supported at their stated strength, bibliographic identities are verified, bibliography coverage is natural and complete for the manuscript's dependencies, the unsupported live-row wording was removed, and there are no undefined citations or unrestricted priority claims.
