# Citation audit

Search date: 2026-08-29.  Status: **PASS**.  Each of the manuscript's three
citations was assigned to a separate isolated audit and checked against
publisher/DOI metadata and the cited theorem text.

## `ERD_S_1961`

- Verified against the Oxford University Press record, DOI
  <https://doi.org/10.1093/qmath/12.1.313>, Crossref, and the archived paper.
- Metadata: P. Erdős, Chao Ko, and R. Rado, *Intersection Theorems for Systems
  of Finite Sets*, *The Quarterly Journal of Mathematics* 12(1) (1961),
  313--320.
- The current entry is an exact field-for-field match to the DOI
  content-negotiation BibTeX.  The publisher page range 313--320 corrects the
  shorter 313--318 range appearing in Huang--Zhang's bibliography.
- Context verified: the original uniform intersecting-family theorem gives
  the star-size bound, and \(\delta_0(\mathcal F)=d_{\mathcal F}(\varnothing)
  =|\mathcal F|\), so the manuscript's \(d=0\) characterization is exact.

## `Huang_2026`

- Verified against DOI <https://doi.org/10.1016/j.jcta.2026.106163>, Crossref,
  Elsevier, and arXiv:2407.14091v1.
- Metadata: Hao Huang and Yi Zhang, *On a d-degree Erdős--Ko--Rado Theorem*,
  *Journal of Combinatorial Theory, Series A* 221 (July 2026), article 106163.
- The current entry exactly matches the official DOI-exported BibTeX.
- Context verified: Conjecture 4.1 has \(k>d\ge0\), \(n\ge2k+1\), and the bound
  used in the manuscript; Theorem 1.1 proves it for \(d\ge2\) and
  \(n\ge2k+2d-3\).  At \((4,3)\), these thresholds are respectively 9 and 11.

## `https://doi.org/10.48550/arxiv.2605.17945`

- Verified against arXiv:2605.17945v1 and DOI
  <https://doi.org/10.48550/arXiv.2605.17945>.  The DOI is registered through
  DataCite; a Crossref 404 is therefore not evidence of a missing record.
- Metadata: Luyining Gan, Jie Han, and Seonghyuk Im, *Note on the codegree
  version of the Erdős--Ko--Rado theorem*, arXiv preprint, submitted May 18,
  2026; only v1 existed at the audit cutoff.
- The current entry exactly matches the DOI content-negotiation BibTeX.  Its
  URL-shaped key is legal and was retained to preserve that official block.
- Context verified: Theorem 1.2 assumes \(d=k-1\) and
  \(n\ge2k+\lceil(\sqrt{8k+1}-1)/2\rceil+3\).  At \(k=4\) this is
  \(8+3+3=14\), so it does not cover \(n=9,10\).  The manuscript wording was
  sharpened to state the specialization \(d=k-1\) explicitly.

## Novelty and bibliography scope

The independent second novelty pass found no earlier public source proving
either endpoint, subject to the explicit limitations in
`literature/search_log.md`.  The manuscript therefore avoids categorical
priority language: it says only “to the best of our knowledge,” gives the
search date, and describes \(9,10\) as values not covered by Huang and Zhang's
theorem.

The final clean build confirmed no missing, undefined, duplicated, or unused
bibliography keys and no BibTeX warnings; full build details are recorded in
`audit/PDF_AUDIT.md`.
