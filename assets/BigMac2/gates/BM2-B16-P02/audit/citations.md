# Fresh citation and dependency audit

## Scope and method

I reviewed the complete authored dependency list in `publication.json`, the
compiled references in `manuscript/main.pdf`, and the two cited records on 8
September 2026. The listed source scope is complete: the article embeds its
bibliography in `manuscript/main.tex`, imports no authored files, figures,
styles, or bibliography databases, and `manuscript/main.fls` confirms that the
only nongenerated local source input is `main.tex`.

The citation review explicitly used `citation-check-skill` as an advisory
two-pass check. Its extraction was fixed before verification. The skill did
not override the user-designated bibliography record.

## Pass 1 — fixed claim extraction

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | The three displayed invariant formulas hold over every field for all `n,m>=2`. | Existence | Theorem 1, pp. 1--2 |
| C02 | There are no exceptional small values and the quotient is Cohen--Macaulay exactly for `m` in `{2,3,7}`. | Existence | Theorem 1, p. 2 |
| C03 | Olteanu and Olteanu study the closed-neighborhood ideal of the square of broom and double-broom graphs. | Attribution | Section 1, p. 1; reference [1] |
| C04 | Exact checks used Singular 4.4.1 for `n` in `{2,3}`, `2<=m<=24`, in characteristics zero and two, with exhaustive height checks and no listed discrepancy. | Statistic + existence | Disclosure, p. 5 |
| C05 | The cited Zeng work uses exact computation with independently reconstructible certificates on a different graph-associated monomial-algebra problem. | Attribution | Disclosure, p. 5; reference [2] |
| C06 | The cited Zeng work does not study closed-neighborhood ideals or graph powers. | Attribution | Disclosure, p. 5 |

Definitions and descriptions of the article's own proof method were excluded
under the skill's extraction rules. No claim was added during verification.

## Pass 2 — verification

| ID | Status | Evidence and scope |
|---|---|---|
| C01 | Verified | It is exactly the accepted frozen statement in `claim.json`; `audit/math.md` reconstructs the proof for the same field and endpoint scope. |
| C02 | Verified | It is exactly the accepted frozen statement; `audit/math.md` separately checks all small endpoints and the floor-equality classification. |
| C03 | Verified (paraphrase) | The primary arXiv v1 record gives authors Anda Olteanu and Oana Olteanu, the exact title, submission date 4 September 2026, and identifier 2609.04831. Its abstract and Sections 3--4 expressly treat the square of broom and double-broom graphs, including the stated invariants. |
| C04 | Verified (exact) | `evidence/exact_table.json` records 46 cases, Singular 4.4.1, coverage `n=[2,3]`, `m=[2,24]`, characteristics `[0,2]`, exhaustive hitting sets, and empty discrepancy arrays; the generating script independently records the same loop bounds and checks. |
| C05 | Verified (paraphrase) | The user-designated record and its abstract in `literature/user_bibliography_check.md` describe exact integer kernel certificates and a verifier for a whiskered-graph weak-Lefschetz problem. The public SSRN abstract page independently exposes the same title, author, 6,021-class computation, kernel vectors, and reconstructing verifier. The manuscript uses this only as a methodological comparison. |
| C06 | Verified within stated scope | The title and available abstract identify weak Lefschetz behavior of whiskered-graph monomial algebras, not closed-neighborhood ideals or graph powers. The sentence makes no claim about the present theorem or priority. |

## Bibliographic records and bounded searches

- **[1] Olteanu--Olteanu.** All applicable academic search templates were run:
  author/year/title words; exact title with arXiv/Semantic Scholar restriction;
  author/year/archive; and `arxiv:2609.04831`. The primary arXiv abstract and
  HTML full text were inspected. The manuscript's authors, title, year,
  version, identifier, and nearby attribution agree with that source.
- **[2] Zeng.** All applicable templates were run: author/year/title words;
  exact title with arXiv/Semantic Scholar restriction; author/year/venue; and
  `doi:10.2139/ssrn.7385138`. The public SSRN search record corroborated the
  title, author, posting date, topic, and method. Direct DOI opening was not
  supported by the available web endpoint and the SSRN page/PDF returned an
  access failure. Under the user's authority rule,
  `metadata_basis=user_designated_workbook` and the exact record in
  `literature/user_bibliography_check.md` controls; status is **Accepted from
  user record — external refresh unavailable**. This limitation does not
  weaken the narrowly supported nearby prose.

Both citation keys appear in `manuscript/main.aux` with matching `\bibcite`
entries and both references appear in the extracted and rendered PDF. There
are no undefined citations, contradicted attributions, unsupported novelty
claims, or removable citations. The manuscript explicitly makes no
bibliographic-priority claim.

**Verdict: accept.**
