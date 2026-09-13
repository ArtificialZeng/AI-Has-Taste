# Fresh citation audit

Release job: `bigMac-00014-p01-release-bc265e3b209b`  
Search date: 2026-09-08  
Method: advisory `citation-check-skill` v2, followed by manual checks of primary
records/text and the user-designated bibliography record.

## Dependency and resolution checks

`publication.json` lists the sole authored compilation dependency
`manuscript/manuscript.tex`. The recorder file confirms that the other local
inputs are generated auxiliary files; all remaining dependencies are system TeX
files. The TeX source contains five citation keys and five matching `\bibitem`
definitions. The clean final compiler log has no undefined citation/reference
diagnostic, and the extracted/rendered PDF displays all five numbered references.

## Fixed-claim verification results

- **C01 — verified (exact).** The primary arXiv v1 HTML identifies Yukun He and
  Jiaoyang Huang, gives the 4 September 2026 submission date, defines
  `M_{N,d}` as the loops-allowed model in Section 2, and states in Lemma 6.2
  that, conditional on no fixed points, `P(I+Q)` with
  `Q ~ Ewens_N(1/2)` is uniform on `M_{N,2}`. Its proof counts the
  `2^{c(A)}` ordered matching decompositions and cancels their weights.
  Source: <https://arxiv.org/html/2609.05297>, Section 2 and Lemma 6.2.
- **C02 — verified (exact/paraphrase).** The author-hosted primary preprint by
  Chi-Kwong Li, Julia Shih-Jung Lin, and Leiba Rodman has the displayed title
  and publication data. Theorem 3.1 and its proof (PDF pp. 4--5) write a
  line-sum-two matrix as a sum of permutation matrices, decompose the relative
  permutation into cycles, and show determinant zero for an even cycle and
  absolute determinant two per odd cycle. Source:
  <https://cklixx.people.wm.edu/llr.pdf>.
- **C03 — verified (exact/paraphrase).** Elsevier's publisher record gives
  David J. Houck and Michael E. Paul, *Linear Algebra and its Applications* 22
  (1978), 263--266, DOI `10.1016/0024-3795(78)90076-9`; its abstract says the
  paper explicitly constructs nonsingular constant-line-sum zero-one matrices
  for `0<k<n` except `(k,n)=(2,4)`. This supports the deliberately broad
  “earlier existence results” attribution. Source:
  <https://www.sciencedirect.com/science/article/pii/0024379578900769>.
- **C04 — verified (paraphrase).** The author-hosted 1990 Flajolet--Odlyzko
  paper has the stated title, authors, journal, pages, and DOI. Its introduction
  describes termwise transfer from dominant-singularity expansions and says a
  finite set of dominant singularities is handled by composite contours; its
  Darboux discussion gives the smooth-remainder/Fourier-coefficient principle.
  The manuscript uses it only as methodological context and proves its needed
  estimate directly. Source:
  <https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf>.
- **C05 — verified at the narrowed scope.** The bibliographic metadata is
  accepted from the user-designated workbook record documented in
  `literature/user_bibliography_check.md` (row 40, Zijian Zeng, 2026, DOI
  `10.2139/ssrn.7380519`). A fresh resolver/full-text refresh was unavailable
  in this bounded pass. The supplied record is authoritative for metadata. The
  title supports only the paper's concern with the distinct-cycle-length
  probability, so the earlier unsupported phrase attributing a parity
  cancellation at `z=-1` was removed before the final build. The remaining
  sentence makes no claim about its proof and expressly distinguishes the two
  events and probability laws.
- **C06 — verified as conservative scope.** The manuscript makes no priority
  claim; it describes only a bounded comparison. The closest sources inspected
  establish the representation, determinant classification, existence, and
  analytic method, while the paper proves its exact probability calculation
  self-containedly.
- **C07 — verified (exact).** Fresh executions of
  `evidence/verify_exact.py` and `evidence/verify_asymptotics.py` reproduce the
  stated finite ranges and identify floating-point output as diagnostic only.
- **C08 — verified.** Four records match current primary author/publisher/arXiv
  sources. The fifth follows the user-designated workbook metadata basis above.

## Verdict

Accept. Every citation key resolves, each nearby attribution is supported at
its final narrow scope, the dependency list is complete, and the novelty
language is bounded. `metadata_basis=user_designated_workbook`; external
refresh of the Zeng record was unavailable in scope, but its supplied metadata
is authoritative and no unsupported mathematical claim depends on it.

