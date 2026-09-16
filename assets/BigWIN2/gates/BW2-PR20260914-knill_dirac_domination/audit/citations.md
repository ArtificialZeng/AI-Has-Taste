# Verification Report

**Mode:** Two-pass primary-source verification, with local evidence for the
paper's own mathematics and computations. **Date:** 2026-09-14 UTC.
**Release job:** `primary-20260914-knill-dirac-domination-release-2935067edeff`.
**Document:** `manuscript/main.tex`; bibliography `manuscript/references.bib`.

| Metric | Count |
|---|---:|
| Frozen claims checked | 26 |
| Distinct ordinary body citation keys | 7 |
| Claims supported at the stated scope | 26 |
| Numerical errors / unsupported strengthening / decorative citations | 0 |
| Selected active-library records | 1 |
| Natural non-library references | 6 |

**Disposition: accept**, with the original-scan access limitation for Fan1949
explicitly recorded below. This is a release review, not external peer review
or a new mathematical acceptance. The original arbitrary-dimensional question
remains unresolved.

## Procedure and extraction integrity

The mathematical skill, release reference, release contract and both requested
citation skills were read completely in separate tool results. No subagents,
other model processes, background workers or interactive questions were used,
as the user explicitly prohibited delegation and requested non-interactive
verification.

Pass 1 read the complete manuscript and froze 26 claims with line intervals
and direct citation keys before source verification. Pass 2 checked those
claims against primary passages and the accepted frozen evidence. The initial
ledger is retained in `audit/citation-claim-ledger-initial.json`; the current
ledger has the same claim/citation pairs and is bound to the current manuscript
snapshot. A mistaken lemma number in the extraction was corrected to the
name-neutral phrase “the spectral lemma.” Only a proof-end glyph and redundant
bibliography grouping changed in the manuscript, in response to the selection
validator's deterministic TeX restrictions. No citation, mathematical sentence
or bibliography entry changed.

The active body parser, bibliography parser and final `.aux` agree on exactly
`Akritas2005, Fan1949, Knill2018, Knill2025, Knill2026, Meurer2017, Zeng2026`.
No key comes only from comments, `nocite`, a macro definition, an opaque command
argument, or a hidden conditional. The ledger's union is exactly this set.

## Citation-to-source checks

