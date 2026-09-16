# Verification Report

Mode: fresh primary-source search verification and exact local evidence replay.
Document: `manuscript/main.tex` with `manuscript/references.bib`.
Job: win-00085-p10-release-67ea8095309a. Date: 2026-09-12 UTC.

All 34 extracted claim groups were checked: 34 verified within their stated
scope, zero numerical errors, zero hallucinations, zero misleading citations,
and zero unresolved citation-support items. The seven ordinary citation
commands use five distinct works. Mathematical statements were checked for
faithful transmission of the accepted result and against the printed argument;
this release record does not replace the frozen mathematical referee audit.

Pass 1 froze claim text, locations, and direct keys before verification. Pass 2
checked the listed claims against the exact source passages and relevant local
evidence. After the canonical-source compatibility repair, the same coefficient
claims were relocated and the affected process description was frozen before
replay. No interactive confirmation or delegation was used, as the user
explicitly required a non-interactive single-worker job.

## Claim-driven bibliography coverage

| Key | Primary record and exact support | Why retained |
|---|---|---|
| Kotek2012 | [Recurrence Relations and Splitting Formulas for the Domination Polynomial](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v19i3p47); Printed page 2, Definition 1.1; PDF text lines 61-73. Publisher record gives 11 October 2012, volume 19, issue 3, P47. | Primary definition and normalization of the graph polynomial. |
| Du2026 | [Trees and Graphs with Non Log-concave Dominating Set Sequence via AI Tools](https://arxiv.org/abs/2605.02193v1); Section 3.2, Theorem 3.3 and its product/proof, HTML lines 232-255; Remark 3.4, lines 256-258; Section 4.1, equations (4.1)-(4.3), lines 286-309. | Original problem, closest positive result, and dynamic-programming method. |
| Zeng2026 | [Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees](https://arxiv.org/abs/2608.18179v1); Section 2, Leaf components and weighted cores, opening paragraphs, HTML lines 55-64; arXiv record lists v1 submitted 18 August 2026. | Shared tree representation explaining the change from positive legs to singleton core components. |
| Gross2015 | [Log-Concavity of Combinations of Sequences and Applications to Genus Distributions](https://epubs.siam.org/doi/10.1137/140978867); Author-hosted manuscript, printed page 5, Section 2, PDF text lines 165-204. Publisher metadata lines 651-671 and authors lines 692-704. | Nontrivial convolution method under the exact required hypotheses. |
| Meurer2017 | [SymPy: symbolic computing in Python](https://github.com/sympy/sympy-paper); Authors’ source repository README, citation and complete BibTeX block, rendered lines 225-251; raw README lines 0-5. | Identification of the symbolic computation software actually used. |

The bibliography covers the actual problem origin and closest positive theorem,
the graph-polynomial definition, convolution, and exact symbolic software. It
is not library-only. All 49 active first-sheet titles were screened; row 17 is
the one gate-bound selection because its leaf/core definitions explain the
singleton components in this family. The paper expressly distinguishes the
chromatic symmetric invariant. No domination inequality or priority claim is
attributed to that library work, and no second library paper was added merely
to increase the count. DOI identity checking confirms four natural non-library
sources; their keys are not renamed library entries.

The full author/title/year/venue/DOI comparison is in
`citation-source-verification.json`. All retained fields agree with inspected
primary records. `references.bib` was retained unchanged: no BibTeX replacement
and no citation-key change was needed. The SymPy author repository includes the
official complete BibTeX and supports the 27-author record. Its publisher PDF
request returned HTTP 403, but the author-maintained primary source was
accessible. No inaccessible source is treated as verified from an identifier.
The pre-edit Crossref-capture enumeration was empty; no saved authoritative
capture was ignored. Du's registered v1 date and the HTML's internal manuscript
date were distinguished rather than inventing a later registered version.

The bounded fresh searches and targeted follow-up are logged in
`citation-search-log.json`. Omar's arXiv:2601.14494 abstract gives a threshold-
graph log-concavity theorem; this family contains an induced four-vertex spine
path and is outside threshold graphs. A short-legged spider lead was not used
as authority and does not establish a covering theorem. None of the inspected
sources supplied the universal zero-leg extension or the present two-parameter
theorem. This is a bounded comparison, not proof of global priority.

## Verification of every frozen claim group

| ID | Evidence | Finding |
|---|---|---|
| C01 | accepted-scope | The statement is exactly the accepted result-note for all positive integer p,q; no universal caterpillar result is asserted. |
| C02 | accepted-scope; Du2026 | Four spine vertices and two zero legs are explicit in the definition. Three sparse additions have 3+3+4 affected centers; arbitrary zero patterns are excluded. |
| C03 | Kotek2012 | Definition 1.1 matches the cardinality generating polynomial, including initial indices. |
| C04 | Du2026 | Theorem 3.3 matches the displayed product with all a_i>=1; Remark 3.4 supplies only a belief for some zero legs. |
| C05 | accepted-scope | N=p+q+4 and 1<=j<=N-1 coincide with claim.json and the accepted audit. |
| C06 | Zeng2026 | The Section 2 core/proper-tree definitions match this sentence exactly in substance. |
| C07 | Zeng2026; direct tree definition | Deleting the three spine edges leaves two stars of orders p+1,q+1 and two isolated spine vertices; the invariant distinction is explicit. |
| C08 | Gross2015; Du2026; accepted-scope | Convolution support is verified in Gross Section 2. Coupling of bare vertices follows from the stated domination rule and endpoint split; no arbitrary-addition closure is claimed. |
| C09 | audit/citation-search-log.json | Verified only as a bounded search report dated 12 September 2026. No equivalent was identified; no exhaustive priority or global current-open-status certificate is asserted. |
| C10 | audit/math.md; endpoint-state inspection | Selected endpoints contribute x(1+x)^p; unselected endpoints force their leaves. Except in the both-selected case, a middle vertex must be chosen, and either choice suffices. |
| C11 | audit/math.md; audit/release-verifier-output.json | The endpoint expression divides by x^2 to give all four displayed H terms, and its leading term has degree p+q+2. |
| C12 | audit/math.md; symbolic identities | Reversal of each of the four terms gives the displayed H* formula with x+2x^2 and x^2+2x^3. |
| C13 | audit/math.md; symbolic identities | Expanding the three nested identities with u=q-p reproduces H*; p<=q is justified by endpoint symmetry. |
| C14 | Gross2015; manuscript proof | Standing nonnegative/no-internal-zero hypotheses match. Toeplitz order-two minors and finite Cauchy-Binet multiplication give convolution closure. |
| C15 | audit/release-certificate-generator.json | Coefficient extraction from the nested products yields the falling-factorial sums; no floating-point approximation occurs. |
| C16 | audit/release-certificate-independent.json | All ten rational polynomial arrays match Fraction-only reconstruction, with nonnegative coefficients; the accepted proof establishes completeness of these centers. |
| C17 | audit/math.md; manuscript proof | A minor uses three adjacent coefficients, so additions alter only the listed centers. Binomial supports cover the additions even at p=1,u=0. |
| C18 | audit/math.md; manuscript proof | Reversal preserves the minors; multiplying by x^2 adds initial zero coefficients. Centers 1 and 2 are immediate, and the remaining range is exactly correct. |
| C19 | Meurer2017; manuscript/generate_certificates.py; audit/release-certificate-generator.json | Software identity is supported by the author repository. The inspected code uses rational SymPy domains and --check compares the JSON and generated TeX source. Inline tables were separately matched byte for byte. |
| C20 | audit/release-verifier-output.json | Fresh replay matches the frozen output: 400 ordered pairs with p,q<=20 and all 36 positive pairs with p+q<=9. These are finite checks. |
| C21 | Du2026; evidence/caterpillar_small_search.py | Section 4.1 equations (4.1)-(4.3) match A=x product(A+B+C), B=product(A+B)-product(B), C=product(B). |
| C22 | audit/release-verifier-output.json | Fresh replay gives exactly 11,325 pairs and 1,744,050 nonnegative minors. Values and quantifiers match; no rounding or proof from sampling. |
| C23 | accepted-scope; manuscript proof | Only a block of two consecutive bare vertices is covered, without induction for longer or separated blocks. |
| C24 | audit/math.md; role records; inspected code | The proposer and referee job IDs differ; accepted audit documents reconstruction and additional exact checks. Publication code uses integer/rational arithmetic, and disclosure does not call this external peer review. |
| C25 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C26 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C27 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C28 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C29 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C30 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C31 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C32 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C33 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |
| C34 | audit/release-certificate-independent.json; audit/release-inline-table-check.json | This exact scaled coefficient polynomial was reconstructed using Fraction arithmetic. Its array equals the generated source; the inline tabular cells match byte for byte. All entries are integers and nonnegative. |

## Canonical sources, scope and release corrections

The original source, checkpoint, claim, mathematical snapshot members, and
accepted audit are unchanged. The theorem remains exactly log-concavity for
T(p,0,0,q), p,q>=1; the original universal question remains unresolved. No new
theorem, hypothesis change, or numerical-to-universal inference was introduced.

The selection validator initially rejected the appendix input command, table
rendering assignments, and opaque title/filename commands. Scope-preserving
repairs expanded the five identical tabular blocks directly into `main.tex`,
used default table spacing, and replaced equivalent title/filename markup.
The generated-table description and README were updated accordingly. PDF title
and author metadata were added. The five inline tabular blocks are byte-identical
to the generator output; ten coefficient arrays were reconstructed exactly.
Fresh clean compilation, refreezing and all six rendered-page views followed.

All eight publication source files were inspected, including the reproduction
scripts, integer arrays, generated table source, and README. The two Python
verification files include their one local import in the source list. There are
no hidden citation macros, conditionals, nocite items, external figures, or
custom class/style files. The canonical main document now contains its tables;
`certificates.tex` is an accompanying reproduction output. System LaTeX packages
and derived bbl/aux files are build dependencies, not omitted authored sources.

The installed hook-compatible selection validator passed with attempt 1 and
the supplied launch UUID. The ledger key union equals the five active body
keys. The BibTeX key/aux checker reports zero missing or unused keys; converged
LaTeX and BibTeX logs have no warnings or undefined references. The configured
pre-publication hook was not invoked; it remains runner-owned.

Verdict: accept citation correctness and coverage for this manuscript snapshot.
