# Fresh citation audit

Audit date: 2026-09-09.  Method: the requested `citation-check-skill` v2 was
applied as an advisory two-pass check, supplemented by direct inspection of the
primary-source text.  The extraction below was fixed before verification.

## Pass 1: fixed claim extraction

- C01 (attribution, pp. 1 and 3): Kozlov studies Euler characteristics for
  generalized anchored configuration spaces and determines their homology on
  circle graphs.
- C02 (attribution, pp. 1 and 3): Mamun--Nalikka--Ramos prove a
  fixed-parameter finite-generation theorem for pointed cographs and a uniform
  restriction on possible integral torsion.
- C03 (attribution, p. 1): their discussion says integral torsion for anchored
  configuration spaces is not known in general beyond the established tree and
  cycle cases.
- C04 (comparative, p. 3): the two cited works do not themselves supply the
  all-degree, all-finite-graph singleton-anchor theorem stated here.
- C05 (attribution/interpretation, p. 3): for connected graphs, the displayed
  Euler characteristic is the singleton-anchor specialization of Kozlov's
  formula.
- C06 (exact numerical claim, p. 3): the retained diamond computation has
  chain ranks `(37,105,75)`, 63 nonzero Smith factors all equal to one, and
  homology ranks `(1,6,12)`.
- C07 (mathematical claim, pp. 1--2): the stated singleton-anchor homology
  formula and torsion-freeness hold at the accepted scope.
- C08 (mathematical claim, p. 2): a torsion witness must satisfy
  `|K|>=2` and `n>=|K|+2`.
- C09 (bibliographic existence/metadata): the Kozlov record has the title,
  author, journal, volume, issue, pages, year, and DOI printed in the references.
- C10 (bibliographic existence/metadata): arXiv:2609.04554v1 has the title,
  authors, year, and version printed in the references.

There are no charts, tables, or empirical data graphics to extract.  Definitions
and descriptions of the author's proof method were not treated as external
factual claims.

## Pass 2: verification

- C01 is verified by Kozlov's abstract and Sections 2 and 4: the paper gives an
  Euler-characteristic formula for arbitrary connected non-tree graphs and an
  all-degree homology calculation for generalized anchored spaces on a cycle.
- C02 is verified by Corollary 4.18 of Mamun--Nalikka--Ramos.  It states finite
  generation at fixed `(i,r,n)` and a uniform exponent divisor
  `d_{i,r,n}` for the integral homology groups.
- C03 is verified by the discussion immediately after Corollary 4.18, which
  identifies the anchored torsion question as unresolved and names trees and
  cycles as the torsion-free cases then known.
- C04 is supported at the manuscript's deliberately bounded wording.  Kozlov's
  result is an Euler-characteristic theorem for general connected non-trees and
  a homology theorem for cycles; Mamun--Nalikka--Ramos give finite generation
  and torsion-exponent restrictions.  The paper makes no priority claim.
- C05 is verified as an explicit specialization of Kozlov, Corollary 2.2:
  set his anchor parameters to `k=q=1` and
  `epsilon=|E|-|V|=beta-1`.  His expression becomes
  `(-1)^(n-1)(beta^n-(beta-1)^n)`, equal to
  `(1-beta)^n-(-beta)^n`.  Confidence: interpretation (transparent algebraic
  specialization, not a verbatim sentence).
- C06 is verified against the frozen exact certificate
  `evidence/diamond_n3/summary.json`; it is explicitly described as a
  nonessential consistency check.
- C07 and C08 are supported by the self-contained manuscript proof and the
  accepted frozen mathematical audit `audit/math.md`.  This release audit does
  not treat that prior acceptance as a literature citation or as proof of
  novelty.
- C09 is verified against the publisher's version-of-record page and the arXiv
  copy (arXiv:2309.17149v2).  The publisher record gives DOI
  `10.1007/s41468-024-00167-8`, Journal of Applied and Computational Topology
  8(4), 1053--1067 (2024).
- C10 is verified against the arXiv v1 record dated 3 September 2026, which
  lists Adityo Mamun, Jonathan Nalikka, and Eric Ramos under the cited title.

Primary sources inspected:

- https://arxiv.org/html/2609.04554v1 (especially Corollary 4.18 and the
  following discussion)
- https://arxiv.org/pdf/2309.17149 (especially Corollary 2.2 and Section 4)
- https://link.springer.com/article/10.1007/s41468-024-00167-8

All citation keys used in the TeX source resolve in the extracted PDF, and the
two rendered bibliography entries agree with `manuscript/references.bib`.
`publication.json` lists the full authored dependency set: `main.tex` and
`references.bib`; the recorder file shows no other project-authored input.

The requested `literature/user_bibliography_check.md` does not exist anywhere
inside this project, so no user-designated Excel record was available to inspect
or invoke as authoritative metadata.  This is a disclosed input limitation, not
an unverified citation: both citations actually used were refreshed successfully
from primary sources and support the nearby prose.  No unrelated reference was
inserted to satisfy a count.  Verdict: **accept**.
