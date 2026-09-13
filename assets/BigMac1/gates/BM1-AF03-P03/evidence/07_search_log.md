# Gate 1 literature and novelty search log

Search date: **2026-08-29 (Asia/Shanghai)**.

Scope: Conjecture 3.2, Definition 3.1, Theorem 3.7, the $n\le4$
verification statement, canonical metadata/version history, later
proofs/disproofs/citations/corrections, and public code. Only primary records
are used as claim evidence. General web indexes were used only to discover
candidate primary records; no mathematical claim is accepted from an index
snippet.

## Pass 1: frozen claim set

Before external search, claims C01--C07 were frozen. C08--C10 were added as
explicit inferences/leads exposed by the audit. Their dispositions are in
<code>literature/claim_ledger.md</code>.

## Pass 2: queries and results

| ID | Date | Database / owner | Exact URL or query | Result used |
|---|---|---|---|---|
| S01 | 2026-08-29 | Algebraic Combinatorics / Centre Mersenne (official publisher) | <https://alco.centre-mersenne.org/articles/10.5802/alco.424/> | Canonical metadata: vol. 8 (2025), no. 3, 711--743; DOI; received/revised/accepted/online dates. No correction/corrigendum or code link is displayed. Publisher page's “Cited by Sources” field is empty at access time. |
| S02 | 2026-08-29 | Centre Mersenne version of record | <https://alco.centre-mersenne.org/item/10.5802/alco.424.pdf> | Downloaded 34-page PDF. Definition 3.1, Conjecture 3.2, and Remark 3.3 are on journal p. 717 / PDF p. 8. Theorem 3.7 is on journal p. 719 / PDF p. 10. |
| S03 | 2026-08-29 | DOI resolver / Crossref DOI metadata | <https://doi.org/10.5802/alco.424>, requested as application/vnd.citationstyles.csl+json | Confirms DOI, title, author, venue, volume, issue, pages, and online date. The relation object is empty, there is no update-to/updated-by entry, and is-referenced-by-count is 0. This count is incomplete: later primary papers below do cite the work. |
| S04 | 2026-08-29 | arXiv abstract/version record | <https://arxiv.org/abs/2406.19715> | Current record is v3, revised 2026-04-07; 33 pages, “Final version”; journal ref and DOI present. Submission history: v1 2024-06-28, v2 2024-11-13, v3 2026-04-07. |
| S05 | 2026-08-29 | arXiv API | <https://export.arxiv.org/api/query?id_list=2406.19715> | Machine-readable current entry 2406.19715v3, update timestamp 2026-04-07T04:24:40Z. Saved raw Atom response. |
| S06 | 2026-08-29 | arXiv PDFs and TeX source | <https://export.arxiv.org/pdf/2406.19715v1>, <https://export.arxiv.org/pdf/2406.19715v2>, <https://export.arxiv.org/pdf/2406.19715>, <https://export.arxiv.org/e-print/2406.19715v1>, <https://export.arxiv.org/e-print/2406.19715v2>, <https://export.arxiv.org/e-print/2406.19715> | All versions contain the same basis conjecture and $n\le4$ report. v3 TeX lines 706--712 and 741--768 give the decisive passages. A v2-to-v3 diff shows proof/base-case and figure corrections but no change to those statements. |
| S07 | 2026-08-29 | arXiv exact-topic search | <https://arxiv.org/search/?query=%221%2C2%22+bosonic+fermionic+coinvariant&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | One hit: the target preprint. This is an exact narrow query, not exhaustive novelty evidence. Raw HTML saved. |
| S08 | 2026-08-29 | arXiv broader phrase search | <https://arxiv.org/search/?query=bosonic-fermionic+coinvariant&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | Five hits at access time: arXiv:2509.15054, 2505.14885, 2501.09920, 2406.19715, and 2005.00924. Relevant later records were inspected at source. Raw HTML saved. |
| S09 | 2026-08-29 | arXiv author API | <https://export.arxiv.org/api/query?search_query=au:%22John_Lentfer%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending> | Returned the author's arXiv list, including newer 2026 records 2608.08187 and 2608.02881, as well as current versions 2505.14885v2, 2501.09920v2, and 2406.19715v3. Each potentially relevant primary paper was downloaded and searched. |
| S10 | 2026-08-29 | arXiv primary paper, Jiang--Lentfer | <https://arxiv.org/abs/2608.02881>, PDF/source via export.arXiv | Submitted 2026-08-03. Table 1 (PDF p. 3; source lines 221--244) marks $\dim R_n^{(1,2)}=2^{n-1}n!$ conjectural. Reference [27] is the target paper. This is the strongest time-near-cutoff primary frontier evidence. |
| S11 | 2026-08-29 | arXiv primary paper, Lentfer | <https://arxiv.org/abs/2501.09920>, current v2 dated 2026-04-07 | PDF p. 15 / source lines 778--787 calls the $R_n^{(1,2)}$ hook characters conjectural and states the borrowed result conditionally. Reference [15] is the target paper. No basis proof/disproof appears. |
| S12 | 2026-08-29 | arXiv primary paper, Lentfer | <https://arxiv.org/abs/2505.14885>, current v2 dated 2026-06-23 | PDF p. 10 says all Frobenius-series cases with $k+j\ge3$ remain open. This concerns the stronger general Frobenius frontier, not specifically the finite $n=5$ basis test. |
| S13 | 2026-08-29 | arXiv primary paper, Corteel--Lentfer | <https://arxiv.org/abs/2608.08187>, v1 dated 2026-08-08 | Concerns $R_n^{(1,1)}$, not a solution of the target. It cites Section 6 of the target paper for a specialized bijection (source line 376) and lists the target as reference [15]. |
| S14 | 2026-08-29 | Séminaire Lotharingien de Combinatoire / FPSAC official proceedings | <https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/129.html>, <https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/129.pdf>, <https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/129/129.tex> | Companion proceedings article, final version 2025-04-01. It repeats Conjecture 3.2 (PDF p. 7) and the cardinality theorem (Theorem 3.6 there, PDF p. 8). It does not settle the conjecture. |
| S15 | 2026-08-29 | John Lentfer's official UC Berkeley research page | <https://math.berkeley.edu/~jlentfer/> | Page says it is superseded by a UCSD site as of July 2026, but lists the 2025 paper under its conjectural title/abstract and provides journal/arXiv links only. No proof, erratum, or code link is listed. Raw HTML saved. |
| S16 | 2026-08-29 | UC Berkeley Mathematics official publication catalog | <https://math.berkeley.edu/publications?keywords=Lentfer>; <https://math.berkeley.edu/publications?keywords=Combinatorics%20of%20Bosonic-Fermionic%20Coinvariant%20Rings>; <https://math.berkeley.edu/publications?topics=183&pubtype=22> | No public catalog record matching Lentfer/the exact 2026 dissertation title was returned. The 2026 topic query listed other dissertations. This records only that the thesis text was not located there. |
| S17 | 2026-08-29 | GitHub official REST repository search | <https://api.github.com/search/repositories?q=%22bosonic-fermionic%20coinvariant%22>; <https://api.github.com/search/repositories?q=2406.19715> | Both returned total_count 0. Repository search is metadata-oriented and does not certify absence from all code/file contents. Raw JSON saved. |
| S18 | 2026-08-29 | GitHub official REST user search | <https://api.github.com/search/users?q=%22John%20Lentfer%22> | Returned total_count 0; no author account was identified by that exact public-name query. This does not establish that the author has no differently named account. |
| S19 | 2026-08-29 | Official publisher/arXiv/source-text correction and code audit | Searches within all downloaded publisher/arXiv TeX/PDF text for erratum, corrigendum, correction, GitHub, repository, code, Macaulay, Sage, computer, and the exact verification sentence | No erratum/code/repository pointer was found in the target paper package. The only decisive target statement about finite verification is Remark 3.3. The v3 changes were checked directly by source diff. |

