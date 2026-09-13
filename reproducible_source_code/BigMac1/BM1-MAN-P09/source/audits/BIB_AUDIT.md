# Citation audit

Date: 2026-08-25

This table records claim-context and primary-source verification for every
reference used by `main.tex`.  A verified entry may be retained when its
content matches the official export even if harmless BibTeX formatting differs.

| Key | Citation context | Official title/source | Verification | BibTeX action | Key action | Uncertainty |
|---|---|---|---|---|---|---|
| `Crouzeix_2003` | Related strip/sector operator estimates | M. Crouzeix and B. Delyon, *Some estimates for analytic functions of strip or sectorial operators*, *Archiv der Mathematik* 81(5) (2003), 559--566; [Springer](https://link.springer.com/article/10.1007/s00013-003-0569-7), DOI `10.1007/s00013-003-0569-7` | Authors, title, journal, volume, issue, pages, November 2003, DOI, and citation context all match Springer and the DOI export | Retain current semantically identical entry; `https` DOI URL and BibTeX `--` page range are deliberate harmless formatting differences from the export | Retain | None |
| `MR2223270` | Classical lens reduction and bounds | B. Beckermann and M. Crouzeix, *A lenticular version of a von Neumann inequality*, *Archiv der Mathematik* 86(4) (2006), 352--355; [Springer](https://link.springer.com/article/10.1007/s00013-005-1533-5), DOI `10.1007/s00013-005-1533-5` | Core metadata and the stated lens-reduction/bounds context match Springer, the DOI export, and the author manuscript | Retain the richer MathSciNet-style entry; no substantive mismatch | Retain stable MR key rather than DOI export key `Beckermann_2006` | MathSciNet-only reviewer/class fields were not re-exported from the current MathSciNet frontend; core publication data are certain |
| `MR2449098` | Uniform bounds for intersections of spherical disks | C. Badea, B. Beckermann and M. Crouzeix, *Intersections of several disks of the Riemann sphere as K-spectral sets*, *Communications on Pure and Applied Analysis* 8(1) (2009), 37--54; [journal](https://www.aimsciences.org/article/doi/10.3934/cpaa.2009.8.37), DOI `10.3934/cpaa.2009.8.37` | Authors, title, journal, year, volume, issue, pages, DOI, ISSNs, arXiv record, and the bound `K <= n+n(n-1)/sqrt(3)` match the primary sources | Retain current MathSciNet-style entry; HTTPS DOI URL, protected title capitalization, and BibTeX page range are preferable harmless formatting differences | Retain stable MR key rather than DOI export key `Badea_2009` | MathSciNet-only fields were not directly re-exported; no core-data uncertainty |
| `MR2047592` | Low-dimensional numerical-range constants and perspectives | M. Crouzeix, *Bounds for Analytical Functions of Matrices*, *Integral Equations and Operator Theory* 48(4) (2004), 461--477; [Springer](https://link.springer.com/article/10.1007/s00020-002-1188-6), DOI `10.1007/s00020-002-1188-6` | Core metadata and the context about numerical-range bounds and explicit two-dimensional cases match the Springer article, official export, and DOI/Crossref | Retain current richer MathSciNet-style entry; missing optional month/day/abstract fields are immaterial | Retain stable MR key rather than Springer export key `Crouzeix2004` | MathSciNet-only reviewer/classification fields were not independently re-exported; core publication data are certain |
| `Crouzeix_2016` | Later numerical-range constants and perspectives | M. Crouzeix, *Some Constants Related to Numerical Ranges*, *SIAM Journal on Matrix Analysis and Applications* 37(1) (2016), 420--442; [SIAM](https://epubs.siam.org/doi/10.1137/15M1020411), DOI `10.1137/15M1020411` | SIAM metadata, author PDF, Crossref export, and the context about constants/partial results/numerical perspectives agree | Retain the current Crossref-equivalent, LaTeX-safe entry; HTTPS DOI URL, escaped ampersand, ASCII page range, and DOI capitalization are benign normalizations | Retain; this is also the Crossref export key | SIAM's direct BibTeX download returned 403, but three authoritative records agree |

## Mechanical consistency

Before any build, the skill checker reported 5 cited keys, 5 BibTeX keys, no
missing bibliography file, no cited key missing from the bibliography, and no
unused BibTeX entry.

## Revised-package incremental check

The v2 mathematical revision changes no citation command and no BibTeX entry.
After rebuilding `main.bbl`, the checker again reports 5 cited keys, 5 BibTeX
keys, no missing or unused entry, and exact agreement between `main.tex` and
`main.aux`.  The converged `main.log` and `main.blg` contain no undefined
citation, missing database entry, repeated entry, LaTeX error, fatal error,
undefined control sequence, or runaway argument.  No citation key or BibTeX
record was changed for v2.

## v3 incremental check

The v3 theorem enlargement changes no citation command and no BibTeX entry.
The v2 and v3 `references.bib` files have the identical SHA-256 digest
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`.
The skill checker reports 5 cited keys, 5 BibTeX keys, no missing bibliography
file, no cited key missing from the bibliography, and no unused entry.  Thus
the five primary-source conclusions in the table remain the applicable
per-reference audit; no key or record was changed for v3.

## v4 incremental check

The v4 endpoint enlargements change no citation command and no BibTeX entry.
The v3 and v4 `references.bib` files have the identical SHA-256 digest
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`,
and their extracted citation-command sets are identical.  The skill checker
reports 5 cited keys, 5 BibTeX keys, no missing bibliography file, no cited
key missing from the bibliography, no unused entry, and exact agreement with
the converged `main.aux`.  The final `main.log` and `main.blg` contain no
undefined citation, missing database entry, repeated entry, LaTeX error,
fatal error, undefined control sequence, runaway argument, overfull box, or
underfull box.  Thus the five primary-source conclusions in the table remain
the applicable per-reference audit; no key or record was changed for v4.

## v6 incremental check

The v6 endpoint enlargements change no citation command, contextual claim
about the cited literature, or BibTeX entry.  The frozen v5 and v6
`references.bib` files have the identical SHA-256 digest
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`,
and their extracted citation-key sets are identical.  Consequently the five
primary-source checks in the table remain applicable; a new web lookup would
not test any changed citation surface.  The skill checker reports 5 cited
keys, 5 BibTeX keys, no missing bibliography file, no cited key missing from
the bibliography, no unused entry, and exact agreement with the converged
`main.aux`.  The final `main.log` and `main.blg` contain no undefined
citation, missing database entry, repeated entry, LaTeX/package warning,
fatal error, undefined control sequence, runaway argument, overfull box, or
underfull box.  No citation key or BibTeX record was changed for v6.

## v7 incremental check

The v7 endpoint enlargements change no citation command, contextual claim
about the cited literature, or BibTeX entry.  The frozen v6 and v7
`references.bib` files have the identical SHA-256 digest
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`,
and their extracted citation-key sets are identical.  The five
primary-source checks in the table therefore remain the applicable
per-reference audit.  The mathematics-workflow auditor and the bibliography
skill checker both report five cited keys, five BibTeX keys, no missing
bibliography file or entry, no unused entry, and exact agreement with the
converged `main.aux`.  The converged `main.log` and `main.blg` contain no
undefined citation or reference, missing database entry, repeated entry,
LaTeX/package warning, fatal error, undefined control sequence, runaway
argument, overfull box, or underfull box.  No citation key or BibTeX record
was changed for v7.

## v12 incremental check

The v12 centered-breakpoint and affine-omega-tilt additions change no
citation command, contextual claim about the cited literature, BibTeX key, or
BibTeX record.  The frozen v11 and present v12 `references.bib` files have the
identical SHA-256 digest
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`;
their citation-command sets are the same five keys audited above.  The skill
checker reports 5 cited keys, 5 BibTeX entries, 5 auxiliary keys, no missing
bibliography file or entry, no unused or duplicate entry, and exact agreement
with `main.aux`.  The first converged v12 build has no undefined citation or
reference, missing/repeated BibTeX entry, or LaTeX/BibTeX/box warning.  The
five primary-source checks in the table therefore remain applicable.

No citation subagents were started: the project hard limit leaves only two
local task slots, and the citation set, metadata, claim context, bibliography,
and generated `main.bbl` are unchanged.  This incremental decision avoids
spending a proof slot on five already official-record-verified entries; it is
not a relaxation of the 5/5 official audit above.

## v13 independent citation recheck

The inward-`Z` theorem changes no literature claim, citation command, BibTeX
key, or BibTeX record.  A fresh independent recheck verified all five cited
records and all five citation contexts against authoritative pages: Springer
for `MR2223270`, `Crouzeix_2003`, and `MR2047592`; AIMS for `MR2449098`; and
SIAM for `Crouzeix_2016`.  The result is **5/5 records verified, 5/5 contexts
supported, 0 replacements, 0 key changes, and 0 bibliographic blockers**.
The AIMS raw BibTeX for `MR2449098` is malformed, so the already verified
current entry is intentionally retained.  SIAM's BibTeX endpoint for
`Crouzeix_2016` returned HTTP 403, but its official article page and Crossref
metadata agree with the retained entry.  The final v13 build must still rerun
the exact key-set comparison and LaTeX/BibTeX warning scan.
