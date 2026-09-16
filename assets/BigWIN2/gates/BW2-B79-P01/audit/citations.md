# Citation and bibliography audit

Release job: `win-00079-p01-release-4de04a17e866`  
Citation attempt: `1`  
Launch UUID: `ab1d5614-b22f-4ce4-b98c-4ca00f958cfe`  
Verification date: 2026-09-10 UTC

## Stage 1: frozen extraction

The manuscript was read in full before source verification.  The four extracted
claim/citation pairs were frozen as `CIT-01` through `CIT-04` in
`audit/citation-claim-ledger.json`.  Its citation-key union is exactly
`Andreev1970`, `Egorov2026`, and `ZengEtAl2026Certificates`, which is also the
complete set of ordinary body-flow keys extracted from `manuscript/main.tex`.
There are no citation macros, hidden conditionals, `\nocite` commands, or inert
comment citations.  The canonical bibliography is `manuscript/references.bib`.

## Stage 2: independent source verification

| Claim | Key | Primary record and exact locator | Result |
|---|---|---|---|
| `CIT-01` | `Egorov2026` | Andrey Egorov, *Minimal-Volume Equiangular Hyperbolic 4-Polytopes*, arXiv:2609.04258v1. Official arXiv record and the hash-bound local v1 PDF: Proposition 2.1 (PDF pp. 3--4), Proposition 2.3 (pp. 4--5), Proposition 5.1 and Remark 5.2 (p. 9). | Verified, exact/paraphrase. Proposition 2.1 gives endpoint ideality; Proposition 2.3 constructs the model, limits cube rigidity to `alpha > alpha_0`, and expressly says endpoint uniqueness is not needed; the later locators retain the same strict restriction. |
| `CIT-02` | `Andreev1970` | E. M. Andreev, *On convex polyhedra in Lobachevskii spaces*, *Mathematics of the USSR-Sbornik* 10(3) (1970), 413--440, DOI `10.1070/SM1970v010n03ABEH001677`; official MathNet article record and Egorov Proposition 2.3/reference [2]. | Verified, paraphrase. Egorov explicitly attributes its compact non-obtuse uniqueness step to this work. MathNet confirms author, title, year, venue, pagination, DOI, and the compact non-obtuse subject. The manuscript makes only this historical attribution and does not use Andreev as an endpoint proof. |
| `CIT-03` | `Egorov2026` | Egorov v1, Section 2.1, displayed equation (2), PDF p. 3. | Verified, exact. With outward unit spacelike normals, meeting facets satisfy `inner product = -cos(theta)` in precisely the cited convention. |
| `CIT-04` | `ZengEtAl2026Certificates` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org version 1, posted 24 August 2026, DOI `10.20944/preprints202608.1658.v1`; Section 6 and the Data, Code, and Computational Disclosure. | Verified, paraphrase. The source distinguishes theorem statements from the exact finite checks, identifies the verifier trust boundary, states that decisive comparisons use exact arithmetic, and denies treating language-model output as evidence. Its non-peer-reviewed status is disclosed in the bibliography. |

The official source URLs checked were
`https://arxiv.org/abs/2609.04258`,
`https://www.mathnet.ru/eng/sm3382`, and
`https://www.preprints.org/manuscript/202608.1658`.
For each work, the title/author/year query, full-title arXiv-or-Semantic-Scholar
query, author/year/venue query, DOI query where present, and arXiv-ID query where
present were replayed.  The primary record, not a search snippet, supplied each
acceptance decision.

## Bibliographic correctness and coverage

All three entries exist and their title, author, year/version, venue, DOI or
arXiv identifier, and nearby support were checked.  The arXiv subject in
`Egorov2026` was corrected from `math.MG` to the official `math.GT`; no citation
key changed.  `latexmk` regenerated the bibliography.  The read-only key checker
finds three cited keys, three bibliography entries, no missing or unused entry,
and exact agreement with the final `.aux`.  The final `.log` and `.blg` contain
no undefined-citation, missing-database-entry, repeated-entry, or BibTeX warning.

Coverage is proportional rather than quota-driven.  Egorov is the problem-origin
and closest-result source; Andreev is a natural non-library historical source for
the compact rigidity step discussed in the comparison; and the selected row-9
user-library paper directly supports the narrow exact-certificate methodology
sentence.  The Lorentz--Gram proof is self-contained and invokes no additional
nontrivial external theorem.  No retained citation is decorative, and an
additional user-library citation would be padding.

The explicit job constraint prohibited subagents, so this per-key verification
was performed sequentially in this fresh release worker rather than delegated.
No source remained unverified and there are no citation blockers.
