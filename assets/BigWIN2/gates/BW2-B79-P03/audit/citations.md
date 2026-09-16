# Citation and bibliography audit

## Verdict and binding

**Accept.** This search-mode audit belongs to release job
`win-00079-p03-release-a669e55d8fa7`, citation attempt 1, launch
`896a57c3-3ff1-49a8-a396-ac4c61936d90`. It covers the canonical
`manuscript/main.tex` and `manuscript/references.bib` at manuscript digest
`da0af80f46244a58e7f156ed985226969c50873f465c1898f1590ed387903cea`
and PDF digest
`fa326ed2d297a3d497d3b1b01cd16d611b0104eda8adba40d916b4ea8bfc5dca`.
The accepted evidence snapshot is
`71cb4c86fc33451424485a0b8d9495aa4e425cf029d346856d6018b998017a51`.

The audit date is 2026-09-10 UTC. The user prohibited sub-agents for this
bounded job, so the otherwise independent verification pass was performed
sequentially by the release worker after freezing the extraction. No claim was
accepted from a DOI match or registry metadata alone.

## Two-stage method

In pass 1, every ordinary body-flow `\cite` command was extracted from the
active TeX, associated with the smallest substantive claim it supports, and
frozen as nine uniquely identified claim/citation pairs in
`audit/citation-claim-ledger.json`. A mechanical comparison confirms that the
union of the ledger's keys is exactly the eight active body-flow citation keys;
there are no keys supplied only by comments, `\nocite`, inert macros, verbatim
text, or hidden conditionals.

In pass 2, each frozen claim was checked against the cited primary paper's
actual abstract, theorem, remark, or proof passage. The saved Dean--Goldsmith
and Li PDFs were independently parsed and their hashes checked against the
accepted evidence snapshot. Official publisher, author, arXiv, institutional,
or Preprints.org records were used for the other sources. The precise locators,
URLs, support decisions, and evidence hashes are recorded in
`audit/citation-verification.json`.

## Claim-to-source results

| ID | Nearby claim and exact primary locator | Result |
|---|---|---|
| C01 | Dean--Goldsmith, abstract and introduction: massive-MIMO physical-layer cryptography and its lattice-problem reduction. | Verified |
| C02 | Regev, abstract and reduction framework; Dean--Goldsmith PDF p. 14 independently says Lemma 7 replaces the LWE oracle in Regev's framework. | Verified in the immediate two-sentence context |
| C03 | Micciancio--Regev, publisher abstract and Gaussian-measure preliminaries: worst-case/average-case reductions based on Gaussian measures and the relevant lattice parameter. | Verified |
| C04 | Official abstracts for arXiv:1507.08015 and arXiv:2001.02632: respectively a zero-forcing attack and two attacks on versions of the Dean--Goldsmith construction. | Verified |
| C05 | Li, PDF p. 10, Proposition 5.1: exact non-membership for an out-of-constellation coefficient or nonzero BDD offset. | Verified |
| C06 | Li, PDF p. 12, Remark 5.3: nonidentity need not give non-negligible statistical distance, which can depend on the restricted target. | Verified |
| C07 | Zeng--Liu--Ratnavelu, Preprints.org version 1, Section 1, Theorems 1--3: an exact matrix counterexample followed by surviving sharp parameter regimes. The manuscript expressly marks this as a different setting. | Verified |
| C08 | Dean--Goldsmith, PDF p. 13, Claim 2: `eta_epsilon(L) <= sqrt(n)/lambda_1(L*)` at `epsilon=2^{-n}`; the displayed `Z^n` bound follows by substitution. | Verified |
| C09 | Hoeffding, Theorem 2, printed p. 16: with range length `2T^2`, the two-sided bounded-summand inequality yields the exact first bound in equation (17). | Verified |

There are no failed, misleading, or unsupported citation-dependent claims. The
manuscript does not claim a general MIMO attack, a repair of the original
reduction, or priority beyond its bounded source comparison.

## Bibliographic-record audit

All eight bibliography entries resolve to primary records and all eight are
cited in ordinary body flow. Author, title, year/version, venue, pagination,
and identifier fields were compared with those records. Three metadata defects
were repaired without changing citation keys: Regev's JACM pagination is now
the article-number form `34:1--34:40`; the official arXiv DOI was added to
Sakzad--Steinfeld 2020; and the IEEE workshop DOI was added to
Steinfeld--Sakzad 2015. No entry is duplicated or unused, and BibTeX reports no
missing entry or repeated key.

| Key | Why it is retained |
|---|---|
| `DeanGoldsmith2017` | Original construction, reduction claim, smoothing bound, and sample constructor. |
| `Regev2009` | Natural primary source for the lattice/LWE reduction framework. |
| `MicciancioRegev2007` | Natural primary source for Gaussian-measure and smoothing theory. |
| `SteinfeldSakzad2015` | Primary source for the earlier related attack. |
| `SakzadSteinfeld2020` | Primary source for the later attacks/comments. |
| `Li2026` | Closest proof-level prior analysis and the exact Proposition 5.1/Remark 5.3 comparison. |
| `Hoeffding1963` | Primary method source for the nontrivial concentration inequality. |
| `ZengLiuRatnavelu2026` | Active user-library paper supporting the narrow, explicitly different-setting scope comparison. |

## Coverage and user-library gate

The active first-sheet registry contains 49 entries. Registry row 2 is the only
entry with a natural claim-level use here; its official Preprints.org version
supports the cited sentence exactly. Selecting another unrelated entry would be
padding. The attempt-bound details and literal compact citation context are in
`audit/user-bibliography-selection.json`, and the hook-compatible selection
validator passes.

This minimum library selection is not used as a bibliography ceiling. Seven
natural non-library primary or method sources occur in ordinary body flow and
cover the problem origin, closest prior analysis, foundational framework,
smoothing theory, related attacks, and concentration method. Thus the dependency
scope is complete without being padded.

## Final citation integrity

The active TeX contains eight distinct citation keys, the BibTeX database has
the same eight distinct keys, and the final `.aux` resolves all eight. The build
log has no undefined citation or reference diagnostic. The bibliography visible
in the rendered PDF was also checked during the page-by-page visual audit.
