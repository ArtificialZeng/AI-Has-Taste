# Citation and bibliography audit

## Scope and result

Mode: search verification.  Audit date: 2026-09-09 UTC.  The accepted result-note scope and all four publication source files were read.  Pass 1 froze the four citation-bearing claims in `audit/citation-claim-ledger.json`; pass 2 verified only that fixed list.  All four claims are supported, all three cited records exist, and no citation is undefined.  Bibliography coverage is appropriate: two natural non-library primary sources cover the problem's definition, best published bounds, SAT formulation, and closest unresolved cases, while one genuinely relevant user-library source supports the verification-method comparison.

The audit was performed locally because the user prohibited spawning agents.  Each key was nevertheless checked separately under the same per-reference protocol.

## Fixed extraction (pass 1)

| ID | Manuscript claim | Type | Location | Direct keys |
|---|---|---|---|---|
| C01 | Heath et al. give the ordinary red-blue Kneser-Ramsey definition used here. | Definition attribution | `manuscript/main.tex:40-44` | `HeathEtAl2025` |
| C02 | Heath et al. prove the bounds 11 and 13 and give the SAT encoding. | Prior result and method | `manuscript/main.tex:44-49` | `HeathEtAl2025` |
| C03 | Gujgiczer et al. list the KG(11,3) and KG(12,3) triangle-free-cover cases as unresolved, distinct from 2.5-colorability. | Closest prior work/status | `manuscript/main.tex:51-58` | `GujgiczerEtAl2026` |
| C04 | Zeng et al. give a finite-combinatorial precedent using stored graph colorings and independent exact reconstruction. | Verification-method precedent | `manuscript/main.tex:159-163` | `202608.1658` |

The union of these keys is exactly the ordinary body-flow citation set extracted by the hook-compatible parser and by `check_bib_keys.py`.

## Independent source verification (pass 2)

| Claims | Status | Primary record and exact support | Metadata check |
|---|---|---|---|
| C01, C02 | Verified (exact/paraphrase) | Heath--McCourt--Parker--Schwieder--Zerbib, arXiv:2510.25734v2, Definition 1; Theorems 11--12; Section 3.3. Definition 1 gives the same ordinary red-blue edge-coloring definition. Theorem 11 gives the lower bound `3r+2`, hence 11 at `r=3`; Theorem 12 gives the upper bound 13; Section 3.3 gives the two-clause-per-triangle SAT formulation. | The official arXiv record confirms title, five authors, v2 date 10 November 2025, identifier, and DOI `10.48550/arXiv.2510.25734`. |
| C03 | Verified (exact) | Gujgiczer--Marits--Ozeki, arXiv:2607.12353v1, Section 4, especially the paragraph following Theorem 4.2: KG(13,3) is not coverable, KG(10,3) is coverable, and only KG(11,3) and KG(12,3) remain unresolved. The surrounding section separately treats two 2.5-colorable covering graphs. | The official arXiv record confirms title, three authors, v1 submission 14 July 2026, identifier, and DOI `10.48550/arXiv.2607.12353`. |
| C04 | Verified (paraphrase) | Official Preprints.org version 1, Sections 3 and 6. Section 3 describes stored colorings and exhaustive independent reconstruction of graph/distance objects; Section 6 lists the stored color maps, a standard-library verifier that reconstructs the finite instance, and a separate exact implementation. This directly supports the nearby methodological analogy and no stronger claim is made. | The official record confirms the title, four authors, version 1, posting date 24 August 2026, and DOI `10.20944/preprints202608.1658.v1`. The active registry row is 9; its exported BibTeX was used with key `202608.1658`. |

Authoritative records inspected:

- <https://arxiv.org/html/2510.25734v2>
- <https://arxiv.org/html/2607.12353v1>
- <https://www.preprints.org/manuscript/202608.1658>

The required academic-citation search templates (author/year/title words, exact title restricted to scholarly hosts, author/year/venue, and DOI) were run for every retained record before inspecting the primary full text.

The remaining substantive numerical and existence assertions are the paper's own finite result rather than external attributions.  They were traced to the frozen coloring and both exact verifiers: fresh replays returned 165 vertices, 4,620 complete edges, 2,308 red and 2,312 blue edges, 15,400 triangles split as 7,720 of type 1R/2B and 7,680 of type 2R/1B, with both negative controls passing.  The abstract, theorem, proof, reproducibility section, and limitations state no stronger conclusion than the accepted claim `R_3^KG(3,3) >= 12`; each explicitly leaves the n=12 case and original exact-value problem unresolved.

## Bibliography and mechanical checks

The final bibliography has three entries and every entry has an ordinary body-flow use.  There are no decorative, missing, duplicate, or unused entries.  The user-library citation is a minimum-coverage item, not a substitute for the two directly relevant non-library primary sources.  The only key correction was `ZengEtAl2026Certificates` to the registry-exported official key `202608.1658`; the corresponding citation was updated exactly.

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reported 3 cited keys, 3 BibTeX keys, no missing/unused entries, and exact AUX agreement.  The converged `main.log` and `main.blg` contain no undefined citations, missing database entries, repeated entries, LaTeX errors, or fatal diagnostics.

No citation claim was strengthened beyond its source, and the manuscript explicitly limits its freshness comparison rather than asserting priority.
