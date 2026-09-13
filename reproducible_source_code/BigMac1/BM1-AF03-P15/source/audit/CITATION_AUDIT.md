# Citation audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Mode: source-verification with web search and archived primary PDFs  
Manuscript: `paper/main.tex`

## Pass 1: frozen citation-dependent claims

The citation surface was extracted before final source checking.  The paper
uses only two bibliography keys and makes the following source-dependent
claims.

| ID | Manuscript claim | Required source location |
|---|---|---|
| P-C01 | Gaetz--Gao conjecture that `Abs(D_n)` has a normalized flow with unit vertex weights | Gaetz--Gao, Conjecture 1.3(a), journal p. 792 |
| P-C02 | Gaetz--Gao reported computer verification through `n=8` | Gaetz--Gao, final paragraph of Section 5, journal p. 799 |
| P-C03 | Their normalized-flow equations specialize to row sums `1/|P_r|` and column sums `1/|P_{r+1}|` for unit vertex weights | Gaetz--Gao, Section 2.4, journal p. 794 |
| P-C04 | Unit-weight normalized flow passes between a poset and an automorphism-orbit quotient with orbit-size weights | Gaetz--Gao, Proposition 3.6, journal p. 797 |
| P-C05 | Carter's root-reflection length equals the number of eigenvalues unequal to 1 | Carter, Section 2, Lemma 2, journal p. 3 |
| P-C06 | The cited Carter reflection set specializes to the 72 type-`D_9` reflections used in the formal statement | Inference from Carter's root-reflection definition and the `D_9` root system `±e_i±e_j`; checked explicitly, not attributed verbatim |
| P-C07 | The original paper/source records provide no code or exact `n≤8` certificate | Inspection of the journal record and complete arXiv v2 source archive; scoped to those records |
| P-C08 | The finite novelty wording is limited to two dated public searches finding no later resolution | `literature/search_log.md`, Sections 1--8; negative result expressly not universal |

The numerical and theorem claims specific to `D_9` are not literature
claims.  They are supported by the primary exact certificate and the
independent no-import verifier recorded in `audit/REFEREE_REPORT.md`.

## Pass 2: source verification

### `ALCO_2020__3_3_791_0`

- Official record: <https://alco.centre-mersenne.org/articles/10.5802/alco.114/>
- DOI: <https://doi.org/10.5802/alco.114>
- Version of record: `literature/sources/gaetz-gao-2020.pdf`, SHA-256
  `c0791aee56aa2ee75f1624075c89c6944abae3fe5ac26623d7f6bf8233fff42f`.
- Latest arXiv record checked separately: `1903.02033v2`, updated
  2020-10-31.
- P-C01: **verified** at Conjecture 1.3(a), journal p. 792.
- P-C02: **verified** at the final paragraph of Section 5, journal p. 799.
- P-C03: **verified** from the edge equations and poset definition in
  Section 2.4, journal p. 794.
- P-C04: **verified** at Proposition 3.6 and its biregularity proof, journal
  p. 797.
- P-C07: **verified within the stated repository boundary**.  The arXiv v2
  source archive contains only `main.tex` and `main.bbl`; the inspected
  journal record links PDF, TeX, and citation exports but no supplement,
  program, or certificate.

The BibTeX entry in `paper/references.bib` is the official publisher export,
including the stable DOI, volume 3, issue 3, pages 791--800, year 2020, and
MR 4113607.  It was not reconstructed from memory.

### `CM_1972__25_1_1_0`

- Official record: <https://www.numdam.org/item/CM_1972__25_1_1_0/>
- Primary PDF: `literature/sources/carter-1972.pdf`, SHA-256
  `9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5`.
- Bibliographic existence and metadata: **verified** -- R. W. Carter,
  *Conjugacy classes in the Weyl group*, *Compositio Mathematica* 25
  (1972), no. 1, 1--59.
- P-C05: **verified exactly**.  Journal p. 3 defines `l(w)` as the minimum
  number of root reflections in a product and Lemma 2 identifies it with the
  number of eigenvalues unequal to 1.
- P-C06: **verified as an applicability inference**.  The type-`D_9` roots
  are `±e_i±e_j`; roots differing by a global sign define the same
  reflection, leaving exactly the two signed transpositions for each
  `i<j`, hence `2*binom(9,2)=72`.  A positive signed cycle has one fixed
  dimension and a negative signed cycle has none, so Carter gives
  `ell_T(w)=9-ell(lambda)`.

The BibTeX entry is the official NUMDAM export, including volume 25, issue 1,
pages 1--59, year 1972, MR 318337, and Zbl 0254.17005.

### Novelty wording

P-C08 is **supported only in its bounded form**.  Gate 1 and the independently
rephrased post-result pass searched the DOI/title, reverse citations,
arXiv, current author records, GitHub, Zenodo, and accessible OSF endpoints.
No public `D_9`, `n≥9`, or general type-`D` normalized-flow solution was
located.  MathSciNet authentication, Google Scholar timeout, Semantic
Scholar rate limiting, Figshare HTTP 403, and other access failures are
listed in `literature/search_log.md`, Section 8.6, and contribute no negative
evidence.  The manuscript therefore does not claim universal priority or
nonexistence of private/unindexed work.

## Citation-to-claim matrix

| Claim | Citation key | Exact locator | Result |
|---|---|---|---|
| P-C01 | `ALCO_2020__3_3_791_0` | Conj. 1.3(a), p. 792 | PASS |
| P-C02 | `ALCO_2020__3_3_791_0` | Section 5 final paragraph, p. 799 | PASS |
| P-C03 | `ALCO_2020__3_3_791_0` | Section 2.4, p. 794 | PASS |
| P-C04 | `ALCO_2020__3_3_791_0` | Proposition 3.6, p. 797 | PASS |
| P-C05 | `CM_1972__25_1_1_0` | Lemma 2, p. 3 | PASS |
| P-C06 | `CM_1972__25_1_1_0` + explicit `D_9` root calculation | p. 3 + manuscript proof | PASS |
| P-C07 | publisher page + complete arXiv v2 source archive | artifact enumeration | PASS (scoped) |
| P-C08 | two dated search logs | Sections 1--8 | PASS (bounded) |

No citation is missing, mismatched, or asked to support a stronger statement
than its source.  No citation-dependent claim relies on a search-result
snippet or inaccessible secondary source.

## Audit conclusion

**PASS.**  Both bibliography entries exist, their official metadata match the
manuscript, every citation points to the claimed location, and the only
negative-search claim retains explicit scope limitations.  Citation keys and
the generated bibliography are checked again during the clean LaTeX build.
