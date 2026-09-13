# Search log

Search date: 2026-08-30 CST (2026-08-29 UTC).  Gate: `NOVELTY_LOCK` pass 1.

| ID | Resource/query | Result and scope |
|---|---|---|
| S01 | `https://oeis.org/A278992` and `/internal` | Live OEIS entry inspected. Name, offset, terms, EGF, and Mathar recurrence label transcribed. Page reports last modification 2026-08-29 EDT. |
| S02 | EJC publisher article page and 23-page PDF for DOI `10.37236/6037` | Publication metadata verified. Theorem 4.3/equation (17) gives the EGF and initial coefficients. Full text inspected around all recurrence statements. |
| S03 | `https://arxiv.org/abs/1601.05073` | Submission history contains v1 only (2016-01-19); journal reference is EJC 24(3), P3.43. |
| S04 | Crossref API, DOI `10.37236/6037` | Authors, title, date 2017-09-08, volume 24, issue 3, publisher, journal-article type, and DOI verified; `is-referenced-by-count=2`. |
| S05 | zbMATH Open API title search | One exact record: Zbl 1369.05112; EJC 24(3), Paper P3.43, 23 pages; authors and arXiv link verified. |
| S06 | DBLP exact-title record | DBLP key `journals/combinatorics/KraskoO17`, DOI and journal metadata verified; metadata dated 2025-12-01. |
| S07 | OpenAlex work `W2381879718` | Exact DOI/title record, diamond open access, cited-by count 1. Its one indexed citing work was not about A278992's D-finite recurrence. |
| S08 | Semantic Scholar DOI record and citations endpoint, limit 100 | Fourteen citing records returned. Titles and available abstracts were screened for `A278992`, `D-finite`, `Mathar`, and the exact simple chord-labelled phrase; no hit. Subjects concern Hamiltonian cycles, linear chord diagrams, hafnians, matchings, phylogenetic networks, or cube unfoldings. |
| S09 | Web exact title plus `citations`, and exact-title searches | Located publisher, arXiv, DBLP, institutional, and secondary metadata pages; no recurrence proof located. |
| S10 | Web exact formula query `"(-n+2)*a(n)" chord` | Returned the OEIS conjecture, not an independent proof. |
| S11 | Web query `"A278992" D-finite recurrence proof` | Returned the OEIS conjecture; no independent proof located. |
| S12 | Web query `"A278992" recurrence generating function` | Returned OEIS and unrelated adjacent sequences; no proof located. |
| S13 | Semantic Scholar citing-title/abstract keyword audit | No citing record mentioned A278992, D-finiteness, Mathar, or the target recurrence in title/available abstract. This is not a full-text nonexistence proof. |
| S14 | GitHub repository API searches for `A278992` and the exact paper title | Both returned `total_count=0`. GitHub code search was not assumed complete without authentication. |
| S15 | Web `site:github.com` searches for A278992 and exact paper title | No repository result was returned. |

## Pass-1 conclusion: `NOVELTY_LOCK`

`LOCKED` for the following bounded research claim: the 2017 paper proves the
EGF, while the live OEIS entry still labels the displayed recurrence as a 2020
conjecture; no proof of that exact recurrence was located in the resources and
queries S01--S15 as of the search date.  This lock does not assert absolute
priority.  A second search after the theorem and its exact identities are fixed
is mandatory before release.

## Pass 2 after exact theorem freeze

| ID | Resource/query | Result and scope |
|---|---|---|
| S16 | `"A278992" proof recurrence D-finite` | No independent proof result; exact sequence searches returned OEIS/adjacent material. |
| S17 | `"t(2t-1)" "6t^2+10t-2" chord diagrams` | No relevant occurrence of the order-5 operator was found. |
| S18 | `"4t^3-3t+1" "12t^3+2t^2-2t-1"` | No relevant occurrence of the order-3 operator was found. |
| S19 | `"2n^2-8n+7" "6n^2-18n+11"` | The exact recurrence led back to OEIS rather than an independent proof. |
| S20 | Live OEIS A278992 re-opened after theorem freeze | The entry still labels the relation conjectural on the access date. |

Pass-2 conclusion: `NOVELTY_LOCK CONFIRMED` in the same bounded sense as pass
1.  The manuscript therefore says only that OEIS marked the recurrence
conjectural on the access date and that the present note supplies a proof; it
does not claim absolute priority over inaccessible or unindexed work.
