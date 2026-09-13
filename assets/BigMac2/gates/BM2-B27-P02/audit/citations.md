# Fresh citation and dependency audit

## Binding and method

This release audit covers evidence snapshot
`0ecbd967a46f945bd6835b7187032eedfcef4d2f0e168b18c9337c6ecc300ddd`,
manuscript snapshot
`dc1b753854a1dbcfc26cbe1a8276cdacc299b48dbd367fec0babd75df0fe61e3`,
and PDF SHA-256
`97e311fe3a312ace39568a515041bbdeba0d754cefa64d3f96270c5724c53880`.
The audit used the requested citation-check skill as an advisory two-pass
check, followed by manual comparison with primary/publisher records. Search
and inspection date: 2026-09-09.

## Pass 1: fixed claim extraction

The entire three-page manuscript was read before verification. The factual
and attribution claims within the skill's extraction rules are:

- C01: Benevides et al. and Flocchini et al. considered minimum percolating
  sets on grids and tori in closely related formulations (page 1).
- C02: Bushaw and Clifton's Theorems 1.6--1.8 give
  `22 <= t_3(8,8) <= 23` (page 1).
- C03: their Question 4.3 asks when the lower bound is strict, identifies the
  `8 x 10` torus as strict, and does not settle `8 x 8` (page 1).
- C04: the paper proves `t_3(8,8)=22` (pages 1--3).
- C05: the displayed initial set contains exactly 22 vertices (page 2).
- C06: the displayed layer sizes are
  `[22,14,4,3,2,2,2,2,2,2,2,2,2,2,1]` and cover all 64 vertices
  (pages 2--3).
- C07: the complement has 42 vertices, is connected, and has 41 induced
  edges (page 3).
- C08: the three bibliography records have the displayed authors, titles,
  venues/identifier, years, volumes, and pages/article number (page 3).

Definitions, proof steps, methodology descriptions, and the assistance
disclosure were not extracted as external factual claims under the advisory
skill's rules. They were nevertheless checked for consistency with the
accepted mathematical scope and build output.

## Pass 2: verification

| Claim | Status | Evidence and scope |
| --- | --- | --- |
| C01 | Verified (paraphrase) | The publisher abstracts for Benevides et al. and Flocchini et al. explicitly study infection/dynamo processes on grids or tori, including minimum initial sets. The manuscript uses this only as broad context. |
| C02 | Verified (exact) | The inspected arXiv v1 PDF, p. 3, states Theorems 1.6--1.8. For `m=n=8`, `ceil((mn+1)/3)=22`, and Theorem 1.8 gives the upper bound 23. |
| C03 | Verified (exact) | The same primary PDF, p. 38, states Question 4.3 and names `8 x 10`, not `8 x 8`, as a known strict case. |
| C04 | Verified within the accepted local mathematical scope | `audit/math.md` accepts the complete lower-bound argument and independently recomputed trace. The manuscript does not strengthen the frozen claim. |
| C05 | Verified (exact) | Direct count in the displayed set and `evidence/22-set-certificate.json` both give 22. |
| C06 | Verified (exact) | The mandated interpreter reran `evidence/verify_22.py` successfully and returned the identical layer-size vector and final infected size 64. |
| C07 | Verified (exact) | The same exact checker returned 42 complement vertices, one component, and 41 induced edges. |
| C08 | Verified | The Bushaw--Clifton metadata agree with the official arXiv record and the hashed local v1 PDF. Elsevier publisher records verify Benevides et al., DOI `10.1016/j.ejc.2023.103801`, and Flocchini et al., DOI `10.1016/S0166-218X(03)00261-0`; DBLP records provide an independent metadata cross-check. |

Primary records consulted were the official arXiv record and PDF for
arXiv:2608.06133v1, the Elsevier article pages for both journal papers, and
their DBLP records. The local arXiv PDF had the expected SHA-256
`d5e8b1a28649cafea12d4b47fead8a692abb9ee1634a556cbd779d59276073e6`.
No contradicted attribution, unsupported novelty claim, or priority claim was
found. The manuscript's comparison is deliberately limited to the explicit
one-unit gap in the cited preprint.

The requested `literature/user_bibliography_check.md` is absent from the
project, so no workbook-derived record could be inspected or claimed as the
metadata basis. This does not leave any cited record unverified: all three
citations were checked independently against accessible primary/publisher
records. The two older papers are genuinely relevant grid/torus precedents.

## Dependency and resolution check

The complete sorted authored/supplementary dependency scope is:

1. `evidence/22-set-certificate.json`
2. `evidence/verify_22.py`
3. `manuscript/main.tex`
4. `manuscript/references.bib`

`main.tex` has no local figure, imported TeX, or custom-style dependency;
all other TeX inputs in the recorder file are system packages. The JSON
certificate and exact checker are the two declared supplementary files.
All three citation keys occur exactly once as resolved bibliography entries,
all three appear in `main.aux` and the rendered bibliography, and there are
no unused bibliography entries or undefined citations. Extracted PDF text
contains references [1]--[3] with the expected metadata.

## Verdict

**Accept.** Citation support, bounded comparison language, bibliography,
resolved keys, and the complete publication dependency scope pass.
