# Citation and bibliography audit

## Scope and method

This is the verification-only second pass for release job
`win-00083-p01-release-af6b0c8b2fa1`, citation attempt 1, launch
`497ac9f0-7dbf-4d37-9cbf-18de6f0ed1a3`, over the twelve claims frozen first in
`audit/citation-claim-ledger.json`.  The audit is bound to mathematical snapshot
`ebaf542da85d2cd1eee04a41a4d51aabf659e482fcdeed19b8e0a7ece4498af2`,
manuscript digest
`427ee76efe397135dcdc7f5dfbacff897e0b752f873b4fda02e7209203085ef2`, and PDF
digest `94d9b6a229fb61390c7d32b1559eccdb7ccebb568eb8da1ab0ed71130394a282`.
The user prohibited sub-agents, so the citation-check and BibTeX audit was
performed sequentially.  Searches used exact titles, authors, venues,
identifiers, and DOI queries; verification then inspected the primary article or
an authoritative publication record and the exact nearby passage.

## Coverage decision

The six ordinary body-flow citation keys exactly equal the union of keys in the
frozen claim ledger.  The bibliography is not library-only.  The arXiv paper that
originates the problem and states the closest prior planar result is cited twice;
the original or authoritative records for the Erdős--Gallai and Havel--Hakimi
graphicality tests are cited at their actual use; and the NetworkX paper is cited
for the package used by the independent implementation.  The one active-library
paper is retained only for a narrow verification-method comparison.  No other
active-library item naturally supports a manuscript claim, and adding one would
be padding.  No substantive literature-dependent claim lacks its natural source,
and no citation is merely decorative.

## Claim-to-source verification

| Claims | Key | Exact source location inspected | Status |
|---|---|---|---|
| C01, C02, C05 | `AscoleseEtAl2026` | Official arXiv record 2609.08803v1 (title, four authors, submission history, and planar scope); frozen primary PDF pp. 17, 19--20, Lemma 5.3, Corollary 5.8, the following conjectural sentence, and Theorem 5.9. | Verified (exact metadata and exact theorem locations) |
| C03, C04 | `ZengEtAl2026Certificates` | Primary Preprints.org v1 record, metadata and abstract; Proposition 1 and Section 6 state use of integer predicates, exact exhaustive search, a separately implemented maximum-clique check, and standard-library reconstruction. | Verified (exact metadata; nearby claim is a conservative paraphrase) |
| C06, C07 | `ErdosGallai1960` | Rényi Institute scan of the original paper, pp. 264--265, especially Theorem 1.2 and its necessary-and-sufficient inequalities; institute bibliography confirms the title, authors, venue, volume, and pages. | Verified (exact theorem and metadata) |
| C08, C09 | `Havel1955` | Czech Digital Mathematics Library primary record/PDF, article page and theorem record: Václav Havel, 1955, vol. 80(4), 477--480, DOI `10.21136/CPM.1955.108220`; the original Erdős--Gallai introduction and NetworkX documentation identify Havel's realization algorithm. | Verified (exact metadata and method attribution) |
| C08, C10 | `Hakimi1962` | SIAM journal record, abstract and publication information: the realizability problem for degree lists, S. L. Hakimi, vol. 10(3), 496--506, DOI `10.1137/0110037`; NetworkX documentation identifies the corresponding Havel--Hakimi method. | Verified (exact metadata and topic) |
| C11, C12 | `HagbergEtAl2008` | Author-hosted and official SciPy proceedings paper, pp. 11--15, describing NetworkX as a Python package implementing graph algorithms; official NetworkX `is_graphical` documentation lists both `method='eg'` and `method='hh'`.  The installed audited environment independently reports NetworkX 3.4.2 and both methods execute. | Verified (exact metadata and method availability) |

All twelve frozen claims are verified.  There are no numerical errors,
hallucinations, misleading attributions, citation-not-found results, or
unverified claims.  No BibTeX entry or key required replacement.

## Authoritative sources consulted

| Key | Primary or authoritative record | Why retained |
|---|---|---|
| `AscoleseEtAl2026` | <https://arxiv.org/abs/2609.08803> and frozen v1 PDF | Problem origin, closest planar result, degree reduction, and source inequality. |
| `ZengEtAl2026Certificates` | <https://www.preprints.org/manuscript/202608.1658> | Gate-selected comparison for exact finite verification practice. |
| `ErdosGallai1960` | <https://www.renyi.hu/~p_erdos/1961-05.pdf> | Original necessary-and-sufficient graphicality criterion. |
| `Havel1955` | <https://dml.cz/handle/10338.dmlcz/108220> | Primary archive record for Havel's degree-realization reduction. |
| `Hakimi1962` | <https://epubs.siam.org/doi/10.1137/0110037> | Primary journal record for Hakimi's realization theorem. |
| `HagbergEtAl2008` | <https://proceedings.scipy.org/articles/TCWV9851.pdf> | Primary software paper for NetworkX. |

## Mechanical consistency

The bibliography checker found six cited keys, six BibTeX entries, no missing or
unused entries, and exact agreement with the six `\bibcite` keys in
`manuscript/main.aux`.  The converged `main.log` and `main.blg` contain no
undefined citation or reference, missing database entry, repeated entry, BibTeX
warning, LaTeX error, or fatal diagnostic.  The hook-compatible active-library
selection validator passed with the exact runner-issued job, attempt, and launch
bindings.
