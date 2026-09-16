# Citation and bibliography audit

## Scope and two-stage method

This is the verification-only second pass for release job
`win-00084-p10-release-aaaec94d61e5`, citation attempt 2, launch
`625c5bd4-c83b-4acf-80b4-520a8ad573d4`. The extraction was frozen first in
`audit/citation-claim-ledger.json`: five substantive claim/citation pairs and
exactly the three ordinary body-flow keys in `manuscript/main.tex`. Extraction
and verification were not interleaved. The user prohibited sub-agents, so all
three records were audited sequentially.

All applicable academic search templates were run on 2026-09-09 UTC: author,
year, and title words; exact title with the prescribed arXiv/Semantic Scholar
restriction; author/year/venue; DOI; and arXiv identifier where applicable.
Verification then used the exact source passages rather than search snippets.
The release is bound to manuscript digest
`92f92d30a2837baf8e8f227ed53f3b19a9f2d24cf8d4bfd37e24b71f9bc9fc94`
and PDF digest
`e33ec377a5ce8afa14ecbd7edb12b06bfb1b514910c238c0446b2b6b598544d5`.

## Coverage decision

The bibliography is claim-driven and not user-library-only. Muney is the
primary problem and closest-prior-result source. Brown is the natural primary
historical source for the subset-sum completeness comparison. The gate-selected
user-library paper supplies only the narrow method-reporting comparison about
finite universes, exact verification, and trust boundaries. Screening all 49
active first-sheet titles and metadata found registry row 9 to be the only
entry with a direct, independently accessible, non-decorative use here; a
second library citation would be padding. Muney and Brown are both natural
non-library citations in ordinary body flow.

## Fixed claim-to-source verification

| Claim | Key | Primary location inspected | Result |
|---|---|---|---|
| C01 | `Muney2026` | arXiv 2606.23721v2 abstract and local PDF pp. 1--3: the paper defines the local extension problem and states that it develops a corrected exact theory, membership criterion, algorithm, and interval criterion. | Verified, paraphrase |
| C02 | `Muney2026` | Local v2 PDF, Proposition 18 on pp. 17--18 and Theorem 20 on pp. 18--20. Proposition 18 gives the ordered preimage recurrence with the lower branch allowed only for `e >= t`; Theorem 20 gives exactly the displayed ordered inequalities. | Verified, exact |
| C03 | `Brown1961` | Official JSTOR issue record, Monthly 68(6), pp. 557--560, DOI 10.2307/2311150, confirms Brown's primary record. Muney's primary v2 text on pp. 18 and 29 explicitly identifies its ordered condition as the analogue of Brown's subset-sum completeness criterion and states the same next-weight/sum shape. | Verified, paraphrase and attribution |
| C04 | `Muney2026` | Local v2 PDF: Example 19 and Theorem 24 identify the first hole at `(2,3,5,9,15)`; Theorem 25 on pp. 22--24 proves minimum width five and the unique minimizer; Question 16(5) on p. 29 asks for the width-at-most-nine stability classification. | Verified, exact |
| C05 | `ZengEtAl2026Certificates` | Official Preprints.org v1 full text, Section 6, especially its opening sentence and verifier inventory: ancillary files separate discovery from certification, standard-library verifiers reconstruct the finite universes, and the generator packages are excluded from the theorem's trust boundary. | Verified, paraphrase |

All five fixed claims pass. There are no numerical errors, citation-not-found
results, misleading attributions, hallucinations, or unverified claims.

## Authoritative records and bibliography audit

| Key | Official record | Metadata/action | Uncertainty |
|---|---|---|---|
| `Muney2026` | https://arxiv.org/abs/2606.23721 | Title, author, math.CO category, v1 date, v2 revision date, identifier, and nearby mathematical support agree. No replacement or key change. | None |
| `Brown1961` | https://www.jstor.org/stable/2311150 and issue record https://www.jstor.org/stable/i314924 | Author, title, journal, volume, issue, pages, year, and DOI agree. No replacement or key change. | None |
| `ZengEtAl2026Certificates` | https://www.preprints.org/manuscript/202608.1658 | Official v1 title, four authors, August 2026 posting, DOI identity, venue, and Section 6 support agree. No replacement or key change. | None |

The active selection is bound to registry SHA-256
`67477dfa5d2f3dfcb5a9123fd79975af80968b43058ff32c774143c2f26112d4`
and source-workbook SHA-256
`93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427`.
The hook-compatible selection validator and its JSON schema validation both
passed for attempt 2. The final bibliography checker reports three cited keys,
three entries, no missing or unused entry, and exact AUX agreement. The
converged log and BLG scan found no undefined citation/reference, missing
database entry, repeated entry, BibTeX warning, LaTeX error, fatal error,
emergency stop, undefined control sequence, or runaway argument.
