# Fresh citation audit

## Scope and method

This audit was performed by release job
`bigMac-00008-p02-release-3defdfe0b6e1` on 2026-09-07 (Asia/Shanghai),
against evidence snapshot
`cf4597267e383e2f6d584b9ff7d0a39dc9e6aea0ab3436c568fe4ad6aebf1752`,
manuscript digest
`a5410eeaa54fffd182f197ac68b5f94a0eb68f05b50790ec06872846b789bff5`,
and PDF digest
`f248e5787b17ec5a563a9de3ac25df0612805c5d84dfbdc5f3e3e2b40cf2a621`.
I explicitly applied the two-pass search-verification procedure from
`citation-check-skill`: claims were first fixed without verification, then
checked in order against primary text and the accepted mathematical snapshot.

## Pass 1: fixed claim extraction

| ID | Claim | Type | Location |
| --- | --- | --- | --- |
| C01 | Tamura and Yamagami prove time-eight rigidity in the real rotation family and propose extension to general two-state unitary coins. | attribution/existence | PDF p. 1, Setting and result |
| C02 | Zeng, Liu, and Ratnavelu use exact rational certificates and equality classification in an unrelated low-dimensional Schatten-norm problem, and their paper supplies no quantum-walk claim. | attribution/comparative | PDF p. 1, Setting and result |
| C03 | Reference [1] has the displayed authors, title, 2026 date, arXiv identifier/version, subject, and submission date. | attribution/temporal | PDF p. 5, reference [1] |
| C04 | Reference [2] has the displayed authors, title, Preprints venue/version, DOI, posting date, and non-peer-reviewed status. | attribution/temporal | PDF p. 5, reference [2] |
| C05 | The complete solution set, weights `1/128`, return probability `3/128`, zero-return locus, and equivalence classification agree with the accepted result. | statistic/existence | PDF pp. 1--2, abstract and Theorem 1 |
| C06 | There are 70 return words, fourteen in each of the five even sojourn classes, and the five displayed coherent sums are exact. | statistic/existence | PDF p. 3, Lemma 3 |
| C07 | The right-phase counterexample at `x=1/4` has the two displayed exact endpoint weights. | statistic/comparative | PDF p. 5, Equivalences |
| C08 | The proof uses an accompanying standard-library exact-arithmetic script, and a separate implementation reconstructed the decisive calculations during review. | existence/methodology | PDF pp. 3 and 5 |

Definitions, proof instructions, hypotheses, and explicitly labelled disclosure
statements were indexed while reading but are not separate external factual
claims under the extraction rules.

## Pass 2: verification

| ID | Status | Evidence and exact support | Confidence |
| --- | --- | --- | --- |
| C01 | Verified | The primary arXiv v1 PDF (SHA-256 `5703bbf648949e50aa49140adece707fa4b8dda128f1d4b850569fa01c495193`) states Theorem 3.1 only for `U(theta)` with `0<theta<pi/2` (pp. 13--14) and Section 5 expressly poses extension to general two-state unitary coins with the listed equivalences (p. 16). | paraphrase |
| C02 | Verified | The publisher record and the primary arXiv full text for arXiv:2608.15558v1 give an exact real `2 x 2` counterexample certified by strict rational inequalities, equality classification for the sharp rank-one theorem, and an arbitrary-complex-matrix `m=2,p=4` result. Neither source concerns quantum walks. | paraphrase |
| C03 | Verified | The authoritative arXiv record gives Shunya Tamura and Tomoki Yamagami, the exact title, submission on 4 September 2026, arXiv:2609.05033v1, and primary class quant-ph. It displays the arXiv-issued DOI while noting that DataCite registration is pending; the paper's scientific support was checked in the primary PDF, not inferred from the DOI. | exact |
| C04 | Verified | The official Preprints.org record gives Zijian Zeng, Houde Liu, and Kurunathan Ratnavelu, the exact title, version 1, posting on 17 August 2026, DOI `10.20944/preprints202608.1067.v1`, and explicit not-peer-reviewed status. The independently accessible arXiv record/full text corroborates title, authors, date, and content. | exact |
| C05 | Verified | Every component is within the accepted `claim.json` statement and `audit/math.md`; there is no strengthening. The equivalent entry-modulus formulation follows immediately from the displayed normal form. | exact |
| C06 | Verified | Fresh runs of `evidence/time8_exact.py` and `audit/referee_recheck.py` both passed: 70 paths, class counts `14,14,14,14,14`, all five matrices, decisive identities, and balanced weights. | exact |
| C07 | Verified | It is part of the accepted equivalence analysis in `audit/math.md` and follows exactly from the displayed endpoint-weight formula at `x=1/4`, for `z=1` and `z=i`. | exact |
| C08 | Verified | `evidence/time8_exact.py` is a standard-library exact symbolic enumerator and passed freshly; `audit/referee_recheck.py` is a distinct finite-field/dense-polynomial implementation and also passed freshly. | exact |

All mandatory academic-citation search patterns were run for both references:
author/year/title prefix, full title restricted to scholarly indexes,
author/year/venue, DOI, and arXiv identifier where present. The direct
Preprints page timed out once;
the official indexed publisher record was then accessible and the primary arXiv
copy supplied full-text corroboration. No claim was accepted from a secondary
snippet alone.

## Claim-to-source fit and novelty boundary

Reference [1] is necessary and supports exactly the nearby rotation-family
theorem and future general-unitary problem. Reference [2] is one of the user's
verified bibliography entries and is genuinely relevant only as the manuscript
says: a methodological parallel in exact low-dimensional complex-matrix work.
The manuscript expressly denies any quantum-walk support from [2], so it is not
misleading. No citation is removable without losing one of those two narrowly
stated roles.

The paper makes no general priority claim. Its only boundary comparison is that
the cited source treats real rotation coins and poses the broader extension;
the primary text supports that comparison. The accepted all-`U(2)` result is
therefore described as a resolution relative to this cited boundary, not as a
claim that all literature was exhausted.

## Dependency and rendered-reference audit

The sorted publication inputs are exactly:

1. `evidence/time8_exact.py`
2. `manuscript/main.tex`
3. `manuscript/references.bib`

The final recorder file confirms that `main.tex` and `references.bib` are the
only authored TeX/bibliography inputs; `main.bbl` is generated. There are no
imported figures, local styles, or included TeX fragments. The exact script is
listed because the manuscript explicitly identifies it as the accompanying
reproducibility source. Thus the declared dependency scope is complete.

The final `.aux` contains both citation keys and both `bibcite` resolutions.
The extracted and rendered PDF shows references [1] and [2] with no placeholders,
tool tokens, missing entries, or undefined citations.

## Verdict

**ACCEPT.** Eight extracted claims were verified, with zero numerical errors,
unverified claims, hallucinations, or misleading attributions. Citation metadata,
nearby support, hypothesis scope, manuscript dependency scope, and the bounded
novelty language all pass.
