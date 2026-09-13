# Fresh citation and claim-support audit

Release job: `bigMac-00015-p02-release-5446c3c97a60`  
Search and inspection date: 2026-09-08  
Evidence snapshot: `3cd1d027218b5c503da5bcf5a88808e84a9d69d2d4668141e37fe863084fdff8`  
Manuscript snapshot: `0985f7cdbc5b998ece78db68e8515e1962f6939f4fd1888046a8a93edc89f151`  
PDF: `68054f7988c4c814c29eebfdb86a299f89d84bf6f6734b100e7ead685481b1be`

## Method and fixed extraction

I explicitly applied the available `citation-check-skill` as an advisory
two-pass search audit.  Pass 1 read the complete five-page PDF and froze the
twelve extracted claims in `audit/citation-claims.md` before external
verification.  Pass 2 used that fixed list.  Mathematical statements were
checked against the accepted frozen proof and exact evidence; external
attributions were checked against primary publisher/arXiv records and source
text.  No citation tool was treated as overriding the accepted mathematics or
any user-supplied record.

## Pass 2: claim-to-source findings

| Claims | Finding | Status |
| --- | --- | --- |
| C01, C06--C09 | These are exactly the accepted resolution claim, exact zero-sum formula, existence lemma, localization, and normalization in `claim.json`, `evidence/zero_sum_proof.md`, and the accepted reconstruction in `audit/math.md`.  The corrected PDF prints the product `a m_*(a)`, not the draft's comma-like typo. | Verified, exact |
| C02 | Yu's equations (8)--(9) retain the nearest four zeros and have an error with fixed `R/r`; the manuscript conservatively says this estimate does not *by itself* control every earlier order in the coupled limit. | Verified, paraphrase/interpretation |
| C03 | The APS record for Blume and Elsevier record for Capel give the displayed 1966 titles, authors, venues, volumes and pages.  Yu's introduction explicitly describes the model as independently introduced by these two works in 1966. | Verified, exact/paraphrase |
| C04 | Yu's abstract and Theorem 1 give sharpness at `Delta=log 2`; Proposition 4 states that for every fixed `Delta>log 2` some even cumulant has the strict failing sign. | Verified, exact |
| C05 | Yu's full text, Proposition 4 and equations (8)--(9), pp. 4--5 of the source PDF, match the manuscript's characterization and hypotheses. | Verified, exact/paraphrase |
| C10 | A fresh run of `evidence/exact_recurrence.py` for all six displayed `N` values returned `8,18,56,79,175,552` with negative exact sign certificates; the values match `evidence/exact_sequence.tsv`. | Verified, exact |
| C11 | Bounded arXiv searches for combinations of Blume--Capel, Ursell, cumulant, first failure, the proposed constant, and the arctangent scale returned Yu's paper but no equivalent first-failure result.  The paper explicitly limits this to a bounded comparison and disclaims priority. | Verified as a bounded search report, not a priority claim |
| C12 | APS confirms Blume's DOI `10.1103/PhysRev.141.517`; Elsevier's record confirms Capel's DOI `10.1016/0031-8914(66)90027-9`; arXiv confirms Sheng Chun Yu, title, 2026, category `math.PR`, and version `2609.04610v1`.  The rendered bibliography agrees. | Verified, exact |

Primary records inspected:

- APS article record: `https://journals.aps.org/pr/abstract/10.1103/PhysRev.141.517`.
- Elsevier article record: `https://www.sciencedirect.com/science/article/pii/0031891466900279`.
- arXiv abstract and complete seven-page source: `https://arxiv.org/abs/2609.04610` and `https://arxiv.org/pdf/2609.04610`.

The academic-citation search templates were run for each of Blume, Capel and
Yu (author/year/title, full-title domain search, author/year/venue, DOI where
present, and arXiv identifier for Yu).  All substantive records refreshed from
a primary source.  The optional project path
`literature/user_bibliography_check.md` does not exist, so there was no Excel
comparison artifact to inspect; this access fact does not create an unverified
citation because the three cited records and nearby claims were independently
verified from primary records.  The manuscript includes the two genuinely
relevant classical model papers plus the directly relevant Yu preprint.

## Dependency and resolution audit

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`.  The TeX source has no imported authored TeX,
figures, local style files, or generated data dependencies.  BibTeX and the
recorder data confirm that `references.bib` is the sole bibliography database.
All three citation keys (`Blume1966`, `Capel1966`, `Yu2026`) exist exactly once,
all three are used, and none is undefined.  The extracted and rendered PDF
contains numbered references [1]--[3] with matching author/title/year data.

No attribution is contradicted, no unsupported priority language remains, and
no citation is removable without losing either the historical model context or
the closest-result comparison.  Verdict: **accept**.

