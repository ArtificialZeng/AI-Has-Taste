# Fresh citation and dependency audit

**Search date:** 2026-09-09 (Asia/Shanghai)  
**Method:** advisory `citation-check-skill`, search mode, with extraction and
verification kept as separate passes.

## Pass 1 — fixed extraction

The complete authored manuscript and rendered reference list were read before
verification.  The substantive source-dependent claims are:

1. `C01` (page 1): Alahmadi, Deza, Dutour Sikirić, and Solé introduced an LCD
   joint-weight-enumerator LP involving a code and its dual.
2. `C02` (abstract, pages 1 and 5): Kang and Xiong define the binary Gauss-phase
   and mixed benchmark LPs, report four exact improvements, and identify
   `(20,8): 7 -> 6` only as a reverse screening observation excluded from their
   exact endpoint claims.
3. `C03` (page 1): the Zeng--Liu--Ratnavelu--Ong preprint is an example of
   finite, independently replayable exact certificates in adjacent coding and
   discrete-geometry computations.  The manuscript expressly disclaims using
   it for an LCD constraint, the theorem, novelty, or priority.

Definitions, the paper's own theorem, certificate counts, exact replay results,
and reproducibility descriptions were not treated as literature attributions;
they were checked against the frozen accepted evidence and fresh exact replays.

## Pass 2 — verification

- `C01` — **verified (exact/paraphrase)**.  The publisher record for *The Joint
  Weight Enumerator of an LCD Code and Its Dual*, *Discrete Applied
  Mathematics* 257 (2019), 12--18, DOI
  `10.1016/j.dam.2018.10.032`, matches the authors, title, venue, pages, year,
  and DOI.  Its abstract and Section 4 explicitly formulate linear constraints
  on the joint enumerator and an LCD linear-programming bound.  Primary record:
  `https://www.sciencedirect.com/science/article/pii/S0166218X18305791`.
- `C02` — **verified (exact)** against arXiv v1.  The versioned HTML at
  `https://arxiv.org/html/2609.08662v1` identifies Kang and Xiong, 8 September
  2026, displays the version-specific title *Gauss-Phase LP Bounds for LCD
  Codes*, gives Definition 4.4 and Definition 5.1, and states both that the
  reverse `(20,8): 7 -> 6` case appears in screening and that it is not included
  among the exact endpoint claims.  The current abstract record uses the longer
  metadata title *Linear Programming Bounds for LCD Codes via Gauss Phases*;
  the manuscript unambiguously cites `arXiv:2609.08662v1`, whose displayed
  title agrees with the bibliography.
- `C03` — **verified (paraphrase, deliberately narrow)**.  The primary
  Preprints.org page for version 1 describes exact finite models, exact
  certificate files, independently replayable standard-library verifiers, and
  integer/rational acceptance checks.  This supports only the manuscript's
  broad adjacent-method comparison.  Primary record:
  `https://www.preprints.org/manuscript/202608.1658`.

For `C03`, `metadata_basis=user_designated_workbook`: the DOI and bibliographic
fields in `literature/user_bibliography_check.md`, transcribed from the user's
authoritative workbook, control this workflow.  External refresh was unavailable
in the original writing scope and remains unavailable in scope as a basis for
replacing that designated record; the bounded advisory lookup nevertheless
found a matching primary page.  No unsupported attribution or novelty claim
depends on this record.

## Resolution and dependency scope

All three `\cite` keys occur in both `manuscript/references.bib` and the rendered
`manuscript/article.bbl`; the final PDF shows references `[1]`--`[3]`, with no
placeholder or unresolved marker.  The bibliography contains no uncited entry.
The accepted theorem is not strengthened in the authored text: it remains the
three frozen LP assertions and expressly disclaims code existence and broader
comparison claims.

Every entry in the sorted `publication.json` `source_files` list was checked:
the TeX, generated BBL, BibTeX database, three exact certificate JSON files, two
standalone checker programs, and two replay reports.  The TeX build imports no
unlisted project-local authored file; the ancillary files cited in prose are all
enumerated.  The dependency scope is complete.

**Verdict: ACCEPT.**  All substantive citations exist and support the nearby,
conservatively bounded prose; there are no undefined citations and no remaining
citation-access limitation requiring qualified acceptance.
