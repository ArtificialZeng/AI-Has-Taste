# Raw Search Record for Independent Referee/Novelty Audit

**Search date:** 2026-08-29  
**Local time zone:** Asia/Shanghai (UTC+08:00)  
**Last recorded local timestamp:** 2026-08-29T21:04:16+08:00  
**Cut-off represented by this log:** public material discoverable by the queries below at that time.  
**Important:** zero hits and zero citation counts are database observations, not proofs of nonexistence or openness.

## Frozen questions

| ID | Question frozen before searching |
|---|---|
| Q1 | What exactly do Definition 2.1, Definition 2.2, Theorem 2.9, and Conjecture 5.1 say in arXiv v1, v2, and the journal version? |
| Q2 | What is the formal journal DOI/issue/PII metadata, and is there a correction or later arXiv version? |
| Q3 | Does Braun--Jal prove only Conjecture 5.1(1), or also the Ehrhart-root disk part? |
| Q4 | What later papers cite/use the original work, and does any resolve the corrected disk endpoint or length 10? |
| Q5 | Is associated public code/data/certificate material available? |
| Q6 | What is the exact corrected length-10 statement after reconciling the source notation? |

## Primary source retrievals

| Time (local, approximate) | Request/query | Result used |
|---|---|---|
| 20:35--20:40 | <https://arxiv.org/abs/2411.18695> | Current version v2; submission history v1 2024-11-27, v2 2026-02-27; comments say accepted in *Discrete Mathematics*. |
| 20:35--20:40 | <https://arxiv.org/html/2411.18695v1> | Definition 2.1/2.2, Theorem 2.9, and Conjecture 5.1 extracted. |
| 20:35--20:40 | <https://arxiv.org/html/2411.18695v2> | Same clauses extracted; Conjecture 5.1 still says length $n+1$, positive disk center, negative axis. |
| 20:35--20:40 | <https://arxiv.org/abs/2607.00922> and <https://arxiv.org/html/2607.00922v1> | v1 only, submitted 2026-07-01; abstract and Section 4 state proof of $h^*$-real-rootedness / Conjecture 5.1(1). |
| 20:40--20:45 | <https://doi.org/10.1016/j.disc.2026.115072> | Redirected to Elsevier PII `S0012365X26000968`. |
| 20:40--20:45 | Crossref REST: `GET https://api.crossref.org/works/10.1016%2Fj.disc.2026.115072` | DOI metadata: Elsevier BV; *Discrete Mathematics* 349(9), 115072; issue date 2026-09; DOI record created 2026-03-10; version-of-record CC BY licence start 2026-02-24; 25 references; no update/correction relation; `is-referenced-by-count=0` at query time. |
| 20:40--20:45 | Elsevier REST core-data query for PII `S0012365X26000968` | PII, title, journal, cover date 2026-09-30, open-access flag, CC BY 4.0. Full text API without a key returned core data / invalid-view errors. |
| 20:40--20:45 | <https://escholarship.org/uc/item/6n85w7mx> and indexed PDF text | Repository identifies the journal DOI/version. Search-indexed final text reproduces Conjecture 5.1 with the same `length n+1` and sign inconsistency. Direct shell download was blocked/empty by CloudFront; no local journal-PDF hash is claimed. |
| 20:45--20:50 | DataCite `GET /dois/10.48550/arxiv.2411.18695` | v1/v2 dates confirmed; no related identifiers supplied in that DataCite record. |
| 20:45--20:50 | DataCite `GET /dois/10.48550/arxiv.2607.00922` | Braun--Jal v1 dates/authors confirmed; no related journal identifier supplied. |
| 20:45--20:50 | Crossref exact-title-style search for Braun--Jal | No matching journal DOI found; results matching `generalized snake posets` were the 2022 and 2026 Lee et al. journal articles. Query ranking was noisy, so this is only negative search evidence. |

## Downloaded arXiv artifacts (temporary, outside project deliverables)