## Subsequent primary citations inspected

| Work | Exact use of the target paper | Relevance to settlement |
|---|---|---|
| Lentfer, *The sign character of the triagonal fermionic coinvariant ring*, arXiv:2501.09920v2 / EJC 33(2) (2026) | Theorem at PDF p. 15 cites target Theorem 8.4 and calls the $R_n^{(1,2)}$ hook-character result conjectural/conditional. | Does not settle Conjecture 3.2; supports continued conjectural status of nearby Frobenius data as of 2026-04-07. |
| Jiang--Lentfer, *Type $B$ fermionic coinvariant rings*, arXiv:2608.02881v1 | Table 1 (PDF p. 3) marks the type-A $(1,2)$ dimension formula conjectural; target paper is ref. [27]. | Strong evidence against an already-known general basis proof in the authors' own frontier as of 2026-08-03. |
| Corteel--Lentfer, *Universal Hilbert series coefficients of the superspace coinvariant ring*, arXiv:2608.08187v1 | Uses a specialization of the map from target Section 6; target is ref. [15]. | Concerns $R_n^{(1,1)}$, not the $n=5$ target. |

The publisher/Crossref zero-citation fields are therefore incomplete and were
not used to infer that there are no citations.

## Public-code audit conclusion

No paper-linked or exact-metadata-matching repository was found. In particular:

