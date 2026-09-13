# Fresh citation audit

**Mode:** Search verification, using the two-pass procedure from
`$citation-check-skill`  
**Documents:** `manuscript/main.tex`, `manuscript/references.bib`  
**Search date:** 2026-09-06  
**Frozen claim list:** `audit/citation-claims.md`  
**Overall status:** PASS

Pass 1 fixed eight citation-dependent claims before any verification.  Pass 2
used that list without re-extraction.  Both bibliography entries exist, their
authorship/title/version/date metadata match, and the nearby prose stays within
what the cited sources support.  There are no numerical errors, misleading
attributions, unverified claims, or undefined citations.

## Claim-to-source results

| ID | Status | Confidence | Primary-source support |
|---|---|---|---|
| C01 | Verified | exact | The arXiv record gives Guangjian Zhang, the exact title, submission date 31 August 2026, identifier 2608.30254v1, and primary class cs.LG. |
| C02 | Verified | paraphrase | Zhang's abstract and Section 7 identify the smallest open intermediate cell `(d,m)=(2,2)`, its two budgets, and the unit-circle moment formulation. |
| C03 | Verified | exact | Conjecture 7.8 states the two infimum inequalities with support at most four and three, respectively. |
| C04 | Verified | exact | Proposition 7.9 proves equivalence with systems supported on at most seven atoms. |
| C05 | Verified | exact | Section 7.6.5 states the four-point `2E/9` result for at most five atoms and the three-point `E/2` result for at most four atoms. |
| C06 | Verified | exact | The Preprints.org v1 record gives the exact title, all three authors, and posted date 19 August 2026; the DOI/record identifier is `10.20944/preprints202608.1346.v1` / `202608.1346`. |
| C07 | Verified | paraphrase | The primary abstract states an order-five rank-two correlation-matrix problem, reduction of two permanents to elementary symmetric functions of five unimodular numbers, and exact sum-of-squares and positive-semidefinite Gram certificates. |
| C08 | Verified | interpretation | Full-text scope is permanent inequalities for correlation matrices; searches of the primary text find neither the present finite moment system nor weighted data selection.  The manuscript explicitly calls the comparison unrelated and uses it only methodologically. |

## Source and hypothesis checks

1. **Zhang 2026.** The local original `literature/Zhang-2608.30254v1.pdf`
   was inspected directly.  Its PDF metadata gives the exact author and title.
   Section 7 is headed “The smallest intermediate cell: `(d,m)=(2,2)`”;
   Conjecture 7.8, Proposition 7.9, and Section 7.6.5 contain exactly the
   statements mapped above.  The current primary arXiv record also confirms
   version and submission metadata:
   <https://arxiv.org/abs/2608.30254>.
2. **Zeng--Liu--Ratnavelu 2026.** The relevant user-workbook entry identified
   in `literature/user_bibliography_check.md` was checked against the full
   primary Preprints.org record, including the abstract and displayed exact
   certificates:
   <https://www.preprints.org/manuscript/202608.1346>.
   It is genuinely relevant only as the narrow methodological parallel stated
   in the manuscript and is not used for novelty, open-status, or moment-system
   claims.

For each paper, all applicable academic-citation search templates were run:
author/year/title words; full title restricted to Semantic Scholar or arXiv;
author/year/venue; and the supplied DOI or arXiv identifier.  Verification then
returned to the primary record/full text rather than relying on secondary
results.

## Citation and dependency integrity

- Defined and cited keys: `Zhang2026`, `ZengLiuRatnavelu2026`.
- Undefined citations: none.
- The final `.bbl` contains both entries and matches the source metadata.
- `main.tex` has no `\\input`, `\\include`, or `\\includegraphics` dependency.
  Its sole authored dependency is `\\bibliography{references}`, so
  `publication.json` completely lists the publication inputs as
  `manuscript/main.tex` and `manuscript/references.bib`.
- No citation is unnecessary for the stated scope: Zhang supplies the actual
  problem context; the single workbook citation supplies the expressly narrow
  methodological comparison requested for the generated PDF.

## Scope-strengthening check

The title, abstract, theorem, introduction, and limitations section all retain
the accepted `3+1+1` five-label stratum.  They explicitly say that other
five-label direction patterns, the six-label assertion, and the seven-atom
conjecture remain unresolved.  No citation is used to strengthen the accepted
mathematical statement or to assert priority.

