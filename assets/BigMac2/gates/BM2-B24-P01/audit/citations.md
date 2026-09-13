# Fresh citation and dependency audit

Audit date: 2026-09-09.  Method: the requested `citation-check-skill` was
applied as an advisory two-pass check, followed by manual inspection of the
supplied primary-source PDF, the rendered manuscript, the BibTeX database, and
the explicit publication dependencies.  The audit is bound to evidence
snapshot `d0ca5ba0df04480ff06cbbca2b1700e66cf8802807299148fe8ab62fa9a77803`,
manuscript snapshot
`4bbf4ac8a77005d903c1e72d17958753350d4f534d8e5284d38783f79c42531e`,
and PDF `411261c85eb5ff25765d14dcdfdf65ccfc68a9987620f5e6dd7aff59b0679e0f`.

## Pass 1: fixed claim extraction

The source-dependent claims extracted before verification were:

1. The root-finding meaning of “convergent” is that the Fatou set consists of
   root basins (manuscript p. 1).
2. Nayak--Phogat study `p_n(z)=z(z^n-1)` and prove convergence for `n <= 16`
   or odd `n` (p. 1).
3. Their concluding question concerns every even `n >= 18`, and their `n=18`
   table gives a floating-point free-critical orbit with capture after two
   iterates (p. 1).
4. For rational maps, every Fatou component is eventually periodic; periodic
   components have the four listed types; immediate attracting/parabolic
   basins contain a critical point; and rotation-domain boundaries lie in the
   postcritical closure (p. 4).
5. Zeng--Liu--Ratnavelu use strict rational inequalities as proof-carrying
   certificates (p. 1).
6. Zeng's convex-lens paper uses exact rational certificates in a
   complex-analytic problem (p. 1).
7. The five bibliography records have the author/title/year/venue or archive
   metadata printed on p. 5.

The new theorem, exact identities, inequalities, and critical-orbit
classification are proved inside the manuscript and were already within the
accepted mathematical audit; they are not converted into literature claims in
this citation review.

## Pass 2: claim-to-source verification

| Claim | Evidence inspected | Result |
|---|---|---|
| 1 | Nayak--Phogat, supplied PDF p. 3, definition immediately before Theorem D; McMullen's official Annals record and author-hosted paper, Section 1 context | Verified paraphrase.  The componentwise formulation is the manuscript's explicit form of the supplied definition. |
| 2 | Supplied PDF p. 3, Theorem D; arXiv record 2609.02884 | Verified exactly. |
| 3 | Supplied PDF p. 27 concluding question and p. 28 Table 1, row `n=18` (`k=2`, “Yes”) | Verified exactly.  The manuscript correctly calls the table floating-point evidence and does not promote it to proof. |
| 4 | Supplied PDF pp. 5--6, Section 2.2 and Lemma 2.4; Beardon bibliographic record and cited theorem locations | Verified.  The supplied source states all four facts in the hypotheses used by the manuscript. |
| 5 | `literature/user_bibliography_check.md`, designated workbook row 2; arXiv:2608.15558 abstract; Preprints.org manuscript 202608.1067, equations (11)--(18) | Verified.  The nearby prose limits the comparison to certificate style and expressly denies dynamical support. |
| 6 | `literature/user_bibliography_check.md`, designated workbook row 13; Preprints.org manuscript 202608.1272 abstract and exact-certificate discussion | Verified paraphrase.  The nearby prose again limits relevance to method and complex-analytic setting. |
| 7 | `manuscript/references.bib`, supplied PDF metadata, official Annals record, Springer book record, arXiv records, and Preprints.org landing records | All printed records are corroborated.  No bibliography record is used to support a claim outside its inspected scope. |

Search templates were run on 2026-09-09 for each author/title/year/venue and,
where present, arXiv identifier or DOI.  Primary records consulted included
`https://arxiv.org/abs/2609.02884`,
`https://annals.math.princeton.edu/1987/125-3/p03`,
`https://people.math.harvard.edu/~ctm/home/text/papers/families/families.pdf`,
`https://arxiv.org/abs/2608.15558`, and the two Preprints.org manuscript
records.  Beardon metadata matches *Graduate Texts in Mathematics* 132,
Springer-Verlag, 1991; the exact dynamics statements were independently read
in the supplied Nayak--Phogat source at pp. 5--6.

For the two user-selected records,
`metadata_basis=user_designated_workbook`: the DOI and BibTeX fields preserved
in `literature/user_bibliography_check.md` control this workflow.  External
refresh unavailable in scope as a replacement authority; advisory arXiv and
publisher landing pages nevertheless corroborated the titles, authors, and
certificate descriptions.  Neither record is represented as a rational-
dynamics source.

The novelty prose is appropriately bounded: it compares only with the supplied
Nayak--Phogat preprint and expressly makes no broader priority claim.  No
unsupported strengthening of the accepted `n=18` statement was found.

## Keys, references, and dependency scope

Every key cited in `manuscript/main.tex` occurs in
`manuscript/references.bib`, every one is resolved in `main.aux`/`main.bbl`, and
all five references are legible in extracted and rendered PDF page 5.  There
are no undefined citations.

The complete authored/source dependency scope is exactly:

- `evidence/verify_orbit_threshold.py`
- `literature/user_bibliography_check.md`
- `manuscript/main.tex`
- `manuscript/references.bib`

The TeX source has no imported authored TeX, project-local package, figure, or
table dependency.  Generated `.aux`, `.bbl`, `.out`, and compiler files are not
authored sources; the real compiler log is separately bound by the build
audit.  Thus `publication.json` lists the complete dependency scope.

## Verdict

Accept.  All substantive citations and nearby claims are supported at their
stated scope, the designated workbook records are preserved under the user's
authority rule, the bibliography is resolved, and the publication dependency
scope is complete.