- the version of record and arXiv v1--v3 TeX/PDF packages contain no code or
  repository URL;
- the author page supplies only paper links;
- the two GitHub repository searches returned zero metadata hits.

This is a **scoped negative result**, not a proof that no code is public under
a different title/account or in non-indexed storage.

## Residual novelty limitations carried into the final lock

1. The 2026 UC Berkeley dissertation *Combinatorics of Bosonic-Fermionic
   Coinvariant Rings* is cited by Jiang--Lentfer but its text was not located in
   the audited official sources. Its contents therefore remain outside the
   evidence set.
2. arXiv, publisher citation feeds, and repository indexes can lag; the final
   lock below freezes only their state at the recorded access times.
3. “No solution found” is not logically equivalent to “no solution exists.”

## Intermediate repeat pass (not the contractual post-result pass)

This intermediate repeat was run on **2026-08-29 at approximately 18:17
Asia/Shanghai**, after the preliminary Gate-1 verdict had been drafted but
before this log was corrected to anchor the contractual second search to the
strict mathematical result. It is retained for provenance and is not counted
as the required result-after novelty pass.

| ID | Database / exact query | Result |
|---|---|---|
| P01 | arXiv API: <https://export.arxiv.org/api/query?id_list=2406.19715,2608.02881,2608.08187> | At feed time 2026-08-29T10:17:05Z, the target remained 2406.19715v3 (updated 2026-04-07); the two newest directly relevant papers remained 2608.02881v1 and 2608.08187v1. No replacement version appeared. |
| P02 | arXiv exact-title search: <https://arxiv.org/search/?query=%22A+conjectural+basis+for+the+%281%2C2%29-bosonic-fermionic+coinvariant+ring%22&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | One hit, arXiv:2406.19715. |
| P03 | arXiv phrase search: <https://arxiv.org/search/?query=%22Conjecture+3.2%22+coinvariant&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | Zero hits. This narrow zero does not imply absence of papers using different numbering/wording. |
| P04 | DOI/Crossref repeat: <https://doi.org/10.5802/alco.424>, CSL JSON content negotiation | Byte-identical to the first-pass saved DOI JSON. Still no update relation and reported citation count still 0. |
| P05 | Official publisher repeat: <https://alco.centre-mersenne.org/articles/10.5802/alco.424/> | Page still presented the original article; no erratum/corrigendum/repository link was found. |
| P06 | GitHub repository search by exact title: <https://api.github.com/search/repositories?q=%22A%20conjectural%20basis%20for%20the%20%281%2C2%29-bosonic-fermionic%20coinvariant%20ring%22> | total_count 0. |
| P07 | GitHub repository search by DOI: <https://api.github.com/search/repositories?q=%2210.5802%2Falco.424%22> | total_count 0. |
| P08 | GitHub code-search API by arXiv ID: <https://api.github.com/search/code?q=%222406.19715%22> | HTTP 401, “Requires authentication.” Therefore a repository-content-wide GitHub code search was **not available** in this unauthenticated audit. The negative code conclusion remains limited to paper links, web discovery, and repository metadata. |

