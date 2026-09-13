# Fresh citation and dependency audit

Release job: `bigMac-00005-p04-release-6b0c3be4a6a2`  
Search date: 2026-09-06  
Method: `$citation-check-skill`, search mode, with a fixed extraction pass in
`audit/citation-extraction.md` followed by this verification-only pass.

## Scope and dependency check

The audited PDF is `manuscript/article.pdf` (five pages), with SHA-256
`9d6d73e2b063bf46c585db6af365c7df977d3e134fa78eb6133ce395c552a146`.
The complete authored dependency set is exactly the sorted list
`manuscript/article.tex`, `manuscript/references.bib`.  The TeX source imports
no local figures, styles, or subsidiary TeX files; `article.fls` confirms that
the other local inputs are generated auxiliary/output files.  All three cite
keys in the TeX resolve to distinct entries in the bibliography and appear in
the extracted PDF reference list.  There are no undefined citations.

## Claim-to-source verification

| ID | Status | Confidence | Verification |
|---|---|---|---|
| C01 | Verified | paraphrase | arXiv:2609.03566v1 has the displayed authors/title/date and explicitly studies Cohen--Macaulayness for five increasing-injection edge-ideal families (abstract and Section 1). |
| C02 | Verified | exact | The source's Lemma 3.13 and Theorem 3.14 state that the cycle-chain ideal is the complete-graph ideal, hence Cohen--Macaulay, for `r >= n-3`. |
| C03 | Verified | exact | Conjecture 3.15 gives `n >= 6` and precisely the article's biconditional threshold and excluded value; the paper's standing setup is over a field. |
| C04 | Verified | paraphrase | The primary SSRN record for 7385138 says characteristic zero, graphs on eight vertices, 6,021 relevant isomorphism classes, exact integer arithmetic, and independently checkable kernel-vector certificates.  The manuscript uses only the narrower methodological summary. |
| C05 | Verified | interpretation | This is an explicit scope disclaimer, not a theorem attributed to Zeng.  The SSRN title and abstract concern weak Lefschetz maps of whiskered graphs, not increasing-injection cycle chains or their Cohen--Macaulay classification. |
| C06 | Verified | exact | Reisner's link-homology criterion makes nonzero reduced `H_1` of a two-dimensional complex (empty-face link) an obstruction.  The exact criterion is also stated in the primary Anwar--Ghayas--Javed source, Theorem 2.7. |
| C07 | Verified | interpretation | Specializing the same criterion gives connectedness for a pure one-dimensional complex and vacuity below dimension zero for a nonempty zero-dimensional complex.  These uses also match the accepted mathematical referee report. |
| C08 | Verified | exact | The arXiv and SSRN primary records match their bibliography entries.  Reisner's record is consistently indexed as Gerald Allen Reisner, *Advances in Mathematics* 21(1) (1976), 30--49, DOI 10.1016/0001-8708(76)90114-6. |
| C09 | Verified | exact | Abstract and Theorem 6 exactly match `claim.json` and the scope accepted in `audit/math.md`: every field, `n >= 6`, `r >= 0`, and the unchanged biconditional. |

No extracted claim has a numerical mismatch, hallucinated reference, misleading
attribution, or unsupported strengthening.  The closest-result language is
bounded to the cited source's Theorem 3.14 and Conjecture 3.15; the manuscript
does not claim journal acceptance or guaranteed priority.

## Sources consulted and access limits

- Primary arXiv record and full HTML for Anwar, Ghayas, and Javed,
  <https://arxiv.org/html/2609.03566v1>, especially metadata/abstract,
  Theorem 2.7, Lemma 3.13, Theorem 3.14, and Conjecture 3.15.
- Primary SSRN record for Zeng, <https://ssrn.com/abstract=7385138>, and DOI
  <https://doi.org/10.2139/ssrn.7385138>.
- Reisner bibliographic DOI record,
  <https://doi.org/10.1016/0001-8708(76)90114-6>, cross-checked against
  publisher-indexed scholarly records and the exact criterion as reproduced in
  the Anwar--Ghayas--Javed source.
- Accepted scope/proof audit: `audit/math.md`.
- User bibliography provenance: `literature/user_bibliography_check.md`.

The SSRN PDF endpoint returned HTTP 403, the ScienceDirect Reisner endpoint
returned HTTP 403, and the optional Crossref API was not reachable from the
container.  The audit did not infer unsupported text from those failures: it
used the accessible primary SSRN abstract for the narrow Zeng claim and the
accessible exact scholarly statement of Reisner's criterion for the theorem
use.  No claim depends on unavailable full-text wording.

## Verdict

The citation, attribution, and authored-dependency scope passes.  Immediately
before handoff, the current `checkpoint.md` SHA-256 again matched the digest
recorded in `audit/snapshot.json`, and the full release gate validated the
evidence, manuscript, PDF, reports, build log, and job provenance together.
