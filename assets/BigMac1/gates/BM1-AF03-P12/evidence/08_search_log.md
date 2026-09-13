# Search log

All searches were performed on 2026-08-29 (Asia/Shanghai).  Search-result
absence is recorded only relative to the named query/provider.

## Pass 1: source and statement lock

1. Web search: exact title `"Properties of plactic monoid centralizers"`.
   Located arXiv:2512.21401, the authors' PDF, and the Springer version of
   record.
2. Web search: DOI `"s00233-026-10652-4"`; opened
   <https://link.springer.com/article/10.1007/s00233-026-10652-4>.
   Springer reports received 2025-12-24, accepted 2026-06-10, published
   2026-06-24, volume 113, pages 242--262, issue date August 2026.
3. Opened <https://arxiv.org/abs/2512.21401> and the public author PDF
   <https://users.math.msu.edu/users/bsagan/Papers/Old/ppm.pdf>.  The visible
   manuscript date is 2026-03-22; arXiv initially submitted 2025-12-24.
4. In the paper, inspected the introduction, Theorems 2.13 and 3.7, and the
   text around Conjecture 3.8.  This established L02--L08 and exposed the
   prompt's incorrect “Conjecture 4.6” label.

## Pass 1: later work, citations, and code

Queries run:

- `"m-packed" "m-stable" plactic`
- `"3-packed" plactic centralizer`
- `"C'(u^k)" plactic`
- `"2512.21401" citations`
- `"Properties of plactic monoid centralizers" code GitHub`
- exact DOI plus `proof`, `counterexample`, `code`, and `GitHub`

The first pass returned the Sagan--Zhao paper, mirrors, author/seminar pages,
and unrelated uses of “3-packed”; it did not locate a later mathematical
paper resolving Conjecture 3.8.  This is only a bounded negative result.  A
second novelty pass is required before any publication claim.

An independent Gate 1 pass then checked Crossref, OpenAlex, Semantic Scholar,
author pages, the official PDF, later exact-phrase searches, and public code.
Its complete query/evidence record is `audit/literature_agent_report.md`.
Notable results:

- arXiv:2512.21401 was still v1 at the cutoff;
- Defant, arXiv:2605.19979v3, cites the area but solves the bounded-row and
  evacuation conjectures, not stability;
- Oberwolfach Report 2/2026, p. 143, records stability as open in January;
- the older Sagan--Wilson repository was found at
  <https://github.com/wilsoa/Centralizers-in-the-Plactic-Monoid>, but its
  committed notebook does not expose the complete larger 2026 test range;
- Google Scholar forward-citation access returned HTTP 429, and zero counts
  from other indices were demonstrably incomplete, so none was used as
  absence evidence.

## Primary URLs frozen

- Version of record: <https://doi.org/10.1007/s00233-026-10652-4>
- Springer article: <https://link.springer.com/article/10.1007/s00233-026-10652-4>
- arXiv record: <https://arxiv.org/abs/2512.21401>
- Public author PDF: <https://users.math.msu.edu/users/bsagan/Papers/Old/ppm.pdf>
- Independent Gate 1 report: `audit/literature_agent_report.md`
- Locked conclusion: `literature/NOVELTY_LOCK.md`

## Pass 2: release novelty check

Run on 2026-08-29 after the candidate full proof and before release.  The
following exact and scoped queries were repeated against the current web and
arXiv-indexed results:

- `"3-packed" plactic stable centralizer proof`;
- `"Properties of plactic monoid centralizers" citations 3-packed`;
- `arXiv plactic monoid packed stability centralizer 2026`;
- `"Conjecture 3.8" "plactic" stability`;
- `site:arxiv.org/abs/26 plactic centralizer stable packed word`;
- `site:arxiv.org plactic centralizer tropical stability 3 packed`;
- `"every 3-packed word" plactic`;
- `"3-stable" "plactic"`.

The results again returned Sagan--Zhao, Sagan--Wilson, the already audited
Defant paper, mirrors, and unrelated uses of “packed” or “stable.”  No public
proof, counterexample, or preprint settling the 3-packed endpoint was located.
The arXiv exact-record result for 2512.21401 remained the original source; no
newer version or resolving citation appeared in the returned sources.  This
is a provider- and query-relative negative result, not a global assertion of
nonexistence.  The release novelty gate therefore passes with that explicit
limitation.

## Pass 3: post-full-DAG release recheck

Run again on 2026-08-29 only after `audit/FULL_DAG_REFEREE.md` had issued its
hash-bound post-repair PASS.  This pass supersedes the earlier pre-release pass
for the final novelty gate.  Queries/providers included:

- exact title and DOI, with `citations`, `cited by`, `proof`, and
  `counterexample`;
- `"Conjecture 3.8" plactic monoid stable`, `"Conjecture 4.6" "m-packed"`,
  `"If u is m-packed then u is m-stable"`, and `"every 3-packed word"`;
- `site:arxiv.org` searches for `plactic centralizer stability packed word`,
  `m-packed m-stable`, and the exact source title;
- exact arXiv identifier `2512.21401` and searches for later versions;
- GitHub-scoped searches for the exact title, `3-packed`, both conjecture
  numbers, and `m-packed` together with `centralizer`.

Primary records re-opened were the Springer DOI page, arXiv:2512.21401, the
Sagan--Wilson arXiv record 2410.20460, and Defant arXiv:2605.19979v3.  The
current Springer HTML still exhibits inconsistent generated numbering: the
general stability conjecture is rendered as 3.8 near the introduction, while
the packed-word conjecture is rendered as 4.6 in Section 3.  The locally
archived source and the previously hash-recorded official PDF remain the
authority used in the project; the manuscript now makes only the locally
verified numbering statement.

Defant's abstract and Section 4 were checked directly.  Its two plactic
results are the bounded-row theorem and the evacuation theorem; neither is
packed-word stability.  Exact phrase searches returned Sagan--Zhao, the
author PDF, mirrors, and unrelated uses of “packed” or “stable.”  GitHub
searches returned no new relevant implementation or claimed solution.

No public proof, counterexample, or preprint settling the 3-packed endpoint
was located in this post-audit pass.  This is a dated, provider- and
query-relative negative result, not a claim of global nonexistence.
