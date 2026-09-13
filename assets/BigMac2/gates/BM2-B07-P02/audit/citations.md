# Fresh citation and dependency audit

Audit date: 2026-09-08 (Asia/Shanghai)  
Method: citation-check-skill advisory two-pass review plus inspection of the
primary arXiv and publisher records  
Release job: `bigMac-00007-p02-release-e3e9934bb4ec`

## Pass 1 — frozen claim extraction

The following citation-dependent factual claims were extracted from the full
manuscript before verification.  Self-contained definitions, proof steps, and
the accepted theorem were not treated as literature attributions.

1. **C01 (attribution; page 1, Setup):** the displayed random-walk and
   uniform-demand Goemans--Linial normalization is the normalization used by
   Stamoulis.
2. **C02 (attribution; page 2, after Theorem 1):** Stamoulis Proposition 6.1
   proves exactness for ordinary cycles, which yields the two coordinate faces
   here after the stated relabeling.
3. **C03 (attribution and scope comparison; page 2):** Stamoulis Theorems 1.1
   and 4.6 assume a minimizing character whose image has size at most four, so
   that cited hypothesis does not cover the interior two-weight problem on
   `Z/5Z`.
4. **C04 (attribution; page 4, Exact finite verification):** Zeng et al. is an
   example, in a different finite extremal problem, of exact finite
   certificates and symmetry-reduced exhaustive enumeration; it makes no claim
   about the Goemans--Linial theorem here.
5. **C05 (bibliographic existence/metadata; reference [1]):** Georgios
   Stamoulis, title, year 2026, arXiv:2609.05368v1, primary class math.CO.
6. **C06 (bibliographic existence/metadata; reference [2]):** Zijian Zeng,
   Houde Liu, Kuru Ratnavelu, and Seng Huat Ong, title, venue/year, and DOI
   `10.20944/preprints202608.1658.v1`.

This fixed list was then used for Pass 2; no claims were added during
verification.

## Pass 2 — claim-to-source verification

| ID | Finding | Evidence and exact scope |
|---|---|---|
| C01 | Verified (paraphrase) | arXiv:2609.05368v1, Sections 2.3--2.5 defines the normalized Cayley random walk, oriented step average, uniform all-pairs denominator, and GL metric ratio used in the manuscript. |
| C02 | Verified (exact source statement plus local relabeling) | Stamoulis Proposition 6.1 states `SDP_GL(C_n)=psi(C_n)` with the exact odd/even values.  At `n=5` it gives `5/6`; the manuscript itself explains the multiplication-by-two relabeling between its two one-weight faces. |
| C03 | Verified (exact source statement) | Theorems 1.1 and 4.6 explicitly require a character realizing the bottom eigenvalue with image size `q<=4`.  The fact that a nontrivial character of `Z/5Z` has image size five is an elementary local group calculation.  The manuscript correctly says only that this cited hypothesis does not itself settle the interior cone. |
| C04 | Verified (paraphrase) | The Preprints.org abstract and article describe exact distance-layer certificates, an exhaustive symmetry-reduced enumeration of 15,056 maximal feasible sets, and exact integer-predicate clique computations.  They concern ternary Borsuk and kissing-code finite libraries, not Goemans--Linial SDP. |
| C05 | Verified (exact metadata) | The primary arXiv record at `https://arxiv.org/abs/2609.05368v1` gives author Georgios Stamoulis, the manuscript title, 4 September 2026, version 1, and class math.CO.  The initially stale math.OC field was repaired before the final build. |
| C06 | Verified (exact metadata and support) | `literature/user_bibliography_check.md` records the user-designated workbook entry and its BibTeX.  `metadata_basis=user_designated_workbook`; the bounded external refresh at `https://www.preprints.org/manuscript/202608.1658` was accessible and concordant on 2026-09-08.  The nearby prose is limited to what the publisher abstract supports. |

The comparison language is deliberately bounded to the cited arXiv version
and expressly disclaims priority.  It does not turn an absence-of-match search
into a novelty theorem.  No external citation is used as a premise of the
self-contained mathematical proof.

## Citation-key and rendered-reference check

The TeX source contains exactly the two keys
`stamoulis2026integrality` and `zeng2026finitecertificates`.  Both occur in
`manuscript/references.bib`, `main.bcf`, `main.bbl`, and the final extracted
reference list.  Biber reports two found citekeys.  There are no undefined or
contradicted citations and no unnecessary citation whose removal is required.

## Publication dependency scope

`publication.json` lists, in sorted order:

- `evidence/check_finite.py`
- `manuscript/main.tex`
- `manuscript/references.bib`

The recorder and Biber inputs show no additional authored TeX, bibliography,
figure, or local style dependency.  Generated auxiliary files are not source
dependencies.  The exact checker is included because the manuscript presents
it as supplementary corroboration; its current digest is bound in the
manuscript snapshot.  The dependency scope is complete.

**Verdict: accept.**
