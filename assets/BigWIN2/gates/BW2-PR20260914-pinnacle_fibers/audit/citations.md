# Verification report

**Verdict: accept at the frozen mathematical scope.**
Mode: two-stage primary-source verification, non-interactive.
Release job: `primary-20260914-pinnacle-fibers-release-9c1ceac429e4`.
UTC verification date: 2026-09-14. Citation attempt: 1.
Launch: `4fc2d55b-97b1-4d44-869b-df4491df18cc`.

| Metric | Count |
| --- | ---: |
| Frozen substantive claims | 23 |
| Verified within stated scope | 23 |
| Citation-bearing claim locations | 7 |
| Direct citation commands | 8 |
| Distinct cited publications | 5 |
| Numerical errors, unsupported claims, misleading attributions | 0 |
| Missing or unused bibliography entries | 0 |

The extraction in `citation-extraction-initial.json` preceded source verification.
The current `citation-claim-ledger.json` preserves all 23 claim records without
re-extracting them. Its manuscript/PDF bindings were refreshed after two setup
repairs outside the claim locations. Verification below uses that fixed list in
claim-id order. The user expressly prohibited child workers, so this release
worker checked all five references sequentially after extraction; no agent was
delegated. Independent search requests were batched, but source support was
assessed in this release context. This is a fresh release review, not external
peer review or a new mathematical acceptance.

## Claim and source verification

| ID | Verification and precise support | Result |
| --- | --- | --- |
| C01 | Liang–Sagan published p.30, Section 8.2, Question 8.6(a), and immediately preceding ordered-fiber definition. | Verified, paraphrase |
| C02 | Accepted `claim.json` and `evidence/research_proof.md`; both displayed tables were replayed by `release-verifier.py`. | Verified, exact |
| C03 | Davis–Nelson–Petersen–Tenner arXiv v2, printed pp.1–2, endpoint exclusion and Definition 1.2. | Verified, paraphrase |
| C04 | Bouvel–Ferrari–Tenner v2, Definitions 1.1–1.2 (HTML lines 48–62); Liang–Sagan published pp.15–16, equation (15) and its following order definition. Coordinates count smaller VALUES to the right. | Verified, exact definitions |
| C05 | Bouvel–Ferrari–Tenner v2, Proposition 1.3 and its proof (lines 70–78), and the subsequent lattice discussion. Only the ambient order is asserted distributive. | Verified, paraphrase |
| C06 | The insertion argument in the manuscript agrees with the accepted proof: later larger insertions cannot change any smaller-value inversion count; coordinate extrema therefore give ambient operations. | Verified, mathematical argument |
| C07 | Published Liang–Sagan Question 8.6(a), p.30; frozen v1 HTML element `S8.Thmthm7` labels the same question 8.7(a). | Verified, exact numbering/scope |
| C08 | Rusu–Tenner v3, Definition 3.1, Theorem 3.6 and proof, HTML lines 118–179, with k_x=x−2|S_x|−1 at lines 200–202. The conclusion characterizes admissibility, not fiber bounds. | Verified, paraphrase |
| C09 | The five displayed elements prove nonemptiness; the accepted disproof thus also refutes the qualified universal question. | Verified, exact |
| C10 | Every one of the five permutation/coordinate/peak-position rows was independently recalculated from the actual TeX. | Verified, exact |
| C11 | Coordinate comparisons and full-fiber bound calculations verify the two chains and all three comparable-pair operations. | Verified, exact |
| C12 | The coordinate maximum of b,c is d, which lies in the fiber; full-fiber replay confirms its universal least-upper-bound property. | Verified, exact |
| C13 | Componentwise inequalities restrict common lower tables precisely to (0,0,u,0,v), u,v in {0,1}; the accepted coordinate bijection is applied. | Verified, exact |
| C14 | All four lower-table rows, decoded permutations and complete pinnacle sequences agree with direct calculation and the ambient common-lower set. | Verified, exact |
| C15 | Only 12354 from that four-element set has pinnacle sequence (5); 13254 instead has (3,5). | Verified, exact |
| C16 | The required internal operations give the two distinct permutations 13524 and 12534. | Verified, exact |
| C17 | Fresh enumeration gives exactly 120 ambient permutations and 56 fiber elements, agreeing with frozen and referee certificates. | Verified, exact |
| C18 | The fresh replay checks all 5×5=25 ordered named pairs against the whole 56-element fiber. The retained referee code and output establish the earlier check described in the paper. | Verified, exact |
| C19 | `referee_verifier.py` lines 21–30, 51–72 and 80–96 implement inverse-position coordinates, a distinct-entry word census, and full-fiber bound tests. Its retained output agrees with the release replay. | Verified, exact process evidence |
| C20 | Zeng et al. v1, Section 4 Lemma 3 and Proposition 1 certificate proof, lines 173–195, explicitly describe an integer predicate, a bitset implementation and a separate list implementation rebuilding the same graph. Section 6, lines 207–218, describes reconstruction and certificate checking. | Verified, paraphrase |
| C21 | The two tables and universal-bound arguments certify all terms of the violated identity without requiring enumeration of the full fiber. | Verified, mathematical argument |
| C22 | The accepted nonempty-fiber disproof answers only Question 8.6(a). The published adjacent part (b) is a separate counting/log-concavity question. No minimality or other-fiber classification is asserted. | Verified, exact scope |
| C23 | `literature/research_verified.md` records the dated bounded screen; the accepted referee report qualifies its scope. Fresh focused queries in `primary-focused-screen.json` returned no equivalent counterexample among the inspected primary records. This verifies the described bounded assessment, not worldwide priority. | Verified, bounded temporal assessment |

