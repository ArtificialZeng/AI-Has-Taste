# Fresh citation and claim audit

Audit date: 2026-09-06.  Method: explicitly invoked
`$citation-check-skill`, using its two-pass search-verification workflow for
the cited literature and frozen-evidence verification for the paper's new
mathematics and computations.  Pass 1 is fixed in
`audit/citation_claims.md`; no claims were added during this verification
pass.

## Summary

All 22 extracted claims are supported at their stated scope.  No citation is
undefined, no reference is misattributed, and no numerical mismatch was found.
The manuscript does not assert absolute priority: its statements about the
remaining two-parameter problem are expressly statements of the note's limited
scope and of a bounded source comparison.

## Claim-to-source verification

| Claims | Status | Verification |
|---|---|---|
| C01, C07--C13, C16, C18 | Verified (exact mathematical scope) | The accepted frozen mathematical report `audit/math.md` reconstructs the singleton-cut lower bound, the cut-dual certificate, the all-cut primal certificate, and both small Hamiltonian cycles.  The manuscript theorem and limitations match `claim.json` without strengthening. |
| C02 | Verified (exact) | Wang, Lemma 7, states that a graph on at least three vertices is fractionally Hamiltonian iff the complete cut LP has optimum equal to its order. |
| C03--C04 | Verified (exact) | Wang defines the same `J_{m,ell}` family; Proposition 15 gives `tau(J_{m,ell})=1+ell/m`, and Proposition 16 gives non-RN for `m>=2ell+4`. |
| C05--C06 | Verified (exact plus elementary implication) | Wang, Theorem 4, gives FH implies RP.  Wang also explicitly records RP implies RN in the containment/threshold discussion.  Therefore Proposition 16 excludes FH; at `ell=1` its sufficient range begins at `m=6`. |
| C14--C15 | Verified (exact reproduction) | A fresh run of `python3 evidence/cut_lp_certify.py verify evidence/J_m_1_certificates.json` reproduced `evidence/J_m_1_verification.json` byte-for-byte (SHA-256 `48a5aecc5180e3ab4ee945937bcb9ba10c5ba7bd41e975dfa36bf3427b24c009`).  It records exactly 31, 127, 511, 2047, and 8191 cuts, minimum cut 2, maximum dual load 1, and matching objectives. |
| C17 | Verified (paraphrase, deliberately narrow) | The official Preprints.org record for Zeng et al. describes exact distance-layer colorings, a symmetry-reduced enumeration, integer-predicate maximum-clique checks, and explicit finite-library limitations.  This supports only the manuscript's methodological comparison; the manuscript correctly says it is not fractional-Hamiltonicity prior art. |
| C19 | Verified as a scope statement | The manuscript says only that it does not solve the original all-parameter task and disclaims absolute priority.  The bounded literature comparison is not converted into a global novelty or open-status claim. |
| C20 | Verified from artifacts | The disclosed assistance matches the project record, and `evidence/cut_lp_certify.py` imports and uses `fractions.Fraction`. |
| C21 | Verified (exact metadata) | Official arXiv v1 record: Zhiyu Wang, exact title, arXiv:2609.03412v1, math.CO, submitted 3 September 2026. |
| C22 | Verified for cited use and displayed metadata | The official Preprints.org Version 1 record gives the exact title, four authors, preprint status, submission 21 August 2026, and posting 24 August 2026.  Its abstract and Sections 3, 4, 6, and 7 support the narrow methodological comparison. |

## Primary sources inspected

1. Zhiyu Wang, *Toughness Bounds for Fractional Hamiltonicity and Resistance
   Positivity*, arXiv:2609.03412v1.  Official abstract/version record:
   <https://arxiv.org/abs/2609.03412v1>; original HTML text inspected at
   <https://arxiv.org/html/2609.03412v1>, specifically Lemma 7, Theorem 4,
   Propositions 15--16, and their hypotheses.
2. Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, *Exact Finite
   Certificates for the Four-Dimensional Ternary Borsuk Problem and
   Five-Dimensional Ternary Kissing Codes*, Version 1.  Official record and
   original text: <https://www.preprints.org/manuscript/202608.1658/v1>.

For each academic citation, all applicable prescribed title/author/venue and
identifier search forms were run.  The DOI resolver and Crossref/DataCite API
endpoints for `10.20944/preprints202608.1658.v1` were not reachable from the
bounded environment (DNS/safe-URL failures).  This optional endpoint limitation
does not affect the claim mapping: the authoritative Preprints.org manuscript
record was directly accessible and supplies the authors, title, dates, version,
content, and finite-scope language actually relied upon.

## Dependency and rendered-reference scope

`publication.json` lists exactly five release sources: the TeX source, BibTeX
database, verifier, certificate, and captured verification output.  The TeX
recorder and BibTeX log show no other local authored dependency or imported
figure/style.  All five files were individually inspected or executed.  The
rendered PDF contains both bibliography entries and resolved callouts `[1]` and
`[2]`; text extraction contains no `?` placeholder.  The Zeng paper is the
genuinely relevant item from `literature/user_bibliography_check.md` and is used
only for the methodological proposition that its official text supports.

Verdict: **accept**.

