# Search log

## 2026-08-29 Gate 1 pass 1: pre-search freeze

Before opening web search results, claims C01--C09 were frozen in
`claim_ledger.md`.  Planned primary-source targets are: arXiv abstract/version
history and source/PDF; Elsevier/ScienceDirect or Crossref DOI metadata; the
paper's bibliography and theorem locations; forward-citation databases and
the citing papers themselves; author/repository/code searches.  Negative
searches will be reported with their exact query strings and scope.

## 2026-08-29 Gate 1 pass 2: primary-source verification

- Opened <https://arxiv.org/abs/2407.14091>, its PDF, and v1 HTML.  The
  record has only v1, submitted 19 July 2024 07:56:57 UTC.  Theorem 1.1
  (PDF p. 2) and Conjecture 4.1 (PDF p. 8) exactly support C01 and C02.
- Repaired a chronology nuance in the user source: the proof was publicly
  available as an arXiv preprint in 2024 and formally published in 2026.
- Audited the \(d=0,1,2\) chain: \(d=0\) is the classical EKR theorem;
  \(d=1\) is Huang--Zhao, arXiv:1605.07535, Theorem 1.1; \(d=2\) follows
  from Huang--Zhang Theorem 1.1 because its threshold becomes \(2k+1\).
  Hao Huang--Yi **Zhao** (the \(d=1\) source) must not be confused with Hao
  Huang--Yi **Zhang** (the current paper).
- Queries: `site:sciencedirect.com "On a d-degree Erdős–Ko–Rado Theorem"
  106163`, exact title plus `DOI`, and exact DOI
  `10.1016/j.jcta.2026.106163`.  Elsevier's PII record is
  <https://www.sciencedirect.com/science/article/abs/pii/S0097316526000063>.
- GET <https://api.crossref.org/works/10.1016%2Fj.jcta.2026.106163>
  confirmed the two authors, journal, volume 221, article 106163, July 2026,
  and DOI.  Its `is-referenced-by-count` was 0 at query time; this is scoped
  negative evidence rather than proof of no citations.
- GET <https://api.openalex.org/works/https://doi.org/10.1016/j.jcta.2026.106163>
  returned OpenAlex work W7125708255 and `cited_by_count: 0` at query time,
  again only database-scoped negative evidence.
- The Semantic Scholar API exact-record request returned 429 and contributes
  no evidence.
- The original EKR bibliography has a minor page-range discrepancy: the
  Huang--Zhang reference gives pp. 313--318, whereas the Oxford publisher
  record for DOI 10.1093/qmath/12.1.313 gives pp. 313--320.  Any new
  bibliography will use the publisher range.
- A later primary paper, Gan--Han--Im, arXiv:2605.17945 (18 May 2026), gives
  a \(d=k-1\) threshold that specializes to \(n\ge14\) at \(k=4\), so it
  does not change the \(n=9,10\) frontier and is weaker here than the
  Huang--Zhang threshold \(n\ge11\).

## 2026-08-29 Gate 1 pass 2: later literature and novelty

The following exact-title/identifier/parameter query families were run in
general web search and, where supported, database full-text search:

```text
"On a d-degree Erdős-Ko-Rado Theorem"
"On a d-degree Erdos-Ko-Rado Theorem"
"2407.14091"
"10.1016/j.jcta.2026.106163"
"Huang and Zhang" "2k+2d-3"
site:arxiv.org/abs "minimum d-degree" "intersecting family"
site:arxiv.org/abs "codegree version" "Erdős--Ko--Rado"
"k=4" "d=3" "Erdős-Ko-Rado"
"(k,d)=(4,3)"
"n=9" "minimum 3-degree" intersecting
"n=10" "minimum 3-degree" intersecting
"Conjecture 4.1" "Huang" "Zhang" Erdős
"On a d-degree Erdős-Ko-Rado Theorem" correction OR erratum
```

- The only later ordinary-set result found that directly discusses the
  codegree case is L. Gan, J. Han, and S. Im, *Note on the codegree version
  of the Erdős--Ko--Rado theorem*, arXiv:2605.17945v1 (18 May 2026),
  <https://arxiv.org/abs/2605.17945>.  Its Theorem 1.2 assumes
  \(n\ge2k+\lceil(\sqrt{8k+1}-1)/2\rceil+3\), which gives \(n\ge14\) for
  \(k=4\); it does not cover 9 or 10.
- Y. Shan and J. Zhou, *d-Degree Erdős--Ko--Rado theorem for finite vector
  spaces*, arXiv:2411.17985 and DOI 10.1007/s10474-025-01543-1, cites the
  Huang--Zhang set theorem but proves a \(q\)-analogue.  Its text provides no
  implication to the ordinary set endpoints via \(q=1\).
- Crossref and OpenAlex each reported zero indexed forward citations at query
  time.  Semantic Scholar returned Shan--Zhou plus a duplicate record but
  omitted Gan--Han--Im.  This observed incompleteness is why full-text search,
  rather than citation counts alone, controls the lock.
- No correction or erratum was found.  No result found in this bounded pass
  resolves \((4,3,9)\), \((4,3,10)\), or the full \((4,3)\) set family.

