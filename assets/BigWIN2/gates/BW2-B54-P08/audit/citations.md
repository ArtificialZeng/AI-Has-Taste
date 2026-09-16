# Fresh citation and bibliography audit

## Verdict

Accept. All five cited works exist, all five metadata records agree with their
primary archive/publisher records, and all six substantive citation uses support
their nearby claims. Pass 1 was frozen before verification in
`audit/citation-claim-ledger.md`; pass 2 and exact source locations are recorded
in `audit/citation-source-verification.md`.

## Citation surface and coverage

| Key | Nearby claim | Primary support | Action |
|---|---|---|---|
| `haqi2026gap` | Chain-gap definition; width-two arbitrary-chain-gap existence | arXiv v1, Definition 1.2 and Theorem 5.1 | Retain; metadata and scope verified |
| `dilworth1950` | Width-at-most-two posets admit a two-chain cover | Original Annals article, pp. 161--166 | Retain; metadata and theorem verified |
| `harris2020numpy` | NumPy software dependency | Nature record and repository imports | Retain; metadata and use verified |
| `lam2015numba` | Numba software dependency | ACM DOI/workshop record and repository imports | Retain; metadata and use verified |
| `zeng2026finite` | Exact finite certificate architecture with symmetry reduction and independent reconstruction | Preprints.org full text, Sections 3 and 6 | Retain; active-library selection and body-flow `\cite` verified |

The bibliography has normal scholarly coverage for the paper's actual claims:
the primary problem origin and closest theorem, the nontrivial order-theory
dependency, the two named implementation dependencies, and the directly used
verification-method comparison. It is neither user-library-only nor padded.
No additional user-library record is naturally relied upon by the manuscript.

## Mechanical audit

The canonical bibliography is `manuscript/references.bib`. The source contains
five distinct citation keys, all five exist exactly once in the bibliography,
all five occur in the final `.aux`, and there are no unused entries. The selected
user-library item uses the ordinary body-flow command
`\cite{zeng2026finite}` at manuscript lines 89--94. No custom or indirect cite
macro is defined. No keys changed and no `.tex` or `.bib` repair was necessary.

The final BibTeX log reports five entries and zero warnings. The final LaTeX log
has no undefined citations or references. The read-only key checker reports zero
missing files, keys, unused entries, or `.aux` inconsistencies.

## Scope control

The accepted claim remains the partial result `m_2(4)>=18`. The manuscript does
not strengthen it to an exact value or a minimizer classification. The negative
literature statement is explicitly a bounded search report, not a priority
claim. Citation success is not treated as mathematical certification.
