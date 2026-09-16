# Citation and bibliography audit

## Result

Pass. The frozen extraction ledger contains seven manuscript claims and four
ordinary citation occurrences using two bibliography records. In the second
pass, all seven claims were verified against either the original source text
or the accepted, hash-bound mathematical evidence. There are no numerical
errors, unsupported strengthenings, undefined citations, decorative retained
references, or key changes.

## Claim-level findings

`JiangYang2026` was checked against arXiv:2609.01256v1 and the byte-frozen
primary PDF. Definition 2.1, Lemma 2.3, Theorem 4.7, Definition 5.1, Lemma
5.2, Lemma 5.4, and Section 9 support the nearby definitions, development
claim, known range, colour formula, chain criterion, and open-question wording.
The manuscript does not turn failure of the ABAB construction into a
nonexistence result.

`ZengEtAl2026ExactFinite`, active user-library row 9, was checked against the
primary Preprints.org full text and DOI identity. Its abstract and Sections 3
and 6 support the narrow comparison to exact finite-domain enumeration,
integer predicates, serialized certificates, and independent replay. The
manuscript explicitly denies any graph-theoretic dependence, so the citation
is relevant without being used as mathematical authority for the theorem.

The four targeted exact-small-case searches recorded in
`audit/citation-verification.json` found the Jiang--Yang source but no separate
determination of the `r=3,7` tuple. The manuscript states this only as a
bounded search report and makes no priority claim.

## Bibliography coverage and metadata

The bibliography is not user-library-only: Jiang--Yang is the primary problem
origin and closest prior result, while the user-library paper supports the
only external methodological comparison. No additional primary source is
naturally required for the literal finite enumeration or the displayed
integer witness. Both current records match the primary title, authors, year,
identifier, and venue/version scope. Direct WSL requests for official arXiv
BibTeX and Crossref exports could not connect; therefore no speculative
replacement was made. The existing records were retained after primary-page
and primary-PDF verification.

The user-library selection is bound to citation attempt 1 and launch ID
`c9e62eac-919d-4e36-a8bc-e64b7bac72fb`; its registry and workbook checksums,
sheet identity, row identity, DOI, final key, direct body citation, nearby
claim, and source passage are recorded in
`audit/user-bibliography-selection.json`. Only one library item is retained
because selecting another of the 49 entries would pad rather than support the
paper.

The bibliography audit was performed serially by the release worker because
the job explicitly prohibited subagents and other workers.
