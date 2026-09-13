# Fresh citation and claim-support audit

Release job: `bigMac-00015-p01-release-3bca604ddec1`  
Search and inspection date: 2026-09-08  
Mode: `$citation-check-skill` v2 search verification, used as an advisory
two-pass check, together with direct inspection of the supplied primary PDF and
the accepted mathematical audit.

## Scope and dependency check

The complete authored dependency list in `publication.json` is:

1. `manuscript/main.tex`
2. `manuscript/references.bib`

It is already sorted, and both files were inspected in full.  The `.fls` file
shows no other project-authored TeX input, figure, local style, or imported
source.  `main.bbl`, `main.aux`, and `main.out` are generated build products,
not authored dependencies.  The extracted PDF contains exactly the two cited
references, and both citation keys in `main.aux` have matching `\bibcite`
records.  There are no undefined citations.

The requested `literature/user_bibliography_check.md` is not present anywhere
in the project, so there is no user-designated workbook record to apply or
override.  This absence was already disclosed by the writing phase.  The two
references actually used are genuinely relevant: Zhang--Zhang is the nearest
primary mathematical source for the raw inversion map and lower bound, while
Abbe--Boix-Adserà--Misiakiewicz supplies the support-ordering leap notion from
which the ANF adaptation takes its organizing idea.

## Pass 1: fixed claim extraction

Extraction was completed before source verification.  Definitions and purely
methodological descriptions were excluded under the citation-check rules.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | The paper proves `L(G_{n,f})=n` for every `n>=2`, every allowed irreducible modulus, the polynomial basis, and the full matrix domain including singular matrices. | Existence / quantified result | Abstract; Theorem 1, pp. 1--2 |
| C02 | The lower bound follows from vanishing on all inputs of Hamming weight below `n`. | Causal / mathematical | Abstract; p. 2 |
| C03 | A cyclic family of `n` supported degree-`n` monomials gives the upper bound and leaves only one matrix row unseen. | Existence / mathematical | Abstract; equations (8)--(12), p. 3 |
| C04 | The joint ANF leap is an ANF analogue of support-ordering notions associated with leap complexity. | Attribution / comparative | Context, p. 1, citation [1] |
| C05 | Zhang and Zhang prove the universal lower bound `L(G)>=n`. | Attribution | Context, p. 1; comparison, p. 3, citation [2] |
| C06 | Zhang and Zhang report equality by exhaustive computation for `n=3,4` and finite certificates in those dimensions. | Attribution / statistic | Context, p. 1; comparison, p. 3, citation [2] |
| C07 | The Zhang--Zhang source defines the same full-space raw map and joint-support invariant used in the comparison. | Attribution / existence | Comparison, p. 3, citation [2] |
| C08 | Complete ANFs were checked for `n=2,3`, and the cyclic coefficients were checked for every irreducible modulus of degrees 2 through 6. | Statistic / existence | Checks and limitations, p. 3 |
| C09 | The Abbe--Boix-Adserà--Misiakiewicz reference has the authors, title, PMLR volume 195, pages 2552--2623, and year 2023 shown in the bibliography. | Citation metadata | Reference [1], p. 4 |
| C10 | The Zhang--Zhang reference has the authors, title, year 2026, and arXiv identifier 2609.04583v1 shown in the bibliography. | Citation metadata | Reference [2], p. 4 |

## Pass 2: verification against fixed claims

| ID | Status | Evidence and exact support |
|---|---|---|
| C01 | Verified | The authored statement matches `claim.json` without strengthening, and the frozen proof was accepted in `audit/math.md` at snapshot `ab3e4198491bf587813a4e9409d5ead91b272ae82481f039447827d825db8405`. |
| C02 | Verified | The argument on p. 2 matches both the accepted referee reconstruction and Zhang--Zhang Theorem 17's subset-XOR/rank proof for the lower bound. |
| C03 | Verified | Equations (8)--(12) reproduce the accepted cyclic-prefix proof; `audit/math.md` independently checks the adjugate orientation, the `n=2` edge case, disjointness, and the one-row remainder. |
| C04 | Verified (paraphrase) | Abbe et al., Definition 1, pp. 3--4, defines leap by minimizing the maximum number of new support coordinates introduced by an ordering.  Zhang--Zhang, Definition 14, printed p. 12, explicitly adapts that ordering idea to joint vector ANF support and distinguishes it from Fourier support.  The manuscript says only “analogue,” not identity. |
| C05 | Verified (exact) | Zhang--Zhang Theorem 17, printed pp. 14--15, states that every raw-support monomial has degree at least `n` and concludes joint ANF leap at least `n`. |
| C06 | Verified (exact) | Zhang--Zhang Experiment 0 and Table 1, printed pp. 17--18, report exact joint leap `3` and `4`; Appendix A.3 and Tables 7--8, printed pp. 27--28, provide the finite support-ordering certificates.  The source itself says these two cases do not prove the general equality. |
| C07 | Verified (exact) | Zhang--Zhang Definition 11 defines `f_raw(P,u)=adj(P)J_n(Pu)` on the full Boolean matrix space; Definitions 13--14 give the joint vector ANF support and the same ordering-leap formula. |
| C08 | Verified (exact local evidence) | `evidence/exact-summary.json` records complete truth tables/ANFs for `n=2,3` and all-modulus sparse coefficient sums for every irreducible modulus in degrees 2 through 6, using exact binary arithmetic.  The prose correctly calls these checks corroborative only. |
| C09 | Verified (exact metadata) | The official PMLR article page and PDF give Emmanuel Abbe, Enric Boix-Adserà, Theodor Misiakiewicz, the stated title, PMLR 195, pp. 2552--2623, 2023. |
| C10 | Verified (exact metadata) | The official arXiv record gives Zheng Zhang and Na Zhang, the stated title, identifier 2609.04583, submitted 4 September 2026; the supplied PDF is v1. |

No extracted claim is contradicted, misleading, numerically mismatched, or
unsupported.  The manuscript makes no priority claim: it explicitly limits
the comparison to inspected sources.  That bounded novelty wording is
appropriate and is preserved.

## Primary sources consulted

- Zheng Zhang and Na Zhang, *Representation Redundancy and Structural
  Complexity in Finite-Field Inversion*, arXiv:2609.04583v1:
  `evidence/2609.04583v1.pdf` and <https://arxiv.org/abs/2609.04583>.
- Emmanuel Abbe, Enric Boix-Adserà, and Theodor Misiakiewicz, *SGD Learning on
  Neural Networks: Leap Complexity and Saddle-to-Saddle Dynamics*, PMLR 195
  (2023), 2552--2623:
  <https://proceedings.mlr.press/v195/abbe23a.html> and the linked official PDF.

The mandatory title/author/venue/identifier query variants were run for both
records.  No DOI is supplied or asserted for either record, so no optional DOI
endpoint is material to this audit.

## Verdict

**Accept.**  Both references exist and support the nearby prose; metadata is
verified from official primary records; attribution and numerical scope are
accurate; dependency scope is complete; and citations are defined and rendered.