**Intermediate-pass outcome:** no newer version, correction, later settlement, or
paper-linked/exact-metadata repository was found. The residual dissertation
risk and the unavailable authenticated GitHub code search remain open.

Raw intermediate-pass artifacts:

- <code>literature/sources/post_result_arxiv_ids_2026-08-29_atom.xml</code>
  (sha256 0226120ea654c44f8eaee5ef4b19c011909e1f84af02ac069f9ec21ea4dfc918)
- <code>literature/sources/post_result_arxiv_search_exact_title_2026-08-29.html</code>
  (sha256 1c9f18ea8ec9600de988ac9c02910d2ebdd3565cc5f82a587731c981af377a9d)
- <code>literature/sources/post_result_arxiv_search_conjecture_3_2_2026-08-29.html</code>
  (sha256 448238fe3f6c5e37931b8515c403b2bc4cace60eb4d912452b081c2ad8b247fd)
- <code>literature/sources/post_result_doi_10.5802_alco.424_csl.json</code>
  (sha256 0e762c47f0d1d8b5a8cb870d9a56ddbd1a7209867482954d4548f7771b081f55)
- <code>literature/sources/post_result_ALCO_424_publisher_2026-08-29.html</code>
  (sha256 67929871848869c29109dcbe117ddd905d6bdd9b75eea3459875e8cdbb5bd3f0)
- <code>literature/sources/post_result_github_repo_exact_title_2026-08-29.json</code>
  and <code>literature/sources/post_result_github_repo_doi_2026-08-29.json</code>
  (each sha256 08c082fdf7ca87ba911a2aabb0f0cf2d3e482a6feeaac9713e4578c20b2600b2)
- <code>literature/sources/post_result_github_code_arxiv_2026-08-29.json</code>
  (sha256 b7dbd173f33b19650f61b1c528737e2037cf768d90076fdfce5d32541765e29e)

## Final pre-release novelty pass after the exact $n=5$ result

This is the contractual second novelty search. It ran on **2026-08-29,
18:17--18:22 Asia/Shanghai**, after the research team reported that the exact
$n=5$ theorem and its certificates were available. It therefore supersedes
the label previously attached to the intermediate P01--P08 pass.

