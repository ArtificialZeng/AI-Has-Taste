# Verification Report

**Mode:** Two-stage source verification: live primary sources and explicitly version-qualified local author manuscripts.
**Document:** `manuscript/main.tex` and canonical `manuscript/references.bib`.
**Generated:** 2026-09-12T23:39:25.527352+00:00.
**Release job:** `primary-20260913-inversion214-release-94470355a3b8`; citation attempt 1; launch `f531765a-3cca-4f33-b3e2-dc1e1f92b1f6`.

| Metric | Count |
|---|---:|
| Fixed claim units checked | 37 |
| Ordinary body citation keys / bibliography entries | 6 / 6 |
| Verified within stated scope | 37 |
| Unsupported, misleading, numerical-error or missing-source claims retained | 0 |
| Selected library references | 1 |
| Natural non-library references in body flow | 5 |

**Overall status:** PASS for source support, bibliography coverage and preservation of the accepted partial theorem. This is a release audit, not a new mathematical acceptance or exhaustive novelty certificate. The original non-algebraicity problem remains unresolved.

## Extraction, scope and repairs

The full manuscript was read before Pass 1 froze 37 substantive claim units. Pass 2 separately checked each fixed unit in id order against primary passages or accepted exact evidence. After scope-preserving syntax repairs the extraction was renewed, and all final units were replayed against those locators. `audit/citation-claim-verification.json` records each result and the final ledger hash. The union of ledger keys exactly equals all six ordinary body keys. There are no hidden conditionals, inert citation macros, nocite substitutes, comments or verbatim citations counted as body evidence. The canonical bibliography is the only bibliography input; no figure or additional TeX dependency exists.

Six retained records were verified. No citation key was renamed and no reference was added or removed. In `manuscript/references.bib`, the selected local-author entry gained the exact DOI field from the saved authoritative registration; its explicit hosted-version disclaimer remains. In `manuscript/main.tex`, the same library claim was separated into a compact direct citation sentence, source locators were preserved in the following prose, and an unsupported decorative boxed wrapper was removed. No theorem, equation content or mathematical evidence changed. The final hook-compatible selection validator passes; its initial boxed-command rejection and correction are documented in `audit/user-bibliography-validation.json`. Neither the configured hook nor publish was invoked.

The active 49-entry first-sheet registry and manifest were read and screened, with their workbook/registry binding recomputed by the installed validator. Row 6 is the closest relevant entry: it illustrates a precise two-basis obstruction beside this paper's unresolved unrestricted non-algebraicity question. Row 40's actual source passages were also checked, but its analytic parity estimates are not developed here, so it was not added. Library metadata alone was never support. The five non-library sources below cover problem origin, closest prior results and the two nontrivial methods; the bibliography is neither library-only nor padded. No extra source is needed for the self-contained append criterion or the directly proved algebraic manipulations.

The requested citation skills were applied in this fresh context. The user explicitly prohibited agents, so the per-citation audit was performed serially by this worker; no agent, external Codex process or background worker was spawned. Applicable academic search templates (author/year/title, full title in scholarly/arXiv search, author/year/venue, supplied DOI and arXiv identifiers) were executed and logged. Search snippets were used only to discover primary records. Exact source passages and version limitations control the decisions. Searches have bounded recall and do not prove absence of other results.

## Source-by-source audit