Limitations: Google Scholar returned 429 and ADS returned 405; citation APIs
have lag and record splitting; searches cannot exclude unpublished, private,
unindexed, or very recent work.  The conclusion is exactly “no prior
resolution found by the recorded searches as of 2026-08-29.”

## 2026-08-29 Gate 1 pass 2: public code and certificate search

Searched public GitHub repositories, issues/PRs, and authenticated public code
for the arXiv ID, exact title, DOI, PII, `d-degree EKR`, `Erdos-Ko-Rado SAT`,
`LRAT`, `DRAT`, `delta_3 intersecting family`, `minimum 3-degree`, `k4d3`,
and the explicit \(n=9,10,k=4\) parameter phrases.  All completed relevant
queries returned zero results.  Representative reproducible code-search URL:
<https://github.com/search?q=%222407.14091%22+is%3Apublic&type=code>.

GitLab project API searches for `2407.14091`, the exact title, `d-degree EKR`,
and `Erdos Ko Rado SAT` returned zero projects.  Zenodo API searches for the
arXiv ID, exact title, and related identifier `10.48550/arXiv.2407.14091`
returned zero records.  The arXiv source is a single `main.tex` with no
ancillary bundle or software link.  The Crossref record has an empty
`relation` object and no data/software DOI; Hao Huang's publication page
<https://blog.nus.edu.sg/huanghao/publications/> lists no code link.

Limitations: private/unindexed/unlinked or differently named artifacts,
institutional storage, and publisher supplements hidden by access controls may
be missed; GitLab search covered project metadata rather than every blob; no
author was contacted.  The defensible conclusion is only “no public artifact
found by these searches.”

## Local proof-tool inventory at Gate 1

CaDiCaL 3.0.1 is installed at `/opt/homebrew/bin/cadical`.  Its help exposes
textual LRAT (`--lrat --no-binary`) and internal proof checking
(`--checkproof=3`).  No independent external `lrat-check`, `drat-trim`,
`gratgen`, `veripb`, or similar checker was installed.  Therefore CaDiCaL's
own internal check is discovery evidence only; Gate 4 must stage and pin a
genuinely separate checker or use an equivalently strict independent
certificate route.

## 2026-08-29 Gate 1 second novelty pass

An isolated second search repeated and broadened the first pass after the
proof and certificates were complete.  It again found no earlier public
source establishing either endpoint \(n=9\) or \(n=10\), and no public code or
certificate for these instances.  The result is a bounded negative PASS, not
an absolute priority proof.

The second pass rechecked Huang--Zhang's Theorem 1.1 and Conjecture 4.1,
Gan--Han--Im arXiv:2605.17945, Shan--Zhou's finite-vector-space analogue, and
later adjacent work on degree powers, degree-vector norms and inner products,
and minimum positive codegree.  None gives a bound on the minimum over all
triples at the two ordinary-set endpoints.  In particular, the
Gan--Han--Im threshold

\[
n\ge 2k+\left\lceil\frac{\sqrt{8k+1}-1}{2}\right\rceil+3
\]

specializes to \(n\ge14\), not \(9\) or \(10\), when \(k=4\).  The adjacent
records inspected included Cao--Lu--Zhang
<https://arxiv.org/abs/2607.28616>, Zhao--Wang
<https://arxiv.org/abs/2608.04615>, a cross-intersecting degree-vector paper
<https://arxiv.org/abs/2608.17219>, and Spiro's positive-codegree paper
<https://arxiv.org/abs/2110.10317>.

Additional representative exact queries included:

```text
"For every n>=9" intersecting family "delta_3" 4
"every intersecting family" "delta_3" "n\\ge 9"
"δ_3" intersecting "n=9" 4-uniform
"minimum 3-degree" intersecting family "n=9"
"(k,d)=(4,3)" Erdős Ko Rado
"delta_3(F)" intersecting family 4-sets
"minimum (k-1)-degree" "intersecting" Erdős Ko Rado
"n=8" "minimum 3-degree" intersecting
"35" "minimum triple degree" intersecting family
"binom{n-d-1}{k-d-1}" intersecting family
"Conjecture 4.1" "On a d-degree"
"2407.14091" correction OR erratum OR corrigendum
"2605.17945" correction OR erratum OR v2
site:github.com "delta_3" "intersecting family" "n=9"
site:zenodo.org "2407.14091" OR "d-degree Erdős-Ko-Rado"
```

Database/API routes included arXiv exact IDs and field searches, Crossref
singletons/title searches, OpenAlex forward-citation filters, and Semantic
Scholar.  Crossref and OpenAlex returned zero linked forward citations, but
their record splitting failed to link Gan--Han--Im's explicit citation; hence
those counts are not treated as complete.  Semantic Scholar returned HTTP
429, Google Scholar was unavailable, and no author was contacted.  Private,
unindexed, same-day, or differently worded work remains outside the search
guarantee.

This audit caused one manuscript change: categorical wording such as
“previously open” was replaced by “the values not covered by Huang and
Zhang's theorem,” and novelty is stated only as “to the best of our
knowledge,” with the search date displayed.
