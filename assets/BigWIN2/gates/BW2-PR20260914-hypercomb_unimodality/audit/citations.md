# Verification Report

**Mode:** Primary-source search verification, with a separate frozen extraction pass.
**Document:** manuscript/main.tex and manuscript/references.bib, plus all publication dependencies.
**Generated (UTC):** 2026-09-14T09:05:07.674795+00:00
**Release job:** primary-20260914-hypercomb-unimodality-release-d6e0c44087b7
**Citation attempt:** 1; **launch:** 53d6334a-813b-427a-a5cb-8fa235c8ca67.

| Metric | Count |
|---|---:|
| Claim groups extracted | 25 |
| Verified at the stated scope | 25 |
| Cited works | 8 |
| Selected user-library works | 1 |
| Ordinary body-cited non-library works | 7 |
| Remaining unverified, numerical-error or misleading claims | 0 |
| Scope-preserving wording repairs | 1 |

**Overall status: PASS for this manuscript and citation scope.** The accepted contribution is a result-note. The original full unimodality question remains unresolved here.

The explicitly required mathematics release skill, release phase reference, shared release contract, citation-check skill and bibliography-audit skill were read separately through EOF. User instructions replaced interactive extraction confirmation with a frozen non-interactive ledger, and prohibited agents, so citation verification was performed in this single fresh release context. No agents, other Codex processes, or background research workers were started. This is not external peer review.

## Extraction and verification

The initial 25-group extraction is preserved in audit/citation-extraction-initial.json. Source inspection revealed one small attribution overstatement: the SSRN abstract promises independently checkable certificates; it does not itself establish that a particular independent check was run. Line 351 was changed from “checked” to “checkable.” No mathematics, bibliography fields or citation keys changed. The entire final extraction was rebound before the final claim-by-claim verification recorded in audit/citation-verification.json. The final ledger covers exactly the eight ordinary body-flow keys, using the installed hook-compatible TeX masker; comments, inert macros, nocite and hidden text supply no keys.

Source discovery used the applicable author/year/title, exact-title archive, venue and DOI/arXiv queries. Searches and direct primary passages are saved in audit/source-*.json; audit/citation-source-map.json gives precise locators and capture hashes. Searches checked metadata and source identity; the final decisions use the actual primary text at the cited scope, not search-result rank or title alone. No bibliography-revision files or Crossref supervisor captures were present when enumerated. The only handoff was literature/outer-intake-handoff.md: its definition, endpoint condition, current recurrence and withdrawal warning agree with the journal. The accepted later-preprint comparison supersedes its older literature frontier.

## Bibliography audit and coverage

No reference is a substitute for an unproved step. The article gives its full finite-sequence order proof and cites the origin, nearest comparison and relevant standard methods. The library selection is a minimum selection, not a reference-count ceiling. All 49 first-sheet titles, authors and DOI identities were screened; rows 34 and 42 were read in full as leads. Row 42 is the specific reconstruction-method comparison; row 34 was not added to pad the bibliography. The active workbook and registry were checked by the installed selection validator and bound dynamically. The selected context is exactly the smallest citation-bearing sentence, with UTC verification date 2026-09-14.

