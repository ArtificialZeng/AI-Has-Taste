# Citation verification report

**Mode:** Search verification  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Generated:** 2026-09-10T09:05:30Z  
**Job:** `win-00086-p07-release-355ff84f5321`  
**Attempt / launch:** `1` / `37efb2f7-213a-4f24-8f00-880e0d8ad02e`

## Summary

| Metric | Count |
|---|---:|
| Citation-bearing claims extracted | 6 |
| Ordinary body-flow citation keys | 5 |
| Verified | 6 |
| Numerical error | 0 |
| Citation not found | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status:** PASS. Every ordinary body-flow key appears in the frozen
claim ledger, exists in the canonical bibliography and converged AUX, and
directly supports its nearby claim. No cited numerical value was rounded or
altered, and no source-dependent claim strengthens the accepted theorem.

## Two-stage method

Pass 1 read the full canonical manuscript and froze the six citation-bearing
claim instances in `audit/citation-claim-ledger.json`. Its key union is exactly
`AudemardSimon2009`, `CaroTuzaZarb2026`, `HeuleHuntWetzler2013`,
`IgnatievMorgadoMarquesSilva2018`, and `ZengLiuRatnaveluHuat2026`, the complete
active `\cite{...}` set. There are no custom cite macros, `\nocite` entries,
comment-only citations, hidden conditional citations, or uncited BibTeX
entries.

Pass 2 held that extraction fixed and checked each claim in order against the
original publication record and the exact source passage. All applicable
author/year/title, full-title, venue, DOI, and arXiv-identifier searches were
run. The release prompt prohibited agents, so the per-reference checks were
performed serially in this single fresh context rather than delegated.

## Claim-by-claim findings

| ID | Key | Manuscript location | Primary-source location | Finding |
|---|---|---|---|---|
| CIT-001 | `CaroTuzaZarb2026` | `main.tex:66-69` | arXiv:2605.22077v2, definition; Theorems 5.1 and 6.1; Section 7, Problem 1 | Verified, exact. For the five-vertex non-star tree with independence number three, the stated results specialize to `8 <= f(T*) <= 16`, and the source asks for every tree value. |
| CIT-002 | `CaroTuzaZarb2026` | `main.tex:99-100` | Theorem 5.1(2), proof | Verified, paraphrase. Its construction `(alpha(H)-1)K_(k-1)` specializes exactly to `2K4`. |
| CIT-003 | `IgnatievMorgadoMarquesSilva2018` | `main.tex:181-184` | PySAT paper, Section 3.1, PDF pp. 3-4 | Verified, exact. The toolkit lists Glucose 3 and gives a direct `Glucose3` interface example. |
| CIT-004 | `AudemardSimon2009` | `main.tex:183-184` | Official IJCAI paper, Sections 3-5, pp. 401-403 | Verified, exact. The paper develops the LBD clause-learning/deletion method and names the resulting solver GLUCOSE. |
| CIT-005 | `HeuleHuntWetzler2013` | `main.tex:190-198` | FMCAD paper, Section II.D and Sections IV-V, pp. 182-185 | Verified, exact. It defines RUP by unit propagation to conflict, an empty-clause refutation, and deletion-aware checking. |
| CIT-006 | `ZengLiuRatnaveluHuat2026` | `main.tex:224-227` | Preprints.org v1, Abstract, Sections 3-4 and 6 | Verified, paraphrase. The paper uses exact finite graph certificates, independent reconstruction, and a separate exact implementation; the manuscript limits the citation to methodological comparison. |

## Bibliographic identity and coverage audit

All five records exist and their retained title, author, year, venue/version,
page, DOI/arXiv identifier, and URL fields agree with the primary records at
the precision asserted in the bibliography. No BibTeX entry or citation key
needed replacement; the old-to-new key map is empty. The five entries in
`manuscript/references.bib` are all cited, and no source remains unofficially
identified or blocked.

The bibliography is not user-library-only. Caro--Tuza--Zarb is the natural
primary origin and closest-prior source. Ignatiev--Morgado--Marques-Silva,
Audemard--Simon, and Heule--Hunt--Wetzler are the natural primary sources for
the actually used PySAT, Glucose, and RUP/deletion-aware methods. The selected
library record is only a narrow, relevant comparison with another independent
exact finite graph-certificate architecture; it is not evidence for the new
theorem. A second library citation would be redundant rather than filling a
coverage gap.

The active user-library selection is bound to the current 49-record registry,
attempt 1, and runner-issued launch UUID. Its UTC verification date is
2026-09-10. The installed hook-compatible validator accepted the smallest
literal citation-bearing context at `main.tex:224-227` after scope-preserving
TeX notation sanitization; citation content and bibliography keys were not
changed.

## Bounded current-literature check

Fresh searches for the exact title and arXiv identifier and combinations of
`H-exact`, `Exact(H)`, `fork`, and `subdivided claw` found the current v2 source
and secondary reviews, but no later primary resolution of this exact case. This
supports only the manuscript's dated, explicitly bounded sentence; it is not a
priority or exhaustive-novelty certification.

## Primary sources consulted

- https://arxiv.org/abs/2605.22077 and its v2 full text.
- https://www.ijcai.org/Proceedings/09/Papers/074.pdf.
- https://doi.org/10.1007/978-3-319-94144-8_26 and the authors' full preprint.
- https://doi.org/10.1109/FMCAD.2013.6679408 and the authors' full paper.
- https://www.preprints.org/manuscript/202608.1658.

No citation is blocked or uncertain at the level asserted in the manuscript.