| Key | Verified record and exact locator | Nearby use and necessity | BibTeX/key action; limitation |
|---|---|---|---|
| BrittBeaton | [Completing the enumeration of inversion sequences avoiding triples of relations](https://arxiv.org/html/2512.21943v2), arXiv:2512.21943v2, 3 August 2026; Table 1, class 214 row and starred-pattern caption; Section 3.5, printed p.18, equations (3.31)-(3.33) and the extraction sentence | Problem origin and the central inherited combinatorial input; not a library citation. | Retained verified entry and key; explicitly cites v2 rather than assigning the first-version year to v2. Only the specified input/comparison is used; numerical asymptotics and the source non-algebraicity belief are not proved results. |
| MartinezSavage | [Patterns in Inversion Sequences II: Inversion Sequences Avoiding Triples of Relations](https://cs.uwaterloo.ca/journals/JIS/VOL21/Martinez/mart2.pdf), Journal of Integer Sequences 21, Article 18.2.2; Introduction, relation-triple definition; Table 3, printed p.8, class 214 row | Origin of the relation-triple classification and label; not a library citation. | Retained verified journal metadata and key. The incorrect older pattern list is expressly excluded from the support attributed to this paper. |
| Mansour | [Inversion sequences avoiding a set of length-3 patterns](https://math.colgate.edu/~integers/y76/y76.pdf), Integers 24, A76; published 16 September 2024; Title page; Table 2, class 44, printed p.45; Theorem 13 and proof, printed p.57 | Closest earlier classification and generating-tree results; not a library citation. | Retained verified entry and key; no unnecessary metadata fields invented. No claim to have audited the full 112-page article or all equivalent encodings. |
| Prodinger | [The Kernel Method: A Collection of Examples](https://www.mat.univie.ac.at/~slc/wpapers/s50proding.html), Seminaire Lotharingien de Combinatoire B50f, 19 pp.; final journal version 13 May 2004; Journal primary abstract; Author copy https://www.finanz.math.tugraz.at/~prodinger/kernel.pdf, p.1 abstract and introduction | Attribution of the nontrivial established kernel-substitution method; not a library citation. | Retained verified journal metadata and key. The journal PDF text extraction was garbled, so the readable journal abstract and author copy support the general attribution. The author copy has 17 pages and is not represented as the 19-page journal file. No present quotient or theorem numbering is attributed to this source. |
| Gessel | [Lagrange Inversion](https://arxiv.org/pdf/1609.05988), Journal of Combinatorial Theory, Series A 144, 212-249; author-deposited arXiv:1609.05988v1 inspected; Theorem 2.1.1, equation (2.1.1), printed p.2; Section 2.3, printed p.5, Catalan substitution | Nontrivial conversion method used by the independent exact verifier; not a library citation. | Retained verified author/title/year/volume/pages/DOI and key. The named theorem locator is in the inspected author-deposited version, whose publication metadata identifies the cited journal article. |
| ZengSquareRoot | [A Square-Root Obstruction to the k=4 Phylogenetic-Network Enumeration Conjecture](https://api.crossref.org/works/10.2139/ssrn.7379478), Local author manuscript dated 29 August 2026, 7 pp.; SSRN-hosted correspondence unverified; Theorem 1.1 p.2; EGF definition (3) p.3; Lemma 3.1/Corollary 3.2 p.4; Lemma 4.1 and ensuing proof p.5 | Selected active library row 6 naturally supports the scope distinction in the limitations paragraph. | Retained the unpublished local-version entry and final key; added only the exact recorded DOI field, with the related-registration and hosted-version disclaimer unchanged. Registration checked through supplied official Crossref capture; primary text checked in the disclosed local copy. Fresh public opens returned Internal Error. Neither historical transaction authentication nor SSRN full-text identity is asserted. Source proofs/certificates were not re-refereed. |

## Claim-by-claim findings

All id locations and direct citation keys are in the fixed UTF-8 schema-version-1 ledger. Mathematical rows below confirm preservation of the accepted proof and exact recorded ranges, not mathematical truth inferred from a citation flag.

| ID | Status and exact supporting locator | Check |
|---|---|---|
| C01 | Verified: claim.json; audit/math.md steps 2-6; evidence/quotient-proof.md | The abstract states only the accepted explicit quotient, formal convergence and exact all-m contact. |
| C02 | Verified: claim.json; audit/math.md accepted scope | Unresolved refers to the original non-algebraicity task; no global priority certificate is implied. |
| C03 | Verified: MartinezSavage Table 3 p.8; direct reduction of the two inequalities; BrittBeaton Table 1 | The two >= relations and label 214 agree. The six patterns follow directly from the inequalities, not the older erroneous annotation. |
| C04 | Verified: BrittBeaton Table 1, starred class 214 row and caption | The source explicitly flags the old pattern-set annotation as wrong. |
| C05 | Verified: BrittBeaton Section 3.5 p.18, equations (3.31)-(3.33) | Rule and auxiliary equation are prior; the section leaves the generating function unsolved. |
| C06 | Verified: Mansour Table 2 class 44 p.45; Theorem 13 and proof p.57 | The target B_210 belongs to the five listed sets; the proof displays the tree rules. |
| C07 | Verified: Prodinger journal abstract and author-copy p.1; claim.json | Kernel substitution attribution is supported. The boundary evaluation and error formula are the present accepted contribution, not a theorem attributed to Prodinger. |
| C08 | Verified: source.md; claim.json; manuscript formal conventions | The unresolved original question and formal rather than analytic scope are preserved. |
| C09 | Verified: audit/math.md step 3; direct substitution into X=z(1+X)^2 | Correct small branch and initial coefficients; no numerical approximation. |
| C10 | Verified: claim.json; audit/math.md steps 4-6; evidence/quotient-proof.md | The theorem agrees with the accepted exact statement, including integral summands, orders, field membership and error sign. Removing a decorative box did not alter it. |
| C11 | Verified: Theorem 1 contact formula; evidence/quotient-proof.md exact statement | Agreement through degree m+2 gives max(0,N-2); no speed claim. |
| C12 | Verified: audit/release-count-crosscheck.json; audit/math.md step 6 | Initial coefficients 1,1,2,4,10,26,73,214,651 agree with independent counting; F0=1+X has first excess one at degree three. |
| C13 | Verified: BrittBeaton Section 3.5 p.18; audit/math.md step 1 | Zero-exception class and run labels match; three runs force a forbidden triple. |
| C14 | Verified: BrittBeaton equation (3.31); audit/math.md step 1 | All four transition ranges, root and parent-recovery explanation preserve the accepted combinatorial construction. |
| C15 | Verified: BrittBeaton extraction sentence after (3.31); audit/math.md steps 1-2 | p<=2 and s=0 are precisely the target; empty and length-two normalizations agree. |
| C16 | Verified: BrittBeaton equation (3.33); manuscript equation (13) | Term-by-term multiplication by y-x is exact, with both signs and the x^2 term preserved. |
| C17 | Verified: audit/math.md step 2; evidence/quotient-proof.md boundary derivation | Substitution is made after denominator clearing in the formal polynomial-coefficient ring; rational simplification and cancellation match the accepted proof. |
| C18 | Verified: audit/math.md step 2 | Coefficient extraction gives zd=(1-z)c-z and F=c/z; c starts at z. |
| C19 | Verified: audit/math.md step 3 | Kernel substitution uses the undivided equation; q,b and integral small-root normalization are unchanged. |
| C20 | Verified: audit/math.md step 4 | Initial W term and both regularization identities match the accepted algebra. |
| C21 | Verified: audit/math.md step 5 | Orbit/product orders and unit inverses give integral summands with leading signs -1,+1 and growing valuations. |
| C22 | Verified: audit/math.md step 6 | Finite iteration includes m=0 and D_-1=1. |
| C23 | Verified: audit/math.md step 6 | W(t_m) has order 2m+6; dividing by the m-factor product gives m+6 with leading coefficient one. |
| C24 | Verified: V(0)=1; manuscript orbit/product definitions; evidence/triage-kernel.md | For the manuscript indexing, V(t_m) is a unit and D_(m-1) has order m, so the unregularized tail has order -m. The older index-shifted form is not substituted. |
| C25 | Verified: audit/math.md step 6 | b=cq+W(q)=A+cL implies the accepted quotient and integral normalized units. |
| C26 | Verified: audit/math.md step 6 | Retaining the finite remainder gives the exact positive leading error, including m=0, and finite algebraic/integral membership. |
| C27 | Verified: audit/math.md step 7 | The least-z-degree uniqueness proof in Q[x][[z]] matches acceptance; combinatorial existence is inherited, not assumed for an arbitrary rational function. |
| C28 | Verified: evidence/quotient-check.json; audit/referee-check.json; audit/release-count-crosscheck.json | Ranges 0..40 and 0..48, and exclusive w precision 120, agree exactly with the records and fresh independent counting. No all-orders conclusion is inferred from these ranges. |
| C29 | Verified: Gessel Theorem 2.1.1 equation (2.1.1) p.2; Section 2.3 p.5 | R(w)=(1+w)^2 and n>=1 give the displayed sum by expanding the derivative; the independent-z restriction is explicitly satisfied. |
| C30 | Verified: source.md definition; audit/math.md step 1; audit/release-count-crosscheck.json | Every new forbidden triple ends at the appended value, giving exactly the two-largest-with-multiplicity criterion and position bound. |
| C31 | Verified: evidence/quotient-check.py literal_definition(9); audit/referee-check.py exhaustive_counts(9); corresponding JSON records | The reported exhaustive range is precisely through length nine. These two historical literal enumerations were read and not represented as rerun in this release. |
| C32 | Verified: audit/referee-check.json contact_checks and orders arrays | Contact checks run from m=0 to45 and order checks from j=0 to47; every listed error degree/coefficient and range matches the manuscript. |
| C33 | Verified: literature/research-live-screen.md; audit/math.md bounded comparison; audit/release-web-evidence.json | The novelty wording is confined to inspected sources/searches. The calendar date 13 September is Asia/Shanghai, equivalent to the current 12 September UTC; no exhaustive priority assertion or newly solved non-algebraicity claim appears. |
| C34 | Verified: claim.json; evidence/quotient-proof.md limits; manuscript statements | Limits of algebraic approximants alone do not force an algebraic limit, and the paper asserts no analytic/asymptotic conclusion. Non-algebraicity remains unresolved by this work. |
| C35 | Verified: ZengSquareRoot local author manuscript Theorem 1.1 p.2, (3) p.3, Corollary 3.2 p.4, Lemma 4.1/proof p.5 | The exact 5/16 coefficient, EGF meaning, two factorial bases and all-ell>=5 restriction agree. The short direct citation sentence is supported by the same precise local passages. |
| C36 | Verified: ZengSquareRoot cited local version and bibliography note; audit/release-recovery-verification.md | The restriction is to two specified bases. The version is explicitly local/datable; no SSRN-hosted identity or transferable non-algebraicity criterion is claimed. |
| C37 | Verified: audit/math.md; audit/referee-check.py/.json; evidence/research-provenance.json | The assistance disclosure and SymPy 1.14.0 correspond to the recorded research/referee artifacts. It expressly excludes human peer review, statistical independence and proof-assistant certification. This release spawned no agents by user instruction. |

## Recovery scope and access

`audit/release-recovery-verification.md` independently binds the exact requested recovery note and all four named source artifacts. The saved Crossref responses were parsed for exact DOI endpoints, recorded 200/ok status, UTC provenance and deposited metadata/abstract scope. Their historical HTTP transactions were not newly authenticated. The two primary local PDF passages were independently read. Current Crossref/SSRN tool opens returned Internal Error; this did not erase the saved authoritative evidence and did not establish an HTTP error code, nonexistence or a mathematical defect.

The selected citation is specifically to the seven-page local author manuscript dated 29 August 2026. Correspondence with an SSRN-hosted PDF remains unverified and is disclosed in the bibliography. The source only supplies the named two-factorial-basis comparison. No source proof/certificate, universal non-algebraicity criterion or Class 214 transcendence result is being certified here. These limits are sufficient for the actual nearby claim; no unsupported strengthening remains.

## Build and visual corroboration

A fresh clean latexmk/pdfLaTeX/BibTeX build succeeded. The final log and .blg have no undefined citation/reference, missing database entry, duplicate entry, fatal error, or over/underfull box warning. The installed bibliography checker confirms exactly six cited, six defined, and six aux-bound keys, with no unused or missing entry. Every final PDF page 1-6 was rendered and actually viewed; bibliography text, source qualifiers and equations were checked. Details are `audit/build.md` and `audit/visual.md`. All release audits use the same current manuscript/PDF snapshot. Checkpoint, source, claim and every frozen mathematical input remain unchanged.
