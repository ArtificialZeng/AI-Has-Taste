# Citation and claim verification report (pass 2)

**Mode:** primary-source search plus frozen-evidence verification  
**Document:** `manuscript/main.tex`  
**Search date:** 2026-09-07  
**Claim input:** the fixed 21-item ledger in
`audit/citation-claim-ledger.md`; no claims were re-extracted in this pass  
**Result:** **accept**

The user explicitly prohibited subagents, so the four keys were verified
sequentially in this release context.  For each academic citation the title,
author/year/venue query, title-plus-primary-host query, identifier query, and
DOI or arXiv query (as applicable) were run.  Primary records and original
text, not search snippets alone, determined the conclusions.

## Summary

| Metric | Count |
|---|---:|
| Claims in frozen ledger | 21 |
| Verified | 21 |
| Numerical errors | 0 |
| Misquoted / misleading / hallucinated | 0 |
| Unverified | 0 |
| Retained citation keys | 4 |
| BibTeX replacements | 0 |
| Citation-key changes | 0 |

## Claim-level conclusions

| Claim(s) | Status | Confidence | Exact evidence location |
|---|---|---|---|
| C01, C03--C05, C11, C13--C21 | Verified | exact | `audit/math.md`, “Reconstruction of the decisive argument” and “Checks actually performed”; `evidence/labelled_checker_report.json`; `audit/referee_recompute_report.json`; hashes rechecked against `audit/snapshot.json`. |
| C02 | Verified | interpretation | A standard cycle has at least three vertices, so 4 is the least even cycle length; Kinnersley--Townsend Theorem 2.7 applies only for \(m\ge18\), while Biswas Section 5.2 supplies only an upper bound at \(m=4\). |
| C06 | Verified | paraphrase | Fomin et al., abstract and opening game definition: bounded speed \(s\), computational complexity, and graph-class results. |
| C07 | Verified | paraphrase | Kinnersley--Townsend, Introduction: cops place first, robber responds, cops move first in each round, each cop stays or traverses one edge, and an infinite-speed robber takes any cop-free path. |
| C08 | Verified | exact | Kinnersley--Townsend, Introduction and Theorem 2.7: \(2n-24\le c_\infty(C_n\square C_n)\le2n\) for \(n\ge18\). |
| C09 | Verified | exact | Biswas v2, Section 5.2, p.15: for \(C_m^{\square k}\), \(m\ge4\), the quotient construction gives \(c_{1,\infty}\le2m^{k-1}\); the same paragraph states the Kinnersley--Townsend two-dimensional estimate. |
| C10 | Verified | interpretation | Substitution \(m=4,k=2\) in the Biswas bound gives 8; neither cited source states equality for this cell. |
| C12 | Verified | paraphrase | Zeng et al., official version 1, Sections 6--7: discovery is separated from exact certification; the standard-library verifier reconstructs the finite instance, and the conclusions are limited to the finite libraries. |

Every number in C03--C05 and C13--C20 matches exactly, including significant
figures and units/counting domains.  In particular, the independently
recomputed report gives exact value 4 and repeats the canonical configuration,
state, and rank counts; the labelled report gives 810,000 ordered four-cop
states, 21,296 labelled losing three-cop states, and 2,662,000 checked ordered
moves.

## Bibliographic records and nearby support

| Key | Current title | Authoritative primary record / text | Nearby support | Action |
|---|---|---|---|---|
| `FominEtAl2010` | *Pursuing a Fast Robber on a Graph* | DOI https://doi.org/10.1016/j.tcs.2009.12.010; author-hosted journal PDF https://fedorvf.github.io/articles/2010/2010c.pdf | C06 | Metadata and support verified; retain unchanged. |
| `KinnersleyTownsend2022` | *Catching an Infinitely Fast Robber on a Grid* | DOI https://doi.org/10.1016/j.dam.2022.06.022; arXiv https://arxiv.org/abs/2107.14193 | C07--C08 | Metadata, convention, hypotheses, and theorem verified; retain unchanged. |
| `Biswas2026` | *Fast Robbers on Abelian Cayley Graphs and Digraphs* | arXiv https://arxiv.org/abs/2608.30474 and frozen v2 PDF `evidence/external/2608.30474.pdf`, Section 5.2, p.15 | C09--C10 | v2/date and exact hypotheses verified; retain unchanged. |
| `ZengEtAl2026Certificates` | *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes* | DOI https://doi.org/10.20944/preprints202608.1658.v1; official text https://www.preprints.org/manuscript/202608.1658 | C12 | Registry row 9, metadata, Sections 6--7, and direct body citation verified; retain unchanged. |

No official record disagreed with the current title, authors, year, venue,
pages, DOI/arXiv identifier, or version note.  Because no correction was
required, the existing canonical entries were not replaced and no cite key was
changed.

## Coverage and relevance

The bibliography is not user-library-only.  Fomin et al. supplies the bounded
speed origin/background, Kinnersley--Townsend supplies the exact convention and
closest published torus theorem, and Biswas supplies the later closest
product/quotient bound and its \(m=4\) specialization.  Registry row 9 is the
one genuinely relevant active-library entry because its Sections 6--7 support
the explicit reproducibility comparison.  It appears as the ordinary body-flow
direct citation `\\cite[Sections~6--7]{ZengEtAl2026Certificates}`.
Other library entries would not support a naturally occurring nearby claim, so
adding a second would be padding.  The reachability fixed point, induction, and
finite checks are defined and proved self-containedly, so no uncited external
method theorem is being invoked.

The active registry and workbook bindings, exact publication-attempt identity,
source passage, nearby claim, and manuscript lines are recorded in
`audit/user-bibliography-selection.json`.

## Mechanical checks

`check_bib_keys.py` found four cited keys, four bibliography entries, no
missing or unused entries, and exact agreement with the final AUX file.  The
converged `main.log` and `main.blg` contain no undefined citation/reference,
missing database entry, repeated entry, BibTeX warning, LaTeX error, overfull
box, or underfull box.  There are no unresolved citation blockers.
