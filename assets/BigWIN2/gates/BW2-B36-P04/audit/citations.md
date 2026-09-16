# Fresh citation and bibliography audit

Job: `win-00036-p04-release-23764c16e129`  
Search date: 2026-09-06  
Method: `citation-check-skill` two-stage search-mode audit and the
`bib-reference-audit` protocol. The user prohibited subagents, so the release
worker performed the four-reference audit directly.

## Frozen extraction pass

Before assigning verification statuses, seven claim/citation pairs and all four
ordinary body-flow cite commands were frozen in
`audit/citation-claim-ledger.json`, bound to manuscript SHA-256
`936f62dc423ede553a7e98c6449866ab357034d8b6efb1c0e9c713fcd9176452`.
No claims were added in the verification pass.

## Independent verification pass

For each paper, searches covered author/year/title words, exact title, venue,
DOI, and arXiv identifier when present. Publisher pages, an arXiv primary copy,
an author-hosted primary PDF, and the exact text of the 1975 article were used;
search snippets were used only to locate records. The new Zeng item was checked
against the preserved publisher-deposited Crossref REST response because the
live SSRN full text remained unavailable. That capture records endpoint, HTTP
status 200, byte length, and exact response SHA-256.

| Claim | Exact source location and support | Status |
|---|---|---|
| CIT-001 | Crossref deposited record for DOI `10.2139/ssrn.7395382`: author, title, posted-content/preprint type, posted year 2026, and abstract recurrence. | Verified, exact/paraphrase |
| CIT-002 | Same deposited abstract: exact certificate `7 795 379 | a20`. | Verified, exact |
| CIT-003 | Same deposited abstract, final sentence: no assertion for indices at least 22. | Verified, exact |
| CIT-004 | Jones, publisher abstract and Theorem 1.2 in arXiv `math/0612415`: the family `x^2+k`, integral `k` other than `-1`, has density zero for every integral initial point. | Verified, paraphrase |
| CIT-005 | Brillhart--Lehmer--Selfridge (1975), Theorem 1, p. 622: complete-factorization `N-1` primality test. | Verified, paraphrase |
| CIT-006 | The same theorem requires noncongruence modulo `N`; gcd equal to 1 implies that noncongruence, so the manuscript's stated hypothesis is stronger. | Verified, interpretation |
| CIT-007 | Grégoire--Théry--Werner (2006), abstract p. 97 and §§1.3, 3--4, pp. 100--106: computations/certificate generation outside the proof checker and certificate checking in Coq. | Verified, paraphrase |

The Zeng source's full-text limitation is disclosed, and no statement from that
preprint is used in the proof. The Jones result is correctly described as
asymptotic. The 1975 criterion has matching complete-factorization hypotheses.
The Coq comparison expressly distinguishes that formal system from the note's
ordinary Python checker. No cited claim is strengthened beyond its source.

## Bibliography coverage and consistency

The bibliography contains the one genuinely relevant active-library paper plus
three primary sources naturally used by the manuscript: closest available
same-recurrence context, arithmetic-dynamical background, the nontrivial
primality criterion, and the certificate-checking technique. Each is cited at
its actual claim; none is decorative. Registry row 46 remains the only active
49-entry first-sheet item supporting the same-recurrence comparison, so the
selection of one library item is justified and no second library citation was
padded in.

All four entries agree with the checked records on title, authors, year, venue,
pages, and DOI. The Zeng block is the checksum-bound registry BibTeX. The other
three retained entries match the supervisor leads after primary-source
verification; no unverified field was added and no key changed. The canonical
file is `manuscript/references.bib` only.

The bibliography checker reports four cited keys and four entries, zero missing
or unused keys, and exact AUX agreement. The converged log and BLG have no
undefined citation, missing/repeated database entry, BibTeX warning, or LaTeX
error. Verdict: **accept**.