| Artifact | SHA-256 | Inspection |
|---|---|---|
| `2411.18695v1` PDF | `77549ea9d5a5d4a5424b8a6249605a8f0011d0f9e1d5ee3d5305b22829dfecb3` | 30 pages; printed Conjecture 5.1 defect present. |
| `2411.18695v2` PDF | `86defc823e76cc8b850a5bedef94e2012bd32ca3cbc1fd1b2c31918a09f04f53` | 30 pages; same defect present. |
| `2411.18695v1` source | `a30646be5376bdb6e7f110d4b4c07d42ea5965140fdc438f7019abde347db30e` | LaTeX/bib/figures; no Sage code. Source line contains `|z - (n+4)/2|`. |
| `2411.18695v2` source | `70f8c81c921f5c2534caf83fc9653e1d50306cb54b56abb227281d2b9054a2e5` | LaTeX/bib/figures; no Sage code. Same source expression. |
| `2607.00922v1` source | `eea3b6fcd050dbd765ba9df7f4ad98ae596953b664cb2a8e96034691658b199a` | `main.tex`, bibliography, arXiv metadata. Section 4 explicitly names Conjecture 5.1(1); no `disk` or Ehrhart-root-location endpoint. |
| `2102.11306v2` source | `b6a836efbb5006272f1e4dc691360920aa82dd891e0f923b997f14f0c161ed69` | Original generalized-snake definitions checked against Lee et al. |

Commands used (temporary paths omitted here):

```bash
curl -L https://arxiv.org/pdf/2411.18695v1 -o snake_v1.pdf
curl -L https://arxiv.org/pdf/2411.18695v2 -o snake_v2.pdf
curl -L https://export.arxiv.org/e-print/2411.18695v1 -o snake_v1.tar
curl -L https://export.arxiv.org/e-print/2411.18695v2 -o snake_v2.tar
curl -L https://export.arxiv.org/e-print/2607.00922v1 -o bj_v1.tar
curl -L https://export.arxiv.org/e-print/2102.11306v2 -o snake2022_v2.tar
pdftotext -layout FILE.pdf FILE.txt
rg -n -i 'Conjecture 5\.1|disk|Sage|github|code|repository' EXTRACTED_SOURCE
sha256sum ARTIFACTS
```

## Web-search queries and observed frontier

Search engine queries were run without a recency filter unless stated. Representative exact queries:

```text
site:arxiv.org/abs/2411.18695 Generalized snake posets order polytopes lattice-point enumeration
"Generalized snake posets, order polytopes, and lattice-point enumeration" DOI
site:arxiv.org/abs/2607.00922 Braun Jal Order polytopes generalized snake posets
"Conjecture 5.1" "generalized snake" Ehrhart
10.1016/j.disc.2026.115072 site:sciencedirect.com
"Generalized snake posets, order polytopes" 115072
"2411.18695" github
"Generalized snake posets, order polytopes, and lattice-point enumeration" -Lee -ResearchGate
"2411.18695" -arxiv -ResearchGate
"10.1016/j.disc.2026.115072" -doi.org
"Ehrhart" "generalized snake posets" roots
"All roots" "generalized snake word" Ehrhart
"contained in the disk" "snake words" Ehrhart
"snake words of length up to 9"
"generalized snake" "length 10" Ehrhart
"Generalized snake posets" corrigendum
"Generalized snake posets" correction Ehrhart
"115072" corrigendum snake posets
"2411.18695v3"
"Order polytopes of generalized snake posets are h-real-rooted" DOI
"Benjamin Braun" "Aryaman Jal" generalized snake journal
Ehrhart polynomial roots disk h-star real-rooted theorem
Ehrhart transform preserves roots disk real negative h* polynomial
Ehrhart polynomial root bounds palindromic real-rooted h-star
Rodriguez-Villegas transform negative real roots Ehrhart disk
```

Observed high-value results:

- original arXiv/article and final repository version;
- Braun--Jal arXiv v1;
- Higashitani--Matsushita--Tani arXiv:2501.05720;
- the 2022 source paper, DOI <https://doi.org/10.5070/C62359166>;
- author publication page listing *Discrete Mathematics* 349(9), 115072, 21 pp.;
- secondary MathDB page that labels the conjecture open but mechanically repeats the malformed printed formula;
- secondary SymCat pages recording Braun--Jal's $h^*$ result, not the Ehrhart disk;
- no exact-match solution/counterexample/length-10 certificate.

Secondary pages were used only as search leads, never as decisive evidence for theorem content.

## arXiv API queries

Endpoint pattern:

```text
https://export.arxiv.org/api/query?search_query=QUERY&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending
```

| Query | Total | Relevant returned records |
|---|---:|---|
| `all:"generalized snake posets"` | 4 | 2102.11306, 2411.18695, 2501.05720, 2607.00922 |
| `all:"Ehrhart" AND all:"snake posets"` | 2 | 2411.18695, 2607.00922 |
| `all:"2411.18695"` | 0 | arXiv full-text search does not reliably index bibliography identifiers; zero is not meaningful by itself. |
| `all:"root location" AND all:"generalized snake"` | 0 | No arXiv record returned. |

