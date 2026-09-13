# Fresh citation audit

Audit date: 2026-09-09. Release job:
`bigMac-00022-p01-release-c14619b2439d`. I applied the available
`citation-check-skill` as an advisory two-pass search audit, supplemented by
the local primary-source PDF and the user-designated workbook record summarized
in `literature/user_bibliography_check.md`.

## Pass 1: fixed claim extraction

The following externally checkable or attribution-bearing claims were fixed
before verification.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Performance-estimation problems turn finite-horizon worst-case questions for first-order methods into semidefinite programs. | Existence/attribution | page 1, section 1 |
| C02 | Du proves the queried-gradient result from horizon seven onward, treats horizon one separately, and leaves the five branches `2 <= N <= 6` analytically uncharacterized. | Attribution/quantified existence | page 1, section 1 |
| C03 | The Kim--Fessler bound used in this context is a relaxed bound and is not, by itself, the exact queried-gradient problem. | Attribution/comparative | page 1, section 1 |
| C04 | The twelve displayed inequalities are the standard exact smooth-convex interpolation conditions. | Attribution/existence | page 2, equation (2) |
| C05 | The fixed convex-lens paper uses exact rational/matrix certificates for sharply delimited constants, only as a methodological comparison. | Attribution | page 1, section 1 |
| C06 | The rank-two self-Chollet paper uses exact sum-of-squares and positive-semidefinite Gram certificates, only as a methodological comparison. | Attribution | page 1, section 1 |
| C07 | The stated horizon-two constant and its decimal expansion are established by the displayed exact certificate and equality instance. | Statistic/existence | abstract, Theorem 1, sections 2--3 |
| C08 | The accompanying exact-arithmetic program performs the checks described in the reproducibility statement. | Existence | page 5 |

No additional claims were introduced during verification.

## Pass 2: verification

| ID | Status | Evidence and scope check |
|---|---|---|
| C01 | Verified (paraphrase) | Drori--Teboulle's official Springer record and arXiv:1206.3209 describe PEP and a convex semidefinite relaxation; Taylor--Hendrickx--Glineur, arXiv:1502.05666, gives the finite dimension-independent semidefinite formulation. |
| C02 | Verified (exact) | The local 18-page PDF `2608.26719v1.pdf`, SHA-256 `34ce307c547848e4f6c36604190195e67e7f59c3db20d7e842093ad313eef2fd`, states this scope on page 3, proves Theorem 7.2 for `N >= 7` on page 12, gives Proposition 8.1 for `N=1` on pages 13--14, and repeatedly records `2 <= N <= 6` as open. The arXiv record 2608.26719 matches author, title, date, and abstract. |
| C03 | Verified (paraphrase) | Du's Theorem 2.1 attributes the dimension-free analytical upper bound to Kim--Fessler and later explicitly calls their SDP an outer relaxation. The official SIAM record for DOI `10.1137/17M112124X` matches the manuscript metadata. The manuscript carefully denies the unsupported implication from relaxed to exact. |
| C04 | Verified (exact) | Taylor--Hendrickx--Glineur's smooth-convex interpolation corollary gives `f_i-f_j-<g_j,x_i-x_j> >= ||g_i-g_j||^2/(2L)` for every ordered pair. With `L=1`, this is exactly equation (2). The arXiv and journal metadata match the bibliography; journal DOI is `10.1007/s10107-016-1009-3`. |
| C05 | Verified (paraphrase) | User-designated workbook row `数学主表!A13:F13` supplies the authoritative DOI/metadata. The official Preprints.org version-1 page `202608.1272` matched title and author and displays exact rational matrix/certificate claims with explicitly delimited scope. The nearby prose does not use it as a premise. |
| C06 | Verified (paraphrase) | User-designated workbook row `数学主表!A23:F23` supplies the authoritative DOI/metadata. The official Preprints.org version-1 page `202608.1346` matched title and authors and explicitly states exact sum-of-squares and positive-semidefinite Gram certificates. The nearby prose does not use it as a premise. |
| C07 | Verified against accepted mathematical evidence | `audit/math.md` accepts the exact full-scope theorem. The displayed certificate, witness, and scaling match that accepted scope. No external paper is cited as proving this new result. |
| C08 | Verified (exact) | A fresh run of `python3 evidence/verify_exact_dual.py` exited zero and reported twelve interpolation inequalities, thirteen positive multipliers, exact objective `1/(a+2)^2=c_2^2`, three exact positive Sylvester minors, PSD rank three, and the required zero coefficients. |

## Bibliography and dependency audit

The extracted PDF renders six numbered references. Every citation key in
`manuscript/main.tex` has one matching `\bibitem` and `\bibcite`; there are no
undefined or duplicate keys. Author, title, year, venue/version, DOI/arXiv
identifier, and nearby support were checked for all six records. The two
workbook-designated records use
`metadata_basis=user_designated_workbook`; external refresh was available and
matched the supplied fields. The Du source was checked in original local text,
not merely by DOI or abstract.

`publication.json` lists the complete authored dependency scope:
`manuscript/main.tex` and `manuscript/references.bib`. The recorder file shows
no other project-authored TeX, style, figure, or bibliography input. The
rendered references are resolved and legible. No citation is contradicted,
unnecessary to the stated comparison, or used to support a stronger claim than
the inspected material permits. Bounded novelty language is confined to the
explicit comparison with Du's recorded open horizon-two branch.

Primary pages consulted on 2026-09-09 included:

- `https://doi.org/10.1007/s10107-013-0653-0`
- `https://arxiv.org/abs/1502.05666`
- `https://doi.org/10.1137/17M112124X`
- `https://arxiv.org/abs/2608.26719`
- `https://www.preprints.org/manuscript/202608.1272`
- `https://www.preprints.org/manuscript/202608.1346`

Verdict: **accept**. There are no remaining citation-access limitations and no
unsupported prose requiring a manuscript change.
