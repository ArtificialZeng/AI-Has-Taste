# Citation and bibliography release audit

## Verdict

**Accept.** The frozen pass-1 ledger contains sixteen claim groups and four
direct citation pairs. Pass 2 verified all sixteen claims and all four
citations. There are no numerical errors, hallucinations, misleading claims,
missing citations, or unverified claims. Detailed results are in
`audit/claim-citation-ledger.json`, `audit/citation-verification.json`, and
`audit/citation-source-evidence.md`.

## Citation findings

| Key | Primary source and locator | Nearby support | Result |
|---|---|---|---|
| `HarlanderQuatrone2026` | arXiv v1 PDF, Definition 1 and Figure 1, pp.1--2 | finite torus, displayed cover, and source scope | Verified exactly; no replacement or key change |
| `ChungDiaconisGraham1992` | Elsevier article, abstract and Sections 2--6, especially pp.1--2 and 12 | universal-cycle consecutive-window framework for several combinatorial families | Verified as a conservative paraphrase; no replacement or key change |
| `GlockEtAl2020` | Springer abstract and arXiv accepted text, Theorem 2 | tight Euler tours under divisibility and complete-hypergraph universal-cycle case | Verified as a conservative paraphrase; no replacement or key change |
| `ZengEtAl2026` | Preprints.org v1, Section 6, online lines 209--218 | exact finite certificate architecture and reconstructing verification | Verified as a conservative paraphrase; no replacement or key change |

The arXiv landing record renders the first title in the singular, while the
hash-fixed version-1 PDF uses the plural title retained in the bibliography.
The Preprints item is correctly presented as a preprint, not as peer reviewed.
Publisher records confirm the retained authors, titles, years, venues, pages,
and identifiers. No BibTeX key changed, and no source edit was required.

## Coverage and mechanical checks

The bibliography now has ordinary body-flow citations to the problem origin,
the specific classical universal-cycle background, the closest broader
hypergraph Euler-tour result, and the selected active-library methodology
comparison. Each supports its nearby sentence. A topology text would be
decorative because the proof uses no external topological theorem, and the
finite reduction and enumeration are proved or reconstructed in the paper and
ancillary verifier.

The BibTeX checker found four cited keys, four bibliography entries, no missing
or unused entries, and exact agreement with the final AUX citation set. The
converged LaTeX and BibTeX logs contain no undefined citation, missing database
entry, duplicate entry, or bibliography warning. All applicable mandatory
search templates were run, with primary publisher/full-text records used for
the conclusions. This audit was performed serially because the job explicitly
prohibited agents.