The four-record exact-phrase frontier is the strongest bounded public-preprint observation in this audit. It does not cover non-arXiv manuscripts, private drafts, or text using substantially different terminology.

## Citation-index checks

| Service/query | Observation | Limitation |
|---|---|---|
| Crossref DOI record for `10.1016/j.disc.2026.115072` | `is-referenced-by-count: 0` | Braun--Jal is an arXiv preprint and need not be represented in Crossref cited-by counts; count is known incomplete. |
| OpenAlex DOI record `W7134947511` | `cited_by_count: 0` | OpenAlex also stored a separate arXiv record, and recent records were not merged/indexed completely. |
| OpenAlex title search | Separate original preprint and journal records; two duplicate Braun--Jal records; zero citation counts | Duplicate fragmentation makes the zero counts non-dispositive. |
| Semantic Scholar link from arXiv | Resolved original to paper ID `665107f68435dd938266ab6de5249cc7edb3af11` and Braun--Jal to `93f48f56ce6d0254c48563b1d495732ac49b89ad` | Graph API subsequently returned HTTP 429. No citation-count conclusion was drawn. |
| Exact-title general web search | Located Braun--Jal and Higashitani--Matsushita--Tani as substantive later works | Search-engine coverage/ranking is not exhaustive. |

## Public-code/data queries

### GitHub REST repository search

Queries (each `per_page=100`):

```text
generalized snake posets
2411.18695
2607.00922
snake poset Ehrhart
```

All four returned `total_count=0` for repositories at query time.

GitHub code search for `"2411.18695"` returned:

```json
{
  "message": "Requires authentication",
  "status": "401"
}
```

Therefore no claim is made about authenticated GitHub code search, private repositories, forks with unrelated names, or unindexed code.

General web queries:

```text
site:github.com "Generalized snake posets"
site:github.com "snake posets" Ehrhart
site:github.com "2411.18695"
site:github.com "2607.00922"
site:github.com Eon Lee "generalized snake"
site:github.com "Andrés R. Vindas-Meléndez"
site:github.com Aryaman Jal "generalized snake"
site:github.com "Ehrhart" "snake words of length"
```

No associated author/project repository was returned. One generic third-party polynomial utility appeared in a broader search because it implements `hstar-to-ehrhart`; it did not claim generalized-snake enumeration or the length-10 endpoint. A later attempt to clone it for inspection failed because the shell's configured GitHub proxy endpoint was unavailable; this failure does not affect the associated-code not-found result.

### Other archives

Queries:

```text
site:zenodo.org "generalized snake posets"
site:osf.io "generalized snake posets"
site:figshare.com "generalized snake posets"
```

The web search returned no results. A Zenodo API request returned HTTP 400 validation error and was not counted as a successful archive query. An OSF API title-filter request returned no data items but did not provide a usable total count. These API failures/ambiguities are explicitly inside the not-found boundary.

## Adjacent-theorem check: does $h^*$-real-rootedness automatically give the disk?

Queries:

```text
Ehrhart polynomial roots disk h-star real-rooted theorem
Ehrhart transform preserves roots disk real negative h* polynomial
Ehrhart polynomial root bounds palindromic real-rooted h-star
Rodriguez-Villegas transform negative real roots Ehrhart disk
```

These located general Ehrhart-root-bound papers and Rodriguez--Villegas-type results for $h^*$-roots on the **unit circle**, but no primary theorem taking arbitrary negative-real-rooted palindromic $h^*$ input to the Lee--Vindas-Meléndez--Wang disk. Braun--Jal themselves neither state such an implication nor mention Conjecture 5.1(2). Consequently their paper cannot be cited as a solution to the disk conjecture without a new intervening theorem.

This paragraph records only the literature result of the query. It does not assert that no such theorem can exist.

## Not-found boundary

The audit supports only this statement:

> By 2026-08-29, no proof, counterexample, certified length-10 result, erratum correcting Conjecture 5.1, or associated computation repository was found in the checked arXiv records/versions, DOI and publisher metadata, Crossref, DataCite, OpenAlex, the accessible portion of Semantic Scholar, exact-title/formula web searches, unauthenticated GitHub repository search, or the recorded archive searches.

It does **not** cover:

- private correspondence, talks, unpublished drafts, closed repositories, or work under unrelated terminology;
- authenticated Google Scholar/MathSciNet/zbMATH full interfaces (not available here);
- authenticated GitHub code search (HTTP 401);
- a complete Semantic Scholar citation graph (HTTP 429);
- a successful direct Zenodo API result (HTTP 400);
- future sources after the cut-off.

Any release or priority claim must repeat the novelty search at release time.
