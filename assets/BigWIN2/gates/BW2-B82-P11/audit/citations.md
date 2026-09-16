# Citation verification report

Job: `win-00082-p11-release-537ef5a321bf`  
Attempt: 2  
Launch: `152e6e83-305d-41a4-95c4-8d650b1ae110`  
Checked (UTC): 2026-09-09  
Mode: search verification supplemented by the frozen local primary-source PDF

## Summary

The extraction pass was frozen first in `audit/citation-claim-ledger.json`.
It contains seven claim/citation pairs and exactly the four ordinary body-flow
citation keys in `manuscript/main.tex`.  The independent verification pass is
recorded in `audit/citation-verification.json`.  Fresh primary-record searches
and passage replay verified all seven claims;
there are no numerical errors, unsupported citation attributions, misleading
uses, missing sources, or unverified items.

| Metric | Count |
|---|---:|
| Citation-bearing claims | 7 |
| Verified | 7 |
| Numerical error | 0 |
| Misleading | 0 |
| Citation not found / unverified | 0 |
| Hallucination | 0 |

## Claim-level findings

| Claim | Key | Primary source and precise locator | Result |
|---|---|---|---|
| C01 | `AmirkhanyanBushCroot2016` | arXiv:1409.8535v2, abstract and opening definition | Verified (paraphrase): it defines an order-preserving Freiman 2-isomorphism by preservation of order and two-term equalities in both directions. |
| C02 | `Zhang2026Sharp` | local arXiv:2609.08915v1 PDF, Definition 2.1, printed p. 3 | Verified (paraphrase): q-equivalence is equivalence of all balanced mass-at-most-q zero relations, explicitly termed the q-zero profile. |
| C03 | `Zhang2026Sharp` | Proposition 6.5, printed p. 11 | Verified (exact): the bound is `mu q(q+1)` under the stated five-letter rank-one and primitive-mass hypotheses. |
| C04 | `Zhang2026Sharp` | Corollary 9.2, printed p. 19 | Verified (exact): the cluster family has exact diameter `q L_4(q)`; at q=3 this is 33 once `L_4(3)=11`. |
| C05 | `Shin2026Spectra` | arXiv:2609.01690v1, Theorem 10.3 and primary abstract | Verified (exact): the four-point B_h minimum is `binom(h+2,2)+1` for odd h, hence 11 at h=3. |
| C06 | `Zhang2026Sharp` | Question 12.3, printed p. 24 | Verified (paraphrase): it asks for five-letter rank-one maxima separately by primitive mass. |
| C07 | `ZengEtAl2026FiniteCertificates` | Preprints v1, Sections 3, 4, and 6 | Verified (paraphrase): it separates exact finite reductions and stored certificates from independently reconstructed exhaustive checks using integer predicates. |

The theorem-bearing counts in the abstract and proof (160 directions, 65
feasible directions, 40,920 alphabets, and 165 cores) are contributions of
this paper rather than borrowed facts.  They trace to the accepted mathematical
audit and the frozen exact enumerations, so they do not call for decorative
external citations.

## Bibliographic identity and coverage

The author, title, year/version, and venue or repository identity of all four
entries in `manuscript/references.bib` were freshly checked against their primary
records.  The DOI `10.20944/preprints202608.1658.v1` resolves to the selected
Preprints version and matches both the active registry row and the final BibTeX
entry.  No key change was needed.

Coverage is complete without padding.  Zhang is the originating and closest
prior source, Shin supplies the exact four-mark result, and
Amirkhanyan--Bush--Croot supplies the historical order-two formulation.  The
single selected user-library paper is used only for the independently checked
finite-certificate architecture that its text actually documents.  The other
48 active-library records concern different problems and would be unnatural
additions.  Thus the bibliography includes three natural non-library sources
in ordinary body flow and is neither Excel-only nor library-only.

The manuscript accurately limits the literature comparison to the cited
versions inspected in September 2026 and explicitly makes no global-priority
claim.  The very recent posting date is therefore disclosed rather than
silently converted into a novelty assertion.

## Mechanical consistency

The canonical bibliography protocol is `\bibliography{references}`.  The
bibliography checker reports four cited keys, four BibTeX entries, no missing
or unused entries, and exact agreement with the final AUX file.  Final log
scans find no undefined citation, undefined reference, missing database entry,
repeated BibTeX entry, LaTeX error, or fatal diagnostic.

## Primary records consulted

- https://arxiv.org/abs/1409.8535
- https://arxiv.org/abs/2609.01690v1
- https://arxiv.org/abs/2609.08915v1, with exact passages inspected in
  `evidence/external/2609.08915.pdf`
- https://www.preprints.org/manuscript/202608.1658

The bibliography audit was performed serially because this bounded release job
explicitly prohibited spawning agents; each key nevertheless received its own
claim-level primary-record verification.