| ID | Database / exact URL or query | Result at final access time |
|---|---|---|
| F01 | arXiv API: <https://export.arxiv.org/api/query?id_list=2406.19715,2608.02881,2608.08187> | Feed timestamp 2026-08-29T10:17:05Z. The target remained 2406.19715v3 (updated 2026-04-07); Jiang--Lentfer remained 2608.02881v1; Corteel--Lentfer remained 2608.08187v1. |
| F02 | arXiv author API: <https://export.arxiv.org/api/query?search_query=au:%22John_Lentfer%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending> | Feed timestamp 2026-08-29T10:01:40Z. The newest author records remained 2608.08187v1 and 2608.02881v1; the target remained 2406.19715v3. No newer author record in the feed claimed the target result. |
| F03 | arXiv exact-title query: <https://arxiv.org/search/?query=%22A+conjectural+basis+for+the+%281%2C2%29-bosonic-fermionic+coinvariant+ring%22&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | One result, arXiv:2406.19715. |
| F04 | arXiv exact-topic query: <https://arxiv.org/search/?query=%221%2C2%22+bosonic+fermionic+coinvariant&searchtype=all&abstracts=show&order=-announced_date_first&size=200> | One result, arXiv:2406.19715. This narrow query is not an exhaustive literature search. |
| F05 | DOI resolver / Crossref CSL: <https://doi.org/10.5802/alco.424>, requested as <code>application/vnd.citationstyles.csl+json</code> | DOI metadata remained byte-identical to the first pass: empty relation object, no update-to/updated-by relation, and the known-incomplete reported citation count 0. |
| F06 | Official publisher: <https://alco.centre-mersenne.org/articles/10.5802/alco.424/> | Still presented the version of record. No formal erratum/corrigendum, correction link, or paper repository link was located on the page. |
| F07 | GitHub repository API exact-title query: <https://api.github.com/search/repositories?q=%22A%20conjectural%20basis%20for%20the%20%281%2C2%29-bosonic-fermionic%20coinvariant%20ring%22> | <code>total_count: 0</code>. |
| F08 | GitHub repository API DOI query: <https://api.github.com/search/repositories?q=%2210.5802%2Falco.424%22> | <code>total_count: 0</code>. |
| F09 | GitHub repository API arXiv-ID query: <https://api.github.com/search/repositories?q=2406.19715> | <code>total_count: 0</code>. These metadata searches do not cover all file contents or differently named repositories. |
| F10 | GitHub code API arXiv-ID query: <https://api.github.com/search/code?q=%222406.19715%22> | HTTP 401, “Requires authentication.” No negative content-wide GitHub claim is drawn from this unavailable search. |
| F11 | General web discovery, exact query: <code>"A conjectural basis for the (1,2)-bosonic-fermionic coinvariant ring" proof n=5</code> | The primary candidates returned were the target arXiv/journal records and its FPSAC companion; no primary source claiming a proof or counterexample was found. |
| F12 | General web discovery, exact query: <code>"10.5802/alco.424" proof counterexample</code> | Returned the target DOI/publisher record and unrelated material; no new primary settlement was discovered. |
| F13 | General web discovery, exact query: <code>"R_n^{(1,2)}" basis coinvariant</code> | Returned the target/related superspace literature plus unrelated notation collisions; no new primary settlement was discovered. |
| F14 | General web discovery, exact query: <code>site:github.com "2406.19715" OR "A conjectural basis for the (1,2)-bosonic-fermionic coinvariant ring"</code> | No matching public GitHub result was returned. This does not replace authenticated GitHub file-content search. |
| F15 | General web discovery, exact query: <code>site:arxiv.org "10.5802/alco.424"</code> | Returned the target arXiv record; no additional arXiv primary record was discovered by this exact DOI query. |
| F16 | General web discovery, exact query: <code>site:arxiv.org "A conjectural basis for the (1,2)-bosonic-fermionic coinvariant ring"</code> | Returned the target arXiv record; no new arXiv primary settlement was discovered. |
| F17 | General web discovery, exact query: <code>"A conjectural basis for the (1,2)-bosonic-fermionic coinvariant ring" -site:alco.centre-mersenne.org -site:arxiv.org</code> | Returned the official FPSAC companion, author page, conference material, and third-party mirrors. The primary items still describe the basis as conjectural; no settlement was found. Third-party citation counts were not used as evidence. |
| F18 | General web discovery, exact query: <code>site:berkeley.edu "Combinatorics of Bosonic-Fermionic Coinvariant Rings" Lentfer</code> | Returned the author's official page and Berkeley seminar material, but no public dissertation text or institutional dissertation record. This is a scoped failure to locate the source, not evidence about its contents. |

**Final-pass outcome:** within these recorded official records and discovery
queries, no prior public proof/disproof of the finite $n=5$ statement, no
settlement of the general basis conjecture, no correction affecting the
target statement, and no paper-linked/exact-metadata public code repository
was found. The 2026 dissertation remains unavailable in the audited official
sources, and authenticated GitHub code search remains outside the evidence
set. These are scoped limitations; no worldwide absence theorem is claimed.
This pass is the final pre-release novelty lock for the present release, so no
additional repeat remains outstanding under the execution contract.

Raw final-pass artifacts:

- <code>literature/sources/final_prerelease_arxiv_ids_2026-08-29_atom.xml</code>
  (sha256 0226120ea654c44f8eaee5ef4b19c011909e1f84af02ac069f9ec21ea4dfc918)
- <code>literature/sources/final_prerelease_arxiv_author_John_Lentfer_2026-08-29_atom.xml</code>
  (sha256 1d8a69de8c5c77bd99eb885f37e0046addd7a0bb558716ae2404526c887679d7)
