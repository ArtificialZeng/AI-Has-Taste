# Fresh citation and claim verification

**Mode:** Search verification, using the two-pass procedure of
`$citation-check-skill`  
**Document:** `manuscript/article.tex` and the rendered
`manuscript/article.pdf`  
**Search date:** 2026-09-06  
**Release job:** `bigMac-00002-p11-release-9217dedd5a5f`

## Summary

| Metric | Count |
|---|---:|
| Fixed claims extracted in pass 1 | 22 |
| Verified | 22 |
| Numerical Error | 0 |
| Citation Not Found / Misquoted | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status: PASS.** Pass 1 is frozen in
`audit/citation-claims.md`; the checks below are the separate verification
pass and do not add claims to that extraction.

## Primary-source checks

1. **Fradelizi--Manui--Meyer--Ndiaye.** The arXiv v1 record verifies the
   title, all four authors, submission date 2026-07-03, subjects
   `math.MG`/`math.FA`, version, and DOI
   `10.48550/arXiv.2607.03582`. The original 41-page PDF states Corollary 29
   on printed page 38 (PDF page index 37), including the general gamma
   constant and sufficiency of parallelograms with a vertex at the origin.
   Substitution of `p=q=2` gives exactly `2+pi/2`. The same page states that
   the translation Firey sums form a shadow system and that their volume
   ratio is convex. Conjecture 5 appears on printed page 39 (PDF page index
   38) and asks exactly for necessity of those parallelograms. Source:
   <https://arxiv.org/pdf/2607.03582v1>.

2. **Zeng--Liu--Ratnavelu--Huat.** The primary Preprints.org record verifies
   the title, four authors, version 1, submission on 2026-08-21 and posting
   on 2026-08-24. The platform's computational-mathematics listing verifies
   DOI `10.20944/preprints202608.1658.v1`. Its abstract expressly calls the
   conclusions finite-library theorems and says that they do not settle the
   ambient Borsuk or kissing-number problems. This supports only the nearby
   restricted-model/ambient-problem comparison; the manuscript explicitly
   says it supplies no proof input. Source:
   <https://www.preprints.org/manuscript/202608.1658>.

3. **Zeng.** The primary Preprints.org record verifies the title, sole
   author, version 1, submission on 2026-08-18 and posting on 2026-08-19.
   The platform's analysis listing verifies DOI
   `10.20944/preprints202608.1272.v1`. Its abstract and Theorem 1 give sharp
   constants on specified operator subclasses while expressly leaving the
   unrestricted fixed-lens value open. This supports only the nearby
   restricted-family/ambient-constant comparison; the manuscript explicitly
   says it supplies no proof input. Source:
   <https://www.preprints.org/manuscript/202608.1272>.

The latter two are the two closest entries identified in the user's cited
Excel list by `literature/user_bibliography_check.md`. They are genuinely
relevant to the one contextual sentence about exact model theorems and are
not represented as prior work on the hexagon theorem.

## Fixed claim verification

| Claim | Status | Basis and location |
|---|---|---|
| C01 | Verified (exact) | Corollary 29, source PDF p. 38; its constant specializes exactly to `2+pi/2` at `p=q=2`. |
| C02 | Verified (exact) | Conjecture 5, source PDF p. 39. |
| C03 | Verified (derivation) | Theorem 1 is exactly the accepted scope in `claim.json` and `audit/math.json`; the exact proof is reconstructed in `audit/math.md`. |
| C04 | Verified (exact) | A centrally symmetric polygon has an even number of vertices; after four (a parallelogram), six is the next possible count. The source's second proof likewise starts the non-parallelogram reduction at six vertices. |
| C05 | Verified (paraphrase) | The finite-certificate paper's abstract says its exact finite-library theorems do not settle the ambient problems. |
| C06 | Verified (paraphrase) | The convex-lens paper proves sharp subclass constants and explicitly leaves the unrestricted constant open. |
| C07 | Verified (paraphrase) | Second proof of Corollary 29, source PDF p. 38, states the translation shadow system and convex volume ratio. |
| C08 | Verified (derivation) | Convexity plus a finite convex combination of polygon vertices gives the displayed maximum reduction; the accepted referee explicitly checked that no strict-convexity premise is used. |
| C09 | Verified (derivation) | The manuscript gives the standard ordered-edge construction of the three centered generating segments; the accepted referee checked the normalization. |
| C10 | Verified (derivation) | Affine normalization at each vertex and the strict conditions `r,s>0` are checked in the accepted proof audit. |
| C11 | Verified (exact) | The zonotope determinant formula gives exactly `4(1+r+s)`; recomputed in `audit/math.md`. |
| C12 | Verified (exact) | Direct sign analysis of `|u1|+|u2|+|r u1+s u2|`; independently reconstructed by the referee. |
| C13 | Verified (exact) | Direct differentiation and `det(vv^T+aa^T)=det(v,a)^2`; independently reconstructed by the referee. |
| C14 | Verified (exact) | Both determinants, endpoint arguments, and the arctangent branch were recomputed in `audit/math.md`. |
| C15 | Verified (exact) | All endpoint and switch terms were independently recomputed and sum to `4(1+r+s)`. |
| C16 | Verified (exact) | Exact combination of the three cone contributions and endpoint terms; diagnostic quadrature also matches. |
| C17 | Verified (exact) | Algebraic substitution of C11 and C16 into the sharp bound. |
| C18 | Verified (exact) | The two cases `r<=s` and `r>s` give the displayed strict lower bounds for every `r,s>0`. |
| C19 | Verified (exact) | The theorem and claim restrict to genuine hexagons at `p=2`; source Conjecture 5 retains the ambient all-body/all-`p>1` question. |
| C20 | Verified (exact) | The closed deficit tends to zero as either interior generator degenerates (`r -> 0+` or, after reorientation, `s -> 0+`), so this argument has no uniform positive gap. |
| C21 | Verified (exact) | Neither the theorem nor its proof asserts a four-generator case; this is a faithful limitation, not a literature claim. |
| C22 | Verified (exact) | `evidence/verify_p2_hexagon.py` was run in this release job on four rational pairs; every asserted error bound and positivity check passed. |

No numerical rounding is used as support for the theorem. The program in C22
is described as diagnostic only, matching its actual role.

## Novelty and scope language

Targeted searches for the exact title/topic combinations, the source arXiv
identifier with "hexagon equality", and Conjecture 5 with the four authors
found the source paper and unrelated hexagon literature but no primary
follow-up containing this six-vertex exclusion. This is only a bounded
negative search, not evidence of priority. The manuscript makes no priority
claim and repeatedly states that Conjecture 5 remains unresolved.

## Dependency and rendered-reference audit

The complete authored dependency list was checked against `publication.json`,
the TeX recorder file, and the latexmk dependency database:

- `evidence/verify_p2_hexagon.py`
- `manuscript/article.tex`
- `manuscript/references.bib`

There are no imported figures, local style files, or additional TeX inputs.
The ancillary verifier is intentionally listed even though it is not a TeX
input. The final `.aux` contains all three expected `bibcite` entries, the
final `.bbl` contains exactly those three sources, and PDF page 4 renders all
three references with readable authors, titles, versions, and DOIs. No `??`,
undefined citation, missing bibliography entry, or unresolved cross-reference
appears in the final PDF or compiler log.

