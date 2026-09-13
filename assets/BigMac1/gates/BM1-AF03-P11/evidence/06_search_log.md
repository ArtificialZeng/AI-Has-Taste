# Search log

## Pass 1: frozen claims (2026-08-29)

Before searching, the following boundary-changing claims were frozen: exact
source/DOI/publication dates; exact definition of `M_N`; exact wording and
reported verification range of Conjecture 4.4; latest arXiv version; later
solutions/corrections/citations; associated public code; and whether `n=7`
is still the first publicly unverified relation.

## Pass 2: primary-record searches

All times below are UTC on 2026-08-29.

| Time | Query or endpoint | Result |
|---|---|---|
| 12:06 | ECA PDF `https://ecajournal.haifa.ac.il/Volume2025/ECA2025_S2A18.pdf` | Read the six-page journal paper. Verified metadata, definitions, Theorems 1.1/1.2, Conjectures 4.3/4.4, and the `n<=6` author report. |
| 12:06 | ECA volume index and DOI `10.54550/ECA2025V5S3R18` | Verified ECA 5:3 (2025), S2R18 and canonical DOI. |
| 12:07 | arXiv `https://arxiv.org/abs/2405.01854` and source archive | Record lists only v1, 2024-05-03. Source archive contains TeX/BibTeX only; no enumeration code. |
| 12:08 | Web exact-title, exact-conjecture, `minimally-sorted`, and `s_{123,132}` searches | Located the source paper and one adjacent set-partition paper; no solution of Conjecture 4.4. |
| 12:10 | Crossref API for DOI | Canonical journal metadata; `is-referenced-by-count=0`. Crossref's malformed extra author-like organization field was not used for authorship. |
| 12:10 | OpenAlex work `W4409744009` and `filter=cites:W4409744009` | Journal record found; `cited_by_count=0`; citing-work query returned zero. |
| 12:10 | Semantic Scholar Graph API for `ARXIV:2405.01854` | `citationCount=1`, identifying arXiv:2408.05377, *More results on stack-sorting for set partitions*. |
| 12:11 | arXiv `https://arxiv.org/abs/2408.05377` | Abstract concerns sock sequences/set partitions, image algorithms, preimages, and fertility; no claimed result on Conjecture 4.4. |
| 12:11 | GitHub repository API for exact phrase `minimally-sorted permutations` | Zero repositories. Unauthenticated GitHub code-search API returned 401, so the negative code claim does not rely on it. |
| 12:12 | Web `site:github.com` searches for exact title, `s_{123,132}`, `minimally-sorted permutations`, and author/title terms | No relevant repository result. |
| 12:14 | Exact initial count-string and OEIS-oriented web searches | No matching sequence for `M_N` was located. Search results with coincident terms were unrelated. |
| 12:31 | Exact title/DOI search for Berlow's *Restricted stacks as functions* | Verified the publisher record: *Discrete Mathematics* 344(11) (2021), 112571, DOI `10.1016/j.disc.2021.112571`. |
| 12:32 | arXiv `https://arxiv.org/abs/2008.01164` and open manuscript | Verified v2 (2021-06-11), Definition 1.3 of `s_T`, and Theorem 4.5 that the periodic points of `s_{123,132}` are exactly the half-decreasing permutations. |

## Novelty lock decision

`NOVELTY_LOCK` is provisionally **PASS** as of 2026-08-29: the exact source
and frontier are verified, and no public proof, disproof, `n=7` certified
count, correction, or associated code was found in the recorded sources.
This is a bounded search statement, not proof of worldwide absence.  A second
novelty pass is mandatory before any publishable release.

The source boundary needs one explicit repair: “first unverified” means first
beyond the source author's reported `n<=6` computation and beyond the above
searches.  It is not assumed as an absolute historical fact.

## Pass 3: post-result fingerprint search (2026-08-29)

After the exact endpoint and its certificate were known, a separate search
used result-specific fingerprints rather than the broad pre-result queries:

| Query | Result |
|---|---|
| exact pair `"47,265,120" "378,120,960"` with stack-sorting terms | no relevant result |
| `"Q_14" "Q_13" "minimally-sorted permutations"` | no relevant result |
| exact candidate title `"A Certified n=7 Case"` with stack-sorting terms | no relevant result |
| `"Conjecture 4.4" "minimally-sorted" permutations` | only the Zhang source paper was located |

The result page for the last query again exposed the primary ECA article and
its exact statement that Conjecture 4.4 had been computationally verified for
`n<=6`; the other displayed results were unrelated uses of labels `Q_13` and
`Q_14`. No matching preprint, paper, correction, source repository, or exact
count pair was located. This is a dated, bounded negative search and does not
establish absolute priority.

The mandatory post-result novelty pass is therefore **PASS** for release with
the manuscript's deliberately limited wording “first relation beyond that
reported range.”