- <code>literature/sources/final_prerelease_arxiv_exact_title_2026-08-29.html</code>
  (sha256 1c9f18ea8ec9600de988ac9c02910d2ebdd3565cc5f82a587731c981af377a9d)
- <code>literature/sources/final_prerelease_arxiv_12_topic_2026-08-29.html</code>
  (sha256 873ffaadb7241cd884bb80ba1e606c31672d5779e2a8bb3d12a819cb3865aa4a)
- <code>literature/sources/final_prerelease_doi_10.5802_alco.424_csl.json</code>
  (sha256 0e762c47f0d1d8b5a8cb870d9a56ddbd1a7209867482954d4548f7771b081f55)
- <code>literature/sources/final_prerelease_ALCO_424_publisher_2026-08-29.html</code>
  (sha256 1880dbcadc9130f29a915a31473dafcbff9d211b1437d7ae9ae88c49491534c2)
- <code>literature/sources/final_prerelease_github_repo_exact_title_2026-08-29.json</code>,
  <code>literature/sources/final_prerelease_github_repo_doi_2026-08-29.json</code>,
  and <code>literature/sources/final_prerelease_github_repo_arxiv_2026-08-29.json</code>
  (each sha256 08c082fdf7ca87ba911a2aabb0f0cf2d3e482a6feeaac9713e4578c20b2600b2)
- <code>literature/sources/final_prerelease_github_code_arxiv_2026-08-29.json</code>
  (sha256 b7dbd173f33b19650f61b1c528737e2037cf768d90076fdfce5d32541765e29e)

## Raw artifact inventory (principal files)

- <code>literature/sources/Lentfer_2025_ALCO_424_published.pdf</code>
  (sha256 37f6b097ff430f9ea498ae2aaf70013e105d0b6221d642ac147103babe8768ca)
- <code>literature/sources/Lentfer_arXiv_2406.19715_latest.pdf</code>
  (sha256 aa7f0b0656722f9108df192434420a3d93ba95010a652f2cc2bd686576ceb495)
- <code>literature/sources/arxiv_2406.19715_atom.xml</code>
  (sha256 c69560fff2fd7209423e7598071af0c26e6d76ebf4e7ffb0ccb67dcc92f12ecf)
- <code>literature/sources/arxiv_v3/12arxiv-FINAL-April-6-2026.tex</code>
  (sha256 bd349b19a46438a3eb33e48220999921ed4a5ea5669ea24da02f999e19ea0868)
- <code>literature/sources/doi_10.5802_alco.424_csl.json</code>
  (sha256 0e762c47f0d1d8b5a8cb870d9a56ddbd1a7209867482954d4548f7771b081f55)
- <code>literature/sources/Jiang_Lentfer_2026_type_B_fermionic_arXiv2608.02881.pdf</code>
  (sha256 dfcdd347ebb26505e69a6c77fd2dcb1b08594542b53dbdf39a1110be4ae3b2ee)
- <code>literature/sources/arxiv_2608.02881/main_type_B_Aug_3_2026.tex</code>
  (sha256 0624da5dc471cf07e481746f1e90ed332cbe512e02de20258eaa27abceecdb96)
- <code>literature/sources/Lentfer_2026_sign_character_arXiv2501.09920v2.pdf</code>
  (sha256 3173364df9f08d2f4ea90a5b53c6ed2d77648c833d69599af74a0616e274fcdf)
- <code>literature/sources/Corteel_Lentfer_2026_universal_Hilbert_arXiv2608.08187.pdf</code>
  (sha256 b58477e562a7ffe1897a6ea100fb8b9ca8f0efe41ee7a1aac8a0a0e9f7642195)
- <code>literature/sources/arxiv_author_John_Lentfer_atom.xml</code>
  (sha256 1d8a69de8c5c77bd99eb885f37e0046addd7a0bb558716ae2404526c887679d7)
- <code>literature/sources/github_repo_search_arxiv_2406.19715.json</code> and
  <code>literature/sources/github_repo_search_bosonic_fermionic_coinvariant.json</code>
  (each sha256 08c082fdf7ca87ba911a2aabb0f0cf2d3e482a6feeaac9713e4578c20b2600b2)
