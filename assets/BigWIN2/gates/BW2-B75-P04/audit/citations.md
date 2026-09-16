# Citation and bibliography audit

Release job: `win-00075-p04-release-8bfe4f162cde`  
Citation attempt: 2  
Launch UUID: `8ba15444-fb5e-4881-92aa-4d2ef40e7da3`  
Verification date (UTC): 2026-09-09

## Frozen extraction

Pass 1 was frozen in `audit/citation-claim-ledger.json` before source
verification.  It contains ten citation-bearing claims and exactly the six
ordinary body-flow keys extracted from `manuscript/main.tex`.  Their union is
`dai2024norm`, `dlmf`, `galanopoulos2014generalized`, `li2026norm`,
`meurer2017sympy`, and `zeng2026counterexample`.  The read-only bibliography
checker found six cited keys, six BibTeX entries, no missing or unused entry,
and exact agreement with `manuscript/main.aux`.
The live hook-compatible user-library selection validator also passed with the
runner-issued attempt and launch UUID.  Source checks were performed serially
in this release context because the job explicitly prohibited subagents.

## Independent claim-to-source verification

| Key | Nearby claim(s) and exact primary location | Bibliographic record checked | Result |
|---|---|---|---|
| `galanopoulos2014generalized` | The contextual claim that generalized Hilbert operators have been studied on analytic spaces.  The publisher abstract defines the generalized operator and says it is studied on Hardy, weighted Bergman, and Dirichlet-type spaces. | Annales publisher record and article, vol. 39 (2014), pp. 231--258, DOI [10.5186/aasfm.2014.3912](https://doi.org/10.5186/aasfm.2014.3912). | Verified (paraphrase); authors, title, year, volume, pages, and DOI match the BibTeX. |
| `dai2024norm` | The contextual claim that exact norm questions on weighted Bergman spaces are active.  The publisher abstract states the Hilbert-matrix norm conjecture and identifies parameter ranges proved in the paper. | Journal of Functional Analysis 287 (2024), article 110587, DOI [10.1016/j.jfa.2024.110587](https://doi.org/10.1016/j.jfa.2024.110587). | Verified (paraphrase); title, author, venue, year, volume, article number, and DOI match. |
| `li2026norm` | Claims CIT-02--CIT-05 and CIT-07--CIT-08.  The official v1 HTML gives the integral representation at lines corresponding to Section 2.3, displays Corollary 3.5 and (3.38), states Theorem 3.4 with a threshold depending only on alpha, displays (3.41), and ends that proof by invoking Corollary 3.5. | Official [arXiv:2609.04833v1](https://arxiv.org/html/2609.04833v1), submitted 2026-09-04; title and five authors match.  Exact locations: Section 2.3, formula for the operator; Corollary 3.5, (3.38); Theorem 3.4 and proof, (3.41)--(3.42). | Verified (exact/paraphrase as appropriate).  The manuscript preserves the source's awkward quantifier order and explicitly labels its interpretation as natural rather than pretending the wording is unambiguous. |
| `dlmf` | The claim that DLMF Section 5.7(i) is a standard source for the log-Gamma power series used in the proof.  Equations 5.7.3--5.7.4 give the log-Gamma/digamma series; expanding the logarithm in 5.7.3 (equivalently integrating 5.7.4) yields the displayed series on the manuscript's smaller domain, absolute value of z less than 1. | NIST DLMF [Section 5.7(i)](https://dlmf.nist.gov/5.7), release 1.2.7 dated 2026-06-15. | Verified (exact mathematical equivalence); institutional title, section, release, and URL match. |
| `zeng2026counterexample` | The comparison claim says a genuine finite-dimensional norm disproof supplies explicit matrices and exact rational separators.  Section 2 displays two real 2 by 2 rank-one matrices in (7), and (11)--(18) give seven positive rational differences separating the attained ratio from the conjectured constant. | Primary [Preprints.org v1 full text](https://www.preprints.org/manuscript/202608.1067/v1), DOI [10.20944/preprints202608.1067.v1](https://doi.org/10.20944/preprints202608.1067.v1); arXiv:2608.15558 independently confirms title, authors, and abstract. | Verified (exact).  This is registry row 2 and is the sole natural user-library selection; the other 48 entries would not support a claim made here. |
| `meurer2017sympy` | The software citation identifies SymPy, while the assertion that version 1.14 was used is a process fact checked directly in the release environment (`sympy.__version__ == 1.14.0`) and by rerunning both evidence programs. | PeerJ Computer Science 3:e103 (2017), DOI [10.7717/peerj-cs.103](https://doi.org/10.7717/peerj-cs.103); the publisher paper and official paper repository agree on the title and complete author list. | Verified.  The citation supports software identity; the local run supports the actual-use/version claim. |

All ten ledger claims are supported.  No citation was decorative or removable:
the list includes the problem's primary source and closest result, two natural
context sources, the special-function method source, the software record, and
one claim-driven user-library comparison.  Five sources are non-library
sources in ordinary body flow, so the library minimum does not displace normal
scholarly coverage.  No additional registry item naturally supports the paper.

## Outcome and limits

PASS.  All six records exist and match their retained BibTeX metadata; every
nearby attributed claim is supported at the stated primary location.  There
are no undefined citations, key changes, unresolved metadata conflicts, or
unverified bibliography items.  This audit checks citation truth and coverage;
it does not turn the literature search into a priority guarantee or the build
into mathematical proof.
