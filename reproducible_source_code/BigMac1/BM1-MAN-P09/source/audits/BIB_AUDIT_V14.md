# v14 bibliography audit

Date: 2026-08-25. Verdict: **PASS -- 5/5 cited records verified, no key or
BibTeX change, no blocker.**

An independent read-only auditor extracted every citation from `main.tex`,
checked its local BibTeX record and citation context, and compared the record
with a primary publisher page and DOI metadata.  The builder separately ran
the mechanical key checker after the converged build: cited keys `5`, BibTeX
keys `5`, AUX bibitems `5`, missing files `0`, cited keys missing from BibTeX
`0`, unused BibTeX keys `0`, cited keys missing from AUX `0`, and AUX keys not
cited `0`.

| key | verified publication | official record | action |
|---|---|---|---|
| `MR2223270` | B. Beckermann and M. Crouzeix, *A lenticular version of a von Neumann inequality*, Archiv der Mathematik 86(4), 352--355 (2006), DOI `10.1007/s00013-005-1533-5` | <https://link.springer.com/article/10.1007/s00013-005-1533-5> | Keep MR key and current richer record. |
| `Crouzeix_2003` | M. Crouzeix and B. Delyon, *Some estimates for analytic functions of strip or sectorial operators*, Archiv der Mathematik 81(5), 559--566 (2003), DOI `10.1007/s00013-003-0569-7` | <https://link.springer.com/article/10.1007/s00013-003-0569-7> | Keep current corrected title; the publisher export concatenates two title words. |
| `MR2449098` | C. Badea, B. Beckermann, and M. Crouzeix, *Intersections of several disks of the Riemann sphere as K-spectral sets*, CPAA 8(1), 37--54 (2009), DOI `10.3934/cpaa.2009.8.37` | <https://www.aimsciences.org/article/doi/10.3934/cpaa.2009.8.37> | Keep MR key and current richer record. |
| `MR2047592` | M. Crouzeix, *Bounds for analytical functions of matrices*, IEOT 48(4), 461--477 (2004), DOI `10.1007/s00020-002-1188-6` | <https://link.springer.com/article/10.1007/s00020-002-1188-6> | Keep current record. |
| `Crouzeix_2016` | M. Crouzeix, *Some Constants Related to Numerical Ranges*, SIAM J. Matrix Anal. Appl. 37(1), 420--442 (2016), DOI `10.1137/15M1020411` | <https://epubs.siam.org/doi/10.1137/15M1020411> | Keep current record. |

The official abstracts support the manuscript contexts: lens-domain bounds,
strip/sector operator estimates, intersections of spherical disks as
spectral sets, analytic matrix-function estimates controlled by numerical
range, and numerical-range constants and perspectives.  The AIMS export
payload and SIAM BibTeX download endpoint were not directly retrievable, but
the official article pages and DOI registration metadata agree on every core
field.  This creates no unresolved bibliographic uncertainty.

No file was changed as a consequence of record verification.  The converged
`latexmk` run and the final `main.log`/`main.blg` scan contain no undefined
citation, missing database entry, duplicate entry, BibTeX warning, LaTeX
error, or fatal stop.
