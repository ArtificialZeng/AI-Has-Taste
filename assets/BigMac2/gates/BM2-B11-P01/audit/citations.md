# Fresh citation and claim audit

**Mode:** search verification, using `citation-check-skill` v2  
**Search date:** 2026-09-07  
**Document:** `manuscript/article.pdf` (five pages)

## Pass 1: fixed extraction

Extraction was completed before verification.  The following externally
checkable or evidence-bound claims were fixed as the audit input.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Colbrook--Stepaniants--Townsend prove, for every restart length \(s\ge4\), a nonterminating dimension-\(s+4\) diagonal SPD example whose even normalized residual directions do not converge. | Attribution / existence | p. 1 and p. 5 |
| C02 | Their paper explicitly asks for the smallest counterexample dimension. | Attribution | p. 1 |
| C03 | Proposition 1.4 and (G.7)--(G.10) supply the factor convergence, energy, chord, fixed-point, and resonant-support facts used in the note. | Attribution | p. 2 |
| C04 | Zeng studies a characteristic-zero relationship between derivative Bezout inversion and distinct-node multipoint evaluation; the citation supplies no restarted-CG dynamics. | Attribution / scope | p. 3 |
| C05 | The note proves convergence through active grade six and concludes only \(7\le n_{\min}(4)\le8\), leaving grade seven unresolved. | Existence / scope | pp. 1 and 5 |
| C06 | An exact-rational standard-library program recomputed five sample restart blocks and checked the listed identities. | Statistic / existence | p. 5 |

## Pass 2: verification

The academic-citation search templates were run for both records (author/year/title
terms, exact-title searches restricted to scholarly indexes, author/year/venue,
and the supplied arXiv or DOI identifier).  The official records and the original
available texts were then inspected.

| ID | Status | Confidence | Verification |
|---|---|---|---|
| C01 | Verified | exact | The official arXiv record for 2609.04659v1 gives the exact title, authors, submission date (4 September 2026), and states the \(s\ge4\), dimension-\(s+4\), nontermination and even-direction nonconvergence result.  The frozen primary PDF states the same in Theorem C.1.1 and gives the restart-four seed in Proposition C.1.2 (physical p. 104). |
| C02 | Verified | exact | The frozen primary PDF's “Consequences and further questions” explicitly names the smallest dimension of nonconvergence as a natural question (physical p. 143). |
| C03 | Verified | paraphrase | Physical pp. 6--9 of the frozen PDF contain the active spectral reduction, signed one-block map (G.5), two-block map (G.7), energy/chord identities (G.8)--(G.10), and Proposition 1.4 with factor convergence, fixedness, and support between \(s+1\) and \(2s\) resonant nodes.  The manuscript preserves the hypotheses and specializes correctly to \(s=4\). |
| C04 | Verified | paraphrase | The canonical Preprints.org v1 record gives Zijian Zeng, the exact title, submission 28 August 2026, posting 31 August 2026, and DOI 10.20944/preprints202608.2160.v1.  Its abstract and §§1--2 concern distinct nodes, derivative Bezout inversion, interpolation, and multipoint evaluation in characteristic zero.  The manuscript makes only a methodological comparison and explicitly disclaims any CG-dynamics implication. |
| C05 | Verified | exact | The theorem text matches `claim.json` without strengthening and preserves `original_status: unresolved`.  `audit/math.json` accepts that exact snapshot.  The upper bound is independently supported by C01; the lower bound is the audited theorem, not attributed to prior work. |
| C06 | Verified | exact | Running `python evidence/verify_grade6_identities.py` on 2026-09-07 reported: five blocks; four division/drift/energy checks; three exact sign-transport checks; and four limiting-functional checks, all passing.  The manuscript correctly labels these finite checks as regression evidence rather than proof. |

All six extracted claims are verified; there are no numerical errors,
hallucinations, misleading attributions, or unverified records.  The comparison
with prior work is explicitly bounded and makes no general priority claim.

## Sources and dependency scope

- Primary record: <https://arxiv.org/abs/2609.04659>; original frozen text:
  `evidence/Colbrook-Stepaniants-Townsend-2609.04659v1.pdf`, SHA-256
  `a8eddb4d369949f3410bc711f657c06725fcbd4e6d8b20ff93a8ddced99244ee`.
- User-list paper and primary record:
  <https://www.preprints.org/manuscript/202608.2160> and
  <https://doi.org/10.20944/preprints202608.2160.v1>.
- Accepted claim and review: `claim.json`, `audit/snapshot.json`,
  `audit/math.json`, and `audit/math.md`.
- Computational disclosure: `evidence/verify_grade6_identities.py`, rerun in
  this release audit.

`publication.json` lists exactly the two authored dependencies
`manuscript/article.tex` and `manuscript/references.bib`.  The TeX recorder shows
no project-local authored figure, style, or imported TeX dependency; `.aux`,
`.bbl`, and `.out` are generated files, and the remaining inputs are system TeX
packages.  BibTeX read `references.bib`; the final `.aux` resolves both citation
keys, and the extracted/rendered PDF contains both bibliography records.  The
dependency scope is complete and there are no undefined citations.

**Verdict: accept.**
