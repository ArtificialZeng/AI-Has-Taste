# Citation and bibliography audit

Verdict: **accept**. Search verification was performed on 2026-09-06 with the
required two-pass procedure. Pass 1 froze all eight body-flow claim/citation
pairs in `audit/citation-claim-ledger.json`; Pass 2 used that ledger without
re-extraction and recorded its results in `audit/citation-verification.json`.

All three cited works exist and their author, title, date/version, venue and
identifier data were checked against primary records. Greaves--Tan v1 was
inspected at Sections 3.1--3.2, Proposition 3.1, the definition
`A_Gamma=A_2+A_4`, Theorem 4.3, Example 5.1 and Question 5.4. Paley's Wiley
version-of-record metadata verifies volume 12, issue 1--4, pages 311--320 and
DOI 10.1002/sapm1933121311; the cited construction is also explicitly invoked
in Greaves--Tan's derivation of their Theorem 1.1. The selected SSRN primary
record's abstract expressly describes exhaustive canonical graph enumeration,
exact certificate vectors and a short reconstruction verifier, which supports
only the nearby methodological analogy.

The applicable academic searches were all run: author/year/title words, exact
full title restricted to Semantic Scholar or arXiv, author/year/venue, and DOI
(plus arXiv ID where applicable). No source conflict was found. The sole
bibliographic repair was to change the Greaves author field from unsupported
middle initials to the arXiv primary record's `Gary Greaves`; no citation key
changed. BibTeX key and AUX checks found three cited keys, three database
entries, no missing or unused keys, and no AUX mismatch.

Coverage is complete without padding: Greaves--Tan is the problem origin,
closest prior result and source of every nontrivial construction/hypothesis;
Paley is the primary historical construction used for the fixed matrix; and
the one selected active-library paper supports the explicit exact-certificate
methodology comparison. A second library paper would merely duplicate that
narrow comparison, so the bound selection records a specific one-reference
explanation. Every retained item has a direct ordinary body-flow `\\cite`.
The bibliography is not user-library-only. No decorative citation remains.

The user explicitly prohibited sub-agents, so the main release worker performed
the same per-key protocol serially. The failed WSL `curl` was not treated as
evidence; authoritative web records were inspected, and the project contained
no `literature/bibliography-revision-*.md` or `literature/crossref-*` captures.
