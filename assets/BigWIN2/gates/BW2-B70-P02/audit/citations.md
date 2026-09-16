# Verification Report

**Mode:** Search verification  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Generated:** 2026-09-08

| Metric | Count |
|---|---:|
| Total frozen citation claims | 4 |
| Verified | 4 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall Status:** PASS: all four frozen citation claims are verified.

## Release binding

Release job `win-00070-p02-release-7fa60259311e`, citation attempt 2, launch
`5ff259c2-8fb0-4fb0-a0f6-a476297147cf`; checked 2026-09-08.

## Two-pass procedure

Pass 1 read the complete canonical manuscript and froze the four substantive
claim/citation pairs in `audit/citation-claim-ledger.json` before source
verification (ledger SHA-256
`7696c603b8d9103cd3c7fb5efe4bbcaa3d090de222d815b12d652578ed4d1568`).
The union of its keys is exactly the ordinary body-flow citation set:
`Hutchinson1981`, `Johansson2017Arb`, `MaoWu2026`, and `ZengEtAl2026`.

Pass 2 used title, author/year/venue, DOI, and arXiv-identifier searches for
each frozen key and then inspected the primary record and the exact supporting
passage. The user prohibited agent delegation for this bounded worker, so the
four per-key checks were performed serially in this fresh release context.
Detailed machine-readable locators are in
`audit/citation-source-verification.json`.

## Claim verification

| Claim | Key | Primary passage | Result |
|---|---|---|---|
| CIT-01 | `Hutchinson1981` | Hutchinson, Section 4.4, pp. 15--16, Theorem 4.4(1): the weighted similitude operator is a contraction and has a unique invariant probability measure. | Verified, faithful paraphrase. |
| CIT-02 | `MaoWu2026` | Official arXiv v1 HTML: Proposition 3.3 (lines 297--306), numerical Section 4.3 (lines 562--589), and the explicit non-proof Remark (line 590). | Verified, including the exact interval and scan endpoint. |
| CIT-03 | `Johansson2017Arb` | Johansson's abstract and Section 1 identify Arb as arbitrary-precision midpoint-radius interval/ball arithmetic with rigorous error tracking; the official Arb citation page supplies the journal record. | Verified. The source does not purport to support this manuscript's project-specific depth or precision, which are local reproducibility facts. |
| CIT-04 | `ZengEtAl2026` | Preprints.org v1, Section 6 describes separated certificates and exact verifiers; Section 7 explicitly confines the claims to finite libraries; the disclosure says finite claims rest on reductions and released exact verifiers. | Verified as a methodological comparison, not as Fourier-analysis evidence. |

All four cited works exist. Author, title, year/version, venue, pages where
applicable, DOI/arXiv identifier, and nearby-claim support agree with
`manuscript/references.bib`. No BibTeX replacement or citation-key change is
needed, and no source was unverified. The Zeng et al. item is explicitly a
non-peer-reviewed preprint and is used only for the narrow method comparison.

## Coverage and consistency

The bibliography is neither user-library-only nor decorative. Hutchinson is
the natural primary source for invariant-measure existence and uniqueness;
Mao--Wu is the problem-origin and closest-prior-result source; Johansson is the
primary method/software source for Arb; and Zeng et al. is the single relevant
active user-library item for proof-carrying finite certificates. The other 48
library records concern different problems and would not naturally support a
nearby claim. The elementary interpolation remainder is derived in the paper,
so it does not depend on an uncited external theorem in a way that impairs
self-containment.

The selected library item is cited directly in ordinary body flow at
`manuscript/main.tex` lines 236--240. The selection is bound to the active
49-record registry and to this exact attempt and launch in
`audit/user-bibliography-selection.json`. Three natural non-library citations
also occur in ordinary body flow.

The read-only BibTeX checker found four cited keys, four bibliography entries,
no missing or unused entries, and exact agreement with the final AUX. The
converged `main.log` and `main.blg` contain no undefined citation/reference,
missing database entry, repeated entry, BibTeX warning, LaTeX error, or fatal
diagnostic. The manuscript does not strengthen the accepted theorem: it
repeatedly limits the certificate to 1024 and leaves the original assertion
through `10^7` unresolved.

## Primary records inspected

- <https://doi.org/10.1512/iumj.1981.30.30055> and the author-hosted full text
  <https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf>
- <https://arxiv.org/html/2609.04701v1>
- <https://doi.org/10.1109/TC.2017.2690633>,
  <https://arxiv.org/abs/1611.02831>, and
  <https://arblib.org/credits.html>
- <https://doi.org/10.20944/preprints202608.1658.v1> and
  <https://www.preprints.org/manuscript/202608.1658>

Verdict: **accept**. All frozen citation claims are supported and bibliography
coverage is complete for the manuscript's actual external dependencies.
