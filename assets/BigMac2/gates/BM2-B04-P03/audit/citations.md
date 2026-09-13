# Verification Report

**Mode:** Search verification with local-primary-source inspection  
**Document:** `manuscript/main.pdf`  
**Generated:** 2026-09-06

## Summary

| Metric | Count |
|---|---:|
| Claims extracted | 6 |
| Verified | 6 |
| Numerical error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status:** PASS. The cited claims, finite verification claims, and
bounded source-comparison language are supported at their stated scope.

## Pass 1: fixed extraction

The following list was fixed before source verification.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Cordella gives a finite-exception theorem for near-tight sextuples, Lemma 2.2's collision/antipode criterion, and an exhaustive search through maximum speed 110. | Attribution + existence + statistic | p. 1 and p. 4 |
| C02 | Cordella's Table 2 gives `ML(V_22)=2/13` and `ML(V_33)=6/37`, and Section 6.1 gives the base-quintuple value `2/11`. | Attribution + statistic | p. 1 |
| C03 | The inspected Cordella source does not give the all-parameter formula for `V_m`; the comparison is limited to that source. | Attribution + existence | p. 1 |
| C04 | Zeng uses exact rational certificates for parameter disks and phase arcs while leaving the unrestricted problem unresolved. | Attribution | p. 4 |
| C05 | The local exact-arithmetic verifier covers all admissible `m<=180`, `n<=100`, and held-out `n=127,251`, recovering the three superlevel components. | Statistic + existence | p. 4 |
| C06 | The manuscript's stated theorem has exactly the accepted full scope and does not promote finite checks into its proof. | Existence | pp. 1--5 |

## Pass 2: verification

| ID | Status | Source and exact support | Confidence |
|---|---|---|---|
| C01 | Verified | Francesco Cordella, *Odd denominators in the Lonely Runner spectrum for six speeds*, arXiv:2609.03444v1: Lemma 2.2 gives the finite collision/antipode candidate set; Theorem 6.1 gives the finite-exception conclusion and no counterexample with speeds at most 110; the abstract and Section 6.1 report the exhaustive search. | exact |
| C02 | Verified | Cordella v1, Table 2 lists `(1,4,5,6,7,22)` with `2/13` and `(1,4,5,6,7,33)` with `6/37`; Section 6.1 states the base quintuple has `2/11`. | exact |
| C03 | Verified | Full-text inspection of Cordella v1 finds this quintuple only as the base example and the two adjoined-runner examples, not an all-`m` value and argmax theorem. The manuscript expressly disclaims comparison beyond this source. | interpretation |
| C04 | Verified | Zijian Zeng, *Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds*, Preprints v1, DOI `10.20944/preprints202608.1272.v1`: the abstract and Sections 1 and 6 describe exact rational disk/phase-arc certificates and state that the unrestricted fixed-lens constant remains open. | paraphrase |
| C05 | Verified | `python3 evidence/verify_family_formula.py` returned `status=pass`, exact `Fraction` arithmetic, 261 parameters, the stated ranges, and the three displayed components on 2026-09-06. | exact |
| C06 | Verified | Theorem 1 and all equality cases match `claim.json` and the accepted `audit/math.md`; the finite checks are explicitly described as supporting calculations and not universal proof. | exact |

## Metadata, search, and dependency audit

- Cordella metadata was checked against the local v1 PDF and the authoritative
  arXiv record: Francesco Cordella; exact title; submitted 3 September 2026;
  arXiv:2609.03444v1; primary class `math.NT`. The prescribed author/title,
  full-title, venue, and arXiv-ID searches were run.
- Zeng metadata was checked against the authoritative Preprints.org v1 record:
  Zijian Zeng; exact title; submitted 18 August and posted 19 August 2026;
  DOI `10.20944/preprints202608.1272.v1`. The prescribed author/title,
  full-title, venue, and DOI searches were run. Direct safe-open of the DOI
  resolver was unavailable; this bounded access limitation was resolved using
  the authoritative host record itself.
- Both rendered references are defined and correspond to bibliography entries;
  there are no unused bibliography entries or unresolved citations.
- `publication.json` lists the complete authored dependency set:
  `manuscript/main.tex` and `manuscript/references.bib`. The recorder file shows
  no other project-local authored input. System TeX packages and generated
  `.aux`/`.bbl` files are not authored source dependencies.
- The required user-bibliography check was inspected. Zeng's paper is genuinely
  relevant only to the narrow methodological comparison used here and is not
  cited for a lonely-runner theorem, history, or priority claim.

No citation is removable without losing context or the required methodological
comparison, and no citation supports a stronger statement than its source.
