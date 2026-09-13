# Search log

## Gate 1 pass 1: frozen claims (2026-08-29, Asia/Shanghai)

Before searching, the following project-changing claims were frozen: exact
conjecture and \(q\)-Fibonacci normalization; claimed \(n\le9\) baseline;
latest arXiv version; journal/DOI status; later corrections or resolutions;
citing literature; and public code.

## Gate 1 pass 2: primary-record and discovery searches

1. Opened `https://arxiv.org/abs/1312.2170` and queried the arXiv export API
   with `search_query=id:1312.2170`.  Result: one record, v1 only, submitted
   2013-12-08 03:39:09 UTC, 11 pages.  The abstract states the general product
   conjecture.
2. Downloaded the exact v1 TeX source from `https://arxiv.org/src/1312.2170v1`.
   Saved archive SHA-256:
   `4c38a62f21364500a69322f10d5ba69709153cf5349502ae6b898ebb7df58182`.
   Extracted TeX SHA-256:
   `6b4ea0bf537ad3f6dc4591f71247bef19a19a56f103bf541460f7e24a4f84561`.
   The final conjecture and “verified for n<=9” author report occur at TeX
   lines 780--792.
3. Queried Crossref (`query.bibliographic`, 100 rows) using the exact title
   and all four authors, then filtered for exact case-folded title equality.
   Result: no exact-title work.
4. Queried OpenAlex work `W2557966912`.  Result: type `preprint`, only
   submitted-version locations, DOI `10.48550/arXiv.1312.2170`, zero recorded
   citing works.  A separate `filter=cites:W2557966912` query also returned
   zero works.
5. Searched the exact title together with `journal`, `DOI`, `Conjecture`,
   `v_n`, and `product of q-Fibonacci`; searched the arXiv ID and exact title
   excluding arXiv/ResearchGate.  No formal publication, correction, or
   explicit resolution was found.  This is a bounded negative result.
6. Opened Peter L. Guo's institutional Nankai publication page.  It places
   the item under “Unpublished Manuscripts,” while separately listing journal
   publications.
7. Queried GitHub's repository API for `1312.2170`, the exact title, and
   `Kazhdan-Lusztig q-Fibonacci`; each query returned zero repositories.
   General web code searches also found no matching implementation.
8. Semantic Scholar's API was attempted but returned HTTP 429; this is an
   unresolved database coverage limitation, not evidence of absence.

## Gate 1 result: `NOVELTY_LOCK` (provisional research lock)

The exact 2013 conjecture and original \(n\le9\) author report are verified.
The source is an unpublished arXiv v1 manuscript; no journal version, later
resolution, citing work, or public code was found in the sources and queries
above.  The finite \(n=10\) computation is therefore a legitimate research
target.  Wording about global openness remains explicitly bounded and must be
rechecked in the mandatory second novelty pass before terminal release.

## Gate 5 second novelty pass (2026-08-29)

The second pass used fresh and differently phrased queries after the exact
finite result was known:

1. Exact-title searches combined with 2024, 2025, and 2026; searches for
   `Kazhdan-Lusztig`, `q-Fibonacci`, `R-polynomials`, `conjecture`, the printed
   `verified for n` phrase, and the displayed factor notation.  Results again
   returned the 2013 arXiv/ResearchGate copies and unrelated literature, but
   no later resolution.
2. A fresh Crossref 100-row title query, filtered to exact normalized title,
   again returned no record.
3. A fresh OpenAlex `filter=cites:W2557966912` query again returned count zero.
4. DataCite record `10.48550/arXiv.1312.2170` classifies the item as a 2013
   arXiv preprint and lists no related identifiers.  This confirms that the
   DOI is not evidence of a journal publication.
5. GitHub repository searches remained empty.  GitHub's unauthenticated code
   search endpoint returned HTTP 401, so repository search and general web
   code search---not global code-search completeness---are what was actually
   checked.
6. The Nankai author page continued to list the item under unpublished
   manuscripts.

No correction, counterexample, proof, `n=10` verification, or public code was
found.  The release therefore uses only the bounded wording “not found in the
recorded searches as of 2026-08-29.”  It does not assert that every database
is complete or that no private/unindexed work exists.
