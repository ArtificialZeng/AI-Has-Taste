# Fresh citation and hallucination audit

**Mode:** search verification using the explicitly requested
`citation-check-skill` two-pass method  
**Document:** `manuscript/main.pdf`, six pages  
**Search date:** 2026-09-07  
**Pass-1 input:** `audit/citation-claims.md`, fixed before verification

## Summary

All sixteen fixed claims are verified at their stated scope. There are no
numerical errors, missing citations, unsupported attributions, hallucinations,
or misleading strengthenings. The manuscript cites five genuine works, uses
the user-bibliography paper only for its supported finite-certificate/scope
comparison, and does not represent that paper as mathematical support for the
charged-core theorem.

| Status | Count | Claims |
|---|---:|---|
| Verified | 16 | C01--C16 |
| Citation not found / unverified | 0 | -- |
| Numerical error / hallucination / misleading | 0 | -- |

## Pass-2 findings

| ID | Status | Primary-source check |
|---|---|---|
| C01 | Verified (exact) | Gerber--Norton v1 defines the charged symbol by `S(lambda,s)={lambda_k-k+1+s}` and Lemma 2.11 gives exactly the nested-row core criterion used in Section 1. |
| C02 | Verified (exact) | Gerber--Norton v1 equation (5.3) is exactly `phi(q)c_3(q)^2=c_{6,(0,3)}(q)+2q c_{6,(0,1)}(q)`. |
| C03 | Verified (exact) | Gerber--Norton v1 Table 2 marks both `(0,1)` and `(0,3)` at `e=6` “conjecturally yes”; the paragraph after Conjecture 3.10 says both are equivalent to the remaining `e=6` case and only computer-supported. |
| C04 | Verified (exact) | Springer and arXiv 2211.03987 agree on Ben Kane and Daejun Kim, the title, Selecta Mathematica 32, article 5 (2026), and DOI `10.1007/s00029-025-01110-0`. |
| C05 | Verified (exact) | The open Springer full text, Proposition 2.2, states the elementary theta transformation with the integrality hypotheses, even `b`, divisibility `2N|c`, phase, character factors, and transformed coset used by the manuscript. |
| C06 | Verified (exact) | The publisher DOI record, arXiv 2507.16225, and Savitt's author-hosted paper agree on title, author, Research in Number Theory 11 (2025), article 78, and DOI `10.1007/s40993-025-00660-8`. |
| C07 | Verified (paraphrase) | Savitt Theorem 1.1 gives Newman's two congruence criteria; the following cusp condition and Theorem 3.5 provide the modularity/Nebentypus ingredients invoked. The manuscript performs its own substitutions and character arithmetic. |
| C08 | Verified (exact) | Elsevier and the author's paper agree on Robert J. Lemke Oliver, title, Advances in Mathematics 241 (2013), pp. 1--17, and DOI `10.1016/j.aim.2013.03.019`. |
| C09 | Verified (exact) | Lemke Oliver equation (2.3), p. 6 of the author PDF, states the eta-quotient cusp-order formula used in Section 3. |
| C10 | Verified (exact) | The authoritative Preprints.org version-1 page gives the exact title, Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, submission/posting dates in August 2026, and record `202608.1658`; the DOI query resolves to `10.20944/preprints202608.1658.v1`. |
| C11 | Verified (paraphrase) | The Preprints.org abstract describes an exhaustive exact finite-set certificate and two exact maximum-clique computations, then states that these finite-library theorems do not settle the ambient Borsuk or unrestricted kissing-number problems. |
| C12 | Verified (exact) | Gerber--Norton Section 1.3 and the Archive of Formal Proofs both state the excluded form `4^a(8b+7)` for Legendre's three-square theorem. |
| C13 | Verified (exact) | Gerber--Norton Lemma 1.11 gives `psi(q)^2=phi(q)psi(q^2)` at the manuscript's normalization and derives its product formulas from Jacobi's triple product; its core-product formula gives `c_3(q)=(q^3;q^3)_infinity^3/(q;q)_infinity`. Direct algebra confirms the displayed Gauss product for `psi`. |
| C14 | Verified (exact/internal) | The methodological paragraph expressly disclaims mathematical dependence, and no proof step cites the finite-geometry paper. |
| C15 | Verified (exact/internal) | The abstract and Section 5 leave `(0,3)` and the original conjunction unresolved and make no priority claim. |
| C16 | Verified (exact) | PDF extraction and all six rendered pages show five complete bibliography entries with resolved in-text numbers. Final LaTeX/BibTeX logs have no undefined citation; neither removed SSRN identifier occurs in source, bibliography, `.bbl`, or extracted PDF text. |

## Search and source scope

For each academic citation, the mandatory author/year/title-prefix,
exact-title-on-arXiv-or-Semantic-Scholar, author/year/venue, DOI, and applicable
arXiv-ID queries were run. Original text, not DOI existence alone, was inspected:

- Gerber--Norton v1: `https://arxiv.org/html/2609.03738v1`.
- Kane--Kim open full text: `https://doi.org/10.1007/s00029-025-01110-0`.
- Savitt primary author PDF: `https://math.jhu.edu/~savitt/papers/pdfs/newman.pdf`.
- Lemke Oliver primary author PDF: `https://lemkeoliver.github.io/papers/06-EtaTheta.pdf`.
- Zeng et al. authoritative record/full text: `https://www.preprints.org/manuscript/202608.1658`.
- Archive of Formal Proofs, *Three Squares Theorem*:
  `https://isa-afp.org/entries/Three_Squares.html`.

The Preprints.org HTML did not expose a separate machine-readable DOI field, but
the publisher landing record and exact DOI search agreed; no optional metadata
endpoint was needed. The paper is correctly labeled version 1 and not peer
reviewed. No priority claim was audited or inferred.

## Dependencies and rendered references

Every path in the sorted `publication.json` `source_files` list was inspected.
Both verifier scripts reran successfully and reproduced empty mismatch lists;
the two JSON certificates match their frozen digests. `main.tex` imports no
authored figure, style, or subsidiary TeX file, and `references.bib` contains
exactly the five rendered entries. The declared dependency scope is complete,
the extracted/rendered references resolve, and there are no undefined
citations.

**Verdict: accept.**
