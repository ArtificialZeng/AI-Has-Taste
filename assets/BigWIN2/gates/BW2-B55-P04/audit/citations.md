# Citation and bibliography audit

Verdict: **accept**.  The two-pass citation-check protocol froze 19 claim pairs
in `audit/claim-ledger.json` and then verified them without re-extraction.  All
19 are verified; there are no numerical errors, hallucinations, misleading
claims, unverified claims, or undefined citations.  Detailed passage locators
and verification evidence are in `audit/source-verification.md` and
`audit/claim-verification.json`.

| Key | Bibliographic record | Nearby support | Result |
|---|---|---|---|
| `LocatelliCoteCoelho2026` | Exact title, three authors, 2026, arXiv:2609.03219v1 verified at the official arXiv record | Sections 4.2, 6.2, 6.3 and Figure 3 support the branching rules, completion test, almost-exact rule, and five-job unsafe event | verified, no repair |
| `TangDenardo1988` | Exact title, authors, Operations Research 36(5):767--777, 1988, DOI verified at INFORMS | Publisher abstract supports the model; the primary Locatelli paper identifies Tang--Denardo's KTNS as solving fixed-sequence loading | verified, no repair |
| `Zeng2026Whiskered` | Exact title, author, 2026 SSRN record and DOI verified at SSRN | Official abstract directly supports exhaustive canonical enumeration, exact integer arithmetic, and a short verifier | verified, no repair |

All three retained keys have ordinary body-flow `\cite{...}` uses and appear in
the canonical `manuscript/references.bib`; no key changed.  The automated key
audit reports three cited keys, three BibTeX entries, and no missing or unused
entries.  The bibliography is not user-library-only: it includes the natural
primary sources for the model origin and exact rule/closest prior construction.
The one selected library record is relevant but nonessential, as the manuscript
states.  No decorative references or missing natural dependencies were found.

Scope: source existence, author/title/date/version/venue metadata, nearby-claim
support, hypotheses, closest-result comparison, coverage, and citation-key
consistency were checked on 2026-09-07.  The full Tang paper was not locally
available; its publisher record/abstract and the complete current primary SSP
paper were used for the exact claims retained.  This limitation does not leave
any nearby claim unsupported.