Definitions and reproduction instructions were reviewed for agreement with the
accepted reading. The disclosure accurately distinguishes model assistance and
a separate review pass from external peer review. No theorem was inferred from
search failure, a successful program, a build, or any audit flag.

## Bibliographic identities and retained uses

All five manuscript titles, author lists, years, venues, volume/page or article
numbers, and DOI identities were compared with primary records. The current
BibTeX entries are retained; no entry was replaced and no citation key changed.
Title-case differences and abbreviated rendered given names are formatting.
The institutional DNPT BibTeX export splits Petersen's given name incorrectly;
the retained `T. Kyle Petersen` agrees with the paper's own author line. No
unverified registry field was substituted for a primary record.

| Key | Primary bibliographic record and version | Necessary nearby use |
| --- | --- | --- |
| BFT | [Publisher record](https://link.springer.com/article/10.1007/s00373-024-02885-3): Mathilde Bouvel, Luca Ferrari, Bridget Eileen Tenner; *Between Weak and Bruhat: The Middle Order on Permutations*; Graphs and Combinatorics 41, article 34 (2025), published 10 February 2025. Content checked in [arXiv v2](https://arxiv.org/html/2405.08943v2). | Value coordinates and ambient product of chains; C04–C05. |
| DNPT | [Author institutional record](https://scholars.depaul.edu/en/publications/the-pinnacle-set-of-a-permutation-2/): Robert Davis, Sarah A. Nelson, T. Kyle Petersen, Bridget E. Tenner; *The pinnacle set of a permutation*; Discrete Mathematics 341(11), 3249–3270 (2018); DOI 10.1016/j.disc.2018.08.011. Definition checked in [primary arXiv PDF](https://arxiv.org/pdf/1704.05494), identified as v2. | Peak/pinnacle convention, C03; no priority claim is attributed. |
| LS | [Publisher record](https://link.springer.com/article/10.1007/s11083-026-09735-2): Jinting Liang and Bruce E. Sagan; *Log-Concavity and Log-Convexity via Distributive Lattices*; Order 43, article 21 (2026), published 2 May 2026. [Author-hosted published PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf), pp.15–16 and 30. | Problem origin, exact coordinate convention, and question scope; C04, C07, C22. |
| RT | [Publisher record](https://link.springer.com/article/10.1007/s00373-021-02306-9): Irena Rusu and Bridget Eileen Tenner; *Admissible Pinnacle Orderings*; Graphs and Combinatorics 37, 1205–1214 (2021). Content checked in [arXiv v3](https://arxiv.org/html/2001.08185v3). | Closest admissibility criterion and its distinction from internal operations; C08. |
| ZLRO | [Primary preprint](https://www.preprints.org/manuscript/202608.1658/v1): Zijian Zeng, Houde Liu, Kuru Ratnavelu, Ong Seng Huat; *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*; v1, posted 24 August 2026, explicitly not peer reviewed. The [publisher's subject index](https://www.preprints.org/subject/browse/computer-science-and-mathematics/computational-mathematics), lines 298–323 of the saved capture, confirms the title/authors and DOI 10.20944/preprints202608.1658.v1. | Exact predicates and separate finite-object reconstruction as a verification-method comparison, C20. No geometric bound or pinnacle theorem is imported. |

The four non-library references are identified by their DOI/title identities,
not by citation-key names. They cover the original question, definitions,
ambient theorem and closest related criterion. The elementary insertion and
bound arguments are proved in the paper; they do not require adding an
uncited lattice-representation theorem or a general computational algorithm.
No missing natural primary dependency or decorative reference was found.

## User-library selection and access limits

The exact active registry and manifest were read, all 49 first-sheet titles,
authors, DOI and keyword fields were screened, and candidate rows 9, 34, 35 and
47 were inspected. Row 9 supplies the useful method comparison; adding a
second unrelated result would not improve coverage. The selection includes
the dynamic registry/workbook checksums, exact attempt and launch, actual UTC
date, and the smallest citation-bearing sentence at lines 174–176. The nearby
claim is a literal substring. `selection-validation.json` records a successful
run of the hook-compatible `validate_selection` function and exact equality
between ledger keys and active body keys. The runner-owned pre-publish hook
was not invoked.

All applicable academic search templates were submitted for each of the five
references, including DOI queries and the four available arXiv identifiers.
Raw responses are saved in `source-search-*.json`; only primary text and
records were used as support. Source passage captures are in
`primary-passages-*.json`, `primary-find.json` and `local-primary-passages.json`.
The published question and source-version numbering were read directly.

No bibliography-revision or fast-completion handoff was present. The sole
`literature/outer-intake-handoff.md` was read, and its two primary-file hashes
were checked against both live local copies. No Crossref capture JSON or
Markdown file was present. Direct WSL HTTP access was denied; the web tool's
DOI resolver and Crossref API requests for ZLRO also failed. These endpoint
failures did not make the source unavailable: its complete primary page
and publisher index were accessible and independently supplied the exact
content, metadata, DOI, and version used. No unsupported DOI or abstract-only
mathematical claim remains. This review does not audit all results of the
cited geometric preprint or certify worldwide novelty.

## Manuscript dependency and rendered-citation audit

The complete publication scope is `manuscript/main.tex`,
`manuscript/references.bib`, and the actually consumed
`manuscript/build/main.bbl`, sorted in the acceptance JSON. The compiler
recorder and BibTeX log were inspected (`release-dependencies.json`). Other
local inputs are generated `.aux` and `.out` files; remaining dependencies
are installed TeX packages, fonts and configuration. There is no hidden
authored TeX import, local style or external figure.

The only source edits replaced `xurl` with the standard `url` package and
changed the bibliography declaration to the canonical `references` basename.
They repair the active validator's standard-setup and bibliography predicates.
The paper was then cleaned, rebuilt from `manuscript`, and refrozen. The final
checker reports five cited keys, five BibTeX keys, five resolved auxiliary
keys, and no missing, duplicate or unused entry. The final compiler and
BibTeX logs contain no unresolved citations or references.

All three final rendered pages were actually viewed. Page 1 resolves the
definition and prior-work citations, page 2 presents the accepted argument,
and page 3 resolves the methodological and concluding citations and all five
bibliography entries. The PDF's text extraction agrees with the source and
the visible bibliography. The exact snapshot bindings are in `citations.json`.