| Key | Identity and exact support | Decision |
|---|---|---|
| Knill2026 | Oliver Knill, *Remarks about Connection and Dirac matrices*, arXiv:2601.18071v2, 29 July 2026. The [primary HTML](https://arxiv.org/html/2601.18071v2) identifies the version and author. Sections 1.1 and 5.1 supply the matrix conventions and descending sums; Section 5.3, Conjecture 1 supplies the displayed comparison. | C02, C04 verified; no import of the source's other degree estimates or its separate inverse question. |
| Knill2025 | The [author's post](https://www.quantumcalculus.org/connection-and-dirac-matrix/) is dated 16 August 2025, with the 17 August spectral-estimate update proposing the additive-one bound and sharpness. The 21 August update still describes the missing proof. | C05 verified; the strengthening is correctly attributed as prior conjectural work. |
| Knill2018 | The [arXiv primary PDF](https://arxiv.org/pdf/1803.01464), v1, gives signed/unsigned conjugacy in Section 1.4 (printed p.3), the hydrogen identity in Theorem 1, Section 2.4 (printed p.4), and a spectral-radius bound in Corollary 1, Section 2.7 (printed pp.5–6). | C07–C09 verified. The body locators are correct. The writing dossier's earlier printed-page numbers were imprecise; this report uses the inspected pages. |
| Fan1949 | [PubMed's primary bibliographic record](https://pubmed.ncbi.nlm.nih.gov/16578320/) confirms Ky Fan, PNAS 35(11) (1949), 652–655, DOI 10.1073/pnas.35.11.652. Fan's own [1955 primary paper](https://msp.org/pjm/1955/5-6/pjm-v5-n6-p08-p.pdf), printed p.913, corollary proof and reference 1, explicitly recalls the minimum property for sums over orthonormal vectors as his 1949 Theorem 1. | C12 verified by primary-author corroboration and the complementary-projection calculation below. The 1949 scan was not inspected; no direct-scan claim is made. |
| Akritas2005 | The [publisher record](https://www.zurnalai.vu.lt/nonlinear-analysis/article/view/15110) and [primary PDF](https://www.zurnalai.vu.lt/nonlinear-analysis/article/download/15110/14122) agree on title, authors, 2005, volume 10(4), pp.297–304 and DOI. Section 1.1, pp.298–299, describes CF isolation for squarefree integral polynomials using rational interval transformations. | C22 verified. No performance or conjectural memory-bound assertion is imported. |
| Meurer2017 | The [published primary article preserved by CERN](https://s3.cern.ch/inspire-prod-files-c/cc049161dfd92d8831db1b9165c0bcf8) confirms the title, author list, 2 January 2017 date, PeerJ Computer Science 3:e103 and DOI. Its Polynomials subsection, p.9, discusses symbolic root isolation. The [official Poly.intervals documentation](https://docs.sympy.org/latest/modules/polys/reference.html#sympy.polys.polytools.Poly.intervals) identifies the VAS continued-fraction method and Akritas–Strzebonski reference. | C22 verified. The actual version 1.14.0 is supported by the frozen computation, not inferred from a 2017 article. “Et al.” is an intentional abbreviation. |
| Zeng2026 | The [version-1 primary full text](https://www.preprints.org/manuscript/202608.1067/v1) confirms Zijian Zeng, Houde Liu and Kurunathan Ratnavelu, title, 17 August 2026 posting and DOI 10.20944/preprints202608.1067.v1. Section 2, equations (8)–(18), derives algebraic spectral quantities and separates their ratio and the proposed constant by rational inequalities; Remark 1 says the decimal values are not used in the proof. | C24 verified. The comparison is methodological; no graph-complex theorem or entrywise-absolute-value result is attributed to this preprint. |

For C12, the inspected minimum property gives the maximum form by taking
complementary orthogonal projections:
`max_rank-k tr(PM) = tr(M) - min_rank-(n-k) tr(PM)`.
A scalar shift treats a general symmetric matrix if one starts from a positive
semidefinite formulation. Equality is attained by a spectral projection. The
manuscript also proves the formula directly. Thus the attribution and method
are supported without depending on an inaccessible proof. PNAS/PMC and Europe
PMC full-scan routes failed or returned a browser challenge. The search for
saved `literature/crossref-*.json` and `literature/crossref-*.md` found no files;
no saved authoritative response was ignored. This limitation is not a
mathematical conclusion.

Metadata were checked against the primary records, not just DOI existence.
No incorrect metadata or key mismatch requiring replacement was found. Attempts
to obtain arXiv and publisher BibTeX exports failed; no replacement export was
invented. `manuscript/references.bib` is unchanged, as are all citation keys.

## All frozen claims

Precise manuscript line intervals and substantive texts are in the JSON ledger.
The source locators and short inspected-passage anchors are in
`audit/source-locators.json`.

| IDs | Verification and scope |
|---|---|
| C01 | Abstract matches the accepted graph theorem and sharpness; higher-dimensional status remains explicitly unresolved. |
| C02 | Knill2026 Sections 1.1 and 5.1–5.3: signs, nonempty faces and descending sums agree. |
| C03 | Face reorientation gives diagonal orthogonal conjugacy of D; L is unaffected. |
| C04 | Knill2026 Conjecture 1 compares the separate sums, not positive semidefiniteness of L−D. |
| C05 | Knill2025 August 17 update; conjectural attribution preserved. |
| C06 | Theorem 1 is exactly the nonempty dimension-at-most-one statement accepted in `audit/math.md`. |
| C07 | Knill2018 Theorem 1 uses the unsigned Hodge square. |
| C08 | Knill2018 Section 1.4 gives bipartite conjugacy; no such equality is assumed for other graphs. |
| C09 | The inspected hydrogen and radius results do not themselves compare all signed partial sums; the paper supplies its own bridge. |
| C10 | Incidence/block entries match the frozen proof and simple-graph hypothesis. |
| C11 | SVD yields v positive and e negative eigenvalues; rank(C)≤e gives enough nonnegative Dirac positions for k≤v. |
| C12 | Primary-author attribution and maximum/minimum equivalence checked above; direct proof is included. |
| C13 | Coordinate projection gives degree majorization; H≤2Δ gives the ordered min–max bounds in the correct direction. |
| C14 | Expanding R and completing the degree squares reproduces the stated bridge inequality. |
| C15 | The odd-cycle test vector has Q-Rayleigh quotient at least 4, hence R(4)=√5−1>1. |
| C16 | The bipartite sign matrix conjugates H to Q; the elementary scalar bound gives k/2. |
| C17 | The nonnegative-vector Rayleigh argument proves the endpoint without mistaking entrywise order for Loewner order. |
| C18 | Kernel functions are componentwise constant; rank and trace give the tail gap (v+c)/2≥1. |
| C19 | The one-edge spectra and exact gap agree with the frozen symbolic witness; only its QED glyph changed. |
| C20 | `evidence/graph-proof-checks.json` and its generator contain 33,867 graphs, 453,098 sums, tolerance 10^-6, 32 structured cases and seven exact examples. These are explicitly original-screen diagnostics; the different referee tolerance is not substituted. |
| C21 | Census data record 7,579 nonempty complexes, agreement of two enumerations and 208 permutation orbits, with unused vertices admitted. |
| C22 | Primary software/method descriptions agree with the actual `Poly.intervals(eps=1/10^9)` call. |
| C23 | Independently summing the stored rational intervals reproduces all 3,151 bounds, 113,716 represented labeled sums and minimum 1583407980/1583407981. The referee's separate `count_roots` verification and the installed SymPy implementation use Sturm sign variations. No additive-one higher-dimensional certificate is claimed. |
| C24 | Zeng2026 Section 2 supports the rational algebraic sign-certification comparison; its decimals are expressly diagnostic. |
| C25 | Enumerated programs/data exist and contain the advertised evidence. The concluding scope stays partial. |
| C26 | Frozen version fields and the accepted separate referee artifacts support the assistance/version description; it does not claim formalization or external peer review. |

## Bibliography coverage and library selection

The active 49-entry first-sheet registry and manifest were parsed, the full title
list was screened, and the relevant spectral/certification abstracts were
compared. Row 2 is retained for its substantive rational spectral-certification
comparison. The minimum selection is one entry; other superficially related
library topics were not inserted. The selection's dynamic registry binding was
recomputed from the active files, and its date is the actual output of
`date -u +%F`. Its context is precisely the first citation-bearing sentence at
lines 293–295. The installed `validate_selection` passes with the exact job's
attempt 1 and launch UUID, without running the runner-owned hook.

The six non-library references have distinct uses: problem definitions/origin,
prior strengthening, closest established spectral relation, variational method,
root-isolation algorithm and software. There is no fixed-count quota, renamed
library citation masquerading as a non-library reference, or unused/decorative
entry. Elementary steps are proved in the article. The software reference and
independently checked implementation also cover the use of Sturm counting;
no historical priority assertion about that classical technique is made.

The full applicable academic search templates, plus the author's-post and
targeted graph-comparison queries, were run in this job; see
`audit/citation-search-log.json`. Search results served as discovery leads only.
No equivalent graph proof was found in the inspected primary results. This
bounded check does not establish exhaustive novelty or absolute priority.

## Dependency and rendered-reference audit

`publication.json` correctly lists the only two authored compile inputs. The
recorder's remaining local inputs are generated `.aux`, `.out` and `.bbl` files;
packages, fonts and `plain.bst` are system dependencies. No local figure, custom
style, imported section or additional database is omitted. Final compiler/BibTeX
logs and the mechanical key check are clean. All five rendered pages were
actually viewed, including the seven resolved references on page 5. Current
hashes are in `audit/manuscript-snapshot.json` and copied exactly into
`audit/citations.json`.
