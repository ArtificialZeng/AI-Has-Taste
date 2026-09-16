# Verification Report

Mode: fresh primary-source search and two-stage non-interactive audit.
Document: `manuscript/main.tex`; bibliography: `manuscript/references.bib`.
UTC verification date: 2026-09-12. Release job: `newwin-00001-p02-release-80f7dac713d2`.
Citation attempt: 1; launch: `f22893c6-0874-48bc-9192-d8660ab74e59`.

**PASS.** 24 frozen claims checked; 8 ordinary body citation occurrences;
4 distinct references verified. No unsupported citation, numerical discrepancy,
undefined citation, hidden-only citation, or unresolved claim-support blocker.
One active-library reference and three non-library primary references are used.

The extraction was saved before source verification. Presentation-only repairs
were followed by a final extraction with the same 24 claim texts, locations and
key pairs. Pass 2 then checked this fixed list. No interactive confirmation or
delegation was used because the user expressly required a non-interactive,
single-worker job. The initial and final extraction records remain inspectable.

## Citation and bibliography coverage

| Key | Exact nearby use | Primary text and metadata | Action |
|---|---|---|---|
| CsakanyWaldhauser2000 | Origin of ordered spectra; Sheffer reconstruction method | [Author PDF](https://www.math.u-szeged.hu/~twaldha/cikkek/2000_2.pdf), Sections 1 and 4.2; [institutional record](https://publicatio.bibl.u-szeged.hu/17341/) | Verified, unchanged |
| HuangLehtonen2023 | Variable-permutation scope; depth-congruence comparison | [Author v2](https://arxiv.org/pdf/2202.11826v2), introduction and Section 7; [publication record](https://novaresearch.unl.pt/en/publications/the-associative-commutative-spectrum-of-a-binary-operation/) | Verified, unchanged |
| HuangLehtonen2024 | SC258 table, nine finite values, original question and limits | Frozen complete journal PDF, pp. 1 and 17; [live primary Section 7](https://arxiv.org/html/2401.15786v1#S7) | Verified, unchanged |
| Zeng2026MultiplicityArxiv | Precisely qualified weighted-tree reconstruction comparison | [Official Lemma 3.1](https://arxiv.org/html/2608.18179v1); [author/version/DOI record](https://arxiv.org/abs/2608.18179) | Verified; citation optional note moved into text; key unchanged |

The source-verification JSON records exact titles, authors, versions, publication
data and passage locators. Existing BibTeX entries match the verified records;
no BibTeX export was substituted, no metadata was invented, and no key changed.
The 2000 journal date is distinguished from the 2011 arXiv upload; the Zeng
record is identified as a 2026 preprint by Zijian Zeng.

The journal PDF for Huang-Lehtonen 2024 and its arXiv related-DOI field print
different DOI suffixes. The bibliography asserts neither conflicting DOI and
uses the unambiguous primary journal URL and matching article metadata.
This is an explicitly recorded identifier omission, not a missing-support claim.

All 49 active registry titles were screened. Row 17 is the closest verified
library comparison: recovery of a tree from invariant data. Its three-vertex
minimum and nonleaf multiplicity condition are retained. The comparison is
not a dependency of the SC258 proof. The three non-library sources naturally
cover the problem origin, closest finite result, definitions and related
structural methods. The single library selection is not a bibliography cap.
No decorative or quota-driven addition is needed. The formal-series algebra
and complete table evaluator are elementary and described in full; no uncredited
external nontrivial theorem or software method is used.

The bounded current search found no later equivalent resolution in its relevant
hits. This supports comparison with inspected work only, not exhaustive priority.
Shell network requests were denied; all four primary texts were available through
the web tool, and the full frozen journal PDF was read locally. No supervisor
revision/handoff leads or Crossref captures existed. Search queries and source
locations are saved under `audit/`.

## Fixed claim verification

| ID | Status | Source or accepted-evidence location | Finding |
|---|---|---|---|
| C01 | Verified | claim.json; evidence/pruning-proof.md, Sections 1-4; manuscript Theorem 1 | The abstract matches the accepted all-arity recurrence and exact pruning classification. |
| C02 | Verified | CsakanyWaldhauser2000, Section 1, author PDF pp. 1-2 | Historical attribution and fixed-order definition agree. |
| C03 | Verified | HuangLehtonen2024, journal p. 17, SC258 table | All nine entries and row/column orientation agree. |
| C04 | Verified | HuangLehtonen2023, author PDF p. 1 | The source explicitly permits arbitrary variable order in full linear terms. |
| C05 | Verified | HuangLehtonen2024, journal p. 17, Section 7 | All nine integers, the finite Padovan comparison, and request for general determination agree. |
| C06 | Verified | claim.json; evidence/pruning-proof.md, Sections 1-4; audit/math.md | The theorem, initial conditions, formal series, quantifiers and equivalence match the accepted scope. |
| C07 | Verified | CsakanyWaldhauser2000, author PDF p. 7, Section 4.2 | The essentiality and factor-recovery argument is present. The manuscript does not assert its surjectivity hypotheses for SC258. |
| C08 | Verified | HuangLehtonen2023, author PDF pp. 19-20, Section 7, (7.1.1) | Leaf-depth congruence is expressly used as the term-function equality criterion for the operations studied there. |
| C09 | Verified | HuangLehtonen2024, Section 7; claim.json; manuscript Sections 2-3 | The comparison is limited to inspected finite data versus the accepted all-arity classification. |
| C10 | Verified | evidence/pruning-proof.md, Section 1; manuscript Lemma 2 | The preservation, first-leaf and composite-child invariants are unchanged. |
| C11 | Verified | source.md operation table; evidence/pruning-proof.md, Section 1 | Every operation output is Boolean and the Boolean subtable is left projection. |
| C12 | Verified | evidence/pruning-proof.md, Section 2, Lemma 1; manuscript Lemma 3 | The statement preserves arbitrary increasing distinct labels and both directions of essential-support equality. |
| C13 | Verified | source.md operation table; evidence/pruning-proof.md, Section 2 | Direct evaluation confirms (0,1,1-g) and (g,g,0); complements apply only to Boolean composite children. |
| C14 | Verified | evidence/pruning-proof.md, Section 2, Lemma 2; manuscript Proposition 4 | The section test, separate one/two-leaf base cases and recovery restrictions coincide with the accepted proof. |
| C15 | Verified | evidence/pruning-proof.md, Section 2 | The accepted comb-separation lemma explicitly allows arbitrary gaps and unattainable combs. |
| C16 | Verified | Zeng2026MultiplicityArxiv, Section 3, Lemma 3.1 and proof | At least three vertices, multiplicity-one nonleaf weights, and the two input data types are all retained; the analogy is limited to reconstruction. |
| C17 | Verified | evidence/pruning-proof.md, Section 3, Lemma 3; manuscript Lemma 5 | The shifted-interval induction and converse construction are preserved, including exclusion of a suffix of length one. |
| C18 | Verified | evidence/pruning-proof.md, Section 3, identity (1) | The disjoint label-set decomposition, empty-sum convention and n>=2 domain agree. |
| C19 | Verified | evidence/pruning-proof.md, Section 4, identity (2) | The root constructions are disjoint and count forms rather than their raw realizations. |
| C20 | Verified | evidence/pruning-proof.md, Section 4; audit/math.md formal algebra | The formal series identities, denominator with constant term one, n>=4 range and boundary values agree. |
| C21 | Verified | manuscript/verify.py: trees, FullEvaluator, scalar and main; audit/release-verification-replay.json | Code reading confirms complete domains, all root splits and independent scalar lookups through n=7. The fresh replay passes. |
| C22 | Verified | audit/release-verification-replay.json: raw_checks; manuscript/verification-results.json | All ten rows exactly reproduce the recorded and referee results; counts and coverage totals were recomputed. |
| C23 | Verified | audit/release-verification-replay.json: all_subset_combs | All 1644 combs, 6561 assignments per tree, no collisions and full essential supports match exactly. |
| C24 | Verified | HuangLehtonen2024, journal p. 17; claim.json; manuscript Theorem 1 | The companion tables occur in the source and are correctly excluded from the present theorem. |

Theorem and proof claims preserve the accepted mathematical scope; the accepted
proof and referee, rather than citation metadata, justify the universal theorem.
The finite replay reproduced the recorded and referee results exactly, including
all 6,918 bracketings through arity ten and all 1,644 subset combs on eight labels.

## Dependency, build and identity checks

All seven sorted publication source files were read. The TeX recorder shows
only `main.tex` and generated `.aux`, `.out`, `.bbl` project inputs; the sole
authored bibliography is `references.bib`. The README, build script, verifier,
input and recorded output complete the publication dependency scope.
The exact-key checker reports four cited keys, four BibTeX keys, zero missing or
unused entries, and exact `.aux` agreement. The final engine/BibTeX logs have
no unresolved references, citations, font warnings or box warnings.

Formatting repairs replaced unsupported `needspace` controls with standard
page flow, used installed Latin Modern fonts with standard `microtype`, and
preserved the MSC codes in a standard footnote. No accepted mathematical text
or frozen mathematical input changed. The final PDF was rebuilt, refrozen, and
all five pages actually viewed. The hook-compatible selection validator passed;
the runner-owned pre-publication hook was not invoked.

Manuscript digest: `95aa4a634943aa99c9729bb42bd41f9c78b1d3e5b69c8d775a7f6353ade0a63a`.
PDF digest: `47c3e8c55bf25260d8fbaf373cfa13ed5da93bb4264008afdb218d7b4bd48874`.
Accepted mathematical snapshot: `8aca2d76efdb7c298a0274e627621944fae218d10fffef79f7925e9838d80b76`.
