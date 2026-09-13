# Fresh citation audit

## Scope, method, and frozen inputs

This release audit used the available `$citation-check-skill` explicitly in
search-verification mode as an advisory two-pass check.  The manuscript,
BibTeX database, extracted PDF text, accepted mathematical audit, exact
certificate/verifier, and `literature/user_bibliography_check.md` were read in
full as relevant.  The search date was 2026-09-09.  The user-designated
workbook recorded in `literature/user_bibliography_check.md` is authoritative
for the DOI and bibliographic metadata of references [2] and [3]
(`metadata_basis=user_designated_workbook`); official pages were nevertheless
refreshed successfully in this bounded audit.

The declared publication dependency list was checked against the TeX source.
It is complete: there are no imported figures, local styles, or `\input` files;
the only authored/build inputs are exactly the five sorted paths listed in
`publication.json`.  Generated `.aux`, `.bbl`, and PDF files are outputs, and
`plainurl.bst` plus the LaTeX packages are system dependencies.

## Pass 1: fixed claim extraction

The following list was fixed before source verification.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Averkov--von Dichter--Soprunov introduced the displayed Hypercube formulation. | Attribution/existence | p. 1, context |
| C02 | The cited source proves the `d=3` Hypercube Inequality. | Attribution | p. 1, context |
| C03 | In the consulted version, the Hypercube Inequality remains open for `d>=4`. | Attribution/temporal | p. 1, context |
| C04 | The source uses `d=n-1`, so `d=4` corresponds to geometric dimension `n=5`, not the proved `n=4` case. | Attribution/comparative | p. 1, context |
| C05 | The unrestricted `d=4` polynomial has approximately 400,000 terms. | Statistic/attribution | p. 1, context |
| C06 | Reference [2] uses symmetry reduction, integer predicates, checkable finite certificates, and explicitly separates finite-library results from ambient open problems. | Attribution | p. 2, context |
| C07 | Reference [3] proves exact positivity only on stated subdomains using retained exact certificates, including Bernstein certificates. | Attribution | p. 2, context |
| C08 | A bounded comparison located no publication of this particular five-support classification as of 2026-09-09; no priority is claimed. | Temporal/existence | p. 2, context |
| C09 | The paper's enumeration has 4,368 supports, 27 orbits, 10 dependent and 17 independent orbits, with census `(1360,2672,320,16)`. | Statistics | abstract and pp. 2--3 |
| C10 | The released standard-library verifier reconstructs the determinants, 384 cube actions, orbit coverage, and exact coefficient maps without floating point. | Existence/statistics | pp. 1, 3--4 |
| C11 | The theorem covers precisely supports of size at most five and leaves full HC4 unresolved. | Existence/scope | abstract, theorem, limitations |
| C12 | The PDF contains three resolved references whose displayed metadata agree with the bibliography records. | Existence | p. 4 |

## Pass 2: verification against fixed claims

| ID | Result | Evidence and support |
|---|---|---|
| C01 | Verified (exact/paraphrase) | arXiv:2608.14909v1, introduction item (iv) and Section 4.4 give the same normalized-volume Hypercube inequality. |
| C02 | Verified (exact) | The primary paper's Theorem 5.1 and Section 6 prove the `d=3` case. |
| C03 | Verified (exact) | Section 7.5 states that the inequality remains open for `d>=4`; the closing paragraph again singles out `d=4`. |
| C04 | Verified (exact) | Introduction item (iv) states `d=n-1`; Section 7.5 states explicitly that `d=4` corresponds to `n=5`. |
| C05 | Verified (source approximation) | Section 7.5 says the 16-variable, degree-eight `d=4` polynomial has approximately 400,000 terms.  The manuscript preserves the approximation word “roughly.” |
| C06 | Verified (paraphrase) | The official Preprints.org v1 page matches title, four authors, August 2026 record, and DOI.  Its abstract/Sections 3, 6, and 7 describe exhaustive symmetry-reduced enumeration, integer predicates, standard-library verification, retained certificates, and explicit finite-library limits. |
| C07 | Verified (paraphrase) | The official SSRN record matches title, five authors, August 2026 record, and DOI.  Its abstract states exact rational/algebraic and Bernstein certificates on sharply delimited local regions and explicitly disclaims the unrestricted parent assertions. |
| C08 | Verified as a bounded-search statement, not priority | Four targeted searches for the exact inequality, “five-support,” and the count 4368 returned the source paper or unrelated uses, but no equivalent classification.  The manuscript accurately disclaims priority. |
| C09 | Verified (exact) | Fresh execution of `evidence/verify_five_supports.py --check evidence/five_support_certificate.json` returned exactly the displayed counts and zero negative coefficients. |
| C10 | Verified (exact) | Direct inspection of the verifier and its successful JSON output confirms the stated reconstruction and integer-only certificate check. |
| C11 | Verified | The title, abstract, theorem, proof, and limitations consistently state the accepted at-most-five scope.  `audit/math.json` accepts exactly that scope and leaves the original status unresolved. |
| C12 | Verified (exact) | `main.aux` resolves all three citation keys, `main.bbl` contains all three entries, `main.blg` reports three used entries and zero BibTeX warnings, and rendered page 4 visibly contains all three records. |

## Sources consulted and metadata conclusions

1. G. Averkov, K. von Dichter, and I. Soprunov, *On the
   Log-submodularity for Zonoids: From Mixed Volume Inequalities to the
   Hypercube*, arXiv:2608.14909v1, especially introduction items (iv)--(v),
   Theorem 5.1, Section 6, and Section 7.5:
   <https://arxiv.org/html/2608.14909v1>.
2. Z. Zeng, H. Liu, K. Ratnavelu, and O. Seng Huat, *Exact Finite
   Certificates for the Four-Dimensional Ternary Borsuk Problem and
   Five-Dimensional Ternary Kissing Codes*, Preprints v1, official page:
   <https://www.preprints.org/manuscript/202608.1658>.
3. Z. Zeng, H. Liu, K. Ratnavelu, O. Seng Huat, and Y. Xiong, *Three
   Exact Local Positivity Islands and a High-Z Complex-Phase Tube for a
   Hermitian Rank-Two Scalar Gate*, official SSRN record:
   <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7348478>.
4. User-designated workbook record as transcribed and audited in
   `literature/user_bibliography_check.md`, cells `数学主表!A9:F9` and
   `数学主表!A29:F29`.

The academic search templates were run for each cited work (author/year/title,
full-title site query, author/year/venue, and DOI or arXiv identifier).  All
three sources exist and support the nearby prose at its stated level.  The two
workbook-selected comparisons are genuinely relevant but explicitly
methodological; the manuscript does not use them as premises for HC4.  No
citation is contradicted, unnecessary, undefined, or left unverified.

**Verdict: ACCEPT.**