| Key | Authors and primary title | Verified publication | Needed nearby use and exact locator |
|---|---|---|---|
| GS | David Galvin; Courtney Sharpe. Independent set sequence of some linear hypertrees | Australasian Journal of Combinatorics 94(1) (2026), 93–121 | Problem origin, exact combinatorial identification, recurrence, factorization and preceding mode estimate. Printed pp. 99–100: Theorem 1.7, Corollary 1.8, Note 1.9, Question 1.10(4); Section 2.5 pp. 112–119, especially (28)–(30) pp. 115–116 and factor condition p. 119. [Primary source](https://ajc.maths.uq.edu.au/pdf/94/ajc_v94_p093.pdf) |
| WZ | Yi Wang; Bao-Xuan Zhu. On the unimodality of independence polynomials of some graphs | European Journal of Combinatorics 32(1) (2011), 10–20; 10.1016/j.ejc.2010.08.003 | Graph-concatenation recurrence factorization is the explicit methodological antecedent. Theorem 3.1 and its proof, preprint p. 6, equations (3.1)–(3.5); publisher record S0195669810001125. [Primary source](https://arxiv.org/pdf/1008.2605) |
| BGG | César Bautista-Ramos; Carlos Guillén-Galván; Paulino Gómez-Salgado. Log-concavity of some independence polynomials via a partial ordering | Discrete Mathematics 342(1) (2019), 18–28; 10.1016/j.disc.2018.09.010 | Identifies related order arguments for graph independence polynomials. Publisher abstract final sentence and ratio-domination keyword; title and publication header. [Primary source](https://www.sciencedirect.com/science/article/pii/S0012365X18303042) |
| BGGcorr | César Bautista-Ramos; Carlos Guillén-Galván; Paulino Gómez-Salgado. Corrigendum to “Log-concavity of some independence polynomials via a partial ordering” [Discrete Math. 342 (1) (2019) 18–28] | Discrete Mathematics 346(12) (2023), article 113608; 10.1016/j.disc.2023.113608 | Documents why support conditions in ratio comparisons matter for the present zero extension. Sections 1–2: counterexample to the original support-endpoint claim, corrected Definition 2.3 and Lemma 2.5. [Primary source](https://www.sciencedirect.com/science/article/abs/pii/S0012365X23002947) |
| DM | Lutz Dümbgen; Alexandre Mösching. On stochastic orders and total positivity | ESAIM: Probability and Statistics 27 (2023), 461–481; 10.1051/ps/2023005 | Standard likelihood-ratio definition, including zero-density cross products. Primary preprint Section 2, Theorem 1(ii), p. 2: g1(y)g2(x)<=g1(x)g2(y) for x<y. Published version uses Theorem 2.1. [Primary source](https://arxiv.org/abs/2209.07868) |
| JG | Oliver Johnson; Christina Goldschmidt. Preservation of log-concavity on summation | ESAIM: Probability and Statistics 10 (2006), 206–215; 10.1051/ps:2006008 | Exact classical convolution-closure result; the note supplies the required interval-support proof. Published Theorem 1.4, printed p. 207; archive publication record and exported BibTeX. [Primary source](https://www.numdam.org/item/PS_2006__10__206_0/) |
| Eventual | OpenAI Codex GPT-6-Astra. Eventual strict log-concavity of weighted linear hypercombs | aiXiv aixiv.260910.000002v1.0, 10 September 2026 | Closest later comparison: fixed-weight sufficiently-large-length log-concavity versus this all-length two-step localization. Equation (1), Theorem 1 and Corollary 2, p. 2; Section 9, pp. 18–19. [Primary source](https://aixiv.science/pdf/aixiv.260910.000002v1.0.pdf) |
| ZengWhiskered | Zijian Zeng. The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices | SSRN preprint, written 1 September 2026, posted 3 September 2026; 10.2139/ssrn.7385138 | Specific comparison of independent exact graph-certificate reconstruction in a related pendant-edge construction. Primary SSRN Abstract, final two sentences; publication header and suggested citation. [Primary source](https://papers.ssrn.com/sol3/Delivery.cfm/7385138.pdf?abstractid=7385138&mirid=1&type=2) |

All eight retained entries have matching authors, substantive titles, publication years and venues/identifiers. The Numdam exported BibTeX agrees with the JG bibliographic fields. Other entries were retained after primary-record and source-text comparison; no unavailable official BibTeX export was invented. No BibTeX replacement was needed; no old-to-new key mapping exists. manuscript/references.bib is unchanged. The regenerated main.bbl and final main.aux resolve all eight keys; audit/bib-key-check.txt reports no missing or unused entries, database gaps or auxiliary mismatch.

Source-access scope matters. BGG is supported only at its publisher-abstract methodological scope. ZengWhiskered is supported only at the primary SSRN abstract and record; the full PDF was not inspected. The DM theorem was checked in its author-posted arXiv PDF; the current primary record supplies its journal DOI. The publisher endpoint returned 403, while the published-paper imprint reproduced in the accessible paper copy confirms pagination. The research-paper text is the primary evidence; no theorem is inferred from mirror metadata. WSL download restrictions did not remove the browser-retrieved primary texts. Eventual is expressly an attributed preprint assertion; its analytic and claimed Lean proofs are not premises and were not audited. The old GS search abstract claiming full log-concavity was rejected against the current journal text.

## Fixed-claim verification

| ID | Manuscript lines | Direct keys | Decision and support |
|---|---|---|---|
| C01 | 20–31 | (self-contained result/evidence) | Verified. Journal Corollary 1.8 and equations (28)–(30); accepted claim exactly matches n>=2,ell>=3, smallest modes, two shifts and unresolved scope. |
| C02 | 46–47 | (self-contained result/evidence) | Verified. The 2n+1 edges cover all vertices and each permits at most one chosen vertex. Choosing one private vertex per edge attains that size. |
| C03 | 49–56 | GS | Verified. Theorem 1.7 and Corollary 1.8 give exactly the stated recurrence and fixed-ell band; Note 1.9 withdraws the old proof and Question 1.10(4) asks to reduce the band. |
| C04 | 65–69 | GS | Verified. At t=ell-1, s=ell-2, expanding z1 gives coefficient 3t^2 at x^2, identical to Theorem 1.7. The n=0 auxiliary convention remains explicit. |
| C05 | 73–77 | GS | Verified. Equation (28) splits into z1 Fn + z0 b F(n-1), because lambda*mu=-b. Equations (29)–(30) give the identical parity factors. |
| C06 | 85–87 | DM | Verified. The source cross-product inequality has the same orientation. Multiplying each sequence by its positive normalization leaves every sign unchanged. |
| C07 | 89–106 | (self-contained result/evidence) | Verified. No change to quantifiers, zero extension, smallest modes or sharpness. Both proof chains are present and the exact witness is reproduced. |
| C08 | 108–110 | (self-contained result/evidence) | Verified. Journal recurrence, factorization and log-concavity are expressly prior. The new simultaneous order comparison is the accepted contribution. This is bounded source comparison, not worldwide priority. |
| C09 | 111–113 | WZ, BGG | Verified. WZ Theorem 3.1 factors graph-concatenation recurrence polynomials. BGG publisher abstract and ratio-domination keyword support only the stated methodological context. |
| C10 | 114–116 | BGGcorr | Verified. Sections 1–2 repair the missing support condition and the support-endpoint lemma. The note retains all-pair minors and independently proves the finite order properties. |
| C11 | 118–126 | Eventual | Verified. At s=ell-2,t=ell-1 equation (1) is identical. Theorem 1 fixes positive weights and only asserts all sufficiently large n. Section 9 preserves the all-length uniform log-concavity question. No source theorem is assumed here. |
| C12 | 130–133 | (self-contained result/evidence) | Verified. Decreasing positive adjacent coefficient ratios pass through 1 at most once; zeros outside the support do not introduce another maximum. |
| C13 | 135–176 | (self-contained result/evidence) | Verified. The endpoint argument, positivity for division in transitivity, paired convolution-minor sum and strict inequality for the smallest tied mode match the accepted proof. No unsupported extension to internally vanishing sequences is made. |
| C14 | 178–183 | JG | Verified. Theorem 1.4 explicitly gives convolution closure. The manuscript states the no-internal-zero convention and proves the needed version via P<=lr xP. |
| C15 | 185–193 | (self-contained result/evidence) | Verified. Linear products and d=a+2x establish the initial factors. The factored Fj and nonnegative recurrence prove the three stated support intervals. |
| C16 | 195–212 | GS | Verified. Expanding (1+tx)Ry recovers a^2+4yb. Both determinant identities agree with the accepted proof; the lower bound at y=1,t=s+1 is s^2(6s^2+4s-1)>0. |
| C17 | 214–229 | GS | Verified. Pairing roots in (lambda^j-mu^j)/(lambda-mu) gives precisely the cosine-square factors with an unpaired a only when j is even. Positive x avoids repeated characteristic roots, then polynomial identity extends it. |
| C18 | 231–235 | (self-contained result/evidence) | Verified. Each factor is log-concave and has interval support; products give log-concavity, and the positive quadratic a fills all degrees through 2j-2. |
| C19 | 240–263 | (self-contained result/evidence) | Verified. The four simultaneous induction comparisons use only kernels already proved log-concave; common-bound addition gives both next-step inequalities. The base minors are exactly 1,t,t^2. |
| C20 | 265–292 | (self-contained result/evidence) | Verified. The z1 versus x^2z0 overlap determinant and the three z0 versus d minors are as accepted. Convolution and transitivity give both target chains without a mode assumption. |
| C21 | 294–308 | (self-contained result/evidence) | Verified. All 24 displayed table entries (including two high-degree zeros in Y) agree exactly with independently generated witness arrays. W and Y unique modes are 6 and 4. |
| C22 | 310–319 | (self-contained result/evidence) | Verified. All adjacent log-concavity differences of the example sum are nonnegative. n=1 is z1. Two monotone tails allow only a strict intermediate valley when separated by two indices. |
| C23 | 325–339 | (self-contained result/evidence) | Verified. Fresh execution produced exactly 388 cases and 958808 all-pair minors in the stated domains, no failures. The coefficient stream matches the referee record; this replay is not another independent algorithm. |
| C24 | 340–347 | (self-contained result/evidence) | Verified. Once attachment occupancy is fixed, n+1-|A| free teeth and h(A) free spine edges give the displayed factor. Fresh exact enumeration reproduced 60 cases on the stated rectangular domain. |
| C25 | 349–353 | ZengWhiskered | Verified. The primary abstract gives integer kernel vectors and independent matrix reconstruction as a way to check them. Revised checkable matches that support exactly; no claim is made that this release worker verified the source theorem or certificates. |

Mathematical statements without external citations were compared against the exact accepted claim, full referee report and the manuscript proof. Finite claims were freshly reproduced with manuscript/verify.py, not promoted to infinite proofs. The single table has no approximate entries: all 24 displayed coefficients match the saved witness, including zero extension; there are no other figures, plots or numerical data visuals. The narrower constant-width interval is specified by summand modes and is not asserted to have a new explicit affine center. Neither sharp summand separation nor failed log-concavity is portrayed as a counterexample to unimodality.

## Dependency, PDF and provenance checks

publication.json lists all authored dependencies: manuscript/main.tex, manuscript/references.bib, manuscript/verify.py, manuscript/README.md and manuscript/build.sh. The source and TeX recorder show no additional authored imports, figures, local style files or dynamic shell-escape inputs. Generated main.aux, main.out and main.bbl are build outputs; the last is generated from references.bib and system plain.bst. System TeX packages need not be copied. Dependency scope is complete.

The final compiler log and BibTeX log contain no fatal diagnostics, unresolved citations/cross-references, repeated entries, layout warnings or other warnings. All six freshly rendered pages and the extracted bibliography were reviewed. This report is bound in audit/citations.json to the current evidence, manuscript and PDF digests. The 16 protected mathematical/input files still match the initial release integrity record. No source.md, checkpoint.md, claim.json, mathematical evidence, accepted math audit or role metadata was edited.

The hook-compatible selection validator passed; its output is audit/selection-validation.json. The configured pre_publish_hook was not invoked, and no runner result.json or citation-prepublish.json was created. The remaining operation is the structural release check, then runner-owned pre-publication hook and publish. These process checks do not certify priority or mathematical truth.
