# Search log

## NOVELTY_LOCK pass 1 — 2026-08-29 (Asia/Shanghai)

Claims C01–C08 in `claim_ledger.md` were frozen before the searches below.

| Time/phase | Database or site | Query / record | Result used |
|---|---|---|---|
| pass 1 | OEIS | `A321614`, entry and internal/b-file views | Definition, offset 0, 22 terms, maximum comment, Barker conjecture and exact formula. https://oeis.org/A321614 |
| pass 1 | OEIS | `A231145` | Free 2-by-2 tile table and diagonal cross-reference. https://oeis.org/A231145 |
| pass 1 | OEIS | `A061593` | Labeled \(4\times2n\) counts and its rational generating function; links to Knuth and Wilf. https://oeis.org/A061593 |
| pass 1 | SciNet | problem `456c1f41-44f3-4eee-87dd-e34b50e0c451` | Original finite-computation challenge and explicit “stronger: all-n proof” frontier. https://api.scinet.pub/p/456c1f41-44f3-4eee-87dd-e34b50e0c451 |
| pass 1 | SciNet | finding `4d13cbaa-b64a-4167-b7c4-8e435279c9d0` | Exact finite verification to 5000 and explicit statement that it is not an all-n proof. https://api.scinet.pub/f/4d13cbaa-b64a-4167-b7c4-8e435279c9d0 |
| pass 1 | EJC publisher / DOI | `H. S. Wilf "The Problem of the Kings"` | Publisher record, abstract, DOI 10.37236/1197, publication metadata and theorem scope. https://doi.org/10.37236/1197 |
| pass 1 | Stanford author page | `Donald Knuth "Nonattacking kings on a chessboard"` | Author-hosted 1994 unpublished note listed; no free-orbit recurrence theorem. |
| pass 1 | arXiv | `A321614`; `"nonattacking kings" chessboard transfer matrix`; exact title searches | No A321614 all-n recurrence proof found. Brown’s arXiv:2111.10331 concerns maximum arrangements on \(2n\times2n\), a different family. |
| pass 1 | Web exact-text | `"(1 - 2*x)*(1 - 6*x + 17*x^2"`; `"A321614" recurrence Barker`; `"Number of nonequivalent ways to place 2n nonattacking kings" proof` | Only OEIS mirrors/source and the finite SciNet result were relevant; no independent all-n proof found. |
| pass 1 | DOI/web metadata | `site:doi.org A321614`; `site:arxiv.org A321614` | No relevant record returned. |

The second novelty pass is intentionally deferred until the exact theorem and
certificate endpoint are frozen.

## NOVELTY_LOCK pass 2 — endpoint frozen, 2026-08-29

Frozen endpoint: exact Barker generating function, recurrence for every
`n >= 10`, and minimal scalar order ten under the explicitly fixed
four-operation group (including at `n=2`).

| Database/site | Exact query or record | Result |
|---|---|---|
| Web/current index | `"A321614" "proof" recurrence` | No relevant all-`n` proof; only the finite SciNet finding and false-positive identifier matches. |
| Web/current index | `"A321614" "order-10" recurrence proof` | Finite SciNet record only. |
| Web exact polynomial | `"1-12x+54x^2-98x^3-17x^4"` | No A321614 proof or independent publication found. |
| arXiv-focused | `site:arxiv.org A321614 OR "maximum nonattacking king placements" "4 x 2n"` | No exact-family all-`n` proof found. |
| OEIS direct current record | A321614, opened on 2026-08-29 | Formula still explicitly labeled Barker conjectures; 22-term b-file unchanged. |
| SciNet direct current record | finding 4d13cbaa, opened on 2026-08-29 | Still states finite `n<=5000` verification and explicit all-`n` limitation. |
| EJC publisher/DOI | Wilf title/author/year/venue/DOI templates | Original article and metadata verified; theorem is adjacent labeled counting/asymptotics, not the A321614 free-count recurrence. |

Bounded conclusion: no prior all-`n` proof was found in these recorded
databases and queries by the cutoff. This does not assert that no private,
unindexed, or differently worded proof exists.
